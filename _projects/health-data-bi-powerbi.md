---
title: "Health Data BI Dashboard"
date: 2025-11-10
summary: "Healthcare analytics case study using Power BI to explore cardiovascular risk patterns — structured EDA across patient demographics, clinical indicators, and outcome distributions."
tags: ["Power BI", "EDA", "Healthcare Analytics"]
featured: true
roleFocus: "Healthcare Analytics | EDA"
projectShows:
  - "EDA structure and clinical KPI design"
  - "Demographic and risk factor breakdowns"
  - "BI dashboard design for non-technical stakeholders"
snapshot:
  problem: "Clinical patterns in cardiovascular data were not visible to non-technical stakeholders without a structured analytical and reporting layer."
  focus: "The project structures patient risk profiles, demographic distributions, and clinical indicators into an interactive Power BI dashboard built on a cleaned, modelled dataset."
  outcome: "Non-technical reviewers can explore cardiovascular risk patterns across age, sex, chest pain type, and clinical indicator dimensions without relying on raw data exports."
repo: "https://github.com/kabelo-analytics/health-data-bi-powerbi"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/health-data-bi-powerbi/"
demoLabel: "View live dashboard"
---

## Overview
Health Data BI Dashboard is a healthcare analytics case study that translates anonymised cardiovascular patient data into an interactive Power BI report structured for exploratory use by non-technical stakeholders.

## Intelligence Layer
Clinical datasets contain high-value diagnostic signals — age bands, chest pain type, resting blood pressure, ST depression, max heart rate — that are invisible to non-technical teams without a structured reporting layer. Without a BI interface, exploration depends on data literacy that most operational or clinical reviewers do not have.

## Problem
Clinical patterns in cardiovascular data were not visible to non-technical stakeholders without a structured analytical and reporting layer. The dataset contained informative variables but no interpretation layer to surface risk distributions, demographic patterns, or indicator separations between positive and negative cases.

## Data / Signals

### Analyst Objective
Build a structured EDA layer and interactive Power BI dashboard that enables non-technical teams to:
- explore cardiovascular risk distributions across demographic and clinical dimensions,
- identify which indicators most clearly differentiate positive from negative cases,
- and review patterns without prior clinical or data literacy.

### Stakeholders
- Clinical or health operations teams needing a clear view of patient risk profiles.
- Non-technical reviewers needing filterable visuals without relying on raw data.
- Analytics teams needing a consistent data model and reliable EDA foundation.

### Key Questions
- Which demographic and clinical variables most clearly differentiate positive from negative cardiovascular cases?
- How do risk indicators vary across age groups and sex?
- Where do chest pain type and ST depression add the most diagnostic signal?
- How can multi-variable patterns be made accessible to a non-clinical audience?

### KPI Framework
- Patient cohort: total records, positive case rate, age distribution, sex split.
- Clinical indicators: average resting BP, average max heart rate, fasting blood sugar prevalence, cholesterol by outcome.
- Risk signals: ST depression spread, chest pain type breakdown, age-band prevalence rates.

## Insight
- A cleaned, anonymised cardiovascular dataset was modelled into a star schema with calculated columns and DAX measures to support filter-driven KPI views.
- Power Query handled type standardisation, null handling, and preparation before model load.
- R Script visuals were integrated for distribution analysis beyond standard Power BI chart types.
- Dashboard structure moves from high-level cohort overview into demographic and clinical breakdowns, with each page framed around a specific analytical question.

## Implication
- Positive cases concentrated in the 55–65 age band — age is the strongest single demographic predictor in the dataset.
- Asymptomatic chest pain presentation carried the highest positive diagnosis rate across all chest pain types, making it the most informative symptomatic variable.
- ST depression above 2.0 aligned strongly with positive outcomes — oldpeak is the clearest single clinical separator in the dataset.
- Serum cholesterol showed limited separation between groups on its own, becoming more informative only when combined with resting BP and ST depression.

## Closing

### Deliverables
- Cleaned and modelled cardiovascular health dataset.
- Power Query transformation steps and preparation logic.
- DAX measures for KPI cards and cross-dimensional analysis.
- Interactive Power BI report covering demographic and clinical breakdowns.
- R Script visual integration for statistical distribution plots.

### Outcome
The project demonstrates structured EDA thinking applied to healthcare data — moving from raw clinical variables to a filterable, interpretation-ready dashboard that non-technical stakeholders can explore independently.

<div style="position:relative;height:78vh;min-height:620px;border:1px solid var(--border);border-radius:.45rem;overflow:hidden;background:var(--panel);margin-top:.75rem;">
  <iframe
    src="https://kabelo-analytics.github.io/health-data-bi-powerbi/"
    title="Health Data BI Dashboard"
    loading="lazy"
    style="width:100%;height:100%;border:0;"
  ></iframe>
</div>

### Link
- Live dashboard: [View live dashboard](https://kabelo-analytics.github.io/health-data-bi-powerbi/)
- GitHub repo: [Open GitHub project](https://github.com/kabelo-analytics/health-data-bi-powerbi)
