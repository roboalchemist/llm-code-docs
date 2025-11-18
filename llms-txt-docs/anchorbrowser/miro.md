# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/miro.md

# Miro

> Automate Miro collaboration workflows with Playwright when APIs aren't available.

# How to Automate Miro with Playwright

Automate critical Miro collaboration workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual board setup and reduce brainstorming session errors by automating repetitive visual collaboration processes. Use Playwright to interact with Miro's web interface programmatically.

[View Miro's API documentation](https://developers.miro.com/docs) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Miro actions:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Miro
await page.goto('https://miro.com/login/');
await page.fill('[data-testid="mr-form-login-btn-start-1"]', process.env.MIRO_EMAIL);
await page.click('[data-testid="mr-form-login-btn-start-1"]');
await page.fill('[data-testid="password"]', process.env.MIRO_PASSWORD);
await page.click('[data-testid="mr-form-login-btn-signin-1"]');

// Create new board
await page.click('[data-testid="create-board-button"]');
await page.fill('[data-testid="board-title-input"]', 'Sprint Planning Session');
await page.selectOption('[data-testid="template-select"]', 'Agile Planning');
await page.click('[data-testid="create-button"]');

// Add sticky notes for user stories
await page.click('[data-testid="toolbar-sticky-note"]');
await page.click('[data-testid="canvas"]', { position: { x: 200, y: 200 } });
await page.fill('[data-testid="sticky-note-text"]', 'As a user, I want to login easily');
await page.press('[data-testid="sticky-note-text"]', 'Escape');

// Create swimlanes
await page.click('[data-testid="toolbar-shapes"]');
await page.click('[data-testid="rectangle-shape"]');
await page.dragAndDrop('[data-testid="canvas"]', '[data-testid="canvas"]', {
  sourcePosition: { x: 100, y: 100 },
  targetPosition: { x: 800, y: 150 }
});

// Share board with team
await page.click('[data-testid="share-board-button"]');
await page.fill('[data-testid="invite-email"]', 'team@company.com');
await page.selectOption('[data-testid="permission-level"]', 'can edit');
await page.click('[data-testid="send-invitation"]');

await browser.close();
```

Playwright handles canvas interactions, shape creation, and collaboration features automatically. You can automate template setup, workshop facilitation, and board organization workflows.

## Scale your Miro automation with Anchor Browser

Run your Playwright Miro automations on cloud browsers with enterprise-grade reliability and persistent Miro sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
