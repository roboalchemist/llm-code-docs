# Source: https://docs.snyk.io/snyk-api/reference/policies.md

# Source: https://docs.snyk.io/manage-risk/policies.md

# Policies

{% hint style="info" %}
**Feature availability**

Policies are available only with Snyk Enterprise plans and apply only to Snyk Open Source scans. For more information, see [plans and pricing](https://snyk.io/plans/).

The `.snyk` file is a policy file that Snyk uses to define specific analysis behaviors for Open Source, Snyk Code, and Snyk IaC. and to specify patches for the CLI and CI/CD plugins. See [The .snyk file](https://docs.snyk.io/manage-risk/policies/the-.snyk-file) for details.
{% endhint %}

Snyk policies contain rules to define how Snyk behaves when encountering specific types of Open Source issues. With policies, you can identify types of issues based on conditions, such as `no exploit available`, and then apply actions to these issues, such as changing the severity. Thus by using customizable Snyk policies, you can define actions for specific types of issues encountered in scanning.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b9765625d9be0504acad00c2d78a078465170f05%2Fimage%20(112)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(2)%20(1)%20(2).png?alt=media&#x26;token=215ef0bc-180c-4d0a-a03f-49c82b6488b3" alt="Snyk Policy manager"><figcaption><p>Snyk Policy manager</p></figcaption></figure></div>

Using the Snyk Policy Manager, you can view, create, and edit policies. For details, see [View, create, and modify policies](https://docs.snyk.io/manage-risk/policies/view-create-and-modify-policies).

## Benefits of Snyk policies

Policies give you a quick and automated way to identify and triage issues that are irrelevant to or unimportant in your application development. This reduces the noise level, saving valuable development time and allowing developers to take more responsibility for and ownership of security.

Policies help prioritize issues to address and can ensure vulnerable or non-compliant components do not escape notice. Policies are part of the governance framework of your company.

For more information, see [Use policies in the SDLC](https://docs.snyk.io/manage-risk/policies/use-policies-in-the-sdlc).

## Categories of policies

Snyk has security and license policies.

* [Security policies](https://docs.snyk.io/manage-risk/policies/security-policies) define Snyk behavior in treating vulnerabilities, for example, according to severity levels or ignored issues.
* [License policies](https://docs.snyk.io/manage-risk/policies/license-policies) define Snyk behavior in treating license issues, such as allowing or disallowing packages with certain license types and avoiding the use of packages containing incompatible licenses.

## Assign **policies to Projects or Organizations**

Different applications may need to be scanned according to different policies. Mission-critical applications are likely to need more control than internal applications in a sandbox environment. You can establish the needed control by assigning policies to:

* [Projects](https://docs.snyk.io/manage-risk/policies/assign-policies-to-projects), after applying attributes to Projects and policies to attributes
* [Organizations](https://docs.snyk.io/manage-risk/policies/assign-a-policy-to-an-organization) in a Snyk Group
