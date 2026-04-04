# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/grafana.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Grafana

> Test Grafana dashboards and monitoring workflows with Playwright's end-to-end testing framework.

# How to Test Grafana with Playwright

Test your Grafana dashboards and monitoring workflows with Playwright's end-to-end testing framework. You'll catch visualization bugs and ensure critical alerts work correctly by testing in a real browser environment. Use Playwright to automate dashboard interactions and validate data accuracy.

[View Grafana's Playwright configuration](https://github.com/grafana/grafana/blob/main/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Grafana testing:

```bash  theme={null}
npm install playwright
```

## Write Tests

Create tests for dashboard functionality:

```JavaScript  theme={null}
import { test, expect } from '@playwright/test';

test('dashboard loads with correct panels', async ({ page }) => {
  await page.goto('http://localhost:3000/d/dashboard-id');
  
  // Login if required
  await page.fill('[name="user"]', 'admin');
  await page.fill('[name="password"]', 'admin');
  await page.click('[type="submit"]');
  
  // Verify dashboard elements
  await expect(page.locator('.panel-title')).toContainText('CPU Usage');
  await expect(page.locator('.graph-panel')).toBeVisible();
});

test('alert rule triggers correctly', async ({ page }) => {
  await page.goto('http://localhost:3000/alerting/list');
  
  // Check alert status
  await expect(page.locator('[data-testid="alert-rule"]')).toBeVisible();
  await expect(page.locator('.alert-state-ok')).toContainText('OK');
});
```

Playwright handles dashboard loading, data refresh cycles, and alert state changes automatically. You can test panel configurations, data source connections, and user permissions.

## Scale your Grafana testing with Anchor Browser

Run your Playwright Grafana tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
