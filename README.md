# Pharmaceutical Data Analysis

Portfolio project using public pharmaceutical datasets, beginning with **openFDA** adverse-event data and later integrating **ChEMBL** pharmacology data.

## Project direction

The project will explore questions such as:

- How do adverse-event profiles differ across drugs and drug classes?
- Which reactions are most commonly reported for selected drugs?
- How do serious outcomes and reported tolerability patterns differ across drugs?
- Do drugs with similar target or mechanism profiles also show similar adverse-event profiles?
- Can differences in targets, mechanisms, or bioactivity help generate hypotheses about differences in observed safety profiles?

Initial API exploration is using GLP-1-based drugs while learning the openFDA workflow. Antidepressants are a planned major analysis area.

## Data sources

- **openFDA Drug Adverse Event API** — FAERS adverse-event reports.
- **ChEMBL** — compounds, drug mechanisms, biological targets, assays, and bioactivity data.

## Planned repository structure

```text
pharmaceutical-data-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── python/
├── sql/
├── docs/
├── PROJECT_LOG.md
└── README.md
```

Raw datasets and secrets are intentionally excluded from version control.

## Interpretation note

FAERS/openFDA data are spontaneous adverse-event reports. Report counts do not establish incidence, comparative risk, or causation. Analyses in this repository will distinguish descriptive reporting patterns from causal or clinical conclusions.
