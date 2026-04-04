# Source: https://docs.snyk.io/manage-risk/policies/assign-a-policy-to-an-organization.md

# Assign a policy to an Organization

When you create a policy, you can apply it to one Organization. You cannot directly apply an Organization to or remove an Organization from the default policy using the Policy Manager.

{% hint style="info" %}
Policies applied to Organizations are in effect when you run the `snyk test` or `snyk monitor` CLI commands.
{% endhint %}

## Apply a policy to an Organization

To apply a policy to an Organization, in the Organization selector panel, check the box for the Organization to which you want to apply the policy.

If an Organization has another policy applied, you can see that policy from the selector, and the policy indicator next to the Organization name will be gray.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bb5fbec6b20d6c6e2665440692edc3550b880bd2%2Fmceclip3-2-.png?alt=media&#x26;token=0ca88067-ef34-4ddd-8bd9-27533e58d1b1" alt=".Gray indicator - Organization has another policy applied"><figcaption><p>Gray indicator - Organization has another policy applied</p></figcaption></figure></div>

If the Organization already has the policy applied, the name of the policy is displayed in a yellow indicator next to the Organization name.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a7257edb5d1f3217e7ee3a2a1fa689cd4be069ea%2Fmceclip2-6-.png?alt=media&#x26;token=8f837b5d-4752-4deb-8004-4bdc01f9f3df" alt="Yellow indicator - Organization already assigned to this policy"><figcaption><p>Yellow indicator - Organization already assigned to this policy</p></figcaption></figure></div>

If you are applying a different policy to an Organization, in order to move that Organization from one policy to another, two indicators appear next to the Organization name in the selector. One shows, in yellow, the policy that is currently applied. The other shows the policy you will be applying to the Organization in gray.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5bb3a0c771022dfa63f8493339ee0826647aa23c%2Fmceclip1-16-.png?alt=media&#x26;token=649e17d7-a989-4753-a6f2-76d44462cceb" alt="Gray and Yellow indicators - Policies applied to the Organization and to be applied"><figcaption><p>Gray and Yellow indicators - Policies applied to the Organizaiton and to be applied</p></figcaption></figure></div>

## Remove a policy from an Organization

To remove a policy from an Organization, uncheck the box next to the Organization you want to remove from the policy that you are viewing.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4896e997211d99abdb0850a17a238f6d41e14b32%2Funtitled-2-.png?alt=media&#x26;token=6949741f-8a75-4e05-a99e-f632a3953457" alt="Remove an Organization from a policy"><figcaption><p>Remove an Organization from a policy</p></figcaption></figure></div>

The unchecked Organization will now automatically revert to the default policy.

## Apply the default policy to an Organization

Remove the policy currently applied to the Organization. The Organization will automatically revert to the default policy.

## Remove the default policy from an Organization

Apply a new policy to the Organization. The Organization will automatically be removed from the default policy and the new policy will be applied.
