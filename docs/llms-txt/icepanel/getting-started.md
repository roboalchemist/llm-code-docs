# Source: https://docs.icepanel.io/getting-started.md

# Getting started

## The basics

IcePanel is an interactive modelling and diagramming tool that uses the [C4 model](http://www.c4model.com) to help you communicate your team's system architectures in a structured way. It helps explain how things work to your audiences through an abstraction-first approach, overlaying details when needed.

With the C4 Model, you can drill down or zoom in and out of different levels of detail, depending on the audience you're communicating your designs to. In most software teams, this is a mix of technical (developers, architects, operations, etc.) and non-technical people (product, business stakeholders, etc.).

Using modelling instead of diagramming alone removes much of the maintenance headache of keeping multiple diagrams up-to-date, as changes sync automatically through all your diagrams.

## Quick start guide

Getting started in IcePanel is simple. Here is a quick example to follow so you can have robust system documentation that will help you educate, learn, make decisions and plan future developments (*which also look pretty cool* 😎).

### Step 1: Create your first context view

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F2xppWPLq68m8rB6NEfSI%2Fgetting-started-1-h.gif?alt=media&#x26;token=2256f7cb-2091-4235-87a2-230c33f2688d" alt=""><figcaption><p>Add Actors, Systems, and Connections</p></figcaption></figure>

1. Create a [landscape](https://docs.icepanel.io/core-features/landscape) (if you haven't already)
2. Add the top-level objects for your design, such as:
   * The system(s) your company develops (start with 1)
   * Third-party systems you depend on
   * People who use your solution, such as customers
3. Add connections between the different objects, highlighting their high-level relationships.

{% hint style="info" %}
Adding and editing objects in diagrams automatically adds them to your model to be re-used later.
{% endhint %}

#### 🤔 What this is for

This is the context level ([Level 1](https://c4model.com/#SystemContextDiagram)) of the C4 model, and the focus here is the big-picture view of your system architecture. This will mainly show how your system(s) solve your customer's problems, remaining primarily at the business level, so keep it simple!

#### 👥 Target audience

Everyone! Anyone in or out of your company who needs a high-level overview of how your system(s) work. Perfect for your business, product, or other non-technical peers, as well as onboarding new technical teammates.

#### 📋 Make sure to

1. Name your objects in a way anyone can understand.
2. Label all connections so the relationships are clear.

### Step 2: Zoom into a system and add your apps/stores

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FNS92zFaalFpO7RUWLDHy%2Fgetting-started-2-h.gif?alt=media&#x26;token=0d0fc820-e219-4d8d-95a6-6f94e2eb2bfe" alt=""><figcaption><p>Zoom-in and add Apps and Stores</p></figcaption></figure>

1. Zoom into a System (using the +🔍 icon on the top left of the system).
2. Add the Apps and Stores that are inside the primary system.
3. Connect them to show messages or relationships between them.

#### 🤔 What this is for (Container Diagram Level)

This is the App level ([Level 2 - known as Container diagram in C4](https://c4model.com/#ContainerDiagram)). It shows the individually deployed/runnable units in each System that execute or store code.

#### 👥 Target audience (Container Diagram Level)

Mainly technical people, such as architects and developers. Some product people (such as product owners, product managers, or business analysts) will gain value here, especially for planning purposes.

#### 📋 Make sure to (Container Diagram Level)

1. Name your objects in a way anyone can understand.
2. Label all connections so the relationships are clear.

### Step 3: Add existing objects from the level above

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FtltzEUa7SSQPyWgY6lta%2Fgetting-started-3-h.gif?alt=media&#x26;token=7f0e2c57-3d0d-499b-a4be-86f09baf0382" alt=""><figcaption><p>Add objects from the level above</p></figcaption></figure>

Because we're using a model, we can add objects from higher levels here, such as other systems you depend on or the people interacting with your solution.

1. Add your Actors and Systems from the level above by either:
   1. Double-clicking in the diagram and typing their name.
   2. Going to the "Model objects" tool on the left and drag them in.
2. Add the connections to the apps/stores inside the system from previously created connections.

You can create multiple diagrams to show different views of your model. Examples include customer-specific views, focusing on one object, and current vs. future design.

{% hint style="info" %}
Connections that were created at a higher level will show as higher connections.
{% endhint %}

### Step 4: Assign tech choices

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F20F1Idh7x4uVN6hIoY8T%2Fgetting-started-4-h.gif?alt=media&#x26;token=e8bbeae2-79dc-4ee7-b639-e69a2bd948f4" alt=""><figcaption><p>Assign tech choices to your objects</p></figcaption></figure>

Once you have your Apps and Stores laid out and connected, start adding any tech choices, such as what service in AWS, GCP or Azure service, languages, libraries or frameworks, etc.

1. Select your model object. You can multi-select objects by holding the `Shift` key.
2. Go to the technology section on the right-hand panel.
3. Search for your tech choice and add it.

These choices come with docs preassigned and a simple description for those unfamiliar. These can be used later to highlight tech choices using the [tags bar](https://docs.icepanel.io/visual-storytelling/perspective-tags), allowing people to learn your architecture's technical choice landscape and filter your model.

### Step 5: Describe each object and diagram

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FzEdcOaeEDXZXDS4vG0FV%2Fgetting-started-5-h.gif?alt=media&#x26;token=d131a59b-96f1-47fc-a9c7-d60633368b32" alt=""><figcaption><p>Add descriptions to your objects</p></figcaption></figure>

Each object and diagram has a description, which adds details to help your teammates understand how things work. Descriptions follow that object wherever it is.

The **minimum** you should add is a brief displayed description for each object. This might seem obvious, but it will help your teammates (especially new ones).

1. Select an object.
2. Go to the right-hand panel.
3. Add a displayed description to each object (max 120 characters).

Try to explain:

* What the object is.
* What its primary responsibilities are.

Use the detailed description field to show other useful information, such as a link to the appropriate repository.

{% hint style="info" %}
The detailed description field supports Markdown, so you can quickly import your existing documents and formatting manually or through our [API](https://docs.icepanel.io/integrations/rest-api).
{% endhint %}

### Step 6: Create your first Flow

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FBOUd7s0Z28wKmtfCrGR3%2Fgetting-started-6-h.gif?alt=media&#x26;token=9a1a1bb3-33d3-45e4-9fed-09799f9b34df" alt=""><figcaption><p>Create your first Flow</p></figcaption></figure>

Your Systems architecture doesn't live in a static world without interactions and data flows, so neither should your diagrams. Flows allow you to show how your system works in multiple scenarios or user journeys on the same view.

1. Click `Create flow` in the diagram Flows tab at the bottom left of the screen. Name your Flow.
2. Select the object or connection you want to show in your first step.
3. Click `+ Step` on the left.
4. Add an optional description to the step.
5. Keep adding steps to show the rest of the flow.
6. Use the `Back` and `Next` buttons to step through your flow when complete.

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>👉 See flows for more</td><td></td><td></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FpFKifwmbJc2Vx3uM4FMy%2FFlows.png?alt=media&#x26;token=0ccd6157-d452-4491-88c6-9aea0f93fe7b">Flows.png</a></td><td><a href="visual-storytelling/flows">flows</a></td></tr></tbody></table>

### Step 7: Add and view Tags to show different perspectives

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F346ZCCpA6bFtkdN4B2xG%2Fgetting-started-7-h.gif?alt=media&#x26;token=8042db25-36c0-4d76-81b0-8c7c264c591f" alt=""><figcaption><p>Add tags to your objects</p></figcaption></figure>

Tags allow you to show multiple perspectives of your diagrams without duplicating them. Use Tag groups to show different information, such as deployment information, the risk, or the cost of your model.

1. Open the Tags bar at the bottom of the screen.
2. Click an object to open the details in the right-hand panel.
3. Click the `Add tags` button.
4. Add tags that apply to the tag group you want to show.
5. Hover over the tags in the bottom tag bar to highlight them. You can also click on them to pin them or select the hide/focus options.

Tags are a great way to change the focus of your design with little effort and help target specific areas of focus for each of your audiences.

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>👉 See Tags for more</td><td>👉 See tags for more</td><td></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fr8sKbRP6ZXIeUE0tpnJb%2FTags.png?alt=media&#x26;token=1e1a9b4b-4121-4430-a28c-2cc9e313d118">Tags.png</a></td><td><a href="visual-storytelling/perspective-tags">perspective-tags</a></td></tr></tbody></table>

### Step 8: Collaborate with your teammates and Share

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FoP6DB2OOfDC06hGxuEPa%2Fgetting-started-8-h.gif?alt=media&#x26;token=51de3349-49d6-4863-baaa-d4340dcd5ebd" alt=""><figcaption><p>Share your diagram</p></figcaption></figure>

IcePanel is a collaborative tool for your whole team. Getting others involved helps you gain knowledge from across your business. Invite them as viewers (unlimited and free on all IcePanel plans) or create interactive read-only share links of your designs. [sharing](https://docs.icepanel.io/collaboration/sharing "mention") are a great way to showcase your designs without them needing an account using just a browser.

#### Invite your teammates:

1. Click the `Share` button in the top right of the screen.
2. Type the emails of the people you want to invite to your team.
3. Send invitations.

**Create share links:**

1. Click the `Share` button in the top right of the screen.
2. Navigate to the `Share link` tab.
3. Toggle on share links.
4. Copy and paste the link to anyone you want to show your designs.

{% hint style="info" %}
Wherever you are when you create a share link will be where your audience lands when opening the URL. This includes position, selected object, Flow, Tags etc.
{% endhint %}

### Step 9: Create your first version

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Ff8WmPkW22x0NzTQwVqcA%2Fgetting-started-9-h.gif?alt=media&#x26;token=af70bcf4-d02d-47ea-9380-780ecec63a64" alt=""><figcaption><p>Create a version of your landscape</p></figcaption></figure>

You can create versions of your landscapes to track changes and use the timeline to visualize how your architecture has evolved.

1. Click the `Current` drop-down at the top left of the canvas.
2. Click the `Create version` button.
3. Name your version and add notes (this will help you and others in the future).
4. Click the `Create version` button to confirm.
5. Select the `Current` drop-down to view the version timeline.

### That's the basics!

Congratulations! You've started your journey into interactive architecture documentation that remains up-to-date and can be accessed by all your teammates!

### What next?

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td>Modelling</td><td></td><td></td><td><a href="core-features/modelling">modelling</a></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FrALlzS1MgXjwkmvhkD8h%2FModelling%20-%20banner.png?alt=media&#x26;token=6a14213e-0ff0-4b3b-b079-db06f4d3b757">Modelling - banner.png</a></td></tr><tr><td>Diagramming</td><td></td><td></td><td><a href="core-features/diagramming">diagramming</a></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Ff7dkXanF1WuebS3aKGlm%2FDiagrams%20-%20banner.png?alt=media&#x26;token=69e50998-2200-466a-84a2-6c689e613438">Diagrams - banner.png</a></td></tr><tr><td>Dependencies</td><td></td><td></td><td><a href="core-features/dependencies-view">dependencies-view</a></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F76NWVA0M1VkzEruaZgSY%2FDependency%20view%20-%20banner.png?alt=media&#x26;token=28838a2a-caf7-40c3-a6c8-e42b390a0d21">Dependency view - banner.png</a></td></tr></tbody></table>

***

Still need help? Let us know at <mail@icepanel.io>, and we'll respond as soon as we can!
