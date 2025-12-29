import gradio as gr
import pandas as pd

# === Load player dataset ===
df = pd.read_csv("nba_players_latest.csv")  # Replace with your latest merged dataset

# === Core team evaluator ===
def evaluate_team(team_abbr):
    team = df[df['TEAM_ABBREVIATION'] == team_abbr.upper()]
    report = []

    # 1. At least 2 players >= 84 inches (~7'0")
    seven_footers = team[team['HEIGHT'] >= 84]
    report.append(f"{'✅' if len(seven_footers) >= 2 else '❌'} Has {len(seven_footers)} 7-footers")

    # 2. Avg frontcourt height >= 77 inches (~6'5")
    frontcourt = team[team['HEIGHT'] >= 77]
    avg_height = frontcourt['HEIGHT'].mean()
    report.append(f"{'✅' if avg_height >= 77 else '❌'} Avg frontcourt height: {avg_height:.1f} in")

    # 3. 7 players under age 27
    under_27 = team[team['AGE'] < 27]
    report.append(f"{'✅' if len(under_27) >= 7 else '❌'} {len(under_27)} players under age 27")

    # 4. At least 3 defense-oriented (e.g., BLK, STL ranks top 150)
    defensive = team[(team['BLK_RANK'] < 150) | (team['STL_RANK'] < 150)]
    report.append(f"{'✅' if len(defensive) >= 3 else '❌'} {len(defensive)} defensive players")

    # 5. At least 5 offensive-oriented (e.g., PTS, AST ranks top 150)
    offensive = team[(team['PTS_RANK'] < 150) | (team['AST_RANK'] < 150)]
    report.append(f"{'✅' if len(offensive) >= 5 else '❌'} {len(offensive)} offensive players")

    # 6. Midrange score bonus (2PT% > 50%)
    midrange_killers = team[team['FG2_PCT'] > 0.50]
    report.append(f"{'✅' if len(midrange_killers) >= 3 else '⚠️'} {len(midrange_killers)} strong midrange shooters")

    # 7. Veteran confidence score (AGE > 30 & 2PT% > 50%)
    vets = team[(team['AGE'] > 30) & (team['FG2_PCT'] > 0.50)]
    report.append(f"{'✅' if len(vets) >= 2 else '⚠️'} {len(vets)} confident veterans")

    return "\n".join(report)

# === Trade target suggester ===
def recommend_players():
    df_filtered = df[(df['AGE'] < 27) & (df['HEIGHT'] >= 84)]
    top = df_filtered[['PLAYER_NAME', 'AGE', 'HEIGHT', 'PTS_RANK', 'BLK_RANK']].sort_values(by='PTS_RANK').head(10)
    return top.to_markdown(index=False)

# === UI ===
with gr.Blocks() as app:
    gr.Markdown("## 🏀 TeamCraft.AI – NBA Roster Evaluator")

    team_input = gr.Textbox(label="Enter NBA Team Abbreviation (e.g., GSW, LAL, MIA)", value="GSW")
    team_output = gr.Textbox(label="Team Evaluation Report")
    trade_output = gr.Textbox(label="Suggested Young Bigs (<27 y/o & 7ft)")

    btn = gr.Button("Analyze Roster")

    def run_all(team):
        return evaluate_team(team), recommend_players()

    btn.click(fn=run_all, inputs=team_input, outputs=[team_output, trade_output])

app.launch(share=True)
