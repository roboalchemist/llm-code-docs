# Source: https://docs.envzero.com/guides/policies-governance/code-optimizer/fixes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating & Applying Fixes

> Create AI-powered fixes and automated pull requests for infrastructure issues

## Overview

When Code Optimizer detects issues, you can generate AI-powered fixes that are submitted as pull requests for team review.

<Warning>
  **VCS Support**: Pull request creation is currently supported for **GitHub** and **GitHub Enterprise** only. Support for other VCS providers is coming soon.
</Warning>

## Generating a Fix

### Step-by-Step Process

<Steps>
  <Step title="Select an Issue">
    From the Code Optimizer dashboard, click on any **Ongoing** issue to view its details.
  </Step>

  <Step title="Review Issue Details">
    Read the issue description, affected code location, and recommended remediation.
  </Step>

  <Step title="Generate Fix">
    Click **"Generate Fix"** to invoke AI-powered remediation.
  </Step>

  <Step title="Review the Pull Request">
    Code Optimizer creates a PR in your repository.
  </Step>
</Steps>

## Issue Resolution

Issues are marked **Resolved** when:

1. You merge the fix PR
2. Trigger a new scan
3. The issue is no longer detected

**If an issue persists after merging:** The fix may not have fully addressed the root cause. Review the scan results and generate a new fix or address it manually.

## Ignoring Issues

**When to ignore:**

* False positives or scanner errors
* Intentional design decisions that violate standard rules
* Rules that don't apply to your use case
* Low priority issues you're not addressing now

## Next Steps

<CardGroup cols={2}>
  <Card title="Back to Scanning" icon="magnifying-glass" href="/guides/policies-governance/code-optimizer/scanning">
    Learn more about triggering scans
  </Card>

  <Card title="Setup Guide" icon="gear" href="/guides/policies-governance/code-optimizer/setup">
    Configure prerequisites and permissions
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
