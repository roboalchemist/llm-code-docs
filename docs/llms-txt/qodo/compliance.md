# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/compliance.md

# Compliance

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The `compliance` tool performs comprehensive compliance checks on PR code changes, validating them against security standards, ticket requirements, and custom organizational compliance checklists, thereby helping teams, enterprises, and agents maintain consistent code quality and security practices while ensuring that development work aligns with business requirements.

{% tabs %}
{% tab title="Fully Compliant" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FqVXTFY3kzHck1rjqfG4w%2Fimage.png?alt=media&#x26;token=d7896610-5bf3-4eb8-a86c-d7f5230278a5" alt="" width="364"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Partially Compliant" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FigdbEkRuzFxeL56b8YpQ%2Fimage.png?alt=media&#x26;token=633c7c7c-be1f-45fc-9c95-5809d2046a52" alt="" width="356"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

***

## Example Usage <a href="#example-usage" id="example-usage"></a>

### Manual Triggering <a href="#manual-triggering" id="manual-triggering"></a>

Invoke the tool manually by commenting `/compliance` on any PR. The compliance results are presented in a comprehensive table:

To edit [configurations](https://qodo-merge-docs.qodo.ai/tools/compliance/#configuration-options) related to the `compliance` tool, use the following template:

```
/compliance --pr_compliance.some_config1=... --pr_compliance.some_config2=...
```

For example, you can enable ticket compliance labels by running:

```
/compliance --pr_compliance.enable_ticket_labels=true
```

### Automatic Triggering <a href="#automatic-triggering" id="automatic-triggering"></a>

The tool can be triggered automatically every time a new PR is opened, or in a push event to an existing PR.

To run the `compliance` tool automatically when a PR is opened, define the following in the configuration file:

```toml
[github_app]  # for example
pr_commands = [
    "/compliance",
    ...
]
```

***

## Compliance Categories <a href="#compliance-categories" id="compliance-categories"></a>

The compliance tool evaluates three main categories:

### 1. Security Compliance <a href="#id-1-security-compliance" id="id-1-security-compliance"></a>

Scans for security vulnerabilities and potential exploits in the PR code changes:

* **Verified Security Concerns** 🔴: Clear security vulnerabilities that require immediate attention
* **Possible Security Risks** ⚪: Potential security issues that need human verification
* **No Security Concerns** 🟢: No security vulnerabilities detected

Examples of security issues:

* Exposure of sensitive information (API keys, passwords, secrets)
* SQL injection vulnerabilities
* Cross-site scripting (XSS) risks
* Cross-site request forgery (CSRF) vulnerabilities
* Insecure data handling patterns

### 2. Ticket Compliance <a href="#id-2-ticket-compliance" id="id-2-ticket-compliance"></a>

{% hint style="info" %}

### How to set up ticket compliance

[Follow the guide on how to set up ticket compliance with Qodo Git interface.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations)
{% endhint %}

{% hint style="info" %}

### Auto-create ticket

[Follow this guide](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/pr-to-ticket) to learn how to enable triggering `create tickets` based on PR content.

![ticket creation via compliance tool](https://codium.ai/images/pr_agent/ticket_creation_from_compliance1.png)
{% endhint %}

Validates that PR changes fulfill the requirements specified in linked tickets:

* **Fully Compliant** 🟢: All ticket requirements are satisfied
* **Partially Compliant** 🟡: Some requirements are met, others need attention
* **Not Compliant** 🔴: Clear violations of ticket requirements
* **Requires Verification** ⚪: Requirements that need human review

### 3. RAG Code Duplication Compliance <a href="#id-3-rag-code-duplication-compliance" id="id-3-rag-code-duplication-compliance"></a>

[Analyzes code changes using RAG endpoint](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/qodo-aware-rag) to detect potential code duplication from the codebase:

* **Fully Compliant** 🟢: No code duplication found
* **Not Compliant** 🔴: Full code duplication found
* **Requires Verification** ⚪: Near code duplication

### 4. [Custom Compliance](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/custom-compliance) <a href="#id-4-custom-compliance" id="id-4-custom-compliance"></a>

Validates against an organization-specific compliance checklist:

* **Fully Compliant** 🟢: All custom compliance are satisfied
* **Not Compliant** 🔴: Violations of custom compliance
* **Requires Verification** ⚪: Compliance that need human assessment
