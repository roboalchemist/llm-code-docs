# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fincen-105.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# FinCEN 105 (CMIR)

> Automate FinCEN 105 currency reporting workflows with Playwright when APIs aren't available.

# How to Automate FinCEN 105 with Playwright

Automate critical FinCEN 105 Currency and Monetary Instrument Report workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual form completion and reduce customs reporting errors by automating repetitive currency declaration processes. Use Playwright to interact with the FinCEN 105 web interface programmatically.

[View more about FinCEN 105](https://fincen105.cbp.dhs.gov/) for available web forms when applicable.

## Setup

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FinCEN 105](https://www.fincen.gov/system/files/shared/fin105_cmir.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FinCEN 105 portal
await page.goto('https://www.fincen.gov/resources/filing-information');

// Start new CMIR filing
await page.click('[data-testid="new-filing-button"]');
await page.selectOption('[name="report_type"]', 'import');

// Fill traveler information
await page.fill('[name="first_name"]', 'John');
await page.fill('[name="last_name"]', 'Smith');
await page.fill('[name="date_of_birth"]', '01/15/1980');
await page.fill('[name="passport_number"]', 'A12345678');
await page.selectOption('[name="country_of_citizenship"]', 'Canada');

// Transportation details
await page.fill('[name="flight_number"]', 'AC123');
await page.fill('[name="arrival_date"]', '12/15/2024');
await page.selectOption('[name="port_of_entry"]', 'JFK');
await page.fill('[name="departure_city"]', 'Toronto, ON');

// Currency information
await page.selectOption('[name="currency_type"]', 'cash');
await page.fill('[name="currency_amount"]', '15000');
await page.selectOption('[name="currency_denomination"]', 'USD');
await page.fill('[name="source_of_funds"]', 'Business proceeds from sale');

// Submit declaration
await page.click('[name="certify_accuracy"]');
await page.fill('[name="electronic_signature"]', 'John Smith');
await page.click('[data-testid="submit-declaration"]');

// Download confirmation receipt
await page.click('[data-testid="download-receipt"]');

await browser.close();
```

Playwright handles form validation, currency calculations, and submission processes automatically. You can automate bulk filings, compliance reporting, and traveler declaration workflows.

## Scale your FinCEN 105 automation with Anchor Browser

Run your Playwright FinCEN 105 automations on cloud browsers with enterprise-grade reliability and persistent customs sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
