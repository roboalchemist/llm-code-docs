# Source: https://docs.gitguardian.com/public-monitoring/remediate/understand-incident-properties.md

# Investigate public incidents

> Describes the metadata, risk score, attachment reasons, tags, and exploration map available for investigating public secret incidents.

## Understanding public incidents

Before you can prioritize or remediate public secret incidents, you need to understand what each incident represents and whether it's relevant to your organization. Identifying whether secret leaks are related to your organization and pose a direct threat is the most crucial challenge and yet essential for effective prioritization, investigation, and remediation.

This guide explains all the context and insights that GitGuardian provides for each secret leak, helping you assess relevance to your organization and remediate effectively.

For every public incident, GitGuardian provides comprehensive metadata to help you understand the scope and impact:

## Risk score

Each public incident includes a **risk score** (0-100, where **100 indicates the highest risk** and **0 the lowest**) that provides ML-powered prioritization based on the technical risk of the exposed secret. The score is displayed prominently in the incident detail page with a detailed explanation of contributing factors.

**Important for public incidents:** The risk score reflects the technical risk of the secret itself (validity, type, exposure), not whether it's relevant to your company. Combine the risk score with [company-relation indicators](#tags-and-contextual-information) to assess the actual risk to your organization.

**Key features:**
- Dynamic scoring that updates as incident context evolves
- Natural language explanation of main risk factors
- Feedback mechanism to help improve the feature

â [Learn more about the Risk Score and how to use it](./prioritize-incidents.md#risk-score-ml-powered-prioritization)

## Secret detail

Every public incident provides detailed information about the secret itself:

### Detector information
The detector identifies the type of secret found. This helps you understand what service or system might be compromised.

### Secret validity
GitGuardian performs [validity checks](/secrets-detection/customize-detection/validity-checks) when possible to determine if the detected secret is still active and usable. Valid secrets pose immediate security risks and, when related to your company, should be prioritized for quick remediation. 

### Secret analyzer results
For some detectors, when the secret is valid, our [secret analyzer](/secrets-detection/secrets-detection-engine/secrets_analyzer) provides additional context about the secret's permissions and scope. This analysis helps you understand the potential impact if the secret were to be exploited. 

## Occurrences detail
The table of occurrences provides you with the detailed information you need:

- **Author identity**: The Git author name and email associated with the commit
- **Commit timestamp**: When the secret occurrence was committed
- **Repository**: The GitHub repository where the secret was found
- **Commit hash**: The specific commit containing the secret
- **File path**: The exact file and location within the repository
- **Patch preview**: A code snippet showing the secret in context (may be hidden for large patches)
- **GitHub link**: Direct link to view the occurrence on GitHub (when still publicly visible)
- **Presence indicator**: Shows whether the occurrence is still visible on public GitHub. The value "removed from GitHub" typically indicates that the repository has been deleted or made private after the leak, or that the commit itself has been deleted. 

:::caution 
The fact that the occurrence has been erased from GitHub does not mean that the incident is resolved! Indeed a malicious actor could have cloned the repository and seen the secret before it was erased from GitHub.
:::

## Attachment reasons
Attachment reasons explain why GitGuardian associated a public secret incident with your organization. Understanding these reasons helps validate the relevance of each incident:

- **By developer from perimeter**: One of your monitored developer is involved in the secret incident.
- **On organization from perimeter**: The secret incident happened on a repository of one of your monitored GitHub organizations.
- **From secret grasper**: The secret incident was attached to your company thanks to a [secret grasper](../perimeter/secret-graspers.md) in the commit.
<!-- - **From Explore search**: The secret incident has been created from an [Explore](link-to-explore) search, either manually or from a recurring scan. -->

:::info
Attachment reasons provide insight into the probability that a leak is related to your organization. Incidents attached "By developer from perimeter" may contain company secrets, but could equally be unrelated personal credentials from your developers. In contrast, incidents leaked "On organization from perimeter" are company-related since they originate from your organization's repositories.
:::

## Tags and contextual information

GitGuardian automatically applies various tags to help you quickly assess and categorize incidents:

### Indicators of company-related incidents

Several tags and indicators can help you identify incidents that are likely related to your organization:

- **Company domain in commit**: One of your monitored domains appears in the file content of the occurrence. 
- **Company name in commit**: Your company name appears in the patch where the secret is leaked.
- **Secret grasper in commit**: One of your defined secret graspers (which can be seen as company-specific identifiers) appears in the occurrence patch.
- **Context related to company**: GitGuardian's ML engine has determined that the context surrounding the secret leak appears related to your company, based on company-specific terms or enterprise-grade indicators.
- **Internally leaked**: This tag (only available if you also have Internal Monitoring) indicates that the same secret has been found in an internal incident within your monitored sources. The [exploration map](#exploration-map) will show you the related internal incident. In Internal Monitoring, this relationship is shown as the **Public incident linked** exposure type on internally leaked secrets. See [Public exposure information](/internal-monitoring/remediate/investigate-incidents#public-exposure-information) for more details.

<!-- ### Vault property
If you have integrated your secret managers, the Vault indicator identifies incidents where secrets are stored in your organization's vaults. This is a strong signal that the leaked secret belongs to your company and requires immediate attention. -->

### Other tags
Some other tags are provided by GitGuardian to help you assess the likely criticality of incidents: 

- **Sensitive file**: One of the occurrences of the incident happened on a potential sensitive file
- **Production**: The commit associated with one of the occurrences seems related to a production environment.
- **Test file**: One of the occurrences of the incident happened on a potential test file. A file is automatically classified as a test file if its path contains any of the following patterns (with only numbers or special characters around them): test/tests, example/examples, mock/mocks, fixture/fixtures, fake, dummy, false, or testdata. For example, .test.env or 00testdata.json will match, but dummydata.json will not.
- **False positive**: GitGuardian's ML engine has identified this as likely not being an actual secret. These incidents can typically be safely ignored. (Learn more [here](../../secrets-detection/secrets-detection-engine/machine_learning.md#false-positive-remover))
- **From historical scan**: The incident was discovered during a historical scan rather than through real-time monitoring.

## Exploration map

:::info
This feature provides the most value when you also use [Internal Monitoring](../../internal-monitoring/home), [NHI Governance](../../nhi-governance/home), or have integrated with your secret managers using [GitGuardian Scout](../../ggscout-docs/integrations/secret-managers) for comprehensive context.
:::

The exploration map provides a visual representation of where GitGuardian has detected this specific secret across your integrated sources and what access it potentially grants.

![Exploration map](/img/public-monitoring/remediate/understand-incident-properties/exploration-map.png)

The map can reveal:
- **Internal incidents** (if you use Internal Monitoring): Whether the secret also appears in your internal codebase, JIRA tickets, Slack messages, or other internal sources
- **Secret manager storage** (if you've integrated secret managers): Whether the secret is stored in your vaults or secret managers
- **Infrastructure usage** (if you use NHI Governance with infrastructure integrations): Whether the secret is used in infrastructure sources like GitLab CI or Kubernetes clusters

:::caution The strongest company-related indicator
**For public secret incidents, an exploration map showing multiple nodes is the strongest possible indicator that this secret truly belongs to your company and requires immediate remediation.**
:::

## ML-powered similar incident grouping

:::note
ML-Powered Similar Incident Grouping is available for Business and Enterprise plans.
:::

GitGuardian's ML-powered similar incident grouping helps you identify and manage related incidents more efficiently by automatically detecting incidents that share similar characteristics and context.

### How it works

When viewing an incident detail page, you'll see a **Similar Incidents** section in the sidebar that displays incidents with similar patterns detected by our machine learning algorithms. This feature analyzes the code context in the patch to identify meaningful relationships between incidents.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/N2iAQMlLzF8?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

### Common grouping scenarios

The ML algorithm identifies various types of similar incidents:

- **Rotating tokens in automated files**: Same file continuously leaking different tokens through automation
- **QA test credentials**: Test keys (Slack bots, Postman API keys) appearing across similar contexts
- **Database connection strings**: Multiple connection strings to the same environment with different credentials
- **Repeated false positives**: High-entropy strings in logs or test scripts that are likely system-generated
- **Templating code leaks**: Multiple developers using shared tutorials or templates with similar leaked secrets
- **Known noisy patterns**: Consistent false positives from specific file types or internal services

### Using similar incidents for investigation

1. **From incident details**: View similar incidents in the sidebar and click on "View X similar incidents" to see them in the main incidents list
2. **Filter by similarity**: In the search box, use `similar_to` to show only incidents similar to a specific incident
3. **Sort by similarity count**: Use the "Similar incidents" column to sort incidents by highest or lowest number of similar incidents

This feature is particularly useful for:
- **Identifying false positives**: Spot patterns that indicate false positive incidents
- **Consistent remediation**: Apply the same remediation approach to incidents that require similar fixes
- **Understanding incident patterns**: Discover recurring issues in your codebase

![ML Similar Incident Grouping](/img/internal-monitoring/remediate/ml-similar-incident-grouping.png)

When investigating public incidents, similar incident grouping helps you:

- **Identify patterns**: Spot recurring issues from specific developers or repositories
- **Assess organizational relevance**: Group incidents that may share the same root cause
- **Prioritize efficiently**: Handle related incidents together rather than individually

:::note
ML-Powered Similar Incident Grouping is available for Business and Enterprise plans.
:::

GitGuardian's ML-powered similar incident grouping helps you identify and manage related incidents more efficiently by automatically detecting incidents that share similar characteristics and context.

### How it works

When viewing an incident detail page, you'll see a **Similar Incidents** section in the sidebar that displays incidents with similar patterns detected by our machine learning algorithms. This feature analyzes the code context in the patch to identify meaningful relationships between incidents.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/N2iAQMlLzF8?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

### Common grouping scenarios

The ML algorithm identifies various types of similar incidents:

- **Rotating tokens in automated files**: Same file continuously leaking different tokens through automation
- **QA test credentials**: Test keys (Slack bots, Postman API keys) appearing across similar contexts
- **Database connection strings**: Multiple connection strings to the same environment with different credentials
- **Repeated false positives**: High-entropy strings in logs or test scripts that are likely system-generated
- **Templating code leaks**: Multiple developers using shared tutorials or templates with similar leaked secrets
- **Known noisy patterns**: Consistent false positives from specific file types or internal services

### Using similar incidents for investigation

1. **From incident details**: View similar incidents in the sidebar and click on "View X similar incidents" to see them in the main incidents list
2. **Filter by similarity**: In the search box, use `similar_to` to show only incidents similar to a specific incident
3. **Sort by similarity count**: Use the "Similar incidents" column to sort incidents by highest or lowest number of similar incidents

This feature is particularly useful for:
- **Identifying false positives**: Spot patterns that indicate false positive incidents
- **Consistent remediation**: Apply the same remediation approach to incidents that require similar fixes
- **Understanding incident patterns**: Discover recurring issues in your codebase
