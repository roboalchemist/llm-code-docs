# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/bop-s243.md

# BOP Form BP-S0243

> Automate Bureau of Prisons inmate request workflows with Playwright when APIs aren't available.

# How to Automate BOP Form BP-S0243 with Playwright

Automate Bureau of Prisons administrative request workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual inmate records processing and reduce administrative delays by automating repetitive BOP filing processes. Use Playwright to interact with BOP's TRULINCS system programmatically.

[View BOP's developer resources](https://www.bop.gov/resources/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [BOP Form BP-S0243](https://www.bop.gov/policy/forms/BP_A0243.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to Bureau of Prisons website
await page.goto('https://www.bop.gov/mobile/policy/forms.jsp');

// Start new BP-S0243 request
await page.click('[data-testid="new-form-s0243"]');
await page.selectOption('[name="request_type"]', 'administrative_remedy');

// Inmate information
await page.fill('[name="register_number"]', '12345-678');
await page.fill('[name="inmate_name"]', 'Smith, John Michael');
await page.fill('[name="date_of_birth"]', '06/20/1980');
await page.selectOption('[name="facility"]', 'FCI_TERMINAL_ISLAND');
await page.fill('[name="unit"]', 'B-2');
await page.fill('[name="cell_number"]', '215');

// Request details
await page.selectOption('[name="subject_category"]', 'medical_services');
await page.fill('[name="request_title"]', 'Request for Specialist Consultation');
await page.fill('[name="request_date"]', '01/15/2025');

// Statement of facts
await page.fill('[name="statement_of_facts"]', 'Requested medical consultation with orthopedic specialist on 12/01/2024. No appointment scheduled after 45 days. Medical staff acknowledged request but provided no timeline.');

// Relief requested
await page.fill('[name="relief_sought"]', 'Schedule consultation with orthopedic specialist within 30 days to address ongoing knee injury documented in medical records.');

// Supporting documentation
await page.check('[name="attachments_included"]');
await page.click('[data-testid="upload-supporting-docs"]');
await page.setInputFiles('[name="supporting_documents"]', './documents/medical_request_form.pdf');

// Previous attempts to resolve
await page.selectOption('[name="informal_resolution_attempted"]', 'yes');
await page.fill('[name="informal_resolution_date"]', '12/15/2024');
await page.fill('[name="staff_contacted"]', 'Medical Unit Manager Thompson');
await page.fill('[name="resolution_outcome"]', 'No resolution provided. Staff stated request was pending review.');

// Witness information (if applicable)
await page.fill('[name="witness_name"]', 'Johnson, Robert');
await page.fill('[name="witness_register"]', '98765-432');
await page.fill('[name="witness_unit"]', 'B-2');

// Emergency request designation
await page.check('[name="expedited_review"]');
await page.fill('[name="expedited_justification"]', 'Ongoing pain affecting daily activities and work assignment performance.');

// Signature and certification
await page.check('[name="certify_accuracy"]');
await page.fill('[name="signature_name"]', 'John Michael Smith');
await page.fill('[name="signature_date"]', '01/15/2025');
await page.fill('[name="register_number_confirm"]', '12345-678');
await page.click('[data-testid="submit-request"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles request categorization, documentation attachment, and BOP submission processes automatically. You can automate remedy requests, appeal filings, and administrative tracking workflows.

## Scale your BOP Form BP-S0243 automation with Anchor Browser

Run your Playwright BOP automations on cloud browsers with enterprise-grade reliability and persistent federal corrections system sessions.

Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
