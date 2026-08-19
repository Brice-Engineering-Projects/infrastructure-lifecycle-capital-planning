# Stage 1 — Engineering Economics Foundation Checklist

## 1. Core Economic Calculations

* [ ] Implement present value calculations
* [ ] Implement future value calculations
* [ ] Implement cash-flow discounting
* [ ] Implement net present value calculations
* [ ] Implement equivalent annual cost calculations
* [ ] Support configurable analysis periods
* [ ] Support discount rates
* [ ] Support inflation and cost escalation
* [ ] Support residual and salvage values
* [ ] Define and document cash-flow sign conventions

## 2. Lifecycle Cash-Flow Modeling

* [ ] Represent initial capital costs
* [ ] Represent recurring O&M costs
* [ ] Represent periodic maintenance costs
* [ ] Represent rehabilitation costs
* [ ] Represent future replacement costs
* [ ] Represent residual values
* [ ] Generate lifecycle cash-flow schedules
* [ ] Apply escalation where appropriate
* [ ] Discount lifecycle cash flows to present value

## 3. Intervention Alternatives

* [ ] Define a common intervention-alternative model
* [ ] Support a do-nothing alternative
* [ ] Support repair alternatives
* [ ] Support rehabilitation alternatives
* [ ] Support replacement alternatives
* [ ] Associate service life with each alternative
* [ ] Associate lifecycle costs with each alternative

## 4. Alternative Comparison

* [ ] Compare alternatives over a common analysis period
* [ ] Calculate lifecycle present value for each alternative
* [ ] Calculate equivalent annual cost for each alternative
* [ ] Account for alternatives with different service lives
* [ ] Produce structured comparison results
* [ ] Identify the lowest lifecycle-cost alternative
* [ ] Preserve results needed for later decision-support stages

## 5. Validation

* [ ] Develop hand-calculated validation cases
* [ ] Compare results against spreadsheet calculations
* [ ] Compare calculations against published engineering economics examples
* [ ] Develop unit tests for core economic functions
* [ ] Develop tests for lifecycle cash-flow generation
* [ ] Develop tests for alternative comparisons
* [ ] Test boundary and edge cases
* [ ] Verify consistent treatment of costs, savings, and residual values

## 6. Representative Engineering Scenario

* [ ] Select a representative municipal infrastructure asset
* [ ] Define realistic do-nothing, repair, rehabilitation, and replacement alternatives
* [ ] Establish realistic lifecycle assumptions
* [ ] Generate lifecycle cash flows for each alternative
* [ ] Compare alternatives using lifecycle present value and equivalent annual cost
* [ ] Document the economic results
* [ ] Provide an engineering interpretation of the comparison

## Stage 1 Completion Criteria

* [ ] Core engineering economics calculations are implemented and tested
* [ ] Lifecycle cash flows can be generated from intervention assumptions
* [ ] Multiple infrastructure alternatives can be evaluated consistently
* [ ] Alternatives with different service lives can be compared
* [ ] Results have been independently validated
* [ ] A representative infrastructure lifecycle decision has been completed end-to-end
* [ ] Stage 1 outputs provide a stable foundation for subsequent risk, uncertainty, portfolio, and capital-planning stages

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
