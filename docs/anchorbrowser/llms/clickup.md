# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/clickup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Clickup

> Automate ClickUp project management workflows with Playwright when APIs aren't available.

# How to Automate ClickUp with Playwright

Automate critical ClickUp project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual task creation and reduce project tracking errors by automating repetitive productivity processes. Use Playwright to interact with ClickUp's web interface programmatically.

[View ClickUp's API documentation](https://clickup.com/api/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common ClickUp tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to ClickUp
await page.goto('https://app.clickup.com/login');
await page.fill('[data-test="login-email-input"]', process.env.CLICKUP_EMAIL);
await page.fill('[data-test="login-password-input"]', process.env.CLICKUP_PASSWORD);
await page.click('[data-test="login-submit"]');

// Navigate to workspace
await page.click('[data-test="sidebar-workspace"]');
await page.click('text=Development Team');

// Create new task
await page.click('[data-test="new-task-button"]');
await page.fill('[data-test="draft-view__title"]', 'Implement user dashboard');
await page.fill('[data-test="description-input"]', 'Create responsive dashboard with analytics widgets');
await page.selectOption('[data-test="priority-select"]', 'high');
await page.click('[data-test="assignee-dropdown"]');
await page.click('text=John Developer');

// Set due date and create task
await page.click('[data-test="due-date-picker"]');
await page.click('[data-test="date-next-week"]');
await page.click('[data-test="save-task"]');

// Update task status
await page.click('[data-test="status-dropdown"]');
await page.click('text=In Progress');

await browser.close();
```

Playwright handles task creation, status updates, and team assignments automatically. You can automate sprint planning, time tracking, and project reporting workflows.

## Scale your Clickup automation with Anchor Browser

Run your Playwright Clickup automations on cloud browsers with enterprise-grade reliability and persistent Clickup sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
