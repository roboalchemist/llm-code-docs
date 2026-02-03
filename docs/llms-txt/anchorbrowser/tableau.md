# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/tableau.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau

> Automate Tableau dashboard workflows with Playwright when APIs aren't available.

# How to Automate Tableau with Playwright

Automate critical Tableau dashboard workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual reporting tasks and reduce data processing errors by automating repetitive visualization processes. Use Playwright to interact with Tableau's web interface programmatically.

[View Tableau's REST API documentation](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright

```

## Automate Workflows

Create scripts for common Tableau tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Tableau Server
await page.goto('https://your-tableau-server.com');
await page.fill('[name="username"]', process.env.TABLEAU_USERNAME);
await page.fill('[name="password"]', process.env.TABLEAU_PASSWORD);
await page.click('[type="submit"]');

// Navigate to workbooks
await page.click('text=Explore');
await page.click('text=All Workbooks');

// Refresh data source
await page.click('text=Sales Dashboard');
await page.click('[data-test-id="refresh-button"]');
await page.waitForSelector('.refresh-complete');

// Export dashboard as PDF
await page.click('[data-test-id="share-button"]');
await page.click('text=Download');
await page.selectOption('[name="format"]', 'pdf');
await page.click('#download-button');

await browser.close();
```

Playwright handles dashboard loading, data refresh cycles, and export processes automatically. You can automate report generation, data source updates, and user permission management.

## Scale your Tableau automation with Anchor Browser

Run your Playwright Tableau automations on cloud browsers with enterprise-grade reliability and persistent Tableau sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
