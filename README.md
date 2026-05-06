# CIS 3120 — Programming for Analytics

**Course repository, Spring 2026**
Baruch College, Zicklin School of Business
Instructor: Patrick Slattery, Baruch College, CUNY

---

## Purpose

This repository hosts the canonical course materials for CIS 3120 (Programming for Analytics) and serves as the submission target for mini-project pull requests. Students fork this repository, complete their assignments on team branches, and submit through pull requests to `main`.

---

## Repository Layout

| Path | Contents |
|:---|:---|
| `notebooks/` | Course notebooks: instructor canonical versions, student starters, and team submissions |
| `maps/` | Rendered folium maps from team submissions |
| `methodology/` | Methodology documents from team submissions |
| `reflections/` | Comparative reflections from team submissions |
| `mp03/` | Importable Python module containing seeded data for MP03 |
| `docs/` | Assignment specifications and reference documents |

---

## Active Mini-Project: MP03 — Press Release to Plot

The current mini-project is MP03, which extends the Module 15 walkthrough into a comparative analysis of Financial Services and Travel and Hospitality industries. See `docs/MP03_Assignment.docx` for the full specification.

### Required submission paths

Each team submits four artifacts at the following paths, where `<NN>` is the two-digit team number assigned in Brightspace:

- `notebooks/MP03_Notebook_team_<NN>.ipynb`
- `maps/mp03_map_team_<NN>.html`
- `methodology/mp03_methodology_team_<NN>.md`
- `reflections/mp03_reflection_team_<NN>.md`

### Starter materials

- `notebooks/MP03_Starter.ipynb` — scaffolded starter notebook to copy and rename. Contains the validated canonical pipeline (Module 15) and TODO scaffolding for the three required new functions.
- `mp03/seeds.py` — seeded ticker lists and search-phrase lists for both industries.
- `notebooks/Module15_InstructorNotebook.ipynb` — full instructor walkthrough with pedagogical annotations (added separately as part of the Module 15 production cycle).

---

## Git Workflow

### Branch naming

Team integrator branches must follow the convention:

```
mp/03-industry-comparison-team-<NN>
```

Pipeline-lead feature branches:

```
mp/03-financial-services-team-<NN>
mp/03-travel-hospitality-team-<NN>
```

### Commit message convention

All commits follow the format `feat(scope): description`. Scopes for MP03:

| Scope | Use for |
|:---|:---|
| `stage1`, `stage2`, `stage3`, `stage4`, `viz` | Modifications to the canonical pipeline stages |
| `tickers` | Changes to industry ticker lists |
| `phrases` | Changes to search-phrase extensions |
| `window` | Window-tuning experiment work |
| `methodology` | Methodology section content |
| `reflection` | Comparative reflection content |
| `integration` | Merges, conflict resolution, integrated test fixes |
| `docs` | README updates, file naming, anything in /reflections |

### Submission tag

After the upstream PR is merged, the integrator tags the submission:

```
git tag -a mp03-team-<NN> -m "MP03 submission for Team <NN>: <Member 1>, <Member 2>, <Member 3>"
git push origin mp03-team-<NN>
```

---

## Setup

### Required packages

See `requirements.txt`. The canonical pipeline depends on `anthropic`, `requests`, `beautifulsoup4`, `folium`, and `pandas`. In Google Colab, install with:

```python
!pip install anthropic folium --quiet
```

The other packages are pre-installed in the Colab base image.

### API key configuration

The Anthropic API key must be configured in Colab Secrets as `ANTHROPIC_API_KEY`. **API keys must never be committed to this repository.** The `.gitignore` excludes the standard environment files; verify that no key appears in any committed cell output before opening a pull request.

### User-Agent header

Both SEC EDGAR and OpenStreetMap Nominatim require a descriptive User-Agent header containing a real name and email. Replace the placeholder in the notebook setup cell with your Baruch email before running.

---

## License

See `LICENSE`.

---

## Contact

Questions on the project, the API, or the pipeline should be brought to office hours or directed to Patrick Slattery, Baruch College, CUNY. 
