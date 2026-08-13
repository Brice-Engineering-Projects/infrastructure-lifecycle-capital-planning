# Infrastructure Asset Risk Assessment Plan

**Client:** [Municipality / Utility Name]  
**Department:** [Department / Utility Division]  
**Asset System:** [Water / Wastewater / Stormwater / Facilities / Transportation]  
**Project:** [Project Name]  
**Prepared By:** [Consultant / Engineering Firm]  
**Date:** [Date]  
**Revision:** [Revision Number]  

---

## 1. Executive Summary

This Risk Assessment Plan establishes a consistent framework for evaluating, prioritizing, and managing risks associated with the [Municipality's] infrastructure assets.

The assessment is intended to support:

* Capital improvement planning;
* Asset renewal and replacement decisions;
* Operations and maintenance planning;
* Reliability and resiliency improvements;
* Emergency preparedness;
* Regulatory compliance;
* Budget prioritization; and
* Long-term infrastructure investment decisions.

Risk is evaluated using the relationship between the **Probability of Failure (PoF)** and the **Consequence of Failure (CoF)**.

$$
Risk = PoF \times CoF
$$

The resulting risk scores provide a relative measure for comparing assets and identifying infrastructure requiring additional investigation, maintenance, rehabilitation, replacement, or other risk mitigation measures.

Risk scores are intended to support engineering and management decisions. They should not be considered substitutes for engineering judgment, field investigations, regulatory requirements, or asset-specific evaluations.

---

# 2. Purpose and Objectives

The purpose of this Risk Assessment Plan is to establish a repeatable and defensible methodology for identifying infrastructure assets that represent the greatest risk to the [Municipality].

Specific objectives include:

1. Establish consistent criteria for evaluating asset condition and reliability.
2. Estimate the probability that individual assets or asset groups may fail to perform their intended function.
3. Evaluate the potential consequences associated with asset failure.
4. Develop relative risk scores for comparison across the asset portfolio.
5. Identify high-risk assets requiring additional evaluation or intervention.
6. Support prioritization of capital improvement projects.
7. Identify opportunities to reduce risk through operational, maintenance, rehabilitation, or capital improvements.
8. Establish a framework that can be updated as additional asset information becomes available.

---

# 3. Asset Portfolio

## 3.1 Assets Included

The assessment includes the following infrastructure assets:

| Asset Class          | Description                            | Approximate Quantity | Primary Data Source |
| -------------------- | -------------------------------------- | -------------------: | ------------------- |
| Water Mains          | Distribution and transmission piping   |                  [ ] | GIS                 |
| Valves               | Isolation and control valves           |                  [ ] | GIS / CMMS          |
| Pump Stations        | Water or wastewater pumping facilities |                  [ ] | GIS / O&M           |
| Force Mains          | Wastewater pressure piping             |                  [ ] | GIS                 |
| Gravity Sewers       | Collection system piping               |                  [ ] | GIS / CCTV          |
| Manholes             | Collection system structures           |                  [ ] | GIS                 |
| Storage Facilities   | Tanks, reservoirs, clearwells          |                  [ ] | Asset Records       |
| Treatment Facilities | Process and supporting assets          |                  [ ] | CMMS                |
| Stormwater Assets    | Pipes, culverts, structures, ponds     |                  [ ] | GIS                 |
| Other                | [Description]                          |                  [ ] | [Source]            |

The specific assets included in the assessment shall be documented in the project asset inventory.

---

## 3.2 Asset Hierarchy

Assets should be organized using a consistent hierarchy appropriate for the infrastructure system.

Example:

**Utility System**

→ Water System
→ Transmission System
→ Water Main
→ Segment
→ Individual Asset

or

**Wastewater System**

→ Collection System
→ Pump Station
→ Mechanical System
→ Pump
→ Individual Component

The level at which risk is evaluated should reflect the quality of available data and the decisions the assessment is intended to support.

---

# 4. Data Sources

Risk evaluations should incorporate available information from multiple sources.

Potential data sources include:

* GIS asset inventory;
* Computerized Maintenance Management System (CMMS);
* Work order history;
* Break and failure records;
* CCTV inspection data;
* Condition assessments;
* Hydraulic models;
* SCADA data;
* Customer complaint records;
* Maintenance staff interviews;
* Record drawings;
* Construction records;
* Asset age and material;
* Soil and geotechnical information;
* Floodplain information;
* Environmental data;
* Critical customer locations;
* Roadway classifications;
* Historical project records; and
* Previous engineering studies.

## 4.1 Data Quality

Available data should be evaluated for:

* Completeness;
* Accuracy;
* Consistency;
* Currency;
* Spatial accuracy; and
* Suitability for the intended analysis.

Data limitations shall be documented and considered when interpreting risk scores.

Where asset information is incomplete, assumptions may be required. Significant assumptions should be documented and periodically revisited as better information becomes available.

---

# 5. Risk Assessment Methodology

Risk shall be evaluated based on two primary components:

1. **Probability of Failure (PoF)**
2. **Consequence of Failure (CoF)**

The basic risk score is calculated as:

$$
Risk = PoF \times CoF
$$

Where appropriate, additional weighting, normalization, or statistical methods may be applied to account for differences among asset classes.

---

# 6. Probability of Failure

Probability of Failure represents the relative likelihood that an asset will fail to perform its intended function within the planning horizon.

PoF should consider available indicators of asset condition and performance.

## 6.1 Potential PoF Factors

Potential factors include:

| Factor               | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| Asset Age            | Age relative to expected useful life                         |
| Material             | Material-specific deterioration characteristics              |
| Condition            | Observed physical or structural condition                    |
| Failure History      | Previous failures, breaks, or service interruptions          |
| Maintenance History  | Frequency and type of corrective maintenance                 |
| Operating Conditions | Pressure, flow, cycling, loading, or environmental exposure  |
| Soil Conditions      | Corrosivity, settlement potential, groundwater, etc.         |
| Installation Era     | Construction practices associated with installation period   |
| Inspection Results   | CCTV, structural inspections, testing, or field observations |
| Performance Trends   | Changes in operating performance over time                   |

---

## 6.2 Example PoF Rating

| Rating | Probability of Failure | General Description                                                            |
| -----: | ---------------------- | ------------------------------------------------------------------------------ |
|      1 | Very Low               | Asset is in good condition with no significant indicators of deterioration     |
|      2 | Low                    | Minor deterioration or aging is present                                        |
|      3 | Moderate               | Deterioration or performance concerns are evident                              |
|      4 | High                   | Significant deterioration, recurring maintenance, or reliability concerns      |
|      5 | Very High              | Failure is imminent, recurring, or strongly indicated by available information |

Asset-specific criteria should be developed for major asset classes where sufficient information is available.

---

# 7. Consequence of Failure

Consequence of Failure represents the potential impact resulting from an asset's inability to perform its intended function.

Unlike PoF, which focuses primarily on the asset itself, CoF considers the broader effects of failure on customers, infrastructure systems, the environment, municipal operations, and the community.

## 7.1 Consequence Categories

The following consequence categories should be considered.

### Service Impact

Potential impacts include:

* Number of customers affected;
* Duration of service interruption;
* Loss of system capacity;
* Loss of redundancy;
* Impact to critical customers; and
* Ability to isolate or bypass the failed asset.

### Public Health and Safety

Potential impacts include:

* Drinking water quality;
* Sanitary sewer overflows;
* Flooding;
* Roadway hazards;
* Structural failure;
* Public exposure to untreated wastewater; and
* Emergency response impacts.

### Environmental Impact

Potential impacts include:

* Surface water impacts;
* Wetland impacts;
* Groundwater impacts;
* Sanitary sewer overflows;
* Permit violations; and
* Sensitive environmental areas.

### Financial Impact

Potential impacts include:

* Emergency repair cost;
* Restoration cost;
* Property damage;
* Business interruption;
* Regulatory penalties;
* Loss of revenue; and
* Increased operating costs.

### Community Impact

Potential impacts include:

* Traffic disruption;
* Road closures;
* Schools;
* Hospitals;
* Emergency services;
* Major employers;
* Commercial districts; and
* Public confidence.

### Regulatory Impact

Potential impacts include:

* Permit violations;
* Consent order requirements;
* Drinking water regulations;
* Environmental compliance;
* Reporting requirements; and
* Potential enforcement actions.

---

## 7.2 Example CoF Rating

| Rating | Consequence   | General Description                                                             |
| -----: | ------------- | ------------------------------------------------------------------------------- |
|      1 | Insignificant | Minimal operational or community impact                                         |
|      2 | Minor         | Localized impact with straightforward recovery                                  |
|      3 | Moderate      | Significant service, financial, or operational impact                           |
|      4 | Major         | Major disruption, environmental impact, or significant financial exposure       |
|      5 | Severe        | Potential public health, regulatory, environmental, or system-wide consequences |

---

# 8. Risk Scoring

Risk scores shall be calculated using:

$$
Risk = PoF \times CoF
$$

For a five-point PoF and CoF scale, resulting scores range from:

$$
1 \leq Risk \leq 25
$$

An example classification is provided below.

| Risk Score | Risk Classification | Typical Response                                                     |
| ---------: | ------------------- | -------------------------------------------------------------------- |
|        1–4 | Low                 | Routine monitoring and maintenance                                   |
|        5–9 | Moderate            | Monitor condition and evaluate during capital planning               |
|      10–16 | High                | Perform additional evaluation and develop mitigation strategy        |
|      17–25 | Critical            | Prioritize investigation, mitigation, rehabilitation, or replacement |

Thresholds should be calibrated based on the Municipality's risk tolerance, available funding, asset portfolio, and operational requirements.

---

# 9. Risk Matrix

The following matrix may be used to visualize relative asset risk.

| **PoF ↓ / CoF →** | **1** | **2** | **3** | **4** | **5** |
| ----------------- | ----: | ----: | ----: | ----: | ----: |
| **5 – Very High** |     5 |    10 |    15 |    20 |    25 |
| **4 – High**      |     4 |     8 |    12 |    16 |    20 |
| **3 – Moderate**  |     3 |     6 |     9 |    12 |    15 |
| **2 – Low**       |     2 |     4 |     6 |     8 |    10 |
| **1 – Very Low**  |     1 |     2 |     3 |     4 |     5 |

The matrix provides a screening and prioritization tool. Assets with identical numerical scores may warrant different management actions depending on the nature of the consequence, available redundancy, regulatory considerations, and engineering judgment.

---

# 10. Criticality Assessment

Certain assets may warrant elevated consideration regardless of calculated risk score.

Critical assets may include infrastructure that:

* Serves hospitals or emergency facilities;
* Provides the sole source of service to an area;
* Lacks system redundancy;
* Is required for treatment process continuity;
* Protects environmentally sensitive areas;
* Is located beneath major roadways, waterways, or railroads;
* Has significant regulatory implications;
* Represents a single point of system failure; or
* Would require substantial time or resources to repair.

Criticality should therefore be evaluated independently from the numerical risk score where appropriate.

---

# 11. Risk Mitigation Strategies

Risk management does not necessarily require immediate asset replacement.

Potential mitigation measures include:

### Operations

* Operational changes;
* Pressure management;
* Pump sequencing;
* System reconfiguration;
* Emergency operating procedures; and
* Increased monitoring.

### Maintenance

* Preventive maintenance;
* Increased inspection frequency;
* Valve exercising;
* Cleaning;
* Root control;
* Corrosion protection; and
* Targeted repairs.

### Rehabilitation

* Pipe lining;
* Structural rehabilitation;
* Coatings;
* Mechanical rehabilitation;
* Electrical upgrades; and
* Component replacement.

### Capital Replacement

Replacement should be considered where rehabilitation or operational mitigation cannot reduce risk to an acceptable level.

### Resiliency Improvements

Potential improvements include:

* Redundant equipment;
* Emergency power;
* Bypass connections;
* Looping;
* Additional isolation valves;
* Flood protection; and
* Alternative operating configurations.

---

# 12. Recommended Actions

Each significant-risk asset should be assigned a recommended management strategy.

| Asset ID | Asset   | PoF | CoF | Risk | Risk Level | Recommended Action | Timeframe |
| -------- | ------- | --: | --: | ---: | ---------- | ------------------ | --------- |
| [ID]     | [Asset] | [ ] | [ ] |  [ ] | [ ]        | [Action]           | [Year]    |
| [ID]     | [Asset] | [ ] | [ ] |  [ ] | [ ]        | [Action]           | [Year]    |

Recommended actions may include:

* No action / routine monitoring;
* Additional data collection;
* Detailed condition assessment;
* Increased inspection;
* Preventive maintenance;
* Rehabilitation;
* Operational modification;
* Preliminary engineering evaluation;
* Capital replacement; or
* Emergency risk mitigation.

---

# 13. Capital Improvement Prioritization

Risk scores should be considered as one component of the Municipality's Capital Improvement Program prioritization process.

Capital prioritization may additionally consider:

* Regulatory requirements;
* Available funding;
* Grant eligibility;
* Project readiness;
* Coordination with roadway or utility projects;
* Growth requirements;
* Hydraulic capacity;
* Operational efficiency;
* Community priorities;
* Project cost;
* Constructability; and
* Opportunity for risk reduction.

Where appropriate, a **Risk Reduction per Dollar Invested** metric may be developed to compare alternative projects.

For example:

$$
Risk\ Reduction = Risk_{Existing} - Risk_{Post-Project}
$$

and

$$
Risk\ Reduction\ Efficiency =
\frac{Risk_{Existing} - Risk_{Post-Project}}
{Project\ Cost}
$$

This approach can help distinguish between projects that address high-risk assets and projects that provide the greatest reduction in system risk for available capital funding.

---

# 14. Uncertainty and Confidence

Risk assessments inherently contain uncertainty because infrastructure condition, failure probability, and failure consequences cannot always be directly observed.

Each risk score should therefore be considered in conjunction with the quality of the underlying information.

An optional confidence rating may be assigned:

| Confidence | Description                                                     |
| ---------- | --------------------------------------------------------------- |
| High       | Recent inspection or reliable asset-specific information        |
| Moderate   | Partial asset information or indirect condition indicators      |
| Low        | Limited records, significant assumptions, or inferred condition |

High-risk assets with low-confidence data should generally be prioritized for additional investigation before major capital decisions are made.

---

# 15. Sensitivity and Scenario Analysis

For significant assets or major capital decisions, additional analysis may be warranted to evaluate uncertainty.

Potential analyses include:

* Alternative PoF assumptions;
* Alternative consequence assumptions;
* Failure scenario analysis;
* Hydraulic modeling;
* Emergency response scenarios;
* Monte Carlo simulation;
* Expected annual loss analysis; and
* Life-cycle cost analysis.

These analyses can provide additional information where a simple risk matrix is insufficient to support a major investment decision.

---

# 16. Implementation Plan

The risk assessment framework should be implemented in phases.

## Phase 1 – Asset Inventory

Establish and validate the infrastructure asset inventory.

## Phase 2 – Data Integration

Compile GIS, maintenance, inspection, operational, and failure data.

## Phase 3 – Initial Risk Screening

Calculate preliminary PoF, CoF, and risk scores.

## Phase 4 – Engineering Review

Review high-risk assets with engineering and operations staff.

## Phase 5 – Field Verification

Perform targeted inspections or condition assessments where additional information is required.

## Phase 6 – Risk Mitigation

Develop maintenance, rehabilitation, operational, and capital improvement recommendations.

## Phase 7 – CIP Integration

Incorporate recommended projects into the Municipality's capital planning process.

---

# 17. Monitoring and Updates

The risk assessment should be maintained as a living asset management tool rather than a one-time study.

Risk scores should be updated when significant new information becomes available, including:

* Asset failures;
* Inspection results;
* Rehabilitation or replacement;
* Changes in system configuration;
* New development;
* Updated hydraulic modeling;
* Regulatory changes; and
* Changes in critical customers or community infrastructure.

A comprehensive review of the risk model should be performed approximately every [3–5] years or as appropriate for the Municipality's asset management program.

---

# 18. Governance and Decision-Making

Responsibility for maintaining the risk assessment should be assigned to designated municipal staff.

Recommended responsibilities include:

**Engineering**

* Maintain risk methodology;
* Evaluate capital improvements;
* Review technical assumptions; and
* Perform engineering evaluations.

**Operations and Maintenance**

* Provide condition and performance information;
* Document failures;
* Identify operational concerns; and
* Validate asset risk rankings.

**GIS / Asset Management**

* Maintain asset inventory;
* Integrate risk attributes;
* Maintain asset identifiers; and
* Support mapping and reporting.

**Utility Management**

* Establish risk tolerance;
* Review high-risk assets;
* Approve mitigation priorities; and
* Incorporate results into budgeting and capital planning.

---

# 19. Deliverables

The Risk Assessment Program should ultimately provide the Municipality with:

1. Updated asset inventory;
2. Documented risk methodology;
3. Probability of Failure scores;
4. Consequence of Failure scores;
5. Overall asset risk scores;
6. GIS-based risk mapping;
7. Critical asset identification;
8. Ranked high-risk asset list;
9. Recommended mitigation strategies;
10. Capital improvement recommendations; and
11. Procedures for periodically updating the assessment.

---

# 20. Limitations

The risk assessment represents a planning-level evaluation based on information available at the time of the assessment.

Risk scores are relative indicators intended to assist with infrastructure management and capital planning. They do not represent predictions of the exact timing or occurrence of individual asset failures.

The results should be interpreted in conjunction with engineering judgment, operational experience, field investigations, regulatory requirements, and other relevant information.

---

# Appendix A – Asset Risk Register

| Asset ID | Asset Type | Location | Age | Condition | PoF | CoF | Risk | Criticality | Confidence | Recommended Action |
| -------- | ---------- | -------- | --: | --------- | --: | --: | ---: | ----------- | ---------- | ------------------ |

---

# Appendix B – Probability of Failure Criteria

Develop asset-specific scoring criteria for:

* Water mains;
* Force mains;
* Gravity sewers;
* Pump stations;
* Treatment facilities;
* Storage facilities;
* Stormwater infrastructure; and
* Other major asset classes.

---

# Appendix C – Consequence of Failure Criteria

Document scoring criteria for:

* Service impacts;
* Public health and safety;
* Environmental impacts;
* Financial impacts;
* Community impacts; and
* Regulatory impacts.

---

# Appendix D – Risk Maps

Provide GIS maps showing:

* Asset risk;
* Probability of failure;
* Consequence of failure;
* Critical assets; and
* Recommended capital improvements.

---

# Appendix E – Recommended Capital Improvements

| Priority | Project | Assets Addressed | Existing Risk | Post-Project Risk | Estimated Cost | Risk Reduction | Recommended Year |
| -------: | ------- | ---------------- | ------------: | ----------------: | -------------: | -------------: | ---------------- |
