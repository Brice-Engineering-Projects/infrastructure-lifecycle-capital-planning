# Project Structure

## Infrastructure Lifecycle & Capital Planning

## 1. Purpose

This document defines the repository structure for the **Infrastructure Lifecycle & Capital Planning** project.

The structure is designed around four primary documentation concerns:

1. **Project Definition** — what is being built, why it is being built, what is included, and how development will progress.
2. **Architecture** — how the analytical software will be organized and how major components interact.
3. **Methodology** — the engineering, financial, statistical, and decision-analysis methods implemented by the project.
4. **Reference** — supporting standards, guidance, datasets, terminology, and external technical sources.

The repository will grow progressively. Directories and modules should be created when they are required by an active implementation stage rather than populated in advance.

---

# 2. Target Repository Structure

```text
infrastructure-lifecycle-capital-planning/
│
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .python-version
│
├── docs/
│   │
│   ├── 00_project/
│   │   ├── 00_overview.md
│   │   ├── 01_scope.md
│   │   ├── 02_deliverables.md
│   │   └── 03_roadmap.md
│   │
│   ├── 01_architecture/
│   │   ├── 00_architecture.md
│   │   ├── 01_structure.md
│   │   ├── 02_domain_model.md
│   │   ├── 03_data_architecture.md
│   │   └── 04_decision_pipeline.md
│   │
│   ├── 02_methodology/
│   │   ├── 00_methodology_overview.md
│   │   ├── engineering_economics.md
│   │   ├── lifecycle_cost_analysis.md
│   │   ├── condition_and_deterioration.md
│   │   ├── remaining_useful_life.md
│   │   ├── risk_methodology.md
│   │   ├── criticality.md
│   │   ├── levels_of_service.md
│   │   ├── uncertainty.md
│   │   └── capital_prioritization.md
│   │
│   └── 03_reference/
│       ├── README.md
│       ├── glossary.md
│       ├── assumptions.md
│       └── references.md
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── synthetic/
│
├── notebooks/
│   ├── 01_engineering_economics/
│   ├── 02_asset_lifecycle/
│   ├── 03_lifecycle_cost/
│   ├── 04_condition_deterioration/
│   ├── 05_risk/
│   ├── 06_levels_of_service/
│   ├── 07_uncertainty/
│   ├── 08_portfolio_prioritization/
│   ├── 09_capital_optimization/
│   └── 10_multi_year_planning/
│
├── src/
│   └── infrastructure_capital_planning/
│       ├── __init__.py
│       │
│       ├── economics/
│       ├── assets/
│       ├── interventions/
│       ├── lifecycle/
│       ├── risk/
│       ├── service/
│       ├── uncertainty/
│       ├── portfolio/
│       ├── optimization/
│       ├── planning/
│       └── visualization/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── examples/
│   ├── 00_asset_management_risk_plan_templates/
│   │   ├── README.md
│   │   ├── 01_asset_risk_assessment_plan.md
│   │   ├── 02_risk_based_capital_prioritization_plan.md
│   │   ├── 03_asset_risk_register.md
│   │   ├── 04_project_risk_evaluation.md
│   │   ├── 05_capital_funding_scenario_analysis.md
│   │   └── 06_risk_reduction_forecast.md
│   │
│   ├── 01_engineering_economics/
│   │   ├── README.md
│   │   ├── present_value/
│   │   ├── life_cycle_cost/
│   │   ├── equivalent_annual_cost/
│   │   └── benefit_cost_analysis/
│   │
│   ├── 02_asset_risk_assessment/
│   │   ├── README.md
│   │   ├── probability_of_failure/
│   │   ├── consequence_of_failure/
│   │   ├── risk_scoring/
│   │   └── criticality/
│   │
│   ├── 03_risk_based_intervention/
│   │   ├── README.md
│   │   ├── intervention_alternatives/
│   │   ├── residual_risk/
│   │   ├── risk_reduction/
│   │   └── intervention_timing/
│   │
│   ├── 04_uncertainty_and_scenarios/
│   │   ├── README.md
│   │   ├── sensitivity_analysis/
│   │   ├── monte_carlo/
│   │   ├── expected_annual_loss/
│   │   └── scenario_analysis/
│   │
│   ├── 05_portfolio_prioritization/
│   │   ├── README.md
│   │   ├── project_ranking/
│   │   ├── risk_reduction_efficiency/
│   │   ├── multi_criteria_prioritization/
│   │   └── budget_constraints/
│   │
│   └── 06_multi_year_capital_planning/
│       ├── README.md
│       ├── funding_scenarios/
│       ├── deterioration_forecast/
│       ├── risk_reduction_forecast/
│       └── cip_optimization/
│
├── reports/
│   ├── figures/
│   └── generated/
│
└── scripts/
```

This represents the **anticipated mature structure**, not the required initial repository.

---

# 3. Documentation Architecture

The `docs/` directory is organized according to the type of information being documented.

```text
docs/
├── 00_project/
├── 01_architecture/
├── 02_methodology/
└── 03_reference/
```

Each directory answers a different question.

| Directory          | Primary Question                                      |
| ------------------ | ----------------------------------------------------- |
| `00_project/`      | What are we building and why?                         |
| `01_architecture/` | How is the system organized?                          |
| `02_methodology/`  | How are the analyses performed?                       |
| `03_reference/`    | What supporting information does the project rely on? |

This separation should be maintained as the project grows.

---

# 4. `docs/00_project/`

The `00_project/` directory defines the project before implementation decisions are made.

```text
00_project/
├── 00_overview.md
├── 01_scope.md
├── 02_deliverables.md
└── 03_roadmap.md
```

These documents collectively serve as the project definition.

---

## `00_overview.md`

Defines the high-level purpose and direction of the project.

It should answer:

* What is Infrastructure Lifecycle & Capital Planning?
* What problem is the project intended to address?
* Why is the problem important?
* What are the primary learning objectives?
* How do engineering, asset management, finance, and analytics intersect?
* What is the long-term vision?

The overview should remain conceptual rather than implementation-specific.

---

## `01_scope.md`

Defines the project boundaries.

It should identify:

* infrastructure domains included
* analytical capabilities included
* engineering economics scope
* lifecycle-analysis scope
* risk-analysis scope
* capital-planning scope
* software boundaries
* data boundaries
* explicitly excluded capabilities

The scope document exists partly to prevent unrelated capabilities from gradually becoming project requirements.

---

## `02_deliverables.md`

Defines the tangible outputs expected from the project.

Deliverables may include:

* analytical modules
* datasets
* case studies
* notebooks
* tested Python implementations
* lifecycle models
* risk models
* portfolio analyses
* capital-planning models
* visualizations
* decision reports

The deliverables document defines **what must eventually exist**, while the roadmap defines **when and in what sequence it should be developed**.

---

## `03_roadmap.md`

Defines the staged implementation sequence.

The roadmap should progress from foundational methods toward integrated decision analysis.

The planned progression is:

```text
Engineering Economics
        ↓
Individual Asset Lifecycle
        ↓
Lifecycle Cost Analysis
        ↓
Condition & Deterioration
        ↓
Risk-Based Decisions
        ↓
Levels of Service & Criticality
        ↓
Uncertainty
        ↓
Portfolio Prioritization
        ↓
Capital Constraints
        ↓
Multi-Year Capital Planning
        ↓
Decision Reporting
        ↓
Integrated Framework
```

The roadmap is intentionally progressive so that later capabilities depend on methods developed and validated earlier.

---

# 5. `docs/01_architecture/`

The `01_architecture/` directory defines how the analytical system is designed.

```text
01_architecture/
├── 00_architecture.md
├── 01_structure.md
├── 02_domain_model.md
├── 03_data_architecture.md
└── 04_decision_pipeline.md
```

Only architecture documents needed for the current stage should be created.

The initial repository may contain only:

```text
01_architecture/
├── 00_architecture.md
└── 01_structure.md
```

Additional architecture documentation should be introduced as the implementation requires it.

---

## `00_architecture.md`

Defines the high-level analytical and software architecture.

It should eventually describe:

* architectural principles
* major analytical components
* relationships between components
* dependency direction
* separation of domain logic from presentation
* analytical workflow
* integration boundaries

At a conceptual level:

```text
Asset Data
    ↓
Asset State
    ↓
Condition / Deterioration
    ↓
Risk
    ↓
Intervention Alternatives
    ↓
Lifecycle Economics
    ↓
Uncertainty
    ↓
Portfolio Prioritization
    ↓
Capital Planning
    ↓
Decision Outputs
```

---

## `01_structure.md`

Defines the physical organization of the repository.

This document explains:

* directory responsibilities
* documentation organization
* source-code organization
* notebook organization
* data organization
* testing organization
* naming conventions
* progressive expansion rules

---

## `02_domain_model.md`

Defines the major concepts represented by the software.

Potential domain objects include:

```text
Asset
Condition
Intervention
Alternative
CashFlow
Risk
LevelOfService
Project
Portfolio
CapitalPlan
```

This document should not be created in detail until the project reaches the point where stable domain abstractions are necessary.

---

## `03_data_architecture.md`

Defines how analytical data moves through the project.

Potential concerns include:

* source data
* synthetic data
* validation
* transformation
* asset records
* cost records
* analysis-ready data
* generated outputs

A conceptual flow may eventually resemble:

```text
Raw Data
   ↓
Validation
   ↓
Interim Data
   ↓
Transformation
   ↓
Processed Data
   ↓
Domain Models
   ↓
Analysis
   ↓
Decision Outputs
```

---

## `04_decision_pipeline.md`

Defines the end-to-end analytical decision workflow.

It should eventually describe how the project moves from infrastructure information to a capital recommendation.

```text
Asset
  ↓
Condition
  ↓
Remaining Useful Life
  ↓
Probability of Failure
  ↓
Consequence of Failure
  ↓
Risk
  ↓
Intervention Alternatives
  ↓
Lifecycle Economics
  ↓
Risk Reduction
  ↓
Portfolio Comparison
  ↓
Capital Constraint
  ↓
Investment Plan
```

---

# 6. `docs/02_methodology/`

The `02_methodology/` directory documents the engineering, financial, statistical, and decision-analysis methods used by the project.

```text
02_methodology/
├── 00_methodology_overview.md
├── engineering_economics.md
├── lifecycle_cost_analysis.md
├── condition_and_deterioration.md
├── remaining_useful_life.md
├── risk_methodology.md
├── criticality.md
├── levels_of_service.md
├── uncertainty.md
└── capital_prioritization.md
```

Methodology documentation should explain **how an analysis works**, independently from its Python implementation.

A methodology document should generally include:

* purpose
* conceptual basis
* equations
* variables
* units
* assumptions
* engineering interpretation
* limitations
* references
* relationship to other methods

For example:

```text
02_methodology/
└── engineering_economics.md
```

might document:

$$
PV = \frac{FV}{(1+r)^n}
$$

and explain the meaning and appropriate use of the calculation.

The Python implementation belongs under `src/`.

---

# 7. `docs/03_reference/`

The `03_reference/` directory contains supporting project information.

```text
03_reference/
├── README.md
├── glossary.md
├── assumptions.md
└── references.md
```

---

## `glossary.md`

Defines terminology used throughout the project.

Potential terms include:

* asset
* condition
* criticality
* probability of failure
* consequence of failure
* risk
* remaining useful life
* lifecycle cost
* intervention
* rehabilitation
* replacement
* level of service
* capital improvement plan

---

## `assumptions.md`

Maintains a centralized record of important project-level assumptions.

Examples may include:

* discount rate
* inflation assumptions
* construction escalation
* planning horizon
* service-life assumptions
* condition scales

Detailed assumptions associated with individual analyses may remain with the corresponding methodology or case study.

---

## `references.md`

Identifies technical sources used by the project.

Potential references include:

* engineering economics texts
* infrastructure asset-management guidance
* ISO 55000 concepts
* IAM/GFMAM guidance
* AWWA guidance
* EPA guidance
* reliability references
* public datasets
* published infrastructure service-life information

External copyrighted material should not be committed unless redistribution is permitted.

---

# 8. `data/`

The `data/` directory contains datasets used for analysis.

```text
data/
├── raw/
├── interim/
├── processed/
└── synthetic/
```

## `raw/`

Contains original source data.

Raw data should remain unchanged after acquisition.

## `interim/`

Contains partially cleaned or transformed data.

## `processed/`

Contains analysis-ready datasets.

## `synthetic/`

Contains generated datasets used for learning, testing, and demonstrations.

Synthetic data should represent realistic engineering relationships and should be documented.

Not every project stage will require all four directories.

---

# 9. `notebooks/`

The `notebooks/` directory contains exploratory analysis, worked examples, and learning exercises.

```text
notebooks/
├── 01_engineering_economics/
├── 02_asset_lifecycle/
├── 03_lifecycle_cost/
├── 04_condition_deterioration/
├── 05_risk/
├── 06_levels_of_service/
├── 07_uncertainty/
├── 08_portfolio_prioritization/
├── 09_capital_optimization/
└── 10_multi_year_planning/
```

The notebook sequence should generally follow the staged roadmap.

Notebooks are intended to support:

* learning
* derivation
* experimentation
* visualization
* validation
* worked examples

Reusable analytical logic should eventually move from notebooks into `src/`.

The intended progression is:

```text
Learn
  ↓
Explore
  ↓
Validate
  ↓
Implement
  ↓
Test
  ↓
Reuse
```

---

# 10. `src/`

Reusable Python code belongs under:

```text
src/
└── infrastructure_capital_planning/
```

The anticipated mature package may include:

```text
infrastructure_capital_planning/
├── economics/
├── assets/
├── interventions/
├── lifecycle/
├── risk/
├── service/
├── uncertainty/
├── portfolio/
├── optimization/
├── planning/
└── visualization/
```

These modules should **not all be created initially**.

Each package should be introduced when its corresponding analytical capability reaches implementation.

---

# 11. `economics/`

Contains engineering economics calculations.

Potential responsibilities include:

* cash flows
* discounting
* present value
* future value
* NPV
* equivalent annual cost
* inflation
* escalation

This module provides financial mathematics used by lifecycle analysis.

It should remain independent from higher-level asset-management logic.

---

# 12. `assets/`

Contains representations of infrastructure assets and their physical state.

Potential responsibilities include:

* asset attributes
* age
* condition
* deterioration
* expected service life
* remaining useful life

---

# 13. `interventions/`

Contains representations of actions taken on infrastructure assets.

Potential interventions include:

* inspection
* maintenance
* rehabilitation
* replacement

Interventions may modify:

* condition
* remaining life
* cost
* probability of failure
* residual risk

---

# 14. `lifecycle/`

Contains lifecycle analysis and alternative-comparison logic.

Conceptually:

```text
Asset
  +
Intervention Strategy
  +
Planning Horizon
  +
Cash Flows
      ↓
Lifecycle Result
```

---

# 15. `risk/`

Contains risk-related calculations.

The architecture should preserve distinctions between:

```text
Probability of Failure
        ×
Consequence of Failure
        ↓
       Risk
```

Criticality may inform consequence calculations without being treated as interchangeable with risk.

---

# 16. `service/`

Contains level-of-service concepts connecting asset performance with utility objectives.

This package may remain small and should only be created when the roadmap reaches level-of-service analysis.

---

# 17. `uncertainty/`

Contains methods for evaluating uncertainty.

Potential capabilities include:

* sensitivity analysis
* scenario analysis
* Monte Carlo simulation

Deterministic models should be established before probabilistic methods are introduced.

---

# 18. `portfolio/`

Contains methods involving multiple infrastructure assets.

Potential responsibilities include:

* asset comparison
* prioritization
* risk reduction
* investment efficiency

Portfolio analysis should consume results from individual asset analyses rather than duplicate them.

---

# 19. `optimization/`

Contains methods for selecting investments under constraints.

Potential later-stage capabilities include:

* budget constraints
* project selection
* linear programming
* integer programming
* constrained optimization
* multi-objective optimization

Advanced optimization is not required during early development.

---

# 20. `planning/`

Contains multi-year capital-planning logic.

Potential responsibilities include:

* annual funding allocation
* project timing
* project deferral
* escalation
* changing risk
* annual expenditure forecasts
* unfunded needs

This represents one of the later integration stages of the project.

---

# 21. `visualization/`

Contains reusable decision-oriented visualization functions.

Potential outputs include:

* deterioration curves
* lifecycle cash-flow diagrams
* lifecycle cost comparisons
* risk matrices
* risk-versus-cost plots
* capital expenditure forecasts
* cumulative risk reduction

Visualization should remain separate from analytical calculations.

---

# 22. `tests/`

Automated tests should mirror the analytical source structure where practical.

```text
tests/
├── unit/
├── integration/
└── fixtures/
```

## Unit Tests

Validate individual calculations.

## Integration Tests

Validate workflows spanning multiple modules.

## Fixtures

Provide reusable test assets, cash flows, datasets, and scenarios.

Testing should distinguish between:

* software correctness
* model validity

Both are necessary for credible engineering analysis.

---

# 23. `examples/`

The `examples/` directory contains clean demonstrations of completed capabilities.

```text
examples/
├── 01_engineering_economics/
├── 02_single_asset/
├── 03_risk_based_intervention/
├── 04_uncertainty/
├── 05_asset_portfolio/
└── 06_multi_year_cip/
```

Examples differ from notebooks.

**Notebooks** document exploration and learning.

**Examples** demonstrate completed and tested capabilities.

---

# 24. `reports/`

Contains generated analytical outputs.

```text
reports/
├── figures/
└── generated/
```

Potential outputs include:

* figures
* analysis summaries
* lifecycle comparisons
* capital plans
* decision reports

Only outputs with lasting project value should normally be committed to version control.

---

# 25. `scripts/`

Contains supporting command-line utilities.

Potential examples include:

```text
generate_synthetic_assets.py
validate_data.py
```

Scripts should orchestrate functionality from `src/` rather than duplicate analytical logic.

---

# 26. Dependency Direction

The architecture should maintain a logical dependency direction.

At maturity, the general analytical flow is expected to resemble:

```text
Asset Data
    ↓
Asset Representation
    ↓
Condition & Deterioration
    ↓
Remaining Useful Life
    ↓
Risk
    ↓
Intervention Alternatives
    ↓
Lifecycle Economics
    ↓
Uncertainty Analysis
    ↓
Portfolio Prioritization
    ↓
Capital Optimization
    ↓
Multi-Year Planning
    ↓
Decision Outputs
```

Lower-level analytical modules should not depend on higher-level planning modules.

For example:

```text
economics/
```

should not depend on:

```text
planning/
```

Engineering economics should remain usable independently of capital-planning workflows.

---

# 27. Development Workflow

New analytical capabilities should generally progress through:

```text
Project Definition
       ↓
Methodology
       ↓
Exploration
       ↓
Validation
       ↓
Architecture
       ↓
Implementation
       ↓
Testing
       ↓
Demonstration
```

In repository terms:

```text
docs/
  ↓
notebooks/
  ↓
src/
  ↓
tests/
  ↓
examples/
```

Architecture documentation should be updated when new capabilities materially change system organization or component relationships.

---

# 28. Initial Repository Structure

The complete target structure should **not** be created at project initialization.

An appropriate starting structure is:

```text
infrastructure-lifecycle-capital-planning/
│
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .python-version
│
├── docs/
│   ├── 00_project/
│   │   ├── 00_overview.md
│   │   ├── 01_scope.md
│   │   ├── 02_deliverables.md
│   │   └── 03_roadmap.md
│   │
│   └── 01_architecture/
│       ├── 00_architecture.md
│       └── 01_structure.md
│
├── notebooks/
│   └── 01_engineering_economics/
│
├── src/
│   └── infrastructure_capital_planning/
│       ├── __init__.py
│       └── economics/
│
└── tests/
    └── unit/
        └── economics/
```

The first implementation stage therefore remains focused on:

> **engineering economics**

rather than creating empty packages for future capabilities.

---

# 29. Expansion Rule

A new directory or package should generally be created only when at least one of the following is true:

1. The corresponding roadmap stage has begun.
2. Reusable code exists that logically belongs in the package.
3. Documentation is needed to define an upcoming implementation.
4. Existing modules have become sufficiently complex that separation improves clarity.
5. A new domain concept has become stable enough to justify its own abstraction.

Directories should not be created solely because they appear in the target architecture.

---

# 30. Structural Principle

The repository should evolve from a small, understandable analytical project into a larger decision-support framework.

The intended progression is:

```text
Simple
  ↓
Correct
  ↓
Validated
  ↓
Reusable
  ↓
Integrated
  ↓
Sophisticated
```

not:

```text
Sophisticated
  ↓
Complicated
  ↓
Eventually Understand It
```

The architecture should therefore grow in response to demonstrated analytical requirements rather than anticipated complexity.
