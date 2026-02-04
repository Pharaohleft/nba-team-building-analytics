
## Portfolio Cost Efficiency & Replacement Analysis  
**Context:** Professional Sports Organization (Anonymized)  
**Role:** Data Analyst  
**Date:** October 2025


---
## Project Overview

Organizations operating under strict budget constraints must ensure that spending is aligned with measurable contribution rather than reputation or historical cost. In environments with limited flexibility, inefficient allocations introduce long-term structural risk rather than short-term financial tradeoffs.

In this project, I supported a professional sports organization’s operations team by analyzing cost efficiency across a constrained asset portfolio under updated regulatory rules. The objective was to evaluate whether high-cost assets were delivering proportionate contribution and to identify lower-cost alternatives capable of preserving output.

The analysis reframes roster construction as a portfolio optimization problem, using historical performance data to support cost-aware decision-making, replacement planning, and long-term risk management.


---



## Business Problem

Portfolio spending showed clear inefficiencies when cost was compared against on-court contribution. A small subset of high-cost assets consumed a disproportionate share of total budget, increasing exposure to aging, injury, and performance volatility.

Leadership needed a data-driven way to:
- Measure contribution independent of labels or reputation  
- Identify functional redundancy within the portfolio  
- Evaluate whether comparable contribution could be achieved at lower cost  
- Reduce financial risk without materially impacting aggregate output  

This analysis addresses those needs by grouping assets into functional archetypes and evaluating similarity within those groups rather than relying on traditional classifications.


---

## Operational Context

Recent regulatory changes introduced hard constraints on portfolio flexibility, limiting the ability to correct inefficiencies through additional spending. Under the updated framework, exceeding predefined thresholds results in long-term penalties, including restricted future options and reduced liquidity.

As a result, inefficient allocations now represent structural risk rather than temporary financial cost. Decision-makers must proactively identify cost-efficient alternatives and manage concentration risk before constraints are breached.

This context makes contribution-based analysis and replacement planning critical components of sustainable portfolio management.


---


## Data Used

The analysis uses season-level asset performance data collected from authoritative public sources and frozen into a structured dataset to ensure reproducibility.

**Dataset characteristics:**
- Time range: 2014–2024  
- Unit of analysis: Asset per season  
- Observations: ~700 asset-seasons after filtering  

**Feature categories:**
- Contribution volume: scoring, playmaking, rebounding, defensive actions  
- Efficiency indicators: shooting efficiency metrics  
- Contextual attributes: age, participation level  

**Preparation steps:**
- Removed duplicated records and embedded header artifacts  
- Standardized numeric features to ensure cross-metric comparability  
- Excluded low-participation assets to reduce small-sample bias  

These steps prioritize structural signal and analytical reliability over short-term variance.

The core dataset consists of NBA player season-level statistics, with one row per player per season. The dataset includes:
- Player identifiers (name, team, position)
- Age by season
- Playing time (games played, minutes)
- Production metrics (points, assists, rebounds)
- Efficiency indicators (field goal %, three-point %, free throw %)
- Supporting statistics (turnovers, steals, blocks)

<img width="752" height="456" alt="Picture1" src="https://github.com/user-attachments/assets/251da94a-5d35-4c15-9b24-fa7972c14285" />

- - - 
## Key Questions Answered

- Which assets deliver the highest contribution relative to cost?
- Where is contribution concentrated, creating dependency risk?
- Which high-cost assets have statistically comparable lower-cost substitutes?
- How can assets be grouped by functional contribution independent of labels?
- Where does the portfolio present opportunities to reduce cost without reducing output?
- Which assets exhibit higher volatility or replacement risk based on stability analysis?
  
---

## Primary Business Value

### Portfolio Risk Management
- **Objective:** Reduce exposure to declining or volatile high-cost assets.
- **Approach:** Analyzed age-related contribution patterns and stability indicators to identify inflection points where contribution decouples from cost.
- **Value:** Enables earlier intervention in contract planning and succession decisions before risk materializes.

### Capital Efficiency
- **Objective:** Maximize total portfolio contribution within fixed budget constraints.
- **Approach:** Grouped assets into functional archetypes and evaluated similarity within those groups to identify lower-cost substitutes with comparable contribution profiles.
- **Value:** Supports reallocation of spend without materially reducing aggregate output.

### Structural Portfolio Auditing
- **Objective:** Identify functional gaps and redundancies that traditional classifications obscure.
- **Approach:** Used contribution-based archetypes rather than labels to assess coverage across functional roles.
- **Value:** Improves targeting of specific capability needs instead of over-investing in redundant profiles.

---
## Key Insights

### 1. Contribution Is Highly Concentrated
A small subset of assets accounts for a disproportionate share of total contribution across the portfolio. This concentration increases dependency risk and amplifies the impact of performance decline or unavailability.

### 2. Cost and Contribution Are Weakly Aligned Within Roles
Within the same functional archetype, contribution profiles vary far less than associated cost. Multiple lower-cost assets exhibit statistically similar contribution patterns to higher-cost counterparts, indicating inefficiencies driven by factors beyond measurable output.

### 3. Functional Archetypes Reveal Hidden Redundancy
Grouping assets by contribution patterns rather than labels exposes both redundancy and coverage gaps that are not visible through traditional classifications. Some portfolios concentrate spend within a narrow set of archetypes, while others distribute contribution more evenly.

### 4. Replacement Feasibility Exists Across Cost Tiers
Similarity analysis identifies viable substitutes delivering approximately 80–90% comparable contribution within the same archetype. These substitutes represent practical options for cost reduction, role transition, or contingency planning.

### 5. Stability Analysis Identifies Higher-Risk Profiles
Robustness testing shows that while most assets retain stable archetype assignments, a subset frequently shifts roles under small perturbations. These borderline profiles carry higher evaluation risk and warrant closer monitoring.

### 6. Aging Patterns Increase Risk in High-Usage Roles
High-usage archetypes exhibit earlier and steeper contribution decline compared to lower-usage profiles. Delayed reallocation away from these roles increases the likelihood of abrupt performance cliffs rather than gradual transitions.


<img width="388" height="198" alt="2" src="https://github.com/user-attachments/assets/9861e7ce-7ef3-4772-ab0b-7d842cc26345" />

<img width="597" height="195" alt="Picture3" src="https://github.com/user-attachments/assets/ec7f6e81-f281-4e6d-a2af-e4727af68050" />

--- 

   <img width="572" height="382" alt="Picture4" src="https://github.com/user-attachments/assets/e8ba91fc-4729-494b-9e44-579aab790f71" />


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

- 144 players changed clusters after noise.

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

- High-usage perimeter roles carry greater aging risk
- Veteran outliers exist but should not be treated as planning baselines
- Teams delaying role transitions often absorb sudden performance cliffs

- **The Peak Performance Zone:** Most players hit their highest scoring potential in their late-20s .


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

The analysis uses a focused set of metrics designed to support portfolio-level decision-making rather than isolated performance evaluation.

### Core Metrics

- **Contribution-to-Cost Ratio**  
  Measures aggregate contribution relative to cost to identify inefficient allocations.

- **Performance Similarity Score**  
  Quantifies statistical similarity between assets within the same functional archetype to evaluate substitution feasibility.

- **Role Stability Index**  
  Captures sensitivity of archetype assignment under small performance perturbations, serving as a proxy for evaluation risk.

- **Usage Concentration Ratio**  
  Measures the share of total contribution generated by the highest-usage assets to assess dependency risk.

- **Aging Exposure Index**  
  Quantifies the proportion of total contribution attributed to older assets, indicating vulnerability to performance decline.

### Portfolio Monitoring Use Cases

These metrics enable leadership to:
- Detect over-reliance on a small subset of high-cost assets  
- Identify opportunities to rebalance spend without reducing output  
- Monitor risk accumulation driven by aging or unstable profiles  
- Track efficiency trends over time rather than relying on point-in-time judgments  



---
## Overview of Findings

The analysis shows that portfolio contribution is concentrated within a limited set of high-usage functional archetypes. While these assets drive a majority of output, they also introduce elevated risk due to cost concentration, aging effects, and higher volatility.

Similarity analysis demonstrates that statistically comparable contribution profiles exist across cost tiers within the same archetypes, indicating underutilized substitution capacity. This creates opportunities to rebalance spend without materially reducing aggregate output.

Age-based patterns further reveal that high-usage archetypes experience earlier and steeper contribution decline, increasing the likelihood of abrupt performance cliffs when transitions are delayed. Together, these findings support proactive reallocation and succession planning rather than reactive correction.



---

## Recommendations

- Reallocate spend away from high-cost assets where statistically comparable substitutes exist within the same functional archetype
- Reduce dependency risk by distributing contribution across multiple archetypes rather than concentrating output within a narrow profile
- Prioritize early transition planning for high-usage roles with elevated aging exposure
- Monitor borderline assets closely due to higher role instability and evaluation risk
- Use similarity analysis as a screening layer for portfolio optimization and replacement planning decisions

---

## Assumptions & Caveats

- Contribution metrics favor higher-usage profiles and may understate low-volume efficiency
- Analysis is based on season-level data and does not capture short-term variance
- Cost figures are treated as external context rather than modeled inputs
- Results are descriptive and intended to inform decision-making, not guarantee outcomes

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
