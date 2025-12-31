# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/owcp-915.md

# OWCP Form 915

> Automate federal workers' compensation claim workflows with Playwright when APIs aren't available.

# How to Automate OWCP Form 915 with Playwright

Automate Department of Labor Office of Workers' Compensation Programs claim submission workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual injury claim processing and reduce approval delays by automating repetitive federal workers' compensation documentation processes. Use Playwright to interact with OWCP systems programmatically.

[View DOL OWCP developer resources](https://www.dol.gov/agencies/owcp) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [OWCP Form 915](https://www.dol.gov/sites/dolgov/files/owcp/dfec/regs/compliance/owcp-915.pdf) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to OWCP system
await page.goto('https://www.dol.gov/agencies/owcp/FECA/regs/compliance/forms');

// Start new OWCP-915 form
await page.click('[data-testid="new-claim"]');
await page.selectOption('[name="form_type"]', 'owcp_915');
await page.selectOption('[name="claim_type"]', 'medical_benefits');

// Employee information
await page.fill('[name="employee_last_name"]', 'Anderson');
await page.fill('[name="employee_first_name"]', 'Robert');
await page.fill('[name="employee_middle_name"]', 'James');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="date_of_birth"]', '04/18/1980');

// Contact information
await page.fill('[name="address"]', '345 Federal Plaza, Apt 7B');
await page.fill('[name="city"]', 'Washington');
await page.selectOption('[name="state"]', 'DC');
await page.fill('[name="zip"]', '20001');
await page.fill('[name="phone_home"]', '202-555-0167');
await page.fill('[name="phone_cell"]', '202-555-0168');
await page.fill('[name="email"]', 'randerson@email.com');

// Employment information
await page.fill('[name="agency_name"]', 'Department of Commerce');
await page.fill('[name="agency_code"]', 'DOC-1300');
await page.fill('[name="employing_office"]', 'Bureau of Economic Analysis');
await page.fill('[name="job_title"]', 'Economic Analyst');
await page.fill('[name="occupation_code"]', 'GS-0110-12');
await page.fill('[name="pay_grade"]', 'GS-12');
await page.fill('[name="step"]', '5');

// Duty station
await page.fill('[name="duty_station_address"]', '4600 Silver Hill Road');
await page.fill('[name="duty_station_city"]', 'Suitland');
await page.selectOption('[name="duty_station_state"]', 'MD');
await page.fill('[name="duty_station_zip"]', '20746');

// Supervisor information
await page.fill('[name="supervisor_name"]', 'Margaret Division Chief');
await page.fill('[name="supervisor_title"]', 'Division Chief');
await page.fill('[name="supervisor_phone"]', '301-555-0145');
await page.fill('[name="supervisor_email"]', 'mdivisionchief@commerce.gov');

// Injury or illness information
await page.fill('[name="injury_date"]', '02/15/2025');
await page.fill('[name="injury_time"]', '10:30 AM');
await page.selectOption('[name="injury_type"]', 'traumatic_injury');
await page.fill('[name="date_disability_began"]', '02/15/2025');

// Location of injury
await page.selectOption('[name="injury_location"]', 'duty_station');
await page.fill('[name="injury_specific_location"]', 'Third floor office, Room 315');

// Nature of injury
await page.selectOption('[name="injury_category"]', 'strain_sprain');
await page.selectOption('[name="body_part"]', 'lower_back');
await page.fill('[name="injury_description"]', 'Lower back strain while lifting heavy box of documents from floor to desk. Immediate sharp pain in lumbar region.');

// How injury occurred
await page.fill('[name="injury_circumstances"]', 'Employee was retrieving archived files from storage boxes. Lifted approximately 40-pound box using improper technique. Felt immediate pain and muscle spasm in lower back. Unable to continue work duties.');

// Witnesses
await page.click('[data-testid="add-witness"]');
await page.fill('[name="witness_name_1"]', 'David Colleague');
await page.fill('[name="witness_phone_1"]', '301-555-0178');
await page.fill('[name="witness_email_1"]', 'dcolleague@commerce.gov');

// Medical treatment information
await page.selectOption('[name="medical_treatment_received"]', 'yes');
await page.fill('[name="first_treatment_date"]', '02/15/2025');
await page.selectOption('[name="treatment_type"]', 'emergency_room');

// Medical facility information
await page.fill('[name="facility_name"]', 'Prince George\'s Hospital Center');
await page.fill('[name="facility_address"]', '3001 Hospital Drive');
await page.fill('[name="facility_city"]', 'Cheverly');
await page.selectOption('[name="facility_state"]', 'MD');
await page.fill('[name="facility_zip"]', '20785');
await page.fill('[name="facility_phone"]', '301-555-0200');

// Attending physician
await page.fill('[name="physician_name"]', 'Dr. Sarah Emergency Physician');
await page.fill('[name="physician_specialty"]', 'Emergency Medicine');
await page.fill('[name="physician_phone"]', '301-555-0201');

// Diagnosis and treatment
await page.fill('[name="diagnosis"]', 'Acute lumbar strain, L4-L5 region');
await page.fill('[name="treatment_provided"]', 'Physical examination, X-rays, pain medication, muscle relaxants, ice therapy, ergonomic counseling');

// Work status
await page.selectOption('[name="return_to_work_status"]', 'limited_duty');
await page.fill('[name="work_restrictions']', 'No lifting over 10 pounds, no bending or twisting, frequent position changes, ergonomic chair required');
await page.fill('[name="estimated_return_date"]', '03/15/2025');

// Time loss information
await page.selectOption('[name="time_lost"]', 'yes');
await page.fill('[name="first_day_missed"]', '02/16/2025');
await page.fill('[name="total_days_lost"]', '5');
await page.fill('[name="work_hours_per_day"]', '8');

// Continuation of pay (COP) election
await page.check('[name="elect_cop"]');
await page.fill('[name="cop_start_date"]', '02/16/2025');
await page.fill('[name="cop_days_requested"]', '45');

// Leave usage
await page.check('[name="used_leave"]');
await page.selectOption('[name="leave_type"]', 'sick_leave');
await page.fill('[name="leave_hours"]', '40');
await page.fill('[name="leave_dates"]', '02/16/2025 - 02/20/2025');

// Claim for compensation
await page.selectOption('[name="claim_type_detail"]', 'medical_expenses');
await page.check('[name="claim_wage_loss"]');
await page.check('[name="claim_schedule_award"]');

// Medical expenses claimed
await page.fill('[name="emergency_room_cost"]', '850');
await page.fill('[name="physician_fees"]', '350');
await page.fill('[name="xray_cost"]', '275');
await page.fill('[name="medication_cost"]', '125');
await page.fill('[name="total_medical_expenses"]', '1600');

// Previous injuries or conditions
await page.selectOption('[name="prior_back_injury"]', 'no');
await page.selectOption('[name="preexisting_condition"]', 'no');

// Third party liability
await page.selectOption('[name="third_party_liability"]', 'no');

// Safety equipment
await page.selectOption('[name="safety_equipment_available"]', 'not_applicable');

// Accident investigation
await page.check('[name="supervisor_notified"]');
await page.fill('[name="notification_date"]', '02/15/2025');
await page.fill('[name="notification_time"]', '10:45 AM');
await page.check('[name="incident_report_filed"]');
await page.fill('[name="incident_report_number"]', 'IR-2025-0234');

// Supporting documentation
await page.click('[data-testid="upload-medical-report"]');
await page.setInputFiles('[name="medical_documentation"]', './documents/er_report.pdf');
await page.click('[data-testid="upload-xray"]');
await page.setInputFiles('[name="diagnostic_imaging"]', './documents/lumbar_xray_report.pdf');
await page.click('[data-testid="upload-receipts"]');
await page.setInputFiles('[name="expense_receipts"]', './documents/medical_receipts.pdf');
await page.click('[data-testid="upload-incident-report"]');
await page.setInputFiles('[name="incident_documentation"]', './documents/supervisor_incident_report.pdf');

// Employee statement
await page.fill('[name="employee_statement"]', 'I was performing routine work duties retrieving archived files when injury occurred. I have consistently followed all safety protocols. The injury was purely accidental and occurred in the normal course of my federal employment.');

// Employee certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_work_related"]');
await page.check('[name="understand_penalties"]');
await page.check('[name="authorize_medical_disclosure"]');

// Employee signature
await page.fill('[name="employee_signature"]', 'Robert James Anderson');
await page.fill('[name="employee_signature_date"]', '02/20/2025');

// Supervisor section
await page.selectOption('[name="supervisor_agrees"]', 'agree');
await page.fill('[name="supervisor_comments"]', 'Employee injury confirmed. Witnessed by coworker. Employee followed reporting procedures. Limited duty assignment available upon medical clearance.');

// Supervisor verification
await page.check('[name="injury_occurred_on_duty"]');
await page.check('[name="employee_good_standing"]');
await page.fill('[name="supervisor_signature"]', 'Margaret Division Chief');
await page.fill('[name="supervisor_signature_date"]', '02/21/2025');

// Agency action
await page.selectOption('[name="cop_approved"]', 'yes');
await page.fill('[name="cop_approval_date"]', '02/21/2025');
await page.fill('[name="agency_case_number"]', 'DOC-WC-2025-0456');

// Personnel office contact
await page.fill('[name="hr_contact_name"]', 'Patricia Personnel Specialist');
await page.fill('[name="hr_contact_phone"]', '301-555-0150');
await page.fill('[name="hr_contact_email"]', 'hr.benefits@commerce.gov');

await page.click('[data-testid="submit-claim"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles injury documentation, medical verification, and OWCP submission processes automatically. You can automate claim filings, status tracking, and medical reimbursement workflows.

## Scale your OWCP Form 915 automation with Anchor Browser

Run your Playwright OWCP automations on cloud browsers with enterprise-grade reliability and persistent workers' compensation system sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
