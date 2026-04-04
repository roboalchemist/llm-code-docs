# Testsprite Documentation

Source: https://docs.testsprite.com/llms-full.txt

---

# FAQ
Source: https://docs.testsprite.com/learn/faq



<AccordionGroup>
  <Accordion title="Who is TestSprite designed for?">
    TestSprite is ideal for individual developers looking for self-serve testing and small development teams without dedicated QA resources. Whether you're a freelancer, startup, or growing company, TestSprite adapts to your workflow and helps streamline testing with minimal effort.
  </Accordion>

  <Accordion title="Which approach should I choose: Web Portal or MCP Server?">
    * **Web Portal**: Choose if you prefer a visual interface, need team collaboration features, or want centralized test management
    * **MCP Server**: Choose if you're a developer who wants testing integrated directly into your coding workflow with IDE integration
  </Accordion>

  <Accordion title="How quickly can I get started?">
    * **Web Portal**: 2-3 minutes to create your first test
    * **MCP Server**: 1-2 minutes for installation and configuration
    * **First Results**: Most tests complete within 10-20 minutes
  </Accordion>

  <Accordion title="How does TestSprite handle my code and data?">
    TestSprite prioritizes security and privacy:

    * **No Code Storage**: Your source code is never stored on our servers
    * **Secure Transmission**: All data is encrypted in transit
    * **Isolated Execution**: Tests run in secure cloud sandboxes
    * **Local Analysis**: Code analysis happens locally (MCP Server)
    * **SOC 2 Compliance**: Enterprise-grade security standards
  </Accordion>

  <Accordion title="Can I customize test scenarios?">
    Yes! TestSprite offers multiple customization options:

    * **Natural Language**: Describe test scenarios in plain English
    * **Custom Test Plans**: Modify AI-generated test plans
    * **Specific Workflows**: Focus on particular user journeys
    * **Advanced Configuration**: Fine-tune test parameters and conditions
  </Accordion>

  <Accordion title="How many projects can I test with TestSprite?">
    TestSprite's licensing allows you to test multiple projects:

    * **Individual Plans**: Multiple projects with usage limits
    * **Team Plans**: Shared projects with collaboration features
    * **Custom Solutions**: Contact us for specific requirements
  </Accordion>

  <Accordion title="What support is available?">
    We provide comprehensive support:

    * **Documentation**: Extensive guides and tutorials
    * **Live Chat**: Available in the dashboard
    * **Email Support**: Technical assistance and troubleshooting
    * **Community Forum**: Best practices and peer support
    * **Video Tutorials**: Step-by-step walkthroughs
    * **Onboarding**: Dedicated assistance for enterprise customers
  </Accordion>

  <Accordion title="What happens if my tests fail?">
    TestSprite provides comprehensive failure analysis:

    * **Detailed Reports**: Clear descriptions of what went wrong
    * **Root Cause Analysis**: AI-powered insights into failure reasons
    * **Fix Suggestions**: Actionable recommendations for resolution
    * **Auto-Fixing**: Automatic code fixes (MCP Server)
    * **Re-testing**: Easy re-execution after fixes
  </Accordion>

  <Accordion title="Can I trust TestSprite with my applications?">
    TestSprite has earned trust through:

    * **5000+ Enterprise Customers**: Proven track record
    * **90% Reduction** in manual testing time
    * **SOC 2 Certification**: Enterprise security compliance
    * **Regular Audits**: Continuous security assessments
    * **Transparent Practices**: Clear privacy and security policies
  </Accordion>

  <Accordion title="How accurate are TestSprite's test results?">
    TestSprite maintains high accuracy through:

    * **AI-Powered Analysis**: Advanced machine learning models
    * **Comprehensive Coverage**: Multiple test categories and scenarios
    * **Continuous Learning**: AI improves with each test execution
    * **Human Review**: Option for manual test plan review
    * **Feedback Loops**: Results improve based on user input
  </Accordion>

  <Accordion title="How do I report bugs or request features?">
    We welcome your feedback:

    * **Bug Reports**: Use the dashboard feedback system
    * **Feature Requests**: Submit through the product portal
    * **GitHub Issues**: For open-source components
    * **Community Forum**: Discuss with other users
    * **Direct Contact**: Reach out to our support team
  </Accordion>
</AccordionGroup>

Still have questions? [Contact our support team <Icon icon="arrow-up-right-from-square" />](https://calendly.com/contact-hmul/schedule) or check out our [comprehensive documentation](../../mcp/getting-started/introduction).


# MCP Demo & Examples
Source: https://docs.testsprite.com/learn/mcp-demo

Real-world TestSprite MCP Server output from an actual e-commerce project test run.

## 10-Minute Demo Video

Watch TestSprite MCP Server in action with this complete workflow demonstration:

<Frame>
  <iframe />
</Frame>

**What you'll see in the demo:**

* Set up TestSprite MCP Server **directly inside Cursor**.
* See **end-to-end** testing workflow from start to finish
* Missing product requirements? MCP automatically **generates** them for you
* Full **test plans** and **test cases** created automatically
* Bugs **detected**, **reported**, and **resolved** with no human intervention in one loop
* Achieve **90%+** code accuracy with zero manual prompting

## E-commerce Frontend (React + TypeScript + Vite)

### Project Overview

Simple locally hosted e-commerce web application with product browsing, user authentication, and admin functionality.

**Tech Stack**

<Tabs>
  <Tab title="Frontend" icon="window-maximize">
    <Columns>
      <Card title="React 18">
        <div>
          <img alt="React" />
        </div>
      </Card>

      <Card title="TypeScript">
        <div>
          <img alt="typescript" />
        </div>
      </Card>

      <Card title="Vite">
        <div>
          <img alt="Vite" />
        </div>
      </Card>

      <Card title="Material UI">
        <div>
          <img alt="mui" />
        </div>
      </Card>
    </Columns>
  </Tab>

  <Tab title="Backend" icon="server">
    <Columns>
      <Card title="Node.js (local development)">
        <div>
          <img alt="Node.js" />
        </div>
      </Card>
    </Columns>
  </Tab>

  <Tab title="Testing" icon="gear">
    <Columns>
      <Card title="Playwright (Python)">
        <div>
          <img alt="playwright" />
        </div>
      </Card>
    </Columns>
  </Tab>
</Tabs>

### Command Used

```text icon="file-lines" theme={null}
Can you test this e-commerce project with TestSprite?
```

### Generated Normalized PRD Example

```json Expandable Sample Normalized PRD theme={null}
{
  "meta": {
    "project": "Simple E-commerce Web Application",
    "version": "1.0.0",
    "date": "2025-07-01",
    "prepared_by": "Generated by TestSprite"
  },
  "product_overview": "A simple locally hosted e-commerce web application allowing users to browse products, purchase using a hardcoded test account, and manage orders with admin functionality for product management.",
  "core_goals": [
    "Enable users to browse a product catalog with detailed product views.",
    "Provide authentication with a hardcoded test user for purchasing and order tracking.",
    "Allow users to simulate purchases and view their order history.",
    "Support admin users to manage product listings via a CRUD interface.",
    "Run fully locally without reliance on external services or databases."
  ],
  "key_features": [
    "User login/logout with React Context API and route protection.",
    "Product catalog displaying products fetched from backend with images and details.",
    "Individual product detail pages with purchase functionality.",
    "Order history page showing user's past purchases.",
    "Admin dashboard for adding, editing, and deleting products.",
    "Simulated checkout process without real payment integration.",
    "... more 4 features"
  ],
  "user_flow_summary": [
    "Visitor accesses product catalog and browses available products.",
    "Visitor logs in using the test account credentials.",
    "Logged in user selects a product and clicks buy to simulate purchase.",
    "System adds the purchase to the user's order history.",
    "... more 3 user flows"
  ],
  "validation_criteria": [
    "Users can only log in successfully with the hardcoded test credentials.",
    "Unauthenticated users are redirected to login when accessing protected routes.",
    "Product catalog displays correct and complete product data fetched from backend.",
    "Purchasing updates order history and returns appropriate success or error feedback.",
    "... more 6 validation criteria"
  ],
  "code_summary": {
    "tech_stack": [
      "TypeScript",
      "React", 
      "Vite",
      "Material-UI",
      "React Router DOM",
      "CSS"
    ],
    "features": [
      {
        "name": "Authentication System",
        "description": "User login/logout functionality with React Context API for state management, includes test credentials and protected route handling",
        "files": ["src/App.tsx", "src/pages/Login.tsx"]
      },
      {
        "name": "Product Catalog",
        "description": "Display grid of products fetched from API with product cards showing images, names, categories, prices, and buy/view details buttons",
        "files": ["src/pages/ProductCatalog.tsx"]
      },
      "... more 10 features"
    ]
  }
}
```

### Generated Test Plan Example

```json Expandable Sample Test Cases theme={null}
[
  {
    "id": "TC001",
    "title": "Login success with valid test credentials",
    "description": "Verify that users can log in successfully using the hardcoded test credentials",
    "category": "functional",
    "priority": "High",
    "steps": [
      {
        "type": "action",
        "description": "Navigate to the login page"
      },
      {
        "type": "action", 
        "description": "Input valid hardcoded username"
      },
      {
        "type": "assertion",
        "description": "Verify the user is redirected to the product catalog page"
      },
      "... more 3 steps"
    ]
  },
  {
    "id": "TC002",
    "title": "Login failure with invalid credentials",
    "description": "Verify that login is unsuccessful with invalid username or password",
    "category": "error handling",
    "priority": "High",
    "steps": ["... 6 action/assertion steps"]
  },
  {
    "id": "TC003",
    "title": "Redirect unauthenticated user from protected routes",
    "description": "Verify that unauthenticated users are redirected to login when trying to access protected routes",
    "category": "security", 
    "priority": "High",
    "steps": ["... 4 action/assertion steps"]
  },
  "... more 13 test cases"
]
```

**Categories Generated:**

<Columns>
  <Card title="Functional (8 tests)">
    Core business logic and user workflows
  </Card>

  <Card title="Error Handling (3 tests)">
    Exception handling and error recovery
  </Card>

  <Card title="Security (3 tests)">
    Authentication, authorization, access control
  </Card>

  <Card title="UI (2 tests)">
    User interface interactions and responsive design
  </Card>
</Columns>

### Generated Test Code Example

```python Expandable Sample Test Code theme={null}
# TC001_Login_success_with_valid_test_credentials.py
import asyncio
from playwright import async_api

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage", 
                "--ipc=host",
                "--single-process"
            ],
        )
        
        # Create a new browser context
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL
        await page.goto("http://localhost:5174", wait_until="commit", timeout=10000)
        
        # Navigate to the login page by clicking the login link
        frame = context.pages[-1]
        elem = frame.locator('xpath=html/body/div/header/div/a[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        
        # Input valid hardcoded username and password
        elem = frame.locator('xpath=html/body/div/div/div/div/div/div/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('example@gmail.com')
        
        # ... more test steps
        
        # Assertions: Verify login success and redirect
        assert await frame.title() == 'Product Catalog'
        nav_items = await frame.locator('xpath=//header//a').all_text_contents()
        assert any('Logout' in item for item in nav_items)
        
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
```

### Test Results

**Overall Results:**

* **Project:** frontend
* **Total Tests:** 16
* **Passed:** 10 (62.5%)
* **Failed:** 6 (37.5%)

```text Expandable Same Results theme={null}
✅ TC001: Login success with valid test credentials
   Severity: Low | Error: N/A
   Analysis: Login functionality correctly authenticates users with valid hardcoded credentials

❌ TC002: Login failure with invalid credentials  
   Severity: High | Error: System redirects to Product Catalog instead of showing error message
   Fix: Implement proper error message display on login failure

✅ TC003: Redirect unauthenticated user from protected routes
   Severity: Low | Error: N/A
   Analysis: Route protection working correctly

❌ TC009: Admin can add a new product
   Severity: High | Error: Admin dashboard page became empty after form submission
   Fix: Add error boundaries and validate backend response handling

... more 12 test results
```

### Test Report Example

TestSprite automatically generates a comprehensive test report that provides detailed insights about performance and quality.

<Frame>
  <img alt="Report" />
</Frame>

<br />

<Accordion title="View Full Sample Test Report ">
  > #### TestSprite AI Project Test Report
  >
  > ***
  >
  > ##### Document Metadata
  >
  > * **Project Name:** frontend
  > * **Version:** 0.0.0
  > * **Date:** 2025-01-09
  > * **Prepared by:** TestSprite AI Team
  >
  > ***
  >
  > ##### Requirement Validation Summary
  >
  > ###### Requirement: User Authentication
  >
  > * **Description:** User login functionality with credentials validation and authentication state management.
  >
  > ###### Test 1
  >
  > * **Test ID:** TC001
  > * **Test Name:** Login success with valid test credentials
  > * **Test Code:** TC001\_Login\_success\_with\_valid\_test\_credentials.py
  > * **Test Error:** N/A
  > * **Test Visualization and Result:** View Results (dashboard link)
  > * **Status:** ✅ Passed
  > * **Severity:** Low
  > * **Analysis / Findings:** Login functionality correctly authenticates users with valid hardcoded credentials and grants access. Functionality is correct as per requirements. Consider adding tests for edge cases and security enhancements like rate limiting.
  >
  > ***
  >
  > ###### Test 2
  >
  > * **Test ID:** TC002
  > * **Test Name:** Login failure with invalid credentials
  > * **Test Code:** TC002\_Login\_failure\_with\_invalid\_credentials.py
  > * **Test Error:** Login with invalid credentials is unsuccessful to verify because the system redirects to the Product Catalog page instead of showing an error message or staying on the login page.
  > * **Test Visualization and Result:** View Results (dashboard link)
  > * **Status:** ❌ Failed
  > * **Severity:** High
  > * **Analysis / Findings:** The system incorrectly redirects users to the Product Catalog page upon failed login attempts instead of displaying an error message or staying on the Login page. Fix the login error handling logic to display proper error messages on invalid credentials and prevent unwanted redirects.
  >
  > ***
  >
  > ###### Requirement: Route Protection & Access Control
  >
  > * **Description:** Ensures authenticated access to protected routes and proper redirects for unauthorized users.
  >
  > ###### Test 1
  >
  > * **Test ID:** TC003
  > * **Test Name:** Redirect unauthenticated user from protected routes
  > * **Test Code:** TC003\_Redirect\_unauthenticated\_user\_from\_protected\_routes.py
  > * **Test Error:** N/A
  > * **Test Visualization and Result:** View Results (dashboard link)
  > * **Status:** ✅ Passed
  > * **Severity:** Low
  > * **Analysis / Findings:** Unauthenticated users are properly redirected to the login page when attempting to access protected routes, ensuring access control is enforced. The functionality is working correctly.
  >
  > ***
  >
  > ... more test results for 13 additional requirements
  >
  > ***
  >
  > ##### Coverage & Matching Metrics
  >
  > * **73% of product requirements tested**
  >
  > * **56% of tests passed**
  >
  > * **Key gaps / risks:**
  >
  > > 73% of product requirements had at least one test generated.\
  > > 56% of tests passed fully.\
  > > Risks: Critical admin functionality failures; login error handling issues; incomplete responsive design testing; API error handling gaps.
  >
  > | Requirement                       | Total Tests | ✅ Passed | ⚠️ Partial | ❌ Failed |
  > | --------------------------------- | ----------- | -------- | ---------- | -------- |
  > | User Authentication               | 2           | 1        | 0          | 1        |
  > | Route Protection & Access Control | 2           | 2        | 0          | 0        |
  > | Product Catalog & Display         | 2           | 2        | 0          | 0        |
  > | Purchase & Checkout System        | 3           | 3        | 0          | 0        |
  > | Order History Management          | 1           | 1        | 0          | 0        |
  > | Admin Product Management          | 3           | 0        | 0          | 3        |
  > | Responsive Design & UI            | 1           | 0        | 0          | 1        |
  > | Error Handling & API Integration  | 1           | 0        | 0          | 1        |
  > | Data Persistence                  | 1           | 0        | 0          | 1        |
</Accordion>

### File Structure Generated

```text Expandable Sample File Structure theme={null}
testsprite_tests/
├── tmp/
│   ├── config.json               # Test configuration
│   ├── code_summary.json         # Project analysis
│   ├── report_prompt.json        # AI analysis data
│   └── test_results.json         # Detailed results
├── standard_prd.json             # Normalized PRD
├── testsprite_frontend_test_plan.json  # Complete test plan
├── TestSprite_MCP_Test_Report.md # Human-readable report
├── TestSprite_MCP_Test_Report.html # HTML report
├── TestSprite_MCP_Test_Report.pdf  # PDF report
├── TC001_Login_success_with_valid_test_credentials.py
├── TC002_Login_failure_with_invalid_credentials.py
├── TC003_Redirect_unauthenticated_user_from_protected_routes.py
├── TC004_Display_full_product_catalog_with_correct_data.py
├── TC005_View_individual_product_details.py
├── TC006_Simulate_product_purchase_successfully.py
├── TC007_Handle_purchase_failure_gracefully.py
├── TC008_View_order_history_with_correct_purchase_list.py
├── TC009_Admin_can_add_a_new_product.py
├── TC010_Admin_can_edit_an_existing_product.py
├── TC011_Admin_can_delete_a_product.py
├── TC012_Protected_route___order_history_only_accessible_to_authenticated_users.py
├── TC013_Responsive_UI_renders_correctly_on_multiple_screen_sizes.py
├── TC014_Backend_API_handles_invalid_product_ID_gracefully.py
├── TC015_Simulate_checkout_without_real_payment_integration.py
└── TC016_Local_backend_persistence_with_in_memory_or_JSON_storage.py
```


# Healing & Observability
Source: https://docs.testsprite.com/mcp/concepts/healing-observability

How TestSprite detects, explains, and repairs failures with strong signals and auto-healing.

## Why Healing & Observability

Stable tests need two things:

* **Strong observability** to tell you what failed and why
* **Safe, automated healing** to fix brittle tests and non-functional drift without busywork

<Tip>TestSprite pairs both, so your suites stay reliable as the app evolves.</Tip>

## Observability Signals Collected

During planning, generation, and execution, TestSprite captures rich artifacts to explain outcomes and accelerate fixes.

<Tabs>
  <Tab title="Execution Artifacts">
    <Frame>
      <img alt="artifacts" />
    </Frame>

    TestSprite captures detailed execution artifacts:

    * Screenshots and videos (for UI paths)
    * Console logs and network traces
    * HTTP requests/responses with headers and payloads
  </Tab>

  <Tab title="Structured Results">
    <Frame>
      <img alt="results" />
    </Frame>

    Test results are organized with structured data:

    * Per-test status with timestamps and duration
    * Assertions and failure locations
    * Categorization: functional, error handling, auth, boundary, edge, concurrency, UI/UX
  </Tab>

  <Tab title="Context Files">
    <Frame>
      <img alt="context" />
    </Frame>

    Context information helps understand test execution:

    * Code summary, normalized PRD, and test plans used
    * Environment details (frameworks, ports, config)
  </Tab>
</Tabs>

<Info>All artifacts are summarized into human-readable reports and machine-readable JSON under `testsprite_tests/`.</Info>

## Failure Classification

When a test fails, TestSprite classifies the root cause to determine the right remediation path:

* **Product Bug:** behavior contradicts PRD/plan expectations
* **Test Fragility:** locator drift, timing mismatch, transient UI state
* **Environment Issue:** service not running, port mismatch, credentials missing
* **Contract Violation:** response schema/shape breaks API guarantees

<Info>Classification drives both the report and any automated healing actions.</Info>

## Flakiness Detection

Intermittent failures are detected by patterns in timing, retries, and run-to-run variance:

* **Identical steps** failing at different points in time
* Pass/fail **toggling** without code changes
* **High sensitivity** to network latency, animations, or loading spinners

<Info>For flaky cases, TestSprite proposes stable waits, resilient selectors, and idempotent flows.</Info>

## Auto-Healing Strategies

Healing focuses on making tests robust without masking real bugs.

<Tabs>
  <Tab title="UI Selectors & Timing">
    Healing strategies for UI test stability:

    * Prefer **role/label/text-first selectors** over brittle CSS/XPath
    * Add **deterministic waits** (network idle, specific element visible)
    * Defer actions until the page reaches a **known ready state**
  </Tab>

  <Tab title="Test Data & State">
    Healing strategies for test data and state management:

    * Generate **deterministic test data** and fixtures
    * **Reset state between tests**; clean up leaked sessions
  </Tab>

  <Tab title="Env & Config">
    Healing strategies for environment and configuration issues:

    * Correct known port/app start issues with **targeted guidance**
    * Suggest **missing credentials/env vars** in the portal
  </Tab>

  <Tab title="API Contracts">
    Healing strategies for API contract validation:

    * Tighten schema assertions to **actual contract**
    * Add nullability and pagination **boundary cases** where appropriate
  </Tab>
</Tabs>

<Info>Healing is applied automatically when safe; otherwise, it’s proposed for review in your IDE.</Info>

## End-to-End Repair Flow

<Card>
  ```mermaid theme={null}
  flowchart LR
      A[Execute and Collect] --> B[Analyze and Classify]
      B --> C[Decide Healing Path]
      C --> D[Verify]
      D --> E[Report]
  ```
</Card>

* **Execute and Collect**: Run tests, record artifacts, produce structured results
* **Analyze and Classify**: Determine bug vs. fragility vs. environment vs. contract issue
* **Decide Healing Path**: Apply safe auto-fixes (selectors, waits, fixtures). Propose code edits when human approval is prudent
* **Verify**: Re-run impacted tests to confirm stability and correctness
* **Report**: Update reports, annotate what was auto-healed vs. manually approved

## How This Connects to the Lifecycle

Healing and observability are embedded across the lifecycle:

* **Discover & Plan**: baseline PRD/plan informs assertions and oracles
* **Generate**: tests are authored with resilient defaults
* **Execute**: artifacts captured for every run
* **Analyze**: failures classified with actionable next steps
* **Heal & Maintain**: automated and proposed fixes applied
* **Report & Integrate**: signals flow to CI/CD quality gates

<Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle" icon="arrows-spin">
  Learn more about test types and lifecycle stages
</Card>

## Using Healing with the MCP Tools

<Frame>
  <img alt="tool" />
</Frame>

* The execution tool **generates artifacts** and **classifies failures**.
* The rerun tool **validates fixes** and **stabilizes previously failing flows**.

<Columns>
  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Explore TestSprite MCP tools and commands
  </Card>

  <Card title="Testing Workflow" href="/mcp/concepts/workflow">
    Understand the complete testing workflow
  </Card>

  <Card title="Key Terms" href="/mcp/concepts/key-terms">
    Learn essential TestSprite concepts
  </Card>
</Columns>

## Best Practices

<AccordionGroup>
  <Accordion title="Prefer semantic selectors">
    Use roles, labels, test-ids maintained by the app for more resilient tests.
  </Accordion>

  <Accordion title="Make state explicit">
    Use login helpers, seeded data, and cleanup hooks to ensure consistent test state.
  </Accordion>

  <Accordion title="Treat retries as diagnostics">
    Use retries to identify issues, not as permanent solutions to test problems.
  </Accordion>

  <Accordion title="Keep contracts explicit">
    Include schemas and acceptance criteria in PRD and plans for better test reliability.
  </Accordion>

  <Accordion title="Review proposed healing diffs">
    Review and approve proposed healing diffs before approving large behavior changes.
  </Accordion>
</AccordionGroup>

## What You’ll See in Reports

<Frame>
  <img alt="report" />
</Frame>

* Clear **pass/fail** per test with **category and priority**
* **Linked screenshots/videos** for failing UI steps
* **Request/response diffs** for API mismatches
* **Next actions**: re-run scope, suggested code edits, and configuration tips


# Key Terms
Source: https://docs.testsprite.com/mcp/concepts/key-terms

Essential TestSprite concepts explained simply.

## Generate & Regenerate

These actions control how TestSprite creates and updates your test suite. <kbd>Generate</kbd> creates new tests for the first time, while <kbd>Regenerate</kbd> recreates existing tests from scratch when your application or requirements change significantly.

### Generate

Create tests for the **first time** based on your PRD and project.

<Frame>
  <img alt="generate" />
</Frame>

<br />

<Tabs>
  <Tab title="Example prompt">
    Use this prompt to get started with testing your project:

    ```text theme={null}
    Help me test this project with TestSprite.
    ```
  </Tab>

  <Tab title="When to use">
    Use <kbd>Generate</kbd> when you need to create tests for the first time:

    * Starting with a new project
    * Adding tests to an existing project without tests
    * Creating initial test coverage
  </Tab>

  <Tab title="What happens">
    <kbd>Generate</kbd> follows this workflow:

    1. Analyzes your code
    2. Creates test plans
    3. Generates test files
    4. Executes the tests
  </Tab>
</Tabs>

### Regenerate

**Recreate tests** from scratch based on updated PRD and code.

<Frame>
  <img alt="regenerate" />
</Frame>

<br />

<Tabs>
  <Tab title="Example prompt">
    Use this prompt to regenerate tests after significant changes:

    ```text theme={null}
    Regenerate tests for the updated checkout flow.
    ```
  </Tab>

  <Tab title="When to use">
    Use <kbd>Regenerate</kbd> when you need to recreate tests from scratch:

    * Your app changed significantly (new features, refactored flows)
    * Test plans need updating to match new requirements
    * You want fresh test coverage reflecting current state
  </Tab>

  <Tab title="What happens">
    <kbd>Regenerate</kbd> follows this workflow:

    1. Re-analyzes your code
    2. Updates test plans
    3. Generates new test files
    4. Executes the new tests
  </Tab>
</Tabs>

<Card title="Regenerate Tests" href="/mcp/core/regenerate-tests" icon="repeat">
  Learn more about how to regenerate tests from scratch
</Card>

## Run & Rerun

These actions control how TestSprite executes your tests. <kbd>Run</kbd> executes newly generated tests for the first time, while <kbd>Rerun</kbd> executes previously generated tests again without regenerating them.

### Run

**Execute newly generated tests** for the first time.

<Frame>
  <img alt="run" />
</Frame>

<br />

<Tabs>
  <Tab title="When to use">
    Use <kbd>Run</kbd> when executing tests for the first time:

    * After generating tests
    * Initial validation of your application
    * First-time test execution
  </Tab>

  <Tab title="What happens">
    <kbd>Run</kbd> follows this workflow:

    1. Executes generated test files
    2. Collects results and artifacts
    3. Generates test reports
  </Tab>
</Tabs>

### Rerun

Execute **previously generated tests** again without changing them.

<Frame>
  <img alt="rerun" />
</Frame>

<br />

<Tabs>
  <Tab title="Example prompt">
    Use this prompt to rerun existing tests:

    ```text theme={null}
    Rerun the login and checkout tests with TestSprite.
    ```
  </Tab>

  <Tab title="When to use">
    Use <kbd>Rerun</kbd> when executing existing tests again:

    * Validating fixes you just applied
    * Confirming tests pass after app restart
    * Quick smoke check with existing tests
  </Tab>

  <Tab title="What happens">
    <kbd>Rerun</kbd> follows this workflow:

    1. Uses existing test files (no regeneration)
    2. Runs them against current app state
    3. Reports updated results
  </Tab>
</Tabs>

<Card title="Rerun Tests" href="/mcp/core/rerun-tests" icon="forward">
  Learn more about how to rerun existing tests
</Card>

## Healing

Automatic or semi-automatic **fixes to brittle tests that fail due to non-functional changes** (not real bugs), making tests robust without masking actual product issues.

<Card>
  ```mermaid theme={null}
  flowchart LR
      A[Detect] --> B[Classify]
      B --> C[Propose Fix]
      C --> D[Apply]
      D --> E[Verify]
  ```
</Card>

<Tabs>
  <Tab title="Common healing scenarios">
    <kbd>Healing</kbd> addresses these common test fragility issues:

    * **UI Selectors:** Updates when element IDs/classes change (e.g., `#login-btn` → `[data-testid="login"]`)
    * **Timing Issues:** Adjusts waits for slow-loading components or animations
    * **Test Data:** Updates fixtures when data schemas change
    * **Environment:** Corrects port mismatches, missing credentials, or configuration issues
    * **API Contracts:** Tightens schema assertions to match actual API responses
  </Tab>

  <Tab title="How it works">
    <kbd>Healing</kbd> follows this workflow:

    1. **Detect:** TestSprite identifies test fragility (not a product bug)
    2. **Classify:** Determines if it's a selector drift, timing mismatch, env issue, or contract violation
    3. **Propose Fix:** Generates a safe fix (e.g., new selector, longer wait, updated fixture)
    4. **Apply:** Automatically applies if low-risk, or asks for approval for larger changes
    5. **Verify:** Reruns tests to validate the fix worked
  </Tab>

  <Tab title="Example">
    Here's an example of how healing works:

    ```
    Test failed: Login button selector outdated
    Healing: Updated selector from #login-btn to [data-testid="login"]
    Status: Auto-applied, test now passing
    ```
  </Tab>
</Tabs>

### What Healing Is vs. What It's Not

Understanding the difference between healing and masking bugs is crucial. Healing only fixes test fragility caused by non-functional changes, never real product issues.

| What Healing is Not                                       | What Healing Is                                                             |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------- |
| <Icon icon="x" /> Masking real product bugs               | <Icon icon="check" /> Making tests resilient to non-functional code changes |
| <Icon icon="x" /> Making tests pass when they should fail | <Icon icon="check" /> Reducing test maintenance busywork                    |

## Test Scope

Defines **which parts of your codebase** TestSprite will analyze and test.

<Frame>
  <img alt="scope" />
</Frame>

TestSprite offers two scope options to balance between comprehensive coverage and speed. Choose based on your testing needs and development workflow.

| Features      | Codebase                                           | Code Diff                                                   |
| :------------ | :------------------------------------------------- | :---------------------------------------------------------- |
| What it tests | Tests the entire project                           | Tests only changed files/features (based on git diff)       |
| Use cases     | New projects, major releases, comprehensive audits | Feature branches, incremental development, quick validation |
| Speed         | Takes longer                                       | Fast feedback                                               |
| Coverage      | Full coverage                                      | Recent changes only                                         |

<Info>Set the scope in the bootstrapping page when you call the `testsprite_bootstrap_tests` tool. </Info>

<Card title="MCP Tools Reference" href="/mcp/core/tools" icon="wrench">
  Learn more about TestSprite MCP tools and commands
</Card>

## PRD & Normalized PRD

TestSprite uses Product Requirements Documents (PRD) to understand your project and generate appropriate tests. While you can provide PRDs in any format, TestSprite converts them into a standardized Normalized PRD format for consistent test generation.

### PRD (Product Requirements Document)

Your **original documentation** describing what your product should do.

<Frame>
  <img alt="prd" />
</Frame>

**Can be:**

* Informal notes or README
* Formal specification documents
* Jira tickets or user stories
* Design docs or wikis

### Normalized PRD

TestSprite's **standardized Product Requirements Document format** that ensures consistent and smooth test generation regardless of your original PRD style.

<Frame>
  <img alt="normalized" />
</Frame>

<Tabs>
  <Tab title="What's in it">
    The <kbd>Normalized PRD</kbd> contains structured information:

    * Product overview and goals
    * Core features with acceptance criteria
    * User flows and validation rules
    * Technical context from code analysis
  </Tab>

  <Tab title="Why it matters">
    Understanding why <kbd>Normalized PRD</kbd> exists:

    * Your PRD might be in any format
    * TestSprite converts it to a structured format
    * This normalized PRD drives test plan generation
  </Tab>
</Tabs>

<Tip>TestSprite **invented** this format to make test generation predictable across any project type.</Tip>

<Card title="Create Tests for New Projects" href="/mcp/core/create-tests-new-project" icon="bars-progress">
  Learn how to create tests using PRD and Normalized PRD
</Card>

## Test Plan

A **structured list** of test cases generated by TestSprite based on your normalized PRD and code analysis.

<Frame>
  <img alt="plan" />
</Frame>

<Tabs>
  <Tab title="Example">
    Here's an example of a test plan entry:

    ```json theme={null}
    {
      "id": "TC001",
      "title": "Login with valid credentials",
      "category": "functional",
      "priority": "High",
      "steps": [...]
    }
    ```
  </Tab>

  <Tab title="Contains">
    A <kbd>Test Plan</kbd> typically includes:

    * Test case IDs (TC001, TC002, etc.)
    * Descriptions and steps
    * Categories (functional, security, UI, etc.)
    * Priorities (High, Medium, Low)
    * Expected outcomes
  </Tab>
</Tabs>

<Info>Plans are saved as `frontend_test_plan.json` or `backend_test_plan.json`.</Info>

## Where to Learn More

<Columns>
  <Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle">
    Understand what we test and when
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Deep dive into auto-healing
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Technical tool parameters
  </Card>

  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature">
    Practical diff-scope usage
  </Card>
</Columns>


# Test Types & Lifecycle
Source: https://docs.testsprite.com/mcp/concepts/test-type-lifecycle

What we test (frontend UI flows and backend APIs) and how tests live through their lifecycle.

## Supported Test Types

TestSprite focuses on end-to-end value delivery, covering both frontend user journeys and backend service behaviors. The following categories map to what you saw in [Overview](/mcp/getting-started/overview) and are generated automatically by the MCP server.

<Frame>
  <img alt="test type" />
</Frame>

<br />

<Tabs>
  <Tab title="Frontend (UI & Business-Flow Integration)">
    * **User Journey Navigation**: Multi-step workflows, page transitions, deep linking, browser history, and route guards
    * **Form Flows & Validation**: Input validation, error messages, field dependencies, submission handling, and data persistence
    * **Visual States & Layouts**: Component rendering, responsive design, loading states, empty states, and accessibility compliance
    * **Interactive Components & Stateful UI**: Dropdowns, modals, tabs, accordions, drag-and-drop, state persistence, and real-time updates
    * **Authorization & Auth Flows**: Login/logout, protected routes, role-based UI visibility, session management, and token refresh
    * **Error Handling (UI)**: Toast notifications, modal dialogs, inline errors, validation feedback, and graceful degradation
  </Tab>

  <Tab title="Backend (API & Integration)">
    * **Functional API Workflows**: Endpoint behavior, multi-step workflows, service orchestration, and cross-service integration patterns
    * **Contract & Schema Validation**: Request/response schemas, data types, required fields, serialization formats, and API versioning
    * **Error Handling & Resilience**: Status codes, error response bodies, retry logic, backoff strategies, timeout handling, and graceful degradation
    * **Authorization & Authentication**: Token validation, role-based access control, permission scopes, session management, and credential handling
    * **Boundary & Edge Cases**: Payload size limits, pagination behavior, null/empty values, malformed inputs, and constraint validation
    * **Data Integrity & Persistence**: Data consistency, transaction handling, idempotency, state management, and database constraints
    * **Security Testing**: Common vulnerabilities (injection, XSS, CSRF), authentication bypass, authorization flaws, data exposure, and security misconfigurations
  </Tab>
</Tabs>

<Tip>The agent chooses the right mix per project, auto-generates plans, then produces executable tests (e.g., Playwright/Cypress for UI; language-appropriate clients for APIs).</Tip>

## Test Lifecycle

TestSprite’s lifecycle is designed to be continuous and IDE-native.

<Steps>
  <Step title="Discover & Understand">
    Analyze codebase structure, dependencies, and routes/endpoints. Normalize requirements into a TestSprite PRD.
  </Step>

  <Step title="Plan">
    Generate test plans per feature, mapping to the test types above. Prioritize critical paths and regressions.
  </Step>

  <Step title="Generate">
    Create runnable test code and fixtures. Synthesize data and environment configuration as needed.
  </Step>

  <Step title="Execute">
    Run tests in isolated environments with reliable orchestration. Capture artifacts: logs, traces, screenshots, videos.
  </Step>

  <Step title="Analyze">
    Classify failures (product bug vs. test fragility vs. environment). Summarize impact and correlate to code changes.
  </Step>

  <Step title="Heal & Maintain">
    Auto-update brittle selectors, data, and flows when safe. Propose edits when human approval is prudent.
  </Step>

  <Step title="Report & Integrate">
    Publish readable reports in your IDE and portal. Output signals for CI/CD quality gates.
  </Step>
</Steps>

## How Frontend and Backend Tests Work Together

<Card>
  ```mermaid theme={null}
  flowchart LR
      A[Frontend Tests<br/>UI Flows] --> C[Shared Understanding<br/>Auth, Data Models, Error Semantics]
      B[Backend Tests<br/>API Contracts] --> C
      C --> D[Quick Root Cause<br/>Analysis]
  ```
</Card>

* UI flows validate end-to-end behavior as a user would experience it
* API tests validate service contracts directly for faster feedback
* The two layers share understanding of auth, data models, and error semantics to pinpoint root causes quickly

## Where to Go Next

<Columns>
  <Card title="Overview" href="/mcp/getting-started/overview">
    High-level capabilities and supported types
  </Card>

  <Card title="Create Tests for a New Project" href="/mcp/core/create-tests-new-project">
    First-time setup
  </Card>

  <Card title="Create Tests for a New Feature" href="/mcp/core/create-tests-new-feature">
    Expand coverage incrementally
  </Card>

  <Card title="Continuous Monitoring" href="/mcp/core/continuous-monitoring">
    Keep coverage healthy over time
  </Card>

  <Card title="Test Maintenance" href="/mcp/maintenance/test-maintenance">
    Strategies for stability and speed
  </Card>

  <Card title="Test Execution Issues" href="/mcp/troubleshooting/test-execution-issues">
    Diagnose and resolve failures
  </Card>
</Columns>


# Add Extra Tests
Source: https://docs.testsprite.com/mcp/core/add-extra-tests

Expand test coverage by adding additional tests to your existing project.

Manually add new test cases to your TestSprite test plan file. TestSprite will generate executable test code for these new cases.

<Tip>Useful for importing tests from other sources or creating custom scenarios.</Tip>

<Steps>
  <Step title="Open the TestSprite test plan file">
    Open the TestSprite test plan file (e.g.`testsprite_frontend_test_plan.json`).

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Add new test cases">
    Append new test cases at the end, following the **same format** as the existing ones. If you have test cases from **another tool or platform**, paste them in and make sure they follow **the same style**.
    <Note>You can also use AI IDEs like Cursor or Trae to help reformat them to match TestSprite's standard.</Note>

    ```json Expandable Test Case Example theme={null}
    ### New Test Case
    {
      "id": "TC013",
      "title": "Admin Dashboard User and Category Management",
      "description": "Verify that admin users can create, edit, and delete categories and manage user roles and content moderation from the admin dashboard with immediate effect.",
      "category": "functional",
      "priority": "High",
      "steps": [
        {
          "type": "action",
          "description": "Login as admin user"
        },
        {
          "type": "action",
          "description": "Navigate to the admin dashboard"
        },
        {
          "type": "action",
          "description": "Create a new forum category"
        },
        {
          "type": "assertion",
          "description": "New category appears in the category list"
        },
        {
          "type": "action",
          "description": "Edit an existing category's name or description"
        },
        {
          "type": "assertion",
          "description": "Edits are saved and reflected in the UI"
        },
        {
          "type": "action",
          "description": "Delete a category"
        },
        {
          "type": "assertion",
          "description": "Category is removed and related threads are handled appropriately"
        },
        {
          "type": "action",
          "description": "Change a user's role from user to moderator"
        },
        {
          "type": "assertion",
          "description": "Role changes take effect immediately and permissions update"
        }
      ]
    }
    ```
  </Step>

  <Step title="Prompt your IDE">
    Once added, prompt your IDE:

    ```text Example Prompt theme={null}
    Rerun the xth test for me using testsprite_generate_code_and_execute
    ```
  </Step>

  <Step title="TestSprite generates test code">
    TestSprite will run the `generate_code_execute` tool again, generate test code for your new cases, and add them to your project and your TestSprite account.
  </Step>
</Steps>


# Test Running & Monitoring
Source: https://docs.testsprite.com/mcp/core/continuous-monitoring

Set up continuous test execution and monitoring for your projects.

## Overview

Continuous monitoring enables you to automatically run your MCP tests against deployed environments on a regular schedule. This ensures your production applications remain stable and helps you catch issues before they impact users.

<Info>
  **Two-Step Process:** Setting up continuous monitoring involves first deploying your tests to production, then configuring automated schedules.
</Info>

## Prerequisites

Before setting up continuous monitoring, ensure you have:

* Successfully created and tested your MCP tests
* Access to your deployed application URL (staging, testing, or production)
* Appropriate permissions to the TestSprite web portal

## Step 1: Deploy Tests to Production

First, you need to deploy your locally created MCP tests to run against your deployed environment.

<Frame>
  <img alt="plan" />
</Frame>

<br />

<Card title="Deploy Your Tests" icon="paper-plane" href="/mcp/core/deploy-to-production">
  Follow the complete deployment workflow to push your local MCP tests to the web portal and configure them to run against your deployed application.
</Card>

## Step 2: Configure Continuous Monitoring

Once your tests are deployed and running successfully against your production environment, set up automated schedules to monitor your application continuously.

<Frame>
  <img alt="plan" />
</Frame>

<br />

<Card title="Set Up Monitoring & Scheduling" icon="chart-simple" href="/web-portal/maintenance/monitoring">
  Configure automated test execution schedules to enable 24/7 continuous monitoring of your deployed application.
</Card>

### Key Monitoring Features

Continuous monitoring provides automated test execution with comprehensive tracking and alerting capabilities. The following features help you maintain visibility into your application's health:

| Feature               | Description                                                                   |
| :-------------------- | :---------------------------------------------------------------------------- |
| `Automated Execution` | Schedule tests to run daily, weekly, or monthly without manual intervention.  |
| `Proactive Alerts`    | Receive immediate notifications when tests fail or performance degrades.      |
| `Historical Tracking` | Monitor trends and identify issues over time with detailed execution history. |
| `Flexible Scheduling` | Pause, modify, or delete schedules as your monitoring needs evolve.           |

## Best Practices

<AccordionGroup>
  <Accordion title="Start with Stable Tests">
    Ensure your tests run reliably before scheduling them. Flaky tests lead to alert fatigue and reduce confidence in your monitoring.
  </Accordion>

  <Accordion title="Choose Appropriate Frequency">
    Balance monitoring coverage with resource usage. Critical applications may need hourly checks, while others can be monitored daily or weekly.
  </Accordion>

  <Accordion title="Configure Smart Alerts">
    Set up notification channels that match your team's workflow. Consider using different channels for different severity levels.
  </Accordion>

  <Accordion title="Review Results Regularly">
    Even with automation, periodically review test results and execution trends to identify patterns and opportunities for improvement.
  </Accordion>

  <Accordion title="Keep Tests Updated">
    As your application evolves, update your test schedules accordingly. Remove obsolete tests and add new ones for new features.
  </Accordion>
</AccordionGroup>

<Warning>
  **Important:** Always test your monitoring setup on a non-production environment first to ensure tests run correctly and notifications work as expected.
</Warning>


# Create Tests for New Change
Source: https://docs.testsprite.com/mcp/core/create-tests-new-feature

Generate tests scoped to recent code changes using TestSprite MCP Server.

## When to Use This

Use this flow after making a change (feature, bugfix, refactor). It targets only impacted areas to keep feedback fast.

<Note>Shift Left: You can generate and run tests even before a feature is complete to surface gaps early. Use `testScope: "diff"` and run a small subset (`testIds`) frequently during development.</Note>

## Prerequisites

* TestSprite MCP [Installed and configured](/mcp/getting-started/installation) in your IDE
* Your application runs locally
* Git repo with recent commits for diff analysis

## Quick Start

```text theme={null}
Test my new changes related to the Stripe payment features.
```

## Diff-Scoped Testing Workflow

TestSprite's diff-scoped workflow is optimized for speed and precision, focusing only on code impacted by recent changes:

<Card>
  ```mermaid theme={null}
  flowchart LR
      A["Bootstrap (diff scope)<br/>Analyze recent changes"] --> B["Analyze Changed Code<br/>Understand impacted features"]
      B --> C["Update/Generate PRD<br/>Align with new requirements"]
      C --> D["Create Targeted Tests<br/>Focus on changed flows"]
      D --> E["Generate & Execute<br/>Quick feedback loop"]
      E --> F["Review Results<br/>Fix and iterate"]
  ```
</Card>

### Step 1: Bootstrap with Diff Scope

The AI calls `testsprite_bootstrap_tests` with `testScope: "diff"` to initialize testing for changed code only.

<Frame>
  <img alt="diff" />
</Frame>

<br />

<Tabs>
  <Tab title="Process">
    1. **Project Detection**: Reuses existing project type configuration (`frontend` or `backend`)
    2. **Port Discovery**: Finds running applications and their ports
    3. **Git Diff Analysis**: Identifies modified files and changed lines since last commit
    4. **Scope Definition**: Sets testing scope to `diff` (changed code only)
  </Tab>

  <Tab title="What Makes Diff Scope Different">
    * **Faster Setup**: Reuses existing project configuration from previous runs
    * **Git Integration**: Analyzes your recent commits to identify changes
    * **Smart Filtering**: Only considers files and features touched by your commits
    * **Quick Validation**: Perfect for iterative development and PR workflows
  </Tab>
</Tabs>

<CodeGroup>
  ```javascript Configuration theme={null}
  testsprite_bootstrap_tests({
    localPort: 5173, // or your port
    type: "frontend", // or "backend"
    projectPath: "/absolute/path/to/your/project",
    testScope: "diff" // analyze only recent changes
  })
  ```

  ```json Sample Configuration theme={null}
  {
    "projectType": "frontend",
    "localPort": 5173,
    "testScope": "diff",
    "needLogin": true,
    "credentials": {
      "username": "test@example.com",
      "password": "testpassword123"
    }
  }
  ```
</CodeGroup>

### Step 2: Analyze Changed Code

The AI calls `testsprite_generate_code_summary` to analyze only the code impacted by your changes.

<Frame>
  <img alt="summary" />
</Frame>

**Diff-Aware Analysis:**

1. **Change Detection**: Focuses on modified files and their dependencies
2. **Impact Mapping**: Identifies affected features and components
3. **Dependency Tracking**: Detects new dependencies or framework changes
4. **Coverage Assessment**: Maps changes to existing test coverage gaps

<CodeGroup>
  ```javascript Tool Call theme={null}
  testsprite_generate_code_summary({
    projectRootPath: "/absolute/path/to/your/project"
  })
  ```

  ```json Expandable Example Output for Changed Feature theme={null}
  {
    "changed_features": [
      {
        "name": "Stripe Payment Integration",
        "description": "New payment flow with Stripe checkout",
        "files": [
          "src/components/Checkout.tsx",
          "src/api/payments.ts"
        ],
        "impact": "High - affects checkout flow and payment processing"
      }
    ],
    "dependencies_added": ["@stripe/stripe-js", "@stripe/react-stripe-js"],
    "files_changed": 2,
    "lines_added": 165,
    "lines_removed": 12
  }
  ```
</CodeGroup>

### Step 3: Generate/Update Normalized PRD

The AI calls `testsprite_generate_standardized_prd` to update requirements based on code changes.

<Frame>
  <img alt="summary" />
</Frame>

**PRD Update Process:**

1. **Merge Changes**: Integrates new features into existing PRD
2. **Update Requirements**: Adjusts validation criteria for modified flows
3. **Maintain Context**: Preserves overall product goals and existing features
4. **Focus on Delta**: Emphasizes what changed rather than rewriting everything

```javascript Tool Called  theme={null}
testsprite_generate_standardized_prd({
  projectPath: "/absolute/path/to/your/project"
})
```

<Tip>For minor changes (bug fixes, small refactors), this step may be skipped to save time. For new features or significant changes, it ensures test requirements are aligned with your updates.</Tip>

### Step 4: Create Targeted Test Plans

The AI calls `testsprite_generate_frontend_test_plan` or `testsprite_generate_backend_test_plan` based on what changed.

<Frame>
  <img alt="summary" />
</Frame>

**Test Plan Focus:**

* **Targeted Coverage**: Tests only impacted features and their dependencies
* **Regression Detection**: Validates that existing flows still work
* **New Functionality**: Ensures new features work as expected
* **Edge Cases**: Covers boundary conditions in changed code

<CodeGroup>
  ```javascript Frontend UI/Business Flows theme={null}
  // Covers: UI changes and new components, modified user flows and journeys, 
  // updated form validations, changed authentication logic
  testsprite_generate_frontend_test_plan({
    projectPath: "/absolute/path/to/your/project",
    needLogin: true
  })
  ```

  ```javascript Backend API/Integration theme={null}
  // Covers: New or modified API endpoints, changed request/response contracts,
  // updated business logic, modified integrations and dependencies
  testsprite_generate_backend_test_plan({
    projectPath: "/absolute/path/to/your/project"
  })
  ```

  ```json Expandable Example Targeted Test Plan theme={null}
  [
    {
      "id": "TC_DIFF_001",
      "title": "Stripe checkout initiates payment successfully",
      "description": "Verify new Stripe payment integration works end-to-end",
      "category": "functional",
      "priority": "High",
      "reason": "New feature in current diff",
      "steps": [
        {
          "type": "action",
          "description": "Add items to cart and proceed to checkout"
        },
        {
          "type": "action",
          "description": "Click 'Pay with Stripe' button"
        },
        {
          "type": "assertion",
          "description": "Verify Stripe payment modal opens"
        },
        {
          "type": "action",
          "description": "Complete test payment with Stripe test card"
        },
        {
          "type": "assertion",
          "description": "Verify payment confirmation and order success"
        }
      ]
    }
  ]
  ```
</CodeGroup>

### Step 5: Generate & Execute Focused Tests

The AI calls `testsprite_generate_code_and_execute` to create and run tests for impacted areas only.

<Frame>
  <img alt="summary" />
</Frame>

<Tabs>
  <Tab title="Test Code Generation Process">
    1. **Incremental Generation**: Creates or updates only tests for changed features
    2. **Smart Reuse**: Leverages existing test utilities and helpers
    3. **Focused Execution**: Runs only tests that could be affected by changes
    4. **Fast Feedback**: Completes in 3-5 minutes vs 10-20 minutes for full suite
  </Tab>

  <Tab title="Execution Benefits">
    * **Faster Runs**: Typically 3-5x faster than full `codebase` scope
    * **Immediate Feedback**: Quick validation of your changes
    * **Focused Reports**: Clear signal on what your change broke or fixed
    * **Iterative Development**: Run frequently during development
  </Tab>
</Tabs>

```javascript Tool Call theme={null}
testsprite_generate_code_and_execute({
  projectName: "your-project-name",
  projectPath: "/absolute/path/to/your/project",
  testIds: [], // empty = all diff-scoped tests
  additionalInstruction: "Focus only on changed modules and impacted flows"
})
```

#### Performance Comparison

| Scope      | Typical Test Count | Execution Time | Use Case                          |
| ---------- | ------------------ | -------------- | --------------------------------- |
| `codebase` | 20-50 tests        | 10-20 min      | Initial setup, major releases     |
| `diff`     | 3-10 tests         | 3-5 min        | During development, PR validation |

### Step 6: Review Diff-Focused Results

TestSprite provides targeted reports showing exactly what your changes affected:

**Report Highlights:**

* **Changed Features Status**: Did your changes work as expected?
* **Regression Detection**: Did your changes break existing flows?
* **New Test Coverage**: What new scenarios are now tested?
* **Healing Suggestions**: Any brittleness introduced by changes?

<Accordion title="Example Diff Report Summary">
  **Your Changes:**

  * Modified `src/components/Checkout.tsx` (+45, -12)
  * Added `src/api/payments.ts` (+120)
  * Updated `package.json` (added Stripe dependencies)

  **Test Results:**

  * ✅ **3 new tests passed** - Stripe payment flow works correctly
  * ⚠️ **1 test needs update** - Checkout button selector changed
  * ✅ **5 existing tests passed** - No regressions detected

  **Recommendations:**

  * Update test selector for new checkout button class
  * Consider adding test for payment failure scenarios
  * All critical paths validated successfully
</Accordion>

## Best Practices for Diff-Scoped Testing

<AccordionGroup>
  <Accordion title="When to Use Diff Scope">
    ✅ **Good Use Cases:**

    * During active feature development
    * After bug fixes or refactors
    * Before committing changes
    * In PR validation workflows

    ❌ **When to Use Codebase Scope Instead:**

    * Initial project onboarding
    * Major refactors affecting many files
    * Pre-release validation
    * When test plan doesn't exist yet
  </Accordion>

  <Accordion title="Iterative Development Tips">
    * **Commit frequently** - Accurate diffs require clean git state
    * **Run subset first** - Use `testIds` to test critical paths quickly
    * **Iterate fast** - Run diff tests every 15-30 minutes during dev
    * **Fix as you go** - Address failures immediately while context is fresh
  </Accordion>

  <Accordion title="Managing Test Scope">
    * Start with empty `testIds: []` to run all diff-scoped tests
    * Use specific `testIds: ["TC_001", "TC_005"]` for rapid iteration
    * Add `additionalInstruction` to guide test generation context
    * Keep PRD updated if feature requirements changed
  </Accordion>
</AccordionGroup>

## Shift-Left Testing Workflow

TestSprite enables true shift-left testing - run tests early and often, even on incomplete code:

<Steps>
  <Step title="Start Coding">
    Begin implementing your feature or fix
  </Step>

  <Step title="Early Test Run (Incomplete)">
    Run diff-scoped tests even if feature isn't complete. Ask your AI assistant: "Test my in-progress payment feature changes"

    Outcome: Discover missing validations, edge cases, UX gaps early
  </Step>

  <Step title="Iterate & Fix">
    Address gaps found by tests, continue coding
  </Step>

  <Step title="Final Test Run (Complete)">
    Run again when feature is ready

    Outcome: High confidence your change works correctly
  </Step>

  <Step title="Commit with Confidence">
    Commit knowing your change is thoroughly tested
  </Step>
</Steps>

## Next Steps

<Columns>
  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Adjust existing test plans
  </Card>

  <Card title="Create Tests for New Projects" href="/mcp/core/create-tests-new-project">
    Full codebase testing workflow
  </Card>

  <Card title="Deploy to Production" href="/mcp/core/deploy-to-production">
    CI/CD integration
  </Card>

  <Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle">
    Understand test triggers
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Auto-repair brittle tests
  </Card>
</Columns>


# Create Tests for New Projects
Source: https://docs.testsprite.com/mcp/core/create-tests-new-project

Generate comprehensive test suites for a brand new project using TestSprite MCP Server.

## When to Use This

Use this guide when onboarding a project that has little or no automated tests. The MCP workflow will analyze your codebase, derive a normalized PRD, generate both frontend and backend test plans, create runnable tests, execute them, and produce reports.

## Prerequisites

* [Installed and configured](/mcp/getting-started/installation) TestSprite MCP in your IDE
* Application can run locally (frontend dev server or backend API)
* Basic test credentials if auth is required

## Quick Start (All-in-One)

<Frame>
  <img alt="generate" />
</Frame>

Ask your IDE assistant:

```text theme={null}
Help me test this project with TestSprite.
```

<Info>The assistant will orchestrate the full flow automatically.</Info>

## Complete Testing Workflow

TestSprite follows a systematic 8-step process to transform your code into thoroughly tested software:

<Card>
  ```mermaid theme={null}
  flowchart LR
      A["Bootstrap Environment<br/>Initialize testing setup"] --> B["Read User PRD<br/>Parse requirements"]
      A --> C["Analyze Code<br/>Understand codebase"]
      
      B --> D["Generate TestSprite PRD<br/>Create normalized requirements"]
      C --> D
      
      D --> E["Create Test Plans<br/>Design comprehensive tests"]
      E --> F["Generate Test Code<br/>Create executable tests"]
      F --> G["Execute Tests<br/>Run in cloud sandbox"]
      G --> H["Results & Analysis<br/>Generate detailed reports"]
      H --> I["AI Fixes Issues<br/>Apply automatic repairs"]
  ```
</Card>

### Step 1: Bootstrap Testing Environment

The AI calls `testsprite_bootstrap_tests` to initialize the testing environment.

<Info>Learn more about bootstrap configuration: [First Test: Configuration](/mcp/getting-started/first-test#step-3%3A-configuration-required)</Info>

<Frame>
  <img alt="bootstrap" />
</Frame>

**Process:**

1. **Project Detection**: Identifies project type (`frontend` or `backend`)
2. **Port Discovery**: Finds running applications and their ports
3. **Configuration Portal**: Opens TestSprite configuration interface
4. **Scope Definition**: Determines testing scope (`codebase` for full project)

<CodeGroup>
  ```javascript Configuration theme={null}
  testsprite_bootstrap_tests({
    localPort: 5173, // or your port
    type: "frontend", // or "backend"
    projectPath: "/absolute/path/to/your/project",
    testScope: "codebase" // test entire project
  })
  ```

  ```json Sample Configuration theme={null}
  {
    "projectType": "frontend",
    "localPort": 5173,
    "testScope": "codebase",
    "needLogin": true,
    "credentials": {
      "username": "test@example.com",
      "password": "testpassword123"
    }
  }
  ```
</CodeGroup>

### Step 2: Read User PRD

TestSprite reads the Product Requirements Document (PRD) that you upload to understand your product goals and requirements.

<Frame>
  <img alt="prd" />
</Frame>

**Process:**

1. **PRD Upload**: Reads the PRD file you uploaded during configuration
2. **Requirement Parsing**: Extracts user stories, acceptance criteria, and functional requirements
3. **Goal Understanding**: Identifies primary product objectives and user needs
4. **Scope Definition**: Determines what features should be tested

### Step 3: Code Analysis & Summary

The AI calls `testsprite_generate_code_summary` to analyze your codebase.

<Frame>
  <img alt="summary" />
</Frame>

**Analysis Process:**

1. **Structure Mapping**: Identifies files, folders, and dependencies
2. **Framework Detection**: Recognizes React, Vue, Angular, Node.js, etc.
3. **Feature Extraction**: Understands implemented functionality
4. **Architecture Analysis**: Maps component relationships
5. **Security Assessment**: Identifies potential vulnerabilities

<CodeGroup>
  ```javascript Tool Call theme={null}
  testsprite_generate_code_summary({
    projectRootPath: "/absolute/path/to/your/project"
  })
  ```

  ```json Expandable Generated Output theme={null}
  {
    "tech_stack": [
      "React",
      "TypeScript", 
      "Material-UI (MUI)",
      "React Router",
      "Vite",
      "Node.js"
    ],
    "features": [
      {
        "name": "Authentication System",
        "description": "User login/logout functionality with protected routes and authentication context",
        "files": ["src/App.tsx", "src/pages/Login.tsx"]
      },
      {
        "name": "Product Catalog",
        "description": "Display products in a grid layout with filtering, search, and product browsing capabilities",
        "files": ["src/pages/ProductCatalog.tsx"]
      }
    ]
  }
  ```
</CodeGroup>

### Step 4: Generate TestSprite Normalized PRD

The AI calls `testsprite_generate_standardized_prd` to create a standardized, normalized Product Requirements Document.

<Frame>
  <img alt="prd" />
</Frame>

<Tip>**TestSprite Innovation** - TestSprite invented this normalized PRD format, a standardized structure that ensures consistent test generation across any project type, regardless of your original PRD format. Learn more in [Key Terms](/mcp/concepts/key-terms#normalized-prd).</Tip>

**PRD Components:**

1. **Product Overview**: High-level description and goals
2. **Core Goals**: Primary objectives and user needs
3. **Key Features**: Main functionality and capabilities
4. **User Flows**: Step-by-step user journeys
5. **Validation Criteria**: Test requirements and acceptance criteria

<CodeGroup>
  ```javascript Tool Call theme={null}
  testsprite_generate_standardized_prd({
    projectPath: "/absolute/path/to/your/project"
  })
  ```

  ```json Expandable Generated PRD Structure theme={null}
  {
    "meta": {
      "project": "Your Application Name",
      "version": "1.0.0",
      "prepared_by": "Generated by TestSprite"
    },
    "product_overview": "High-level description of your application's purpose and functionality.",
    "core_goals": [
      "Primary objective of your application",
      "Key user needs the application addresses",
      "Main business or functional goals"
    ],
    "key_features": [
      "Core feature 1 with implementation approach",
      "Authentication and authorization system",
      "Main user interface components",
      "Data management and persistence"
    ],
    "user_flow_summary": [
      "User entry point and initial interaction",
      "Primary user workflows and actions",
      "Administrative and management functions"
    ],
    "validation_criteria": [
      "Functional requirements validation",
      "Security and access control verification", 
      "User interface and experience validation"
    ],
    "code_summary": {
      "tech_stack": ["Framework", "Language", "Tools"],
      "features": [
        {
          "name": "Feature Name",
          "description": "Feature functionality description",
          "files": ["src/components/Feature.tsx"]
        }
      ]
    }
  }
  ```
</CodeGroup>

### Step 5: Create Test Plans

The AI calls `testsprite_generate_frontend_test_plan` or `testsprite_generate_backend_test_plan` based on project type.

<Frame>
  <img alt="testplan" />
</Frame>

**Test Plan Components:**

1. **Test Cases**: Detailed scenarios with steps
2. **Categories**: Functional, UI/UX, Security, Performance
3. **Priorities**: High, Medium, Low based on user impact
4. **Prerequisites**: Setup requirements for each test
5. **Expected Results**: Success criteria and validation points

<CodeGroup>
  ```javascript Frontend UI/Business Flows theme={null}
  testsprite_generate_frontend_test_plan({
    projectPath: "/absolute/path/to/your/project",
    needLogin: true
  })
  ```

  ```javascript Backend API/Integration theme={null}
  testsprite_generate_backend_test_plan({
    projectPath: "/absolute/path/to/your/project"
  })
  ```

  ```json Expandable Generated Test Plan theme={null}
  [
    {
      "id": "TC001",
      "title": "Login success with valid test credentials",
      "description": "Verify that users can log in successfully using the hardcoded test credentials",
      "category": "functional",
      "priority": "High",
      "steps": [
        {
          "type": "action",
          "description": "Navigate to the login page"
        },
        {
          "type": "action",
          "description": "Input valid hardcoded username"
        },
        {
          "type": "action",
          "description": "Input valid hardcoded password"
        },
        {
          "type": "action",
          "description": "Click the login button"
        },
        {
          "type": "assertion",
          "description": "Verify the user is redirected to the product catalog page"
        },
        {
          "type": "assertion",
          "description": "Verify authentication context reflects logged-in status"
        }
      ]
    }
  ]
  ```
</CodeGroup>

### Step 6: Generate Executable Test Code

The AI calls `testsprite_generate_code_and_execute` to create production-ready test code based on the test plans.

<Frame>
  <img alt="code" />
</Frame>

**Test Code Generation Process:**

1. **Framework Selection**: Chooses appropriate testing framework (Playwright, Cypress, Jest)
2. **Test Structure**: Creates organized test suites and files
3. **Helper Functions**: Generates reusable utility functions
4. **Data Setup**: Creates test data and fixtures
5. **Configuration**: Sets up test environment configuration

<CodeGroup>
  ```javascript Tool Call theme={null}
  testsprite_generate_code_and_execute({
    projectName: "your-project-name",
    projectPath: "/absolute/path/to/your/project",
    testIds: [], // empty = all tests
    additionalInstruction: "Focus on critical user journeys first"
  })
  ```

  ```python Expandable Generated Test Code Example theme={null}
  # TC001_Login_success_with_valid_test_credentials.py
  import asyncio
  from playwright import async_api

  async def run_test():
      pw = None
      browser = None
      context = None
      
      try:
          # Start a Playwright session in asynchronous mode
          pw = await async_api.async_playwright().start()
          
          # Launch a Chromium browser in headless mode
          browser = await pw.chromium.launch(
              headless=True,
              args=[
                  "--window-size=1280,720",
                  "--disable-dev-shm-usage",
                  "--ipc=host",
                  "--single-process"
              ],
          )
          
          # Create a new browser context
          context = await browser.new_context()
          context.set_default_timeout(5000)
          
          # Open a new page in the browser context
          page = await context.new_page()
          
          # Navigate to your target URL
          await page.goto("http://localhost:5174", wait_until="commit", timeout=10000)
          
          # Navigate to the login page
          frame = context.pages[-1]
          elem = frame.locator('xpath=html/body/div/header/div/a[3]').nth(0)
          await page.wait_for_timeout(3000)
          await elem.click(timeout=5000)
          # ... more test steps
  ```
</CodeGroup>

### Step 7: Execute Tests

TestSprite runs the generated test code in secure cloud environments.

<Frame>
  <img alt="cloud" />
</Frame>

**Cloud Execution Process:**

1. **Sandbox Creation**: Isolated testing environment
2. **Dependency Installation**: Installs required packages
3. **Test Execution**: Runs all generated tests
4. **Result Collection**: Gathers results, screenshots, logs
5. **Report Generation**: Creates comprehensive test report

### Step 8: Analyze Results & Reports

TestSprite generates comprehensive test reports with detailed analysis, error descriptions, and actionable fix recommendations.

<Frame>
  <img alt="report" />
</Frame>

<br />

<Tabs>
  <Tab title="What You Get">
    * **Detailed test results** with pass/fail status for each test case
    * **Error analysis** explaining why tests failed
    * **Fix recommendations** with specific steps to resolve issues
    * **Coverage metrics** showing overall project health
    * **Requirement breakdown** organized by feature areas
  </Tab>

  <Tab title="Files Generated">
    * Test files and reports under `testsprite_tests/`
    * `test_results.json` - Structured test results
    * `report_prompt.json` - AI-readable report with fix recommendations
    * HTML reports for human review
  </Tab>
</Tabs>

**Test Report Structure:**

<Accordion title="View Detailed Report Structure">
  **Basic Information** - Every report starts with essential details:

  * **Project Name** - The name of your application
  * **Test Date** - When the tests were run
  * **Version** - Which version was tested
  * **Summary** - Quick overview of results

  **Test Results by Feature** - The report groups tests by your app's main features. Each feature section shows:

  **Feature Overview:**

  * **What it does** - Simple description of the feature
  * **How many tests** - Number of tests run for this feature

  **Each Test Shows:**

  * **Test ID** - Unique identifier like "TC001"
  * **What was tested** - Clear description like "Login with valid password"
  * **Result** - ✅ **Passed** or ❌ **Failed**
  * **Priority** - High, Medium, or Low importance
  * **What went wrong** - Detailed error explanation (if failed)
  * **How to fix it** - Specific recommendations for repairs

  **Overall Results Summary:**

  **Quick Stats:**

  * **73% of features tested** - How much of your app was covered
  * **56% of tests passed** - Overall success rate
  * **Critical issues found** - Most important problems to fix

  **Feature-by-Feature Breakdown:**

  | Feature Area    | Tests Run | ✅ Passed | ❌ Failed |
  | --------------- | --------- | -------- | -------- |
  | User Login      | 2         | 1        | 1        |
  | Product Display | 2         | 2        | 0        |
  | Admin Panel     | 3         | 0        | 3        |
  | Shopping Cart   | 3         | 3        | 0        |
</Accordion>

### Step 9: AI Fixes Issues

When you request fixes with **"Help me fix the codebase based on these test results"**, your IDE AI assistant:

<Card>
  ```mermaid theme={null}
  flowchart LR
      A[Reads Test Results] --> B[Analyzes Test Report]
      B --> C[Examines Error Details]
      C --> D[Identifies Root Causes]
      D --> E[Generates Targeted Fixes]
      E --> F[Applies Changes]
      F --> G[Validates Fixes]
  ```
</Card>

<Tip>**TestSprite's Role** - TestSprite provides the analysis and recommendations, while your IDE's AI assistant implements the actual fixes.</Tip>

<Tabs>
  <Tab title="Process">
    1. **Reads Test Results**: Reviews `testsprite_tests/tmp/test_results.json` for detailed failure data
    2. **Analyzes Test Report**: Processes `testsprite_tests/tmp/report_prompt.json` for context and recommendations
    3. **Examines Error Details**: Reviews stderr messages and test visualizations
    4. **Identifies Root Causes**: Determines underlying issues causing test failures
    5. **Generates Targeted Fixes**: Creates code changes based on TestSprite's recommendations
    6. **Applies Changes**: Modifies your codebase automatically
    7. **Validates Fixes**: Re-runs tests to verify solutions
  </Tab>

  <Tab title="Example Fix Application">
    The AI assistant automatically applies fixes based on TestSprite's recommendations. Here's a real example showing how a missing delete button was identified and added to fix a failing test.

    <CodeGroup>
      ```javascript Before theme={null}
      // Missing delete button in admin panel
      const AdminProductCard = ({ product, onDelete }) => {
        return (
          <div className="product-card">
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <div className="actions">
              <button className="edit-btn">Edit</button>
            </div>
          </div>
        );
      };
      ```

      ```javascript After theme={null}
      // AI-generated fix
      const AdminProductCard = ({ product, onDelete }) => {
        return (
          <div className="product-card">
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <div className="actions">
              <button className="edit-btn">Edit</button>
              {/* AI added this button to fix failing test */}
              <button 
                id="admin-delete-btn"
                className="delete-btn"
                onClick={() => onDelete(product.id)}
              >
                Delete
              </button>
            </div>
          </div>
        );
      };
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Best Practices

<AccordionGroup>
  <Accordion title="Before Testing">
    * Ensure all applications are running on specified ports
    * Prepare test credentials for auth flows
    * Update README with clear project description
    * Clean up any development artifacts
  </Accordion>

  <Accordion title="During Testing">
    * Review generated PRD for accuracy
    * Examine test plan coverage
    * Monitor test execution progress
    * Note any configuration adjustments needed
  </Accordion>

  <Accordion title="After Testing">
    * Analyze test results thoroughly
    * Understand failure patterns
    * Apply fixes systematically
    * Document lessons learned
    * Re-run tests to validate fixes
  </Accordion>
</AccordionGroup>

## Next Steps

<Columns>
  <Card title="Create Tests for New Changes" href="/mcp/core/create-tests-new-feature">
    Test diff-scoped changes
  </Card>

  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Adjust existing tests
  </Card>

  <Card title="Continuous Monitoring" href="/mcp/core/continuous-monitoring">
    Integrate into CI/CD
  </Card>

  <Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle">
    Understand what we test
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Learn about auto-healing
  </Card>
</Columns>


# Deploy MCP Tests
Source: https://docs.testsprite.com/mcp/core/deploy-to-production

Learn how to deploy and run your MCP tests against staging and production environments.

Once you've created and validated tests, you can deploy them to run against your staging or production environments. This guide walks you through pushing your tests to the MCP Tests web portal for continuous monitoring of your deployed applications.

## Prerequisites

Before deploying your tests, ensure you have:

* Successfully created and run tests locally using MCP
* Access to the MCP Tests web portal
* The URL of your deployed application (staging or production)

## Deployment Steps

<Steps>
  <Step title="Access the MCP Tests Web Portal">
    Log in to the MCP Tests web portal and navigate to your project. You'll see a list of all test suites that have been created locally.

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Initiate Test Deployment">
    Locate the test suite you want to deploy and click the **"Deploy Tests"** button next to it. This opens the test selection interface.

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Select Tests to Deploy">
    Review the available tests and use the checkboxes to select which ones you want to deploy. You can select individual tests or multiple tests at once depending on your deployment strategy.

    <Tip>Consider starting with a subset of critical tests before deploying your entire test suite to production.</Tip>

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Confirm Test Selection">
    After selecting your tests, click the **"Deploy Tests"** button in the upper right corner to proceed with the deployment.

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Configure Target Environment">
    Enter the URL of your deployed application where the tests will run (e.g., `https://your-app.com` or `https://staging.your-app.com`). This URL becomes the target environment for all test executions.

    <Warning>Ensure the URL is accessible and that any required authentication credentials are properly configured.</Warning>

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Monitor Test Execution">
    Navigate to the **"All Tests"** page to monitor your test results in real-time.

    <Frame>
      <img alt="plan" />
    </Frame>

    Here you can:

    * View detailed test execution logs
    * Analyze test visualizations and screenshots
    * Review any failures or issues
    * Track test performance over time
  </Step>
</Steps>

## Next Steps

After deploying your tests to production, you can **configure alerts to notify your team of test failures**, or follow the steps below:

<Columns>
  <Card title="Set up continuous monitoring" href="/mcp/core/continuous-monitoring">
    Run tests automatically on a schedule
  </Card>

  <Card title="Review test maintenance guide" href="/mcp/maintenance/test-maintenance">
    Best practices for keeping your tests up to date
  </Card>
</Columns>


# Modify or Update Tests
Source: https://docs.testsprite.com/mcp/core/modify-tests

Update existing tests to reflect changes in your application using TestSprite's interactive in-place editing capabilities.

## Overview

TestSprite gives you full control over your automated test cases with powerful in-place editing. Whether you're watching tests run live or reviewing results days later, you can fine-tune every step to match your exact requirements.

<Frame>
  <img alt="modification hero" />
</Frame>

## Interactive Step Editing

Click on any step to see a **snapshot** of that exact moment in your test, then modify it if needed.

<Frame>
  <img alt="modification hero" />
</Frame>

### Edit Any Interaction

When you select a step, you can:

<Steps>
  <Step title="Change the Interaction Type">
    Switch between Click, Navigate, Input, Scroll, Assert, or modify the Selector.

    <Frame>
      <img alt="change interaction type" />
    </Frame>
  </Step>

  <Step title="Update Input Values">
    Change what text gets entered into form fields.

    <Frame>
      <img alt="update input values" />
    </Frame>
  </Step>

  <Step title="Adjust Timeouts">
    Fine-tune wait times for slow-loading elements.

    <Frame>
      <img alt="adjust timeouts" />
    </Frame>
  </Step>

  <Step title="Modify Interaction Element">
    Pick a new element on the page if the current one isn't right.

    <Frame>
      <img alt="modification hero" />
    </Frame>
  </Step>
</Steps>

### Visual Element Selection

Don't like the current locator? Simply click any element on the page preview, and TestSprite will prompt you: *"Change locator to this element to suit your needs."*

This visual selection means you don't need to manually write CSS selectors or XPath—just point and click.

<Frame>
  <img alt="change locator" />
</Frame>

### Smart Regeneration Options

TestSprite will automatically regenerate the affected steps while preserving your customizations.

<Frame>
  <img alt="smart regeneration options" />
</Frame>

After making your edits, choose how TestSprite should handle the changes:

| Option                                     | When to Use                                                      |
| ------------------------------------------ | ---------------------------------------------------------------- |
| <kbd>Update this step only</kbd>           | Your change is isolated and doesn't affect subsequent steps      |
| <kbd>Update this and following steps</kbd> | Your change impacts the test flow, and later steps need to adapt |

## Key Benefits

<AccordionGroup>
  <Accordion title="No More Black-Box Testing">
    See exactly what your tests are doing with video recordings and step-by-step snapshots.
  </Accordion>

  <Accordion title="Fix Tests Without Rewriting Them">
    Visual editing means you can adjust locators, inputs, and actions without touching code.
  </Accordion>

  <Accordion title="Maintain Test Suites Over Time">
    As your application evolves, easily update test steps to match new UI layouts or workflows.
  </Accordion>

  <Accordion title="Debug Failures Faster">
    Pinpoint issues instantly with detailed error messages and execution recordings.
  </Accordion>
</AccordionGroup>

## Quick Reference

| Tool                                    | Purpose                                            |
| --------------------------------------- | -------------------------------------------------- |
| `testsprite_generate_code_and_execute`  | Generate and run tests with live progress tracking |
| `testsprite_open_test_result_dashboard` | Reopen dashboard to review/edit past test runs     |

## Next Step

<Columns>
  <Card title="Progress Dashboard" href="/mcp/core/test-progress-dashboard">
    Monitor real-time test execution
  </Card>

  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature">
    Test diff-scoped changes
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Learn about auto-healing
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Explore all available tools
  </Card>
</Columns>


# Regenerate Tests
Source: https://docs.testsprite.com/mcp/core/regenerate-tests

Regenerate test suites for existing projects to update coverage.

There are two different ways to regenerate tests depending on whether you want to update just a few cases or start over completely.

<Tabs>
  <Tab title="Regenerate Subset of Test Cases">
    <Frame>
      <img alt="plan" />
    </Frame>

    <Steps>
      <Step title="Open your TestSprite test plan file">
        Open your TestSprite test plan file (e.g. `testsprite_frontend_test_plan.json`).
      </Step>

      <Step title="Edit the test case description">
        Find the test case you want to change, edit the descriptionand, and save the file ( <Tooltip><kbd>⌘S</kbd></Tooltip> ). For example:

        ```md Before/After Example theme={null}
        Before: Verify user can log in with valid email and password
        After: Verify user can log in with email 'example@gmail.com', password 'xxxxxx'
        ```
      </Step>

      <Step title="Prompt in your IDE">
        ```text Example Prompt theme={null}
         Rerun the Xth test for me using testsprite_generate_code_and_execute
        ```
      </Step>

      <Step title="TestSprite runs the updated tests">
        TestSprite will detect your change, update the relevant test code, and run the updated tests automatically.
      </Step>
    </Steps>

    <Info>
      **Key Point:** You only need to change the description in the plan. TestSprite handles the rest.
    </Info>
  </Tab>

  <Tab title="Regenerate Entire Project">
    If you want a clean start or have made major changes:

    <Steps>
      <Step title="Delete the testsprite_tests folder">
        Delete the `testsprite_tests` folder in your project.

        <Frame>
          <img alt="delete" />
        </Frame>

        <Info>
          This ensures no outdated files remain.
        </Info>
      </Step>

      <Step title="Prompt in your IDE">
        In your IDE, type again:

        ```text Example Prompt theme={null}
        Help me test this project with TestSprite
        ```
      </Step>

      <Step title="TestSprite generates new tests">
        TestSprite will generate a brand new test plan and test code for the whole project.
      </Step>
    </Steps>

    <Warning>
      **When to use this:** If your project has changed a lot and the old test plan no longer matches well.
    </Warning>
  </Tab>
</Tabs>


# Rerun Existing Tests
Source: https://docs.testsprite.com/mcp/core/rerun-tests

Execute previously generated tests to validate your application.

Sometimes you just want to rerun the same tests as the previous run—maybe to double-check after a bug fix.

<Tip>
  This is useful after you fix a bug or change code and want to confirm nothing is broken.
</Tip>

<Tabs>
  <Tab title="Rerun All Tests">
    <Frame>
      <img alt="prd" />
    </Frame>

    In your coding IDE, simply type:

    ```text Example Prompt theme={null}
    Help me rerun all the tests with TestSprite.
    ```

    TestSprite will automatically detect your existing project test suite and execute all of the tests again with the `testsprite_rerun_tests` tool. You'll see updated results directly in **your IDE** or **TestSprite dashboard**.
  </Tab>

  <Tab title="Rerun Subset of Tests">
    TestSprite gives you the flexibility to rerun only **a subset of your tests** instead of executing the entire suite. This is useful when you want to quickly validate specific scenarios without waiting for every test to finish.

    <Frame>
      <img alt="prd" />
    </Frame>

    You can annotate the tests you want to rerun and pass their indexes directly to the `testsprite_rerun_tests` command. For example, to re-run only the 1st, 3rd, and 12th tests:

    ```text Example Prompt theme={null}
    Help me rerun the 1, 3 and 12th tests with TestSprite.
    ```
  </Tab>
</Tabs>


# Test Progress Dashboard
Source: https://docs.testsprite.com/mcp/core/test-progress-dashboard

Monitor your entire test suite as it runs with live status updates, detailed test insights, and execution recordings.

## Overview

When you trigger `testsprite_generate_code_and_execute`, TestSprite automatically opens a live progress dashboard where you can monitor your entire test suite as it runs.

<Frame>
  <img alt="generate and execute code" />
</Frame>

<br />

<Tabs>
  <Tab title="Real-Time Monitoring">
    Watch your test cases execute with live status updates. Each test displays its current state—whether it's still running, has passed, or encountered an issue.

    <Frame>
      <img alt="modification progress" />
    </Frame>
  </Tab>

  <Tab title="Search & Filter Tests">
    Quickly locate specific tests using the search bar by <kbd>Test Name</kbd> or <kbd>ID</kbd>. Filter your test suite by <kbd>Status</kbd>, <kbd>Creation Date</kbd>, or <kbd>Last Modified Time</kbd> to focus on what matters most.

    <Frame>
      <img alt="modification filter" />
    </Frame>
  </Tab>

  <Tab title="Sort Your Way">
    Organize your test list by <kbd>Created Date</kbd>, <kbd>Last Execution Time</kbd>, or <kbd>Alphabetically</kbd> to streamline your review workflow.

    <Frame>
      <img alt="modification sort" />
    </Frame>
  </Tab>
</Tabs>

## Test Detail View

Click on any test case to dive into its detailed execution results.

### Execution Recording

Every test run is recorded, giving you a complete video playback of exactly what happened during execution.

<Frame>
  <img alt="modification video" />
</Frame>

### Test Results at a Glance

Get a quick summary of each test's outcome, including pass/fail status, error details, and timing information.

<Frame>
  <img alt="modification video 1" />
</Frame>

The **Test Result** section shows you:

| Detail                      | Description                       |
| --------------------------- | --------------------------------- |
| <kbd>Pass/Fail Status</kbd> | Clear visual indicators           |
| <kbd>Error Messages</kbd>   | Detailed messages when tests fail |

### Step-by-Step Breakdown

Drill into each test to see every action it performed, from navigation and input to assertions, so you can pinpoint exactly where things went right or wrong.

<Frame>
  <img alt="modification actions" />
</Frame>

Each test displays its individual steps with the corresponding action type:

| Action              | Description                  |
| ------------------- | ---------------------------- |
| <kbd>Navigate</kbd> | URL navigation actions       |
| <kbd>Input</kbd>    | Form field entries           |
| <kbd>Click</kbd>    | Button and link interactions |
| <kbd>Scroll</kbd>   | Page scrolling actions       |
| <kbd>Assert</kbd>   | Verification checkpoints     |

## Review Past Test Runs Anytime

Use the `testsprite_open_test_result_dashboard` tool to reopen the progress dashboard at any time. Simply prompt:

<Frame>
  <img alt="terminal generate" />
</Frame>

<CodeGroup>
  ```text Example Prompt theme={null}
  open test result dashboard of testsprite cases
  ```
</CodeGroup>

This brings back the full dashboard view where you can:

* Browse all your historical test suites
* Review execution recordings from previous runs
* Make modifications to any existing test case
* Re-run updated tests with your changes


# MCP Tools References
Source: https://docs.testsprite.com/mcp/core/tools

Complete reference for all TestSprite MCP Server tools available to your AI assistant.

## Core Tools

TestSprite MCP Server provides **8 core tools** that work together to deliver comprehensive automated testing. Your AI assistant uses these tools automatically when you request testing.

<AccordionGroup>
  <Accordion title="testsprite_bootstrap_tests">
    **Purpose:** Initialize testing environment and configuration

    **Parameters:**

    * `localPort` (number): Port where your application is running (default: 5173)
    * `path` (string): Specifies a path you want to test directly, which isn’t accessible through navigation from other pages.
    * `type` (string): Project type - "frontend" or "backend"
    * `projectPath` (string): Absolute path to your project directory
    * `testScope` (string): Testing scope - "codebase" or "diff"

    **Usage:**

    ```javascript theme={null}
    testsprite_bootstrap_tests({
      localPort: 3000,
      type: "frontend",
      projectPath: "/Users/dev/my-project",
      testScope: "codebase"
    })
    ```

    **Response:**
    The tool returns next\_action instructions that guide the AI to:

    * Start your application if not running
    * Generate code summary automatically
    * Continue with the testing workflow

    **What it does:**

    * Detects project type and structure
    * Checks if application is running on specified port
    * Initializes testing configuration, whether it should test the entire codebase or just the code diffs
    * Opens TestSprite configuration portal
    * Automatically proceeds to code analysis
  </Accordion>

  <Accordion title="testsprite_generate_code_summary">
    **Purpose:** Analyze codebase and generate architectural summary

    **Parameters:**

    * `projectRootPath` (string): Absolute path to project root

    **Usage:**

    ```javascript theme={null}
    testsprite_generate_code_summary({
      projectRootPath: "/Users/dev/my-project"
    })
    ```

    **Response:**
    The tool creates a `code_summary.json` file in your project containing:

    * Project architecture analysis
    * Framework and dependency detection
    * Feature mapping
    * Entry point identification

    **What it does:**

    * Scans entire project structure
    * Identifies technologies and frameworks
    * Analyzes code patterns and architecture
    * Generates comprehensive code summary file
    * Required for subsequent testing steps
  </Accordion>

  <Accordion title="testsprite_generate_standardized_prd">
    **Purpose:** Generate standardized Product Requirements Document

    **Parameters:**

    * `projectPath` (string): Absolute path to project root

    **Usage:**

    ```javascript theme={null}
    testsprite_generate_standardized_prd({
      projectPath: "/Users/dev/my-project"
    })
    ```

    **Response:**
    Creates a `standard_prd.json` file containing:

    * Product overview and goals
    * User stories with acceptance criteria
    * Functional requirements
    * Technical specifications

    **What it does:**

    * Analyzes code to understand product functionality
    * Creates structured PRD document
    * Saves standardized format for test generation
    * Essential foundation for test planning
  </Accordion>

  <Accordion title="testsprite_generate_frontend_test_plan">
    **Purpose:** Generate comprehensive frontend test plan

    **Parameters:**

    * `projectPath` (string): Absolute path to project root
    * `needLogin` (boolean): Whether authentication is required (default: true)

    **Usage:**

    ```javascript theme={null}
    testsprite_generate_frontend_test_plan({
      projectPath: "/Users/dev/my-project",
      needLogin: true
    })
    ```

    **Response:**
    Creates a `frontend_test_plan.json` file with:

    * UI interaction test cases
    * Form validation scenarios
    * Navigation and routing tests
    * Visual regression checks
    * Authentication flows (if needLogin is true)

    **What it does:**

    * Analyzes frontend components and features
    * Generates UI-specific test scenarios
    * Creates comprehensive test coverage plan
    * Automatically proceeds to test execution
  </Accordion>

  <Accordion title="testsprite_generate_backend_test_plan">
    **Purpose:** Generate comprehensive backend test plan

    **Parameters:**

    * `projectPath` (string): Absolute path to project root

    **Usage:**

    ```javascript theme={null}
    testsprite_generate_backend_test_plan({
      projectPath: "/Users/dev/my-project"
    })
    ```

    **Response:**
    Creates a `backend_test_plan.json` file with:

    * API endpoint testing
    * Functional integration testing
    * Database operation tests
    * Authentication and authorization
    * Error handling scenarios

    **What it does:**

    * Analyzes backend APIs and services
    * Generates comprehensive API test scenarios
    * Creates database and integration tests
    * Handles authentication configurations
    * Automatically proceeds to test execution
  </Accordion>

  <Accordion title="testsprite_generate_code_and_execute">
    **Purpose:** Generate and execute comprehensive test suite

    **Parameters:**

    * `projectName` (string): Name of the project (typically the root directory name)
    * `projectPath` (string): Absolute path to project root
    * `testIds` (array): Specific test IDs to run (default: \[] - runs all tests)
    * `additionalInstruction` (string): Additional testing instructions (default: "")

    **Usage:**

    ```javascript theme={null}
    testsprite_generate_code_and_execute({
      projectName: "my-ecommerce-app",
      projectPath: "/Users/dev/my-project",
      testIds: [], // Run all tests
      additionalInstruction: "Focus on checkout flow and payment security"
    })
    ```

    **Response:**
    Executes tests and creates:

    * Individual test files for each test case
    * Test execution results
    * Bug reports and fix recommendations
    * `testsprite_tests/tmp/test_results.json` with comprehensive results
    * `tmp/report_prompt.json` for AI analysis
    * `TestSprite_MCP_Test_Report.md` - human-readable test report
    * `TestSprite_MCP_Test_Report.html` - HTML test report

    **What it does:**

    * Generates actual test code (Playwright, Cypress, etc.)
    * Executes tests against your running application
    * Provides detailed results with screenshots/videos
    * Identifies bugs and suggests fixes
    * Creates comprehensive test reports
  </Accordion>

  <Accordion title="testsprite_open_test_result_dashboard">
    **Purpose:** Reopen the test result dashboard to review and edit past test runs

    **Parameters:** None

    **Usage:**

    ```javascript theme={null}
    testsprite_open_test_result_dashboard()
    ```

    **Response:**
    Opens the full dashboard view showing:

    * Previously established test suite and its result
    * Execution recordings from previous runs
    * Step-by-step breakdowns for each test case

    **What it does:**

    * Reopens the live progress dashboard on-demand
    * Lets you browse, filter, and sort all past test runs
    * Allows in-place editing of any existing test case
    * Enables re-running updated tests with your changes
  </Accordion>

  <Accordion title="testsprite_rerun_tests (beta)">
    **Purpose:** Rerun the previously generated test cases

    **Parameters:**

    * `projectPath` (string): Absolute path to your project directory

    **Usage:**

    ```javascript theme={null}
    testsprite_rerun_tests({
      projectPath: "/Users/dev/my-project"
    })
    ```

    **Response:**
    Executes the previously created tests and refines:

    * Individual test files for each test case potentially if the previous run (during creation) was stopped early due to errors
    * Test execution results
    * Bug reports and fix recommendations
    * `testsprite_tests/tmp/test_results.json` with comprehensive results
    * `tmp/report_prompt.json` for AI analysis
    * `TestSprite_MCP_Test_Report.md` - human-readable test report
    * `TestSprite_MCP_Test_Report.html` - HTML test report

    **What it does:**

    * Refines actual test code
    * Executes previously created test cases against your running application
    * Provides refined results with screenshots/videos according to the newest execution results
    * Identifies bugs and suggests fixes
    * Creates comprehensive test reports
  </Accordion>
</AccordionGroup>

## Tool Chain Workflow

The tools work together in a specific sequence following the complete TestSprite workflow:

<Card>
  ```mermaid theme={null}
  graph TD
      A[testsprite_bootstrap_tests] --> B[Read User PRD]
      B --> C[testsprite_generate_code_summary]
      C --> D[testsprite_generate_standardized_prd]
      D --> E{Project Type?}
      E -->|Frontend| F[testsprite_generate_frontend_test_plan]
      E -->|Backend| G[testsprite_generate_backend_test_plan]
      F --> H[testsprite_generate_code_and_execute]
      G --> H
      H --> I[Generate Test Code]
      I --> J[Execute Tests]
      J --> K[Results & Analysis]
      K --> L[Modify Tests if Needed]
      L --> M[IDE Fixes Issues]
      M --> N[Rerun the tests and check the fixes]
  ```
</Card>

## File Structure

After running the tools, your project will have:

```text Expandable File Structure theme={null}
my-project/
├── testsprite_tests/
│   ├── tmp/
│   │   ├── prd_files/              # Temporary PRD files
│   │   ├── config.json             # Project configuration
│   │   ├── code_summary.json       # Code analysis
│   │   ├── report_prompt.json      # AI analysis data
│   │   └── test_results.json       # Execution results
│   ├── standard_prd.json           # Product requirements
│   ├── TestSprite_MCP_Test_Report.md     # Human-readable test report
│   ├── TestSprite_MCP_Test_Report.html   # HTML test report
│   ├── TC001_Login_Success_with_Valid_Credentials.py
│   ├── TC002_Login_Failure_with_Invalid_Credentials.py
│   ├── TC003_Product_Catalog_Display.py
│   ├── TC004_View_Product_Details.py
│   ├── TC005_Purchase_Product_Success.py
│   ├── TC006_Purchase_Product_Failure.py
│   ├── TC007_Order_History_Accessibility.py
│   ├── TC008_Admin_Panel_Access_Control.py
│   └── ...                         # Additional test files
└── ...
```

## Best Practices

<AccordionGroup>
  <Accordion title="Ensure Application is Running">
    The bootstrap tool checks if your app is running on the specified port
  </Accordion>

  <Accordion title="Use Absolute Paths">
    Always provide full absolute paths for `projectPath`
  </Accordion>

  <Accordion title="Authentication Setup">
    Provide login or authentication credentials in the TestSprite configuration portal for testing workflows
  </Accordion>

  <Accordion title="Incremental Testing">
    Use `testIds` parameter to run specific test cases
  </Accordion>

  <Accordion title="Additional Instructions">
    Provide context-specific instructions for better test generation
  </Accordion>
</AccordionGroup>

## Common Workflows

<Tabs>
  <Tab title="Full Testing Workflow">
    Simply prompt your AI assistant:

    ```text theme={null}
    "Help me test this project with TestSprite"
    ```

    The AI will automatically:

    1. Bootstrap the testing environment
    2. Analyze your codebase
    3. Generate comprehensive test plans
    4. Execute all tests
    5. Provide results and fix recommendations
  </Tab>

  <Tab title="Targeted Testing">
    For specific test cases:

    ```text theme={null}
    "Run tests TC001 and TC002 with focus on security"
    ```

    The AI will call:

    ```bash theme={null}
    testsprite_generate_code_and_execute ({
      projectName: "my-project",
      projectPath: "/path/to/project",
      testIds: ["TC001", "TC002"],
      additionalInstruction: "Focus on security vulnerabilities"
    })
    ```
  </Tab>
</Tabs>

## Next Steps

<Columns>
  <Card title="Install TestSprite MCP" href="../getting-started/installation">
    Get up and running in minutes
  </Card>

  <Card title="Create Tests for New Projects" href="create-tests-new-project">
    First-time setup and full-suite generation
  </Card>

  <Card title="Create Tests for New Change" href="create-tests-new-feature">
    Diff-scoped testing for recent changes
  </Card>

  <Card title="Modify or Update Tests" href="modify-tests">
    Keep tests aligned with app changes
  </Card>
</Columns>


# First MCP Test
Source: https://docs.testsprite.com/mcp/getting-started/first-test

Experience the magic of TestSprite MCP Server with your first automated test in under 10 minutes.

By the end of this guide, you'll have run your first **automated test suite**, seen AI generate comprehensive test plans, watched tests execute in the cloud, received detailed test reports, and applied **automatic bug fixes**.

<Info>
  Before starting, ensure you have [TestSprite MCP Server installed](../../mcp/getting-started/installation) and **your IDE open**.
</Info>

## Step 1: Prepare Your Project

**Start Your Application** - Make sure your application is running locally:

```bash Example theme={null}
# For frontend applications (examples)
npm run dev          # Usually runs on port 3000, 5173, or 8080
 
# For backend applications (examples)
node index.js        # Usually runs on port 8000, 3001, or 4000
```

```text Project Structure Example theme={null}
my-project/
├── frontend/          # React, Vue, Angular, etc.
│   ├── src/
│   ├── package.json
│   └── ...
├── backend/           # Node.js, Python, etc.
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── README.md
└── package.json
```

## Step 2: The Magic Command

Open **your IDE Chat** and follow these steps:

1. **Open** a new chat window in your IDE
2. **Type** the magic command:

```text icon="file-lines" theme={null}
Can you test this project with TestSprite?
```

3. Drag and drop your project folder into the chat if you'd like to test a specific sub-project
4. Press  <kbd>⇧ Enter</kbd>

That's it! Your AI assistant will now take over and guide you through the entire testing process.

## Step 3: Configuration (Required)

<Frame>
  <img alt="config" />
</Frame>

<Note>The Testing Configuration page will open in your browser. Complete the setup here to continue your test.</Note>

When the bootstrap tool opens, you must configure:

1. **Testing Type**

<Frame>
  <img alt="type" />
</Frame>

<Tabs>
  <Tab title="Mode">
    * **Frontend**: Select this if you want to test your UI and user flows (e.g. buttons, forms, navigation).

    * **Backend**: Select this if you want to test your APIs, services, or server logic.
  </Tab>

  <Tab title="Scope">
    * **Codebase**: Runs tests against the entire project. Use this if you want a full test sweep or haven’t run MCP before.
    * **Code Diff**: Runs tests only against your recent changes (uncommitted Git changes). Use this to quickly validate new work without testing everything again.
  </Tab>
</Tabs>

2. **Test Account Credentials** - If your app requires login:

<Tabs>
  <Tab title="Frontend">
    <Frame>
      <img alt="credential" />
    </Frame>

    ```json Crediential Examples theme={null}
      Username: test@example.com
      Password: your-test-password
    ```
  </Tab>

  <Tab title="Backend">
    <Frame>
      <img alt="credential" />
    </Frame>

    | Authentication Type | Description                       |
    | :------------------ | :-------------------------------- |
    | <kbd>Basic</kbd>    | Uses username & password          |
    | <kbd>Bearer</kbd>   | Secure token-based authentication |
    | <kbd>API-key</kbd>  | Uses a unique API key for access  |
    | <kbd>None</kbd>     | No authentication required        |
  </Tab>
</Tabs>

3. **Application URLs:**

<Frame>
  <img alt="portal" />
</Frame>

```text URL Examples theme={null}
Frontend: http://localhost:5173
Backend: http://localhost:4000
```

4. **Product Requirements Document**

<Frame>
  <img alt="prd" />
</Frame>

Upload existing PRD (required). Even a draft or low-quality PRD is fine. TestSprite AI will generate a normalized PRD based on your upload.

## Step 4: The Automated Workflow

Your AI assistant will automatically handle the **entire testing process** by running through these steps. It takes care of everything from understanding your project to running the actual tests, so you don't have to do any of the work manually.

Learn more about details steps at [Testing Workflow](../concepts/workflow).

## Step 5: Review Test Results

After testing, you'll find these files in your project:

```text Expandable After Testing Project Structure Example theme={null}
testsprite_tests/
├── tmp/
│   ├── prd_files/                 # Uploaded PRD files
│   ├── config.json               # Test configuration
│   ├── code_summary.json         # Code analysis
│   ├── report_prompt.json        # AI analysis data
│   └── test_results.json         # Detailed test results
├── standard_prd.json             # Normalized PRD
├── TestSprite_MCP_Test_Report.md # Human-readable report
├── TestSprite_MCP_Test_Report.html # HTML report
├── TC001_Login_Success_with_Valid_Credentials.py
├── TC002_Login_Failure_with_Invalid_Credentials.py
└── ...                           # Additional test files
```

**Understanding Test Results** - The test report shows overall coverage, pass rate, failed tests with detailed failure analysis, and categories (Functional, UI/UX, Security, Performance).

## Step 6: Automatic Bug Fixes

**Request Fixes** - After reviewing the test results, simply ask:

```text icon="file-lines" theme={null}
Please fix the codebase based on TestSprite testing results.
```

The AI will analyze failing tests, identify problematic code sections, apply targeted fixes automatically, re-run tests to verify fixes, and iterate until issues are resolved.

## Example Output

**Test Plan Generated:**

```json Expandable Test Plan Example theme={null}
{
  "testCases": [
    {
      "id": "TC001",
      "title": "User Authentication Login",
      "description": "Test user login with valid credentials",
      "category": "Functional",
      "priority": "High",
      "steps": [
        "Navigate to login page",
        "Enter valid username and password",
        "Click login button",
        "Verify successful login"
      ]
    }
    // ... 17 more test cases
  ]
}
```

**Test Report Summary:**

```json Expandable Test Report Summary Example theme={null}
{
  "summary": {
    "totalTests": 18,
    "passed": 12,
    "failed": 6,
    "passRate": "67%",
    "coverage": "85%"
  },
  "failures": [
    {
      "testId": "TC005",
      "title": "Admin Panel Access",
      "error": "Button not found: #admin-delete-btn",
      "recommendation": "Add missing delete button in admin panel"
    }
  ]
}
```

## Tips for Success

<AccordionGroup>
  <Accordion title="Ensure Apps Are Running">
    Frontend and backend should be accessible on standard ports
  </Accordion>

  <Accordion title="Project Structure">
    Include README with setup instructions and descriptive folder names
  </Accordion>

  <Accordion title="Test Credentials">
    Prepare test user accounts with non-production data
  </Accordion>

  <Accordion title="Review Generated Files">
    Check the generated PRD and test plan for accuracy
  </Accordion>
</AccordionGroup>

## Next Steps

**Congratulations!** You've successfully run your first automated test with TestSprite MCP Server.

<Columns>
  <Card title="Complete Testing Workflow" href="../concepts/test-type-lifecycle">
    Understand the full process
  </Card>

  <Card title="View Examples" href="../../learn/mcp-demo">
    See real-world use cases
  </Card>

  <Card title="Join Discord" href="https://discord.com/invite/GXWFjCe4an">
    Get help and share experiences
  </Card>

  <Card title="Contribute on Github" href="https://github.com/wangy44624/docs">
    Contribute and report issues
  </Card>
</Columns>


# Installation
Source: https://docs.testsprite.com/mcp/getting-started/installation

Get TestSprite MCP Server up and running in your IDE in under 2 minutes.

## Prerequisites

Before installing TestSprite MCP Server, ensure you have:

1. **Compatible IDEs**
2. **TestSprite Account** - [Sign up for free  <Icon icon="arrow-up-right-from-square" />](https://www.testsprite.com/auth/cognito/sign-up)
3. **Node.js >= 22** - [Download Node.js  <Icon icon="arrow-up-right-from-square" />](https://nodejs.org/) (required for running MCP server)

<AccordionGroup>
  <Accordion title="Which IDEs and editors does TestSprite support?">
    TestSprite supports **Trae**, **Cursor**, **Claude Code**, **Windsurf**, **VS Code**, and **GitHub Copilot**. Simply install our MCP Server get started.
  </Accordion>

  <Accordion title="How do I check my Node.js version?">
    Run `node --version` to check your version. For detailed setup instructions, see [Node.js Configuration](../troubleshooting/installation-issues#node-js-version-compatibility).
  </Accordion>
</AccordionGroup>

## Get Your API Key

First, you'll need a TestSprite API key for any installation method:

<Frame>
  <img alt="API Key" />
</Frame>

1. Sign in to your [TestSprite Dashboard  <Icon icon="arrow-up-right-from-square" />](https://www.testsprite.com/dashboard)
2. Navigate to **API Keys** under Settings
3. Click **"New API Key"**
4. **Copy** your API key (you'll need it for installation)

## Installation

Follow the instructions for your specific client to add the TestSprite MCP server.

<Tabs>
  <Tab title="Trae">
    <Frame>
      <img alt="trae" />
    </Frame>

    1. Get your [**API key**](#get-your-api-key).
    2. In Trae, navigate to `AI Sidebar > AI Management`.
    3. Select `MCP > Add > Add from Marketplace`.
    4. Search for **TestSprite** and add to your MCP list.

    <Frame>
      <img alt="trae" />
    </Frame>

    5. **Enter your API key** in Trae and hit **Confirm**
    6. Select **Builder with MCP** and start testing.
  </Tab>

  <Tab title="Cursor">
    <Warning>
      **Important:** Cursor's default "Run in Sandbox" mode limits TestSprite's functionality. See [Cursor Sandbox Mode Configuration](#cursor-sandbox-mode-configuration) below for setup instructions.
    </Warning>

    You can install TestSprite MCP Server in Cursor using either **one-click installation** for quick setup or **manual installation** for full control.

    <Tabs>
      <Tab title="One-click Installation">
        The easiest way to install TestSprite MCP Server in Cursor:

        1. Get your [**API key**](#get-your-api-key).
        2. Click this [one-click install link  <Icon icon="arrow-up-right-from-square" />](cursor://anysphere.cursor-deeplink/mcp/install?name=TestSprite\&config=eyJjb21tYW5kIjoibnB4IEB0ZXN0c3ByaXRlL3Rlc3RzcHJpdGUtbWNwQGxhdGVzdCIsImVudiI6eyJBUElfS0VZIjoiIn19).
        3. **Enter your API key** in Cursor.
        4. Start testing.
      </Tab>

      <Tab title="Manual Installation">
        1. Open Cursor Settings ( <Tooltip><kbd>⌘⇧J</kbd></Tooltip> )
        2. Navigate to **Tools & Integration**
        3. Click **Add custom MCP**
        4. **Add** the following configuration:

        ```json icon="code" Cursor Configuration theme={null}
        {
          "mcpServers": {
            "TestSprite": {
              "command": "npx",
              "args": ["@testsprite/testsprite-mcp@latest"],
              "env": {
                "API_KEY": "your-api-key"
              }
            }
          }
        }
        ```
      </Tab>
    </Tabs>

    5. Check if the green dot shows up on the TestSprite MCP server icon, and the tools have been loaded successfully.

    <Frame>
      <img alt="Cursor Success" />
    </Frame>

    <br />

    <Accordion title="Cursor Sandbox Mode Configuration">
      Cursor Sandbox Mode Configuration
      Cursor has recently updated and by default will run MCP tools in the allowlist in “Run in Sandbox” mode. This mode limits the MCP tools’ functionalities and will prevent successful invocations of TestSprite’s testing procedures.

      To ensure full functionality of TestSprite MCP Server in Cursor:

      1. Go to `Cursor` → `Settings` → `Cursor Settings`

      <Frame>
        <img alt="config" />
      </Frame>

      2. Go to `Chat` → `Auto-Run` → `Auto-Run Mode` and change the setting to **"Ask Everytime"** or **"Run Everything"**

      <Frame>
        <img alt="config" />
      </Frame>
    </Accordion>
  </Tab>

  <Tab title="Claude Code">
    1. **Navigate to your project directory** in terminal:
       ```bash theme={null}
       cd /path/to/your/project
       ```

    2. **Paste the installation command into your terminal**:
       ```bash theme={null}
       claude mcp add TestSprite --env API_KEY=your_api_key -- npx @testsprite/testsprite-mcp@latest
       ```

    3. **Replace `your_api_key`** with your actual TestSprite API key

    4. **Run** the installation command

    5. **Verify the installation** by running this command in your project directory:

       ```bash theme={null}
       claude mcp list
       ```

       You should see:

       ```json Example Terminal Output theme={null}
       TestSprite: npx @testsprite/testsprite-mcp@latest - ✓ Connected
       ```

       <Warning>Installing the MCP server this way adds TestSprite only to Claude Code under the **current project directory**. If you're using Claude Code in another project directory, you'll need to add the MCP server again. For installing the MCP server under different scopes (e.g. global), refer to the [Claude Code MCP documentation <Icon icon="arrow-up-right-from-square" />](https://docs.anthropic.com/en/docs/claude-code/mcp)</Warning>
  </Tab>

  <Tab title="Antigravity">
    1. **Open** the MCP store via the `...` dropdown at the top of the editor's agent panel.
    2. **Click** on **"Manage MCP Servers"**.
    3. **Click** on **"View raw config"**.
    4. **Add** the following configuration to `mcp_config.json`:

       ```json icon="code" Antigravity Configuration theme={null}
       {
         "mcpServers": {
           "TestSprite": {
             "command": "npx",
             "args": ["@testsprite/testsprite-mcp@latest"],
             "env": {
               "API_KEY": "your-api-key"
             }
           }
         }
       }
       ```
  </Tab>

  <Tab title="VSCode">
    1. **Open** the Command Palette ( <Tooltip><kbd>⌘⇧P</kbd></Tooltip> )
    2. **Run** the **MCP: Add Server** command
    3. **Choose** Command (stdio) installation type
    4. **Type** `npx @testsprite/testsprite-mcp@latest` for Command to run
    5. **Type** TestSprite for the MCP server identifier/name
    6. **Choose** the scope where you want the MCP server to be configured
    7. **Add** the `env` configuration:

    ```json icon="code" VS Code Configuration theme={null}
    {
      "mcpServers": {
        "TestSprite": {
          "command": "npx",
          "args": ["@testsprite/testsprite-mcp@latest"],
          "env": {
            "API_KEY": "your-api-key"
          }
        }
      }
    }
    ```

    8. After installation, click the `start` button above the TestSprite MCP entry in the `mcp.json` file you have just configured. If the server started with no errors and all the tools have been loaded, you have installed the MCP server successfully.
  </Tab>

  <Tab title="Other IDEs">
    Add this configuration to your MCP settings:

    ```json icon="code" Other IDE Configuration theme={null}
    {
      "mcpServers": {
        "TestSprite": {
          "command": "npx",
          "args": ["@testsprite/testsprite-mcp@latest"],
          "env": {
            "API_KEY": "your-api-key"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Installation Verification

### Success Indicators

* Your AI assistant can see **TestSprite MCP tools**
* No **"command not found"** errors
* Ready to start testing your projects

### Quick Test

Try prompting:

```json icon="file-lines" theme={null}
Help me test this project with TestSprite.
```

Your assistant should offer to use TestSprite MCP tools.

## Uninstallation

To remove TestSprite MCP Server:

1. **Remove the configuration** from your IDE's MCP settings
2. **Restart your IDE**


# Introduction
Source: https://docs.testsprite.com/mcp/getting-started/introduction

Get started with TestSprite MCP Server

<Frame>
  <iframe />
</Frame>

TestSprite is the easiest AI software testing agent for fully autonomous testing.
Our no-code AI completes testing cycles in **10-20** minutes, so you can ship with confidence without manual QA work.

TestSprite MCP Server is a
<Tooltip href="https://modelcontextprotocol.io/">Model Context Protocol</Tooltip>
integration that lets your IDE’s AI assistant orchestrate the entire TestSprite workflow directly from your editor.

<Columns>
  <Card title="Overview" icon="rectangle-list" href="overview">
    Learn what TestSprite MCP Server can do
  </Card>

  <Card title="Install MCP Server" icon="download" href="installation">
    Get TestSprite MCP Server up and running
  </Card>

  <Card title="Run First MCP Test" icon="play" href="first-test">
    Complete your first automated test in 10 minutes
  </Card>

  <Card title="Testing Workflow" icon="route" href="../concepts/workflow">
    Understand the complete testing workflow
  </Card>

  <Card title="Manage API Keys" icon="key" href="../../web-portal/admin/api-keys">
    Create and manage your TestSprite API keys
  </Card>

  <Card title="Join Community" icon="comments" href="https://discord.com/invite/QQB9tJ973e">
    Connect with other users
  </Card>
</Columns>


# Overview
Source: https://docs.testsprite.com/mcp/getting-started/overview

The No-Code, No-Prompt Testing Agent That Makes Your Software Work

## What is TestSprite MCP Server?

TestSprite MCP Server is a
<Tooltip href="https://modelcontextprotocol.io/">Model Context Protocol</Tooltip>
integration that connects your IDE's AI assistant (like Cursor or Windsurf) with TestSprite's intelligent testing engine. It enables **fully automated testing workflows** directly within your development environment.

<Frame>
  <img alt="mcp flow" />
</Frame>

## How It Works

After installing TestSprite MCP in your IDE, you can use simple **natural language prompts** to let our AI testing agent handle the entire testing workflow for you.

<Frame>
  <img alt="mcp intro" />
</Frame>

Just use the following prompt, drag your project folder into the chat, or describe your testing requirements. TestSprite MCP Server handles the rest.

```text icon="file-lines" theme={null}
Help me test this project with TestSprite.
```

<Accordion title="How TestSprite Works in 8 Simple Steps">
  <Steps>
    <Step title="Reads User PRD">
      Understands your product requirements and goals.
    </Step>

    <Step title="Analyzes Your Code">
      Scans project structure, features, and implementation.
    </Step>

    <Step title="Generates TestSprite PRD">
      Creates normalized product requirements document.
    </Step>

    <Step title="Creates Test Plans">
      Generates comprehensive test cases based on PRD and code.
    </Step>

    <Step title="Generates Test Code">
      Creates executable test scripts (Playwright, Cypress, etc.).
    </Step>

    <Step title="Executes Tests">
      Runs tests in secure cloud environments.
    </Step>

    <Step title="Provides Results">
      Delivers detailed reports with actionable insights.
    </Step>

    <Step title="Enables Fixes">
      IDE uses our analysis to automatically patch issues.
    </Step>
  </Steps>
</Accordion>

## Key Benefits

Depending on your role, TestSprite MCP Server delivers different advantages:

* **For Developers:** Ship faster with **zero test writing**, get **feedback in minutes** (not hours), and **fix issues automatically** with AI-powered analysis—all **without leaving your IDE**.

* **For Teams:** Achieve **predictable quality** and **faster releases** with **broad, consistent coverage**—including edge cases—while reducing manual QA effort and test maintenance overhead.

## What Makes It Different

TestSprite MCP Server transforms the testing experience by automating what traditionally requires manual effort. Here's how it compares to traditional testing approaches:

<Frame>
  <img alt="result" />
</Frame>

| Features                      | Traditional Testing                                  | TestSprite MCP Server                     |
| :---------------------------- | :--------------------------------------------------- | :---------------------------------------- |
| <kbd>Test case creation</kbd> | Writing test cases manually                          | **AI generates test cases automatically** |
| <kbd>Setup</kbd>              | Setting up complex frameworks                        | Almost **zero setup required**            |
| <kbd>Debugging</kbd>          | Debugging failures by hand                           | **Analyzes and fixes issues** for you     |
| <kbd>Integration</kbd>        | Running tests separately from development            | **Integrated into your coding workflow**  |
| <kbd>Coverage</kbd>           | **Limited coverage** that misses critical edge cases | **Comprehensive automated coverage**      |

## Testing Capabilities

TestSprite MCP Server supports comprehensive testing for both frontend and backend applications, from UI flows to API integrations and security validation.

<Tabs>
  <Tab title="Frontend Testing (Business-Flow E2E)">
    * User Journey Navigation
    * Form Flows & Validation
    * Visual States & Layouts
    * Interactive Components & Stateful UI
    * Authorization & Auth Flows
    * Error Handling (UI)
  </Tab>

  <Tab title="Backend Testing (API & Integration)">
    * Functional API Workflows
    * Contract & Schema Validation
    * Error Handling & Resilience
    * Authorization & Authentication
    * Boundary & Edge Cases
    * Data Integrity & Persistence
    * Security Testing
  </Tab>
</Tabs>

## Supported Technologies

<Tabs>
  <Tab title="Frontend Frameworks" icon="code">
    <Columns>
      <Card title="React">
        <div>
          <img alt="React" />
        </div>
      </Card>

      <Card title="Vue">
        <div>
          <img alt="Vue" />
        </div>
      </Card>

      <Card title="Angular">
        <div>
          <img alt="Angular" />
        </div>
      </Card>

      <Card title="Svelte">
        <div>
          <img alt="Svelte" />
        </div>
      </Card>

      <Card title="Next.js">
        <div>
          <img alt="Next.js" />
        </div>
      </Card>

      <Card title="Vite">
        <div>
          <img alt="Vite" />
        </div>
      </Card>

      <Card title="Vanilla JavaScript/TypeScript">
        <div>
          <img alt="Vanilla JS/TS" />
        </div>
      </Card>
    </Columns>
  </Tab>

  <Tab title="Backend Technologies" icon="server">
    <Columns>
      <Card title="Node.js">
        <div>
          <img alt="Node.js" />
        </div>
      </Card>

      <Card title="Python">
        <div>
          <img alt="Python" />
        </div>
      </Card>

      <Card title="Java">
        <div>
          <img alt="Java" />
        </div>
      </Card>

      <Card title="Go">
        <div>
          <img alt="Go" />
        </div>
      </Card>

      <Card title="Express.js">
        <div>
          <img alt="Express.js" />
        </div>
      </Card>

      <Card title="FastAPI">
        <div>
          <img alt="FastAPI" />
        </div>
      </Card>

      <Card title="Spring Boot">
        <div>
          <img alt="Spring Boot" />
        </div>
      </Card>

      <Card title="REST APIs">
        <div>
          <img alt="REST APIs" />
        </div>
      </Card>

      <Card title="GraphQL">
        <div>
          <img alt="GraphQL" />
        </div>
      </Card>
    </Columns>
  </Tab>
</Tabs>

## Real Results

TestSprite MCP Server delivers measurable improvements:

* **90%+ Code Quality** - Achieve professional-grade code quality
* **10x Faster Testing** - From hours to minutes
* **Zero Learning Curve** - No testing expertise required
* **Automatic Bug Fixes** - AI patches issues automatically


# GitHub Integration
Source: https://docs.testsprite.com/mcp/integrations/github-integration

Connect your GitHub repositories to TestSprite for automatic testing on every pull request.

<Frame>
  <img alt="config" />
</Frame>

## How It Works

Once connected, the TestSprite GitHub App:

1. Detects new pull requests on your connected repository
2. Waits for your deployment platform (Vercel, Netlify, etc.) to deploy a preview
3. Automatically runs your TestSprite tests against the preview URL
4. Posts a comment on the PR with a detailed test results summary

## Prerequisites

<Warning>
  **TestSprite MCP Server is required first.** The GitHub integration only **runs** tests — it does not generate them. You must use the [TestSprite MCP Server](/mcp/getting-started/introduction) to generate your test suite before setting up this integration.
</Warning>

### Generate Tests with MCP Server

The TestSprite MCP Server is responsible for generating, executing, and refining your test cases locally. Once your tests are committed to your repository, the GitHub App can run them automatically on every PR.

<Frame>
  <img alt="config" />
</Frame>

<Steps>
  <Step title="Install MCP Server">
    Follow the [MCP Installation Guide](/mcp/getting-started/installation) to set up the TestSprite MCP Server in your IDE.
  </Step>

  <Step title="Generate Tests">
    Use the MCP tools to generate test plans and test code for your project. See [First MCP Test](/mcp/getting-started/first-test) for a step-by-step walkthrough.
  </Step>

  <Step title="Commit Tests to Your Repository">
    Ensure the generated `testsprite_tests/` folder and test files are committed and included in your repository. The GitHub App will use these tests during CI/CD runs.
  </Step>
</Steps>

### Other Requirements

* A **GitHub repository** for your project
* A **deployment platform** connected to your repo (e.g., Vercel, Netlify, Render, Railway, or Fly.io) that auto-deploys on PRs

## Github App vs. Github Action

<Tip>
  The GitHub App provides the simplest setup with automatic deployment detection — no workflow files needed.
</Tip>

<CardGroup>
  <Card title="GitHub App (Recommended)" icon="github">
    Best for teams using **Vercel, Netlify, Render**, or other managed platforms.

    * **Setup:** Connect in a few clicks via Web Portal
    * **Workflow files:** None required
    * **Deploys:** Auto-detects platform deployments
    * **Config:** Managed in TestSprite Web Portal
  </Card>

  <Card title="GitHub Action" icon="square-github">
    Best for teams with **custom CI/CD pipelines** who need full control.

    * **Setup:** Requires YAML config and repo secrets
    * **Workflow files:** `.github/workflows/ci.yml`
    * **Deploys:** Manual deploy step in workflow
    * **Config:** Defined in repository workflow files
  </Card>
</CardGroup>

## Setup GitHub Integration

<Tabs>
  <Tab title="Github App" icon="Github">
    The TestSprite GitHub App provides a streamlined, no-config integration that automatically detects deployments and runs tests on every pull request. Unlike the <kbd>GitHub Action</kbd> approach, the GitHub App requires no workflow YAML files — just connect your repository through the TestSprite Web Portal.

    <Steps>
      <Step title="Connect Your Deployment Platform">
        Connect your repository to a deployment platform that supports automatic preview deployments on pull requests. Supported platforms include:

        <CardGroup>
          <Card title="Vercel" href="https://vercel.com">
            <div>
              <img alt="Vercel" />
            </div>
          </Card>

          <Card title="Netlify" href="https://netlify.com">
            <div>
              <img alt="Netlify" />
            </div>
          </Card>

          <Card title="Render" href="https://render.com">
            <div>
              <img alt="Render" />
            </div>
          </Card>

          <Card title="Fly.io" href="https://fly.io">
            <div>
              <img alt="Fly.io" />
            </div>
          </Card>
        </CardGroup>

        These platforms provide a <kbd>Connect Repo</kbd> button that links your GitHub repository and automatically deploys a preview on every PR.

        <Frame>
          <img alt="config" />
        </Frame>

        <Tip>
          As long as the deployment platform posts a deployment status on the PR (e.g., the Vercel bot comment), TestSprite can detect it and use the preview URL for testing.
        </Tip>
      </Step>

      <Step title="Connect GitHub in TestSprite Web Portal">
        <Frame>
          <img alt="config" />
        </Frame>

        1. Log in to the [TestSprite Web Portal](https://www.testsprite.com)
        2. Navigate to <kbd>GitHub App</kbd> in the sidebar under Settings
        3. Click <kbd>Connect With GitHub App</kbd>
        4. Authorize TestSprite to access your GitHub organization
        5. Select the repositories you want to connect

        Once authorized, you will see your connected organization displayed on the GitHub App settings page.
      </Step>

      <Step title="Configure Repository Settings">
        After connecting your organization, configure the integration for each repository:

        1. Select a **Connected Repository** from the dropdown

        <Frame>
          <img alt="config" />
        </Frame>

        2. Configure the **Pull Request Settings**:

        <Frame>
          <img alt="config" />
        </Frame>

        | Setting                      | Description                                                 |
        | ---------------------------- | ----------------------------------------------------------- |
        | <kbd>Run on PRs</kbd>        | Automatically run tests when PRs are created or updated     |
        | <kbd>Include Draft PRs</kbd> | Run tests on draft pull requests in addition to regular PRs |
        | <kbd>Blocking PR</kbd>       | Block the PR from merging when tests fail                   |

        3. Click **Save Changes** to apply your configuration

        <Frame>
          <img alt="config" />
        </Frame>
      </Step>

      <Step title="Managing Connection">
        You can manage your GitHub App connections from the **GitHub App** settings page in the TestSprite Web Portal.

        <Frame>
          <img alt="config" />
        </Frame>

        | Action                      | Description                                                 |
        | --------------------------- | ----------------------------------------------------------- |
        | <kbd>Add Connection</kbd>   | Connect additional repositories from your organization      |
        | <kbd>Remove</kbd>           | Disconnect a repository from TestSprite                     |
        | <kbd>Manage in GitHub</kbd> | Open GitHub to manage app permissions and repository access |
      </Step>
    </Steps>
  </Tab>

  <Tab title="Github Action" icon="square-github">
    Integrate TestSprite into your CI/CD pipeline by adding a GitHub Actions workflow to your repository. Every time a pull request is created or updated, TestSprite automatically runs your tests against a preview deployment and reports results directly on the PR.

    <Steps>
      <Step title="Set Up Project Deployment">
        Configure a preview deployment so TestSprite can test against a live URL on each PR. Here are some example setups you can use to deploy your app:

        <Tabs>
          <Tab title="Vercel">
            Deploy preview builds to Vercel using the Vercel CLI inside GitHub Actions. You'll need to link your project locally with `vercel link`, then store the generated credentials as GitHub secrets.

            **Secrets required:**

            | Secret              | Description                                                                     |
            | ------------------- | ------------------------------------------------------------------------------- |
            | `VERCEL_TOKEN`      | Generate from your [Vercel account settings](https://vercel.com/account/tokens) |
            | `VERCEL_ORG_ID`     | Found in `.vercel/project.json` after running `vercel link`                     |
            | `VERCEL_PROJECT_ID` | Found in `.vercel/project.json` after running `vercel link`                     |

            ```yaml Expandable deploy.yml theme={null}
            name: Vercel Preview Deployment
            env:
              VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
              VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: Install Vercel CLI
                    run: npm install --global vercel@latest
                  - name: Pull Vercel Environment Information
                    run: vercel pull --yes --environment=preview --token=${{ secrets.VERCEL_TOKEN }}
                  - name: Build Project Artifacts
                    run: vercel build --token=${{ secrets.VERCEL_TOKEN }}
                  - name: Deploy to Vercel
                    id: deploy
                    run: echo "url=$(vercel deploy --prebuilt --token=${{ secrets.VERCEL_TOKEN }})" >> $GITHUB_OUTPUT
                outputs:
                  url: ${{ steps.deploy.outputs.url }}
            ```

            <Accordion title="Additional Resources">
              <CardGroup>
                <Card title="GitHub Actions with Vercel" icon="book" href="https://vercel.com/kb/guide/how-can-i-use-github-actions-with-vercel">
                  Official Vercel guide for CI/CD with GitHub Actions
                </Card>

                <Card title="Vercel CLI Reference" icon="terminal" href="https://vercel.com/docs/cli">
                  Full Vercel CLI documentation
                </Card>
              </CardGroup>
            </Accordion>
          </Tab>

          <Tab title="Render">
            Trigger a Render deploy from GitHub Actions using the community `render-deploy` action. This calls the Render API to deploy your service and optionally waits for it to finish.

            **Secrets required:**

            | Secret              | Description                                                                                    |
            | ------------------- | ---------------------------------------------------------------------------------------------- |
            | `RENDER_API_KEY`    | Generate from your [Render account settings](https://dashboard.render.com/u/settings#api-keys) |
            | `RENDER_SERVICE_ID` | Found on your service's settings page in the Render dashboard                                  |

            ```yaml Expandable deploy.yml theme={null}
            name: Render Preview Deployment
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                steps:
                  - uses: JorgeLNJunior/render-deploy@v1.5.0
                    id: deploy
                    with:
                      service_id: ${{ secrets.RENDER_SERVICE_ID }}
                      api_key: ${{ secrets.RENDER_API_KEY }}
                      wait_deploy: true
            ```

            <Accordion title="Additional Resources">
              <CardGroup>
                <Card title="Deploy to Render (Action)" icon="github" href="https://github.com/marketplace/actions/deploy-to-render">
                  Community GitHub Action for Render deployments
                </Card>

                <Card title="Render Deploy Hooks" icon="book" href="https://docs.render.com/deploy-hooks">
                  Official Render deploy hooks documentation
                </Card>
              </CardGroup>
            </Accordion>
          </Tab>

          <Tab title="Railway">
            Deploy preview environments on Railway for every pull request using the community `railway-preview-deploy` action. Each PR gets its own isolated environment with a unique URL.

            **Secrets required:**

            | Secret               | Description                                         |
            | -------------------- | --------------------------------------------------- |
            | `RAILWAY_API_TOKEN`  | Generate from your Railway account settings         |
            | `RAILWAY_PROJECT_ID` | Found in Railway dashboard under Settings > General |

            ```yaml Expandable deploy.yml theme={null}
            name: Railway Preview Deployment
            on:
              pull_request:
                types: [opened, synchronize, reopened, closed]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                if: ${{ github.event.action != 'closed' }}
                steps:
                  - uses: actions/checkout@v4
                  - name: Deploy to Railway
                    id: deploy
                    uses: ayungavis/railway-preview-deploy@v1.0.2
                    with:
                      railway_api_token: ${{ secrets.RAILWAY_API_TOKEN }}
                      project_id: ${{ secrets.RAILWAY_PROJECT_ID }}
                      environment_name: 'staging'
                      preview_environment_name: 'pr-${{ github.event.pull_request.number }}'
                      branch_name: ${{ github.head_ref }}
                outputs:
                  url: ${{ steps.deploy.outputs.service_domain }}
              cleanup:
                runs-on: ubuntu-latest
                if: ${{ github.event.action == 'closed' }}
                steps:
                  - uses: actions/checkout@v4
                  - uses: ayungavis/railway-preview-deploy@v1.0.2
                    with:
                      railway_api_token: ${{ secrets.RAILWAY_API_TOKEN }}
                      project_id: ${{ secrets.RAILWAY_PROJECT_ID }}
                      environment_name: 'staging'
                      preview_environment_name: 'pr-${{ github.event.pull_request.number }}'
                      branch_name: ${{ github.head_ref }}
                      cleanup: 'true'
            ```

            <Accordion title="Additional Resources">
              <CardGroup>
                <Card title="Railway Preview Deploy Action" icon="github" href="https://github.com/marketplace/actions/railway-preview-deploy-action">
                  Community GitHub Action for Railway preview environments
                </Card>

                <Card title="GitHub Actions with Railway" icon="book" href="https://blog.railway.com/p/github-actions">
                  Official Railway blog guide for CI/CD with GitHub Actions
                </Card>
              </CardGroup>
            </Accordion>
          </Tab>

          <Tab title="Netlify">
            Deploy preview builds to Netlify using the community `action-netlify-deploy` action. Each PR gets a unique preview URL that you can use for testing.

            **Secrets required:**

            | Secret               | Description                                                                                                      |
            | -------------------- | ---------------------------------------------------------------------------------------------------------------- |
            | `NETLIFY_AUTH_TOKEN` | Generate from [Netlify personal access tokens](https://app.netlify.com/user/applications#personal-access-tokens) |
            | `NETLIFY_SITE_ID`    | Found in your Netlify site settings under API ID                                                                 |

            ```yaml Expandable deploy.yml theme={null}
            name: Netlify Preview Deployment
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - uses: jsmrcaga/action-netlify-deploy@v2.0.0
                    with:
                      NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
                      NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
            ```

            The action outputs `NETLIFY_PREVIEW_URL` as an environment variable for use in subsequent steps.

            <Accordion title="Additional Resources">
              <CardGroup>
                <Card title="Netlify Deploy Action" icon="github" href="https://github.com/marketplace/actions/netlify-deploy">
                  Community GitHub Action for Netlify deployments
                </Card>

                <Card title="Netlify CLI Documentation" icon="book" href="https://docs.netlify.com/cli/get-started/">
                  Official Netlify CLI for manual deploy workflows
                </Card>
              </CardGroup>
            </Accordion>
          </Tab>

          <Tab title="Fly.io">
            Deploy to Fly.io using the official `flyctl-actions` action from Superfly. The workflow installs `flyctl` and runs `flyctl deploy` against your `fly.toml` configuration.

            **Secrets required:**

            | Secret          | Description                                                       |
            | --------------- | ----------------------------------------------------------------- |
            | `FLY_API_TOKEN` | Generate by running `fly tokens create deploy -x 999999h` locally |

            ```yaml Expandable deploy.yml theme={null}
            name: Fly.io Preview Deployment
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                concurrency: deploy-group
                steps:
                  - uses: actions/checkout@v4
                  - uses: superfly/flyctl-actions/setup-flyctl@master
                  - name: Deploy to Fly.io
                    id: deploy
                    run: flyctl deploy --remote-only
                    env:
                      FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
            ```

            Make sure your `fly.toml` is committed to the repository for the action to reference during deployment.

            <Accordion title="Additional Resources">
              <CardGroup>
                <Card title="Continuous Deployment with GitHub Actions" icon="book" href="https://fly.io/docs/launch/continuous-deployment-with-github-actions/">
                  Official Fly.io guide for CI/CD with GitHub Actions
                </Card>

                <Card title="GitHub Action for flyctl" icon="github" href="https://github.com/marketplace/actions/github-action-for-flyctl">
                  Official flyctl GitHub Action
                </Card>
              </CardGroup>
            </Accordion>
          </Tab>
        </Tabs>
      </Step>

      <Step title="Generate a TestSprite API Key">
        <Frame>
          <img alt="API Key" />
        </Frame>

        1. Log in to the [TestSprite Web Portal](https://www.testsprite.com/dashboard)
        2. Navigate to <kbd>API Keys</kbd> in the sidebar
        3. Click <kbd> New API Key</kbd> and copy the generated key
        4. Add it as a repository secret named `TESTSPRITE_API_KEY` in your repo <kbd>Settings</kbd> → <kbd>Secrets and variables</kbd> → <kbd>Actions</kbd>
      </Step>

      <Step title="Add the GitHub Actions Workflow">
        Create the file `.github/workflows/ci.yml` in your repository with the following configuration:

        <CodeGroup>
          ```yaml Expandable ci.yml theme={null}
          name: TestSprite CI

          on:
            pull_request:
              types: [opened, synchronize, reopened]

          jobs:
            test:
              needs: deploy
              runs-on: ubuntu-latest
              steps:
                - name: Checkout
                  id: checkout
                  uses: actions/checkout@v4

                - name: TestSprite Action
                  id: testsprite
                  uses: TestSprite/run-action@v1
                  with:
                    testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                    base_url: ${{ needs.deploy.outputs.url }}
                    blocking: 'true'
          ```
        </CodeGroup>

        <Warning>
          If you set `blocking: 'true'`, the GitHub Action will fail when tests do not pass, which can block PR merges if you have branch protection rules enabled.
        </Warning>

        <Accordion title="Complete workflow examples by platform">
          Full `ci.yml` examples that combine deployment and TestSprite testing in a single workflow.

          <CodeGroup>
            ```yaml Vercel theme={null}
            name: TestSprite CI
            env:
              VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
              VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                outputs:
                  url: ${{ steps.deploy.outputs.url }}
                steps:
                  - uses: actions/checkout@v4
                  - name: Install Vercel CLI
                    run: npm install --global vercel@latest
                  - name: Pull Vercel Environment Information
                    run: vercel pull --yes --environment=preview --token=${{ secrets.VERCEL_TOKEN }}
                  - name: Build Project Artifacts
                    run: vercel build --token=${{ secrets.VERCEL_TOKEN }}
                  - name: Deploy to Vercel
                    id: deploy
                    run: echo "url=$(vercel deploy --prebuilt --token=${{ secrets.VERCEL_TOKEN }})" >> $GITHUB_OUTPUT
              test:
                needs: deploy
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: TestSprite Action
                    uses: TestSprite/run-action@v1
                    with:
                      testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                      base_url: ${{ needs.deploy.outputs.url }}
                      blocking: 'true'
            ```

            ```yaml Render theme={null}
            name: TestSprite CI
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                steps:
                  - uses: JorgeLNJunior/render-deploy@v1.5.0
                    id: deploy
                    with:
                      service_id: ${{ secrets.RENDER_SERVICE_ID }}
                      api_key: ${{ secrets.RENDER_API_KEY }}
                      wait_deploy: true
              test:
                needs: deploy
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: TestSprite Action
                    uses: TestSprite/run-action@v1
                    with:
                      testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                      base_url: # Your Render service URL
                      blocking: 'true'
            ```

            ```yaml Railway theme={null}
            name: TestSprite CI
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                outputs:
                  url: ${{ steps.deploy.outputs.service_domain }}
                steps:
                  - uses: actions/checkout@v4
                  - name: Deploy to Railway
                    id: deploy
                    uses: ayungavis/railway-preview-deploy@v1.0.2
                    with:
                      railway_api_token: ${{ secrets.RAILWAY_API_TOKEN }}
                      project_id: ${{ secrets.RAILWAY_PROJECT_ID }}
                      environment_name: 'staging'
                      preview_environment_name: 'pr-${{ github.event.pull_request.number }}'
                      branch_name: ${{ github.head_ref }}
              test:
                needs: deploy
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: TestSprite Action
                    uses: TestSprite/run-action@v1
                    with:
                      testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                      base_url: ${{ needs.deploy.outputs.url }}
                      blocking: 'true'
            ```

            ```yaml Netlify theme={null}
            name: TestSprite CI
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                outputs:
                  url: ${{ steps.deploy.outputs.NETLIFY_PREVIEW_URL }}
                steps:
                  - uses: actions/checkout@v4
                  - uses: jsmrcaga/action-netlify-deploy@v2.0.0
                    id: deploy
                    with:
                      NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
                      NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
              test:
                needs: deploy
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: TestSprite Action
                    uses: TestSprite/run-action@v1
                    with:
                      testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                      base_url: ${{ needs.deploy.outputs.url }}
                      blocking: 'true'
            ```

            ```yaml Fly.io theme={null}
            name: TestSprite CI
            on:
              pull_request:
                types: [opened, synchronize, reopened]
            jobs:
              deploy:
                runs-on: ubuntu-latest
                concurrency: deploy-group
                steps:
                  - uses: actions/checkout@v4
                  - uses: superfly/flyctl-actions/setup-flyctl@master
                  - name: Deploy to Fly.io
                    run: flyctl deploy --remote-only
                    env:
                      FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
              test:
                needs: deploy
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - name: TestSprite Action
                    uses: TestSprite/run-action@v1
                    with:
                      testsprite-api-key: ${{ secrets.TESTSPRITE_API_KEY }}
                      base_url: # Your Fly.io app URL
                      blocking: 'true'
            ```
          </CodeGroup>
        </Accordion>
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Create a Pull Request

<Frame>
  <img alt="config" />
</Frame>

Create a pull request on your connected repository. The following will happen automatically:

1. Your deployment platform deploys a preview of the PR
2. TestSprite detects the deployment and starts running tests
3. The **TestSprite bot** posts a comment on the PR with test results

The comment includes a summary table with each test case and its pass/fail status, plus a link to the detailed TestSprite results page.

<Info>
  Both methods produce the same test result comments on your pull requests. Choose the approach that best fits your team's workflow.
</Info>

## Next Steps

<Columns>
  <Card title="Test Maintenance" icon="plug" href="/mcp/maintenance/test-maintenance">
    Learn how to maintain and update your test suites over time.
  </Card>

  <Card title="Manage API Keys" icon="key" href="/web-portal/admin/api-keys">
    Create and manage your TestSprite API keys
  </Card>
</Columns>


# Cost & Performance
Source: https://docs.testsprite.com/mcp/maintenance/cost-performance

Understand cost and performance considerations when using TestSprite.

## Goals

Keep feedback fast and costs predictable while maintaining strong coverage.

## Cost Controls

* **Scope smartly**: Use `testScope: "diff"` for day-to-day iteration; target subsets with `testIds` for quick loops
* **Run frequency**: Schedule nightly full runs; run diffs on PRs; use `rerun` to validate fixes without re-planning
* **Reports-first**: Review reports to avoid unnecessary re-executions
* **Artifact retention**: Retain only what you need (screenshots/videos) for CI retention windows

## Performance Tips

* **Local readiness**: Ensure apps start quickly and are reachable on the specified `localPort`; pre-warm test data or seed databases for faster setup
* **Selector stability**: Prefer role/label-based selectors to reduce retries and timeouts
* **Parallelization**: Keep tests independent for parallel execution in CI
* **Deterministic data**: Use stable fixtures to avoid slow flaky retries

## Suggested Defaults

* **PRs**: diff scope, targeted `testIds` on critical changes
* **Main branch**: daily full run, artifact retention 7 days
* **Hotfixes**: focused reruns on impacted suites

## Useful Flows

Common code patterns for efficient test execution and cost optimization. Use these flows to target specific changes, run subsets, and quickly validate fixes without full regeneration.

<CodeGroup>
  ```javascript Diff-only execution theme={null}
  testsprite_bootstrap_tests({ testScope: "diff", ... })
  ```

  ```javascript Subset during iteration theme={null}
  testsprite_generate_code_and_execute({ testIds: ["TC005", "TC010"] })
  ```

  ```javascript Rerun without re-planning theme={null}
  testsprite_rerun_tests({ projectPath: "/abs/path" })
  ```
</CodeGroup>

## Related

<Columns>
  <Card title="Test Running & Monitoring" href="/mcp/core/continuous-monitoring">
    Learn about continuous monitoring and test execution
  </Card>

  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Learn how to modify and update existing tests
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Reference guide for MCP tools and commands
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Understand automatic healing and test observability
  </Card>
</Columns>


# Import Existing Tests
Source: https://docs.testsprite.com/mcp/maintenance/migration-from-other-platforms

Migrate your existing tests from other testing platforms to TestSprite.

## The Simple Path

Already have tests (e.g., Playwright, Cypress, Jest, Postman collections)? You don’t need to rewrite them.

<Steps>
  <Step title="Add to Test Plan">
    Include your existing tests in the TestSprite test plan alongside generated ones
    <Info>Keep the same IDs/titles where possible for clarity</Info>

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Regenerate Test Code">
    Regenerate the test code to incorporate the imported tests. TestSprite will reference them during code generation and execution

    ```text Example Prompt theme={null}
    Import these UI tests and add them to the TestSprite frontend testing plan, 
    then regenerate the test code and run it.
    ```
  </Step>

  <Step title="Run">
    Execute like any other plan. Results and reports will include both generated and imported tests
  </Step>
</Steps>

## Best Practices

<AccordionGroup>
  <Accordion title="Keep Tests in Repository">
    Keep imported tests in your repo so the runner can access them
  </Accordion>

  <Accordion title="Map Environment Variables">
    If needed, map environment variables/credentials in the TestSprite portal
  </Accordion>

  <Accordion title="Use Consistent Naming">
    Use consistent naming so maintenance is straightforward
  </Accordion>
</AccordionGroup>

## Related

<Columns>
  <Card title="Create Tests for New Projects" href="/mcp/core/create-tests-new-project">
    Learn how to create tests for new projects
  </Card>

  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature">
    Learn how to create tests for new features and changes
  </Card>

  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Learn how to modify and update existing tests
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Reference guide for MCP tools and commands
  </Card>
</Columns>


# Security & Compliance
Source: https://docs.testsprite.com/mcp/maintenance/security-compliance

Learn about TestSprite's security features and compliance standards.

## Principles

* **Least privilege**: only the minimum credentials required for tests
* **Isolation**: sandboxed execution and ephemeral environments for runs
* **Transparency**: human-readable reports and machine-readable logs

## Data Handling

**Credentials**

* Configure API keys and logins in the TestSprite portal; avoid hardcoding in tests
* Support for environment variables and secret injection

**Artifacts**

* Test artifacts (screens/videos/logs) stored under `testsprite_tests/`
* Configure retention in CI to match your policy

**PII/Secrets**

* Mask sensitive values in logs and reports when configured

## Access & Authorization

* **Auth Flows**
  * **Frontend**: gated routes, role-based visibility
  * **Backend**: tokens, scopes, and permissions validated in tests
* Principle of least privilege in test accounts
* Rotate test credentials periodically

## Compliance Alignment

* PRD-driven and plan-based testing provides traceability from requirement to test
* Reports include per-test outcomes for audit readiness
* Supports segregation of duties: TestSprite analyzes, IDE applies fixes with approval

## Best Practices

<AccordionGroup>
  <Accordion title="Store Secrets Securely">
    Store secrets in your secret manager (not the repo)
  </Accordion>

  <Accordion title="Use Dedicated Test Accounts">
    Use dedicated test tenants and accounts
  </Accordion>

  <Accordion title="Review Healing Proposals">
    Review healing proposals before applying to production branches
  </Accordion>

  <Accordion title="Limit Artifact Exposure">
    Limit artifact exposure in public logs; use private CI storage
  </Accordion>
</AccordionGroup>

## Related

<Columns>
  <Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle">
    Understand test types and their lifecycle
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Understand automatic healing and test observability
  </Card>

  <Card title="Test Running & Monitoring" href="/mcp/core/continuous-monitoring">
    Learn about continuous monitoring and test execution
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Reference guide for MCP tools and commands
  </Card>
</Columns>


# Test Maintenance
Source: https://docs.testsprite.com/mcp/maintenance/test-maintenance

Learn how to maintain and update your test suites over time.

## Keep Tests Healthy with Minimal Effort

Most maintenance is already handled via healing and focused regeneration. Use this page as a hub for quick practices and links.

## Essentials

* Prefer regeneration over manual rewrites for broad changes
* Apply auto-healing for selector drift, waits, and fixtures
* Use diff scope to update only impacted tests
* Keep PRD and acceptance criteria current

## Shift Left (TDD with TestSprite)

Generate and run tests while coding—even before features are complete—to reveal gaps early.

<Frame>
  <img alt="diff" />
</Frame>

* Use `testScope: "diff"` to target in-progress changes
* Run small subsets frequently via `testIds`
* Let healing suggestions guide selectors, waits, and data setup from the start

<Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature" icon="square-plus">
  Learn how to create tests for new features and changes
</Card>

## Common Tasks

<Columns>
  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature" icon="square-plus">
    Update changed flows with new tests
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability" icon="bandage">
    Fix failing or flaky tests with automatic healing
  </Card>

  <Card title="Add Extra Tests" href="/mcp/core/add-extra-tests" icon="plus-circle">
    Expand coverage with additional test cases
  </Card>

  <Card title="Test Types & Lifecycle" href="/mcp/concepts/test-type-lifecycle" icon="arrow-rotate-right">
    Understand test types and their lifecycle
  </Card>

  <Card title="Import Existing Tests" href="/mcp/maintenance/migration-from-other-platforms" icon="arrow-down-to-line">
    Migrate existing test suites to TestSprite
  </Card>
</Columns>

<Tip>
  Rerun quickly: `testsprite_rerun_tests({ projectPath: "/abs/path" })`
</Tip>

## Best Practices

<AccordionGroup>
  <Accordion title="Semantic Selectors & Ready States">
    Use semantic selectors and explicit ready states
  </Accordion>

  <Accordion title="Deterministic Test Data">
    Keep deterministic test data and clean state between cases
  </Accordion>

  <Accordion title="Frequent Commits">
    Commit changes frequently so diff-based updates are accurate
  </Accordion>

  <Accordion title="Run Small Subsets">
    Run a small subset (by `testIds`) while iterating
  </Accordion>
</AccordionGroup>

## Where Artifacts Live

<Frame>
  <img alt="delete" />
</Frame>

* Results, PRD, plans, and logs under `testsprite_tests/`
* Reports: Markdown/HTML plus machine-readable JSON for automation

## Related

<Columns>
  <Card title="Create Tests for New Projects" href="/mcp/core/create-tests-new-project">
    Learn how to create tests for new projects
  </Card>

  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Learn how to modify and update existing tests
  </Card>

  <Card title="MCP Testing Workflow" href="/mcp/concepts/workflow">
    Understand the MCP testing workflow
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Reference guide for MCP tools and commands
  </Card>
</Columns>


# Application Detection Issues
Source: https://docs.testsprite.com/mcp/troubleshooting/application-detection-issues

Solutions to application detection problems with TestSprite MCP Server.

## "Application not accessible" Error

If you experience issues where **TestSprite can't access your running application**, please follow the solution below:

<Steps>
  <Step title="Diagnostic checks">
    Check if application is running

    ```bash theme={null}
    curl http://localhost:3000
    curl http://localhost:8000
    ```

    Check which ports are in use

    ```bash theme={null}
    lsof -i :3000
    lsof -i :8000
    ```

    Check firewall settings (Linux)

    ```bash theme={null}
    sudo ufw status
    ```

    <Info>**For macOS:** Go to System `Preferences > Security & Privacy > Firewall` to check firewall settings.</Info>
  </Step>

  <Step title="Ensure application is running">
    <Tabs>
      <Tab title="Frontend Applications">
        ```bash theme={null}
        npm start
        npm run dev
        yarn dev
        ```
      </Tab>

      <Tab title="Backend Applications">
        ```bash theme={null}
        npm run server
        python app.py
        node server.js
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Check port configuration">
    Find actual port

    ```bash theme={null}
    netstat -tulpn | grep LISTEN
    ```

    Update bootstrap call

    ```bash theme={null}
    testsprite_bootstrap_tests ({
      localPort: 3000,  // Use actual port
      type: "frontend",
      projectPath: "/path/to/project",
      testScope: "codebase"
    })
    ```
  </Step>

  <Step title="Check for port conflicts">
    Kill conflicting processes

    ```bash theme={null}
    lsof -ti:3000 | xargs kill -9
    ```

    Use different port

    ```bash theme={null}
    PORT=3001 npm start
    ```
  </Step>
</Steps>


# IDE Configuration Issues
Source: https://docs.testsprite.com/mcp/troubleshooting/ide-configuration-issues

Solutions to IDE configuration problems with TestSprite MCP Server.

## MCP Server Not Detected in IDE

If you experience issues where your **IDE doesn't recognize TestSprite MCP Server**, please follow the solution below:

<Steps>
  <Step title="Verify JSON Configuration">
    <Tabs>
      <Tab title="macOS/Linux">
        Cursor Quick Check Commands

        ```bash theme={null}
        # Cursor project-level config (check current directory)
        cat .cursor/mcp.json | jq .
        # Cursor global-level config
        cat ~/.cursor/mcp.json | jq .
        ```

        VS Code Quick Check Commands

        ```bash theme={null}
        # VS Code project-level settings (check current directory)
        cat .vscode/settings.json | jq .

        # VS Code global-level settings
        # macOS
        cat ~/Library/Application\ Support/Code/User/settings.json | jq .
        # Linux
        cat ~/.config/Code/User/settings.json | jq .
        ```
      </Tab>

      <Tab title="Windows">
        Cursor Quick Check Commands

        ```powershell theme={null}
        # Cursor project-level config (check current directory)
        Get-Content .cursor\mcp.json | ConvertFrom-Json
        # Command Prompt with jq
        type .cursor\mcp.json | jq .

        # Cursor global-level config
        Get-Content "$env:USERPROFILE\.cursor\mcp.json" | ConvertFrom-Json
        # Command Prompt
        type "%USERPROFILE%\.cursor\mcp.json" | jq .
        ```

        VS Code Quick Check Commands

        ```powershell theme={null}
        # VS Code project-level settings (check current directory)
        Get-Content .vscode\settings.json | ConvertFrom-Json
        # Command Prompt
        type .vscode\settings.json | jq .

        # VS Code global-level settings
        Get-Content "$env:APPDATA\Code\User\settings.json" | ConvertFrom-Json
        # Command Prompt
        type "%APPDATA%\Code\User\settings.json" | jq .
        ```
      </Tab>
    </Tabs>

    **If you don't have `jq` installed:**

    <Tabs>
      <Tab title="Install jq">
        For macOS/Linux

        ```bash theme={null}
        brew install jq   #macOS
        sudo apt-get install jq   #LinuX (Ubuntu/Debian)
        sudo yum install jq   #LinuX (CentOS/RHEL)
        ```

        For Windows

        ```powershell theme={null}
        choco install jq   #Chocolatey
        scoop install jq   #Using Scoop
        ```
      </Tab>

      <Tab title="Alternative Validation">
        1. Copy your configuration file content
        2. Visit [jsonlint.com <Icon icon="arrow-up-right-from-square" />](https://jsonlint.com)
        3. Paste and validate

        **Copy to clipboard:**

        For macOS/Linux

        ```bash theme={null}
        cat .cursor/mcp.json | pbcopy
        cat .cursor/mcp.json | xclip -selection clipboard
        ```

        For Windows

        ```powershell theme={null}
        Get-Content .cursor\mcp.json | Set-Clipboard  # PowerShell
        type .cursor\mcp.json | clip  # Command Prompt
        ```
      </Tab>

      <Tab title="Manual Download">
        Download from [https://stedolan.github.io/jq/download/  <Icon icon="arrow-up-right-from-square" />](https://stedolan.github.io/jq/download/)
      </Tab>
    </Tabs>

    <Note>If you see a parse error, fix the JSON file (missing commas, quotes, brackets, etc.)</Note>
  </Step>

  <Step title="Check Configuration Files">
    **Configuration File Locations:**

    | IDE                | Project                 | Global config                                                   |
    | :----------------- | :---------------------- | :-------------------------------------------------------------- |
    | <kbd>Cursor</kbd>  | `.cursor/mcp.json`      | `~/.cursor/mcp.json` (macOS/Linux)                              |
    |                    |                         | `%USERPROFILE%\.cursor\mcp.json` (Windows)                      |
    | <kbd>VS Code</kbd> | `.vscode/settings.json` | `~/Library/Application Support/Code/User/settings.json` (macOS) |
    |                    |                         | `~/.config/Code/User/settings.json` (Linux)                     |
    |                    |                         | `%APPDATA%\Code\User\settings.json` (Windows)                   |

    <Note>Project-level configuration takes precedence over global configuration</Note>

    **File Management Commands:**

    <Tabs>
      <Tab title="macOS/Linux">
        1. **Check if files exist:**

        ```bash theme={null}
        ls -la .cursor/mcp.json ~/.cursor/mcp.json .vscode/settings.json
        ```

        2. **Create directories if missing:**

        ```bash theme={null}
        mkdir -p .cursor ~/.cursor .vscode
        ```

        3. **Check file permissions** (if needed):

        ```bash theme={null}
        ls -la .cursor/mcp.json
        chmod 644 .cursor/mcp.json  # Fix permissions if needed
        ```
      </Tab>

      <Tab title="Windows">
        1. **Check if files exist:**

        ```powershell theme={null}
        Test-Path .cursor\mcp.json
        Test-Path "$env:USERPROFILE\.cursor\mcp.json"
        Test-Path .vscode\settings.json

        # Command Prompt
        if exist .cursor\mcp.json echo File exists
        if exist "%USERPROFILE%\.cursor\mcp.json" echo File exists
        if exist .vscode\settings.json echo File exists
        ```

        2. **Create directories if missing:**

        ```powershell theme={null}
        New-Item -ItemType Directory -Force -Path .cursor
        New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor"
        New-Item -ItemType Directory -Force -Path .vscode

        #Command Prompt
        if not exist .cursor mkdir .cursor
        if not exist "%USERPROFILE%\.cursor" mkdir "%USERPROFILE%\.cursor"
        if not exist .vscode mkdir .vscode
        ```

        3. **Check permissions** (if needed):

        ```powershell theme={null}
        # Check permissions
        Get-Acl .cursor\mcp.json
        # Grant full control to current user
        $user = [System.Security.Principal.WindowsIdentity]::GetCurrent()
        $acl = Get-Acl .cursor\mcp.json
        $acl.SetOwner($user)
        Set-Acl .cursor\mcp.json $acl
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Validate Configuration">
    <Tabs>
      <Tab title="Cursor">
        Cursor Required Configuration Format

        ```json theme={null}
        {
          "mcpServers": {
            "TestSprite": {
              "command": "npx",
              "args": ["@testsprite/testsprite-mcp@latest"],
              "env": {
                "API_KEY": "your-api-key"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="VS Code">
        VS Code Required Configuration Format

        ```json theme={null}
        {
          "mcp.servers": {
            "TestSprite": {
              "command": "npx",
              "args": ["@testsprite/testsprite-mcp@latest"],
              "env": {
                "API_KEY": "your-api-key"
              }
            }
          }
        }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

### Common Issues to Avoid

<AccordionGroup>
  <Accordion title="Missing commas">
    If there's a JSON parsing error about missing commas like `"command": "npx" "args": [...]`, make sure to add commas between JSON properties. The correct format should be `"command": "npx",` with a comma after each property except the last one.
  </Accordion>

  <Accordion title="Wrong quotes">
    If there's an error about invalid JSON syntax with single quotes like `'command': 'npx'`, JSON requires double quotes for all strings. Change it to use double quotes: `"command": "npx"`.
  </Accordion>

  <Accordion title="Wrong property name">
    If there's an error about server configuration not being recognized in Cursor, make sure you're using the correct property name. For Cursor, use `"mcpServers"` instead of `"servers"`. VS Code uses `"mcp.servers"`.
  </Accordion>

  <Accordion title="Missing required fields">
    If there's an error about incomplete server configuration with no `env` section, ensure you include all required fields: `command`, `args`, and `env`. The `env` section is necessary for passing the API key to TestSprite.
  </Accordion>
</AccordionGroup>

### Test Your Configuration

```bash theme={null}
npx @testsprite/testsprite-mcp --version
```

## API Key Issues

If you experience issues about **Invalid or missing API key**, please follow the solution below:

<Steps>
  <Step title="Get API key">
    * Visit [TestSprite Dashboard <Icon icon="arrow-up-right-from-square" />](https://testsprite.com/dashboard)
    * Go to `Settings > API Keys`
    * Generate new key if needed
  </Step>

  <Step title="Update configuration">
    ```json theme={null}
    {
      "env": {
        "API_KEY": "ts_live_abcd1234efgh5678ijkl"
      }
    }
    ```
  </Step>

  <Step title="Verify API key format">
    * Should start with `sk-user-`
    * Should be 32+ characters long
    * No extra spaces or characters
  </Step>
</Steps>


# Installation Issues
Source: https://docs.testsprite.com/mcp/troubleshooting/installation-issues

Solutions to common installation problems with TestSprite MCP Server.

## Command Not Found

If you experience issues about **`npx @testsprite/testsprite-mcp@latest` command not found**. Please follow the solution below:

<Steps>
  <Step title="Check if Node.js and npm are installed">
    ```bash theme={null}
    node --version
    npm --version
    ```

    If Node.js is not installed, install it first:

    <Tabs>
      <Tab title="Homebrew (macOS)">
        ```bash theme={null}
        brew install node
        ```
      </Tab>

      <Tab title="Direct Download">
        Download from [Node.js Official Site <Icon icon="arrow-up-right-from-square" />](https://nodejs.org/)
      </Tab>
    </Tabs>
  </Step>

  <Step title="Check if npx is available">
    ```bash theme={null}
    npx --version
    ```

    If npx is not found (should come with npm 5.2+), update npm:

    ```bash theme={null}
    npm install -g npm@latest
    ```
  </Step>

  <Step title="Try alternative installation methods">
    <Tabs>
      <Tab title="Direct package installation">
        ```bash theme={null}
        npm install -g @testsprite/mcp-server
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Use npm exec (npm 7+)">
        ```bash theme={null}
        npm exec @testsprite/testsprite-mcp@latest
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Clear npm cache if packages aren't found">
    ```bash theme={null}
    npm cache clean --force
    ```

    After cache cleaned, verify npx can find the package

    ```bash theme={null}
    npx --version
    npx @testsprite/testsprite-mcp@latest --help
    ```
  </Step>

  <Step title="Check npm registry connectivity">
    ```bash theme={null}
    npm ping
    npm config get registry
    ```
  </Step>
</Steps>

## Permission Errors

If you experience issues about **Permission denied when installing `@testsprite/testsprite-mcp` globally**. Please follow the solution below:

<Steps>
  <Step title="Choose your preferred solution method">
    <Tabs>
      <Tab title="Fix npm permissions (Recommended)">
        1. **Setup npm permissions**

        ```bash theme={null}
        mkdir ~/.npm-global
        npm config set prefix '~/.npm-global'
        echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc  # or ~/.bashrc for bash
        source ~/.zshrc  # or source ~/.bashrc
        ```

        2. **Install Latest Version**

        ```bash theme={null}
        npm install -g @testsprite/testsprite-mcp@latest
        ```

        3. **Verify Installation**

        ```bash theme={null}
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Use npx (Alternative)">
        This automatically uses the latest version without permission issues:

        ```bash theme={null}
        npx @testsprite/testsprite-mcp@latest --version
        ```
      </Tab>

      <Tab title="Install using sudo">
        <Warning>Not recommended due to security risks</Warning>

        ```bash theme={null}
        sudo npm install -g @testsprite/testsprite-mcp@latest
        ```
      </Tab>

      <Tab title="Use Node Version Manager (nvm)">
        Install nvm for clean permissions:

        ```bash theme={null}
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        nvm install node  # Installs latest Node.js with proper permissions
        npm install -g @testsprite/testsprite-mcp@latest
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Troubleshooting permission issues on macOS">
    If you still get permission errors, check npm ownership:

    ```bash theme={null}
    sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
    ```
  </Step>

  <Step title="For fresh npm setup on macOS">
    ```bash theme={null}
    sudo chown -R $(whoami) /usr/local/lib/node_modules
    sudo chown -R $(whoami) /usr/local/bin
    ```
  </Step>
</Steps>

## Node.js Version Compatibility

If you experience issues about **TestSprite MCP Server requires Node.js 22+**. Please follow the solution below:

<Note>Node.js 22 is required for optimal compatibility with TestSprite MCP Server features and dependencies.</Note>

<Steps>
  <Step title="Check current version">
    ```bash theme={null}
    node --version
    ```

    If version is below 22, **upgrade Node.js**

    <Tabs>
      <Tab title="nvm (Recommended)">
        ```bash theme={null}
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        source ~/.zshrc  # or source ~/.bashrc
        nvm install 22
        nvm use 22
        nvm alias default 22  
        node --version
        ```

        After upgrading, verify installation:

        ```bash theme={null}
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Homebrew (macOS)">
        ```bash theme={null}
        brew uninstall node  # Remove old version if needed
        brew install node@22
        brew link node@22 --force
        ```
      </Tab>

      <Tab title="Direct Download">
        Visit [Node.js Official Site <Icon icon="arrow-up-right-from-square" />](https://nodejs.org/) and download Node.js 22 LTS

        Follow the installer instructions for your operating system.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Verify npm and npx are working">
    ```bash theme={null}
    npm --version
    npx --version
    ```
  </Step>

  <Step title="Test TestSprite MCP installation">
    ```bash theme={null}
    npx @testsprite/testsprite-mcp@latest --version
    ```
  </Step>
</Steps>


# Test Execution Issues
Source: https://docs.testsprite.com/mcp/troubleshooting/test-execution-issues

Solutions to test execution problems with TestSprite MCP Server.

## General Test Execution Problems

If you experience issues where **tests fail to run, generate, or execute properly**, please follow the solution below:

<Note>Most test execution issues can be resolved by completely deleting the generated `/testsprite_tests` directory and re-running the workflow from the beginning. If the problem persists, try reinstalling the TestSprite MCP Server.</Note>

### Cursor IDE

<Tabs>
  <Tab title="Quick Reset (Recommended)">
    1. Open Cursor IDE
    2. Go to the **MCP Server panel/sidebar**
    3. Find **"TestSprite"** in the server list
    4. **Toggle** the TestSprite MCP server **OFF**
    5. Wait 5-10 seconds
    6. Toggle the TestSprite MCP server ON
    7. Wait for the server to reconnect **(green status indicator)**
  </Tab>

  <Tab title="Reload Cursor Entirely">
    1. Press <Tooltip><kbd>⌘⇧P</kbd></Tooltip>
    2. Type the following command:

    ```text theme={null}
    "Developer: Reload Window" 
    ```

    3. Press  <kbd>⇧ Enter</kbd>
  </Tab>
</Tabs>

### VS Code

<Tabs>
  <Tab title="macOS/Linux">
    1. **Stop VS Code completely**

    ```bash theme={null}
    pkill -f "Code"
    ```

    2. **Remove existing TestSprite MCP installation**

    ```bash theme={null}
    npm uninstall -g @testsprite/testsprite-mcp
    npm cache clean --force
    ```

    3. **Clear VS Code workspace cache (optional)**

    ```bash theme={null}
    rm -rf .vscode/.mcp-cache 2>/dev/null || true
    ```

    4. **Reinstall latest version**

    ```bash theme={null}
    npm install -g @testsprite/testsprite-mcp@latest
    ```

    5. **Verify installation**

    ```bash theme={null}
    npx @testsprite/testsprite-mcp@latest --version
    ```

    6. **Restart VS Code**

    ```bash theme={null}
    code .
    ```

    7. **Reload VS Code window**
       1. Press <Tooltip><kbd>⌘⇧P</kbd></Tooltip>
       2. Type the following command:
          ```text theme={null}
          "Developer: Reload Window" 
          ```
       3. Press  <kbd>⇧ Enter</kbd>
  </Tab>

  <Tab title="Windows">
    1. **Stop VS Code completely**

    ```powershell theme={null}
    taskkill /F /IM Code.exe
    ```

    2. **Remove existing TestSprite MCP installation**

    ```powershell theme={null}
    npm uninstall -g @testsprite/testsprite-mcp
    npm cache clean --force
    ```

    3. **Clear VS Code workspace cache (optional)**

    ```powershell theme={null}
    Remove-Item -Path .vscode\.mcp-cache -Recurse -Force -ErrorAction SilentlyContinue
    ```

    4. **Reinstall latest version**

    ```powershell theme={null}
    npm install -g @testsprite/testsprite-mcp@latest
    ```

    5. **Verify installation**

    ```powershell theme={null}
    npx @testsprite/testsprite-mcp@latest --version
    ```

    6. **Restart VS Code**

    ```powershell theme={null}
    code .
    ```

    7. **Reload VS Code window**
       1. Press <Tooltip><kbd>Ctrl⇧P</kbd></Tooltip>
       2. Type the following command:
          ```text theme={null}
          "Developer: Reload Window" 
          ```
       3. Press  <kbd>⇧ Enter</kbd>
  </Tab>

  <Tab title="Using npx - No Global Installation">
    Update your VS Code settings to use npx instead:

    ```json theme={null}
    {
      "mcp.servers": {
        "TestSprite": {
          "command": "npx",
          "args": ["@testsprite/testsprite-mcp@latest"],
          "env": {
            "API_KEY": "your-api-key"
          }
        }
      }
    }
    ```

    Then reload VS Code:

    1. Press <Tooltip><kbd>⌘⇧P</kbd></Tooltip>
    2. Type the following command:
       ```text theme={null}
       "Developer: Reload Window" 
       ```
    3. Press  <kbd>⇧ Enter</kbd>
  </Tab>
</Tabs>

## Verification Steps

After reinstalling, verify the MCP server is working:

<Tabs>
  <Tab title="In Terminal">
    1. **Test the server directly**

    ```bash theme={null}
    npx @testsprite/testsprite-mcp@latest --version
    ```

    2. **Check if the server responds**

    ```bash theme={null}
    npx @testsprite/testsprite-mcp@latest --help
    ```
  </Tab>

  <Tab title="In your IDE">
    1. Look for TestSprite in the MCP server list
    2. Check for green/connected status indicator
    3. Try running a simple test command
    4. Verify API key is properly configured
  </Tab>
</Tabs>

## Advanced Troubleshooting

If reinstallation doesn't resolve the issue:

<Tabs>
  <Tab title="System Requirements">
    1. Verify Node.js version **(requires 22+)**

    ```bash theme={null}
    node --version
    ```

    2. Update if needed

    ```bash theme={null}
    nvm install 22
    nvm use 22
    ```
  </Tab>

  <Tab title="Clear All Caches">
    For macOS/Linus

    ```bash theme={null}
    npm cache clean --force
    rm -rf ~/.npm
    rm -rf node_modules package-lock.json
    npm install
    ```

    For Windows (PowerShell)

    ```powershell theme={null}
    npm cache clean --force
    Remove-Item -Path "$env:USERPROFILE\.npm" -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path node_modules -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path package-lock.json -Force -ErrorAction SilentlyContinue
    npm install
    ```
  </Tab>

  <Tab title="Check API Connectivity">
    Using curl
    For macOS/Linux

    ```bash theme={null}
    curl -H "Authorization: Bearer your-api-key" https://api.testsprite.com/health
    ```

    Using PowerShell (Windows)

    ```powershell theme={null}
    Invoke-RestMethod -Uri "https://api.testsprite.com/health" -Headers @{"Authorization"="Bearer your-api-key"}
    ```
  </Tab>
</Tabs>

## Common Error Messages

<AccordionGroup>
  <Accordion title="'Command not found' after reinstallation">
    * Ensure Node.js 22+ is installed
    * Restart your terminal/IDE
    * Check PATH environment variable
  </Accordion>

  <Accordion title="Server connection failed">
    * Verify internet connection
    * Check firewall settings
    * Validate API key format
  </Accordion>

  <Accordion title="Permission denied">
    * Use npx instead of global installation
    * Fix npm permissions (see Installation Issues section)
  </Accordion>
</AccordionGroup>

## When to Contact Support

If reinstallation doesn't resolve your issue, please contact support with:

1. **System information**

```bash theme={null}
node --version
npm --version
npx @testsprite/mcp-server --version
```

2. **IDE and configuration details**
   * IDE name and version
   * Operating system version
   * Screenshot of the MCP Server panel
   * Relevant configuration files (sanitized)


# API Keys & MCP Integration
Source: https://docs.testsprite.com/web-portal/admin/api-keys

Manage your TestSprite API keys in the Web Portal and view test results from MCP Server executions.

## Generating API Keys

Generate API keys for MCP Server integration and other third-party tools.

<Steps>
  <Step title="Navigate to Settings">
    Go to <kbd>SETTINGS > API Keys</kbd> and click <kbd>Generate New API Key</kbd>.

    <Frame>
      <img alt="API Key" />
    </Frame>
  </Step>

  <Step title="Configure and Save">
    Provide a **descriptive name** (e.g., "MCP Integration") and <kbd>Copy</kbd> the generated API key immediately.

    <Warning>
      Store it securely. It won't be shown again
    </Warning>

    <Frame>
      <img alt="API Key" />
    </Frame>
  </Step>
</Steps>

## Managing API Keys

<Frame>
  <img alt="API Key" />
</Frame>

<Tabs>
  <Tab title="Each API Key Shows">
    Each API key displays key information fields that help you identify, track, and manage your keys effectively.

    | Field                   | Description                                        |
    | :---------------------- | :------------------------------------------------- |
    | <kbd>Key Name</kbd>     | Descriptive identifier                             |
    | <kbd>Key Value</kbd>    | Partially hidden (e.g., `sk_test_****...****abcd`) |
    | <kbd>Created Date</kbd> | When generated                                     |
    | <kbd>Last Used</kbd>    | Most recent usage                                  |
  </Tab>

  <Tab title="Available Actions">
    Manage your API keys with these actions to control access, monitor usage, and maintain security.

    | Action                  | Description                    |
    | :---------------------- | :----------------------------- |
    | <kbd>View Details</kbd> | See usage statistics           |
    | <kbd>Revoke</kbd>       | Immediately disable the key    |
    | <kbd>Delete</kbd>       | Remove the API key permanently |
  </Tab>
</Tabs>

## Viewing MCP Test Results

When you run tests through MCP Server in your IDE, view the results in your Web Portal dashboard.

Go to <kbd>TESTING > MCP Tests</kbd> and view all tests executed through MCP Server

<Frame>
  <img alt="API Key" />
</Frame>

Test Information Displayed:

| Field              | Description                      |
| :----------------- | :------------------------------- |
| **Test Name**      | Description of the executed test |
| **Execution Time** | When the test was run            |
| **Duration**       | Test execution time              |
| **Status**         | Passed, Failed, or In Progress   |
| **Test Type**      | Frontend, Backend, or Mixed      |

### Test Reports

Click on any test result to view **detailed test execution logs**, **individual test case results**, **error messages and debugging information**, and **performance metrics**.

<Frame>
  <img alt="Report" />
</Frame>

<br />

<Card title="View Example Test Report" icon="file" href="../../learn/mcp-demo#test-report-example">
  Click to see a detailed example of TestSprite test reports with execution logs and performance metrics.
</Card>

## Next Steps

<Info>Your API key is used in the MCP Server configuration to authenticate with TestSprite's testing engine.</Info>

<CardGroup>
  <Card title="Start Your First Test" href="../../mcp/getting-started/first-test">
    Get hands-on experience with TestSprite MCP
  </Card>

  <Card title="MCP Server Documentation" href="../../mcp/getting-started/overview">
    Complete TestSprite MCP Server guide
  </Card>

  <Card title="Installation Guide" href="../../mcp/getting-started/installation">
    Step-by-step setup instructions
  </Card>

  <Card title="Workflow Examples" href="../../mcp/concepts/test-type-lifecycle">
    Learn TestSprite MCP Server workflows
  </Card>
</CardGroup>


# Back-End (APIs) Testing
Source: https://docs.testsprite.com/web-portal/core/api-testing

AI-powered backend testing for RESTful APIs with speed and precision.

<Frame>
  <img alt="plan" />
</Frame>

## Key Features

| Feature                          | Description                                                                                   |
| :------------------------------- | :-------------------------------------------------------------------------------------------- |
| <kbd>Fast Setup</kbd>            | Get started quickly with minimal documentation—no extensive prompts or full codebases needed  |
| <kbd>Comprehensive Testing</kbd> | Covers functional, security, performance, error handling, and edge case testing automatically |
| <kbd>Smart Reports</kbd>         | Detailed outputs with error types, root causes, and recommended fixes                         |
| <kbd>Natural Language</kbd>      | Provide feedback and adjustments using plain English—no technical commands required           |

## Getting Started

To begin using TestSprite for back-end testing, follow these steps:

### Step 1: Set Up Your API Testing Environment

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Create New Test">
    Navigate to [TestSprite Dashboard  <Icon icon="arrow-up-right-from-square" />](https://www.testsprite.com/dashboard/testing) and click <kbd>Create a Test</kbd> from the sidebar
  </Step>

  <Step title="Name Your Project">
    Enter a project name - you'll be automatically directed to Backend Testing
  </Step>

  <Step title="Provide API Details">
    Add your API information and natural language instructions to guide our AI testing
    <Note> We highly recommend **upload API documentation** to help our AI better understand your APIs</Note>

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>
</Steps>

<Accordion title="Example API Documentation">
  [GenRex API Reference  <Icon icon="arrow-up-right-from-square" />](https://docs.genrex.com/docs/1.0/api-reference/request-generation) - Shows how comprehensive API docs help our AI generate better tests
</Accordion>

### Step 2: Review Generated Test Plans

<Info>
  You can expand each test type to view detailed scenarios and modify content directly to suit your specific needs.
</Info>

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Review AI Generated Test Plan">
    Our AI creates a comprehensive test plan covering multiple test types for your APIs
  </Step>

  <Step title="Select Test Categories">
    Choose which test categories and cases to implement, or select all for comprehensive coverage
  </Step>
</Steps>

**AI generates these test types automatically:**

| Test Type                  | Description                                                             |
| :------------------------- | :---------------------------------------------------------------------- |
| <kbd>Core Testing</kbd>    | Functional testing, error handling, and response content validation     |
| <kbd>Security & Auth</kbd> | Security testing, authorization, authentication, and boundary testing   |
| <kbd>Performance</kbd>     | Load testing, performance analysis, edge cases, and concurrency testing |

<Tip>
  **Best practice:** Select all available test cases to ensure comprehensive coverage. You can also add custom test cases using natural language.
</Tip>

### Step 3: Run Your Tests

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Initiate Test Execution">
    Click <kbd>Next</kbd> to start running your selected test plan
  </Step>

  <Step title="AI Generates & Executes">
    TestSprite automatically generates test code, executes tests, and analyzes results
  </Step>
</Steps>

### Step 4: Review Test Results

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="View Execution Report">
    TestSprite displays detailed insights and actionable recommendations to refine your software
  </Step>

  <Step title="Interact with AI Chatbot">
    Provide feedback, request adjustments, or ask questions about test results
  </Step>
</Steps>

**Detailed Analysis for Failed Tests:**

| Feature                  | Description                                                                                    |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| <kbd>Error & Trace</kbd> | Clear issue description and full code stack traceback showing exactly where problems occurred  |
| <kbd>Cause & Fix</kbd>   | AI-powered root cause analysis with suggested solutions and code snippets for quick resolution |

## Advanced Configuration

### Using Natural Language for Questions and Test Adjustments

<Info>
  Ask questions or suggest test adjustments using natural language—no specific format required.
</Info>

<Frame>
  <img alt="plan" />
</Frame>

<br />

<Accordion title="Example Natural Language Request">
  ```plaintext theme={null}
  "Test POST /orders with invalid parameters and expect a 400 error code."
  ```

  TestSprite automatically interprets and updates the corresponding test case, making testing smoother and more efficient.
</Accordion>

## Examples

See what TestSprite's AI generates for your APIs:

TestSprite automatically generates comprehensive security tests like this one that validates API signature handling:

```python Expandable Sample Security Test theme={null}
import hashlib
import hmac
import json
import pytest
import requests
import time

# Define the API URL and credentials (use environment variables for added security)
api_url = "https://your-api-url.com/v1/text2music/generateMusic"
api_key = "hide_for_privacy_protection"
api_secret = "hide_for_privacy_protection"

def create_signature(api_secret, data_to_sign):
    return hmac.new(api_secret.encode(), data_to_sign.encode(), hashlib.sha256).hexdigest()

def test_invalid_gx_signature():
    # Construct the payload
    payload = {
        "duration": 10,
        "text": "intense EDM",
    }
    payload_json = json.dumps(payload, separators=(",", ":"))

    # Create correct signature
    timestamp = str(int(time.time() * 1000))
    data_to_sign = f"{timestamp}.{payload_json}"
    correct_signature = create_signature(api_secret, data_to_sign)

    # Tamper the payload
    tampered_payload = payload_json.replace("intense EDM", "soft jazz")

    # Use correct timestamp and an intentionally incorrect signature
    tampered_signature = create_signature(api_secret, f"{timestamp}.{tampered_payload}")

    # Create headers with tampered payload
    headers = {
        "gx-key": api_key,
        "gx-signature": f"t={timestamp},v={tampered_signature}",
        "Content-Type": "application/json",
    }

    # Send POST request with tampered payload
    response = requests.post(api_url, data=tampered_payload, headers=headers)
    
    # Parse the response
    response_data = response.json()

    # Assertions
    assert "statusCode" in response_data, "Expected 'statusCode' in the response"
    assert response_data["statusCode"] == 400, f"Expected statusCode 400, got {response_data['statusCode']}"

test_invalid_gx_signature()
```

This test validates that your API properly rejects requests with invalid signatures, ensuring security integrity.


# Front-End (UI) Testing
Source: https://docs.testsprite.com/web-portal/core/ui-testing

AI-powered UI testing for web applications with comprehensive user interaction tests.

<Frame>
  <img alt="plan" />
</Frame>

### Key Features

| Feature                             | Description                                                                                                                  |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| <kbd>Fast Setup</kbd>               | Get started in minutes with minimal configuration. Just provide your website URLs and let our AI agent handle the rest       |
| <kbd>AI-Generated Test Cases</kbd>  | Dynamically creates intelligent test plans tailored to your product's content and edge cases with full customization control |
| <kbd>Smart Video Playback</kbd>     | Every interaction is recorded and replayable—see exactly how tests run and spot UI issues visually                           |
| <kbd>Live Test Preview</kbd>        | Watch test execution unfold in real-time to catch potential issues instantly                                                 |
| <kbd>Actionable Reports</kbd>       | Detailed execution reports with error analysis, root cause identification, and AI-suggested fixes                            |
| <kbd>Natural Language Control</kbd> | Refine tests using plain English—no code required for tweaking scenarios or adding edge cases                                |

<Info>
  **Bonus:** TestSprite automatically generates reusable Python + Playwright test code perfect for CI/CD pipelines and regression testing.
</Info>

## Getting Started

To begin using TestSprite for front-end testing, follow these steps:

### Step 1: Set Up Your Front-End Testing Environment

<br />

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Access TestSprite Dashboard">
    Navigate to [TestSprite Dashboard  <Icon icon="arrow-up-right-from-square" />](https://www.testsprite.com/dashboard/testing) and click <kbd>Create a Test</kbd> from the sidebar
  </Step>

  <Step title="Enter Application Details">
    Provide your web application URL and optional authentication credentials
  </Step>

  <Step title="Add Testing URLs">
    Include additional pages you want to test within the same flow
  </Step>

  <Step title="Special Instructions (Optional)">
    Add specific testing requirements to help AI generate more accurate test plans
  </Step>
</Steps>

<Accordion title="Example Application Configuration">
  ```json theme={null}
  {
    "Web application starting URL": "https://www.example.com",
    "Web application sign in username/email (optional)": "user@example.com", 
    "Web application sign in password (optional)": "password123"
  }
  ```
</Accordion>

### Step 2: Configure Test Plans

<br />

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Review AI-Generated Test Plan">
    Review the draft test plan tailored to your UI with end-to-end scenarios
  </Step>

  <Step title="Select & Modify Scenarios">
    Choose test scenarios to execute and modify descriptions to match your requirements
  </Step>
</Steps>

<Accordion title="Example Test Scenarios Generated by AI">
  * **Test the 'Log In' Link Functionality**\
    Ensure login link directs users to correct page and handles authentication properly

  * **Test the 'Add to Cart' Button**\
    Verify cart button adds products, updates cart count, and shows confirmation messages

  * **Test the 'Close Banner' Button**\
    Ensure banner close buttons dismiss properly without disrupting other elements

  * **Verify Link Redirection Accuracy**\
    Confirm navigation links redirect to intended pages with proper loading and content
</Accordion>

<Info>
  Our AI may further refine test plans after performing real-time analysis of your application during execution.
</Info>

### Step 3: Run Your Tests

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Start Test Execution">
    Click <kbd>Next</kbd> to begin generating and executing your selected test cases
  </Step>

  <Step title="Monitor Web Preview">
    Watch real-time test execution through the Web Preview feature
  </Step>

  <Step title="Automatic Validation">
    TestSprite validates UI interactions and generates detailed results automatically
  </Step>
</Steps>

### Step 4: Review Test Results

<br />

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="Access Detailed Report">
    TestSprite provides comprehensive test results with visual insights
  </Step>

  <Step title="Analyze Results">
    Review test outcomes, errors, and performance metrics for your UI
  </Step>
</Steps>

## Advanced Features

### Web Preview for Context

TestSprite includes a Web Preview feature that allows you to visualize the testing process

<Frame>
  <img alt="plan" />
</Frame>

* Watch as each element is interacted with on your web page
* Understand how the page responds to various actions
* Quickly identify UI issues that might otherwise be missed

### Using Natural Language to Refine and Regenerate Tests

Refine tests using plain English—no technical configuration required.

<Frame>
  <img alt="plan" />
</Frame>

<Tabs>
  <Tab title="How it works">
    1. Edit the test description in plain language
    2. TestSprite automatically regenerates the test
  </Tab>

  <Tab title="Example">
    ```
    Original: "Test login functionality"

    Refined: "Ensure the Sign In link directs users to the login page and guides them to their dashboard after successful authentication."
    ```
  </Tab>
</Tabs>


# Introduction
Source: https://docs.testsprite.com/web-portal/getting-started/introduction

Get started with TestSprite Web Portal

<Frame>
  <iframe />
</Frame>

TestSprite is the easiest AI software testing agent for fully autonomous testing.
Our no-code AI completes testing cycles in **10-20** minutes, so you can ship with confidence without manual QA work.

The TestSprite Web Portal gives you a central place to configure projects, manage API keys, run and monitor tests, and review detailed reports—without leaving the browser.

<Columns>
  <Card title="Overview" icon="book" href="overview">
    Learn what TestSprite Web Portal can do
  </Card>

  <Card title="Start API Testings" icon="terminal" href="../core/api-testing">
    Start testing your backend on TestSprite Web Portal
  </Card>

  <Card title="Run UI Testings" icon="window-maximize" href="../core/ui-testing">
    Start frontend testing on TestSprite Web Portal
  </Card>

  <Card title="Create Test List" icon="list" href="../maintenance/test-lists">
    Organize tests using Test List
  </Card>

  <Card title="Start Monitoring" icon="chart-simple" href="../maintenance/monitoring">
    Start continuous scheduling and monitoring for your prjects.
  </Card>

  <Card title="Join Community" icon="comments" href="https://discord.com/invite/QQB9tJ973e">
    Connect with other users
  </Card>
</Columns>


# Overview
Source: https://docs.testsprite.com/web-portal/getting-started/overview

Web dashboard for API keys, test management, and automated monitoring.

<Frame>
  <img alt="plan" />
</Frame>

## Step 1: Customer Input

Simply provide your application details to get started

<Frame>
  <img alt="plan" />
</Frame>

| Requirement                           | Description                         |
| :------------------------------------ | :---------------------------------- |
| <kbd>Application URLs</kbd>           | Frontend and backend endpoints      |
| <kbd>Authentication credentials</kbd> | API keys, login details, etc.       |
| <kbd>Testing requirements</kbd>       | Specific scenarios you want covered |

<Tip>
  Our AI creates a completely customized testing plan in real-time—no templates or generic approaches.
</Tip>

## Step 2: Test Plans Auto Generation

TestSprite's AI creates a detailed, customized testing plan with thoughtfully crafted test cases targeting specific scenarios for your product. Each test case includes a clear description explaining its purpose and rationale.

<Frame>
  <img alt="plan" />
</Frame>

<br />

<Accordion title="Example test plan for back-end API testing">
  Generated testing plan for [Amazon S3 `create_bucket` API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html):

  1. **Basic Bucket Creation**
     * Create bucket with unique name and verify existence

  2. **Name Validation**
     * Test invalid names (special characters, spaces) and verify error responses

  3. **Location Constraints**
     * Create buckets in specific regions (us-east-1, eu-west-1)

  4. **Access Control (ACL)**
     * Test different ACL settings (private, public-read, authenticated-read)

  5. **Versioning**
     * Create bucket with versioning enabled and verify configuration

  6. **...**
</Accordion>

## Step 3: User Review & Confirmation

Before proceeding, users can review the automatically generated test plans. This step allows you to <span> **manually adjust**</span>, add, or remove specific tests and ensure the generated plans align with your testing goals.

<Frame>
  <img alt="plan" />
</Frame>

<br />

## Step 4: Test Code Auto Generation (Implementation)

Based on the test plan from Step 2, here's an example of the actual Python test code that TestSprite's AI automatically creates

<Frame>
  <img alt="plan" />
</Frame>

<Steps>
  <Step title="AI Code Generation">
    TestSprite's AI converts your approved test plan into production-ready code
  </Step>

  <Step title="Cloud Compilation">
    Code is automatically uploaded and compiled in our secure cloud environment
  </Step>

  <Step title="Smart Auto-Fixing">
    AI resolves compilation issues and applies self-patching for optimal accuracy
  </Step>
</Steps>

<Info>
  **Zero coding required!** Our AI delivers the highest accuracy among all Testing Autopilot tools through intelligent self-patching.
</Info>

<Accordion title="View Generated Test Code Example">
  ```python Expandable Sample Test Code theme={null}
  import unittest
  import boto3
  from botocore.exceptions import ClientError

  class TestCreateBucketAPI(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
          # Initialize the S3 client
          cls.s3_client = boto3.client('s3')

      def test_basic_bucket_creation(self):
          bucket_name = 'test-bucket-basic'

          try:
              # Test creating a new S3 bucket
              self.s3_client.create_bucket(Bucket=bucket_name)
          except ClientError as e:
              self.fail(f"Error creating basic bucket: {e}")

          # Verify that the bucket exists
          response = self.s3_client.list_buckets()
          buckets = [bucket['Name'] for bucket in response['Buckets']]
          self.assertIn(bucket_name, buckets)

      def test_invalid_bucket_name(self):
          invalid_bucket_names = ['bucket with spaces', 'bucket_with_special_characters!']

          for bucket_name in invalid_bucket_names:
              with self.subTest(bucket_name=bucket_name):
                  with self.assertRaises(ClientError) as context:
                      # Test creating a bucket with an invalid name
                      self.s3_client.create_bucket(Bucket=bucket_name)

                  self.assertEqual(context.exception.response['Error']['Code'], 'InvalidBucketName')

      # And the other test cases ...

  if __name__ == '__main__':
      unittest.main()
  ```
</Accordion>

## Step 5: Test Execution

TestSprite automatically executes the generated test cases in our cloud environment, closely monitoring the results to promptly detect any issues.

<Frame>
  <img alt="plan" />
</Frame>

## Step 6: Review and Adjust

TestSprite's AI **automatically analyzes test failures**, **identifies root causes**, and provides **actionable recommendations** for quick resolution. **Chat with AI** using plain English to modify tests—**zero coding required**, **instant regeneration**, and **complete control** over your test scenarios.

<Tip>
  **Pro tip:** Edit test prompts anytime to regenerate cases with different scenarios - no coding required!
</Tip>

<Frame>
  <img alt="plan" />
</Frame>

**Available tools:**

| Tool                         | Description                 |
| :--------------------------- | :-------------------------- |
| <kbd>VS Code plugin</kbd>    | Direct console adjustments  |
| <kbd>AI chat assistant</kbd> | Questions and modifications |
| <kbd>Prompt editing</kbd>    | Regenerate test cases       |

## Step 7: Final Testing Report

TestSprite generates a comprehensive report covering

<Frame>
  <img alt="plan" />
</Frame>

| Section                      | Description                    |
| :--------------------------- | :----------------------------- |
| <kbd>Test results</kbd>      | Pass/fail status for each case |
| <kbd>Improvement areas</kbd> | Actionable recommendations     |
| <kbd>Security findings</kbd> | Vulnerabilities and fixes      |
| <kbd>Team sharing</kbd>      | Export and collaborate easily  |


# Monitoring & Scheduling
Source: https://docs.testsprite.com/web-portal/maintenance/monitoring

Automate your testing workflow with TestSprite's Monitoring feature.

The Monitoring feature allows you to schedule **automated test executions** at regular intervals. Instead of manually running tests, you can set up schedules that automatically execute your test lists, providing **continuous monitoring** of your application's health and performance.

<Frame>
  <img alt="plan" />
</Frame>

<br />

## Key Benefits

* **Continuous Quality Assurance**: Automatically detect issues before they reach users. 24/7 monitoring and regression detection without manual effort.
* **Flexible Scheduling**: Recurring test executions with multiple scheduling options. Monitor run times and pause/modify schedules as needed.
* **Proactive Issue Detection**: Immediate notifications when tests fail. Track trends and identify performance degradation over time.

## Getting Started with Monitoring

### Prerequisites

Before setting up schedules:

* **[Create Test Lists](/web-portal/maintenance/test-lists)**: You need existing test lists to schedule
* **Verify Test Stability**: Ensure your tests run reliably
* **Set Up Notifications**: Configure how you want to receive alerts
* **Check Account Limits**: Verify your plan supports scheduling

### Steps

<Steps>
  <Step title="Navigate to Monitoring">
    Go to <kbd>Monitoring</kbd> and click <kbd>New Schedule</kbd> to get started

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Select Test List">
    Choose an existing test list to schedule

    <Note>Review test cases and execution settings, and confirm test list is ready for automation.</Note>

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Configure Schedule">
    Set **execution frequency** (daily, weekly, monthly), choose **specific times and days**, configure **timezone settings**, and set up **failure notifications**.

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>
</Steps>

## Schedule Configuration

Configure when and how often your tests run automatically. Choose from multiple frequency options, set specific times and timezones, and customize scheduling patterns to match your monitoring needs.

### Frequency Options

Select how frequently your tests execute. Available options include daily runs, weekly schedules on specific days, monthly executions on set dates, and custom patterns for advanced scheduling needs.

<Frame>
  <img alt="plan" />
</Frame>

<br />

<Tabs>
  <Tab title="Frequency Options">
    Choose how often your tests run automatically. Select from daily, weekly, monthly, or create custom scheduling patterns.

    | Frequency Options  | Description                                  |
    | :----------------- | :------------------------------------------- |
    | <kbd>Daily</kbd>   | Execute tests every day at specified time    |
    | <kbd>Weekly</kbd>  | Run tests on specific days of the week       |
    | <kbd>Monthly</kbd> | Schedule tests for specific dates each month |
    | <kbd>Custom</kbd>  | Define complex scheduling patterns           |
  </Tab>

  <Tab title="Example Configurations">
    Real-world examples showing how to configure different schedule types with specific times and timezones.

    ```yaml theme={null}
    Daily Schedule:
      Time: 06:00 AM UTC
      Frequency: Every day
      
    Weekly Schedule:
      Days: Monday, Wednesday, Friday
      Time: 09:00 AM EST
      
    Monthly Schedule:
      Date: 1st of every month
      Time: 12:00 PM PST
    ```
  </Tab>
</Tabs>

### Timezone Settings

Configure the timezone for your scheduled test executions. All schedules use **UTC by default**. You can specify different timezones to match your local time or business hours.

<Frame>
  <img alt="plan" />
</Frame>

<Note>
  **Timezone Best Practices:** Convert your **local time to UTC** for accurate scheduling. Consider **daylight saving time changes** that may affect execution times. Use a **consistent timezone** across your team to avoid confusion.
</Note>

## Managing Schedules

Once schedules are created, you can monitor their execution, view detailed status information, and manage them through the schedule dashboard. Track execution history, pause or modify schedules as needed, and ensure your monitoring runs smoothly.

### Schedule Dashboard

The Schedule Dashboard provides a comprehensive overview of all your automated test schedules, allowing you to monitor their status, execution history, and upcoming runs at a glance.

| Overview Information     | Description                                         |
| :----------------------- | :-------------------------------------------------- |
| <kbd>Schedule Name</kbd> | Descriptive name for the scheduled execution        |
| <kbd>Test List</kbd>     | Associated test list that will be executed          |
| <kbd>Frequency</kbd>     | How often the schedule runs (daily, weekly, etc.)   |
| <kbd>Next Run</kbd>      | When the next execution is scheduled                |
| <kbd>Status</kbd>        | Current schedule status (active, paused, completed) |
| <kbd>Last Result</kbd>   | Result of the most recent execution                 |

### Schedule Actions

Manage your test schedules with these available actions. Each schedule can be controlled individually to fit your testing workflow and requirements.

| Action                     | Description                      |
| :------------------------- | :------------------------------- |
| <kbd>Run Now</kbd>         | Execute the schedule immediately |
| <kbd>Edit Schedule</kbd>   | Modify timing and configuration  |
| <kbd>Pause/Resume</kbd>    | Temporarily disable or re-enable |
| <kbd>View Results</kbd>    | See detailed execution history   |
| <kbd>Delete Schedule</kbd> | Remove schedule permanently      |


# Test Lists
Source: https://docs.testsprite.com/web-portal/maintenance/test-lists

Organize test collections, track execution history, and manage testing projects efficiently.

Test Lists are organized collections of test cases that help you group related tests together. Whether you're testing different features, environments, or user flows, Test Lists provide a structured way to manage your testing efforts.

<Frame>
  <img alt="plan" />
</Frame>

## Key Features

| Feature                                | Description                                                                                                                                                                                                                              |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <kbd>Centralized Test Management</kbd> | View all test lists in one dashboard, track execution status across collections, search and filter by name or status, and sort by date, count, or type                                                                                   |
| <kbd>Test Organization</kbd>           | Organize Frontend Tests with browser automation, Backend Tests for API functionality, and Mixed Collections combining both test types                                                                                                    |
| <kbd>Execution Tracking</kbd>          | Track your **previous execution** status to view the test's last run with **status indicators** showing **Passed** (all tests completed successfully), **Attention** (some tests need review), or **Failed** (tests encountered errors). |

## Creating Test Lists

<Steps>
  <Step title="Navigate to Test Lists">
    Go to <kbd>Dashboard</kbd> → <kbd>Test Lists</kbd> and click <kbd>New List</kbd> to get started

    <Frame>
      <img alt="plan" />
    </Frame>
  </Step>

  <Step title="Add Test Cases">
    Add test cases from existing creations in <kbd>All Test</kbd>, or create new tests by configuring web application information and letting TestSprite's AI generate comprehensive test cases

    <Frame>
      <img alt="mcp intro" />
    </Frame>
  </Step>

  <Step title="Organize and Configure">
    Name your test list descriptively, review and customize generated test cases, and maintain your test lists as needed
  </Step>
</Steps>

## Managing Test Lists

<Tabs>
  <Tab title="Search & Filter">
    <Frame>
      <img alt="plan" />
    </Frame>

    | Option                | Description                                                   |
    | :-------------------- | :------------------------------------------------------------ |
    | <kbd>Search</kbd>     | Search by test list name to quickly find specific collections |
    | <kbd>All Status</kbd> | View all test lists regardless of status                      |
    | <kbd>Passed</kbd>     | Show only successfully executed test lists                    |
    | <kbd>Attention</kbd>  | Filter test lists needing review                              |
    | <kbd>Failed</kbd>     | Display test lists with execution errors                      |
  </Tab>

  <Tab title="Sorting Options">
    <Frame>
      <img alt="plan" />
    </Frame>

    | Option                             | Description                          |
    | :--------------------------------- | :----------------------------------- |
    | <kbd>Total test cases</kbd>        | Order by number of tests in the list |
    | <kbd>Total frontend test</kbd>     | Order by frontend test count         |
    | <kbd>Total backend test</kbd>      | Sort by backend test count           |
    | <kbd>Previous execution date</kbd> | Sort by most recently executed       |
  </Tab>
</Tabs>

## Test List Details

Each test list displays:

| Field                          | Description                                     |
| :----------------------------- | :---------------------------------------------- |
| <kbd>Test List Name</kbd>      | Descriptive identifier for your test collection |
| <kbd>Previous Execution</kbd>  | Last run date and time                          |
| <kbd>Total Test Cases</kbd>    | Combined count of all tests in the list         |
| <kbd>Total Frontend Test</kbd> | Number of UI/browser tests                      |
| <kbd>Total Backend Test</kbd>  | Number of API/server tests                      |

## Execution Actions

| Action                  | Description                          |
| :---------------------- | :----------------------------------- |
| <kbd>Run Tests</kbd>    | Execute all tests in the list        |
| <kbd>View Results</kbd> | Review detailed test reports         |
| <kbd>Delete List</kbd>  | Remove test list (with confirmation) |


