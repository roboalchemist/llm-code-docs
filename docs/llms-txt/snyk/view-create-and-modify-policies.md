# Source: https://docs.snyk.io/manage-risk/policies/view-create-and-modify-policies.md

# View, create, and modify policies

## View policies

{% hint style="info" %}
You must be a Group administrator to view, create, and modify policies for that Group.
{% endhint %}

Select the **Policies** menu option to see the policies in your Group, arranged by category, [License policies](https://docs.snyk.io/manage-risk/policies/license-policies), and [Security policies](https://docs.snyk.io/manage-risk/policies/security-policies).

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8da9fbb0b280a589aa8f4146cdd6bc1fada984c1%2FPolicies-menu.png?alt=media" alt="View policies"><figcaption><p>View policies</p></figcaption></figure></div>

Expand a category to see a list of the policies in that category:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3f82d5169bd22a26be83cbd055cb5b5d12bdccdf%2Fsnyk-policy-manager.png?alt=media" alt="License policies list expanded"><figcaption><p>License policies list expanded</p></figcaption></figure>

{% hint style="info" %}
This list includes the [default policy](#default-policies), which is automatically created for new Groups for each policy category and cannot be removed.
{% endhint %}

### Policy details

When you expand a category, the screen shows the policies applied to **Project attributes** and applied to **Organizations**. You can click to **Learn which policies take precedence** in each category. You can also search for a particular policy.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-552fefa87ca0cbcc4b129d66089060d003fbbe54%2Fscreenshot_2021-03-26_at_11.04.50_am.png?alt=media&#x26;token=b3279156-463e-4190-af18-d146dae8d696" alt="Policy manager screen including attributes and Organizations to which each policy is applied"><figcaption><p>Policy manager screen including attributes and Organizations to which each policy is applied</p></figcaption></figure>

### Default policies

Each policy category has a default policy. Default policies can be applied only to Organizations, not Project attributes.

When you create a new Organization, it will automatically be added to the default policy unless you have copied the settings of an existing Organization. You can assign an Organization to a different policy if desired.

The default policy cannot be deleted; however, the default policy name, description, and rules can be edited to match your preferences. A default policy can also contain no rules if you'd prefer.

See [Assign a policy to an Organization](https://docs.snyk.io/manage-risk/policies/assign-a-policy-to-an-organization) for details.

The Policy Manager allows you to [create](#create-a-policy), [edit](#edit-a-policy), and [duplicate or delete a policy](#duplicate-or-delete-a-policy).

## Create a policy

1. On the Policy Manager screen, select **Add new policy** and in response to the prompts, enter the details.
2. Enter a policy name and a description to help you quickly identify a policy.\
   Policies in the same category cannot have the same name. You cannot save a policy without a name.
3. Select whether to apply the policy to Organizations or Project attributes.
4. Select the [Organizations](https://docs.snyk.io/manage-risk/policies/assign-a-policy-to-an-organization) or [attributes](https://docs.snyk.io/manage-risk/policies/assign-policies-to-projects) to which you want to apply the policy.
5. Add rules to the policy. See [Create a license policy and rules](https://docs.snyk.io/manage-risk/policies/license-policies/create-a-license-policy-and-rules) or [Create a security policy and rules](https://docs.snyk.io/manage-risk/policies/security-policies/create-a-security-policy-and-rules).
6. Click **Submit** to create and save the policy.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c0b67338608e2383583971398c5e9b3338be9c10%2Fscreenshot_2020-05-26_at_9.47.26_am.png?alt=media&#x26;token=6583a015-ea4f-4ed1-8491-521e0a08eca6" alt="Create a policy" width="563"><figcaption><p>Create a policy</p></figcaption></figure></div>

## Edit a policy

1. Click the name of an existing policy in the Policy Manager tab to make any changes.
2. Change the [Organizations](https://docs.snyk.io/manage-risk/policies/assign-a-policy-to-an-organization), [attributes](https://docs.snyk.io/manage-risk/policies/assign-policies-to-projects), and rules as you wish.
3. Click **Submit** to save your changes.

## Duplicate or delete a policy

To duplicate or delete a policy, click the three dots on the right-hand side:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-08c9793f89d8b2608547cf83e573db98e20059fc%2FScreenshot%202023-03-28%20at%2016.42.45.png?alt=media" alt="Other policy actions"><figcaption><p>Duplicate or delete a policy</p></figcaption></figure></div>

Duplicating a policy copies the rules of a policy but not the assigned Organizations or Projects. The new policy is automatically called **Copy of (Policy Name)…** and can be edited as [explained in Edit a policy](#edit-a-policy).

{% hint style="info" %}
Deleting a policy cannot be undone. If you delete a policy with Organizations assigned to it, those Organizations will return to the default policy.
{% endhint %}
