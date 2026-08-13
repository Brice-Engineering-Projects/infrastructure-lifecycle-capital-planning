# System Architecture

## Infrastructure Lifecycle & Capital Planning

## 1. Purpose

This document defines the high-level architecture for the **Infrastructure Lifecycle & Capital Planning** project.

The architecture describes how engineering asset information, lifecycle models, risk analysis, financial analysis, uncertainty, and capital-planning methods interact to support infrastructure investment decisions.

This document focuses on:

* major analytical components
* component responsibilities
* information flow
* dependency boundaries
* separation of concerns
* architectural principles
* progressive system development

Detailed repository organization is documented separately in:

`docs/01_architecture/01_structure.md`

---

# 2. Architectural Objective

The system is intended to support a progression from individual infrastructure asset information to defensible capital investment recommendations.

At maturity, the analytical workflow is expected to resemble:

```text
Asset Data
    ↓
Asset Representation
    ↓
Condition & Performance
    ↓
Deterioration & Remaining Useful Life
    ↓
Probability of Failure
    ↓
Consequence & Criticality
    ↓
Risk
    ↓
Intervention Alternatives
    ↓
Lifecycle Economics
    ↓
Risk Reduction
    ↓
Uncertainty Analysis
    ↓
Portfolio Prioritization
    ↓
Capital Constraints & Optimization
    ↓
Multi-Year Capital Planning
    ↓
Decision Outputs
```

The architecture should make this process:

* transparent
* modular
* testable
* explainable
* progressively extensible

The system is intended to support engineering judgment rather than replace it.

---

# 3. Architectural Principles

## 3.1 Engineering Domain First

The architecture should represent infrastructure decision concepts directly.

Examples include:

* assets
* condition
* deterioration
* remaining useful life
* interventions
* failure
* consequences
* risk
* lifecycle cost
* levels of service
* capital projects
* portfolios

The software architecture should follow the engineering problem rather than forcing the engineering problem into generic software abstractions.

---

## 3.2 Progressive Complexity

The project should begin with simple, deterministic, independently verifiable methods.

More sophisticated techniques should be introduced only when they provide a demonstrated analytical benefit.

The preferred progression is:

```text
Simple
  ↓
Correct
  ↓
Validated
  ↓
Reusable
  ↓
Probabilistic
  ↓
Optimized
  ↓
Integrated
```

For example, lifecycle analysis should work deterministically before Monte Carlo simulation is introduced.

Similarly, transparent project prioritization should be understood before formal optimization methods are added.

---

## 3.3 Separation of Engineering State and Decision Analysis

Information describing an infrastructure asset should remain conceptually separate from methods used to make decisions about that asset.

For example:

```text
Asset State
├── Age
├── Material
├── Condition
├── Capacity
└── Failure History

Decision Analysis
├── Intervention Alternatives
├── Lifecycle Cost
├── Risk Reduction
└── Recommended Timing
```

An asset represents what exists.

An intervention represents what could be done.

An analysis evaluates the consequences of those alternatives.

---

## 3.4 Separation of Methodology and Assumptions

Analytical methods should remain separate from project-specific assumptions.

For example:

$$
PV = \frac{FV}{(1+r)^n}
$$

is methodology.

A statement such as:

> Assume a real discount rate of 4%.

is an analytical assumption.

This distinction allows assumptions to change without requiring changes to the underlying analytical method.

---

## 3.5 Separation of Deterministic Analysis and Uncertainty

Core analytical models should initially operate using deterministic inputs.

Uncertainty analysis should wrap or repeatedly evaluate those models rather than require separate implementations of the underlying calculations.

Conceptually:

```text
              Deterministic Model
                     ↑
                     │
       ┌─────────────┼─────────────┐
       │             │             │
Sensitivity      Scenarios     Monte Carlo
Analysis         Analysis       Simulation
```

This allows one validated model to support multiple uncertainty-analysis techniques.

---

## 3.6 Explainability

Infrastructure investment recommendations must remain traceable.

A decision should be explainable through:

```text
Input Data
    ↓
Engineering Assumptions
    ↓
Analytical Method
    ↓
Intermediate Results
    ↓
Decision Criteria
    ↓
Recommendation
```

The architecture should avoid analytical black boxes where a score or recommendation cannot be traced to its underlying drivers.

---

## 3.7 Testability

Core analytical components should be independently testable.

For example:

```text
Present Value
Risk
Deterioration
Remaining Useful Life
Lifecycle Cost
Risk Reduction
Project Selection
```

should be capable of validation without requiring execution of the entire system.

---

# 4. Architectural Layers

The mature system can be viewed as several conceptual layers.

```text
┌──────────────────────────────────────────┐
│          Decision & Reporting            │
├──────────────────────────────────────────┤
│          Capital Planning                │
├──────────────────────────────────────────┤
│       Portfolio Decision Analysis        │
├──────────────────────────────────────────┤
│        Uncertainty Analysis              │
├──────────────────────────────────────────┤
│   Lifecycle & Intervention Analysis      │
├──────────────────────────────────────────┤
│     Risk & Service Analysis              │
├──────────────────────────────────────────┤
│       Asset State & Behavior             │
├──────────────────────────────────────────┤
│        Engineering Economics             │
├──────────────────────────────────────────┤
│       Data & Validation                  │
└──────────────────────────────────────────┘
```

These are conceptual layers rather than mandatory software packages.

Their purpose is to establish responsibilities and dependency direction.

---

# 5. Data & Validation Layer

## Responsibility

The data layer provides reliable information to the analytical system.

Potential data includes:

* asset inventory
* installation dates
* materials
* dimensions
* capacities
* condition assessments
* inspection records
* maintenance history
* failure records
* cost information
* operational information
* spatial attributes

## Data Flow

```text
Source Data
    ↓
Validation
    ↓
Cleaning / Transformation
    ↓
Analysis-Ready Data
    ↓
Domain Representation
```

Data validation should occur before analytical calculations whenever practical.

The analytical model should not silently repair invalid engineering information.

---

# 6. Engineering Economics Layer

## Responsibility

Engineering economics provides reusable financial mathematics required by lifecycle analysis.

Potential capabilities include:

* cash-flow representation
* present value
* future value
* discounting
* net present value
* equivalent annual cost
* inflation
* escalation
* residual value

This layer should remain independent of specific infrastructure asset types.

For example:

```text
Present Value
```

should not need to know whether the cash flow represents a pump replacement, pipeline rehabilitation, or inspection program.

---

# 7. Asset State & Behavior Layer

## Responsibility

The asset layer represents infrastructure assets and how their physical state changes over time.

Potential concepts include:

* asset identity
* asset class
* age
* material
* condition
* expected service life
* deterioration
* remaining useful life
* failure history

Conceptually:

```text
Asset
  ↓
Current State
  ↓
Expected Deterioration
  ↓
Future State
```

The asset model should describe the infrastructure without deciding what action should be taken.

---

# 8. Condition & Deterioration

Condition and deterioration represent related but distinct concepts.

**Condition** describes the current physical or functional state of an asset.

**Deterioration** describes how that state is expected to change over time.

Initial models may be deterministic.

Later models may incorporate:

* nonlinear deterioration
* condition-state transitions
* Markov models
* survival methods
* predictive analytics

The architecture should allow these methods to evolve without requiring lifecycle and capital-planning logic to be rewritten.

---

# 9. Remaining Useful Life

Remaining useful life connects asset state with intervention timing.

Potential inputs include:

```text
Age
 +
Condition
 +
Expected Service Life
 +
Deterioration
 +
Operating Environment
        ↓
Remaining Useful Life
```

Early implementations may use simplified engineering assumptions.

Later implementations may incorporate probabilistic or predictive methods.

Downstream components should consume remaining-life estimates without depending directly on how those estimates were produced.

---

# 10. Risk & Service Layer

## Responsibility

The risk layer evaluates the consequences of continued asset operation and potential failure.

The fundamental relationship is:

$$
\text{Risk}
===========

\text{Probability of Failure}
\times
\text{Consequence of Failure}
$$

The architecture should preserve the distinction between:

* probability of failure
* consequence of failure
* criticality
* level of service
* total risk

These concepts are related but should not be collapsed into a single unexplained score.

---

# 11. Probability of Failure

Probability of failure may depend on:

* age
* condition
* deterioration
* material
* failure history
* operating environment
* loading
* inspection results

Initial implementations may use simplified models.

Later implementations may incorporate predictive models developed internally or imported from other analytical workflows.

The rest of the system should consume probability-of-failure estimates through a consistent interface regardless of the underlying model.

---

# 12. Consequence of Failure

Consequence analysis evaluates what happens if an asset fails.

Potential consequences include:

* emergency repair cost
* service interruption
* environmental impacts
* regulatory impacts
* public health and safety
* property damage
* critical customer impacts
* loss of redundancy
* operational disruption

Consequences may include both:

* financial measures
* non-financial measures

The architecture should avoid forcing every consequence into monetary terms when doing so would create false precision.

---

# 13. Criticality

Criticality represents the importance of an asset to infrastructure system performance.

Potential factors include:

* customers served
* critical facilities
* redundancy
* hydraulic importance
* process importance
* environmental sensitivity
* regulatory significance
* accessibility
* expected outage duration

Criticality may contribute to consequence analysis while remaining independently available for decision support.

---

# 14. Levels of Service

Levels of service connect infrastructure assets to utility or owner objectives.

Potential measures include:

* reliability
* availability
* pressure
* capacity
* water quality
* regulatory compliance
* customer interruptions
* emergency response
* resilience

Conceptually:

```text
Asset Performance
        ↓
System Performance
        ↓
Level of Service
        ↓
Investment Need
```

This prevents asset-management decisions from becoming solely condition-driven.

An asset in poor condition may not necessarily represent the highest investment priority if its service consequence is low.

---

# 15. Intervention Layer

## Responsibility

Interventions represent actions that may change an asset's future state.

Potential interventions include:

* inspection
* monitoring
* preventive maintenance
* corrective maintenance
* rehabilitation
* partial replacement
* full replacement
* operate to failure

An intervention may affect:

```text
Condition
Remaining Useful Life
Probability of Failure
Operating Cost
Maintenance Cost
Capital Cost
Residual Risk
```

The architecture should allow multiple intervention alternatives to be evaluated against the same asset.

---

# 16. Lifecycle Analysis Layer

## Responsibility

Lifecycle analysis evaluates the long-term consequences of alternative infrastructure strategies.

Conceptually:

```text
Asset
  +
Intervention Strategy
  +
Planning Horizon
  +
Engineering Economics
  +
Risk
      ↓
Lifecycle Result
```

A lifecycle result may include:

* discounted lifecycle cost
* equivalent annual cost
* intervention timing
* expected failure cost
* residual value
* residual risk
* risk reduction

This layer represents the primary connection between engineering and financial analysis.

---

# 17. Alternative Analysis

Infrastructure decisions generally involve multiple feasible alternatives.

For example:

```text
Existing Water Main
        │
        ├── Continue Operation
        │
        ├── Increase Inspection
        │
        ├── Rehabilitate
        │
        ├── Replace in Year 5
        │
        └── Replace Immediately
```

Each alternative should be evaluated through the same analytical framework so that comparisons remain consistent.

The output should explain the tradeoffs rather than merely identify a numerical winner.

---

# 18. Risk Reduction

Interventions should be evaluated according to how they change infrastructure risk.

```text
Current Risk
    ↓
Intervention
    ↓
Residual Risk
    ↓
Risk Reduction
```

Risk reduction may later support measures such as:

$$
\text{Risk Reduction Efficiency}
================================

\frac{\text{Risk Reduction}}
{\text{Investment Cost}}
$$

This provides an important connection between asset risk and capital allocation.

---

# 19. Uncertainty Layer

## Responsibility

The uncertainty layer evaluates how uncertain assumptions affect analytical results.

Potential methods include:

* sensitivity analysis
* scenario analysis
* Monte Carlo simulation

The architecture should use existing deterministic analytical components rather than recreate calculations specifically for uncertainty analysis.

Conceptually:

```text
Uncertain Inputs
       ↓
Sampling / Scenario Definition
       ↓
Existing Analytical Model
       ↓
Distribution of Outcomes
       ↓
Decision Robustness
```

Potential uncertain inputs include:

* asset life
* deterioration
* construction cost
* escalation
* failure probability
* failure timing
* intervention effectiveness
* consequence estimates

---

# 20. Portfolio Decision Layer

## Responsibility

Portfolio analysis expands decision making from one asset to many competing infrastructure needs.

```text
Asset A ─┐
Asset B ─┤
Asset C ─┤
Asset D ─┼──→ Portfolio Analysis
Asset E ─┤
Asset F ─┘
```

Each asset or proposed project may contribute information such as:

* condition
* risk
* criticality
* lifecycle cost
* intervention cost
* risk reduction
* level-of-service impact
* regulatory need

The portfolio layer compares these needs using transparent decision criteria.

---

# 21. Prioritization

Prioritization determines the relative importance of competing infrastructure investments.

Potential criteria include:

* condition
* risk
* criticality
* regulatory requirements
* lifecycle economics
* risk reduction
* level-of-service impact
* project urgency

Prioritization should remain explainable.

A project should not receive a high ranking solely because an opaque weighted score says so.

The system should retain the factors that drove the result.

---

# 22. Capital Planning Layer

## Responsibility

Capital planning determines which investments can actually be implemented given limited funding.

This differs from prioritization.

Prioritization asks:

> Which projects are most important?

Capital planning asks:

> Given available funding and other constraints, which projects should actually be implemented?

Conceptually:

```text
Prioritized Needs
       +
Available Capital
       +
Project Constraints
       ↓
Selected Investments
```

---

# 23. Capital Constraints

Potential constraints include:

* annual budgets
* total program funding
* project dependencies
* regulatory deadlines
* minimum service requirements
* implementation timing
* resource availability

Initial methods may use transparent selection rules.

Later stages may introduce formal optimization.

---

# 24. Optimization

Advanced capital selection may eventually use:

* linear programming
* integer programming
* constrained optimization
* multi-objective optimization

Optimization should remain downstream of the engineering analysis.

The architecture should follow:

```text
Engineering Analysis
        ↓
Candidate Investments
        ↓
Decision Metrics
        ↓
Constraints
        ↓
Optimization
```

not:

```text
Optimization Algorithm
        ↓
Invent Reasons to Use It
```

The mathematical technique should serve the infrastructure decision problem.

---

# 25. Multi-Year Capital Planning

Multi-year planning extends project selection across time.

Potential inputs include:

* annual capital budgets
* intervention costs
* escalation
* deterioration
* changing failure probability
* deferred risk
* regulatory deadlines
* project dependencies

Potential outputs include:

* annual capital expenditures
* funded projects
* deferred projects
* unfunded needs
* annual risk exposure
* cumulative risk reduction

Conceptually:

```text
Current Portfolio
       ↓
Year 1 Decisions
       ↓
Updated Asset State
       ↓
Year 2 Decisions
       ↓
Updated Asset State
       ↓
       ...
       ↓
Long-Term Capital Plan
```

This requires the architecture to recognize that delaying an investment may change both its cost and its risk.

---

# 26. Decision & Reporting Layer

## Responsibility

The reporting layer converts analytical results into information suitable for engineering and management decisions.

Potential outputs include:

* lifecycle comparisons
* risk matrices
* deterioration curves
* intervention timelines
* capital forecasts
* funded and unfunded needs
* sensitivity results
* risk-reduction summaries
* multi-year capital plans

Reporting should consume analytical results.

It should not contain core engineering or financial calculations.

---

# 27. Dependency Direction

Dependencies should generally flow from foundational components toward higher-level decision components.

```text
Data
 ↓
Economics
 ↓
Assets
 ↓
Condition / Deterioration
 ↓
Risk & Service
 ↓
Interventions
 ↓
Lifecycle Analysis
 ↓
Uncertainty
 ↓
Portfolio Analysis
 ↓
Capital Planning
 ↓
Reporting
```

This diagram represents conceptual dependency direction rather than a strict requirement that every component depend on the one immediately above it.

Lower-level components should remain usable independently.

For example:

* present-value calculations should not depend on asset models
* asset models should not depend on capital planning
* lifecycle analysis should not depend on visualization
* risk calculations should not depend on reporting

---

# 28. External Analytical Inputs

The architecture should allow specialized analytical outputs to be introduced without requiring those models to be implemented directly within this project.

Potential examples include:

```text
Failure Prediction Model
          ↓
Probability of Failure
          ↓
Lifecycle & Risk Analysis
```

```text
Cost Intelligence
       ↓
Intervention Cost
       ↓
Lifecycle Economics
```

```text
Geospatial Risk Analysis
          ↓
Exposure / Consequence
          ↓
Risk Analysis
```

This creates potential future integration with other infrastructure analytics projects while maintaining clear project boundaries.

---

# 29. Relationship to Other Projects

The project may eventually consume analytical concepts or outputs from related infrastructure projects.

Conceptually:

```text
Applied Infrastructure Analytics
        ↓
Statistics / Probability / Uncertainty
        │
        │
Toronto Pipeline Failure Prediction
        ↓
Failure Analytics
        │
        │
CostQueryPro
        ↓
Cost Intelligence
        │
        │
Lift Station Predictive Maintenance
        ↓
Condition / Reliability Intelligence
        │
        │
Geospatial Infrastructure Risk
        ↓
Spatial Risk Factors
        │
        ▼
Infrastructure Lifecycle
& Capital Planning
        │
        ▼
Utility Asset Risk Platform
```

These integrations represent potential long-term relationships.

They are not dependencies required for initial project implementation.

---

# 30. Analytical Traceability

A core architectural requirement is the ability to trace a recommendation back through the analytical workflow.

For example:

```text
Recommended:
Replace Asset A in Year 3
        ↑
Selected in Capital Plan
        ↑
High Investment Priority
        ↑
Large Risk Reduction
        ↑
Replacement Alternative
        ↑
Increasing Failure Risk
        ↑
Poor Condition / Low Remaining Life
        ↑
Asset Data
```

The system should preserve enough intermediate information to explain each step.

This is especially important where analytical outputs may eventually support capital recommendations presented to utility management, finance staff, governing boards, or other decision-makers.

---

# 31. Engineering Judgment Boundary

The architecture distinguishes between:

### Model Responsibilities

The system may:

* calculate
* compare
* estimate
* rank
* simulate
* optimize
* visualize

### Professional Responsibilities

Engineers and decision-makers must:

* validate assumptions
* evaluate data quality
* determine technical feasibility
* interpret unusual conditions
* assess non-quantifiable consequences
* consider regulatory requirements
* evaluate stakeholder concerns
* select final recommendations

The final architecture therefore follows:

```text
Data
  ↓
Analytics
  ↓
Decision Support
  ↓
Engineering Judgment
  ↓
Management Decision
```

rather than:

```text
Data
  ↓
Algorithm
  ↓
Automatic Capital Decision
```

---

# 32. Progressive Implementation Architecture

The complete architecture is a long-term target.

The initial implementation should remain substantially smaller.

## Initial Architecture

```text
Engineering Economics
        ↓
Lifecycle Cash Flows
        ↓
Alternative Comparison
```

## Intermediate Architecture

```text
Asset
  ↓
Condition
  ↓
Interventions
  ↓
Risk
  ↓
Lifecycle Economics
  ↓
Alternative Comparison
```

## Advanced Architecture

```text
Asset Portfolio
      ↓
Asset-Level Analysis
      ↓
Risk & Lifecycle Results
      ↓
Uncertainty
      ↓
Portfolio Prioritization
      ↓
Capital Constraints
      ↓
Multi-Year Planning
      ↓
Decision Reporting
```

New architectural components should be introduced as the staged roadmap requires them.

---

# 33. Architectural Success Criteria

The architecture should be considered successful if it allows the project to:

1. Represent infrastructure assets and their condition.
2. Model deterioration and remaining useful life.
3. Evaluate multiple intervention strategies.
4. Calculate lifecycle economic consequences.
5. Incorporate probability and consequence of failure.
6. Evaluate risk reduction.
7. Represent uncertainty without duplicating core analytical logic.
8. Compare competing infrastructure investments.
9. Apply capital constraints.
10. Develop multi-year investment strategies.
11. Preserve traceability from source information to recommendation.
12. Allow analytical components to evolve independently where practical.

Most importantly, the architecture should support answering:

> **Given the condition, performance, risk, lifecycle economics, and service importance of infrastructure assets, how should limited capital be allocated over time to produce a defensible long-term investment strategy?**

That decision problem defines the architecture. The architecture does not define the decision problem.
