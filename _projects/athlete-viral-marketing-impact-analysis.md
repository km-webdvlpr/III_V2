---
title: "Athlete-Led Viral Marketing — Impact Analysis"
date: 2026-03-28
summary: "Analytics case study examining whether an athlete-led viral campaign converted reach into gym memberships — across channels, funnel stages, brand lift signals, and offline behaviour."
tags: ["Campaign Analytics", "Python", "Power BI", "Funnel Analysis"]
featured: true
roleFocus: "Campaign Analytics | Product Analytics"
projectShows:
  - "Multi-channel campaign attribution and efficiency analysis"
  - "Full funnel conversion from impressions to memberships"
  - "Brand lift and offline behaviour measurement"
snapshot:
  problem: "Wellness brands investing in athlete-led viral campaigns face a measurement challenge: reach metrics spike, but it is rarely clear how much of that reach converts into actual product adoption. Without a structured analytics layer, spend decisions default to gut feel and last-click attribution — both of which distort the true channel contribution picture."
  focus: "The project structures a synthetic but realistic campaign dataset into a full analytics pipeline — from raw channel data through to funnel conversion rates, cost-per-acquisition by channel, brand lift tracking, and offline gym activity signals. The data model is built for Power BI consumption and designed to answer real marketing accountability questions."
  outcome: "Stakeholders can review channel efficiency beyond impressions, understand where in the funnel spend is most effective, and see how brand awareness translates — with a lag — into offline membership behaviour."
repo: "https://github.com/kabelo-analytics/athlete-viral-marketing-impact-analysis"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/"
demoLabel: "View live dashboard"
---

## Overview
Athlete-Led Viral Marketing Impact Analysis is a product analytics case study examining a TikTok-anchored wellness campaign. The analysis moves from reach metrics through conversion efficiency to brand lift and offline signals — using a star-schema data model built for direct BI tool consumption.

## Intelligence Layer
Brands routinely over-index on reach when evaluating influencer and athlete campaigns. Impressions are visible and immediate; conversion and brand lift are delayed and harder to attribute. This project builds the measurement framework that sits between campaign activity and acquisition outcomes.

## Problem
Wellness brands investing in athlete-led viral campaigns face a measurement challenge: reach metrics spike, but it is rarely clear how much of that reach converts into actual product adoption. Without a structured analytics layer, spend decisions default to gut feel and last-click attribution — both of which distort the true channel contribution picture.

## Data / Signals

### Analyst Objective
Structure campaign data to enable marketing and product teams to:
- determine which channels drove reach versus which drove efficient acquisition,
- identify where in the funnel conversion broke down by channel,
- and measure brand lift and offline behaviour signals relative to campaign timing.

### Stakeholders
- Marketing leads evaluating channel ROI and spend reallocation decisions.
- Product teams tracking acquisition funnel health and conversion benchmarks.
- Finance and partnerships teams requiring cost-per-acquisition evidence.

### Key Questions
- Did TikTok's reach volume translate into proportional acquisition volume?
- Which channel had the lowest cost per gym membership?
- How long was the consideration-to-action lag between campaign exposure and offline behaviour?
- What does the brand search index tell us about awareness that conversion metrics miss?

### KPI Framework
- Reach: impressions, CTR by channel and date.
- Conversion: signup rate, trial rate, membership rate through funnel stages.
- Efficiency: CPA (spend / memberships) by channel.
- Brand: brand search index trend across pre, during, and post-campaign windows.
- Offline: gym visits and new membership trend relative to campaign timeline.

## Insight
- TikTok delivered the highest reach volume but the weakest direct conversion efficiency — consistent with its role as an upper-funnel awareness channel.
- Paid search and email produced the lowest cost-per-membership despite significantly lower impression volumes.
- Brand search index showed a measurable uplift during the campaign window — suggesting awareness was building even where immediate conversion was not occurring.
- Offline gym activity spiked approximately two weeks post-campaign, consistent with a consideration-to-action lag typical of wellness product adoption.

## Implication
- Last-click attribution significantly undervalues TikTok's contribution to the overall acquisition picture.
- Budget optimisation should evaluate upper-funnel channels on brand lift and assisted conversion, not direct CPA alone.
- The two-week offline lag is a predictable signal — one that could be modelled forward to improve campaign timing and crew readiness for membership intake surges.

## Closing

### Deliverables
- Python data pipeline covering synthetic data generation, cleaning, and feature engineering.
- Star-schema data model ready for Power BI consumption.
- Interactive HTML dashboard for stakeholder review.
- KPI framework covering reach, conversion, efficiency, brand lift, and offline signals.

### Outcome
The project demonstrates how structured campaign analytics moves beyond vanity metrics — connecting reach, conversion, brand lift, and offline behaviour into a single coherent measurement framework.

<div style="position:relative;height:78vh;min-height:620px;border:1px solid var(--border);border-radius:.45rem;overflow:hidden;background:var(--panel);margin-top:.75rem;">
  <iframe
    src="https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/"
    title="Athlete-Led Viral Marketing Impact Analysis"
    loading="lazy"
    style="width:100%;height:100%;border:0;"
  ></iframe>
</div>

### Link
- Live dashboard: [View live dashboard](https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/)
- GitHub repo: [Open GitHub project](https://github.com/kabelo-analytics/athlete-viral-marketing-impact-analysis)
