# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/uipath.md

# UiPath

> Automate UiPath RPA management workflows with Playwright when APIs aren't available.

# How to Automate UiPath with Playwright

Automate critical UiPath RPA management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual bot deployment and reduce automation management errors by automating repetitive RPA administration processes. Use Playwright to interact with UiPath's web interface programmatically.

[View UiPath's API documentation](https://docs.uipath.com/orchestrator/reference) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common UiPath tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to UiPath Orchestrator
await page.goto('https://your-tenant.uipath.com/');
await page.fill('[data-testid="email"]', process.env.UIPATH_EMAIL);
await page.fill('[data-testid="password"]', process.env.UIPATH_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to Automation Cloud
await page.click('[data-testid="orchestrator-tile"]');
await page.click('[data-testid="processes-menu"]');

// Deploy new process
await page.click('[data-testid="add-process-button"]');
await page.fill('[data-testid="process-name"]', 'Invoice Processing Bot');
await page.selectOption('[data-testid="package-select"]', 'InvoiceBot_v1.2');
await page.selectOption('[data-testid="environment-select"]', 'Production');
await page.click('[data-testid="deploy-process"]');

// Schedule automation job
await page.click('[data-testid="jobs-menu"]');
await page.click('[data-testid="create-job-button"]');
await page.selectOption('[data-testid="process-dropdown"]', 'Invoice Processing Bot');
await page.selectOption('[data-testid="robot-select"]', 'Robot-01');
await page.fill('[data-testid="job-priority"]', 'High');
await page.click('[data-testid="start-job"]');

// Monitor job status
await page.click('[data-testid="monitoring-tab"]');
await expect(page.locator('[data-testid="job-status"]')).toContainText('Running');

await browser.close();
```

Playwright handles process deployment, job scheduling, and monitoring workflows automatically. You can automate bot management, queue processing, and performance reporting workflows.

## Scale your UiPath automation with Anchor Browser

Run your Playwright UiPath automations on cloud browsers with enterprise-grade reliability and persistent UiPath sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
