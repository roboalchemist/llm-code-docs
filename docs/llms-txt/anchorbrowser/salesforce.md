# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/salesforce.md

# Salesforce

> Automate Salesforce CRM workflows with Playwright when APIs aren't available.

# How to Automate Salesforce with Playwright

Automate critical Salesforce CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual data entry and reduce lead processing errors by automating repetitive sales processes. Use Playwright to interact with Salesforce's web interface programmatically.

[View Salesforce's REST API documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

### Authentication Options

**Option 1: Direct Login (Basic)**
Store credentials securely using environment variables:

```JavaScript  theme={null}
// Use environment variables for security
const SALESFORCE_USERNAME = process.env.SALESFORCE_USERNAME;
const SALESFORCE_PASSWORD = process.env.SALESFORCE_PASSWORD;
```

**Option 2: OAuth2 Integration**
For production environments, implement OAuth2 flow:

```
import { chromium } from 'playwright';

// OAuth2 flow for secure authentication
const page = await browser.newPage();
await page.goto('https://login.salesforce.com/services/oauth2/authorize?...');
// Handle OAuth callback and token exchange
const accessToken = await handleOAuthCallback(page);
```

## Automate Workflows

Create scripts for common Salesforce tasks:

```
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Salesforce
await page.goto('https://login.salesforce.com/');
await page.fill('#username', process.env.SALESFORCE_USERNAME);
await page.fill('#password', process.env.SALESFORCE_PASSWORD);
await page.click('#Login');

// Navigate to Leads
await page.click('[title="App Launcher"]');
await page.fill('input[placeholder="Search apps and items..."]', 'Leads');
await page.click('text=Leads');

// Create new lead
await page.click('text=New');
await page.fill('[name="firstName"]', 'John');
await page.fill('[name="lastName"]', 'Doe');
await page.fill('[name="Company"]', 'Acme Corporation');
await page.fill('[name="Email"]', 'john.doe@acme.com');
await page.selectOption('[name="LeadSource"]', 'Website');
await page.click('button[name="SaveEdit"]');

await browser.close();
```

Playwright handles dynamic Lightning components, field validations, and record saves automatically. You can automate lead conversion, opportunity updates, and account management workflows.

## Scale your Salesforce automation with Anchor Browser

Run your Playwright Salesforce automations on cloud browsers with enterprise-grade reliability and persistent Salesforce sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
