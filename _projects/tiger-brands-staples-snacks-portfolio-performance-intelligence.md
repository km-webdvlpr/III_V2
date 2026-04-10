---
title: "Tiger Brands: Staples & Snacks Portfolio Performance and Household Growth Intelligence"
date: 2026-04-04
summary: "FMCG manufacturer case study using synthetic household data to examine repeat purchase, basket-broadening behaviour, pack architecture, and promotion trade-offs in Gauteng."
tags: ["FMCG", "Commercial Intelligence", "Synthetic Data", "Portfolio Analytics"]
featured: true
roleFocus: "Commercial Intelligence | FMCG Portfolio Performance"
projectShows:
  - "Household repeat-purchase analysis"
  - "Cross-category lift modelling"
  - "Pack-size and promotion trade-off logic"
snapshot:
  problem: "Large household portfolios do not grow evenly, especially when repeat demand, basket role, pack fit, and promotion response pull in different directions."
  focus: "I built a synthetic Tiger Brands portfolio dataset to test how category role, pack-size fit, repeat purchase, and cross-category lift behave across Gauteng households."
  outcome: "The result is a portfolio model that helps sort stable demand from noisier growth signals and shows which lines are worth reviewing first."
repo: "https://github.com/km-webdvlpr/tiger-brands-portfolio-performance"
demo: "https://km-webdvlpr.github.io/tiger-brands-portfolio-performance/"
repoLabel: "Open GitHub project"
demoLabel: "Open live project"
---

## Overview
This case study looks at how Tiger Brands' staples and snacks portfolio performs in Gauteng households, with a focus on repeat purchase, cross-category lift, pack-size fit, and promotion quality.

## Business Context
Manufacturer portfolios do not grow on brand strength alone. Repeat purchase, pack fit, basket role, and promotional pressure all shape the quality of growth.

## Problem Statement
Tiger Brands needed a clearer view of which categories, product lines, and pack formats were creating more stable household behaviour, and where portfolio support should go once margin trade-offs are taken seriously.

## Analyst Objective
Build an FMCG portfolio case study that identifies where staples and snacks contribute to repeat demand, broader household baskets, and the clearest opportunities to investigate further in Gauteng.

## Stakeholders
- Category and commercial teams deciding where the portfolio needs stronger support.
- Consumer-insights teams evaluating how household behaviour differs across staples and snacks.
- Growth teams reviewing where pack architecture and promotions are helping or weakening portfolio quality.
- Leadership teams needing a clearer view of portfolio role beyond topline sales movement.

## Key Questions
- Which categories create the clearest repeat-purchase pattern?
- Which product lines contribute most to cross-category lift?
- How does pack format change by household size?
- Where are promotions helping demand, and where are they creating weaker trade-offs?
- Which Gauteng opportunities rank highest once repeat strength, basket participation, margin, and value are read together?

## Analysis Logic
- Staples should lead repeat purchase, but not every staple line should behave identically.
- Snacks should show stronger promo sensitivity and broader basket participation.
- Larger households should lean more heavily into family and value packs.
- Cross-category lift should help separate broader household missions from narrow volume spikes.

## KPI Framework
- Portfolio metrics: value contribution, volume units, average margin.
- Behaviour metrics: repeat purchase rate, cross-category lift, household-size fit.
- Commercial metrics: promo responsiveness, margin change, weighted growth score.

These metrics mattered because the project is designed as a synthetic decision-support model, not just a descriptive category summary.

## Approach
- Built a synthetic transaction-level FMCG dataset across Albany, Jungle, Bakers, Koo, and All Gold.
- Modelled category behaviour across bakery, grains and cereals, snacks, and culinary staples.
- Tested repeat purchase, cross-category lift, pack-size fit, and promotion effects.
- Ranked Gauteng opportunities using a weighted score built from repeat strength, basket participation, value contribution, and margin quality.

## Insights
- Grains & Cereals carries the highest repeat-purchase rate in the final model.
- Bakers is the clearest cross-category connector in the portfolio.
- Larger household formats play a visible role in repeat strength.
- Promotions create useful volume support, but the margin trade-off remains visible by category.
- The highest-ranked Gauteng opportunities sit where repeat demand and basket-broadening behaviour overlap.

## Deliverables
- Synthetic FMCG transaction dataset and supporting source tables
- Summary outputs across category, product line, repeat purchase, cross-category lift, promotions, and Gauteng growth
- Exported visuals and Jupyter notebook
- Published standalone project plus embedded portfolio case file

## Results
- Overall repeat purchase rate landed at 59.6%.
- Grains & Cereals delivered the strongest repeat-purchase performance.
- Bakers showed the highest cross-category lift in the final model.
- Jungle value pack ranked first in the Gauteng scoring model.

## Recommendations
- Keep staples at the centre of the portfolio review because they still carry the repeat base in the model.
- Use family and value packs more deliberately where household size supports them.
- Let snacks broaden the basket, but keep staples separate as the repeat anchor rather than asking every category to do the same job.
- Treat promotion support carefully in categories where uplift comes with weaker margin quality.

## Interpretation Notes
- This is a synthetic case study built to test portfolio decision logic, not a claim about Tiger Brands' real market performance.
- Cross-category lift in this project is a behavioural flag used to show when a line sits in a broader basket.
- The Gauteng ranking is a triage tool built from weighted inputs. It is useful for prioritisation, but it is not a final commercial answer.

## Embedded Project
<div style="position:relative;height:78vh;min-height:460px;border:1px solid var(--border);border-radius:.45rem;overflow:hidden;background:var(--panel);margin-top:.75rem;">
  <iframe
    src="https://km-webdvlpr.github.io/tiger-brands-portfolio-performance/"
    title="Tiger Brands: Staples & Snacks Portfolio Performance and Household Growth Intelligence"
    loading="lazy"
    style="width:100%;height:100%;border:0;"
  ></iframe>
</div>

## Links
- Live project: [Tiger Brands: Staples & Snacks Portfolio Performance and Household Growth Intelligence](https://km-webdvlpr.github.io/tiger-brands-portfolio-performance/)
- GitHub repo: [tiger-brands-portfolio-performance](https://github.com/km-webdvlpr/tiger-brands-portfolio-performance)
