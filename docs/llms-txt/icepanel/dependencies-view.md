# Source: https://docs.icepanel.io/core-features/dependencies-view.md

# Dependencies view

{% hint style="info" %}
The dependencies view is available on all plans.
{% endhint %}

Identifying critical parts of your system is key to understanding risk and vulnerabilities. The dependency view helps you investigate parts of your system based on incoming and outgoing connections across your model.&#x20;

We recommend using this view to answer things like:

* What systems, apps, or components have a lot of dependencies (and therefore risk)?
* What's the complexity of updating a system, app, or component?
* What third-party entities is my system exposed to?

With the dependency view, answering these questions becomes easy once a complex model is built over time. Instead of diagramming these views, you get them out of the box from your model.

## Using the Dependencies view

To view dependencies, click on the `Dependencies` tab from the landscape view. By default, the internal system with the most connections will be selected as the object of focus.

Here, you'll be able to:

* Select an object of focus (system, app, component, actor)
* Search incoming or outgoing dependencies of an object
* View and edit object details of dependencies
* View connections (direct, lower) between an object and a dependency

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FvD5rxsVdZyFxTGgDBGm7%2FDependencies-view.gif?alt=media&#x26;token=b3a63d9c-62d8-48db-bbb7-20b3e4c0db24" alt=""><figcaption><p>Viewing dependencies in IcePanel</p></figcaption></figure>

{% hint style="info" %}
The connections count represents the number of unique **direct** connections (lower connections are not included).
{% endhint %}

## Viewing dependencies from a diagram

To view the dependencies of an object in a diagram, navigate to the `Connections` tab in the object details panel and click on the `View dependencies` button.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FDcKjDNPFrSbzHILu0Ahj%2FDependencies-Diagram.gif?alt=media&#x26;token=3d1f491e-e191-4a84-8525-079041a20f13" alt=""><figcaption><p>Viewing dependencies of an object in a diagram</p></figcaption></figure>

&#x20;
