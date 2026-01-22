# Causal Inference Course Materials

This repository contains teaching materials for a 10-week course on causal inference, aimed at undergraduate and master's level business students. 

The course covers:

- How (and when) we can use data to learn about cause-effect relationships in the world (***"causal inference"***)
- How we can use causal concepts to make better decisions, particularly in business settings (***"causal reasoning"***)

Many students who take the course have little statistical training and have never done any programming before, so the materials are designed to focus on building intuition with case studies and demonstrations. 

The R demo files explore key concepts using simulated data and real-world datasets. They are written to use a minimal number of R functions, mainly from the tidyverse and fixest packages. The "_blank" R Markdown files can be used as templates for in-class coding demonstrations.

Past assignments and answer keys are available upon request.


## Course Outline

### Weekly Topics

1. **Introduction to Causality** - Intro to the Potential Outcomes framework, counterfactuals, and the fundamental problem of causal inference
2. **Confounders** - Intro to Directed Acyclic Graphs (DAGs) and identifying confounding relationships
3. **Randomized Experiments** - Why randomization works and how to analyze experimental data
4. **Controlling for Observables** - Building an intuition for how controlling for variables can help identify causal effects
5. **Good and Bad Controls** - Understanding which variables we should control for (and which we should *not* control for)
6. **Regression for Causal Inference** - Intro to linear regression and how regression can be used to estimate causal effects
7. **Intro to Difference-in-Differences** - Event studies, fixed effects, and the parallel trends assumption
8. **Difference-in-Differences** - Dynamic treatment effects and advanced DiD designs
9. **Natural Experiments** - Instrumental variables and regression discontinuity designs
10. **Machine Learning Methods** - A high-level intro to how machine learning can aid causal inference by flexibly controlling for confounders and estimating of heterogeneous treatment effects

### Readings

- Week 1:





## Repository Contents

### Slides

The `slides/` directory contains lecture materials in markdown format. These slides use the Beamer framework and can be converted to PDF using the included `toBeamerPDF.py` script.

Core lectures:

- `01_IntroToCausality.md` - Potential outcomes and the eBay advertising case
- `02_confounders.md` - DAGs and identifying confounding
- `03_experiments.md` - Randomized experiments and estimation
- `04_controlling.md` - Introduction to controlling for observables
- `05_GoodAndBadControls.md` - When to (and not to) control for variables
- `06_regression.md` - Regression as a tool for causal inference
- `07_IntroToDiD.md` - Event studies and introduction to difference-in-differences
- `08_DiD.md` - Difference-in-differences designs in depth
- `09_NaturalExperiments.md` - Instrumental variables and regression discontinuity
- `10_ML.md` - Machine learning methods for causal inference

Appendices:
- `A1_StatisticalInference.md` - Statistical inference refresher
- `A2_MatchingWeightingAndMore.md` - Advanced methods for controlling

### R Demos

The `R_demos/` directory contains R Markdown files demonstrating the concepts covered in lectures through simulated examples and real data applications.

### Activities

The `activities/` directory contains materials for two in-class activities.

### Data

The `data/` directory contains datasets used in demos and exercises.

## Recommended Textbooks

- ***The Effect: An Introduction to Research Design and Causality*** by Nick Huntington-Klein
- ***R for Data Science*** by Hadley Wickham & Garrett Grolemund

## Applications

These materials emphasize real-world applications of causal inference methods, including examples from:

- **Online advertising effectiveness** (eBay keyword ads)
- **Product features and safety** (Tesla Autopilot)
- **Policy evaluation** (minimum wage, environmental regulations)
- **Technology adoption** (Netflix password sharing, Spotify recommendations)
- **Labor economics** (returns to education, work-from-home policies)

## About

These materials were developed by Brad Hackinen for use in graduate business education. The course assumes familiarity with basic statistics and regression, and uses R for all computational examples.

## License

These materials are provided for educational purposes. Feel free to use and adapt them for your own teaching, with attribution.
