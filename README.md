# Playwright BDD Project

## Project Structure

- `features/` — Gherkin feature files
- `tests/features/steps/` — Step definitions for BDD
- `tests/pages/` — Page Object Model classes
- `tests/` — Test runner scripts (e.g., `test_e2e.py`)
- `.env` — Environment variables (at project root)
- `reports/` — Test and HTML reports (gitignored)
- `test-results/`, `evidence/` — Playwright artifacts (gitignored)

## Setup

1. Install dependencies:
   ```sh
   pip install -r tests/requirements.txt
   ```
2. Set up your `.env` file at the project root (see example in repo).

## Running Tests

- Run all BDD tests and generate reports:
  ```sh
  pytest tests/test_e2e.py --cucumberjson=reports/cucumber.json --html=reports/report.html --disable-warnings -v
  ```
- To run in headed mode and take screenshots:
  ```sh
  pytest tests/test_e2e.py --headed --screenshot=on --disable-warnings -v
  ```

## Best Practices
- Keep step definitions and page objects modular and reusable.
- Use environment variables for sensitive data and URLs.
- Keep test artifacts and environment files out of version control.

---

For more details, see the code comments and structure above.
