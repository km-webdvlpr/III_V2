---
title: "JHB Municipal Infrastructure Intelligence"
date: 2026-03-28
summary: "Municipal analytics case study tracking pothole and water leak incidents across Johannesburg wards — built around SLA compliance, hotspot detection, and operational KPI reporting."
tags: ["Infrastructure Analytics", "Civic Data", "Python", "Data Visualization"]
featured: true
roleFocus: "Infrastructure Analytics | Civic Data"
projectShows:
  - "SLA and operational KPI design"
  - "Hotspot and ward-level analysis"
  - "Civic data storytelling"
snapshot:
  problem: "Municipal infrastructure data — potholes, burst pipes, water leaks — is fragmented across departments, making it difficult to prioritize repairs, monitor contractor SLA compliance, or identify repeat-incident zones before they become systemic failures."
  focus: "The project builds a Python-first analytics pipeline on synthetic, JHB-shaped incident data. The analytical focus is operational KPI design: response time, repair time, SLA breach rates, backlog trends, and geographic hotspot detection at ward and suburb level."
  outcome: "Infrastructure teams and civic decision-makers can review where backlogs are forming, which wards are underperforming on SLAs, and where repeat incidents signal systemic failure — with a dashboard that makes these signals immediately readable."
repo: "https://github.com/kabelo-analytics/jhb-infrastructure-intelligence"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/jhb-infrastructure-intelligence/"
demoLabel: "View live dashboard"
---

## Overview
JHB Municipal Infrastructure Intelligence is a portfolio-grade civic analytics project simulating how a City of Johannesburg infrastructure team could track and prioritize service delivery using evidence-based KPIs and a Python-driven analysis pipeline.

## Intelligence Layer
Johannesburg faces recurring infrastructure pressure: aging road surfaces, burst water mains, and reactive-only maintenance cycles. Without an analytics layer, ward managers and operations leads cannot distinguish systemic failure zones from isolated incidents — and cannot hold contractors accountable to SLA expectations.

## Problem
Municipal infrastructure data — potholes, burst pipes, water leaks — is fragmented across departments, making it difficult to prioritize repairs, monitor contractor SLA compliance, or identify repeat-incident zones before they become systemic failures.

## Data / Signals

### Analyst Objective
Design a Python analytics pipeline that enables infrastructure teams to:
- monitor SLA compliance by incident type, ward, and contractor,
- detect repeat-incident hotspots before they become systemic,
- and track backlog trends over time for prioritization.

### Stakeholders
- Ward managers needing operational visibility by area.
- Infrastructure operations leads monitoring contractor performance.
- Civic oversight teams requiring SLA compliance evidence.

### Key Questions
- Which wards have the highest SLA breach rates and why?
- Where are pothole and water leak incidents clustering into repeat-problem zones?
- What is the relationship between response time and resolution quality?
- How does backlog trend over time — and which contractor is contributing most to it?

### KPI Framework
- Response: median time-to-first-response (hours) by incident type and ward.
- Resolution: mean time-to-repair (days), SLA compliance rate, breach rate by contractor.
- Backlog: open incident count trend, repeat-incident rate per street and pipe zone.
- Hotspots: top 10 wards, suburbs, and streets by incident density and SLA breach frequency.

## Insight
- A relational synthetic dataset (200,000 rows) was structured to mirror real JHB operational patterns — messy, realistic, and BI-ready.
- A modular Python pipeline covers data generation, cleaning, EDA, KPI calculation, and hotspot detection across all pipeline stages.
- Analysis output is structured as an interactive HTML dashboard for immediate stakeholder readability.
- Every KPI output is framed around a specific operational decision — not just a description.

## Implication
- SLA breach rates varied significantly by contractor and ward, pointing to both resourcing gaps and accountability failures.
- Repeat-incident patterns in high-density wards indicated infrastructure asset deterioration, not random failure.
- Backlog trend analysis revealed that reactive-only maintenance creates compounding service debt over time.

## Closing

### Deliverables
- Python pipeline covering data generation, cleaning, EDA, and KPI output.
- Interactive HTML dashboard for operational and stakeholder review.
- Ward and suburb-level hotspot detection layer.
- KPI framework aligned to real municipal service delivery standards.

### Outcome
The project demonstrates how analyst-grade Python work translates into decision-ready civic intelligence — moving from raw incident logs to prioritized, SLA-aware, ward-level operational insight.

<div style="position:relative;height:78vh;min-height:620px;border:1px solid var(--border);border-radius:.45rem;overflow:hidden;background:var(--panel);margin-top:.75rem;">
  <iframe
    src="https://kabelo-analytics.github.io/jhb-infrastructure-intelligence/"
    title="JHB Municipal Infrastructure Intelligence"
    loading="lazy"
    style="width:100%;height:100%;border:0;"
  ></iframe>
</div>

### Link
- Live dashboard: [View live dashboard](https://kabelo-analytics.github.io/jhb-infrastructure-intelligence/)
- GitHub repo: [Open GitHub project](https://github.com/kabelo-analytics/jhb-infrastructure-intelligence)
