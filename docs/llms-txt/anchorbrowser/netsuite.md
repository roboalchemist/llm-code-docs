# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/netsuite.md

# NetSuite

> Automate NetSuite business workflows with Playwright when APIs aren't available.

# How to Automate NetSuite with Playwright

Automate critical NetSuite workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual data entry and reduce errors by automating repetitive business processes. Use Playwright to interact with NetSuite's web interface programmatically.

[View NetSuite's SuiteScript documentation](https://system.netsuite.com/help/helpcenter/en_US/APIs/REST_API_Browser/record/v1/2023.1/index.html) for API alternatives when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common NetSuite tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to NetSuite
await page.goto('https://system.netsuite.com/pages/customerlogin.jsp');
await page.fill('#email', process.env.NETSUITE_EMAIL);
await page.fill('#password', process.env.NETSUITE_PASSWORD);
await page.click('#login-submit');

// Navigate to customer records
await page.click('text=Lists');
await page.click('text=Customers');

// Create new customer record
await page.click('text=New');
await page.fill('#companyname', 'Acme Corporation');
await page.fill('#email', 'contact@acme.com');
await page.click('#btn_multibutton_submitter');

await browser.close();
```

Playwright handles dynamic loading, form submissions, and navigation automatically. You can automate financial reporting, customer management, and inventory updates.

## Scale your NetSuite automation with Anchor Browser

Run your Playwright NetSuite automations on cloud browsers with enterprise-grade reliability and session persistence. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
