# Source: https://docs.crewai.com/en/enterprise/features/pii-trace-redactions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PII Redaction for Traces

> Automatically redact sensitive data from crew and flow execution traces

## Overview

PII Redaction is a CrewAI AMP feature that automatically detects and masks Personally Identifiable Information (PII) in your crew and flow execution traces. This ensures sensitive data like credit card numbers, social security numbers, email addresses, and names are not exposed in your CrewAI AMP traces. You can also create custom recognizers to protect organization-specific data.

<Info>
  PII Redaction is available on the Enterprise plan.
  Deployment must be version 1.8.0 or higher.
</Info>

<Frame>
    <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=dd6cc375c0429fe05581078fcd64878f" alt="PII Redaction Overview" data-og-width="1038" width="1038" data-og-height="580" height="580" data-path="images/enterprise/pii_mask_recognizer_trace_example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=5fc24b6d3400416b72f57dedcb987460 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=ab57a20d789059280a501458d6ffd7f3 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=2c260c300bdde6b43fd03e39bb81e635 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=aa125d159c056933fd60768f23e5daa5 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=7c7cefb75b67d47d1c701b16d2df57df 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_trace_example.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=acc7de582734d8a01417a366c26db5d8 2500w" />
</Frame>

## Why PII Redaction Matters

When running AI agents in production, sensitive information often flows through your crews:

* Customer data from CRM integrations
* Financial information from payment processors
* Personal details from form submissions
* Internal employee data

Without proper redaction, this data appears in traces, making compliance with regulations like GDPR, HIPAA, and PCI-DSS challenging. PII Redaction solves this by automatically masking sensitive data before it's stored in traces.

## How It Works

1. **Detect** - Scan trace event data for known PII patterns
2. **Classify** - Identify the type of sensitive data (credit card, SSN, email, etc.)
3. **Mask/Redact** - Replace the sensitive data with masked values based on your configuration

```
Original: "Contact john.doe@company.com or call 555-123-4567"
Redacted: "Contact <EMAIL_ADDRESS> or call <PHONE_NUMBER>"
```

## Enabling PII Redaction

<Info>
  You must be on the Enterprise plan and your deployment must be version 1.8.0 or higher to use this feature.
</Info>

<Steps>
  <Step title="Navigate to Crew Settings">
    In the CrewAI AMP dashboard, select your deployed crew and go to one of your deployments/automations, then navigate to **Settings** → **PII Protection**.
  </Step>

  <Step title="Enable PII Protection">
    Toggle on **PII Redaction for Traces**. This will enable automatic scanning and redaction of trace data.

    <Info>
      You need to manually enable PII Redaction for each deployment.
    </Info>

    <Frame>
            <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=84bc5f827526a8a3744e46a3bc3a8996" alt="Enable PII Redaction" data-og-width="1804" width="1804" data-og-height="630" height="630" data-path="images/enterprise/pii_mask_recognizer_enable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=9daaa697d15ef6762d4e5a2bfac481fb 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=13e963a83d5b299a946300af0ff02394 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=462eb210318d45df03518772dc38b22a 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=ea222d39bb1e8c33180ef434e589c77a 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=c9ee6df144e4137518943607d95a277e 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_enable.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=45c6f3a7d41342a010b4bbadf0516a97 2500w" />
    </Frame>
  </Step>

  <Step title="Configure Entity Types">
    Select which types of PII to detect and redact. Each entity can be individually enabled or disabled.

    <Frame>
            <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=3ee3c500417adb7376a1099f7edb5456" alt="Configure Entities" data-og-width="1774" width="1774" data-og-height="890" height="890" data-path="images/enterprise/pii_mask_recognizer_supported_entities.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=2756e09744b24a2d1df455e8681c57ef 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=89447827685cfde606532702b71d25a1 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=9e9a992dcd4fb78c710301e7284ed6d9 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=1e68d9d23c2e798580d7f8034969a243 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=3f2cf1d0b4da0c10b93dd7ac8610b3ab 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_supported_entities.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=6fcc66fd685b143677477d712aceeaaa 2500w" />
    </Frame>
  </Step>

  <Step title="Save">
    Save your configuration. PII redaction will be active on all subsequent crew executions, no redeployment is needed.
  </Step>
</Steps>

## Supported Entity Types

CrewAI supports the following PII entity types, organized by category.

### Global Entities

| Entity            | Description                                   | Example                                       |
| ----------------- | --------------------------------------------- | --------------------------------------------- |
| `CREDIT_CARD`     | Credit/debit card numbers                     | "4111-1111-1111-1111"                         |
| `CRYPTO`          | Cryptocurrency wallet addresses               | "bc1qxy2kgd..."                               |
| `DATE_TIME`       | Dates and times                               | "January 15, 2024"                            |
| `EMAIL_ADDRESS`   | Email addresses                               | "[john@example.com](mailto:john@example.com)" |
| `IBAN_CODE`       | International bank account numbers            | "DE89 3704 0044 0532 0130 00"                 |
| `IP_ADDRESS`      | IPv4 and IPv6 addresses                       | "192.168.1.1"                                 |
| `LOCATION`        | Geographic locations                          | "New York City"                               |
| `MEDICAL_LICENSE` | Medical license numbers                       | "MD12345"                                     |
| `NRP`             | Nationalities, religious, or political groups | -                                             |
| `PERSON`          | Personal names                                | "John Doe"                                    |
| `PHONE_NUMBER`    | Phone numbers in various formats              | "+1 (555) 123-4567"                           |
| `URL`             | Web URLs                                      | "[https://example.com](https://example.com)"  |

### US-Specific Entities

| Entity              | Description                 | Example       |
| ------------------- | --------------------------- | ------------- |
| `US_BANK_NUMBER`    | US Bank account numbers     | "1234567890"  |
| `US_DRIVER_LICENSE` | US Driver's license numbers | "D1234567"    |
| `US_ITIN`           | Individual Taxpayer ID      | "900-70-0000" |
| `US_PASSPORT`       | US Passport numbers         | "123456789"   |
| `US_SSN`            | Social Security Numbers     | "123-45-6789" |

## Redaction Actions

For each enabled entity, you can configure how the data is redacted:

| Action   | Description                        | Example Output  |
| -------- | ---------------------------------- | --------------- |
| `mask`   | Replace with the entity type label | `<CREDIT_CARD>` |
| `redact` | Completely remove the text         | *(empty)*       |

## Custom Recognizers

In addition to built-in entities, you can create **custom recognizers** to detect organization-specific PII patterns.

<Frame>
    <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=017cd32c2d856d95476e3137a21b45f2" alt="Custom Recognizers" data-og-width="2760" width="2760" data-og-height="1072" height="1072" data-path="images/enterprise/pii_mask_recognizer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=07e0c2a332f55662d8d69295aa085df3 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=9e0a1bd666c3b970bcfaa1bd24c7fdf2 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=0a605ce619cdcf610cc330be2f3dd75d 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=a446aa8664f0759793a4eb7ebdbfc1ca 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=e575d7639cadc6dcecb2c53000f2ad11 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=9b984d2c77c1b1b20359a7f41dbb215b 2500w" />
</Frame>

### Recognizer Types

You have two options for custom recognizers:

| Type                      | Best For                                 | Example Use Case                                  |
| ------------------------- | ---------------------------------------- | ------------------------------------------------- |
| **Pattern-based (Regex)** | Structured data with predictable formats | Salary amounts, employee IDs, project codes       |
| **Deny-list**             | Exact string matches                     | Company names, internal codenames, specific terms |

### Creating a Custom Recognizer

<Steps>
  <Step title="Navigate to Custom Recognizers">
    Go to your Organization **Settings** → **Organization** → **Add Recognizer**.
  </Step>

  <Step title="Configure the Recognizer">
    <Frame>
            <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=678fd086346d2a12649df04670ae66fe" alt="Configure Recognizer" data-og-width="3680" width="3680" data-og-height="2392" height="2392" data-path="images/enterprise/pii_mask_recognizer_create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=617de34f1d61823d8c5e0786c4e1cdf0 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=656210c857fbbaad4170c8a277efebda 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=4cf824640e706f40f79df2e56ac5795b 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=5e0412157c5fe21fc5c9fd0b7e198c98 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=12fb94ca51adea99cc7bd18bb533a966 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizer_create.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=be8f8c1f27f1305cf0bbc62baeb60385 2500w" />
    </Frame>

    Configure the following fields:

    * **Name**: A descriptive name for the recognizer
    * **Entity Type**: The entity label that will appear in redacted output (e.g., `EMPLOYEE_ID`, `SALARY`)
    * **Type**: Choose between Regex Pattern or Deny List
    * **Pattern/Values**: Regex pattern or list of strings to match
    * **Confidence Threshold**: Minimum score (0.0-1.0) required for a match to trigger redaction. Higher values (e.g., 0.8) reduce false positives but may miss some matches. Lower values (e.g., 0.5) catch more matches but may over-redact. Default is 0.8.
    * **Context Words** (optional): Words that increase detection confidence when found nearby
  </Step>

  <Step title="Save">
    Save the recognizer. It will be available to enable on your deployments.
  </Step>
</Steps>

### Understanding Entity Types

The **Entity Type** determines how matched content appears in redacted traces:

```
Entity Type: SALARY
Pattern: salary:\s*\$\s*\d+
Input: "Employee salary: $50,000"
Output: "Employee <SALARY>"
```

### Using Context Words

Context words improve accuracy by increasing confidence when specific terms appear near the matched pattern:

```
Context Words: "project", "code", "internal"
Entity Type: PROJECT_CODE
Pattern: PRJ-\d{4}
```

When "project" or "code" appears near "PRJ-1234", the recognizer has higher confidence it's a true match, reducing false positives.

## Viewing Redacted Traces

Once PII redaction is enabled, your traces will show redacted values in place of sensitive data:

```
Task Output: "Customer <PERSON> placed order #12345.
Contact email: <EMAIL_ADDRESS>, phone: <PHONE_NUMBER>.
Payment processed for card ending in <CREDIT_CARD>."
```

Redacted values are clearly marked with angle brackets and the entity type label (e.g., `<EMAIL_ADDRESS>`), making it easy to understand what data was protected while still allowing you to debug and monitor crew behavior.

## Best Practices

### Performance Considerations

<Steps>
  <Step title="Enable Only Needed Entities">
    Each enabled entity adds processing overhead. Only enable entities relevant to your data.
  </Step>

  <Step title="Use Specific Patterns">
    For custom recognizers, use specific patterns to reduce false positives and improve performance. Regex patterns are best when identifying specific patterns in the traces such as salary, employee id, project code, etc. Deny-list recognizers are best when identifying exact strings in the traces such as company names, internal codenames, etc.
  </Step>

  <Step title="Leverage Context Words">
    Context words improve accuracy by only triggering detection when surrounding text matches.
  </Step>
</Steps>

## Troubleshooting

<Accordion title="PII Not Being Redacted">
  **Possible Causes:**

  * Entity type not enabled in configuration
  * Pattern doesn't match the data format
  * Custom recognizer has syntax errors

  **Solutions:**

  * Verify entity is enabled in Settings → Security
  * Test regex patterns with sample data
  * Check logs for configuration errors
</Accordion>

<Accordion title="Too Much Data Being Redacted">
  **Possible Causes:**

  * Overly broad entity types enabled (e.g., `DATE_TIME` catches dates everywhere)
  * Custom recognizer patterns are too general

  **Solutions:**

  * Disable entities that cause false positives
  * Make custom patterns more specific
  * Add context words to improve accuracy
</Accordion>

<Accordion title="Performance Issues">
  **Possible Causes:**

  * Too many entities enabled
  * NLP-based entities (`PERSON`, `LOCATION`, `NRP`) are computationally expensive as they use machine learning models

  **Solutions:**

  * Only enable entities you actually need
  * Consider using pattern-based alternatives where possible
  * Monitor trace processing times in the dashboard
</Accordion>

***

## Practical Example: Salary Pattern Matching

This example demonstrates how to create a custom recognizer to detect and mask salary information in your traces.

### Use Case

Your crew processes employee or financial data that includes salary information in formats like:

* `salary: $50,000`
* `salary: $125,000.00`
* `salary:$1,500.50`

You want to automatically mask these values to protect sensitive compensation data.

### Configuration

<Frame>
    <img src="https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=92837ca9a69cb7796ba30635f4c39e4d" alt="Salary Recognizer Configuration" data-og-width="3680" width="3680" data-og-height="2392" height="2392" data-path="images/enterprise/pii_mask_custom_recognizer_salary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=280&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=f096020e8dc34a9830d554d2051b1604 280w, https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=560&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=37fa009b70cc62d889c405b407d0effe 560w, https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=840&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=e6922b37614770c762f97ea36e321ae8 840w, https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=1100&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=8d2b633102bbd7bc1a884fd18a16837d 1100w, https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=1650&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=b45e0fb59c8de4237210fc99bcf98176 1650w, https://mintcdn.com/crewai/jJakCH-Fw6QjaqDk/images/enterprise/pii_mask_custom_recognizer_salary.png?w=2500&fit=max&auto=format&n=jJakCH-Fw6QjaqDk&q=85&s=fe42dfd778f2cc0d12364c3985a5b133 2500w" />
</Frame>

| Field                    | Value                                       |
| ------------------------ | ------------------------------------------- |
| **Name**                 | `SALARY`                                    |
| **Entity Type**          | `SALARY`                                    |
| **Type**                 | Regex Pattern                               |
| **Regex Pattern**        | `salary:\s*\$\s*\d{1,3}(,\d{3})*(\.\d{2})?` |
| **Action**               | Mask                                        |
| **Confidence Threshold** | `0.8`                                       |
| **Context Words**        | `salary, compensation, pay, wage, income`   |

### Regex Pattern Breakdown

| Pattern Component | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| `salary:`         | Matches the literal text "salary:"                           |
| `\s*`             | Matches zero or more whitespace characters                   |
| `\$`              | Matches the dollar sign (escaped)                            |
| `\s*`             | Matches zero or more whitespace characters after \$          |
| `\d{1,3}`         | Matches 1-3 digits (e.g., "1", "50", "125")                  |
| `(,\d{3})*`       | Matches comma-separated thousands (e.g., ",000", ",500,000") |
| `(\.\d{2})?`      | Optionally matches cents (e.g., ".00", ".50")                |

### Example Results

```
Original: "Employee record shows salary: $125,000.00 annually"
Redacted: "Employee record shows <SALARY> annually"

Original: "Base salary:$50,000 with bonus potential"
Redacted: "Base <SALARY> with bonus potential"
```

<Tip>
  Adding context words like "salary", "compensation", "pay", "wage", and "income" helps increase detection confidence when these terms appear near the matched pattern, reducing false positives.
</Tip>

### Enable the Recognizer for Your Deployments

<Warning>
  Creating a custom recognizer at the organization level does not automatically enable it for your deployments. You must manually enable each recognizer for every deployment where you want it applied.
</Warning>

After creating your custom recognizer, enable it for each deployment:

<Steps>
  <Step title="Navigate to Your Deployment">
    Go to your deployment/automation and open **Settings** → **PII Protection**.
  </Step>

  <Step title="Select Custom Recognizers">
    Under **Mask Recognizers**, you'll see your organization-defined recognizers. Check the box next to the recognizers you want to enable.

    <Frame>
            <img src="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=00564c6614b0559df44bae4b4a73f2d5" alt="Enable Custom Recognizer" data-og-width="2034" width="2034" data-og-height="542" height="542" data-path="images/enterprise/pii_mask_recognizers_options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=280&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=8681e5c00652b5b37b5bb07c0dd8b82f 280w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=560&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=c724e7fd6979fdedc2e3bcc53caf9620 560w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=840&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=c6529584d29a0b5504c195f2c3de6418 840w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=1100&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=c7f6882d517b4038e6a1e46af5c1961e 1100w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=1650&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=3e4f119f7597f8ef28cfdb6d90ce186c 1650w, https://mintcdn.com/crewai/rRbIBTp0TLHy1mKJ/images/enterprise/pii_mask_recognizers_options.png?w=2500&fit=max&auto=format&n=rRbIBTp0TLHy1mKJ&q=85&s=fe61d7dae12b6c79fb92a31169d07d0f 2500w" />
    </Frame>
  </Step>

  <Step title="Save Configuration">
    Save your changes. The recognizer will be active on all subsequent executions for this deployment.
  </Step>
</Steps>

<Info>
  Repeat this process for each deployment where you need the custom recognizer. This gives you granular control over which recognizers are active in different environments (e.g., development vs. production).
</Info>
