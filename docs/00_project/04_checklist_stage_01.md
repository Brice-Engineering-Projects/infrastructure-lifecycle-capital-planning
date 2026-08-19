# Stage 1 — Engineering Economics Foundation Checklist

## 1. Core Economic Calculations

### 1.1 Time-Value-of-Money Calculations

* [x] Implement present value of a single future cash flow
* [ ] Implement future value of a single present cash flow
* [x] Implement present value of a uniform recurring series
* [ ] Implement future value of a uniform recurring series
* [x] Implement present value of an escalating recurring series
* [ ] Implement discount-factor calculations
* [ ] Implement compound-factor calculations

### 1.2 Cash-Flow Analysis

* [ ] Discount individual cash flows occurring at specified periods
* [ ] Discount irregular cash-flow schedules
* [ ] Calculate net present value of a cash-flow schedule
* [ ] Support cash flows occurring at year zero
* [ ] Support positive and negative cash flows
* [ ] Support residual and salvage values
* [ ] Define and document cash-flow timing conventions
* [ ] Define and document cash-flow sign conventions

### 1.3 Economic Assumptions

* [ ] Support configurable analysis periods
* [ ] Support configurable discount rates
* [ ] Support inflation assumptions
* [ ] Support cost-escalation assumptions
* [ ] Distinguish between real and nominal discount rates
* [ ] Define consistent treatment of inflation and escalation
* [ ] Prevent inconsistent combinations of real and nominal assumptions where appropriate

### 1.4 Annualized Economic Measures

* [ ] Implement capital recovery calculations
* [ ] Implement equivalent annual cost calculations
* [ ] Convert lifecycle present values to equivalent annual costs
* [ ] Support comparison of alternatives using equivalent annual cost

---

## 2. Lifecycle Cash-Flow Modeling

### 2.1 Cash-Flow Representation

* [ ] Define a common representation for lifecycle cash flows
* [ ] Associate each cash flow with a time period
* [ ] Associate each cash flow with an amount
* [ ] Support categorization of cash flows by type
* [ ] Preserve sufficient metadata to identify the source of each lifecycle cost

### 2.2 Lifecycle Cost Components

* [ ] Represent initial capital costs
* [ ] Represent engineering and construction costs
* [ ] Represent recurring O&M costs
* [ ] Represent inspection and monitoring costs
* [ ] Represent preventive maintenance costs
* [ ] Represent corrective maintenance costs
* [ ] Represent periodic major maintenance costs
* [ ] Represent rehabilitation costs
* [ ] Represent future replacement costs
* [ ] Represent emergency repair costs where applicable
* [ ] Represent residual and salvage values

### 2.3 Lifecycle Cash-Flow Generation

* [ ] Generate lifecycle cash-flow schedules from defined assumptions
* [ ] Generate recurring costs at specified intervals
* [ ] Generate periodic maintenance costs
* [ ] Generate rehabilitation costs at specified intervention years
* [ ] Generate replacement costs at specified replacement years
* [ ] Apply inflation or escalation where appropriate
* [ ] Apply residual or salvage value at the end of the analysis period
* [ ] Discount lifecycle cash flows to present value
* [ ] Calculate total lifecycle present value
* [ ] Calculate equivalent annual lifecycle cost

---

## 3. Intervention Alternatives

### 3.1 Intervention Model

* [ ] Define a common intervention-alternative model
* [ ] Define a unique identifier or name for each alternative
* [ ] Associate an intervention year with each alternative
* [ ] Associate an expected service-life effect with each alternative
* [ ] Associate lifecycle costs with each alternative
* [ ] Associate recurring post-intervention costs where appropriate
* [ ] Preserve assumptions used to construct each alternative

### 3.2 Intervention Types

* [ ] Support a do-nothing or continue-operation alternative
* [ ] Support inspection or increased-monitoring alternatives
* [ ] Support preventive-maintenance alternatives
* [ ] Support repair alternatives
* [ ] Support rehabilitation alternatives
* [ ] Support partial-replacement alternatives
* [ ] Support full-replacement alternatives
* [ ] Support operate-to-failure alternatives

### 3.3 Intervention Timing

* [ ] Support immediate intervention
* [ ] Support deferred intervention
* [ ] Support multiple interventions during an analysis period
* [ ] Represent service-life extension resulting from rehabilitation
* [ ] Represent asset replacement and lifecycle reset
* [ ] Support different intervention timing among competing alternatives

---

## 4. Alternative Comparison

### 4.1 Common Economic Basis

* [ ] Compare alternatives over a common analysis period
* [ ] Apply consistent economic assumptions across alternatives
* [ ] Apply consistent cash-flow timing conventions
* [ ] Apply consistent inflation and escalation assumptions
* [ ] Apply consistent treatment of residual value

### 4.2 Different Service Lives

* [ ] Support alternatives with different expected service lives
* [ ] Account for replacement cycles occurring within the analysis period
* [ ] Account for remaining service life at the end of the analysis period
* [ ] Calculate residual value where an alternative retains useful life beyond the analysis period
* [ ] Use equivalent annual cost where appropriate for alternatives with unequal service lives

### 4.3 Economic Comparison Results

* [ ] Calculate lifecycle present value for each alternative
* [ ] Calculate equivalent annual cost for each alternative
* [ ] Produce structured comparison results
* [ ] Rank alternatives by lifecycle economic cost
* [ ] Identify the lowest lifecycle-cost alternative
* [ ] Preserve individual cost components within comparison results
* [ ] Preserve intervention timing within comparison results
* [ ] Preserve assumptions used for each comparison
* [ ] Preserve results required by later risk and decision-support stages

### 4.4 Engineering Interpretation

* [ ] Distinguish economic comparison from engineering recommendation
* [ ] Avoid automatically treating lowest lifecycle cost as the preferred engineering alternative
* [ ] Identify economic tradeoffs among alternatives
* [ ] Document limitations of economic-only comparisons
* [ ] Prepare comparison outputs for later integration with risk, level-of-service, and uncertainty analysis

---

## 5. Validation

### 5.1 Hand-Calculated Validation

* [ ] Develop hand-calculated validation case for single-payment present value
* [ ] Develop hand-calculated validation case for single-payment future value
* [ ] Develop hand-calculated validation case for a uniform recurring series
* [ ] Develop hand-calculated validation case for an escalating recurring series
* [ ] Develop hand-calculated validation case for an irregular cash-flow schedule
* [ ] Develop hand-calculated validation case for net present value
* [ ] Develop hand-calculated validation case for equivalent annual cost

### 5.2 Independent Validation

* [ ] Compare calculations against spreadsheet calculations
* [ ] Compare calculations against published engineering-economics examples
* [ ] Verify closed-form calculations against explicitly generated cash-flow schedules where applicable
* [ ] Document expected values used in validation cases

### 5.3 Unit Testing

* [x] Develop unit tests for present-value functions
* [ ] Develop unit tests for future-value functions
* [ ] Develop unit tests for discount-factor calculations
* [ ] Develop unit tests for cash-flow discounting
* [ ] Develop unit tests for net present value
* [ ] Develop unit tests for equivalent annual cost
* [ ] Develop tests for lifecycle cash-flow generation
* [ ] Develop tests for intervention timing
* [ ] Develop tests for alternative comparisons

### 5.4 Boundary and Edge Cases

* [ ] Test zero discount rate where mathematically valid
* [ ] Test zero-length or minimum-length analysis periods
* [ ] Test year-zero cash flows
* [ ] Test positive and negative cash flows
* [ ] Test zero-value cash flows
* [ ] Test residual and salvage values
* [ ] Test alternatives with no recurring costs
* [ ] Test alternatives requiring multiple replacements
* [ ] Test alternatives with service life extending beyond the analysis period
* [ ] Test invalid discount-rate inputs
* [ ] Test invalid analysis-period inputs
* [ ] Verify consistent treatment of costs, savings, and residual values

---

## 6. Representative Engineering Scenario

### 6.1 Scenario Definition

* [ ] Select a representative municipal infrastructure asset
* [ ] Define the asset's current age
* [ ] Define the asset's expected service life
* [ ] Define the asset's current condition and relevant engineering context
* [ ] Establish an appropriate economic analysis period
* [ ] Establish discount-rate assumptions
* [ ] Establish inflation and escalation assumptions
* [ ] Document all major economic assumptions

### 6.2 Intervention Alternatives

* [ ] Define a realistic continue-operation or do-nothing alternative
* [ ] Define a realistic repair or maintenance alternative
* [ ] Define a realistic rehabilitation alternative
* [ ] Define a realistic replacement alternative
* [ ] Establish intervention timing for each alternative
* [ ] Establish service-life assumptions for each alternative
* [ ] Establish realistic initial and future costs for each alternative
* [ ] Establish realistic O&M and maintenance assumptions

### 6.3 Lifecycle Analysis

* [ ] Generate lifecycle cash flows for each alternative
* [ ] Apply inflation or escalation assumptions
* [ ] Apply discounting
* [ ] Account for future rehabilitation or replacement cycles
* [ ] Account for residual value where appropriate
* [ ] Calculate lifecycle present value for each alternative
* [ ] Calculate equivalent annual cost for each alternative

### 6.4 Results and Interpretation

* [ ] Compare alternatives on a consistent economic basis
* [ ] Identify major drivers of lifecycle cost
* [ ] Identify the lowest lifecycle-cost alternative
* [ ] Explain why lowest lifecycle cost does not necessarily determine the final engineering recommendation
* [ ] Document the economic results
* [ ] Provide an engineering interpretation of the comparison
* [ ] Identify information that will be incorporated during later risk and uncertainty stages

---

## 7. Software Design and Architecture

### 7.1 Core Economics Design

* [ ] Implement core financial mathematics as stateless functions where appropriate
* [ ] Define clear function signatures
* [ ] Use full Python type hints
* [ ] Provide docstrings describing parameters, returns, assumptions, and conventions
* [ ] Keep core economic calculations independent of infrastructure-specific asset types
* [ ] Avoid unnecessary specialized financial functions when general cash-flow calculations provide the required capability

### 7.2 Domain Models

* [ ] Determine whether a `CashFlow` domain model is required
* [ ] Determine whether a `CashFlowSchedule` domain model is required
* [ ] Determine whether an `EconomicAssumptions` model is required
* [ ] Define an `InterventionAlternative` model
* [ ] Keep infrastructure-domain state separate from pure economic calculations
* [ ] Design domain models to support later lifecycle, risk, uncertainty, and portfolio stages

### 7.3 Package Responsibilities

* [ ] Define the responsibility of `economics/`
* [ ] Define the responsibility of `assets/`
* [ ] Define the responsibility of `interventions/`
* [ ] Define the responsibility of `lifecycle/`
* [ ] Prevent lifecycle or intervention logic from leaking unnecessarily into core economic functions
* [ ] Document dependencies between Stage 1 packages
* [ ] Avoid circular dependencies between economic and domain modules

### 7.4 Extensibility

* [ ] Ensure lifecycle results can later incorporate failure risk
* [ ] Ensure economic assumptions can later support sensitivity analysis
* [ ] Ensure model inputs can later support probability distributions
* [ ] Ensure lifecycle calculations can later support Monte Carlo simulation
* [ ] Ensure alternative results can later feed portfolio analysis
* [ ] Ensure alternative results can later feed capital optimization
* [ ] Ensure calculations remain usable at both individual-asset and portfolio scales

---

## 8. Documentation

### 8.1 Economic Methodology

* [ ] Document present-value methodology
* [ ] Document future-value methodology
* [ ] Document recurring-series methodology
* [ ] Document escalating-series methodology
* [ ] Document net-present-value methodology
* [ ] Document equivalent-annual-cost methodology
* [ ] Document real versus nominal discount rates
* [ ] Document inflation and escalation treatment

### 8.2 Modeling Conventions

* [ ] Document cash-flow sign conventions
* [ ] Document cash-flow timing conventions
* [ ] Document treatment of year-zero costs
* [ ] Document treatment of recurring costs
* [ ] Document treatment of residual and salvage values
* [ ] Document treatment of alternatives with different service lives
* [ ] Document analysis-period assumptions

### 8.3 Engineering Context

* [ ] Explain the role of engineering economics within infrastructure lifecycle analysis
* [ ] Explain why lifecycle cost is preferred over initial-cost-only comparisons
* [ ] Explain the limitations of economic-only decision making
* [ ] Explain how Stage 1 outputs will later integrate with risk analysis
* [ ] Explain how Stage 1 outputs will later integrate with uncertainty analysis
* [ ] Explain how Stage 1 outputs will later support capital prioritization

---

# Stage 1 Completion Criteria

* [ ] Core time-value-of-money calculations are implemented and tested
* [ ] Single, recurring, escalating, and irregular cash flows can be evaluated
* [ ] Cash-flow timing and sign conventions are explicitly defined
* [ ] Real and nominal economic assumptions are handled consistently
* [ ] Lifecycle cash-flow schedules can be generated from infrastructure intervention assumptions
* [ ] Lifecycle present value can be calculated for each intervention alternative
* [ ] Equivalent annual cost can be calculated where appropriate
* [ ] Multiple infrastructure alternatives can be evaluated consistently
* [ ] Alternatives with different service lives can be compared
* [ ] Deferred interventions and replacement cycles can be represented
* [ ] Residual and salvage values can be represented consistently
* [ ] Core calculations have been independently validated
* [ ] Unit and edge-case tests provide adequate coverage of Stage 1 calculations
* [ ] A representative infrastructure lifecycle decision has been completed end-to-end
* [ ] Economic results are separated from final engineering recommendations
* [ ] Stage 1 outputs provide a stable foundation for subsequent risk, uncertainty, portfolio, optimization, and capital-planning stages


# Classes vs Functions

* [ ] Decide whether to implement core economic calculations as classes or functions
* [ ] If using classes, define appropriate class structures and methods
* [ ] If using functions, define clear function signatures and documentation
* [ ] Ensure that the chosen approach supports extensibility for future stages
* [ ] Document the rationale for the chosen implementation approach

## Suggested List

```text
economics/
    Pure mathematical functions
        ↓
assets/
    Asset domain models
        ↓
interventions/
    Intervention domain models
        ↓
lifecycle/
    Combines assets + interventions + economics
        ↓
risk/
    Probability × consequence
        ↓
uncertainty/
    Uncertain inputs / simulation
        ↓
portfolio/
    Multiple assets / projects
        ↓
optimization/
    Resource allocation
        ↓
planning/
    Multi-year CIP
```
