---
title: "Jozication LMS Insights"
date: 2026-03-22
summary: "Learning analytics case study focused on funnel reporting, completion, retention, and course-level performance in a synthetic LMS dataset."
tags: ["Education Analytics", "LMS", "Product Analytics", "Reporting"]
featured: true
roleFocus: "Learning Analytics | Product Reporting"
projectShows:
  - "KPI definition"
  - "Funnel analysis"
  - "Reporting clarity"
snapshot:
  problem: "LMS reporting was spread across engagement, completion, and retention metrics without a clear view of where learner loss was actually happening."
  focus: "I used a synthetic LMS dataset and reporting exports to build a single walkthrough covering activation, completion, retention, course performance, and learner segments."
  outcome: "The case study makes the main bottlenecks easier to see, especially early drop-off between enrollment and course start."
repo: "https://github.com/kabelo-analytics/Jozication-LMS-insights"
repoLabel: "Open GitHub project"
demo: "https://kabelo-analytics.github.io/Jozication-LMS-insights/"
demoLabel: "View project walkthrough"
---

## Overview
Jozication LMS Insights is a reporting-focused learning analytics case study. It uses a synthetic LMS dataset to show how an analyst might turn enrollment, engagement, completion, and retention data into a more usable view for academic and programme teams.

## Problem
The core issue was not lack of data. It was lack of a clear reporting layer. Teams could see enrollment counts, course outcomes, and activity signals, but not in a way that made the main bottlenecks obvious.

## Data / Signals
### Analyst Objective
Build a clear reporting structure that helps teams:
- compare activation, engagement, completion, and retention in one place,
- spot where learners are falling out of the journey,
- and review course and segment patterns without needing SQL or raw exports.

### Stakeholders
- Academic leads reviewing cohort and course performance.
- Facilitators tracking learner follow-through.
- Programme managers deciding where intervention effort should go first.

### Key Questions
- Where is the largest loss in the learner journey?
- Which courses underperform on completion and satisfaction?
- How do device, region, and age group relate to outcomes?
- Which metrics are reliable enough for regular reporting?

### KPI Framework
- Funnel: enrollments, starts, active learners, completions.
- Retention: checkpoint-based return rates, especially Day 30.
- Course performance: completion, engagement, satisfaction.
- Segmentation: broad differences by device, region, and age group.

## Insight
- The largest funnel loss happens before course start, not later in the learning journey.
- Completion is much stronger among learners who move into active learning.
- Advanced courses underperform beginner courses in the current synthetic model.
- Mobile learners trail desktop learners on completion and engagement.

## Implication
- Activation is the clearest operational pressure point in this version of the model.
- Course design and support should be reviewed more closely for advanced content than for beginner content.
- Segment views are useful for broad patterns, but very small segment cells should not drive strong decisions.

## Closing
### Deliverables
- Synthetic LMS dataset in SQLite and CSV form.
- SQL analysis outputs covering funnel, retention, segmentation, and drop-off.
- Static walkthrough page for stakeholder-style review.
- Repo documentation explaining the metric logic and reporting limits.

### Outcome
The project is strongest as a clear reporting case study. It shows how to define metrics carefully, surface the biggest learner-loss points, and present the results in a format that is easier to review than raw query output.

### Embedded Project
<div style="position:relative;height:78vh;min-height:620px;border:1px solid var(--border);border-radius:.45rem;overflow:hidden;background:var(--panel);margin-top:.75rem;">
  <iframe
    src="https://kabelo-analytics.github.io/Jozication-LMS-insights/"
    title="Jozication LMS Insights"
    loading="lazy"
    style="width:100%;height:100%;border:0;"
  ></iframe>
</div>

### Link
- Case project: [Jozication LMS Insights](https://kabelo-analytics.github.io/Jozication-LMS-insights/)
- GitHub repo: [Open GitHub project](https://github.com/kabelo-analytics/Jozication-LMS-insights)
