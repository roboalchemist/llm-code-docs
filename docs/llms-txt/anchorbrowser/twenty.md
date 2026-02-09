# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/twenty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Twenty

> Test Twenty CRM workflows with Playwright's end-to-end testing framework.

# How to Test Twenty with Playwright

Test your Twenty CRM workflows with Playwright's end-to-end testing framework. You'll catch UI bugs and ensure contact management works correctly by testing in a real browser environment. Use Playwright to automate lead creation, pipeline management, and data validation features.

[View Twenty's Playwright configuration](https://github.com/twentyhq/twenty/blob/main/packages/twenty-e2e-testing/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Twenty testing:

```bash  theme={null}
npm install playwright
```

## Write Tests

Create tests for CRM functionality:

```JavaScript  theme={null}
import { test, expect } from '@playwright/test';

test('creates new contact successfully', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Navigate to contacts
  await page.click('[data-testid="nav-contacts"]');
  await expect(page.locator('[data-testid="contacts-table"]')).toBeVisible();
  
  // Create new contact
  await page.click('[data-testid="add-contact-button"]');
  await page.fill('[data-testid="contact-first-name"]', 'John');
  await page.fill('[data-testid="contact-last-name"]', 'Doe');
  await page.fill('[data-testid="contact-email"]', 'john.doe@example.com');
  await page.click('[data-testid="save-contact"]');
  
  // Verify contact appears in list
  await expect(page.locator('text=John Doe')).toBeVisible();
});

test('manages sales pipeline correctly', async ({ page }) => {
  await page.goto('http://localhost:3000/opportunities');
  
  // Create new opportunity
  await page.click('[data-testid="add-opportunity"]');
  await page.fill('[data-testid="opportunity-name"]', 'Enterprise Deal');
  await page.fill('[data-testid="opportunity-amount"]', '50000');
  await page.selectOption('[data-testid="opportunity-stage"]', 'qualification');
  await page.click('[data-testid="save-opportunity"]');
  
  // Verify opportunity in pipeline
  await expect(page.locator('.pipeline-stage')).toContainText('Enterprise Deal');
});
```

Playwright handles dynamic loading, form validations, and state updates automatically. You can test contact imports, task management, and custom field configurations.

## Scale your Twenty testing with Anchor Browser

Run your Playwright Twenty tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
