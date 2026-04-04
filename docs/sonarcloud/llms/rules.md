# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/rules.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/rules.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/rules.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/rules.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules.md

# Rules

### Overview <a href="#overview" id="overview"></a>

SonarQube's analyzers run rules on source code, resulting in the generation of issues and security hotspots. These rules address three software qualities—security, reliability, and maintainability—and are categorized into four types: bugs, vulnerabilities, code smells, and security hotspots.

For code smells and bugs, zero false-positives are expected. At least this is the target so you don’t have to wonder if a fix is required.

For vulnerabilities, the target is to have more than 80% of issues be *true* positives.

Security hotspot rules draw attention to code that is security-sensitive. After being reviewed by a developer, more than 80% of issues are expected to be quickly resolved.

The [Sonar Rules website](https://rules.sonarsource.com/) is the entry point where you can discover all the existing rules.

### Rules page <a href="#rules-page" id="rules-page"></a>

1. From within your organization, select **Rules** in the navigation bar to see all the available rules.
2. Use filters to narrow your results.
3. A list of rules appears on the right side of the page.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-1edbce7c94ebb496a7b4c6b23d17e301eff73a51%2Fbb0517ffee35888ff957e46a92c98954c3912d9c.png?alt=media" alt="The SonarQube Cloud Rules page allows you to filter issues (on left) and show the list on the right side of the page."><figcaption></figcaption></figure>

#### Filters <a href="#filters" id="filters"></a>

You can filter the list of rules using the following criteria in the left sidebar:

* **Language**: the language to which a rule applies.
* **Code Attribute**: the single attribute evaluated by the rule. A code attribute contributes to the long-term value of your software. The possible values are: consistency, intentionality, adaptability, responsibility. For more information, see the [glossary](https://docs.sonarsource.com/sonarqube-cloud/appendices/glossary#c).
* **Software Quality**: the software quality addressed by the rule. The same rule may address several software qualities. The possible values are: security, reliability, maintainability.
* **Severity** (software quality): the impact level with which a software quality is impacted if the rule is broken. The possible values are: blocker, high, medium, low, info.
* **Type**: the category of the issue raised by the rule if the rule is broken. The possible values are: bug, vulnerability, code smell, security hotspot.
* **Type severity**: the severity of the issue or hotspot raised by the rule if the rule is broken. The possible values are : blocker, critical, major, minor, info. \
  Note that quality gate conditions related to severity currently use type severities.
* **Tag**: you can add tags to rules in order to classify them and to help discover them more easily.
* **Repository**: the engine/analyzer that contributes rules to SonarQube Cloud.
* **Status**: rules can have 3 different statuses:
  * **Ready**: the rule is ready to be used in production.
  * **Beta**: the rule has been recently implemented and Sonar hasn’t gotten enough feedback from users yet, so there may be false positives or false negatives.
  * **Deprecated**: the rule should no longer be used because a similar, but more powerful and accurate rule exists.
* **Security Category**: security rules are classified according to well-established security standards such as [CWE](https://cwe.mitre.org/) and [OWASP Top 10](https://owasp.org/Top10/). See the [security-related-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-related-rules "mention") page for more detail.
* **Available Since**: The date when a rule was first added on SonarQube Cloud. This is useful to list all the new rules since the last upgrade of a plugin, for instance.
* **Quality Profile**: *Inclusion in* or *exclusion from* a specific profile.
* **Inheritance**: Available when an inherited quality profile is selected. It filters inherited rules, other rules, or inherited rules that have been overridden by other settings.
* **Activation severity** is available when an inherited quality profile is selected. It can filter by severity using the value chosen when the rule was activated in the quality profile.

See the [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") for more details about how your rule selection affects your analysis.

### Rule details <a href="#rule-details" id="rule-details"></a>

To see the details of a rule, either select the rule title or use the arrow keys to cycle through the list. Inside the detailed view, along side the basic rule data, you’ll also see which profiles the rule is active in.

**Add/Remove tags**:

* You can add existing tags to a rule or create new ones, just enter a new name while typing in the text field. For more information, see [#tagging](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/editing#tagging "mention"). &#x20;
* Note that some rules have built-in tags that you cannot remove. They are provided by the plugins that contribute the rules.

**Extend description**:

* You can extend rule descriptions to let users know how your organization uses a particular rule or give more insight into a rule.

### Rule types, software qualities and severities <a href="#rule-types-software-qualities-and-severities" id="rule-types-software-qualities-and-severities"></a>

{% tabs %}
{% tab title="SOFTWARE QUALITY CATEGORIZATION" %}
How are rules categorized by software qualities impacted? There are four categories: security, reliability, maintainability, and security hotspots. Rules are assigned to one or more software quality categories based on the answers to these questions:

**Is the rule about code that could be exploited by an attacker?** If yes, then it’s a security rule.

**Is the rule about code that is demonstrably wrong, or more likely wrong than not?** If the answer is "yes", then it’s a reliability rule.

**Is the rule neither a bug nor a vulnerability?** If yes, then it’s a maintainability rule.
{% endtab %}

{% tab title="TYPES CATEGORIZATION" %}
How are rules categorized by type? There are four categories: bugs, vulnerabilities, code smells, and security hotspots. Rules are assigned to categories based on the answers to these questions:

**Is the rule about code that could be exploited by an attacker?** If yes, then it’s a vulnerability rule.

**Is the rule about code that is security-sensitive?** If yes, then it’s a security hotspot rule.

**Is the rule about code that is demonstrably wrong, or more likely wrong than not?** If the answer is "yes", then it’s a bug rule.

**Is the rule neither a bug nor a vulnerability?** If yes, then it’s a code smell rule.
{% endtab %}
{% endtabs %}

### How severities are assigned <a href="#how-severities-are-assigned" id="how-severities-are-assigned"></a>

{% tabs %}
{% tab title="SOFTWARE QUALITY SEVERITIES" %}
List of severity metrics used in software qualities.

<table><thead><tr><th width="134">Severity</th><th>Definition</th></tr></thead><tbody><tr><td>Blocker</td><td>An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or run malicious code.</td></tr><tr><td>High</td><td>An issue with a high impact on the application that should be fixed as soon as possible.</td></tr><tr><td>Medium</td><td>An issue with a medium impact on the application.</td></tr><tr><td>Low</td><td>An issue with a low impact on the application.</td></tr><tr><td>Info</td><td>There is no expected impact on the application. For informational purposes only.</td></tr></tbody></table>
{% endtab %}

{% tab title="TYPE SEVERITIES" %}
List of severity metrics used in types.

<table data-header-hidden><thead><tr><th width="125">Severity</th><th>Definition</th></tr></thead><tbody><tr><td>Blocker</td><td>An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or run malicious code.</td></tr><tr><td>Critical</td><td>An issue with a critical impact on the application that should be fixed as soon as possible.</td></tr><tr><td>Major</td><td>An issue with a major impact on the application.</td></tr><tr><td>Minor</td><td>An issue with a minor impact on the application.</td></tr><tr><td>Info</td><td>There is no expected impact on the application. For informational purposes only.</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

To assign severity to a rule, we ask a further series of questions. The first one is:

**What’s the worst-case scenario that could happen?**

In answering this question, we try to factor in Murphy’s Law, without predicting Armageddon.

Then we assess whether the impact and likelihood of the worst-case scenario are high or low (see [#how-severity-and-likelihood-are-decided](#how-severity-and-likelihood-are-decided "mention")), and plug the answers into a truth table:

| Software quality | Type     | Impact | Likelihood |
| ---------------- | -------- | ------ | ---------- |
| Blocker          | Blocker  | ✅      | ✅          |
| High             | Critical | ✅      | ❌          |
| Medium           | Major    | ❌      | ✅          |
| Low              | Minor    | ❌      | ❌          |

### How severity and likelihood are decided <a href="#how-severity-and-likelihood-are-decided" id="how-severity-and-likelihood-are-decided"></a>

To assess the severity of a rule, we start from the worst-case scenario (see [#how-severity-and-likelihood-are-decided](#how-severity-and-likelihood-are-decided "mention")) and ask category-specific questions.

{% tabs %}
{% tab title="SOFTWARE QUALITY" %}
**Reliability**

Impact: Could the worst thing cause the application to crash or corrupt stored data?

Likelihood: What’s the probability that the worst thing will happen?

**Security**

Impact: Could the exploitation of the worst thing result in significant damage to your assets or your users?

Likelihood: What is the probability that an attacker will be able to exploit the worst thing.
{% endtab %}

{% tab title="TYPES" %}
**Bugs**

Impact: Could the worst thing cause the application to crash or corrupt stored data?

Likelihood: What’s the probability that the worst thing will happen?

**Vulnerabilities**

Impact: Could the exploitation of the worst thing result in significant damage to your assets or your users?

Likelihood: What is the probability that an attacker will be able to exploit the worst thing?

**Security Hotspot**

Security hotspots are not assigned severities as it is unknown whether there is truly an underlying vulnerability until they are reviewed.
{% endtab %}
{% endtabs %}

### Commercial-level rules

There are commercial-level rules that are available in SonarQube Cloud to all plans. This availability is shown on the Sonar rules page.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-77b6c415f69c84782cf07ab79ff1399b9bc7d0c4%2Fcommercial-level-rules.png?alt=media" alt=""><figcaption></figcaption></figure>

In order for these rules to appear in SonarQube for IDE, it must be in connected mode. In the standalone mode these rules are not visible. See [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") for more information about the connected mode.

### What might change after a software update <a href="#what-might-change-after-an-update" id="what-might-change-after-an-update"></a>

Sonar developers continually re-evaluate Sonar rules to provide the best results. This process is evident in each release and means some rule-specific properties may change after a software update, even in a custom quality profile. This is normal and expected, and is no cause for alarm. The following are rule-specific properties that may change after a software update.

* **Software quality** (security, reliability, maintainability) updates to rules can occur. Changes to a rule’s software qualities will not be applied to issues previously raised by the rule until the project is reanalyzed.
* **Type** (bug, vulnerability, code smell) updates happen on occasion. When a rule type is updated, its value will update automatically in every profile that uses it. Although the rule will be updated, issues previously raised by the rule will remain the same. For example, if a rule transitioned from bug to code smell, the existing issues will retain their original bug type, and new issues will get the new type, code smell.
* **Severity**: Changes to a rule’s default severity will automatically be applied in quality profiles where the default severity was used. Although the rule will be updated, existing issues raised by the rule will remain the same. Note that it is possible to override a rule’s default severity in a profile, and your custom override should remain intact in your Quality Profile after the software update.
* **Tags** include two types: the default tags that come out of the box, and the custom tags added by administrators. When the default tags attached to a rule are updated in SonarQube Cloud, those changes will happen automatically. Custom tags associated with a rule will not change.
* **Key** can change but this is uncommon. Typically this happens in the rare case that, for whatever reason, a key that was non-normal and needs to be normalized. When the key of a rule is changed, related issues are updated as well, so that they remain related to the re-keyed rule.
* **Status** does not affect the operation of a rule and has no impact on its issues. There are three possible rule statuses: ready, beta, and deprecated. Sometimes, rules are first issued in beta status and then moved to ready. Most rules are in ready status; ready to be used in production. When Sonar developers realize that a rule no longer makes sense, they first deprecate the rule, then eventually drop it.

See the [Sonar Rules catalog](https://rules.sonarsource.com/) for a comprehensive list of rules and their properties.

### Rules covered with AI CodeFix <a href="#ai-codefix-rules" id="ai-codefix-rules"></a>

SonarQube Cloud’s AI CodeFix is a feature that uses <code class="expression">space.vars.SQC\_Supported\_LLM\_version</code> to suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++. See the [Sonar AI CodeFix terms](https://www.sonarsource.com/legal/ai-codefix-terms/) for details about the terms of access.

To learn more about which rules are eligible for AI CodeFix, please see the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-cloud/rules-for-ai-codefix#ai-codefix-rules "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [security-related-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-related-rules "mention")
* [security-hotspots](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-hotspots "mention")
* [rules-for-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix "mention")
* [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction "mention") to managing your code issues
* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention")
