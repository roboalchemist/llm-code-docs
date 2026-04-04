# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/openhands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenHands

> Test OpenHands' AI-driven software development workflows with Playwright's end-to-end testing framework.

# How to Test OpenHands with Playwright

Test your OpenHands AI development workflows with Playwright's end-to-end testing framework. You'll catch UI bugs and ensure agent interactions work correctly by testing in a real browser environment. Use Playwright to automate chat interactions and validate code generation features.

[View OpenHands' Playwright configuration](https://github.com/All-Hands-AI/OpenHands/blob/main/frontend/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for OpenHands testing:

```bash  theme={null}
npm install playwright
```

## Write Tests

Create tests for AI agent functionality:

```JavaScript  theme={null}
import { test, expect } from '@playwright/test';

test('chat interface loads and responds', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Verify chat interface is ready
  await expect(page.locator('[data-testid="chat-input"]')).toBeVisible();
  await expect(page.locator('[data-testid="send-button"]')).toBeEnabled();
  
  // Send a message to the agent
  await page.fill('[data-testid="chat-input"]', 'Create a simple Python function');
  await page.click('[data-testid="send-button"]');
  
  // Verify agent response appears
  await expect(page.locator('.agent-response')).toBeVisible();
  await expect(page.locator('.code-block')).toContainText('def');
});

test('file explorer functionality works', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Test file tree navigation
  await page.click('[data-testid="file-explorer"]');
  await expect(page.locator('.file-tree')).toBeVisible();
  
  // Create new file through UI
  await page.click('[data-testid="new-file-button"]');
  await page.fill('[data-testid="file-name-input"]', 'test.py');
  await page.click('[data-testid="confirm-button"]');
  
  // Verify file appears in explorer
  await expect(page.locator('text=test.py')).toBeVisible();
});
```

Playwright handles agent response timing, code syntax highlighting, and file system interactions automatically. You can test multi-step workflows, error handling, and agent memory persistence.

## Scale your OpenHands testing with Anchor Browser

Run your Playwright OpenHands tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
