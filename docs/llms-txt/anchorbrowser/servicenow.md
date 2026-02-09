# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/servicenow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# ServiceNow

> Automate ServiceNow IT service management workflows with Playwright when APIs aren't available.

# How to Automate ServiceNow with Playwright

Automate critical ServiceNow IT service management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket processing and reduce service delivery errors by automating repetitive ITSM processes. Use Playwright to interact with ServiceNow's web interface programmatically.

[View ServiceNow's API documentation](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common ServiceNow tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to ServiceNow
await page.goto('https://your-instance.service-now.com/');
await page.fill('[name="user_name"]', process.env.SERVICENOW_USERNAME);
await page.fill('[name="user_password"]', process.env.SERVICENOW_PASSWORD);
await page.click('[name="not_important"]');

// Navigate to Incident Management
await page.click('[data-testid="nav-incident-management"]');
await page.click('[data-testid="create-new-incident"]');

// Create new incident
await page.fill('[data-testid="caller-field"]', 'John Smith');
await page.selectOption('[data-testid="category-select"]', 'Hardware');
await page.selectOption('[data-testid="subcategory-select"]', 'Monitor');
await page.fill('[data-testid="short-description"]', 'Monitor display issues');
await page.fill('[data-testid="description"]', 'User reports flickering and color distortion on primary monitor');
await page.selectOption('[data-testid="priority-select"]', '3 - Moderate');
await page.selectOption('[data-testid="assignment-group"]', 'Desktop Support');

// Add work notes and resolve
await page.fill('[data-testid="work-notes"]', 'Replaced monitor cable. Issue resolved.');
await page.selectOption('[data-testid="incident-state"]', 'Resolved');
await page.selectOption('[data-testid="resolution-code"]', 'Solved (Permanently)');
await page.click('[data-testid="update-incident"]');

// Create change request
await page.click('[data-testid="change-management"]');
await page.click('[data-testid="create-change-request"]');
await page.fill('[data-testid="change-short-description"]', 'Server memory upgrade');
await page.selectOption('[data-testid="change-type"]', 'Standard');
await page.selectOption('[data-testid="risk-level"]', 'Low');
await page.click('[data-testid="submit-change"]');

await browser.close();
```

Playwright handles form navigation, dropdown selections, and workflow transitions automatically. You can automate incident resolution, change approvals, and asset management workflows.

## Scale your ServiceNow automation with Anchor Browser

Run your Playwright ServiceNow automations on cloud browsers with enterprise-grade reliability and persistent ServiceNow sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
