# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/docusign.md

# DocuSign

> Automate DocuSign electronic signature workflows with Playwright when APIs aren't available.

# How to Automate DocuSign with Playwright

Automate critical DocuSign electronic signature workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual document sending and reduce signature processing errors by automating repetitive contract management processes. Use Playwright to interact with DocuSign's web interface programmatically.

[View DocuSign's API documentation](https://developers.docusign.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common DocuSign tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to DocuSign
await page.goto('https://account.docusign.com/');
await page.fill('[data-qa="Username"]', process.env.DOCUSIGN_EMAIL);
await page.fill('[data-qa="Password"]', process.env.DOCUSIGN_PASSWORD);
await page.click('[data-qa="Log In"]');

// Navigate to envelope creation
await page.click('[data-qa="nav-send"]');
await page.click('[data-qa="start-sending"]');

// Upload document
await page.click('[data-qa="upload-document"]');
const fileInput = await page.locator('input[type="file"]');
await fileInput.setInputFiles('./contracts/employment-agreement.pdf');

// Add recipients
await page.click('[data-qa="add-recipient"]');
await page.fill('[data-qa="recipient-name"]', 'John Smith');
await page.fill('[data-qa="recipient-email"]', 'john.smith@company.com');
await page.selectOption('[data-qa="recipient-role"]', 'signer');

// Position signature fields
await page.click('[data-qa="tag-document"]');
await page.click('[data-qa="signature-tab"]');
await page.click('[data-qa="signature-placement"]', { position: { x: 200, y: 400 } });

// Send envelope
await page.click('[data-qa="send-envelope"]');

await browser.close();
```

Playwright handles document uploads, recipient management, and signature field positioning automatically. You can automate contract distribution, template creation, and signing ceremony workflows.

## Scale your DocuSign automation with Anchor Browser

Run your Playwright DocuSign automations on cloud browsers with enterprise-grade reliability and persistent DocuSign sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
