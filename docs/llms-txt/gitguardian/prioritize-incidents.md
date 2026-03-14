# Source: https://docs.gitguardian.com/public-monitoring/remediate/prioritize-incidents.md

# Source: https://docs.gitguardian.com/internal-monitoring/remediate/prioritize-incidents.md

# Prioritize incidents

> Prioritize secret incidents using the incidents table, saved views, severity scoring, validity checks, tags, and ML-powered risk scores.

One of the key challenges of a secrets detection and remediation program is **prioritizing incidents and identifying where you should focus remediation efforts.**

> Prioritization is the first step in your remediation journey. After prioritizing incidents, you will need to [investigate](./investigate-incidents.md) to gather context, then lastly [remediate](./remediation-overview.md) to address the most critical ones.

GitGuardian focuses on the precision of its secrets detection engine (to raise the highest percentage of true positives). You can refer to our [dedicated documentation for the GitGuardian secrets detection engine](../../secrets-detection/home) for further information. That being said, the severity of a secret incident is still a notion that is hard to grasp from an external standpoint. That is why GitGuardian tries to give as much factual information as possible in order to help you categorize the severity of the secret incident.

## 1. Prioritize with the incidents table

You can find a table of all your incidents in the Incident section. Our aim is to help you navigate this table in the most efficient way possible.

### Using saved views

Prioritizing incidents efficiently is crucial for effective remediation. The [Saved views](../../platform/collaboration-and-sharing/saved-views.md) feature allows you to quickly access and manage your preferred filter sets, focusing on the most important incidents without repeatedly adjusting filters.

Some views are pre-set by GitGuardian, providing a starting point for effective incident management:

- **Open**: View all incidents that are currently open and require attention.
- **Critical**: Focus on open incidents with a risk score above 80/100, highlighting the highest-priority incidents to address first.
- **My open incidents**: Display incidents assigned to the current user, allowing for personalized incident management.
- **Closed but valid**: Review incidents that have been resolved or ignored while the secret is still marked as valid.

Users can also create their own custom views to fit their specific remediation processes.

### Most recent incidents

By default, the table of incidents is sorted by "most recent" incidents. As a matter of fact, **secrets that were detected most recently have the highest probability of being valid and thus harmful**. The date of an incident is the date of its first occurrence.

It is especially important to note here that **GitGuardian creates secrets incidents during historical scans**. The date of those incidents is the date of the commit where the secret exposure happened, not the date of the historical scan. Such incidents will be marked with the "From historical scan" tag.

Therefore, you can end up with very old incidents as you run GitGuardian on your git history. That is why, we allow you to modify the time frame of the listed incidents and set it to **All time**. By default, this time frame is set to Last Month.

### Secret preview

You can **quickly preview the actual secret from the incidents table** with a simple hover. If you would like to further investigate, you can click on the secret incident and visit its dedicated page.

Be cautious: **sometimes the broader context of a secret can be much more harmful than the secret itself**. We always recommend going beyond the secret preview and conducting an in-depth investigation before making a decision on a particular incident.

![secret preview](/img/internal-monitoring/remediate/incidents/secret_preview.png)

### Secret validity

The table of incidents indicates for each incident if the exposed secret is still valid or not. You can also filter your incidents to view valid secrets only. This can help you prioritize your incidents and focus on secrets that can still be exploited. We recommend you take care of exposed and valid credentials as soon as possible, since they represent a higher risk of exploitation.

![Secret validity preview and filter](/img/internal-monitoring/remediate/incidents/secret_validity_filter.png)

For more details on this feature, please refer to the dedicated section on [validity checkers](../../secrets-detection/customize-detection/validity-checks).

### Occurrences count and presence in git history

The table of incidents also indicates the number of occurrences for each incident. **The severity of an incident should not be determined simply by its number of occurrences**. This informs you about the potential sprawl of the secret but keep in mind that a secret that is present in more than one place is often not a harmful secret.

The total count is split between the occurrences of the incident present in your git repository and the ones that have been rendered non-existent (following the deletion of a repository or rewriting of the git history).

![Occurrences count and breakdown](/img/internal-monitoring/remediate/incidents/occurrence_count.png)

Removing any trace of the secret in your git repositories may be one of your requirements for full incident remediation. If that is the case, it is possible to filter your incidents to only view the ones for which at least one occurrence is still present or in other words, the ones for which remediation is incomplete.

![Incident presence filter](/img/internal-monitoring/remediate/incidents/occurrence_presence_filter.png)

### GitGuardian Tags

For each incident, we try to give you as much contextual information as possible. **GitGuardian tags are meant to help you quickly evaluate each incident**. In the incidents table, you will see all the tags associated with occurrences of an incident. The different tags are:

- **Default branch**: at least one occurrence of the incident is found in the default branch of a repository.
- **Publicly leaked**: the secret has been found in one or more public locations. This tag indicates public exposure and should be prioritized for remediation. See [Public exposure information](#public-exposure-information) for details on the types of exposure.
- **From historical scan**: one of the occurrences of the incident was detected thanks to a historical scan, as opposed to being detected in real-time.
- **Regression**: the incident was once resolved but GitGuardian detected a new occurrence.
- **Sensitive file**: one of the occurrences of the incident happened on a potential sensitive file.
- **Tagged as false positive in check runs**: one of the occurrences of the incident has been tagged as a false positive in GitHub by one of your developers.
- **Test file**: one of the occurrences of the incident happened on a potential test file. A file is automatically classified as a test file if its path contains any of the following patterns (with only numbers or special characters around them): `test`/`tests`, `example`/`examples`, `mock`/`mocks`, `fixture`/`fixtures`, `fake`, `dummy`, `false`, or `testdata`. For example, `.test.env` or `00testdata.json` will match, but `dummydata.json` will not.
- **Vaulted**: the secret is stored in one of your Secret Managers, increasing confidence it is a true positive.
- **Revocable by GitGuardian**: the secret can be revoked directly from the GitGuardian dashboard. [Learn more about revocation](/internal-monitoring/remediate/remediate-incidents#secret-revocation-from-gitguardian).

:::info

About the **Default branch** tag. After this feature is activated on your workspace, the tag will be automatically applied to future incidents. For incidents raised by GitGuardian before July 2023, or repositories where the default branch has been modified at the VCS level, a full scan of your repositories needs to be re-run.

Please visit the [perimeter](https://dashboard.gitguardian.com/perimeter) page to run a historical scan.

:::

![Tags](/img/internal-monitoring/remediate/incidents/tags.png)

### Public exposure information

When a secret has the **Publicly leaked** tag, GitGuardian provides additional details through the **Public exposure** property. There are three types of public exposure:

- **Source is publicly visible**: The incident has at least one occurrence in a monitored source that is publicly visible. This information is available to all Internal Monitoring users.
- **Has linked public incident**: The secret also appears in one or more public incidents from your company's public perimeter. Seeing full details about the public incidents requires a Public Monitoring subscription.
- **Found outside perimeter**: The secret has been found in public locations unrelated to your company (such as public GitHub repositories, issues, or gists your organization does not own). Seeing full details about the locations requires a Public Monitoring subscription.

You can filter incidents by exposure type to focus your remediation efforts. For more detailed information about each exposure type, see the [Public exposure information](./investigate-incidents.md#public-exposure-information) section.

:::note Self-hosted installations
For self-hosted installations, only the "Source is publicly visible" exposure type is available.
:::

### Severity

#### Manual severity assignment

To help you prioritize incidents during triage, you can set a severity for each incident. You can define the severity of an incident either in its dedicated remediation page, or directly from the table of incidents.

The different severity levels are:

- **Critical**: concerns a critical service. **Must be tackled as quickly as possible.**
- **High**: concerns an important service with a potentially broad impact.
- **Medium**: concerns an important service with a potentially limited impact.
- **Low**: concerns a minor service with a potentially broad impact.
- **Info**: concerns a minor service with a potentially limited impact.
- **Unknown**: default level applied by GitGuardian to new incidents.

![Severity](/img/internal-monitoring/remediate/incidents/severity.png)

#### Automated severity scoring

:::info

Only Managers and Owner can activate this feature.

:::

Manual severity assignment requires a case-by-case examination of your open incidents and can be time-consuming for your teams. GitGuardian's severity scoring feature automates this approach, where and when applicable, to the incidents in your workspace so that you can save time on their triaging and prioritization.

:::tip

Automated severity scoring comes in handy after running a historical scan on your perimeter that surfaces hundreds or thousands of incidents.
It can help you focus your remediation efforts on the most critical incidents first!

:::

To activate the automated severity scoring feature, go to the [Severity rules pages in the Secrets section of your GitGuardian workspace settings](https://dashboard.gitguardian.com/settings/secrets/severity-rules).

You can see the coverage of the automated severity scoring engine. GitGuardian computes this by dividing the total number of incidents for which it has automatically assigned a severity by the total number of open incidents in your workspace.

![automated-severity-toggle](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-settings.png)

GitGuardian determines the severity of each incident by following a predefined ruleset that can be customized. The rules are evaluated sequentially for each incident from the first to the last. The severity assigned will be that of the first rule whose conditions are met. In case of multiple occurrences for an incident, the rules engine will evaluate all of them and assign the highest severity among them. You can inspect this ruleset in the [Severity rules page of the Secrets section of your settings](https://dashboard.gitguardian.com/settings/secrets/severity-rules).

![automated-severity-ruleset](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-ruleset.png)

Each rule of the ruleset is composed of the following:

- A **name** identifying the rule
- A **description** of the rule
- A **severity** to be assigned automatically in case of a match
- A **set of conditions** defining the rule
- The **total number of incidents** for which the rule has set the severity

As a Manager or Owner of the workspace, you can customize this ruleset by clicking on the **Edit ruleset** button. This allows you to maximize the coverage of automatically scored incidents by defining a ruleset related to your own context.

![automated-severity-ruleset-edit](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-ruleset-edit.png)

:::info

The default ruleset designed by GitGuardian can benefit from regular updates.
Once customized, the ruleset will not benefit from these updates as you become the manager of these rules.

:::

Once entered the edit mode of the ruleset, you can:

- **Add a new rule** by clicking on the `New rule` button _(up to 20 rules)_
- **Edit a rule** by clicking on the pen icon of the rule
- **Delete a rule** by clicking on the bin icon of the rule _(You can't empty your entire ruleset)_
- **Reorder rules** by dragging them in relation to each other

![automated-severity-rule-edits](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-rule-edits.png)

Creating or editing a rule allows you to define the:

- **Name** identifying the rule
- **Description** of the rule _(optional)_
- **Set of conditions** defining the rule _(up to 20 conditions)_
- **Severity** to be assigned automatically in case of a match

![automated-severity-rule-edition](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-rule-edition.gif)

Once you have customized your ruleset, don't forget to save it by clicking on the `Save changes` button. This will result in a new scoring of your open incidents based on your fresh new ruleset. The scoring time depends on the number of your secret incidents and occurrences.

If you wish, you can always reset to the default ruleset defined by GitGuardian by selecting the `Reset to default` option in the `...` menu. This will allow you to benefit from GitGuardian's ruleset updates again.
You can also manually recompute your severity scoring by selecting the `Recompute severity scoring` option.

![automated-severity-ruleset-reset](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-ruleset-options.png)

In the incidents table view, hovering over the severity badge of an incident will display a tooltip indicating whether it was set manually or automatically. In the latter case, the rule that matched will also be indicated. You can always override the automated severity set by GitGuardian by selecting a severity of your choice.

![automated-severity-tooltip](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-tooltip.png)

On the details page of a critical or high incident, you will find a banner indicating the automated severity score and its corresponding rule.

![automated-severity-banner](/img/internal-monitoring/remediate/automated-severity-scoring/automated-severity-banner.png)

In case GitGuardian cannot determine the severity of the incident, it will also inform you in the same banner, and you can assign one directly from there â using the dropdown menu.

### Risk score (ML-powered prioritization)

:::info Business feature
Only workspaces with a Business plan can access risk score.
:::

The risk score is an ML-powered feature that automatically assesses the risk level of each incident on a scale of 0-100, where **100 indicates the highest risk** requiring immediate attention and **0 indicates the lowest risk**. It provides an additional layer of prioritization by analyzing multiple risk signals to help you focus on the incidents that pose the greatest threat.

The risk score complements severity scoring by providing a more granular, continuously updated risk assessment.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/jVXXsS4tBbY?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

#### How it works

The risk score is calculated using machine learning models that consider various factors including:
- Secret type
- Validity (past or present)
- Detection context (test files, sensitive files, production environment, etc.)
- Secret exposure patterns
- Additional contextual signals

The score is dynamic and recalculates regularly to reflect changes in the incident's risk profile.

#### Using risk score in your workflow

:::tip We value your feedback

The risk score uses machine learning models that are continuously improved based on user feedback. If you notice incidents with unexpected scores or explanations, we encourage you to share feedback directly through the dashboard â your input helps us refine the scoring model.

:::

##### In the incidents table

The risk score can be used to prioritize incidents in multiple ways:

**Filtering and sorting**:
- **Filter by risk score range**: Use the "Risk score" filter to focus on specific risk levels (e.g., Risk score â¥ 80 for highest priority)
- **Sort by risk score**: Select "Sort by Risk score" to order incidents by priority
- **Use the "Critical" saved view**: This pre-configured view displays all open incidents with a risk score above 80/100, giving you quick access to the highest-priority incidents

**Adding the Risk score column**:

By default, the risk score column is not displayed in the incidents table. To view the actual score values:

1. Click the **Columns** button in the top-right of the incidents table
2. Find "Risk score" in the list of available columns
3. Click the eye icon to make it visible
4. The column will now appear in your table, showing the 0-100 score for each incident

![Risk score column configuration](/img/internal-monitoring/remediate/incidents/risk-score-column.png)

##### "Critical" saved view

The **"Critical"** saved view is pre-configured to display all open incidents with a risk score above 80/100. This view helps you immediately focus on the incidents that require the most urgent attention.

![Critical saved view](/img/internal-monitoring/remediate/incidents/critical-saved-view.png)

:::tip Customize your threshold

You can duplicate the "Critical" saved view and adjust the risk score threshold to match your workflow. For example:
- Set a higher threshold (e.g., 90/100) to focus on fewer, extremely high-risk incidents
- Set a lower threshold (e.g., 70/100) to capture a broader set of incidents for review

This flexibility allows you to control the volume of incidents you want to prioritize based on your team's capacity and risk tolerance.

:::

##### In the incident detail page

When investigating an incident, you'll find the risk score at the top of the incident detail page showing:
 - **The current risk score** (0-100) with a visual indicator
 - **A detailed explanation** of what drives the score, based on the incident's context and characteristics, so you know what to prioritize.
 - **Feedback buttons** to help us improve the feature (thumbs up/down)

![Risk score in incident detail page](/img/internal-monitoring/remediate/incident-detail/risk-score-explanation-internal-incident.png)

**Score evolution:**

The risk score is dynamic and recalculates regularly as the incident context evolves. Changes in detection context, exposure patterns, or other risk signals may cause the score to adjust over time. Additionally, our ML model is continuously improved, which may lead to score refinements.

**Providing feedback:**

Your feedback helps us continuously improve the ML model. In the incident detail page, you can:
1. Review the risk score and its explanation
2. Use the thumbs up button if the score accurately reflects the risk, or the thumbs down button if the score doesn't match your assessment
3. Expand/collapse the explanation using the arrow button

Feedback is reviewed by our team to regularly refine the scoring algorithm.

#### Risk score vs. Severity

Both tools help with prioritization but serve different purposes:

| Feature | Risk Score | Severity |
|---------|-----------|----------|
| Calculation | ML-powered, automatic | Rule-based, can be manual |
| Granularity | 0-100 scale | 6 levels (Critical to Unknown) |
| Updates | Dynamic, recalculates automatically | Static unless manually changed or rules recomputed |
| Best for | Granular risk assessment | Policy-based categorization |

## 2. Explore with the incident page

Each incident has a dedicated page in which you can find additional information to help you investigate.

### Secret overview

The secret overview provides all the details related to the secret itself and main information:
- the type of secret along with the detector information.
- the [secret validity](./prioritize-incidents#secret-validity) if available.
- the secret values depending on the detector (e.g. client_id, client_secret, etc...).
- the [secret analyzer](../../secrets-detection/secrets-detection-engine/secrets_analyzer) if available.
- the secret scopes if the above secret analyzer is available and the analysis succeeds.

It enables you to perform an initial diagnosis on how critical this incident may be.

### Secret Manager presence

GitGuardian integrates with Secret Managers through **[ggscout](/ggscout-docs/home)**, enabling you to synchronize secrets incidents with secrets stored in your Secret Managers. 
This integration allows you to track whether a specific secret is stored in one or more Secret Managers, providing additional insights such as the secret's path, lease time, and any custom metadata associated with it.

![Duplicated Secrets](/img/internal-monitoring/integrate-sources/secrets-managers-integrations/duplicated-secrets.png)

Quickly identifying the location of secrets within your Secret Manager helps save time for you and your developers, while accelerating the remediation process. It can also assist in identifying poor Secret Management practices, such as the presence of duplicated secrets. 
**[Discover more use cases](/internal-monitoring/integrate-sources/secrets-managers-integrations/overview.md)** that you can benefit from Secrets Managers integrations.

### Impacted perimeter

The Impacted Perimeter feature addresses the critical need for comprehensive secret management in modern software development. It provides a quick overview and detailed breakdown of secret occurrences across your codebase and other data sources, enabling teams to rapidly assess vulnerabilities and prioritize remediation efforts. By tracking the status of secrets from detection through remediation, this feature enhances security awareness, streamlines the fix process, and supports compliance efforts.

The **Impacted perimeter** is divided in two sections to get either a quick or detailed view of the impact of the incident on your perimeter.

**Secret presence** helps you get a glimpse of the incident status across your perimeter by showing the following metrics:

- **requiring code fix** which counts the number of *files containing at least one mention of the secret in the last commit of the default branch*
- the number of occurrences present **overall** or in **other data sources**

The **Vulnerable sources** part lists in details the occurrences of the secret for each impacted source, either requiring code fix or not.

N.B. non-monitored and deleted sources are also included.

![Impacted perimeter](/img/internal-monitoring/remediate/incident-detail/impacted_perimeter.jpg)

#### Occurrences requiring code fix

Occurrences requiring code fix matter particularly as they are *present in the current state of the code when browsing the VCS or when cloning the repository*. It is the current state of the repository that is monitored here. It is possible to change the default branch monitored by updating the default branch directly in the VCS.

Therefore, vulnerable files are listed on top in the **files requiring code fix** section, with a link to the file in the VCS.

As it is important to fix them as a priority, the **files pending merge** section keeps track of the code fixing.
To do so we monitor the pull requests of the source and check if they are about to remediate an incident (i.e. remove at least one mention of the secret), and if so list them and the associated files.

Once merged, the pull request is listed next to the files fixed in the **files fixed** section.

The pull request names can be clicked to view them in more details on the VCS website.

Feature limitations:

- *The number of files in the PR is limited to 200 for GitHub* to avoid making too many API calls; above that limit the feature won't work properly.
- Currently, the feature *only works for GitHub and GitLab*.

#### All occurrences

The table of occurrences provides you with the following detailed information:

- when the occurrence happened
- who is the developer responsible for the leak (git name, git email)
- where the occurrence took place (commit, file)
- when the occurrence was last seen by GitGuardian and if it still visible in your git history
- the tags associated with the occurrence

For the needs of conducting further investigation, each occurrence has its own menu, with a link to the actual place of the secret occurrence on the VCS, if still present.

![Occurrence log](/img/internal-monitoring/remediate/incident-detail/occurrence_log.jpg)

#### Patch

For each occurrence of a given secret incident, you have access to **the patch of the commit where the secret has been detected**. The patch is composed of:

- the lines of code added by the commit
- the lines of code deleted by the commit
- the contextual lines surrounding the added or deleted lines. These lines are also monitored by GitGuardian since they are part of the commit.

A secret can consist of several components. For example, an AWS secret is the combination of `client_id` and `client_secret`. You can easily navigate and understand these multiple secret components with the patch in your GitGuardian workspace.

![Patch](/img/internal-monitoring/remediate/incident-detail/patch.jpg)

N.B. In the screenshot the secret is obfuscated because the [privacy mode](/docs/platform/security-data-privacy/privacy-mode.md) is enabled

<!-- needs to be done again when tags release -->

From our experience, **lots of valuable information can be found around the patch of a secret** (other secrets, sensitive data, ...).

## 3. Explore generic incidents (Generic Secret Enricher ML model)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RTS2BpoxrN8?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

After detecting a generic incident, the platform analyzes the entire context of the document to identify the associated provider or category of the secret. **When successful, the enriched secret name automatically replaces the generic detector name** throughout the platform, transforming vague findings like "Generic Database Assignment" into precise, actionable names like "Redis Identifiers" or "PostgreSQL Connection String."

This functionality is powered by "Secret Enricher", a specialized machine learning model designed for contextual secret analysis. The enriched names provide immediate context, allowing you to quickly understand what type of secret was exposed without opening each incident.

### How to use it ?

#### Enriched names in incident lists

Enriched secret names appear automatically in your incident listsâno configuration needed. When the ML model successfully identifies a secret type, you'll see precise names like:

- **Redis Identifiers** instead of "Generic Database Assignment"
- **Stripe API Key** instead of "Generic High Entropy Secret"
- **AWS Access Key** instead of "Generic High Entropy Secret"
- **PostgreSQL Connection String** instead of "Generic Database Assignment"

This makes incident triage faster and more intuitive, giving you immediate context about what was exposed.

#### Customize your views

From the incidents list, you can customize how your incidents are displayed by clicking on the "Columns" button in the top-right corner of the table.
![GSE-columns](/img/internal-monitoring/remediate/incidents/customize_columns.png)

This allows you to add the "Secret category" and "Secret provider" columns, which display additional enrichment properties alongside the enriched secret name.

With this customization, you can quickly spot important categories (such as "Data Storage") or specific providers that might require immediate attention.

![GSE-columns](/img/internal-monitoring/remediate/incidents/gse_predictions.png)

#### Filter your data

Three filters (Provider, Category, Family) help you identify the most significant or critical incidents, such as those classified under "Data Storage" or linked to the provider "PostgreSQL."

You can apply these filters to all enriched incidents or combine them with the "Generic" type filter for focused analysis.

![GSE-filters](/img/secrets-detection/machine-learning/gse-howto.png)

With these new filters you can explore your generic incidents and unveil the one that matters for your operations.

:::tip Learn More About Categories and Providers
For detailed definitions of all GSE categories and providers, including what they mean and how to prioritize them, see our comprehensive [GSE Categories and Providers Reference](../../secrets-detection/secrets-detection-engine/gse-categories-providers-reference).
:::

### FAQ
#### Why Aren't These Transformed into Specific Incidents?

The analysis might be incomplete. We may only be able to identify the Provider or the Category (or potentially neither). As we continue to refine this feature, our definitions will become more precise.

#### What is the model trained to discover?

For detailed information about the categories and providers the model can identify, see the [Machine Learning documentation](../../secrets-detection/secrets-detection-engine/machine_learning#what-is-the-model-trained-to-discover) in the Secrets Detection section.

## Next steps: from prioritization to investigation

Once you've identified and prioritized your most important incidents, you're ready to investigate them for proper remediation planning.

### What you should have after prioritization

- **A focused list** of incidents to work on first (high severity, valid secrets, critical systems, etc...)
- **Context about urgency:** which incidents have public exposure or elevated privileges.

### Ready to investigate?

Move to the [Investigation phase](./investigate-incidents.md) to:
- Understand what each secret accesses
- Assess the impact of potential revocation
- Gather context needed for safe remediation
- Identify dependencies and affected systems

> **Pro Tip**: Even urgent incidents benefit from a few minutes of investigation to avoid breaking systems during remediation. Use the investigation phase to make informed decisions about your remediation approach.
