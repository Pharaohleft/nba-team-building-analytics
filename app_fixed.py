import gradio as gr
import pandas as pd
import plotly.express as px
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load updated fallback CSV with real heights
df = pd.read_csv("nba_fallback.csv")

# Preprocessing
df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
df["Height (inches)"] = pd.to_numeric(df["Height (inches)"], errors="coerce")
df["PTS"] = pd.to_numeric(df["PTS"], errors="coerce")
df["REB"] = pd.to_numeric(df["REB"], errors="coerce")
df["AST"] = pd.to_numeric(df["AST"], errors="coerce")
df["PLAYER_NAME"] = df["PLAYER_NAME"].fillna("Unknown")
df.dropna(subset=["TEAM_ABBREVIATION", "PLAYER_NAME"], inplace=True)

# Utility Functions
def team_structure_analysis(team_name):
    team_df = df[df["TEAM_ABBREVIATION"] == team_name]
    results = {}
    results["Total Players"] = len(team_df)
    results["Players Under 27"] = len(team_df[team_df["AGE"] < 27])
    results["7-Footers"] = len(team_df[team_df["Height (inches)"] >= 84])
    results["Frontcourt Avg Height"] = round(team_df[team_df["Pos"].isin(["C", "PF", "SF"])]["Height (inches)"].mean(), 2)
    results["Top Scorers"] = team_df.sort_values("PTS", ascending=False).head(3)["PLAYER_NAME"].tolist()
    results["Top Rebounders"] = team_df.sort_values("REB", ascending=False).head(3)["PLAYER_NAME"].tolist()
    results["Top Playmakers"] = team_df.sort_values("AST", ascending=False).head(3)["PLAYER_NAME"].tolist()
    return results

def compare_teams(team1, team2):
    analysis1 = team_structure_analysis(team1)
    analysis2 = team_structure_analysis(team2)
    return pd.DataFrame([analysis1, analysis2], index=[team1, team2])

def suggest_trade(team_name):
    team_df = df[df["TEAM_ABBREVIATION"] == team_name]
    trade_candidates = df[(df["TEAM_ABBREVIATION"] != team_name) & (df["AGE"] < 27)]
    current_avg_pts = team_df["PTS"].mean()
    current_avg_reb = team_df["REB"].mean()
    current_avg_ast = team_df["AST"].mean()
    trade_candidates["ScoreDelta"] = (
        (trade_candidates["PTS"] - current_avg_pts).abs() +
        (trade_candidates["REB"] - current_avg_reb).abs() +
        (trade_candidates["AST"] - current_avg_ast).abs()
    )
    best_trade = trade_candidates.sort_values("ScoreDelta").head(1)
    return best_trade[["PLAYER_NAME", "TEAM_ABBREVIATION", "AGE", "PTS", "REB", "AST"]]

def predict_parlay(player_name):
    player = df[df["PLAYER_NAME"] == player_name]
    if player.empty:
        return "Player not found."
    row = player.iloc[0]
    forecast = {
        "Predicted Points": round(row["PTS"] + random.uniform(-2, 2), 1),
        "Predicted Rebounds": round(row["REB"] + random.uniform(-1, 1), 1),
        "Predicted Assists": round(row["AST"] + random.uniform(-1, 1), 1)
    }
    return forecast

def plot_team(team_name):
    team_df = df[df["TEAM_ABBREVIATION"] == team_name]
    fig = px.scatter(team_df, x="PTS", y="REB", color="Pos", size="AST",
                     hover_name="PLAYER_NAME", title=f"{team_name} Player Stats")
    return fig

def role_finder(role):
    if role == "3&D Wing":
        result = df[(df["Pos"].isin(["SF", "SG"])) & (df["PTS"] > 10) & (df["REB"] > 3)]
    elif role == "Playmaker":
        result = df[(df["AST"] > 5)]
    elif role == "Stretch Big":
        result = df[(df["Pos"].isin(["PF", "C"])) & (df["PTS"] > 10)]
    else:
        result = df.head(10)
    return result[["PLAYER_NAME", "TEAM_ABBREVIATION", "Pos", "PTS", "REB", "AST"]].sort_values("PTS", ascending=False)

def archetype_matcher(player_name):
    target = df[df["PLAYER_NAME"] == player_name]
    if target.empty:
        return "Player not found."
    t = target.iloc[0]
    df["Similarity"] = ((df["PTS"] - t["PTS"]).abs() +
                        (df["REB"] - t["REB"]).abs() +
                        (df["AST"] - t["AST"]).abs() +
                        (df["AGE"] - t["AGE"]).abs())
    similar = df[df["PLAYER_NAME"] != player_name].sort_values("Similarity").head(3)
    return similar[["PLAYER_NAME", "TEAM_ABBREVIATION", "Pos", "PTS", "REB", "AST"]]

def top_x_lists():
    under_25 = df[df["AGE"] < 25].sort_values("PTS", ascending=False).head(10)
    by_pos = df.groupby("Pos").apply(lambda x: x.sort_values("REB", ascending=False).head(1))
    tallest = df.loc[df.groupby("TEAM_ABBREVIATION")["Height (inches)"].idxmax()]
    return under_25[["PLAYER_NAME", "PTS"]], by_pos[["PLAYER_NAME", "Pos", "REB"]], tallest[["PLAYER_NAME", "TEAM_ABBREVIATION", "Height (inches)"]]

def embedding_similarity(player_name):
    df_clean = df.dropna(subset=["PTS", "REB", "AST", "AGE", "Height (inches)"])
    features = df_clean[["PTS", "REB", "AST", "AGE", "Height (inches)"]]
    if player_name not in df_clean["PLAYER_NAME"].values:
        return "Player not found."
    player_vector = features[df_clean["PLAYER_NAME"] == player_name].values
    similarities = cosine_similarity(features, player_vector).flatten()
    df_clean["Similarity"] = similarities
    result = df_clean[df_clean["PLAYER_NAME"] != player_name].sort_values("Similarity", ascending=False).head(5)
    return result[["PLAYER_NAME", "TEAM_ABBREVIATION", "Pos", "PTS", "REB", "AST"]]

def team_needs(team_name):
    team_df = df[df["TEAM_ABBREVIATION"] == team_name]
    needs = []
    if len(team_df[team_df["Pos"] == "PG"]) < 2:
        needs.append("Needs more point guards")
    if len(team_df[team_df["Pos"] == "C"]) < 1:
        needs.append("Needs at least 1 true center")
    if team_df["AST"].mean() < 3:
        needs.append("Low playmaking")
    if team_df["REB"].mean() < 4:
        needs.append("Low rebounding")
    return needs if needs else ["Well-balanced roster"]

# Gradio Interface with Blocks
def launch_app():
    with gr.Blocks() as app:
        gr.Markdown("# 🏀 NBA Role Search Dashboard")

        with gr.Tab("Team Analysis"):
            with gr.Row():
                team_dropdown = gr.Dropdown(choices=sorted(df["TEAM_ABBREVIATION"].unique()), label="Select Team")
                analyze_btn = gr.Button("Analyze Team")
            team_output = gr.JSON()
            team_plot = gr.Plot()

        with gr.Tab("Compare Teams"):
            with gr.Row():
                team1 = gr.Dropdown(choices=sorted(df["TEAM_ABBREVIATION"].unique()), label="Team 1")
                team2 = gr.Dropdown(choices=sorted(df["TEAM_ABBREVIATION"].unique()), label="Team 2")
                compare_btn = gr.Button("Compare")
            compare_output = gr.Dataframe()

        with gr.Tab("Suggest Trade"):
            trade_team = gr.Dropdown(choices=sorted(df["TEAM_ABBREVIATION"].unique()), label="Team")
            trade_btn = gr.Button("Suggest Trade")
            trade_output = gr.Dataframe()

        with gr.Tab("Parlay Predictor"):
            player_name = gr.Dropdown(choices=sorted(df["PLAYER_NAME"].unique()), label="Player")
            parlay_btn = gr.Button("Predict")
            parlay_output = gr.JSON()

        with gr.Tab("Find Roles"):
            role_input = gr.Dropdown(choices=["3&D Wing", "Playmaker", "Stretch Big"], label="Choose Role")
            role_btn = gr.Button("Find Players")
            role_output = gr.Dataframe()

        with gr.Tab("Match Archetype"):
            match_player = gr.Dropdown(choices=sorted(df["PLAYER_NAME"].unique()), label="Select Player")
            match_btn = gr.Button("Find Matches")
            match_output = gr.Dataframe()

        with gr.Tab("Top X Lists"):
            topx_btn = gr.Button("Generate Lists")
            under25_output = gr.Dataframe(label="Top Scorers Under 25")
            topreb_output = gr.Dataframe(label="Top Rebounders by Position")
            tallest_output = gr.Dataframe(label="Tallest by Team")

        with gr.Tab("Advanced Similarity"):
            embed_player = gr.Dropdown(choices=sorted(df["PLAYER_NAME"].unique()), label="Select Player")
            embed_btn = gr.Button("Find Similar Players (Embeddings)")
            embed_output = gr.Dataframe()

        with gr.Tab("Team Needs"):
            team_need_input = gr.Dropdown(choices=sorted(df["TEAM_ABBREVIATION"].unique()), label="Team")
            need_btn = gr.Button("Check Team Needs")
            need_output = gr.JSON()

        analyze_btn.click(fn=team_structure_analysis, inputs=team_dropdown, outputs=team_output)
        analyze_btn.click(fn=plot_team, inputs=team_dropdown, outputs=team_plot)
        compare_btn.click(fn=compare_teams, inputs=[team1, team2], outputs=compare_output)
        trade_btn.click(fn=suggest_trade, inputs=trade_team, outputs=trade_output)
        parlay_btn.click(fn=predict_parlay, inputs=player_name, outputs=parlay_output)
        role_btn.click(fn=role_finder, inputs=role_input, outputs=role_output)
        match_btn.click(fn=archetype_matcher, inputs=match_player, outputs=match_output)
        topx_btn.click(fn=top_x_lists, inputs=[], outputs=[under25_output, topreb_output, tallest_output])
        embed_btn.click(fn=embedding_similarity, inputs=embed_player, outputs=embed_output)
        need_btn.click(fn=team_needs, inputs=team_need_input, outputs=need_output)

    app.launch()

if __name__ == "__main__":
    launch_app()
