# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/monday.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Monday

> Automate Monday.com project management workflows with Playwright when APIs aren't available.

# How to Automate Monday with Playwright

Automate critical Monday.com project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual board setup and reduce task tracking errors by automating repetitive project management processes. Use Playwright to interact with Monday.com's web interface programmatically.

[View Monday.com's API documentation](https://developer.monday.com/api-reference/docs) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Monday.com tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Monday.com
await page.goto('https://auth.monday.com/login');
await page.fill('[data-testid="email-field"]', process.env.MONDAY_EMAIL);
await page.fill('[data-testid="password-field"]', process.env.MONDAY_PASSWORD);
await page.click('[data-testid="login-button"]');

// Create new board
await page.click('[data-testid="create-board-button"]');
await page.fill('[data-testid="board-name-input"]', 'Product Launch Campaign');
await page.selectOption('[data-testid="board-template"]', 'Marketing Campaign');
await page.click('[data-testid="create-board-confirm"]');

// Add new item to board
await page.click('[data-testid="add-item-button"]');
await page.fill('[data-testid="item-name"]', 'Website Landing Page');
await page.selectOption('[data-testid="status-column"]', 'Working on it');
await page.fill('[data-testid="person-column"]', 'Sarah Marketing');
await page.click('[data-testid="date-column"]');
await page.fill('[data-testid="due-date"]', '2024-03-15');

// Update item progress
await page.click('[data-testid="timeline-column"]');
await page.dragAndDrop('[data-testid="timeline-bar"]', '[data-testid="timeline-bar"]', {
  sourcePosition: { x: 0, y: 0 },
  targetPosition: { x: 100, y: 0 }
});

// Add automation
await page.click('[data-testid="board-menu"]');
await page.click('[data-testid="automations-tab"]');
await page.click('[data-testid="add-automation"]');
await page.selectOption('[data-testid="automation-trigger"]', 'when status changes to Done');
await page.selectOption('[data-testid="automation-action"]', 'notify person');
await page.click('[data-testid="save-automation"]');

await browser.close();
```

Playwright handles board creation, item management, and automation setup automatically. You can automate project tracking, team notifications, and reporting workflows.

## Scale your Monday.com automation with Anchor Browser

Run your Playwright Monday automations on cloud browsers with enterprise-grade reliability and persistent Monday sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
