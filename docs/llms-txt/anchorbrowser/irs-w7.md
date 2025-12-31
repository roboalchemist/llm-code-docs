# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/irs-w7.md

# IRS Form W-7

> Automate ITIN application workflows with Playwright when APIs aren't available.

# How to Automate IRS Form W-7 with Playwright

Automate IRS Individual Taxpayer Identification Number (ITIN) application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual tax identification processing and reduce approval delays by automating repetitive ITIN application processes. Use Playwright to interact with IRS systems programmatically.

[View IRS developer resources](https://www.irs.gov/e-file-providers/modernized-e-file-program-information) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [IRS Form W-7](https://www.irs.gov/pub/irs-pdf/fw7.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to IRS online system
await page.goto('https://www.irs.gov/forms-instructions);

// Start new W-7 application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="form_type"]', 'w7');

// Reason for applying
await page.selectOption('[name="reason_for_itin"]', 'tax_return_filing');
await page.check('[name="attach_federal_return"]');
await page.selectOption('[name="tax_treaty_exception"]', 'no');

// Applicant information
await page.fill('[name="legal_name_first"]', 'Carlos');
await page.fill('[name="legal_name_middle"]', 'Alberto');
await page.fill('[name="legal_name_last"]', 'Mendoza');

// Name at birth (if different)
await page.selectOption('[name="name_changed"]', 'no');

// Date of birth and place
await page.fill('[name="date_of_birth"]', '05/22/1985');
await page.fill('[name="country_of_birth"]', 'Mexico');
await page.fill('[name="state_province_birth"]', 'Jalisco');
await page.fill('[name="city_birth"]', 'Guadalajara');

// Gender
await page.selectOption('[name="gender"]', 'male');

// Mailing address - foreign
await page.selectOption('[name="address_type"]', 'foreign');
await page.fill('[name="foreign_address_line_1"]', 'Calle Reforma 456');
await page.fill('[name="foreign_address_line_2"]', 'Colonia Centro');
await page.fill('[name="foreign_city"]', 'Guadalajara');
await page.fill('[name="foreign_state_province"]', 'Jalisco');
await page.fill('[name="foreign_postal_code"]', '44100');
await page.selectOption('[name="foreign_country"]', 'Mexico');

// US address (if applicable)
await page.check('[name="has_us_address"]');
await page.fill('[name="us_address']', '789 Temporary Street, Apt 3C');
await page.fill('[name="us_city"]', 'Los Angeles');
await page.selectOption('[name="us_state"]', 'CA');
await page.fill('[name="us_zip"]', '90012');

// Contact information
await page.fill('[name="phone_foreign"]', '+52-33-1234-5678');
await page.fill('[name="phone_us"]', '213-555-0145');
await page.fill('[name="email"]', 'cmendoza@email.com');

// Country of citizenship
await page.selectOption('[name="country_citizenship"]', 'Mexico');

// Foreign tax ID (if applicable)
await page.check('[name="has_foreign_tax_id"]');
await page.fill('[name="foreign_tax_id"]', 'MEMC850522HJ8');
await page.selectOption('[name="foreign_tax_country"]', 'Mexico');

// Visa information
await page.selectOption('[name="visa_type"]', 'h1b');
await page.fill('[name="visa_number"]', 'H1B-2024-123456');
await page.fill('[name="visa_expiration"]', '12/31/2026');

// Entry date to US
await page.fill('[name="us_entry_date"]', '01/15/2024');

// Passport information
await page.fill('[name="passport_number"]', 'G12345678');
await page.selectOption('[name="passport_country"]', 'Mexico');
await page.fill('[name="passport_issue_date"]', '03/10/2019');
await page.fill('[name="passport_expiration']', '03/10/2029');

// Family information
await page.selectOption('[name="marital_status"]', 'married');
await page.fill('[name="spouse_name"]', 'Maria Elena Mendoza');
await page.fill('[name="spouse_ssn_itin"]', 'Not applicable');

// Dependent information (if applicable)
await page.click('[data-testid="add-dependent"]');
await page.fill('[name="dependent_first_name"]', 'Sofia');
await page.fill('[name="dependent_middle_name"]', 'Isabel');
await page.fill('[name="dependent_last_name"]', 'Mendoza');
await page.fill('[name="dependent_dob"]', '08/12/2015');
await page.selectOption('[name="dependent_country_birth"]', 'Mexico');
await page.selectOption('[name="dependent_relationship"]', 'daughter');

// Previous ITIN applications
await page.selectOption('[name="previously_applied"]', 'no');

// Previous SSN applications
await page.selectOption('[name="previously_applied_ssn"]', 'no');

// Tax return information
await page.fill('[name="tax_year"]', '2024');
await page.selectOption('[name="filing_status"]', 'married_filing_jointly');
await page.check('[name="claiming_dependents"]');
await page.fill('[name="number_of_dependents"]', '1');

// Income information
await page.fill('[name="us_source_income"]', 'yes');
await page.fill('[name="employer_name"]', 'Tech Innovations Inc');
await page.fill('[name="employer_ein"]', '12-3456789');
await page.fill('[name="employer_address"]', '500 Silicon Valley Drive');
await page.fill('[name="employer_city"]', 'San Jose');
await page.selectOption('[name="employer_state"]', 'CA');
await page.fill('[name="employer_zip"]', '95110');

// Tax treaty benefits (if applicable)
await page.selectOption('[name="claim_treaty_benefits"]', 'no');

// Acceptance agent information (if used)
await page.selectOption('[name="using_acceptance_agent"]', 'yes');
await page.fill('[name="agent_name"]', 'Global Tax Services LLC');
await page.fill('[name="agent_ein"]', '98-7654321');
await page.fill('[name="agent_address"]', '1200 Financial Plaza, Suite 300');
await page.fill('[name="agent_city"]', 'Los Angeles');
await page.selectOption('[name="agent_state"]', 'CA');
await page.fill('[name="agent_zip"]', '90071');
await page.fill('[name="agent_phone"]', '213-555-0190');

// Agent certification
await page.fill('[name="agent_representative"]', 'Patricia Tax Professional');
await page.fill('[name="agent_caf_number"]', 'CAF-123456');

// Supporting documentation checklist
await page.check('[name="doc_passport"]');
await page.check('[name="doc_birth_certificate"]');
await page.check('[name="doc_visa']');
await page.check('[name="doc_employment_letter"]');
await page.check('[name="doc_tax_return"]');

// Document authentication
await page.selectOption('[name="documents_certified"]', 'acceptance_agent');
await page.fill('[name="certification_date"]', '03/05/2025');

// Upload supporting documents
await page.click('[data-testid="upload-passport"]');
await page.setInputFiles('[name="passport_copy"]', './documents/passport_certified_copy.pdf');
await page.click('[data-testid="upload-birth-certificate"]');
await page.setInputFiles('[name="birth_certificate"]', './documents/birth_certificate_certified.pdf');
await page.click('[data-testid="upload-visa"]');
await page.setInputFiles('[name="visa_document"]', './documents/h1b_visa_copy.pdf');
await page.click('[data-testid="upload-tax-return"]');
await page.setInputFiles('[name="tax_return_copy"]', './documents/2024_form_1040.pdf');

// Signature under penalty of perjury
await page.check('[name="certify_true_correct"]');
await page.check('[name="understand_penalties"]');
await page.check('[name="authorize_disclosure"]');

// Applicant signature
await page.fill('[name="applicant_signature"]', 'Carlos Alberto Mendoza');
await page.fill('[name="signature_date"]', '03/05/2025');

// Delegate signature (if applicable)
await page.fill('[name="delegate_signature"]', 'Patricia Tax Professional');
await page.fill('[name="delegate_pin"]', 'CAF-123456');
await page.fill('[name="delegate_date"]', '03/05/2025');

// Acceptance agent signature
await page.fill('[name="agent_signature"]', 'Patricia Tax Professional');
await page.fill('[name="agent_title"]', 'Certified Acceptance Agent');
await page.fill('[name="agent_signature_date"]', '03/05/2025');

// Application submission details
await page.selectOption('[name="submission_method"]', 'acceptance_agent');
await page.fill('[name="submission_date"]', '03/05/2025');

// Mailing address for ITIN
await page.selectOption('[name="send_itin_to"]', 'us_address');

// Special handling instructions
await page.fill('[name="special_instructions"]', 'Expedited processing requested due to pending tax return deadline. Original documents authenticated by CAA.');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles document verification, identity validation, and IRS submission processes automatically. You can automate ITIN applications, renewal requests, and dependent ITIN workflows.

## Scale your IRS Form W-7 automation with Anchor Browser

Run your Playwright IRS automations on cloud browsers with enterprise-grade reliability and persistent tax system sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
