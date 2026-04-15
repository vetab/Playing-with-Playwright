# Playwright BDD Test Automation Framework

A modern, scalable test automation framework for end-to-end testing using **Playwright**, **pytest-bdd**, and the **Behavior-Driven Development (BDD)** approach. This framework tests the SauceDemo e-commerce application with comprehensive coverage of user authentication, inventory management, cart operations, and checkout flows.

## 🎯 Framework Overview

### Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Browser Automation** | Playwright | 1.43.0 | Cross-browser automated testing |
| **Test Framework** | pytest | 7.1.3 | Test execution and reporting |
| **BDD Framework** | pytest-bdd | 8.1.0 | Gherkin feature file support |
| **Playwright Integration** | pytest-playwright | 0.4.4 | Pytest plugin for Playwright |
| **Test Reporting** | pytest-html | 4.2.0 | HTML report generation |
| **Configuration** | python-dotenv | 0.21.0 | Environment variable management |
| **Parallel Execution** | pytest-xdist | 3.5.0 | Distributed test execution |

### Design Patterns

- **Behavior-Driven Development (BDD)**: Tests are written in Gherkin language, making them readable for both technical and non-technical stakeholders
- **Page Object Model (POM)**: Each page is encapsulated in a class with methods for interactions, reducing test maintenance
- **Scenario-based Testing**: Feature files group related test scenarios following Cucumber best practices

## 📁 Project Structure

```
tests/
├── features/
│   ├── login.feature              # User authentication scenarios
│   ├── inventory.feature          # Product browsing and cart management
│   └── checkout.feature           # Cart operations and order processing
├── pages/
│   ├── login.py                   # LoginPage object with selectors and actions
│   ├── inventory.py               # InventoryPage object for product interactions
│   ├── cart.py                    # CartPage object for cart management
│   └── payment.py                 # PaymentPage object for checkout flows
├── steps/
│   ├── login_steps.py             # Step definitions for login feature
│   ├── inventory_steps.py         # Step definitions for inventory feature
│   ├── cart_steps.py              # Step definitions for cart operations
│   ├── payment_steps.py           # Step definitions for checkout and payment
│   └── conftest.py                # pytest fixtures and configuration
├── test_e2e.py                    # Main test runner (pytest-bdd entry point)
├── conftest.py                    # Global pytest configuration
├── requirements.txt               # Python dependencies
└── __init__.py                    # Package initialization
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- macOS, Linux, or Windows

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vetab/SauceDemo-E2E-Test-Automation.git
   cd SauceDemo-E2E-Test-Automation
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r tests/requirements.txt
   ```

4. **Install Playwright browsers:**
   ```sh
   playwright install
   ```

5. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   BASE_URL=https://www.saucedemo.com
   HEADLESS=True
   ```

## ✅ Running Tests

### Run All Tests with Reports
```sh
pytest tests/test_e2e.py \
  --cucumberjson=reports/cucumber.json \
  --html=reports/report.html \
  --disable-warnings -v
```

### Run Tests in Headed Mode (View Browser)
```sh
pytest tests/test_e2e.py --headed --screenshot=on --disable-warnings -v
```

### Run Specific Feature File
```sh
pytest tests/test_e2e.py -k "login" -v
```

### Run Tests in Parallel (4 workers)
```sh
pytest tests/test_e2e.py -n 4 --html=reports/report.html
```

### Generate Cucumber JSON Report Only
```sh
pytest tests/test_e2e.py --cucumberjson=reports/cucumber.json
```

## 📊 Test Coverage

The framework currently covers:

| Feature | Scenarios | Status |
|---------|-----------|--------|
| **Login** | 5 scenarios (empty fields, invalid credentials, locked user, success) | ✅ Passing |
| **Inventory** | 3 scenarios (browse products, add/remove items) | ✅ Passing |
| **Checkout** | 9 scenarios (cart management, billing, order summary) | ✅ Passing |
| **Total** | **17 test scenarios** | **100% Passing** |

## 🏗️ Architecture & Best Practices

### BDD Approach
- **Feature Files**: Written in Gherkin syntax for clarity and non-technical readability
- **Step Definitions**: Implement Given-When-Then steps with clean, reusable logic
- **Single Responsibility**: Each scenario tests one specific user behavior
- **Background**: Common setup steps (e.g., login) defined once and reused

### Page Object Model
- Encapsulates page selectors and interactions
- Reduces maintenance when UI changes
- Promotes reusability across step definitions
- Example:
  ```python
  class LoginPage:
      def __init__(self, page):
          self.page = page
          self.username_field = page.locator("#user-name")
      
      def login(self, username, password):
          self.username_field.fill(username)
          # ...
  ```

### Code Organization
- **Separation of Concerns**: UI interactions in pages, business logic in steps
- **DRY Principle**: Shared fixtures and utilities prevent code duplication
- **Environment Configuration**: Uses `.env` for sensitive data and environment-specific settings

## 📝 Example Feature File

```gherkin
Feature: SauceDemo User Authentication
  As a user
  I want to log in to the SauceDemo application
  So that I can access my account and view products

  Scenario: Login with valid credentials
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page
```

## 🔧 Configuration

### pytest.ini & conftest.py
- Browser type (chromium, firefox, webkit)
- Headless/headed mode
- Screenshot and video capture settings
- Report generation options

### .env File
```
BASE_URL=https://www.saucedemo.com
HEADLESS=True
SLOW_MO=100  # Slow down actions by 100ms
```

## 📈 Test Reports

- **HTML Report**: `reports/report.html` - Detailed test results with screenshots
- **Cucumber JSON**: `reports/cucumber.json` - Machine-readable format for CI/CD integration

## 🤝 Contributing

### Adding a New Test Scenario
1. Add a scenario to the appropriate `.feature` file
2. Implement corresponding step definitions in `steps/`
3. Create/update page objects in `pages/` if needed
4. Run tests locally to verify
5. Commit with descriptive message: `feat: add [scenario description]`

### Naming Conventions
- Feature files: `snake_case.feature` (e.g., `checkout.feature`)
- Step definitions: `feature_steps.py` (e.g., `login_steps.py`)
- Page objects: `PascalCase.py` (e.g., `LoginPage.py`)

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)
- [Gherkin Syntax Guide](https://cucumber.io/docs/gherkin/)
- [Cucumber Best Practices](https://cucumber.io/docs/bdd/)

## 🐛 Troubleshooting

### Tests Fail with "Browser not found"
```sh
playwright install
```

### Tests Timeout
- Increase timeout in `conftest.py`: `page.set_default_timeout(30000)`
- Check if `BASE_URL` is accessible

### Environment Variables Not Loading
- Ensure `.env` file exists in project root
- Verify `python-dotenv` is installed

## 📄 License

See LICENSE file for details.

---

**Last Updated**: March 2026 | **Framework Version**: 1.0.0
