# NBA Roster Optimization Analysis

## LA clippers Roster Cost Efficiency & Replacement Analysis

**Date:** October 2025  
**Document Type:** Technical Audit  
**Target Audience:** Director of Analytics

---

## Project Overview

The Los Angeles Clippers operate in one of the most financially constrained environments in professional sports. As a Data Analyst supporting the LA Clippers’ basketball operations team, I worked on evaluating roster cost efficiency under the constraints of the 2024 NBA Collective Bargaining Agreement. With stricter luxury tax penalties and limited roster flexibility, leadership needed a way to analyse player production to optimize player contracts. Under the previous CBA, teams could correct roster inefficiencies by paying additional luxury tax. Under the current CBA, exceeding the Second Apron results in severe long-term penalties, including frozen future draft picks and restricted trade flexibility. As a result, inefficient contracts now pose a structural risk to the franchise rather than a temporary financial cost.

As a result, NBA front offices can no longer rely on financial spending alone to correct roster inefficiencies. Instead, teams must identify cost-efficient player alternatives that preserve on-court production while maintaining salary cap flexibility.

This analysis supports that objective by examining league-wide player performance data to identify statistically comparable players available at lower cost, helping decision-makers evaluate replacement options, contract risk, and roster efficiency under modern cap constraints

---



## Business Problem

NBA roster spending shows clear inefficiencies when player salary is compared against on-court production. A small group of high-cost players consumes a disproportionate share of payroll. By grouping players into performance-based roles and measuring similarity within those groups, the analysis identifies viable replacement candidates delivering 80–90% of the production of higher-salary players. Importantly, these groupings remain largely stable under small statistical variation, indicating that identified alternatives are not driven by noise or outlier performance.

The objective was to analyze league-wide player data to uncover usage concentration, role redundancy, player similarity, and age-related performance decline patterns that influence roster stability, succession planning, and long-term competitive viability. The analysis uses season-level NBA player data and combines exploratory analysis, unsupervised learning, similarity modeling, dimensionality reduction, and interactive visualization to move from raw statistics to decision-support insights.

This project reframes roster building as a resource allocation problem, rather than a talent ranking exercise.

---

## Context

### 2024 NBA Collective Bargaining Agreement

- **The Frozen Pick:** Teams above the apron have their 1st-round pick seven years out (e.g., 2032) frozen. If they remain above the apron for 2 of the next 4 years, that pick drops to the end of the round.
- **Liquidity Freeze:** Teams cannot aggregate salaries in trades, cannot send cash in deals, and cannot use existing Trade Exceptions (TEs).
- **The "One-Way" Trap:** High-salary players become immovable assets because opposing teams cannot aggregate smaller contracts to match the salary.

By utilizing Principal Component Analysis (PCA) to reduce noise and Cosine Similarity to identify statistically similar players, we identify low-cost assets (Minimum/Mid-Level Exception players) that provide >85% statistical similarity to high-cost stars but with lower volume.

---


## Data Used

The data was pulled using beautifulsoup to scrape nba stats table for 2014 – 2024 This year frame was decided since the game dynamics have severly changed in the past 10 years.Players with fewer than 10 games played were excluded to reduce small-sample bias.

**Source:** Basketball-Reference “NBA 2024 Totals” table (scraped via Python).

### Feature set used for clustering (9 total):
- Volume/impact: PTS, AST, TRB, STL, BLK, TOV
- Efficiency: FG%, 3P%, FT%

### Preparation steps implemented in the notebook
- Removed duplicate header rows embedded in the HTML table
- Converted numeric columns to numeric types
- Filled missing values with 0 before modeling
- Standardized features using StandardScaler prior to clustering

### Dataset Overview

The core dataset consists of NBA player season-level statistics, with one row per player per season. The dataset includes:
- Player identifiers (name, team, position)
- Age by season
- Playing time (games played, minutes)
- Production metrics (points, assists, rebounds)
- Efficiency indicators (field goal %, three-point %, free throw %)
- Supporting statistics (turnovers, steals, blocks)

This dataset was assembled from authoritative public NBA sources and frozen into a CSV to ensure reproducibility across Python analyses and Tableau dashboards.

### Scope Decisions
- Analysis is conducted at the season level, not game level
- Players with minimal playing time were excluded to reduce noise

### Key data components:
- Offensive production: Points, assists, turnovers
- Rebounding & defense: Total rebounds, steals, blocks
- Efficiency metrics: Field goal %, three-point %, free throw %
- Team identifiers: Used for roster composition analysis

All numeric features were standardized prior to analysis to ensure comparability across metrics with different scales.

<img width="752" height="456" alt="Picture1" src="https://github.com/user-attachments/assets/251da94a-5d35-4c15-9b24-fa7972c14285" />

- - - 
## Key Questions Answered

- Which players provide the highest on-court production relative to their cost?
- Which high-salary players have statistically similar lower-cost alternatives?
- How can players be grouped by performance profile independent of position?
- Which players sit on the boundary between roles, indicating replaceability or volatility?
- Where do rosters present opportunities to reduce payroll without reducing output?
- Can player production be replicated at a lower cost?
- Are there players across the league who produce statistically similar output to high-usage or high-salary players, but are paid significantly less?
- Which player attributes actually define “similarity”?
- Beyond points per game, which combination of usage, efficiency, playmaking, and defensive metrics best capture a player’s on-court role?
- Which undervalued players are the best fit to fill specific team gaps?


---

## Primary Business Value

### Portfolio Risk Management
- **Objective:** Prevent over-allocation of capital toward declining assets.
- **Methodology:** Utilizing the Age-Performance Dashboard, the system identifies the statistical "inflection point" where production begins to decouple from market value.

### Capital Efficiency & Asset Arbitrage
- **Objective:** Maximize roster productivity within the constraints of the salary cap.
- **Methodology:** identifies "undervalued clusters" - players who deliver elite-tier output (efficiency, defensive impact) but are currently priced as mid-tier assets because of lower volume.
- **Business Outcome:** Locates market inefficiencies to optimize "Points per Dollar" spent.

### Structural Roster Auditing
- **Objective:** Identify tactical gaps that traditional depth charts obscure.
- **Methodology:** Implemented K-Means Clustering to categorize players by functional Archetypes over standard positions (Secondary Playmakers vs. Interior Anchors).
- **Business Outcome:** Visualizes roster gaps allowing GMs to target specific skill sets such as perimeter spacing or rim protection rather than filling a PG, SG, PF, C, SF.

---

##  Key Insights
### Performance-Based Player Segmentation

Players were grouped into four performance profiles based on multi-dimensional statistical similarity rather than traditional positions:

<img width="388" height="198" alt="2" src="https://github.com/user-attachments/assets/9861e7ce-7ef3-4772-ab0b-7d842cc26345" />


- Cluster 2 has the highest average PTS and AST (high-usage offensive hub profile).

<img width="597" height="195" alt="Picture3" src="https://github.com/user-attachments/assets/ec7f6e81-f281-4e6d-a2af-e4727af68050" />

- Luka Dončić, Shai Gilgeous-Alexander, Giannis Antetokounmpo, Jalen Brunson, Nikola Jokić appear with Cluster = 2 in the displayed head output. This supports the interpretation that one cluster is capturing primary offensive engines.
- Cluster 0 shows the highest average TRB and BLK (interior/rebounding + rim protection profile).
- Cluster 1 is extremely low across metrics (low-usage / limited production profile).
- Cluster 3 sits between clusters 1 and 2 (mid-usage contributors).

This role-based segmentation reveals that players with similar on-court responsibilities often exist across salary tiers.

--- 

### Cost–Production Misalignment
   <img width="572" height="382" alt="Picture4" src="https://github.com/user-attachments/assets/e8ba91fc-4729-494b-9e44-579aab790f71" />
Within the same performance groups, player production varies far less than player compensation. Multiple lower-cost players demonstrate statistical profiles that closely mirror those of significantly higher-paid peers, suggesting market inefficiencies driven by reputation, tenure, or contract timing rather than output alone. This misalignment creates opportunities for teams to reallocate salary without materially impacting performance.

---

### Replacement Value Identification


<img width="580" height="385" alt="Picture5" src="https://github.com/user-attachments/assets/b96edcfc-4780-4e29-bd71-f21bbeb5e20c" />

<img width="575" height="412" alt="Picture6" src="https://github.com/user-attachments/assets/3159e836-fa28-4baf-aacd-a798229b2fd7" />
Our analysis prioritized finding "Borderline Players"—athletes mathematically positioned between clusters. These players represent "hybrid" value that traditional scouting often misses.

- **Key Findings:** The PCA model explicitly identified specific players as outliers or "misfits" near cluster boundaries.
  - Victor Wembanyama: Identified as a "Two-Way Threat" with a high Euclidean distance ($7.59$), confirming his statistical uniqueness.
  - Domantas Sabonis: Categorized as a "Floor General" (Distance: $5.95$), validating his role as a hub rather than a traditional big.
  - Luke Kornet: Identified as a "Glass Cleaner" (Distance: $6.23$), suggesting a specific niche utility.

By measuring player-to-player similarity within performance groups, the analysis surfaces replacement candidates delivering 85%+ statistical similarity to higher-salary players across core metrics.

<img width="573" height="285" alt="Picture7" src="https://github.com/user-attachments/assets/6e9cfa6d-b610-4830-a142-2727efeed840" />

To test robustness, controlled statistical noise was introduced and player groupings were recalculated. The majority of players retained their original role classification, indicating that identified similarities are structural rather than incidental.

- “144 players changed clusters after noise.”

**Interpretation:**
- Some clusters are stable (core members remain)
- A meaningful subset of players are borderline and can flip clusters with moderate perturbation
- This is expected in player profiles that sit between roles (e.g., scorer vs two-way wing, wing vs big, etc.)

Players who frequently shifted roles were flagged as borderline contributors, representing higher uncertainty and potential performance volatility.

---


### Roster Composition Insights
<img width="578" height="455" alt="Picture8" src="https://github.com/user-attachments/assets/39db0515-fa77-4c8b-843b-1e4f34f5ebd1" />
- KMeans (k=4) assigns each player to one of four performance clusters.
- PCA (2D) compresses the standardized feature space to visualize cluster separation.

Aggregating player roles at the team level highlights differences in roster construction strategies. Some teams concentrate salary in a narrow set of roles, increasing financial risk, while others distribute production more evenly across lower-cost contributors.

The clustering results show clear separation between role archetypes:
- A small cluster of high-usage offensive hubs dominates scoring and playmaking
- A second group of primary scorers contributes points with less playmaking responsibility
- Larger clusters consist of all-around contributors and low-usage specialists

The distribution of players across clusters is uneven: High-usage roles represent a minority of players but account for a majority of offensive output.

---

### Why This Matters

This mirrors concentration risk in other industries:
- A small number of assets carry outsized importance
- Failure or decline in those assets has disproportionate impact

For NBA teams, this creates:
- Increased injury sensitivity
- Steeper performance drop-offs when stars age
- Higher volatility in outcomes tied to a single role cluster

---

### Role Redundancy and Player Similarity

If a high-usage player declines or misses time, are there statistically comparable players who can absorb that role?

- Many players classified as secondary or low-usage contributors exhibit statistical profiles similar to higher-usage peers
- Differences between players often stem from usage volume, not efficiency
- Some teams possess internal redundancy that is not reflected in current rotations

---

### Why This Matters

Similarity analysis reveals latent substitution capacity:
- Load management opportunities
- Role transitions without major tactical changes
- Lower-risk succession planning for aging players

This challenges the assumption that high-usage roles are irreplaceable.

---

### Career Trajectories and Profile Evolution

Do players with similar early-career profiles evolve similarly over time?


<img width="752" height="476" alt="Picture9" src="https://github.com/user-attachments/assets/6471c84d-7784-42e6-ac86-f5675e451b2c" />
<img width="752" height="479" alt="Picture10" src="https://github.com/user-attachments/assets/82ee505e-8822-4306-a50e-ccf7cb39b2bc" />
<img width="752" height="484" alt="Picture11" src="https://github.com/user-attachments/assets/45efb7d2-ee13-455a-9c6e-951a446aba61" />
<img width="752" height="485" alt="Picture12" src="https://github.com/user-attachments/assets/2760b86d-6ac1-401f-9853-87d300f80d2b" />

- Early-career similarity does not guarantee parallel development
- Some players converge toward similar profiles, others diverge sharply
- Usage growth and efficiency changes drive most trajectory divergence

---

### Why This Matters

Front offices often extrapolate future performance from early success. This analysis shows that development paths are unstable, reinforcing the need for ongoing profile monitoring rather than static projections.

---

### Aging Curve and Scoring Decline

How does scoring output change with age, and does this differ by position?
<img width="752" height="405" alt="Picture13" src="https://github.com/user-attachments/assets/7e1e7831-2e99-4349-a0ab-9fb23bd9b5d0" />

<img width="752" height="305" alt="Picture14" src="https://github.com/user-attachments/assets/047b35fa-1afa-4a76-b039-5642465b0c89" />
<img width="752" height="318" alt="Picture15" src="https://github.com/user-attachments/assets/16b122c4-e29e-454d-9842-2d4f413ff2a6" />
<img width="752" height="306" alt="Picture16" src="https://github.com/user-attachments/assets/726f90ed-f1c7-43a7-920d-7799c21b1cdd" />
**Guards and Wings**
- Scoring output peaks in the mid-to-late 20s
- Sharp thinning of high-PPG players after age 30
- Only a small fraction of players maintain elite scoring beyond this point

**Centers**
- Flatter scoring curves
- Slower decline
- Less extreme dependency on athleticism and shot creation

---

### Why This Matters

- High-usage perimeter roles carry greater aging risk
- Veteran outliers exist but should not be treated as planning baselines
- Teams delaying role transitions often absorb sudden performance cliffs

---

### Youth vs. Experience

- **The Peak Performance Zone:** Most players hit their highest scoring potential in their mid-20s (like Jayson Tatum or Jaylen Brown).
- **The Specialized Veterans:** Players like Al Horford show us that as you get older, your role changes.

---

### Connecting the Insights: Structural Roster Risk

When combined, these analyses reveal a consistent pattern:

- Offensive responsibility is concentrated
- High-usage roles age poorly
- Comparable substitutes often exist but are underutilized
- Teams frequently react to player decline instead of anticipating it

---

### FG% – 2P% coorelation

**The Midrange(The 0.96 Correlation)**

<img width="602" height="533" alt="Picture17" src="https://github.com/user-attachments/assets/92e8e449-887e-4859-9d78-75457f03751c" />
- analysis reveals a 0.96 correlation between Midrange Efficiency (10-16ft) and FG% Efficiency.
- The Signal: A high Midrange% is the strongest leading indicator success.
- Draft Strategy: Teams should aggressively draft "Midrange Specialists" as the market undervalues them.

---

We input the target vector (Player: Zach LaVine) into the ROE using Cosine Similarity constraints.

The model returned a "Composite Aggregate" of three players:

**Target Asset:**
- Zach LaVine: 24.8 PPG, 37% 3P, $40.0M Cost

**The Aggregate (Model Recommendation):**
- Player A (Malik Monk): High-volume scorer / Secondary Creator (Similarity: 0.89)
- Player B (Gary Trent Jr.): Movement Shooter (Similarity: 0.82)
- Player C (Minimum Contract Wing): Low-usage spacer.

**Aggregate Output:**
- Total Cost: $22.5M (43% Savings)
- Aggregate PPG: 28.4 PPG (+3.6 vs Target)
- Aggregate 3P%: 38.1% (+1.1% vs Target).

---

## KPIs & Decision Metrics

### Key Performance Indicators used in this analysis include:
- Cost per Unit of Production (salary proxy vs composite performance)
- Performance Similarity Score (%)
- Cluster Distance from Role Center (volatility indicator)
- Percentage of Roster in High-Cost / High-Replaceability Roles

### 1. Usage Concentration Ratio
- Top X players’ usage / total team usage
- Purpose: Identify over-dependence on a small core

### 2. Role Redundancy Score
- Average similarity distance between top-usage players and next-tier contributors
- Purpose: Measure substitution readiness

### 3. Aging Exposure Index
- Share of usage allocated to players aged 30+
- Purpose: Quantify decline risk concentration

### Cluster Composition Metrics
- Players per cluster
- Cluster-level average PTS/AST/TRB/STL/BLK

---

## Overview of Findings

NBA player contribution is highly concentrated within a small number of high-usage roles. Clustering analysis reveals that a limited subset of players accounts for a disproportionate share of scoring and playmaking across the league. Similarity analysis shows that many statistically comparable players exist within these roles, suggesting underutilized substitution and load-management opportunities. Age-based analysis demonstrates that scoring output peaks in the mid-to-late 20s for guards and wings, followed by a sharp decline after age 30, with only a small number of outliers sustaining elite production.

---

## Recommendations

- Instead of overpaying for Cluster 2 players, we should target the 3 players identified in the PCA outputs (e.g., players statistically similar to the cluster 3 but undervalued).
- Prioritize replacing or restructuring contracts where lower-cost assets provide comparable production
- Monitor borderline players closely due to higher performance volatility
- Balance roster composition to reduce concentration of salary within a single role

---

## Assumptions & Caveats

- Raw PPG favors high-usage roles
- Analysis is based on a single season snapshot and does not capture multi-year trends
- Salary figures are treated as external context rather than modeled directly

---

### Tableau Public Dashboard
→ See interactive roster comparisons and player role distributions
https://public.tableau.com/app/profile/austin.abraham5815/viz/NBAathleteyoungvsold/AgeDashboard

### Youtube Project Walkthrough ( Trade Recommender App)
https://youtu.be/-bg97gmqsvw

### Hugging face spaces nba app
https://huggingface.co/spaces/pharaohleft/nba-role-search

 ### Substack Blog
→ Narrative walkthrough of insights and roster logic
https://pharaohleft.substack.com/p/data-driven-investigation-into-what
