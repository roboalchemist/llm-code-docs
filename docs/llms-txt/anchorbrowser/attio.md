# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/attio.md

# Attio

> Automate Attio CRM workflows with Playwright when APIs aren't available.

# How to Automate Attio with Playwright

Automate critical Attio CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual contact management and reduce data entry errors by automating repetitive customer relationship processes. Use Playwright to interact with Attio's web interface programmatically.

[View Attio's API documentation](https://docs.attio.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Attio tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Attio
await page.goto('https://app.attio.com/login');
await page.fill('[data-testid="email-input"]', process.env.ATTIO_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.ATTIO_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to contacts
await page.click('[data-testid="nav-people"]');
await page.click('[data-testid="add-person-button"]');

// Create new contact
await page.fill('[data-testid="first-name"]', 'Sarah');
await page.fill('[data-testid="last-name"]', 'Johnson');
await page.fill('[data-testid="email-field"]', 'sarah.johnson@company.com');
await page.fill('[data-testid="company-field"]', 'Tech Innovations Inc');
await page.selectOption('[data-testid="status-select"]', 'qualified-lead');

// Add deal to pipeline
await page.click('[data-testid="deals-tab"]');
await page.click('[data-testid="add-deal-button"]');
await page.fill('[data-testid="deal-name"]', 'Enterprise Software License');
await page.fill('[data-testid="deal-value"]', '25000');
await page.click('[data-testid="save-contact"]');

await browser.close();
```

Playwright handles dynamic form fields, relationship linking, and pipeline updates automatically. You can automate lead qualification, deal progression, and contact enrichment workflows.

## Scale your Attio automation with Anchor Browser

Run your Playwright Attio automations on cloud browsers with enterprise-grade reliability and persistent Attio sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
