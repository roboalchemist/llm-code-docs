# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cicd/github/script_block_injection.md

---
title: Script block injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Script block injection
---

# Script block injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `62ff6823-927a-427f-acf9-f1ea2932d616`

**Cloud Provider:** GitHub

**Platform:** CICD

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://securitylab.github.com/research/github-actions-untrusted-input/)

### Description{% #description %}

GitHub Actions workflows can be triggered by a variety of events. Each trigger includes a GitHub context with details about the event, such as the user who triggered it, the branch name, and other relevant information. Some of this data, like the base repository name, changeset hash, or pull request number, is typically not controlled by the user and is unlikely to be used for injection.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
name: test-script-run

on:
  issues:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```

```yaml
name: test-script-run

on:
  workflow_run:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```

```yaml
name: test-script-run

on:
  author:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
name: test-script-run

on:
  pull_request_target:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync('/tmp/${{ github.event.pull_request.title }}.txt', {encoding: 'utf8'});

            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```

```yaml
name: test-script-run

on:
  issue_comment:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync('/tmp/${{ github.event.issue.title }}.txt', {encoding: 'utf8'});

            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```

```yaml
name: test-script-run

on:
  discussion:
    types: [opened]

jobs:
  script-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run script
        uses: actions/github-script@latest
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync('/tmp/${{ github.event.discussion.title }}.txt', {encoding: 'utf8'});

            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for reporting!'
            })

            return true;
```
