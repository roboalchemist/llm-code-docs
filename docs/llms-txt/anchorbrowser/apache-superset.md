# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/apache-superset.md

# Apache Superset

> Test Apache Superset dashboards and data visualization workflows with Playwright's end-to-end testing framework.

# How to Test Apache Superset with Playwright

Test your Apache Superset dashboards and data exploration workflows with Playwright's end-to-end testing framework. You'll catch visualization errors and ensure data accuracy by testing charts and filters in a real browser environment. Use Playwright to automate dashboard interactions and validate SQL queries.

[View Superset's Playwright configuration](https://github.com/apache/superset/blob/master/superset-frontend/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Superset testing:

```bash  theme={null}
npm install playwright
```

## Write Tests

Create tests for dashboard and chart functionality:

```JavaScript  theme={null}
import { test, expect } from '@playwright/test';

test('dashboard loads with correct charts', async ({ page }) => {
  await page.goto('http://localhost:8088/superset/dashboard/1/');
  
  // Login if required
  await page.fill('[name="username"]', 'admin');
  await page.fill('[name="password"]', 'admin');
  await page.click('[type="submit"]');
  
  // Verify dashboard elements
  await expect(page.locator('.dashboard-header')).toBeVisible();
  await expect(page.locator('.chart-container')).toHaveCount(4);
});

test('chart filters update data correctly', async ({ page }) => {
  await page.goto('http://localhost:8088/explore/');
  
  // Apply filter
  await page.click('[data-test="adhoc-filter-edit"]');
  await page.selectOption('[data-test="select-column"]', 'category');
  await page.fill('[data-test="filter-value"]', 'Technology');
  await page.click('[data-test="run-query"]');
  
  // Verify filtered results
  await expect(page.locator('.slice_container')).toContainText('Technology');
});
```

Playwright handles chart rendering, filter interactions, and SQL query execution automatically. You can test custom visualizations, dashboard permissions, and data source connections.

## Scale your Apache Superset testing with Anchor Browser

Run your Playwright Superset tests on cloud browsers with enterprise-grade reliability and persistent database connections. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
