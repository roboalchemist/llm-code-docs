# Source: https://docs.firehydrant.com/docs/runbook-step-add-a-retrospective.md

# Add a Retrospective

<Image align="center" width="650px" src="https://files.readme.io/f8fff269459e6993686a5e8a9cf2d9f24568f65add7ecdcfab85ef5248452540-CleanShot_2025-01-15_at_16.46.43.png" />

FireHydrant's new Retrospective experience allows attaching one or more [Retrospective Templates](https://docs.firehydrant.com/docs/retrospective-templates) to an incident via Runbooks. This allows maximum flexibility in determining which incidents should have which templates.

## Prerequisites

Ensure you have at least one Retrospective template. Once the feature exits beta and GAs, all existing Retro questions and configurations will automatically be inserted/backfilled into a "Default Template" for all customers.

## Configuration

1. Navigate to a Runbook and click "Add step."
2. Search for this Runbook step or find it under the FireHydrant dropdown and click on it.
3. Modify the **Name** of the step if desired and then select the Retrospective Template that should be added to incidents for this particular Runbook.
4. On the next tab, configure any trigger conditions if desired.
5. Click "Add step" and then remember to save the Runbook to persist changes.

## Best Practices

Generally speaking, you can manually attach Retrospective templates to incidents after the fact, so the Runbook step isn't strictly necessary. However, it's best practice to think about and automate this beforehand so you don't have to make the decision manually.

Also, when automated with Runbooks, you have access to the full library of different conditions and triggers. This allows powerful automation such as:

* Attach both internal and external-facing retro templates if it's a particular severity
* Attach Retro Template B if this incident involves Service B
* ...etc.

Experiment and find ways to make FireHydrant work for you and your team!

### Example conditions

You can automatically attach specific retrospective templates based on:

#### Severity-based

```
Severity = SEV-1 or SEV-2
 Attach "Critical Incident Retrospective Template"
```

#### Customer Impact

```
Customer Impact > 1000 users
Attach "Major Customer Impact Template"
```

#### Duration-based

```
Incident Duration > 2 hours
Attach "Extended Incident Analysis Template"
```

#### Service-specific

```
Affected Service = "Payment Processing"
Attach "Financial Services Retrospective"
```

#### Team-based

```
Responding Team = "Infrastructure"
Attach "Infrastructure Post-Mortem Template"
```

#### Multiple Conditions

```
Severity = SEV-1 AND Duration > 1 hour AND Customer Impact = True
Attach "Critical Customer Impact Review Template"
```