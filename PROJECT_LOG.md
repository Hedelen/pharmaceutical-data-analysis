# Project Log

## 2026-09-16 — Project setup

### Direction
Pivoted from the AACT clinical-trials project to a broader pharmaceutical data-analysis project focused on drug safety and pharmacology.

### Planned data sources
- openFDA Drug Adverse Event API
- ChEMBL

### Initial analysis areas
- Compare adverse-event profiles across drugs and drug classes.
- Explore serious outcomes, tolerability, and reported therapeutic failure.
- Build pharmacologic profiles using targets, mechanisms, and bioactivity from ChEMBL.
- Investigate whether mechanistic similarity is associated with similarity in reported adverse-event profiles.
- Use antidepressants as a major analysis area; GLP-1-based drugs are currently being used for API-learning exercises.

### Current progress
- Learned the basic openFDA query structure: endpoint + query parameters.
- Successfully queried individual drugs and counted reported reactions.
- Began translating browser API calls into Python using the `requests` library.

### Next steps
- Connect the local project folder to this GitHub repository.
- Keep API keys out of source control using environment variables.
- Build a reusable Python workflow for querying multiple drugs.
- Save raw API responses locally and design a clean processed dataset.
- Add ChEMBL once the openFDA pipeline is understood.
