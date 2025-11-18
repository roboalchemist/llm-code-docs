# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-op-1-p.md

# FMCSA Form OP-1(P)

> Automate motor carrier passenger operating authority application workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form OP-1(P) with Playwright

Automate FMCSA passenger carrier operating authority application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual registration processes and reduce authority approval delays by automating repetitive FMCSA application workflows. Use Playwright to interact with FMCSA's Unified Registration System programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form OP-1(P)](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/OP-1%28P%29%20Form.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new OP-1(P) application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="application_type"]', 'passenger_carrier_authority');
await page.selectOption('[name="operation_classification"]', 'for_hire');

// Legal business name
await page.fill('[name="legal_name"]', 'Gateway Freight Systems LLC');
await page.fill('[name="dba_name"]', 'Gateway Express');
await page.selectOption('[name="entity_type"]', 'limited_liability_company');
await page.fill('[name="state_of_formation"]', 'GA');
await page.fill('[name="date_of_formation"]', '01/15/2024');

// Tax identification
await page.fill('[name="federal_ein"]', '58-9876543');
await page.selectOption('[name="tax_status"]', 'corporation');

// Principal place of business
await page.fill('[name="business_address"]', '2500 Commerce Parkway');
await page.fill('[name="business_suite"]', 'Suite 300');
await page.fill('[name="business_city"]', 'Atlanta');
await page.selectOption('[name="business_state"]', 'GA');
await page.fill('[name="business_zip"]', '30339');
await page.fill('[name="business_phone"]', '404-555-0192');
await page.fill('[name="business_fax"]', '404-555-0193');
await page.fill('[name="business_email"]', 'operations@gatewayfreight.com');

// Mailing address (if different)
await page.check('[name="mailing_same_as_business"]');

// Ownership information
await page.click('[data-testid="add-owner"]');
await page.fill('[name="owner_name"]', 'Thomas Anderson');
await page.fill('[name="owner_title"]', 'Managing Member');
await page.fill('[name="owner_percentage"]', '60');
await page.fill('[name="owner_ssn"]', '234-56-7890');
await page.fill('[name="owner_address"]', '789 Executive Drive');
await page.fill('[name="owner_city"]', 'Alpharetta');
await page.selectOption('[name="owner_state"]', 'GA');
await page.fill('[name="owner_zip"]', '30022');

// Add second owner
await page.click('[data-testid="add-owner"]');
await page.fill('[name="owner_name_2"]', 'Patricia Wilson');
await page.fill('[name="owner_title_2"]', 'Member');
await page.fill('[name="owner_percentage_2"]', '40');
await page.fill('[name="owner_ssn_2"]', '345-67-8901');

// Operating authority requested
await page.check('[name="interstate_authority"]');
await page.selectOption('[name="passenger_type"]', 'bus');

// Geographic scope
await page.check('[name="48_states"]');
await page.check('[name="mexico"]');
await page.check('[name="canada"]');

// Cargo carried
await page.check('[name="general_commodities"]');
await page.check('[name="household_goods_carrier"]');
await page.fill('[name="commodity_description"]', 'General freight including consumer goods, electronics, and refrigerated products');

// Type of operation
await page.selectOption('[name="operating_status"]', 'new_entrant');
await page.fill('[name="operations_begin_date"]', '04/01/2025');
await page.fill('[name="estimated_mileage"]', '500000');

// Fleet information
await page.fill('[name="power_units_owned"]', '12');
await page.fill('[name="power_units_term_leased"]', '3');
await page.fill('[name="power_units_trip_leased"]', '0');
await page.fill('[name="trailers_owned"]', '25');
await page.fill('[name="trailers_leased"]', '5');
await page.fill('[name="drivers_employed"]', '18');

// MCS-150 mileage information
await page.fill('[name="total_annual_mileage"]', '500000');
await page.fill('[name="vehicle_miles_us"]', '450000');
await page.fill('[name="vehicle_miles_canada"]', '30000');
await page.fill('[name="vehicle_miles_mexico"]', '20000');

// Safety management information
await page.fill('[name="safety_director_name"]', 'Karen Transportation Manager');
await page.fill('[name="safety_director_phone"]', '404-555-0198');
await page.fill('[name="safety_director_email"]', 'safety@gatewayfreight.com');

// Process agent designation
await page.fill('[name="process_agent_name"]', 'National Registered Agents Inc');
await page.fill('[name="process_agent_address"]', '456 Legal Services Blvd');
await page.fill('[name="process_agent_city"]', 'Atlanta');
await page.selectOption('[name="process_agent_state"]', 'GA');
await page.fill('[name="process_agent_zip"]', '30303');
await page.fill('[name="process_agent_phone"]', '404-555-0177');

// Unified Carrier Registration
await page.check('[name="ucr_participation"]');
await page.selectOption('[name="ucr_tier"]', 'tier_3');
await page.fill('[name="ucr_year"]', '2025');

// Insurance information
await page.fill('[name="insurance_carrier"]', 'Continental Insurance Group');
await page.fill('[name="insurance_policy"]', 'CIG-2025-789123');
await page.fill('[name="insurance_coverage_amount"]', '1000000');
await page.fill('[name="insurance_effective_date"]', '04/01/2025');

// Cargo insurance
await page.fill('[name="cargo_insurance_carrier"]', 'Transport Insurance Services');
await page.fill('[name="cargo_policy_number"]', 'TIS-2025-456789');
await page.fill('[name="cargo_coverage"]', '100000');

// USDOT PIN creation
await page.fill('[name="pin_password"]', process.env.USDOT_PIN);
await page.fill('[name="pin_confirm"]', process.env.USDOT_PIN);
await page.fill('[name="security_question_1"]', 'What is your mother\'s maiden name?');
await page.fill('[name="security_answer_1"]', process.env.SECURITY_ANSWER_1);

// Background information
await page.selectOption('[name="prior_authority"]', 'no');
await page.selectOption('[name="safety_rating"]', 'none');
await page.selectOption('[name="suspended_authority"]', 'no');
await page.selectOption('[name="bankruptcy_proceedings"]', 'no');

// Felony conviction disclosure
await page.selectOption('[name="felony_convictions"]', 'no');

// Contact person for application
await page.fill('[name="contact_name"]', 'Thomas Anderson');
await page.fill('[name="contact_title"]', 'Managing Member');
await page.fill('[name="contact_phone"]', '404-555-0192');
await page.fill('[name="contact_email"]', 'tanderson@gatewayfreight.com');

// Supporting documentation
await page.click('[data-testid="upload-articles-of-organization"]');
await page.setInputFiles('[name="formation_documents"]', './documents/llc_articles.pdf');
await page.click('[data-testid="upload-ein-letter"]');
await page.setInputFiles('[name="ein_verification"]', './documents/irs_ein_letter.pdf');
await page.click('[data-testid="upload-lease-agreements"]');
await page.setInputFiles('[name="equipment_leases"]', './documents/truck_leases.pdf');

// Certification and signature
await page.check('[name="certify_truth"]');
await page.check('[name="certify_authority"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_regulations"]');
await page.fill('[name="signature_name"]', 'Thomas Anderson');
await page.fill('[name="signature_title"]', 'Managing Member');
await page.fill('[name="signature_date"]', '02/05/2025');

// Payment information
await page.selectOption('[name="payment_method"]', 'credit_card');
await page.fill('[name="card_number"]', process.env.PAYMENT_CARD);
await page.fill('[name="card_expiry"]', '12/27');
await page.fill('[name="card_cvv"]', process.env.CARD_CVV);
await page.fill('[name="billing_zip"]', '30339');
await page.fill('[name="registration_fee"]', '300');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles fleet validation, insurance verification, and FMCSA submission processes automatically. You can automate new authority applications, operating authority amendments, and biennial updates workflows.

## Scale your FMCSA Form OP-1(P) automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
