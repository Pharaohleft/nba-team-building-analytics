import gradio as gr
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sentence_transformers import SentenceTransformer
import faiss

# Load fallback CSV
df = pd.read_csv("nba_fallback.csv")

# Mock height and position until real data
df['HEIGHT'] = 80
df['POS'] = df['PLAYER_NAME'].apply(lambda x: 'F' if 'F' in x else 'G')

# Normalize stats for similarity comparisons
scaler = StandardScaler()
numerical_cols = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'AGE', 'GP']
X = scaler.fit_transform(df[numerical_cols].fillna(0))

# Build FAISS index for player similarity
index = faiss.IndexFlatL2(X.shape[1])
index.add(X)

# Embed player bios for sentence transformer demo
player_texts = df['PLAYER_NAME'] + " is " + df['AGE'].astype(str) + " years old and plays for " + df['TEAM_ABBREVIATION']
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(player_texts, convert_to_numpy=True, show_progress_bar=False)

# FAISS index for bios
bio_index = faiss.IndexFlatL2(embeddings.shape[1])
bio_index.add(embeddings)

def evaluate_team(team_abbr):
    team = df[df['TEAM_ABBREVIATION'] == team_abbr]
    if team.empty:
        return "Team not found."
    report = [f"# Team: {team_abbr}\n"]

    # Roster age check
    under_27 = team[team['AGE'] < 27]
    report.append(f"✅ Players under 27: {len(under_27)}")

    # 7-footers
    tall = team[team['HEIGHT'] >= 84]
    report.append(f"✅ 7-Footers: {len(tall)}")

    # Star creators
    top_pts = team.nlargest(3, 'PTS')['PLAYER_NAME'].tolist()
    top_ast = team.nlargest(3, 'AST')['PLAYER_NAME'].tolist()
    report.append(f"✅ Top Scorers: {', '.join(top_pts)}")
    report.append(f"✅ Top Creators: {', '.join(top_ast)}")

    return "\n".join(report)

def find_similar_players(player_name):
    if player_name not in df['PLAYER_NAME'].values:
        return "Player not found."
    idx = df[df['PLAYER_NAME'] == player_name].index[0]
    _, sim_ids = index.search(X[idx:idx+1], 6)
    sim_players = df.iloc[sim_ids[0][1:]]['PLAYER_NAME'].tolist()
    return f"Similar to {player_name}: " + ", ".join(sim_players)

def recommend_trade_targets(team_abbr):
    team = df[df['TEAM_ABBREVIATION'] == team_abbr]
    target = df[(df['AGE'] < 25) & (df['HEIGHT'] >= 81) & (df['TEAM_ABBREVIATION'] != team_abbr)]
    top_targets = target.nlargest(5, 'PTS')[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'AGE']]
    return top_targets

def team_stat_plot(stat):
    fig = px.box(df, x='TEAM_ABBREVIATION', y=stat, title=f"{stat} Distribution by Team")
    return fig

def similar_bio_players(query):
    q_emb = model.encode([query], convert_to_numpy=True)
    _, ids = bio_index.search(q_emb, 5)
    results = df.iloc[ids[0]]['PLAYER_NAME'].tolist()
    return "Closest players: " + ", ".join(results)

# Gradio Blocks UI
with gr.Blocks() as demo:
    gr.Markdown("# 🏀 NBA Role Search & Team Evaluator")

    with gr.Row():
        team_dropdown = gr.Dropdown(label="Select NBA Team", choices=sorted(df['TEAM_ABBREVIATION'].unique()))
        player_dropdown = gr.Dropdown(label="Select Player", choices=sorted(df['PLAYER_NAME'].unique()))

    with gr.Row():
        stat_dropdown = gr.Dropdown(label="Choose Stat", choices=['PTS', 'REB', 'AST', 'STL', 'BLK', 'AGE'])

    with gr.Row():
        query_input = gr.Textbox(label="Describe player you're looking for", placeholder="e.g. tall scorer under 25")

    with gr.Row():
        team_eval_btn = gr.Button("Evaluate Team")
        sim_btn = gr.Button("Find Similar Players")
        trade_btn = gr.Button("Trade Targets")
        stat_btn = gr.Button("Stat Distribution")
        bio_btn = gr.Button("Bio Similarity Search")

    with gr.Row():
        output_markdown = gr.Markdown()
        output_table = gr.Dataframe()
        output_plot = gr.Plot()

    team_eval_btn.click(fn=evaluate_team, inputs=team_dropdown, outputs=output_markdown)
    sim_btn.click(fn=find_similar_players, inputs=player_dropdown, outputs=output_markdown)
    trade_btn.click(fn=recommend_trade_targets, inputs=team_dropdown, outputs=output_table)
    stat_btn.click(fn=team_stat_plot, inputs=stat_dropdown, outputs=output_plot)
    bio_btn.click(fn=similar_bio_players, inputs=query_input, outputs=output_markdown)

demo.launch(share=True)
