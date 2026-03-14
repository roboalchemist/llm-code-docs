# Source: https://docs.acceldata.io/documentation/data-quality-management.md

# Data Quality Management

## Using ADM for Policy Creation

### Workflow Best Practices

#### Before Starting

- Review the table schema.
- Understand applicable business rules.
- Identify critical data elements.
- Define acceptable thresholds.
- Plan your notification and escalation strategy.

#### During Creation

- Use clear, descriptive language.
- Provide examples where possible.
- Review AI-generated rules carefully.
- Test rules before deployment.
- Add a business explanation for each rule.

#### After Creation

- Verify that the policy appears correctly in ADOC.
- Run an initial execution to validate behavior.
- Review results and investigate anomalies.
- Adjust thresholds or logic if needed.
- Document the purpose and owner of the policy.

### Example Policy Creation Workflow

**Step 1: Initial Request**

> “Create a data quality policy for the `customer_email` table to ensure:
> 
> - Email addresses are valid
> - No duplicates exist
> - All records contain email values
> - Email domain is from an approved list”

**Step 2: Review the Generated Policy**

- Validate each rule’s logic.
- Adjust thresholds (e.g., 95% → 98%).
- Add custom validation logic if required.
- Include a business rationale for transparency.

**Step 3: Test and Deploy**

- Save the policy configuration.
- Run the policy manually.
- Review the first execution results.
- Fine-tune rules and thresholds as necessary.

## Policy Validation

### Testing Generated Policies

#### Before Deployment

- Review the logic behind each rule.
- Validate threshold appropriateness.
- Check generated SQL syntax.
- Test the policy on sample data.
- Confirm notification and alert configurations.

#### Validation Checklist

- Rule names are descriptive
- Business explanations are clear
- Thresholds reflect requirements
- SQL syntax is valid (if applicable)
- Assets are correctly mapped
- Scheduling is configured properly
- Notifications and severity levels are set

### Common Issues to Check

#### Threshold Problems

| **Incorrect** | **Correct** | 
| ---- | ---- | 
| Threshold: 100% for optional fields | Threshold: 100% for mandatory fields only | 
| Threshold: 50% for critical validations | Threshold: 95%+ for critical validations | 


#### Rule Logic Issues

| **Incorrect** | **Correct** | 
| ---- | ---- | 
| Email regex: `^.*@.*$` (too permissive) | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | 
| Date range: `date < '2025-01-01'` (hardcoded) | `date <= CURRENT_DATE` | 


#### Performance Considerations

- Avoid complex joins in validation SQL.
- Use indexed columns where possible.
- Apply sampling for large datasets.
- Set realistic timeouts for long-running validations.

## Understanding Policy Scores

### What Is a Policy Score?

A **policy score** measures the overall health of data quality.

**Formula:**

> Policy Score = (Passed Rules ÷ Total Rules) × 100

### Score Ranges

| **Date** | **Score** | **Status** | 
| ---- | ---- | ---- | 
| Oct 1 | 98% | ✓ Stable | 
| Oct 2 | 97% | ✓ Stable | 
| Oct 3 | 89% | ⚠ Declining | 
| Oct 4 | 85% | ⚠ Declining | 
| Oct 5 | 82% | ❌ Alert | 


### Interpreting Scores

#### High Scores (95–100%)

- Data meets established standards.
- Minor deviations are acceptable.
- Continue monitoring and review thresholds periodically.

#### Medium Scores (85–94%)

- Some rules fail regularly.
- Investigate root causes and pipeline logic.
- Adjust thresholds or improve upstream data quality.

#### Low Scores (&lt; 85%)

- Significant quality degradation.
- Requires immediate investigation and remediation.
- Review pipelines, validation logic, and data sources.

### Example Trend Analysis

**Trend Insights**

- A declining score indicates new issues emerging.
- Sudden drops suggest pipeline or ingestion failures.
- Gradual declines point to schema drift or process regression.
- Stable trends confirm data reliability.

### Example ADM Interaction

**You:** “Why did the customer policy score drop to 85%?”
 **ADM:**
 **Analysis of Decline:**

1. **Email validation rule** pass rate dropped (15% → 8%)
    - Cause: New data source with inconsistent format.

2. **Completeness check** fell (100% → 92%)
    - Cause: Missing phone numbers in latest records.

3. **Uniqueness rule** remained stable (100%).

**Recommendations:**

- Add email normalization to ETL.
- Enforce phone number collection or adjust rule priority.
- Monitor for three days to confirm stability.

## Troubleshooting Policy Issues

### 1. Policy Not Executing

**Symptoms**

- No execution history
- Status shows “Not Scheduled”
- No output results

**Solutions**

- Confirm the schedule is enabled.
- Check execution permissions.
- Verify notification group configuration.
- Confirm access to the target asset.

**ADM Query:**

> “Why hasn’t the `customer_validation` policy executed today?”

### 2. All Rules Failing

**Symptoms**

- All rules show 0% pass rate.
- Policy score = 0%.
- Error messages in execution logs.

**Solutions**

- Check database connectivity.
- Verify table and column references.
- Review SQL syntax in custom rules.
- Confirm user or service permissions.

**ADM Query:**

> “Analyze the failure pattern for `customer_validation` policy and identify common causes.”

### 3. False Positives

**Symptoms**

- Rules fail though data looks correct.
- Inconsistent results between runs.
- Thresholds appear too strict.

**Solutions**

- Revisit rule logic and thresholds.
- Add exception handling conditions.
- Refine validation criteria for special cases.

**ADM Query:**

> “Show me records failing the email validation rule to verify whether they’re actually invalid.”

### 4. Performance Issues

**Symptoms**

- Policy execution takes excessive time.
- Timeout or resource exhaustion errors.

**Solutions**

- Optimize SQL and reduce joins.
- Use sample-based validation for large tables.
- Add indexes to frequently validated columns.
- Break the policy into smaller, targeted ones.

**ADM Query:**

> “Suggest optimizations for the `customer_validation` policy that’s taking over two hours to execute.”