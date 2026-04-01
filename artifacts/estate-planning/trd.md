---
layout: artifact
title: "Estate Planning | TRD Summary"
description: "Reconstructed technical requirements document for the estate planning case study."
projectTitle: "Digitising Estate Planning for Emerging Households"
artifactLabel: "TRD Summary"
caseStudyHref: "/projects/digitising-estate-planning-for-emerging-households"
---

## Technical Purpose
This document captures the main technical requirements behind the estate planning concept. It focuses on how the system would support guided intake, validation, document generation, delivery, and basic operational traceability.

## Technical Objective
Support a guided digital journey that can reliably:
- capture structured user input
- validate required data before progression
- generate a document from captured data
- deliver the output
- retain enough traceability for review and support

## Solution Overview
The proposed technical flow was built around a messaging interface connected to backend services responsible for workflow control, validation, and document output. The system was intended to separate conversation handling, logic enforcement, and document generation so that each part could be monitored and managed more clearly.

## Core Components
### Interaction Layer
Handles the guided user conversation and step-by-step progression through the process.

### Validation Layer
Checks completeness, required formats, and progression logic before a user can move forward.

### Document Generation Layer
Transforms structured data into a formatted will document.

### Delivery Layer
Handles final email delivery of the completed output.

### Logging and Traceability
Records process state, failures, and completion events to support review and operational follow-up.

## Functional Requirements
- The system must capture structured inputs by stage.
- The system must know which fields are required before document creation.
- Invalid or incomplete submissions must be blocked from final output generation.
- The system must generate a document from valid structured inputs.
- The system must trigger email delivery after successful generation.
- The system must record key process events for review.

## Data Requirements
- Inputs must be stored in a way that supports both validation and document formatting.
- Required fields must be identifiable by process stage.
- Process state must remain traceable from first interaction through final delivery.
- Failure events must be logged with enough detail for troubleshooting.

## Validation Rules
- required fields must be present before the user advances past key stages
- formatting rules must be applied where inputs require standardisation
- contradictory or incomplete data must block final output generation
- the system should distinguish between recoverable validation issues and hard-stop failures

## Delivery and Error Handling
- successful generation must trigger a delivery event
- failed delivery should be logged separately from generation failure
- incomplete sessions should remain visible for operational review
- the system should support basic retry or intervention handling where practical

## Security and Compliance Considerations
- personal data must be handled carefully and only stored where needed
- access to submitted user information should be restricted to appropriate roles or operational contexts
- traceability should not compromise privacy requirements

## Operational Monitoring
- number of journeys started
- number completed
- validation failure points
- generation success and failure
- delivery success and failure

## Technical Constraints
- the solution must stay lightweight enough for a first working version
- legal review requirements may affect how documents are finalized
- the system needs to prioritise reliability and clarity over technical complexity

## Technical Recommendation
The technical design should remain modular and practical. The priority is not building a large platform at first. The priority is building a reliable guided flow with clear validation, clean output generation, and enough operational visibility to improve the process over time.
