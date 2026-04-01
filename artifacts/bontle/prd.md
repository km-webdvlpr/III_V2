---
layout: artifact
title: "Bontle | PRD Summary"
description: "Reconstructed product requirements document for the Bontle case study."
projectTitle: "Bontle: Operational Intelligence for Service Teams"
artifactLabel: "PRD Summary"
caseStudyHref: "/projects/bontle-operational-intelligence-for-service-teams"
---

## Product Purpose
This document captures the product requirements behind Bontle as an operational workflow system. The emphasis is on how users interact with the workflow, how management visibility is created, and how the product supports live service delivery rather than only retrospective reporting.

## Product Vision
Bontle was designed to help service teams manage live work through a clear operational flow. The product needed to support frontline execution, operations review, and leadership reporting from the same workflow foundation.

## User Types
### Customer
Creates or confirms a booking through the customer-facing booking journey.

### Consultant
Handles assigned work and needs clarity on what is owned, active, and complete.

### Admin or Operations User
Monitors queue conditions, exceptions, reassignment, and branch flow.

### Leadership User
Needs a summarised but reliable view of service performance across locations.

## Product Problem
A booking interface alone does not solve operational visibility. Once work is booked, the business still needs to know how that work moves, where it gets delayed, how ownership changes, and which patterns are affecting service output.

## Product Workflow
1. Customer creates a booking through the front-end interface.
2. The booking enters the operating workflow.
3. The item is owned, progressed, reassigned, or completed through defined states.
4. Managers monitor queue position, exceptions, and branch-level conditions.
5. Reporting reflects actual workflow movement, not reconstructed manual summaries.

## Core Product Requirements
- Work items must move through clearly defined states.
- State transitions must be role-aware and operationally valid.
- Ownership changes must be visible.
- Managers must be able to identify stalled work and queue pressure quickly.
- Branch views must support comparison without requiring manual reconciliation.
- Reporting must reflect live workflow history.

## Front-End and User Experience Requirements
- The customer booking experience must remain simple and mobile-friendly.
- Consultant and admin views must prioritise clarity over visual noise.
- Users should understand the current state of work without digging through multiple screens.
- Queue and workflow views should support fast triage rather than passive observation.

## Functional Requirements
- booking creation
- state transition management
- assignment and reassignment handling
- queue filtering and branch views
- export and reporting support
- role-based access and visibility

## Edge Cases
- reassignment after work has started
- duplicate or repeated actions
- partially completed work
- queue concentration in one branch
- delay without explicit reassignment

## Acceptance Criteria
- Work can move through valid workflow states with preserved history.
- Admin and operations users can identify stalled or delayed items quickly.
- Branch performance views can be compared using shared definitions.
- KPI reporting can be produced from workflow data without manual reconstruction.
- The product supports both operating use and management review.

## Product Measures
- throughput by state
- backlog age
- reassignment frequency
- completion timing
- queue pressure by branch

## Product Recommendation
The product should continue to evolve as an operational control system rather than as a simple booking application. The strongest product value comes from the combination of workflow visibility, queue management, and reporting derived from actual process movement.
