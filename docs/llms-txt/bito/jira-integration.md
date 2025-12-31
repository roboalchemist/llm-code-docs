# Source: https://docs.bito.ai/ai-code-reviews-in-git/jira-integration.md

# Jira integration

{% hint style="info" %}
**Note:** The Jira integration is available only on the [**Enterprise Plan**](https://bito.ai/pricing/).
{% endhint %}

Bito integrates with Jira to automatically validate pull request code changes against linked Jira ticket requirements, helping ensure your implementations align with the specified requirements in those tickets.

## How it works

When you create a pull request, Bito automatically:

1. **Detects Jira ticket references** in your pull request description, title, or branch name
2. **Crawls the linked Jira tickets** to extract requirements from issue descriptions and related Stories/Epics
3. **Analyzes your code changes** against these requirements
4. **Provides structured validation results** directly in your pull request comments

## **Jira integration options in Bito**

Bito supports two ways to connect with Jira, depending on where your Jira instance is hosted:

1. [**Jira Cloud**](#connect-bito-with-jira-cloud-hosted-by-atlassian)**:** for Jira sites hosted by Atlassian (e.g., `https://mycompany.atlassian.net`).
2. [**Jira Data Center**](#connect-bito-with-jira-data-center-hosted-on-your-own-server)**:** for Jira instances hosted on your own company domain or servers (e.g., `https://jira.mycompany.com`).

## Connect Bito with Jira Cloud (hosted by Atlassian)

{% stepper %}
{% step %}

### Connect Bito to Jira

1. Navigate to the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page in your Bito dashboard
2. In the **Available integrations** section, you will see **Jira**. Click **Connect** to proceed.
3. Select the option **Jira Cloud**. You will be redirected to the official Jira website, where you need to grant Bito access to your Atlassian account.
4. Click **Accept** to continue. If the integration is successful, you will be redirected back to Bito.
   {% endstep %}

{% step %}

### Agent-specific settings

After completing the initial setup, you can control Jira integration on a per-agent basis:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page in your Bito dashboard.
2. Find the Agent instance you want to connect with Jira and open its settings.
3. Within the Agent settings screen, click on the **Integrations** tab.
4. Locate the **Functional validation** option and **enable** this setting to activate automatic pull request validation against Jira tickets.
   {% endstep %}
   {% endstepper %}

{% hint style="info" %}
**Note:** The **Functional validation** feature must be enabled in your Bito agent settings for the integration to work.
{% endhint %}

## Connect Bito with Jira Data Center (hosted on your own server)

{% stepper %}
{% step %}

### Connect Bito to Jira

1. Navigate to the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page in your Bito dashboard
2. In the **Available integrations** section, you will see **Jira**. Click **Connect** to proceed.
3. Select the option **Jira Data Center (self-managed)**.
4. Provide connection details:
   * **Domain URL**: Enter the base URL for your Jira instance (e.g. `https://jira.mycompany.com`).
   * **Personal Access Token**: Enter a valid Personal Access Token with admin permissions. Read the [official Jira documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) to learn how to create a Personal Access Token.
5. Click **Connect to Jira**. You will be redirected to your self-hosted Jira website, where you need to grant Bito access to your Jira account.
6. Click **Allow** to continue. If the integration is successful, you will be redirected back to Bito.
   {% endstep %}

{% step %}

### Agent-specific settings

After completing the initial setup, you can control Jira integration on a per-agent basis:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page in your Bito dashboard.
2. Find the Agent instance you want to connect with Jira and open its settings.
3. Within the Agent settings screen, click on the **Integrations** tab.
4. Locate the **Functional validation** option and **enable** this setting to activate automatic pull request validation against Jira tickets.
   {% endstep %}
   {% endstepper %}

## Linking Jira tickets to pull requests

Bito offers multiple ways to link your Jira tickets with pull requests. You can use any of these methods:

#### Method 1: Branch name

Name your source branch using the Jira issue key:

```
feature/QP-123-implement-user-authentication
bugfix/QP-456-fix-login-error
```

#### Method 2: Pull request description

Include the Jira ticket reference in your PR description:

```
This PR implements user authentication as specified in QP-123.

Related tickets: QP-123, QP-124
```

OR

```
This PR implements shopping cart functionality as specified in:
https://your-company.atlassian.net/browse/QP-3
https://your-company.atlassian.net/browse/QP-7
```

#### Method 3: Pull request title

Include the Jira issue key in your PR title:

```
QP-123: Implement user authentication feature
[QP-456] Fix login validation error
```

## Understanding the validation results

When Bito completes its analysis, it adds a **"Functional Validation by Bito"** table to your pull request comments. This table contains four columns:

#### Source

Displays the **Jira issue key** (e.g., "QP-11", "QP-123") that references the specific Jira ticket being validated.

#### Requirement / Code Area

Shows a brief description of the requirement or task that needs to be completed, summarizing what needs to be done according to the Jira ticket.

#### Status

Indicates the completion status of each requirement:

* **Met**: The requirement has been fully implemented in the pull request
* **Missed**: The requirement has not been addressed in the pull request
* **Partial**: The requirement has been partially implemented but still needs additional work

#### Notes

Provides detailed information about the validation status:

* **For "Met" items**: Explains what has been successfully implemented
* **For "Missed" items**: Describes what is missing and needs to be addressed
* **For "Partial" items**: Details what has been completed and what still remains to be done

## Example validation output

Here's what a typical validation table looks like:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZLqYnwgMQ0bSmzdAUbmv%2Fscrnli_KjIe1WJ48Jm3Cf.png?alt=media&#x26;token=932928cb-447a-4cb9-956a-fc246a96c30f" alt=""><figcaption></figcaption></figure>

## Benefits

* **Automated quality assurance**: Ensure code changes meet specified requirements
* **Improved collaboration**: Bridge the gap between project management and development
* **Reduced manual reviews**: Bito AI automatically catches missing implementations during code review
* **Better traceability**: Maintain clear links between requirements and code changes

By leveraging Bito's Jira integration, your development team can maintain higher code quality while ensuring that all requirements are properly addressed in every pull request.

## Best practices

#### For developers

* Always reference Jira tickets in your pull requests using one of the supported methods
* Review the validation table and address any "Missed" or "Partial" items before merging

#### For teams

* Ensure Jira tickets contain clear, detailed requirements
* Use consistent naming conventions for branches and pull request titles
* Enable functional validation for all relevant agents

## Troubleshooting

**Validation table not appearing:**

* Check that your Jira integration is properly configured in the [**Manage integrations**](https://alpha.bito.ai/home/cra-integrations) page
* Verify that **Functional validation** is enabled in your agent settings
* Ensure your pull request contains valid Jira issue key references

**Incorrect validation results:**

* Review your Jira ticket descriptions for clarity and completeness
* Verify that linked Stories/Epics contain relevant requirements
* Check that your code changes are in the expected areas
