# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-op-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# FMCSA Form OP-1

> Automate motor carrier operating authority application workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form OP-1 with Playwright

Automate FMCSA motor carrier operating authority application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual registration processes and reduce authority approval delays by automating repetitive FMCSA application workflows. Use Playwright to interact with FMCSA's Unified Registration System programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form OP-1](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/OP-1%20Form.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new OP-1 application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="application_type"]', 'motor_carrier_authority');
await page.selectOption('[name="operation_classification"]', 'passenger_carrier');

// Legal business name
await page.fill('[name="legal_name"]', 'Premier Charter Bus Services Inc');
await page.fill('[name="dba_name"]', 'Premier Coaches');
await page.selectOption('[name="entity_type"]', 'corporation');
await page.fill('[name="state_of_incorporation"]', 'FL');
await page.fill('[name="date_of_incorporation"]', '03/20/2023');

// Tax identification
await page.fill('[name="federal_ein"]', '65-4321987');
await page.selectOption('[name="tax_status"]', 'corporation');

// Principal place of business
await page.fill('[name="business_address"]', '3400 Transportation Boulevard');
await page.fill('[name="business_suite"]', '');
await page.fill('[name="business_city"]', 'Orlando');
await page.selectOption('[name="business_state"]', 'FL');
await page.fill('[name="business_zip"]', '32801');
await page.fill('[name="business_phone"]', '407-555-0164');
await page.fill('[name="business_fax"]', '407-555-0165');
await page.fill('[name="business_email"]', 'info@premiercoaches.com');

// Mailing address
await page.check('[name="mailing_same_as_business"]');

// Ownership information
await page.click('[data-testid="add-officer"]');
await page.fill('[name="officer_name"]', 'Elizabeth Martinez');
await page.fill('[name="officer_title"]', 'President/CEO');
await page.fill('[name="officer_ownership"]', '55');
await page.fill('[name="officer_ssn"]', '456-78-9012');
await page.fill('[name="officer_address"]', '1200 Executive Circle');
await page.fill('[name="officer_city"]', 'Winter Park');
await page.selectOption('[name="officer_state"]', 'FL');
await page.fill('[name="officer_zip"]', '32789');

// Add additional officer
await page.click('[data-testid="add-officer"]');
await page.fill('[name="officer_name_2"]', 'James Rodriguez');
await page.fill('[name="officer_title_2"]', 'Vice President/CFO');
await page.fill('[name="officer_ownership_2"]', '45');
await page.fill('[name="officer_ssn_2"]', '567-89-0123');

// Operating authority requested
await page.check('[name="interstate_authority"]');
await page.selectOption('[name="carrier_type"]', 'passenger');
await page.check('[name="charter_service"]');
await page.check('[name="tour_service"]');
await page.check('[name="special_operations"]');

// Passenger service details
await page.selectOption('[name="service_type"]', 'charter_tour');
await page.fill('[name="passenger_capacity"]', '450');
await page.check('[name="wheelchair_accessible"]');
await page.fill('[name="accessible_vehicles"]', '8');

// Geographic scope
await page.check('[name="48_states"]');
await page.check('[name="canada"]');
await page.selectOption('[name="primary_service_area"]', 'southeast');

// Type of operation
await page.selectOption('[name="operating_status"]', 'new_entrant');
await page.fill('[name="operations_begin_date"]', '05/01/2025');
await page.fill('[name="estimated_annual_mileage"]', '350000');

// Fleet information
await page.fill('[name="motorcoaches_owned"]', '10');
await page.fill('[name="motorcoaches_leased"]', '2');
await page.fill('[name="minibuses_owned"]', '3');
await page.fill('[name="vans_owned"]', '5');
await page.fill('[name="total_seating_capacity"]', '450');
await page.fill('[name="drivers_employed"]', '15');

// Vehicle specifications
await page.fill('[name="average_vehicle_age"]', '3');
await page.fill('[name="newest_vehicle_year"]', '2024');
await page.fill('[name="oldest_vehicle_year"]', '2019');

// MCS-150 mileage information
await page.fill('[name="total_annual_mileage"]', '350000');
await page.fill('[name="vehicle_miles_us"]', '330000');
await page.fill('[name="vehicle_miles_canada"]', '20000');
await page.fill('[name="vehicle_miles_mexico"]', '0');

// Safety management information
await page.fill('[name="safety_director_name"]', 'Michael Safety Director');
await page.fill('[name="safety_director_phone"]', '407-555-0170');
await page.fill('[name="safety_director_email"]', 'safety@premiercoaches.com');
await page.check('[name="drug_testing_program"]');
await page.check('[name="alcohol_testing_program"]');

// Driver qualification files
await page.check('[name="maintains_driver_files"]');
await page.fill('[name="driver_file_location"]', '3400 Transportation Boulevard, Orlando FL 32801');

// Process agent designation
await page.fill('[name="process_agent_name"]', 'Florida Registered Agents LLC');
await page.fill('[name="process_agent_address"]', '678 Legal Plaza');
await page.fill('[name="process_agent_city"]', 'Tallahassee');
await page.selectOption('[name="process_agent_state"]', 'FL');
await page.fill('[name="process_agent_zip"]', '32301');
await page.fill('[name="process_agent_phone"]', '850-555-0188');

// Unified Carrier Registration
await page.check('[name="ucr_participation"]');
await page.selectOption('[name="ucr_tier"]', 'tier_2');
await page.fill('[name="ucr_year"]', '2025');

// Liability insurance
await page.fill('[name="insurance_carrier"]', 'National Transit Insurance Company');
await page.fill('[name="insurance_policy"]', 'NTIC-2025-PC-789456');
await page.fill('[name="liability_coverage"]', '5000000');
await page.fill('[name="insurance_effective_date"]', '05/01/2025');
await page.fill('[name="insurance_agent_name"]', 'Sarah Insurance Agent');
await page.fill('[name="insurance_agent_phone"]', '407-555-0199');

// Additional insurance coverage
await page.check('[name="physical_damage_coverage"]');
await page.fill('[name="physical_damage_amount"]', '2500000');
await page.check('[name="medical_payments"]');
await page.fill('[name="medical_payments_limit"]', '5000');

// USDOT PIN creation
await page.fill('[name="pin_password"]', process.env.USDOT_PIN);
await page.fill('[name="pin_confirm"]', process.env.USDOT_PIN);
await page.fill('[name="security_question_1"]', 'What city were you born in?');
await page.fill('[name="security_answer_1"]', process.env.SECURITY_ANSWER_1);
await page.fill('[name="security_question_2"]', 'What was your first pet\'s name?');
await page.fill('[name="security_answer_2"]', process.env.SECURITY_ANSWER_2);

// Background information
await page.selectOption('[name="prior_authority"]', 'no');
await page.selectOption('[name="revoked_authority"]', 'no');
await page.selectOption('[name="safety_rating"]', 'none');
await page.selectOption('[name="out_of_service"]', 'no');
await page.selectOption('[name="bankruptcy_proceedings"]', 'no');

// Criminal history disclosure
await page.selectOption('[name="felony_convictions"]', 'no');
await page.selectOption('[name="officer_convictions"]', 'no');

// State operating authority
await page.check('[name="state_authority_florida"]');
await page.fill('[name="fl_permit_number"]', 'FL-PC-456789');
await page.check('[name="additional_state_authority"]');
await page.fill('[name="states_authorized"]', 'GA, AL, SC, NC, TN');

// Contact person for application
await page.fill('[name="contact_name"]', 'Elizabeth Martinez');
await page.fill('[name="contact_title"]', 'President/CEO');
await page.fill('[name="contact_phone"]', '407-555-0164');
await page.fill('[name="contact_email"]', 'emartinez@premiercoaches.com');

// Supporting documentation
await page.click('[data-testid="upload-articles-incorporation"]');
await page.setInputFiles('[name="incorporation_documents"]', './documents/articles_of_incorporation.pdf');
await page.click('[data-testid="upload-ein-letter"]');
await page.setInputFiles('[name="ein_verification"]', './documents/irs_ein_letter.pdf');
await page.click('[data-testid="upload-vehicle-list"]');
await page.setInputFiles('[name="fleet_roster"]', './documents/vehicle_inventory.pdf');
await page.click('[data-testid="upload-lease-agreements"]');
await page.setInputFiles('[name="equipment_leases"]', './documents/coach_leases.pdf');

// Certification and signature
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_authority_to_sign"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_fmcsa_regulations"]');
await page.check('[name="acknowledge_safety_fitness"]');
await page.fill('[name="signature_name"]', 'Elizabeth Martinez');
await page.fill('[name="signature_title"]', 'President/CEO');
await page.fill('[name="signature_date"]', '02/10/2025');

// Payment information
await page.selectOption('[name="payment_method"]', 'credit_card');
await page.fill('[name="card_number"]', process.env.PAYMENT_CARD);
await page.fill('[name="card_expiry"]', '11/28');
await page.fill('[name="card_cvv"]', process.env.CARD_CVV);
await page.fill('[name="cardholder_name"]', 'Elizabeth Martinez');
await page.fill('[name="billing_zip"]', '32801');
await page.fill('[name="registration_fee"]', '300');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles fleet validation, insurance verification, and FMCSA submission processes automatically. You can automate new authority applications, passenger carrier registrations, and biennial updates workflows.

## Scale your FMCSA Form OP-1 automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
