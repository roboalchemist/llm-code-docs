# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/wrike.md

# Wrike

> Automate Wrike project management workflows with Playwright when APIs aren't available.

# How to Automate Wrike with Playwright

Automate critical Wrike project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual project setup and reduce task management errors by automating repetitive work management processes. Use Playwright to interact with Wrike's web interface programmatically.

[View Wrike's API documentation](https://developers.wrike.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Wrike tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Wrike
await page.goto('https://www.wrike.com/login/');
await page.fill('[data-testid="email-input"]', process.env.WRIKE_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.WRIKE_PASSWORD);
await page.click('[data-testid="login-button"]');

// Create new project
await page.click('[data-testid="create-project-button"]');
await page.fill('[data-testid="project-title"]', 'Website Redesign Project');
await page.selectOption('[data-testid="project-template"]', 'Marketing Project');
await page.click('[data-testid="create-project-confirm"]');

// Add new task
await page.click('[data-testid="add-task-button"]');
await page.fill('[data-testid="task-title"]', 'Design homepage mockup');
await page.fill('[data-testid="task-description"]', 'Create responsive design mockups for new homepage');
await page.selectOption('[data-testid="task-status"]', 'In Progress');
await page.click('[data-testid="assignee-dropdown"]');
await page.click('text=Design Team');

// Set task dates and priority
await page.click('[data-testid="start-date-picker"]');
await page.click('[data-testid="today-button"]');
await page.click('[data-testid="due-date-picker"]');
await page.click('[data-testid="next-week-button"]');
await page.selectOption('[data-testid="priority-select"]', 'High');
await page.click('[data-testid="save-task"]');

// Create custom dashboard
await page.click('[data-testid="dashboards-menu"]');
await page.click('[data-testid="create-dashboard"]');
await page.fill('[data-testid="dashboard-name"]', 'Project Overview');
await page.click('[data-testid="add-widget"]');
await page.selectOption('[data-testid="widget-type"]', 'Tasks by Status');
await page.click('[data-testid="save-dashboard"]');

await browser.close();
```

Playwright handles project creation, task assignment, and dashboard customization automatically. You can automate time tracking, resource allocation, and progress reporting workflows.

## Scale your Wrike automation with Anchor Browser

Run your Playwright Wrike automations on cloud browsers with enterprise-grade reliability and persistent Wrike sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
