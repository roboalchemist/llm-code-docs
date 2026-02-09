# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/form-122a-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Form 122A-1

> Automate Chapter 7 bankruptcy means test and income statement workflows with Playwright when APIs aren't available.

# How to Automate Form 122A-1 with Playwright

Automate Chapter 7 bankruptcy means test and current monthly income statement workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual income calculation errors and reduce case filing delays by automating repetitive bankruptcy documentation processes. Use Playwright to interact with PACER and bankruptcy court systems programmatically.

[View PACER developer resources](https://pacer.uscourts.gov/file-case/developer-resources) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash  theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [Form 122A-1](https://www.uscourts.gov/file/26712/download) tasks:

```JavaScript  theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to US Federal Courts system
await page.goto('https://www.uscourts.gov/forms-rules/forms');

// Start new Form 122A-1
await page.click('[data-testid="bankruptcy-filing"]');
await page.click('[data-testid="form-122a-1"]');
await page.selectOption('[name="case_chapter"]', 'chapter_7');

// Debtor information
await page.fill('[name="debtor_first_name"]', 'Christopher');
await page.fill('[name="debtor_middle_name"]', 'Daniel');
await page.fill('[name="debtor_last_name"]', 'Peterson');
await page.fill('[name="ssn_last_4"]', '6789');
await page.fill('[name="case_number"]', '25-10234');

// Court information
await page.selectOption('[name="district"]', 'eastern_michigan');
await page.selectOption('[name="division"]', 'detroit');

// Joint debtor (if applicable)
await page.check('[name="joint_case"]');
await page.fill('[name="joint_first_name"]', 'Amanda');
await page.fill('[name="joint_middle_name"]', 'Lynn');
await page.fill('[name="joint_last_name"]', 'Peterson');
await page.fill('[name="joint_ssn_last_4"]', '4321');

// Marital and household status
await page.selectOption('[name="marital_status"]', 'married');
await page.fill('[name="household_size"]', '4');
await page.fill('[name="dependents"]', '2');
await page.fill('[name="dependent_ages"]', '8, 12');

// Employment status - Debtor
await page.selectOption('[name="debtor_employment"]', 'employed');
await page.fill('[name="debtor_employer"]', 'Metro Manufacturing Inc');
await page.fill('[name="debtor_occupation"]', 'Production Supervisor');
await page.fill('[name="debtor_employment_start"]', '03/2019');

// Employment status - Spouse
await page.selectOption('[name="spouse_employment"]', 'employed');
await page.fill('[name="spouse_employer"]', 'Community Hospital');
await page.fill('[name="spouse_occupation"]', 'Registered Nurse');
await page.fill('[name="spouse_employment_start"]', '06/2018');

// Part 1: Calculate Your Current Monthly Income
// Income from employment (6-month average)
await page.fill('[name="debtor_gross_month_1"]', '4200');
await page.fill('[name="debtor_gross_month_2"]', '4200');
await page.fill('[name="debtor_gross_month_3"]', '4200');
await page.fill('[name="debtor_gross_month_4"]', '4350');
await page.fill('[name="debtor_gross_month_5"]', '4200');
await page.fill('[name="debtor_gross_month_6"]', '4200');

await page.fill('[name="spouse_gross_month_1"]', '5100');
await page.fill('[name="spouse_gross_month_2"]', '5400');
await page.fill('[name="spouse_gross_month_3"]', '5100');
await page.fill('[name="spouse_gross_month_4"]', '5100');
await page.fill('[name="spouse_gross_month_5"]', '5250');
await page.fill('[name="spouse_gross_month_6"]', '5100');

// Business income (if applicable)
await page.selectOption('[name="operates_business"]', 'no');
await page.fill('[name="business_gross_income"]', '0');
await page.fill('[name="business_expenses"]', '0');

// Rental and real property income
await page.check('[name="rental_income_exists"]');
await page.fill('[name="rental_gross_receipts"]', '1200');
await page.fill('[name="rental_ordinary_expenses"]', '850');
await page.fill('[name="rental_net_income"]', '350');

// Interest, dividends, and royalties
await page.fill('[name="interest_income"]', '15');
await page.fill('[name="dividend_income"]', '0');
await page.fill('[name="royalty_income"]', '0');

// Pension and retirement income
await page.fill('[name="pension_income"]', '0');
await page.fill('[name="401k_withdrawals"]', '0');
await page.fill('[name="social_security"]', '0');

// Other monthly income
await page.fill('[name="unemployment_compensation"]', '0');
await page.fill('[name="workers_compensation"]', '0');
await page.fill('[name="child_support_received"]', '0');
await page.fill('[name="alimony_received"]', '0');
await page.fill('[name="other_income"]', '0');

// Income from all sources (calculated automatically)
await page.fill('[name="total_monthly_income"]', '9630');
await page.fill('[name="annual_income']', '115560');

// Part 2: Determine Whether the Presumption of Abuse Applies
// Median family income comparison
await page.selectOption('[name="state_of_residence"]', 'MI');
await page.fill('[name="household_size_means_test"]', '4');
await page.fill('[name="applicable_median_income"]', '106847');

// Marital adjustment deductions
await page.check('[name="non_filing_spouse_income"]');
await page.fill('[name="spouse_income_not_contributed"]', '850');
await page.fill('[name="spouse_separate_debt_payments"]', '0');

// Calculate current monthly income for means test
await page.fill('[name="cmi_total"]', '8780');
await page.fill('[name="annualized_cmi"]', '105360');

// Compare to median income
await page.check('[name="income_below_median"]');

// Presumption determination
await page.selectOption('[name="presumption_result"]', 'does_not_arise');

// Additional information
await page.fill('[name="calculation_period_start"]', '08/01/2024');
await page.fill('[name="calculation_period_end"]', '01/31/2025');

// Income fluctuation explanation
await page.fill('[name="income_changes_explanation"]', 'Spouse received overtime pay in December 2024 for holiday coverage. Rental property tenant moved in during calculation period.');

// Excluded income (if applicable)
await page.selectOption('[name="excluded_income_exists"]', 'yes');
await page.fill('[name="excluded_income_type"]', 'Social Security benefits for minor child');
await page.fill('[name="excluded_income_amount"]', '685');

// Non-filing spouse contribution
await page.fill('[name="spouse_household_contribution"]', '4250');
await page.fill('[name="spouse_separate_household_expenses"]', '850');

// Special circumstances (if any)
await page.selectOption('[name="special_circumstances"]', 'no');

// Attorney information
await page.check('[name="represented_by_attorney"]');
await page.fill('[name="attorney_name"]', 'Patricia Morrison');
await page.fill('[name="attorney_bar_number"]', 'MI-P67890');
await page.fill('[name="attorney_firm"]', 'Morrison Bankruptcy Law PLLC');
await page.fill('[name="attorney_address"]', '1500 Woodward Avenue, Suite 800');
await page.fill('[name="attorney_city"]', 'Detroit');
await page.selectOption('[name="attorney_state"]', 'MI');
await page.fill('[name="attorney_zip"]', '48226');
await page.fill('[name="attorney_phone"]', '313-555-0145');

// Supporting documentation
await page.click('[data-testid="upload-pay-stubs"]');
await page.setInputFiles('[name="income_verification"]', './documents/paystubs_6months.pdf');
await page.click('[data-testid="upload-tax-returns"]');
await page.setInputFiles('[name="tax_documents"]', './documents/2024_tax_return.pdf');
await page.click('[data-testid="upload-rental-statements"]');
await page.setInputFiles('[name="rental_documentation"]', './documents/rental_income_statements.pdf');

// Certification under penalty of perjury
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_complete"]');
await page.check('[name="understand_penalties"]');

// Debtor signature
await page.fill('[name="debtor_signature"]', 'Christopher Daniel Peterson');
await page.fill('[name="debtor_signature_date"]', '02/15/2025');

// Joint debtor signature
await page.fill('[name="joint_debtor_signature"]', 'Amanda Lynn Peterson');
await page.fill('[name="joint_debtor_signature_date"]', '02/15/2025');

// Attorney certification
await page.fill('[name="attorney_signature"]', 'Patricia Morrison');
await page.fill('[name="attorney_signature_date"]', '02/15/2025');
await page.click('[data-testid="submit-form"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles income calculations, median income comparisons, and bankruptcy court submission processes automatically. You can automate means test filings, income statement updates, and case documentation workflows.

## Scale your Form 122A-1 automation with Anchor Browser

Run your Playwright bankruptcy court automations on cloud browsers with enterprise-grade reliability and persistent PACER sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
