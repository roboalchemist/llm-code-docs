# Source: https://docs.icepanel.io/other-information/faq.md

# FAQ

## Can diagrams be embedded in other documents and pages?

Yes! See [sharing](https://docs.icepanel.io/collaboration/sharing "mention") for details.

### How do I share feature suggestions?

Submit your ideas through our [Feedback](https://feedback.icepanel.io/) portal, where you can also vote on other users’ suggestions.\
\
We actively review these posts to gauge interest and prioritize future development. You also get notified when a feature that you upvoted gets released!&#x20;

### I have an issue, how do I get help?

Start by reviewing the [troubleshooting](https://docs.icepanel.io/other-information/troubleshooting "mention") page. If your issue isn’t covered, you can:

* Contact your Customer Success Manager (Scale customers).&#x20;
* Use the Contact Us feature in the Help Center.
* Email <mail@icepanel.io> (if Contact us feature isn’t accessible)

For technical issues, including a recording is preferred, as it provides the most complete context. Screenshots and detailed reproduction steps are also helpful.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FIYOn2HooVX3glsUyNF6u%2Fimage.png?alt=media&#x26;token=62343118-d1c1-4e41-80ac-bd151a090614" alt=""><figcaption><p>Getting help</p></figcaption></figure>

When using Contact Us, be sure to select the appropriate I need help with option to ensure you receive the support you need:

* *Support* - An immediate issue you need resolved ASAP
* *Bug* - An unexpected behavior that can be addressed in a future release
* *Sales* - Questions regarding billing or licenses
* *Other* - Miscellaneous inquiries

### Where are the objects and connections from my other diagram?

Changes to model objects and connections propagate across the model, but diagrams display only what has been explicitly added.

Our reasoning for this design choice is that each diagram is meant to tell a specific story, so automatically adding objects from other diagrams often disrupts the intended narrative.

Instead, a number of tools are provided to support quickly adding existing content to any diagram, including:

* Each of the features shown in [Adding existing objects](https://docs.icepanel.io/core-features/diagramming#adding-existing-objects)
* Toggling connections on/off, as shown in [Viewing dependencies and connections of an object](https://docs.icepanel.io/core-features/diagramming#viewing-dependencies-and-connections-of-an-object).

### Why am I getting an “already exists” error?

Each model object must have a unique name within its scope. Violating this rule raises an “already exists” error.

In practice, this means that a model object cannot share a name with another object that:

* Share the same parent, or
* Reside higher in the hierarchy within the same Domain.

Otherwise, sharing names is allowed.

This lets you apply the same naming conventions across Systems, as long as no ambiguities arise. For example, each system can have a Store named “database” and an App named “front-end” without issue.

### Why isn’t the Technology I want available?

There are a lot of technologies out there, so we probably just haven’t added it yet!

You can add a new [technology-choices](https://docs.icepanel.io/visual-storytelling/technology-choices "mention") by following [Adding a new technology](https://docs.icepanel.io/visual-storytelling/technology-choices#adding-a-new-technology). Once added, it is immediately available to all users in your organization.

### Can I change multiple objects at once?&#x20;

Yes, IcePanel supports multi-selection! Options include:

* Multi-select / unselect: Shift + Click (each object)
* Multi-select box: Shift + Click + drag

Changes made while a selection is active apply to all objects it contains. Common use cases include:

* [Add or remove from Group](https://docs.icepanel.io/core-features/modelling/groups#multi-select-assigning-groups-to-objects)
* [Add or remove Tag](https://docs.icepanel.io/visual-storytelling/perspective-tags#adding-a-tag-to-an-object)
* [Remove from diagram](https://docs.icepanel.io/core-features/modelling#removing-model-objects-from-a-diagram)
* [Delete from model](https://docs.icepanel.io/core-features/modelling#deleting-objects-from-the-model)

See the [hotkeys](https://docs.icepanel.io/other-information/hotkeys "mention") article for more useful shortcuts!

### Should Interfaces be modeled as objects or connections?

Many interfaces meet the criteria for Systems and are therefore best modeled as objects.

<table data-header-hidden><thead><tr><th width="74.33984375"></th><th></th><th></th></tr></thead><tbody><tr><td>#</td><td>Criteria</td><td>Interface</td></tr><tr><td>1</td><td>Delivers value to its users, whether they are human or not.</td><td>✔ Transforms and transports data between Systems.</td></tr><tr><td>2</td><td>Owned and maintained by a single technical team.</td><td>✔ Typically managed by a middleware or data team</td></tr></tbody></table>

For diagrams aimed at non-technical audiences, using the[via property](https://docs.icepanel.io/core-features/diagramming#connection-via-property) of Connections to reference interfaces instead of explicitly showing them can help reduce visual noise.

***

Any other questions? Reach out to us <mail@icepanel.io> 🧊
