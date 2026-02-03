# Source: https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/classification-policy.md

# Classification policy

You can use the **Set Asset Class** action from the Policies view to classify the assets based on importance, where class A is the most important and class D is the least important.

You can set the asset class based on:

* the repository name
* the asset labels

{% hint style="info" %}
Snyk Essentials identifies GitHub and GitLab topics as asset labels.
{% endhint %}

Use the classification policy to give business context to your application. When you set up a classification policy, all your assets are automatically classified.

If you just started using the classification policy, the recommendation is to focus first on the Class D assets, since they are the least important.

The following example filters the assets that contain `sandbox`, `test`, and `to-delete` in their names. In Snyk Essentials, GitHub and GitLab topics are pulled in from the SCM integration and applied to repository assets, so if topics like `PCI-Compliance` have been added to repos in the SCM, Snyk can take those tags in Snyk Essentials and classify those assets as Class A.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-384193e1d1f233abe15a5cf7e4fd35457373b38a%2FCreate%20policy.png?alt=media" alt="AppRisk - Setting up filters for a classification policy"><figcaption><p>Assets Policy - Setting up filters for a classification policy</p></figcaption></figure>

After you set up the filters, you need to apply a Class D asset classification to those assets.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5de9ac02cde46c1ac2edcc6df0b7a14e0413c320%2FSet%20action.png?alt=media" alt="AppRisk - Setting up actions for a classification policy"><figcaption><p>Assets Policy - Setting up actions for a classification policy</p></figcaption></figure>

You can apply a similar pattern and create actions for Class A, B, and C assets, within the same policy.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9600314d93f24abf109441356012b34ce6ff8aa2%2FSet%20Class.png?alt=media" alt="AppRisk - Setting up multiple actions for a classification policy"><figcaption><p>Assets Policy - Setting up multiple actions for a classification policy</p></figcaption></figure>
