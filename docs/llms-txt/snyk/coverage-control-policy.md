# Source: https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/coverage-control-policy.md

# Coverage control policy

You can use the **Set Coverage Control** action from the Policies view to identify your application assets, monitor them, and prioritize the risks. You can select one or multiple security products and also specify a timeframe for when the last scan should have taken place.

Identifying and setting coverage policies allows your team to define where certain security controls are expected to be in place.

The following example filters out assets that should have Snyk Open Source and Snyk Code security controls in place and then sets the coverage policies.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fe28dd27b1db470d3796d3df56ad2093a458e471%2Fimage%20(126).png?alt=media" alt="AppRisk - Setting up a Coverage Control policy"><figcaption><p>Assets Policy - Setting up a Coverage Control policy</p></figcaption></figure>

To follow the example, these are the filters you need to apply:

* **Filter 1**: include only assets that are repositories.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3a7e2fd203a024437a630318463bb24775749e8f%2Fimage%20(127).png?alt=media" alt="Filter configuration for asset type" width="350"><figcaption><p>Filter configuration for asset type</p></figcaption></figure>

* **Filter 2**: include assets that have coding language tags relevant to your application (Apex, ASP, C, C#, C++, CMake, Go, HTML, Java, JavaScript, Kotlin, PHP, Python, Ruby, Scala, Swift, TypeScript, VisualBasic, Handlebars, Makefile, Objective-C).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c924770c5e0a67b83e77e9d2f23b93ea6d873024%2Fimage%20(129).png?alt=media" alt="Filter configuration for tags" width="354"><figcaption><p>Filter configuration for tags</p></figcaption></figure>

Next, you need to define two actions, one for Snyk Open Source, and one for Snyk Code, since the example is focused on these two security controls.

* **Action 1**: add a Set Coverage Control Policy action with Snyk Open Source selected.

  In Snyk, by default, Open Source manifest files that are imported using the SCM integration are scanned on a daily basis. The Coverage Control Policy needs to check that a Snyk Open Source scan occurred for that repository in the last two days.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7ed509b10907a0851972f044905b5f72115e7362%2Fimage.png?alt=media" alt="Filter configuration for coverage control" width="352"><figcaption><p>Filter configuration for coverage control</p></figcaption></figure>

* **Action 2**: add a Set Coverage Control Policy action with Snyk Code selected.

  For Snyk Code, scans happen by default once a week, or when changes have been pushed to the monitored branch. The Coverage Control Policy needs to check that a Snyk Code scan occurred for that repository in the last week.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ac9d37fe91f7838a5ea9006f6222a98c529064b1%2Fimage%20(131).png?alt=media" alt="Filter configuration for coverage control" width="350"><figcaption><p>Filter configuration for coverage control</p></figcaption></figure>

In the Inventory view, any coverage gap is indicated with strikes through the control coverage icon. See more details about each icon on the [Inventory capabilities](https://docs.snyk.io/manage-assets/assets-inventory-components) page.

The following video explains how to configure a Coverage policy:

{% embed url="<https://res.cloudinary.com/snyk/video/upload/v1737656949/snyk-learn/product-training-videos/Snyk_Essentials_and_Snyk_AppRisk_-5d_-_v1_-_Policy_editor_-_Coverage_policy_example.mp4>" %}
Asset coverage policy example
{% endembed %}
