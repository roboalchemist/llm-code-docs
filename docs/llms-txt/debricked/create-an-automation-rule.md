# Source: https://docs.debricked.com/product/automation/create-an-automation-rule.md

# Create an automation rule

1. Go to **Automations** on the left side menu (You can also access automations for a specific repository by clicking the **Automate** button on the top right corner).
2. Click the **+New** button, then **+New rule**.
3. Select the repository(s) you want the rule to be applied to.
4. Build your if-statement:
   1. Choose criteria for the rule to trigger. For example, *CVSS is at least high (7.0-8.9).* Click **AND or OR** to add a new criterion. You can select multiple criteria connected by the operators. See below for more information.
   2. Choose an action to be executed when the condition is true. For example, fail pipeline. See below for more information.
5. If you do not want the rule to apply for vulnerabilities that have been marked as unaffected by you or someone on your team, leave the pre-filled checkbox in the bottom right checked.
6. Click **Generate rule** and review any warnings (if applicable). Make sure that the statement corresponds to what you were looking to achieve with your rule.
7. Click **Save.**

### Rule conditions <a href="#ruleconditions" id="ruleconditions"></a>

Rules can incorporate multiple OR and AND operators. When working with multiple criteria and operators, the following precedents are applied:

* AND conditions inherit previous IF or OR conditions
* OR conditions do not inherit the previous IF or OR condition

### Rule actions <a href="#ruleactions" id="ruleactions"></a>

You can select one of the following actions to be performed once a rule is triggered:

* Fail pipeline - If the rule conditions are met, your pipeline fails.
* Pipeline warning:
  * GitHub - If the rule conditions are met, your pipeline passes, the pipeline check is set to neutral, and a warning is printed.
  * GitLab, Bitbucket and Azure DevOps - If the rule conditions are met, your pipeline passes, and a warning is printed.
* Notification by email - If the rule conditions are met, you receive an email notification.
* Notify user groups by email - If the rule conditions are met, all users in a chosen user group receive an email notification.
* Mark as unaffected - If the rule conditions are met, the affected vulnerabilities are marked as unaffected.
* Flag as vulnerable - If the rule conditions are met, the affected vulnerabilities are marked as vulnerable.
* Trigger webhook - If the rule conditions are met, a webhook is sent.&#x20;

### Missing CVSS score  <a href="#whatifthecvssscoreismissing" id="whatifthecvssscoreismissing"></a>

Rules that use the CVSS score as one of the conditions, might not trigger for vulnerabilities that lack a CVSS score. This does not mean that the vulnerability is not severe, but that the data source lacked the CVSS score information. To account for this, you can add the statement:

*OR CVSS is missing*

Keep in mind that adding the OR statement does not take previous IF or AND statements into consideration.&#x20;

### Production dependencies

{% hint style="info" %}
This option is currently supported for Javascript (Yarn, NPM), Nuget, Java (Maven, Gradle), PHP (Composer), Python (requirements.txt), and Go.
{% endhint %}

You can make your policies or automations only trigger if the related dependency is used in production, to reduce the number of false positives or very low-risk triggers. To set this up, simply add another condition to the rules you want triggered only for non-dev dependencies:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FnLVABd4P2KfvNfX1IEgC%2FDependency_scope_production.png?alt=media&#x26;token=a13afe8d-f974-4bd8-9106-3ca0726bf7a1" alt=""><figcaption></figcaption></figure>

### Automation rule examples <a href="#automationruleexamples" id="automationruleexamples"></a>

* **Prevent new dependencies with vulnerabilities**

  Imagine you have a developer branch called dev where you add new exciting features. Being security-aware, you want to fail the pipeline if a new commit introduces a new vulnerability with a severity of high or more. You also want to be notified of this incident.
* **Prevent unknown license families and GPL**

  In this scenario, OpenText Core SCA fails the pipelines if there are dependencies with either an unknown license family, or if the dependencies have any of the GPL-2.0 and AGPL-3.0 licenses. OpenText Core SCA also notifies all the administrators for the company account.
