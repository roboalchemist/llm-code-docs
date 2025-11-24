# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/pipedrive.md

# Pipedrive

> Automate Pipedrive CRM workflows with Playwright when APIs aren't available.

# How to Automate Pipedrive with Playwright

Automate critical Pipedrive CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual deal tracking and reduce sales pipeline errors by automating repetitive sales processes. Use Playwright to interact with Pipedrive's web interface programmatically.

[View Pipedrive's API documentation](https://developers.pipedrive.com/docs/api/v1) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Pipedrive tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Pipedrive
await page.goto('https://your-company.pipedrive.com/');
await page.fill('[data-testid="login-email"]', process.env.PIPEDRIVE_EMAIL);
await page.fill('[data-testid="login-password"]', process.env.PIPEDRIVE_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to deals pipeline
await page.click('[data-testid="menu-deals"]');
await page.click('[data-testid="add-deal-button"]');

// Create new deal
await page.fill('[data-testid="deal-title"]', 'Enterprise Software License');
await page.fill('[data-testid="deal-value"]', '45000');
await page.selectOption('[data-testid="deal-stage"]', 'qualified-to-buy');
await page.fill('[data-testid="person-name"]', 'Lisa Rodriguez');
await page.fill('[data-testid="organization-name"]', 'Global Tech Solutions');

// Set follow-up activity
await page.click('[data-testid="add-activity-button"]');
await page.selectOption('[data-testid="activity-type"]', 'call');
await page.fill('[data-testid="activity-subject"]', 'Follow-up demo call');
await page.click('[data-testid="save-deal"]');

await browser.close();
```

Playwright handles pipeline navigation, deal progression, and activity scheduling automatically. You can automate lead qualification, sales forecasting, and customer follow-up workflows.

## Scale your Pipedrive automation with Anchor Browser

Run your Playwright Pipedrive automations on cloud browsers with enterprise-grade reliability and persistent Pipedrive sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
