# Project Scope

## Infrastructure Lifecycle & Capital Planning

## 1. Purpose

The purpose of **Infrastructure Lifecycle & Capital Planning** is to develop a Python-based engineering decision-analysis framework for evaluating infrastructure lifecycle strategies and capital investment decisions.

The project focuses on the analytical connection between:

* infrastructure asset condition
* deterioration and remaining useful life
* failure risk
* intervention alternatives
* lifecycle costs
* engineering economics
* levels of service
* capital constraints
* investment prioritization
* multi-year capital planning

The project is primarily a **learning and engineering analytics project**. It is intended to progressively develop the technical, financial, and decision-analysis methods used in infrastructure asset management.

The project will begin with transparent individual-asset analyses and progressively advance toward portfolio-level capital planning.

---

# 2. Primary Project Question

The project is organized around the following decision problem:

> **Given limited capital, when should infrastructure assets be maintained, rehabilitated, or replaced to provide the greatest long-term value while managing risk and maintaining acceptable levels of service?**

Supporting questions include:

* What is the expected remaining life of an asset?
* What happens if intervention is deferred?
* What intervention alternatives are technically feasible?
* What is the lifecycle cost of each alternative?
* How should future costs be discounted and compared?
* How does failure risk change over time?
* How much risk does an intervention reduce?
* What is the economic value of that risk reduction?
* Which investments should receive priority?
* How should limited capital be allocated across competing assets?
* How should investments be scheduled across multiple years?
* How sensitive is the recommendation to uncertain assumptions?

---

# 3. Infrastructure Domain

The project will primarily use **municipal water and wastewater infrastructure** for examples, datasets, and case studies.

Potential asset classes include:

### Linear Assets

* water mains
* force mains
* gravity sewers
* reclaimed water mains

### Vertical and Facility Assets

* pumps
* lift stations
* pump stations
* storage tanks
* treatment process equipment
* electrical equipment
* mechanical equipment

The underlying analytical methods should remain sufficiently general that they could later be adapted to other infrastructure sectors.

Examples may include:

* stormwater
* transportation
* public facilities
* energy infrastructure

Expansion beyond water and wastewater is not required for initial project success.

---

# 4. In-Scope Capabilities

## 4.1 Asset Representation

The project will develop simplified representations of infrastructure assets containing information such as:

* asset identifier
* asset class
* installation date
* age
* material
* size or capacity
* replacement value
* expected service life
* condition
* criticality
* maintenance history
* failure history
* operating characteristics

The asset representation will evolve as additional analytical capabilities are introduced.

---

## 4.2 Asset Condition

The project will evaluate methods for representing infrastructure condition.

Initial methods may include:

* condition scores
* inspection ratings
* age-based assumptions
* engineering assessments
* threshold-based classifications

Later methods may incorporate:

* deterioration models
* inspection histories
* probabilistic condition estimates
* condition transitions

Condition information will support lifecycle and intervention decisions.

---

## 4.3 Deterioration

The project will evaluate how infrastructure condition changes over time.

Initial models should remain simple and interpretable.

Potential approaches include:

* deterministic deterioration curves
* age-based deterioration
* condition-state transitions

Later analysis may explore:

* regression-based deterioration
* Markov models
* survival analysis
* probabilistic deterioration

Advanced deterioration modeling is considered a later-stage capability rather than an initial requirement.

---

## 4.4 Remaining Useful Life

The project will evaluate methods for estimating the remaining useful life of infrastructure assets.

Remaining useful life may initially be estimated using:

* expected service life
* asset age
* condition
* engineering assumptions

Later implementations may incorporate:

* deterioration models
* failure histories
* survival analysis
* predictive models

Remaining useful life estimates will support intervention timing and lifecycle economic analysis.

---

## 4.5 Intervention Strategies

The project will evaluate alternative strategies for managing infrastructure assets.

Potential interventions include:

* continue normal operation
* increase monitoring
* inspection
* preventive maintenance
* corrective maintenance
* rehabilitation
* partial replacement
* full replacement
* operate to failure

Each intervention may affect:

* future condition
* remaining useful life
* probability of failure
* operating cost
* maintenance cost
* capital cost
* residual risk

---

# 5. Engineering Economics

Engineering economics is a core component of the project.

The project will develop and apply methods including:

* cash-flow modeling
* present value
* future value
* discounting
* compounding
* net present value
* equivalent annual cost
* real and nominal costs
* inflation
* construction cost escalation
* residual value
* analysis-period comparison

Financial methods will be used to compare engineering alternatives occurring at different points in time.

The project does **not** treat financial analysis as independent from engineering considerations.

Instead:

```text
Engineering Alternative
        ↓
Expected Performance
        ↓
Lifecycle Cash Flows
        ↓
Economic Analysis
        ↓
Engineering Decision
```

---

# 6. Lifecycle Cost Analysis

The project will evaluate the total costs associated with infrastructure ownership and intervention over a defined planning horizon.

Potential lifecycle costs include:

* initial capital cost
* engineering and design
* construction
* inspection
* monitoring
* preventive maintenance
* corrective maintenance
* energy
* operations
* rehabilitation
* emergency repair
* replacement
* disposal
* residual value

Lifecycle analysis will be used to compare alternatives whose costs occur at different times and whose expected service lives may differ.

---

# 7. Failure Risk

Risk-based analysis is within the project scope.

The general framework is:

$$
\text{Risk} =
\text{Probability of Failure}
\times
\text{Consequence of Failure}
$$

## Probability of Failure

Potential factors include:

* age
* condition
* material
* environment
* failure history
* operating conditions
* inspection results

## Consequence of Failure

Potential consequences include:

* direct repair cost
* emergency response
* service interruption
* environmental impact
* regulatory impact
* public health and safety
* property damage
* critical customer impacts
* loss of redundancy
* operational disruption

The project may represent consequences using financial and non-financial measures.

---

# 8. Criticality

Asset criticality will be considered when evaluating investment priorities.

Potential criticality factors include:

* population served
* critical customers
* hospitals and emergency facilities
* redundancy
* hydraulic importance
* process importance
* environmental sensitivity
* regulatory significance
* repair accessibility
* expected outage duration

Criticality may be incorporated into consequence-of-failure calculations or maintained as a separate decision factor where appropriate.

---

# 9. Levels of Service

The project will explore the relationship between infrastructure investment and levels of service.

Potential measures include:

* reliability
* availability
* system capacity
* pressure
* water quality
* regulatory compliance
* customer interruptions
* response time
* resilience

The purpose is to connect asset-level investment decisions with the service outcomes infrastructure owners are expected to provide.

---

# 10. Risk Reduction

Infrastructure investments will be evaluated partly according to their expected reduction in risk.

The general framework is:

```text
Existing Risk
      ↓
Intervention
      ↓
Residual Risk
      ↓
Risk Reduction
```

Potential measures may include:

* absolute risk reduction
* percentage risk reduction
* annualized risk reduction
* risk reduction per dollar invested

Risk reduction provides a connection between engineering need and capital efficiency.

---

# 11. Uncertainty Analysis

The project will explicitly evaluate uncertainty where it materially affects infrastructure decisions.

Potential uncertain variables include:

* asset service life
* deterioration rate
* intervention effectiveness
* construction cost
* inflation
* escalation
* discount rate
* failure probability
* failure timing
* emergency repair cost
* consequence estimates

Methods may include:

* sensitivity analysis
* scenario analysis
* probability distributions
* Monte Carlo simulation

Advanced uncertainty methods will be introduced progressively after deterministic models are established.

---

# 12. Asset Portfolio Analysis

The project will eventually expand from individual-asset decisions to portfolios of infrastructure assets.

Portfolio analysis may include:

* multiple asset classes
* competing infrastructure needs
* differing risk levels
* differing intervention costs
* differing service impacts
* regulatory requirements
* project dependencies

Portfolio analysis will provide the foundation for capital prioritization.

---

# 13. Capital Prioritization

The project will develop methods for prioritizing competing infrastructure investments.

Potential prioritization criteria include:

* condition
* probability of failure
* consequence of failure
* risk
* criticality
* level-of-service impact
* regulatory requirements
* lifecycle cost
* intervention cost
* risk reduction
* cost effectiveness
* project urgency
* project dependencies

Prioritization methods should remain transparent and explainable.

The project will distinguish between:

> **Ranking projects**

and:

> **Selecting projects under actual capital constraints**

These are related but different decision problems.

---

# 14. Capital Constraints

The project will evaluate infrastructure investment decisions where identified needs exceed available funding.

Example:

```text
Identified Capital Needs:    $100 million
Available Capital Funding:    $50 million
Funding Gap:                  $50 million
```

The analysis will explore which combination of investments provides the greatest value within available funding.

Initial approaches may use:

* ranking
* thresholds
* risk reduction per dollar
* priority categories

Later approaches may incorporate formal optimization methods.

---

# 15. Multi-Year Capital Planning

The project will eventually extend capital selection across a multi-year planning horizon.

Potential considerations include:

* annual capital budgets
* project timing
* inflation and escalation
* deterioration during deferral
* changing failure probability
* accumulated risk
* regulatory deadlines
* project dependencies
* construction sequencing
* funding scenarios

Potential outputs include:

* annual capital expenditures
* funded projects
* deferred projects
* unfunded needs
* annual risk exposure
* cumulative risk reduction

The resulting analysis should support development of a simplified multi-year capital improvement program.

---

# 16. Decision Visualization

The project may develop visualizations that improve understanding of infrastructure investment decisions.

Potential visualizations include:

* lifecycle cash-flow diagrams
* deterioration curves
* condition distributions
* risk matrices
* risk-versus-cost plots
* lifecycle cost comparisons
* intervention timelines
* capital expenditure forecasts
* funded versus unfunded needs
* annual risk exposure
* cumulative risk reduction
* sensitivity plots
* uncertainty distributions

Visualizations should support decision-making rather than exist solely for presentation.

---

# 17. Reporting

The project may produce structured decision reports summarizing:

* asset information
* engineering assumptions
* alternatives considered
* lifecycle costs
* risk
* uncertainty
* capital requirements
* recommended intervention
* recommended timing
* reasons for the recommendation

Reports should distinguish between:

* model outputs
* engineering assumptions
* analytical conclusions
* professional judgment

---

# 18. Software Scope

The project will primarily be implemented using Python.

Potential technical components include:

* reusable calculation modules
* data models
* validation
* analysis workflows
* notebooks
* automated tests
* visualization
* structured reporting

Initial development should prioritize analytical correctness and explainability over application complexity.

A production web application, enterprise database, or elaborate user interface is **not required** for the project to achieve its primary learning objectives.

---

# 19. Data Scope

The project may use:

* synthetic datasets
* publicly available infrastructure datasets
* generalized engineering examples
* published cost information
* anonymized example data where appropriate

Synthetic datasets should be designed to reproduce realistic infrastructure relationships rather than simply generate arbitrary random values.

All assumptions used to generate synthetic data should be documented.

---

# 20. Out of Scope

The following capabilities are explicitly outside the primary scope of the project.

## Enterprise Asset Management Systems

The project will not attempt to replace or reproduce systems such as:

* IBM Maximo
* SAP
* Infor
* Cityworks
* other CMMS/EAM platforms

Conceptual integration with these systems may be discussed, but implementing a full EAM system is outside scope.

---

## Detailed Hydraulic Modeling

The project will not replace hydraulic modeling software or detailed hydraulic engineering analysis.

Hydraulic outputs may eventually be used as analytical inputs where relevant.

---

## Detailed Process Modeling

Water and wastewater treatment process simulation is outside the primary scope.

---

## Detailed Design

The project will not perform detailed engineering design of rehabilitation or replacement projects.

Engineering alternatives will be represented at the planning and asset-management level.

---

## Construction Cost Estimating

Detailed quantity takeoffs and construction estimating are outside scope.

Planning-level cost estimates may be used as lifecycle-analysis inputs.

---

## Accounting and Financial Management Systems

The project will apply engineering economics but will not attempt to reproduce:

* utility accounting
* enterprise budgeting systems
* financial reporting
* treasury management
* bond financing systems

---

## CMMS Work Management

Detailed work-order management, labor scheduling, inventory management, and maintenance dispatch are outside scope.

Reliability and maintenance strategies may be evaluated analytically without reproducing CMMS functionality.

---

## Fully Autonomous Decision Making

The project will not automatically determine engineering investment decisions without human review.

Analytical results are intended to support:

> **engineering judgment, management decisions, and transparent capital planning.**

---

# 21. Future Integration

Methods developed in this project may eventually support or integrate with other infrastructure analytics projects.

Potential relationships include:

```text
Applied Infrastructure Analytics
        ↓
Statistical & Uncertainty Methods

Toronto Pipeline Failure Prediction
        ↓
Failure Probability / Remaining Life

CostQueryPro
        ↓
Historical Cost Intelligence

Lift Station Predictive Maintenance
        ↓
Condition / Reliability Intelligence

Geospatial Infrastructure Analysis
        ↓
Environmental & Spatial Risk Factors

Infrastructure Lifecycle & Capital Planning
        ↓
Lifecycle Economics / Investment Decisions

Utility Asset Risk Platform
        ↓
Integrated Asset Decision Intelligence
```

These relationships represent potential long-term integration rather than requirements for the initial implementation.

---

# 22. Scope Management Principle

New features should be evaluated according to whether they directly improve the project's ability to answer one of four questions:

1. **What condition is the asset in and how is it expected to change?**
2. **What intervention should be considered and when?**
3. **What are the lifecycle cost and risk implications of that intervention?**
4. **Given limited capital, which investments should be made and when?**

Features that do not materially support these questions should generally remain outside the project scope.

---

# 23. Definition of Scope Completion

The planned scope will be substantially achieved when the project can demonstrate a traceable analytical workflow from:

```text
Asset
  ↓
Condition
  ↓
Remaining Life
  ↓
Risk
  ↓
Intervention Alternatives
  ↓
Lifecycle Cost
  ↓
Economic & Risk Comparison
  ↓
Portfolio Priority
  ↓
Capital Constraint
  ↓
Multi-Year Investment Plan
```

The final result should explain not merely **which project receives funding**, but:

> **why the investment is recommended, what assumptions drive the recommendation, what risk it addresses, what it costs over its lifecycle, and what happens if the investment is deferred.**
