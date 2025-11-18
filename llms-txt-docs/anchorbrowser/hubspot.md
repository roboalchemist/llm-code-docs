# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/hubspot.md

# HubSpot

> Automate HubSpot CRM workflows with Playwright when APIs aren't available.

# How to Automate HubSpot with Playwright

Automate critical HubSpot CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual lead processing and reduce sales pipeline errors by automating repetitive marketing and sales processes. Use Playwright to interact with HubSpot's web interface programmatically.

[View HubSpot's API documentation](https://developers.hubspot.com/docs/api/overview) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common HubSpot tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to HubSpot
await page.goto('https://app.hubspot.com/login');
await page.fill('#username', process.env.HUBSPOT_EMAIL);
await page.fill('#password', process.env.HUBSPOT_PASSWORD);
await page.click('#loginBtn');

// Navigate to contacts
await page.click('[data-selenium-test="nav-primary-contacts-contacts"]');
await page.click('[data-selenium-test="create-contact-button"]');

// Create new contact
await page.fill('[data-field="firstname"]', 'Michael');
await page.fill('[data-field="lastname"]', 'Chen');
await page.fill('[data-field="email"]', 'michael.chen@techcorp.com');
await page.fill('[data-field="company"]', 'TechCorp Solutions');
await page.selectOption('[data-field="lifecyclestage"]', 'marketingqualifiedlead');

// Create associated deal
await page.click('[data-selenium-test="associations-tab"]');
await page.click('[data-selenium-test="create-deal-button"]');
await page.fill('[data-field="dealname"]', 'TechCorp Enterprise Package');
await page.fill('[data-field="amount"]', '75000');
await page.selectOption('[data-field="dealstage"]', 'qualifiedtobuy');
await page.click('[data-selenium-test="save-contact"]');

await browser.close();
```

Playwright handles form validations, association creation, and pipeline updates automatically. You can automate lead scoring, email campaign management, and sales forecasting workflows.

## Scale your HubSpot automation with Anchor Browser

Run your Playwright HubSpot automations on cloud browsers with enterprise-grade reliability and persistent HubSpot CRM sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
