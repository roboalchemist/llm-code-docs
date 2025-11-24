# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/jira.md

# Jira

> Automate Jira project management workflows with Playwright when APIs aren't available.

# How to Automate Jira with Playwright

Automate critical Jira project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket creation and reduce project tracking errors by automating repetitive development processes. Use Playwright to interact with Jira's web interface programmatically.

[View Jira's REST API documentation](https://developer.atlassian.com/server/jira/platform/rest/v11000/intro/#gettingstarted) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Jira tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Jira
await page.goto('https://your-company.atlassian.net/');
await page.fill('#username', process.env.JIRA_USERNAME);
await page.click('#login-submit');
await page.fill('#password', process.env.JIRA_PASSWORD);
await page.click('#login-submit');

// Navigate to project
await page.click('[data-testid="global-pages.directories.projects-directory-v2"]');
await page.click('text=Development Project');

// Create new issue
await page.click('[data-testid="project-sidebar.create-issue-button"]');
await page.selectOption('[data-testid="issue-type-select"]', 'Story');
await page.fill('[data-testid="issue-summary-field"]', 'Implement user authentication');
await page.fill('[data-testid="issue-description-field"]', 'Add OAuth login functionality');
await page.selectOption('[data-testid="assignee-select"]', 'john.doe');
await page.click('[data-testid="issue-create-submit"]');

// Update issue status
await page.click('text=DEV-123');
await page.click('[data-testid="issue-workflow-transition"]');
await page.click('text=In Progress');

await browser.close();
```

Playwright handles issue creation, workflow transitions, and field updates automatically. You can automate sprint planning, bulk status updates, and project reporting workflows.

## Scale your Jira automation with Anchor Browser

Run your Playwright Jira automations on cloud browsers with enterprise-grade reliability and persistent Jira sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
