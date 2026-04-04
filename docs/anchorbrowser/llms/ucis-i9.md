# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/ucis-i9.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# USCIS Form I-9

> Automate employment eligibility verification workflows with Playwright when APIs aren't available.

# How to Automate USCIS Form I-9 with Playwright

Automate USCIS employment eligibility verification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual onboarding documentation and reduce compliance errors by automating repetitive employee verification processes. Use Playwright to interact with E-Verify and USCIS systems programmatically.

[View USCIS developer resources](https://www.uscis.gov/tools) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [USCIS Form I-9](https://www.uscis.gov/sites/default/files/document/forms/i-9.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to E-Verify system
await page.goto('https://www.e-verify.gov/');
await page.fill('[data-testid="username"]', process.env.EVERIFY_USERNAME);
await page.fill('[data-testid="password"]', process.env.EVERIFY_PASSWORD);
await page.click('[data-testid="login-button"]');

// Start new I-9 form
await page.click('[data-testid="new-case"]');
await page.click('[data-testid="form-i9"]');
await page.selectOption('[name="form_version"]', '11_21_2023');

// Employer information
await page.fill('[name="employer_name"]', 'TechVentures Solutions Inc');
await page.fill('[name="employer_ein"]', '12-3456789');
await page.fill('[name="employer_address"]', '2800 Corporate Drive, Suite 500');
await page.fill('[name="employer_city"]', 'San Jose');
await page.selectOption('[name="employer_state"]', 'CA');
await page.fill('[name="employer_zip"]', '95134');

// Section 1: Employee Information and Attestation
// Employee personal information
await page.fill('[name="last_name"]', 'Rodriguez');
await page.fill('[name="first_name"]', 'Maria');
await page.fill('[name="middle_initial"]', 'C');
await page.fill('[name="other_last_names"]', 'Garcia');

// Address
await page.fill('[name="address"]', '456 Apartment Street, Unit 12B');
await page.fill('[name="city"]', 'San Jose');
await page.selectOption('[name="state"]', 'CA');
await page.fill('[name="zip"]', '95110');

// Date of birth and contact
await page.fill('[name="date_of_birth"]', '07/15/1992');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="email"]', 'maria.rodriguez@email.com');
await page.fill('[name="phone"]', '408-555-0189');

// Citizenship/immigration status
await page.selectOption('[name="citizenship_status"]', 'us_citizen');

// Employee attestation
await page.check('[name="employee_aware_penalties"]');
await page.fill('[name="employee_signature"]', 'Maria C Rodriguez');
await page.fill('[name="employee_signature_date"]', '03/01/2025');

// Preparer/translator (if applicable)
await page.selectOption('[name="preparer_used"]', 'no');

// Section 2: Employer Review and Verification
// Document verification - List A (identity and employment authorization)
await page.selectOption('[name="document_list"]', 'list_a');
await page.selectOption('[name="list_a_document"]', 'us_passport');
await page.fill('[name="document_title"]', 'U.S. Passport');
await page.fill('[name="issuing_authority"]', 'U.S. Department of State');
await page.fill('[name="document_number"]', '123456789');
await page.fill('[name="expiration_date"]', '06/15/2030');

// Alternative: List B and List C documents
// Uncomment if using List B + List C instead of List A
/*
await page.selectOption('[name="document_list"]', 'list_b_and_c');

// List B - Identity document
await page.selectOption('[name="list_b_document"]', 'drivers_license');
await page.fill('[name="list_b_document_title"]', 'Driver\'s License');
await page.fill('[name="list_b_issuing_authority"]', 'California DMV');
await page.fill('[name="list_b_document_number"]', 'D1234567');
await page.fill('[name="list_b_expiration"]', '07/15/2029');

// List C - Employment authorization document
await page.selectOption('[name="list_c_document"]', 'social_security_card');
await page.fill('[name="list_c_document_title"]', 'Social Security Card');
await page.fill('[name="list_c_issuing_authority"]', 'Social Security Administration');
await page.fill('[name="list_c_document_number"]', '123-45-6789');
*/

// Physical examination of documents
await page.check('[name="documents_appear_genuine"]');
await page.check('[name="documents_relate_to_employee"]');
await page.fill('[name="first_day_of_employment"]', '03/15/2025');

// Additional information
await page.fill('[name="employer_business_name"]', 'TechVentures Solutions Inc');
await page.fill('[name="employer_representative_name"]', 'Jennifer HR Manager');
await page.fill('[name="employer_representative_title"]', 'Human Resources Manager');

// Employer certification
await page.check('[name="certify_examination_completed"]');
await page.fill('[name="employer_signature"]', 'Jennifer HR Manager');
await page.fill('[name="employer_signature_date"]', '03/01/2025');

// Section 3: Reverification and Rehires (if applicable)
await page.selectOption('[name="section_3_required"]', 'no');

// E-Verify case creation (if enrolled)
await page.check('[name="create_everify_case"]');
await page.fill('[name="hire_date"]', '03/15/2025');
await page.selectOption('[name="employee_type"]', 'regular_full_time');

// Supporting documentation upload
await page.click('[data-testid="upload-document-front"]');
await page.setInputFiles('[name="document_image_front"]', './documents/passport_photo_page.pdf');
await page.click('[data-testid="upload-document-back"]');
await page.setInputFiles('[name="document_image_back"]', './documents/passport_signature_page.pdf');

// Record retention information
await page.fill('[name="retention_start_date"]', '03/01/2025');
await page.selectOption('[name="storage_location"]', 'secure_digital_system');
await page.fill('[name="retention_period_years"]', '3');

// Remote verification (if applicable)
await page.selectOption('[name="remote_verification"]', 'no');

// Quality assurance review
await page.check('[name="qa_documents_legible"]');
await page.check('[name="qa_dates_consistent"]');
await page.check('[name="qa_sections_complete"]');
await page.check('[name="qa_signatures_present"]');

// Compliance notes
await page.fill('[name="internal_notes"]', 'Employee provided original U.S. passport. Documents examined in person on 3/1/25. All information verified and accurate. E-Verify case will be created upon hire date.');

// Authorized representative information
await page.fill('[name="hr_contact_name"]', 'Jennifer HR Manager');
await page.fill('[name="hr_contact_email"]', 'hr@techventures.com');
await page.fill('[name="hr_contact_phone"]', '408-555-0100');

// Company location for this employee
await page.fill('[name="work_location_address"]', '2800 Corporate Drive, Suite 500');
await page.fill('[name="work_location_city"]', 'San Jose');
await page.selectOption('[name="work_location_state"]', 'CA');
await page.fill('[name="work_location_zip"]', '95134');

// Supervisor information
await page.fill('[name="supervisor_name"]', 'David Engineering Manager');
await page.fill('[name="supervisor_email"]', 'dmanager@techventures.com');
await page.fill('[name="department"]', 'Software Engineering');

// Job title and details
await page.fill('[name="job_title"]', 'Software Engineer II');
await page.fill('[name="employee_id"]', 'EMP-2025-0789');
await page.selectOption('[name="employment_type"]', 'permanent_full_time');
await page.fill('[name="annual_salary"]', '125000');

// Final certification
await page.check('[name="certify_compliance"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_retention_requirements"]');

await page.click('[data-testid="submit-i9"]');

// Download completed form
await page.click('[data-testid="download-i9-pdf"]');

await browser.close();
```

Playwright handles document validation, data verification, and USCIS submission processes automatically. You can automate new hire onboarding, reverification workflows, and compliance audits.

## Scale your USCIS Form I-9 automation with Anchor Browser

Run your Playwright USCIS automations on cloud browsers with enterprise-grade reliability and persistent employment verification sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
