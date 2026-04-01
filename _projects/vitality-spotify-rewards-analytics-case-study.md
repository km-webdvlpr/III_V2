---
title: "Vitality × Spotify Rewards — Product Analytics"
date: 2026-03-28
summary: "Product analytics case study modelling a Vitality-style rewards partnership with Spotify Africa — measuring whether music engagement incentives drive activity improvements and member retention."
tags: ["Product Analytics", "Retention", "Python", "Power BI", "Rewards"]
featured: true
roleFocus: "Product Analytics | Rewards & Retention"
projectShows:
  - "Pilot measurement design with pre and post cohort analysis"
  - "Retention and engagement analytics for rewards programmes"
  - "Selection bias documentation and transparent limitation framing"
snapshot:
  problem: "Rewards programmes that integrate lifestyle products face a fundamental measurement question — do the rewards change behaviour, or do they simply attract members who were already active? Without a structured pilot framework and bias controls, programme ROI claims rest on shaky ground."
  focus: "The project designs a 12-week pilot measurement framework to evaluate whether a Spotify integration drives measurable improvements in physical activity and retention. The analysis includes bias documentation, cohort comparison, and a warehouse-style data model built for Power BI."
  outcome: "Product and partnerships teams can review engagement and retention deltas with appropriate context — understanding not just what the data shows, but where the measurement limitations sit and what a stronger experimental design would require."
repo: "https://github.com/kabelo-analytics/vitality-spotify-rewards-analytics-case-study"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/vitality-spotify-rewards-analytics-case-study/"
demoLabel: "View live dashboard"
---

## Overview
Vitality × Spotify Rewards is a product analytics case study simulating a wellness-music partnership. The analytical focus is pilot evaluation — measuring behavioural change, documenting selection bias risks, and translating findings into actionable product recommendations.

## Intelligence Layer
Opt-in reward designs are structurally prone to selection bias. Members who choose to activate rewards are rarely representative of the full base. A credible analytics layer surfaces this risk explicitly rather than papering over it.

## Problem Statement
Rewards programmes that integrate third-party lifestyle products face a core measurement challenge — do rewards change behaviour, or do they attract members who were already active? Without a structured pilot framework and bias controls, programme ROI claims rest on shaky ground.

## Analyst Objective
Design a 12-week pilot measurement framework to evaluate whether a Spotify Africa integration drives measurable improvements in physical activity and retention. Document bias risks and translate findings into concrete programme design recommendations.

## Stakeholders
- Product owner (engagement and habit loop design)
- Partnerships lead (commercial ROI)
- Analytics lead (measurement integrity)
- Marketing (segment targeting)

## Key Questions
- Did reward activation correlate with activity score improvements above baseline?
- Was retention materially higher in the reward-engaged cohort at 8 weeks?
- How much of the observed difference is explained by pre-existing activity level differences?
- Which member segments respond most strongly to the reward?

## KPI Framework
- Spotify streams pre vs post activation
- Weekly activity score delta from baseline
- Monthly cohort retention rate by engagement tier
- Baseline equivalence test between opt-in and control cohorts
- Cost-per-active-member by reward tier

## Approach
- Designed a 12-week pilot with opt-in cohort vs control group structure.
- Built a warehouse-style star schema data model (dim_member, dim_week, dim_month, dim_reward, dim_content_category; fact tables for activity, Spotify, campaign exposure, reward events, retention).
- Generated analysis-ready outputs: member_week_pilot.csv and member_summary.csv.
- Ran baseline equivalence tests to document selection bias before comparing cohort outcomes.
- Produced Python pipeline covering data generation, cleaning, and feature engineering.

## Insights
Reward-engaged members showed higher post-pilot activity scores relative to their own baseline. Retention was notably higher at 8 weeks in the engaged cohort. Baseline testing confirmed opt-in members were already more active — selection bias is a documented confounding factor. The reward performs best as a retention tool, not an activation lever.

## Implication
A tiered reward structure targeting different engagement segments would sharpen programme impact. Inactive segments require a different intervention. A randomised design in a future pilot would allow causal rather than directional attribution.

## Deliverables
- Warehouse-style star schema data model for Power BI
- Python pipeline covering data generation, cleaning, and feature engineering
- 12-week pilot evaluation framework with cohort comparison
- Interactive HTML dashboard for stakeholder review

## Results
The project demonstrates rigorous product analytics thinking — building a measurement framework that surfaces its own limitations and translates findings into concrete programme design recommendations.

## Links
- Live dashboard: [Vitality × Spotify Rewards Dashboard](https://kabelo-analytics.github.io/vitality-spotify-rewards-analytics-case-study/)
- GitHub: [vitality-spotify-rewards-analytics-case-study](https://github.com/kabelo-analytics/vitality-spotify-rewards-analytics-case-study)
