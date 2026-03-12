# Source: https://docs.acceldata.io/documentation/writing-effective-prompts.md

# Writing Effective Prompts

## Prompt Structure

**Basic Formula**

`[Context] + [Specific Request] + [Output Format] `

**Example**

- **Context:** “For the `customer_orders` table”
- **Request:** “show me data quality issues”
- **Format:** “in the last 24 hours”

**Full Prompt:**
 “For the `customer_orders` table, show me data quality issues in the last 24 hours.”

### Components of a Good Prompt

1. **Be Specific**
    - ✓ “Show failed policies for `customer_orders` table”
    - ✗ “Show me some policies”

2. **Provide Context**
    - ✓ “As a data steward reviewing monthly compliance”
    - ✗ [No context provided]

3. **State Your Goal**
    - ✓ “I need to create a report for management”
    - ✗ [Unclear purpose]

4. **Specify Output Format**
    - ✓ “Provide as a table with columns for policy name, failure count, and asset”
    - ✗ [No format specified]

## Context Provision

### Why Context Matters

Context helps ADM:

- Select the right tools and agents
- Adjust tone and depth of responses
- Apply domain-specific knowledge
- Deliver accurate, relevant examples

### Types of Context

**Role Context**

- “As a data engineer maintaining production pipelines…”
- “From a compliance officer’s perspective…”
- “As someone new to data quality…”

**Temporal Context**

- “For Q3 2025…”
- “In the last 24 hours…”
- “Since the last deployment…”

**Scope Context**

- “For all customer-related tables…”
- “Within the finance database…”
- “Across all data sources…”

**Background Context**

- “We recently migrated to cloud storage…”
- “Our policy requires 99% quality…”
- “This is for regulatory reporting…”

## Specificity and Clarity

### Vague vs. Specific

| **Vague** | Specific | 
| ---- | ---- | 
| “Show me policies” | “Show me active data quality policies for production tables.” | 
| “What’s wrong?” | “What data quality issues occurred in the customer database today?” | 
| “Find tables” | “Find tables containing customer PII data.” | 
| “Create a policy” | “Create a data quality policy to validate email formats in the `user_accounts` table.” | 


### Use Concrete Terms

- ✓ “`customer_orders` table” ✗ “that table we use”
- ✓ “last 7 days” ✗ “recently”
- ✓ “policies with &lt; 90% success rate” ✗ “bad policies”

### Avoid Ambiguity

- **Ambiguous:** “Show me the data.”
 _(Which data? Where? When?)_
- **Clear:** “Show me the row count for the `customer_orders` table for each day in the last week.”

## Examples

### Question Answering

- **Poor:** “How’s the data?”
- **Good:** “What is the current data quality score for tables in the customer database?”
- **Best:** “Show me the data quality scores for all tables in the customer database, highlighting any below 95% over the last 30 days.”

### Policy Creation

- **Poor:** “Make a policy.”
- **Good:** “Create a data quality policy for the `orders` table.”
- **Best:** “Create a comprehensive data quality policy for the `orders` table that validates:
    - Order amount is positive and less than $1M
    - Order date is not in the future
    - Customer ID exists in the customer table
    - Status is one of: pending, shipped, delivered, or cancelled”

### Troubleshooting

- **Poor:** “Why did it fail?”
- **Good:** “Why did the `customer_validation` policy fail?”
- **Best:** “The `customer_validation` policy failed at 2 PM today with 450 rows. Analyze the failure pattern and suggest possible causes for the email validation rule failure.”

### Analysis

- **Poor:** “Tell me about problems.”
- **Good:** “What data quality problems exist?”
- **Best:** “Analyze data quality trends for the finance database over the last 30 days. Identify:
    1. Most frequently failing policies
    2. Tables with declining quality scores
    3. New issues that appeared this month
 Provide recommendations for improvement.”