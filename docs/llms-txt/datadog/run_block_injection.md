# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cicd/github/run_block_injection.md

---
title: Run block injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Run block injection
---

# Run block injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `20f14e1a-a899-4e79-9f09-b6a84cd4649b`

**Cloud Provider:** GitHub

**Platform:** CICD

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://securitylab.github.com/research/github-actions-untrusted-input/)

### Description{% #description %}

GitHub Actions workflows can be triggered by a variety of events. Each trigger includes a GitHub context with details about the event, such as the user who triggered it, the branch name, and other relevant information. Some of this data, like the base repository name, changeset hash, or pull request number, is typically not controlled by the user and is unlikely to be used for injection.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
name: check-go-coverage

on:
  pull_request_target:
    branches: [master]

jobs:
  coverage:
    name: Check Go coverage
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Set up Go 1.22.x
        uses: actions/setup-go@v5
        with:
          go-version: 1.22.x
      - name: Run test metrics script
        id: testcov
        run: |
          make test-coverage-report | tee test-results
          echo "coverage=$(cat test-results | grep "Total coverage: " test-results | cut -d ":" -f 2 | bc)" >> $GITHUB_ENV
      - name: Checks if Go coverage is at least 80%
        if: env.coverage < 80
        run: |
          echo "Go coverage is lower than 80%: ${{ env.coverage }}%"
          exit 1
```

```yaml
name: Author Workflow

on:
  author:
    types:
      - created

jobs:
  process_author:
    runs-on: ubuntu-latest
    steps:
      - name: Greet the New Author
        run: |
          echo "Hello, a new author has been created!"
```

```yaml
name: Workflow Run Workflow

on:
  workflow_run:
    workflows:
      - "Your Workflow Name" # Replace with the name of your specific workflow

jobs:
  process_workflow_run:
    runs-on: ubuntu-latest
    steps:
      - name: Greet the New Workflow Run
        run: |
          echo "Hello, a new workflow run has started for 'Your Workflow Name'!"
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
name: Pull Request Workflow

on:
  pull_request_target:
    types:
      - opened

jobs:
  process_pull_request:
    runs-on: ubuntu-latest
    steps:
      - name: Echo Pull Request Body
        run: |
          echo "Pull Request Body: ${{ github.event.pull_request.body }}"
```

```yaml
name: Issue Comment Workflow

on:
  issue_comment:
    types:
      - created

jobs:
  process_issue_comment:
    runs-on: ubuntu-latest
    steps:
      - name: Echo Issue Comment Body
        run: |
          echo "Issue Comment Body: ${{ github.event.comment.body }}"
```

```yaml
name: Discussion Workflow

on:
  discussion:
    types:
      - created

jobs:
  process_discussion:
    runs-on: ubuntu-latest
    steps:
      - name: Echo Discussion Title
        run: |
          echo "Discussion Title: ${{ github.event.discussion.title }}"
```
