# nba-team-building-analytics

Note: Notebook filenames (e.g., Untitled / numeric IDs) are preserved from the original interactive environment to prevent content loss and maintain reproducibility.

Overview

This project applies a Moneyball-style analytical framework to NBA roster construction, focusing on how teams can maximize on-court value by identifying undervalued role players rather than over-investing in individual star talent.

Instead of evaluating players in isolation, the analysis treats a roster as a system — where performance emerges from role fit, usage allocation, and lineup balance.

The goal is to support data-driven roster strategy, trade evaluation, and recruitment decisions under real-world constraints such as salary caps, playing time, and role redundancy.

Business Problem

NBA teams face a recurring strategic challenge:

How can a team compete effectively when star players are scarce, expensive, or injured?

Traditional evaluation methods often:

Overweight raw points and usage

Undervalue defense, efficiency, and off-ball impact

Miss how multiple role players can collectively replace a star’s output

This project reframes roster building as a resource allocation problem, not a talent ranking exercise.

Analytical Approach

The analysis follows four core ideas:

Role-based player evaluation
Players are evaluated relative to their role (usage, efficiency, defensive contribution), not absolute star metrics.

Value normalization
Player output is adjusted for minutes, usage, and opportunity to avoid overvaluing high-volume players.

Roster gap diagnostics
Team-level metrics identify where roster construction is unbalanced (e.g., offense-heavy, defense-light, aging core).

Replacement logic (Moneyball principle)
Tests whether the combined output of multiple role players can approximate or exceed a star player’s contribution when minutes are redistributed.

Key Questions Answered

Which players provide high impact relative to their usage?

Which teams rely too heavily on a small number of players?

Where do rosters lack balance (offense vs defense, size, age, skill mix)?

Which undervalued players could fill specific team gaps?

How do alternative roster constructions change projected team strength?

Key Insights

Team success is often driven by roster balance, not star concentration.

Several low-usage players deliver strong per-minute impact that is invisible in traditional rankings.

Over-reliance on stars increases fragility under injuries, fatigue, and playoff rotations.

Role-specialized players can collectively replace star output when minutes are reallocated intelligently.

Tools & Skills Demonstrated

Data cleaning & feature engineering

Role-based metric design

Comparative player analysis

Team-level diagnostics

Analytical storytelling & decision framing

Assumptions & Limitations

Analysis is based on historical regular-season data.

Contract and cap mechanics are simplified for clarity.

Metrics focus on measurable on-court contribution, not intangibles.

Outputs

📊 Tableau Public Dashboard
→ See interactive roster comparisons and player role distributions
https://public.tableau.com/app/profile/austin.abraham5815/viz/NBAathleteyoungvsold/AgeDashboard


Huggine face spaces nba app
https://huggingface.co/spaces/pharaohleft/nba-role-search

✍️ Substack Blog
→ Narrative walkthrough of insights and roster logic

https://pharaohleft.substack.com/p/data-driven-investigation-into-what
