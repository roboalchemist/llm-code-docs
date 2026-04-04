# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/figma.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Figma

> Automate Figma design workflows with Playwright when APIs aren't available.

# How to Automate Figma with Playwright

Automate critical Figma design workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual design handoffs and reduce version control errors by automating repetitive design collaboration processes. Use Playwright to interact with Figma's web interface programmatically.

[View Figma's API documentation](https://www.figma.com/developers/api) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Figma actions:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Figma
await page.goto('https://www.figma.com/login');
await page.fill('[data-testid="email"]', process.env.FIGMA_EMAIL);
await page.fill('[data-testid="password"]', process.env.FIGMA_PASSWORD);
await page.click('[data-testid="submit"]');

// Navigate to team files
await page.click('[data-testid="dashboard-team-switcher"]');
await page.click('text=Design Team');
await page.click('text=Mobile App Redesign');

// Create new frame
await page.click('[data-testid="toolbar-frame-tool"]');
await page.click('[data-testid="canvas"]');
await page.selectOption('[data-testid="frame-preset"]', 'iPhone 14');

// Add components and export
await page.click('[data-testid="assets-panel"]');
await page.dragAndDrop('[data-testid="button-component"]', '[data-testid="canvas-frame"]');
await page.fill('[data-testid="text-input"]', 'Get Started');

// Export assets
await page.click('[data-testid="export-button"]');
await page.selectOption('[data-testid="export-format"]', 'PNG');
await page.selectOption('[data-testid="export-scale"]', '2x');
await page.click('[data-testid="export-download"]');

// Share with developer
await page.click('[data-testid="share-button"]');
await page.fill('[data-testid="share-email"]', 'developer@company.com');
await page.selectOption('[data-testid="permission-level"]', 'can view');
await page.click('[data-testid="send-invite"]');

await browser.close();
```

Playwright handles component manipulation, export processes, and collaboration workflows automatically. You can automate design system updates, asset generation, and developer handoff processes.

## Scale your Figma automation with Anchor Browser

Run your Playwright Figma automations on cloud browsers with enterprise-grade reliability and persistent Figma sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
