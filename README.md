# Infrastructure Lifecycle & Capital Planning

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-blueviolet.svg)](https://docs.astral.sh/uv/)
[![Status](https://img.shields.io/badge/Status-Planned-lightgrey.svg)]()
[![Domain](https://img.shields.io/badge/Domain-Infrastructure%20Asset%20Management-green.svg)]()

> A Python-based engineering analytics project for evaluating infrastructure lifecycle strategies, investment alternatives, and capital planning decisions.

---

## Overview

**Infrastructure Lifecycle & Capital Planning** explores how engineering condition, asset performance, failure risk, intervention alternatives, lifecycle costs, and capital constraints can be combined to support defensible infrastructure investment decisions.

The project bridges:

* **Infrastructure Engineering**
* **Asset Management**
* **Engineering Economics**
* **Risk Analysis**
* **Decision Analytics**
* **Capital Planning**

The central question is:

> **Given limited capital, when should infrastructure assets be maintained, rehabilitated, or replaced to provide the greatest long-term value while managing risk and maintaining acceptable levels of service?**

The project is designed first as a **learning and engineering decision-analysis platform**, with the long-term goal of developing reusable methods for infrastructure lifecycle and capital investment planning.

---

## Why This Project?

Infrastructure owners rarely have enough funding to address every identified asset need at once.

A utility may face hundreds of millions of dollars in potential:

* maintenance
* rehabilitation
* replacement
* regulatory
* resilience
* capacity

needs while operating under constrained annual capital budgets.

The engineering problem therefore extends beyond identifying assets that are old or in poor condition.

Decision-makers must determine:

* Which assets require intervention?
* When should intervention occur?
* Should an asset be maintained, rehabilitated, replaced, or operated to failure?
* What does each alternative cost over its full lifecycle?
* What risk is associated with delaying intervention?
* How much risk does an investment reduce?
* Which investments provide the greatest long-term value?
* How should limited capital be allocated across competing needs?
* How should investments be scheduled across multiple years?

This project develops the analytical methods needed to investigate those questions systematically.

---

## Decision Framework

The project follows a general infrastructure investment decision process:

```text
Asset Inventory
      ↓
Asset Condition
      ↓
Performance & Remaining Life
      ↓
Failure Risk
      ↓
Levels of Service
      ↓
Intervention Alternatives
      ↓
Lifecycle Cost Analysis
      ↓
Economic Comparison
      ↓
Capital Constraints
      ↓
Investment Prioritization
      ↓
Multi-Year Capital Plan
```

The objective is not to automate engineering decisions.

The objective is to improve the **consistency, transparency, and defensibility** of those decisions.

---

## Project Focus

The project primarily focuses on municipal **water and wastewater infrastructure**, including potential applications to:

* water mains
* force mains
* gravity sewers
* pumps
* lift stations
* pump stations
* storage facilities
* treatment assets
* mechanical equipment
* electrical equipment

The underlying methods may eventually be applicable to other infrastructure sectors.

---

## Core Analytical Areas

### Engineering Economics

Financial mathematics provides the foundation for comparing infrastructure alternatives whose costs occur at different points in time.

Topics include:

* present value
* future value
* discounting
* net present value
* equivalent annual cost
* inflation
* escalation
* residual value
* cash-flow modeling

---

### Asset Lifecycle Analysis

Infrastructure decisions are evaluated across the full asset lifecycle.

Topics include:

* asset age
* condition
* deterioration
* expected service life
* remaining useful life
* maintenance
* rehabilitation
* replacement
* intervention timing

---

### Lifecycle Cost Analysis

Investment alternatives are compared based on their total economic impact rather than initial capital cost alone.

Potential costs include:

* capital
* engineering
* construction
* inspection
* maintenance
* operations
* energy
* rehabilitation
* emergency repair
* replacement
* disposal
* residual value

---

### Risk-Based Decision Making

Infrastructure risk is represented conceptually as:

$$
\text{Risk}
===========

\text{Probability of Failure}
\times
\text{Consequence of Failure}
$$

Potential consequences include:

* service interruption
* emergency repair
* environmental impacts
* regulatory impacts
* public health and safety
* property damage
* critical customer impacts
* loss of redundancy

The project evaluates how interventions change both lifecycle cost and infrastructure risk.

---

### Levels of Service

Asset investment decisions should ultimately support infrastructure service objectives.

Potential considerations include:

* reliability
* availability
* capacity
* pressure
* water quality
* regulatory compliance
* customer interruptions
* emergency response
* resilience

---

### Uncertainty

Infrastructure planning depends on assumptions that cannot be known with certainty.

The project will progressively explore:

* sensitivity analysis
* scenario analysis
* probability distributions
* Monte Carlo simulation

Potential uncertain variables include:

* remaining useful life
* deterioration
* construction cost
* escalation
* failure probability
* failure timing
* intervention effectiveness
* emergency repair cost

---

### Portfolio Prioritization

Individual asset decisions eventually become portfolio decisions.

The project will evaluate methods for comparing competing investments based on factors such as:

* condition
* risk
* criticality
* regulatory requirements
* level-of-service impacts
* lifecycle cost
* intervention cost
* risk reduction
* investment efficiency

---

### Capital Planning

The final analytical problem is not simply identifying the highest-priority asset.

It is determining:

> **Which combination of investments should be funded when identified infrastructure needs exceed available capital?**

Later stages will explore:

* annual budget constraints
* project selection
* project deferral
* capital optimization
* cost escalation
* changing risk
* project dependencies
* multi-year capital improvement planning

---

## Progressive Development

The project is intentionally developed in stages.

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

Advanced methods are introduced only after the underlying concepts and simpler analytical approaches have been understood and validated.

---

## Development Philosophy

### Engineering Comes First

Financial, statistical, and computational methods support infrastructure decisions. They do not replace engineering understanding.

### Learn Before Abstracting

New analytical concepts are explored and validated before being converted into reusable software components.

### Validate the Mathematics

Key engineering and financial calculations should be independently verified through hand calculations, published examples, spreadsheets, or alternative implementations.

### Separate Assumptions From Methods

Analytical methodology should remain distinct from project-specific assumptions such as discount rates, service lives, deterioration rates, and construction escalation.

### Make Uncertainty Visible

Infrastructure decisions should communicate uncertainty rather than conceal it behind overly precise deterministic results.

### Preserve Explainability

A recommendation should be traceable from:

```text
Input Data
    ↓
Engineering Assumptions
    ↓
Analytical Method
    ↓
Calculated Results
    ↓
Decision Criteria
    ↓
Recommendation
```

### Engineering Judgment Remains Essential

The project is intended to support professional judgment, not automate it.

---

## Documentation

Detailed project documentation is maintained under [`docs/`](docs/).

### Project Definition

[`docs/00_project/`](docs/00_project/)

Contains:

* project overview
* project scope
* project deliverables
* staged implementation roadmap

### Architecture

[`docs/01_architecture/`](docs/01_architecture/)

Contains:

* system architecture
* repository structure
* domain modeling
* data architecture
* analytical decision pipeline

Architecture documents are added progressively as the corresponding capabilities are developed.

### Methodology

[`docs/02_methodology/`](docs/02_methodology/)

Documents the engineering, financial, statistical, and decision-analysis methods implemented by the project.

### Reference

[`docs/03_reference/`](docs/03_reference/)

Contains supporting terminology, assumptions, references, standards, guidance, and technical sources.

For the detailed repository tree and directory responsibilities, see:

**[`docs/01_architecture/01_structure.md`](docs/01_architecture/01_structure.md)**

---

## Technology

Primary development technologies include:

* Python 3.12+
* NumPy
* pandas
* SciPy
* Matplotlib
* Jupyter
* pytest
* uv

Additional libraries may be introduced as required by later analytical stages.

Dependencies should be added in response to demonstrated requirements rather than anticipated functionality.

---

## Long-Term Vision

At maturity, the project should support an analytical workflow resembling:

```text
Asset Data
    ↓
Condition & Performance
    ↓
Deterioration
    ↓
Remaining Useful Life
    ↓
Failure Risk
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
Capital Optimization
    ↓
Multi-Year Investment Plan
    ↓
Decision Reporting
```

The ultimate objective is to move beyond asking:

> **Which assets are in the worst condition?**

toward answering:

> **Given asset condition, failure risk, lifecycle economics, service objectives, uncertainty, and limited funding, which infrastructure investments should be made, when should they occur, and why?**

---

## Project Status

**Status:** Planned / Initial Development

The project is currently in the project-definition and architecture stage.

Initial implementation will focus on **engineering economics** before progressing into asset lifecycle analysis and more advanced asset-management methods.

---

## Disclaimer

This project is intended for educational, research, and engineering decision-support purposes.

The methods, models, datasets, and examples developed within this repository are not substitutes for project-specific engineering analysis, professional judgment, utility policies, regulatory requirements, or formal asset-management programs.
