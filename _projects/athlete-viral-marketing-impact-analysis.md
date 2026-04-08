---
title: "Athlete-Led Viral Marketing - Impact Analysis"
date: 2026-03-28
summary: "Analytics case study examining how an athlete-led viral campaign moved reach, conversion, brand lift, and offline membership activity in a synthetic marketing scenario."
tags: ["Campaign Analytics", "Python", "Power BI", "Funnel Analysis"]
featured: true
roleFocus: "Campaign Analytics | Product Analytics"
projectShows:
  - "Multi-channel campaign efficiency analysis"
  - "Funnel measurement from impressions to memberships"
  - "Brand lift and offline behaviour tracking"
snapshot:
  problem: "Wellness brands investing in athlete-led viral campaigns face a measurement challenge: reach can spike while the path to signups, trials, and memberships stays unclear. Without a structured measurement view, teams can over-index on top-line reach or over-credit the final conversion touchpoint."
  focus: "The project packages a synthetic campaign dataset into raw and processed tables for channel comparison, funnel analysis, brand lift tracking, and offline gym activity monitoring. The reporting layer is designed to help stakeholders separate media efficiency, conversion handoff, and timing effects."
  outcome: "Stakeholders can compare reach against downstream conversion, isolate spend-bearing channel efficiency, and track how brand search and offline membership activity move around the campaign launch window."
repo: "https://github.com/kabelo-analytics/athlete-viral-marketing-impact-analysis"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/"
demoLabel: "View live dashboard"
---

## Overview
Athlete-Led Viral Marketing Impact Analysis is a product analytics case study examining a TikTok-anchored wellness campaign. The analysis moves from reach metrics through conversion efficiency to brand lift and offline signals using a Power BI-friendly packaged dataset built around channel, period, and proxy tables.

## Intelligence Layer
Brands routinely over-index on reach when evaluating influencer and athlete campaigns. Impressions are visible and immediate; downstream conversion and offline response are harder to interpret. This project builds a measurement layer that helps separate scale, efficiency, and timing effects.

## Problem
Wellness brands investing in athlete-led viral campaigns face a measurement challenge: reach metrics spike, but it is rarely clear how much of that attention converts into actual product adoption. Without a structured analytics layer, teams can over-index on reach or over-credit the final conversion touchpoint.

## Data / Signals

### Analyst Objective
Structure campaign data to enable marketing and product teams to:
- determine which channels drove reach versus which converted that reach more efficiently,
- identify where in the funnel conversion weakened by channel,
- and measure brand lift and offline behaviour signals relative to campaign timing.

### Stakeholders
- Marketing leads evaluating channel ROI and spend reallocation decisions.
- Product teams tracking acquisition funnel health and conversion benchmarks.
- Finance and partnerships teams requiring cost-per-membership evidence from spend-bearing channels.

### Key Questions
- Did TikTok's reach volume translate into proportional acquisition volume?
- Which spend-bearing channel had the lowest reported cost per gym membership?
- When did offline membership activity peak relative to the campaign window?
- What does the brand search index tell us about awareness that conversion metrics miss?

### KPI Framework
- Reach: impressions, CTR by channel and date.
- Conversion: signup rate, trial rate, membership rate through funnel stages.
- Efficiency: CPA (spend / memberships) for spend-bearing channels, with Website treated separately as a conversion destination.
- Brand: brand search index trend across pre, during, and post-campaign windows.
- Offline: gym visits and new membership trend relative to campaign timeline.

## Insight
- TikTok delivered by far the highest reach volume and the largest absolute membership volume, but its membership-per-click trailed Website, Instagram, and YouTube.
- Among spend-bearing channels in this synthetic dataset, TikTok posted the lowest reported CPA, while Website functioned as the strongest conversion destination rather than a comparable media channel.
- Brand search index showed a clear uplift during the campaign window relative to the pre-campaign baseline.
- Offline membership activity spiked early in the campaign window, indicating demand concentrated around launch rather than appearing on a fixed two-week lag.

## Implication
- Separate media efficiency from destination conversion in reporting; Website should not be interpreted as a media buy.
- Evaluate TikTok on scale, downstream handoff, and total membership contribution alongside direct conversion metrics.
- Plan staffing and follow-up offers around the launch week and immediate post-launch period, where offline demand was strongest in this scenario.

## Closing

### Deliverables
- Packaged raw and processed CSV tables for synthetic campaign analysis.
- Power BI-friendly data model centred on `fact_channel_daily` plus supporting dimension and proxy tables.
- Interactive HTML dashboard for stakeholder review.
- KPI framework covering reach, conversion, efficiency, brand lift, and offline signals.

### Outcome
The project demonstrates how structured campaign analytics can move beyond vanity metrics by comparing reach, downstream conversion, brand lift, and offline behaviour in one measurement framework.

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
