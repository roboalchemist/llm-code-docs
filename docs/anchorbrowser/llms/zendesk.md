# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/zendesk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk

> Automate Zendesk customer service workflows with Playwright when APIs aren't available.

# How to Automate Zendesk with Playwright

Automate critical Zendesk customer service workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket processing and reduce response time errors by automating repetitive support processes. Use Playwright to interact with Zendesk's web interface programmatically.

[View Zendesk's API documentation](https://developer.zendesk.com/api-reference/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Zendesk tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Zendesk
await page.goto('https://your-company.zendesk.com/agent/');
await page.fill('[name="user[email]"]', process.env.ZENDESK_EMAIL);
await page.fill('[name="user[password]"]', process.env.ZENDESK_PASSWORD);
await page.click('[type="submit"]');

// Navigate to tickets
await page.click('[data-test-id="views_views-list_row-item"]');
await page.click('text=Open tickets');

// Update ticket priority
await page.click('.ticket-row:first-child');
await page.click('[data-test-id="priority-field"]');
await page.selectOption('[data-test-id="priority-field"]', 'high');

// Add internal note
await page.fill('[data-test-id="omni-composer-rich-text"]', 'Customer escalation processed - priority updated');
await page.click('[data-test-id="submit-button"]');

await browser.close();

```

Playwright handles ticket loading, field updates, and comment submissions automatically. You can automate ticket routing, bulk status updates, and customer communication workflows.

## Scale your Zendesk automation with Anchor Browser

Run your Playwright Zendesk automations on cloud browsers with enterprise-grade reliability and persistent Zendesk sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
