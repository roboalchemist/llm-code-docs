# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-bmc-40.md

# FMCSA Form BMC-40

> Automate motor carrier surety bond and trust fund filing workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form BMC-40 with Playwright

Automate FMCSA motor carrier surety bond and trust fund filing workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual bond filing processes and reduce operating authority delays by automating repetitive FMCSA compliance workflows. Use Playwright to interact with FMCSA's registration systems programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form BMC-40](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/BMC-40%20Form.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new BMC-40 filing
await page.click('[data-testid="insurance-filing"]');
await page.click('[data-testid="form-bmc-40"]');
await page.selectOption('[name="filing_type"]', 'surety_bond');

// Motor carrier information
await page.fill('[name="legal_name"]', 'Midwest Transport Solutions LLC');
await page.fill('[name="dba_name"]', 'Midwest Express Freight');
await page.fill('[name="usdot_number"]', '3456789');
await page.fill('[name="mc_number"]', 'MC-987654');
await page.fill('[name="federal_ein"]', '45-6789012');

// Principal address
await page.fill('[name="address"]', '1200 Industrial Parkway');
await page.fill('[name="city"]', 'Indianapolis');
await page.selectOption('[name="state"]', 'IN');
await page.fill('[name="zip"]', '46204');
await page.fill('[name="phone"]', '317-555-0187');
await page.fill('[name="email"]', 'compliance@midwesttransport.com');

// Operating authority
await page.selectOption('[name="authority_type"]', 'property_carrier');
await page.check('[name="interstate_authority"]');
await page.fill('[name="effective_date"]', '03/01/2025');

// Surety company information
await page.fill('[name="surety_company"]', 'National Surety Corporation');
await page.fill('[name="surety_code"]', '12345');
await page.fill('[name="surety_address"]', '500 Insurance Plaza');
await page.fill('[name="surety_city"]', 'Chicago');
await page.selectOption('[name="surety_state"]', 'IL');
await page.fill('[name="surety_zip"]', '60601');
await page.fill('[name="surety_phone"]', '312-555-0145');

// Bond details
await page.fill('[name="bond_number"]', 'SB-2025-789456');
await page.fill('[name="bond_amount"]', '75000');
await page.fill('[name="bond_effective_date"]', '03/01/2025');
await page.selectOption('[name="bond_type"]', 'continuous');

// Coverage information
await page.check('[name="cargo_liability"]');
await page.check('[name="auto_liability"]');
await page.fill('[name="cargo_limit"]', '100000');
await page.fill('[name="auto_limit"]', '750000');

// Agent for service of process
await page.fill('[name="agent_name"]', 'Corporate Agents Inc');
await page.fill('[name="agent_address"]', '789 State Street');
await page.fill('[name="agent_city"]', 'Indianapolis');
await page.selectOption('[name="agent_state"]', 'IN');
await page.fill('[name="agent_zip"]', '46201');
await page.fill('[name="agent_phone"]', '317-555-0166');

// Power of attorney information
await page.fill('[name="attorney_in_fact']', 'Robert J. Anderson');
await page.fill('[name="attorney_title"]', 'Authorized Representative');
await page.fill('[name="power_of_attorney_number"]', 'POA-456789');

// Cancellation provisions
await page.selectOption('[name="cancellation_notice_days"]', '30');
await page.check('[name="continuous_until_cancelled"]');

// Claims contact information
await page.fill('[name="claims_contact_name"]', 'Jennifer Claims Manager');
await page.fill('[name="claims_phone"]', '312-555-0199');
await page.fill('[name="claims_email"]', 'claims@nationalsurety.com');
await page.fill('[name="claims_fax"]', '312-555-0200');

// Additional insured parties (if applicable)
await page.click('[data-testid="add-additional-insured"]');
await page.fill('[name="additional_insured_name"]', 'ABC Logistics Partners');
await page.fill('[name="additional_insured_address"]', '234 Commerce Drive');
await page.fill('[name="additional_insured_city"]', 'Fort Wayne');
await page.selectOption('[name="additional_insured_state"]', 'IN');
await page.fill('[name="additional_insured_zip"]', '46802');

// Filing reason
await page.selectOption('[name="filing_reason"]', 'new_authority');
await page.fill('[name="previous_bond_number"]', 'N/A');

// Broker authority (if applicable)
await page.check('[name="broker_authority"]');
await page.fill('[name="broker_bond_amount"]', '75000');
await page.fill('[name="broker_bond_number"]', 'BB-2025-789457');

// Supporting documentation
await page.click('[data-testid="upload-bond-document"]');
await page.setInputFiles('[name="bond_document"]', './documents/surety_bond_original.pdf');
await page.click('[data-testid="upload-power-of-attorney"]');
await page.setInputFiles('[name="poa_document"]', './documents/power_of_attorney.pdf');
await page.click('[data-testid="upload-certificate"]');
await page.setInputFiles('[name="certificate_document"]', './documents/insurance_certificate.pdf');

// Carrier certification
await page.check('[name="certify_financial_responsibility"]');
await page.check('[name="certify_continuous_coverage"]');
await page.check('[name="acknowledge_cancellation_terms"]');
await page.check('[name="certify_accuracy"]');

// Carrier signature
await page.fill('[name="carrier_signature_name"]', 'David Transport Owner');
await page.fill('[name="carrier_signature_title"]', 'President');
await page.fill('[name="carrier_signature_date"]', '02/01/2025');

// Surety company certification
await page.fill('[name="surety_signature_name"]', 'Robert J. Anderson');
await page.fill('[name="surety_signature_title"]', 'Authorized Representative');
await page.fill('[name="surety_signature_date"]', '02/01/2025');
await page.click('[data-testid="submit-filing"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles bond validation, surety verification, and FMCSA submission processes automatically. You can automate new authority filings, bond renewals, and coverage modification workflows.

## Scale your FMCSA Form BMC-40 automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent motor carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
