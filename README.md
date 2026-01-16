# NBA Team Building & Roster Optimization
### *A Data-Driven Framework for Resource Allocation and Role Replacement*

---

## 🏀 Project Overview
This project applies a **Moneyball-style analytical framework** to NBA roster construction. Instead of evaluating players in isolation, this analysis treats a roster as a **system** where performance emerges from role fit, usage allocation, and lineup balance. 

The goal is to support data-driven roster strategy, trade evaluation, and recruitment decisions under real-world constraints such as salary caps and role redundancy.

---

## 💼 Business Problem
NBA front offices face a recurring strategic challenge: **How can a team compete effectively when star players are scarce, expensive, or injured?**

Traditional evaluation methods often:
* **Overweight** raw points and high-usage statistics.
* **Undervalue** defense, efficiency, and off-ball impact.
* **Miss** how multiple role players can collectively replace a star’s output.

This project reframes roster building as a **resource allocation problem**, rather than a talent ranking exercise.

---

##  Analytical Approach
The analysis is built upon four core methodological pillars:

* **Role-Based Player Evaluation:** Players are evaluated relative to their specific role (usage, efficiency, defensive contribution) rather than absolute star metrics.
* **Value Normalization:** Player output is adjusted for minutes, usage, and opportunity to avoid overvaluing high-volume players and identifying "hidden" efficiency.
* **Roster Gap Diagnostics:** Team-level metrics identify where roster construction is unbalanced (e.g., offense-heavy, defense-light, or aging cores).
* **Replacement Logic:** Utilizes the **Moneyball principle** to test whether the combined output of multiple role players can approximate or exceed a star player’s contribution.

---

##  Key Questions Answered
* Which players provide the highest impact relative to their **usage rates**?
* Which teams rely too heavily on a small number of players, creating **operational fragility**?
* Where do rosters lack balance in terms of skill mix, age, and defensive presence?
* Which **undervalued players** are the best fit to fill specific team gaps?

---

##  Key Insights
* **Roster Balance:** Team success is often driven by the synergy of role players rather than just star concentration.
* **Invisible Impact:** Several low-usage players deliver a strong per-minute impact that is invisible in traditional rankings but critical for winning.
* **Fragility Analysis:** Over-reliance on stars increases risk under injury, fatigue, and shortened playoff rotations.
* **Collective Replacement:** Role-specialized players can collectively replace star output when minutes are reallocated intelligently.

---

##  Tools & Skills Demonstrated
* **Data Cleaning & Feature Engineering:** Preparing complex sports datasets for analysis.
* **Role-Based Metric Design:** Creating custom KPIs to measure player archetypes.
* **Comparative Analysis:** Benchmarking players against peers and league averages.
* **Team Diagnostics:** Identifying organizational-level strengths and weaknesses.
* **Analytical Storytelling:** Framing technical data as actionable strategy for decision-makers.

---

##  Assumptions & Limitations
* Analysis is based on historical regular-season data.
* Contract and cap mechanics are simplified for clarity.
* Metrics focus on measurable on-court contribution, excluding "intangible" factors.

> **Note:** Notebook filenames (e.g., Untitled / numeric IDs) are preserved from the original interactive environment to maintain reproducibility and content integrity.

📊 Tableau Public Dashboard
→ See interactive roster comparisons and player role distributions
https://public.tableau.com/app/profile/austin.abraham5815/viz/NBAathleteyoungvsold/AgeDashboard

Youtube Project Walkthrough ( trade recommender part)
https://youtu.be/-bg97gmqsvw

Hugging face spaces nba app
https://huggingface.co/spaces/pharaohleft/nba-role-search

✍️ Substack Blog
→ Narrative walkthrough of insights and roster logic

https://pharaohleft.substack.com/p/data-driven-investigation-into-what
