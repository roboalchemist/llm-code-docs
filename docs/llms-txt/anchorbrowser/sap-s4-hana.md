# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/sap-s4-hana.md

# SAP S/4HANA

> Automate SAP S/4HANA business workflows with Playwright when APIs aren't available.

# How to Automate SAP S/4HANA with Playwright

Automate critical SAP S/4HANA workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ERP tasks and reduce processing errors by automating repetitive business processes. Use Playwright to interact with SAP's web interface programmatically.

[View SAP's API documentation](https://api.sap.com/products/SAPS4HANA/apis/REST) for programmatic connections when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common SAP tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to SAP S/4HANA
await page.goto('https://your-sap-system.com:8000/sap/bc/gui/sap/its/webgui');
await page.fill('#sap-user', process.env.SAP_USERNAME);
await page.fill('#sap-password', process.env.SAP_PASSWORD);
await page.click('#LOGON_BUTTON');

// Navigate to purchase orders
await page.fill('#RSWPSearchTextField', 'ME21N');
await page.press('#RSWPSearchTextField', 'Enter');

// Create new purchase order
await page.fill('[title="Vendor"]', '100001');
await page.fill('[title="Purchase Organization"]', '1000');
await page.fill('[title="Material"]', 'MAT-001');
await page.fill('[title="Quantity"]', '10');
await page.click('#toolbar_save');

await browser.close();
```

Playwright handles SAP GUI navigation, transaction codes, and form submissions automatically. You can automate procurement, financial postings, and material movements.

## Scale your SAP S/4HANA automation with Anchor Browser

Run your Playwright SAP automations on cloud browsers with enterprise-grade reliability and persistent SAP sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
