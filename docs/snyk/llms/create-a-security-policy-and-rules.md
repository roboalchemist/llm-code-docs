# Source: https://docs.snyk.io/manage-risk/policies/security-policies/create-a-security-policy-and-rules.md

# Create a security policy and rules

To create a new security policy, navigate to **Policies** in your Group menu, and in the Policies manager, expand the **Security policies** category and click **Add new policy**. For details, see [View policies](https://docs.snyk.io/manage-risk/policies/view-create-and-modify-policies).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-422e7a7a047ed0305e49d3df4ea202f46f472ee5%2Fscreenshot_2020-10-20_at_10.01.49_am.png?alt=media&#x26;token=2ebde889-a031-4b3d-8a57-2cc93d7a6ae8" alt="Security policies category expanded"><figcaption><p>Security policies category expanded</p></figcaption></figure>

{% hint style="info" %}
Select **Snyk Default Security Policy** to change the conditions or actions for a security policy that applies to all Projects in all Organizations in the Group.

Security policies are applicable to Snyk Open Source and Snyk Container Projects.
{% endhint %}

## Rules, conditions, and actions

Security policy rules are in the “if, then” format with one or more conditions and an action. An example follows:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-166bf0378825efa9ff813539a8593f0d0bfe3e9a%2Fscreenshot_2020-07-06_at_11.38.07.png?alt=media&#x26;token=fd09ae08-0e0d-43fe-80d3-bde332f0dd51" alt="Security policy rule format with plus sign to add a rule and three dots top right"><figcaption><p>Security policy rule format with plus sign to add a rule and three dots top right</p></figcaption></figure></div>

{% hint style="info" %}
When you create a new security policy, the first blank rule is created automatically.
{% endhint %}

Select the conditions and actions to complete a rule. See [Security policy conditions](https://docs.snyk.io/manage-risk/policies/security-policies/security-policies-conditions) and [Security policy actions](https://docs.snyk.io/manage-risk/policies/security-policies/security-policy-actions) for details.

* To add a new blank rule, click on the plus sign beneath the previous rule.
* To delete or duplicate a rule, click the three dots at the top right of the rule box.

{% hint style="info" %}
The order of the rules you create determines the order they will be applied. If multiple rules with the same action type match the same issue, the rule closest to the top takes precedence over any subsequent rules.

**Example:**

* Rule 1: Sets severity to HIGH for issues with mature exploit maturity.
* Rule 2: Sets severity to LOW for issue ID "CVE-2025-0001".

If an issue with "CVE-2025-0001" also has mature exploit maturity, both rules apply. Because Rule 1 is listed first, the final severity will be HIGH.
{% endhint %}
