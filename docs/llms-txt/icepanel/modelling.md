# Source: https://docs.icepanel.io/core-features/modelling.md

# Modelling

IcePanel uses a modern, lightweight, and agile way to model system architecture using the [C4 Model](http://c4model.com) - *created by Simon Brown*. This helps create simple, easily digestible, and maintainable diagrams targeted at each of your audiences.

Using modelling instead of diagramming tells the full story, not just a single diagram view.

Using the C4 model, you can create different hierarchical diagrams that explain how your solution works, from the high-level business of your systems to the low-level technical details.

IcePanel makes it easy for anyone (technical or non-technical) to use this powerful way to visualize software.

## What is modelling?

Modelling (*in software architecture*) is a way to see the **full picture** of how your system(s) work. It is view-agnostic and provides more detail than a single diagram.

## Why is modelling better?

There are a few core benefits of a model-based approach, as opposed to just diagramming (i.e. with just shapes and lines):

### 1. Reusability

You can reuse the same objects, including all existing connections and previously assigned metadata.

### 2. Syncing diagrams

When you change the reusable object, it updates in all other places it was referenced, massively reducing maintenance.

### 3. Deeper insights

Because your objects live in a source of truth, you can analyze how they're being used, what objects have specific traits or technologies, and more!

### 4. Consistency&#x20;

You can visualize your solutions consistently when paired with a standard modelling language, such as the C4 model. This means you don't have to relearn how others think a diagram should look, making conversations flow better.

## What is the C4 model?

Simon Brown created the C4 model to resolve the pains of explaining and communicating software architecture in the agile world. It acts as a map of your system, starting at the high-level detail (imagine looking at the whole world on Google Earth) down to the low-level technical details needed to develop your product (zooming into your street).

It is a way to communicate design decisions to multiple audiences at the level of detail they need. From business logic to technical decisions, the C4 model makes it easy to maintain in the long run when changes inevitably occur to your design.

## 🔢 The 4 C's in C4

The 4 C's relate to the different levels of detail in the diagrams created from the model.

### 1️⃣ Level 1 - Context diagrams

<div align="center"><figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F46NKgyIWMDPcCzczvWPL%2Flevel-1.png?alt=media&#x26;token=4168b272-7a45-4279-a4b4-c8d09285e609" alt="" width="328"><figcaption><p>Level 1 - Context diagram breakdown</p></figcaption></figure></div>

**The big picture**—high-level overviews of how your system(s) work in the overall ecosystem with other external systems and the people who use them (users, customers, etc.).

**Scope** - Systems (internal and external) and actors.

**Intended audience** - Anyone! Business, Product, Architects, Developers and Operations.

***

### 2️⃣ Level 2 - Container diagrams

{% hint style="info" %}
We call these App diagrams in IcePanel, as "Container" is more commonly used for Docker.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FiowMgG2U5d2RRDhqHAOO%2Flevel-2.png?alt=media&#x26;token=d784ae02-f87c-4f16-be40-26d82990e5bd" alt="" width="328"><figcaption><p>Level 2 - App diagram breakdown</p></figcaption></figure>

**High-level responsibilities of a system**—These diagrams show how the separately deployable components interact to make a system work.

**Scope** - Apps and stores (inside the system you're zoomed into), other systems (internal and external) and actors.

**Intended audience** - Architects, Developers, Product, and Operations.

***

### 3️⃣ Level 3 - Component diagrams

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fu3OfQ5COGOV3YoKjXxYN%2Flevel-3.png?alt=media&#x26;token=cb352089-87e9-4537-9a34-e627b1005ee5" alt="" width="328"><figcaption><p>Level 3 - Component diagram breakdown</p></figcaption></figure>

**The building blocks and interactions of an app**—Zoom in on each app to show the components that make each app work and the interactions within. These are more technical diagrams for a technical audience.

**Scope** - Components (inside the app you're zoomed into), other apps and stores in the same system, other systems (internal and external) and actors.

**Intended audience** - Architects, Developers and Operations.

***

### 4️⃣ Level 4 - Code diagrams

These show how an app or store works and functions inside—currently, you can't diagram the fourth level in IcePanel. We believe you should refrain from diagramming this manually and [link your model objects](https://docs.icepanel.io/integrations/linking-to-reality) to the code itself (reality).

This level is rarely diagrammed in practice. As Simon says, "...most IDEs can generate this level of detail on demand."

## Using the C4 model in IcePanel

IcePanel is a visual C4 modelling, diagramming, and documentation tool that maintains the C4 hierarchical structure.

### IcePanel's model object structure

* Organization
  * Landscape
    * Domain
      * Actor
      * Group
      * System
        * App or store
          * Component

### Model object details

When you select a model object (Actor, Group, System, App, Store or Component), you can view and edit the details in the right-hand panel. These details include:

* Icon (linked to technology choices)
* Name of object
* Connections
* History
* Team edit access `(Growth plan only)`
* Internal or external object type
* Abstraction (Actor, System, Group, App, Store, Component)
* Status (Live, future, deprecated or removed)
* [Domain](https://docs.icepanel.io/core-features/domains) `(Growth plan only)`
* [Ownership team](https://docs.icepanel.io/ownership-teams) `(Growth plan only)`
* Diagrams list
* [Flows](https://docs.icepanel.io/visual-storytelling/flows) list
* [Tags](https://docs.icepanel.io/visual-storytelling/perspective-tags)
* Display description
* Technology choices
* Reality or generic links (see [Linking to reality](https://docs.icepanel.io/integrations/linking-to-reality))
* Detailed description

{% hint style="warning" %}
Each model object must have a unique name within its scope. Violating this rule raises an “already exists” error.

In practice, this means that a model object cannot share a name with another object that:

* Share the same parent, or
* Reside higher in the hierarchy within the same Domain.

Otherwise, sharing names is allowed. This lets you apply the same naming conventions across Systems, as long as no ambiguities arise. For example, each system can have a Store named “database” and an App named “front-end” without issue.
{% endhint %}

### Adding objects in the diagram view

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FEmlxFzxQwjut31wbyF0E%2Fadd-object.gif?alt=media&#x26;token=3b7b45f9-ec16-403e-bfcd-b103396d6ac4" alt=""><figcaption><p>Adding objects in IcePanel via the diagram view</p></figcaption></figure>

You can add, edit or remove objects from your model in a diagram.

**To add new objects in a diagram:**

1. Click the `+` button on the left toolbar.
2. Drag and drop the object button in the canvas (you can also click and drop).
3. Name the object and add a displayed description.
4. Drag a new connection from an existing object to a blank space in the canvas to create a new object.

Adding objects this way adds them to your model for reuse. This is the best and quickest way to build up your model while keeping it in the context of the diagram you're creating.

{% hint style="warning" %}
Make sure to name your objects in a way anyone can understand.
{% endhint %}

### **Editing model objects**

In IcePanel, changing an object will update it everywhere it exists. This includes all diagrams, flows, and the model. Make a change anywhere, and it will auto-sync everywhere.

### **Removing model objects from a diagram**&#x20;

You can remove model objects from just a diagram but keep them in the model for later or another diagram. To do this:

* Select the object in the diagram.
* Press the `Backspace` or `Del` key.
* OR click the 3 dot `...` menu and select `Remove from the diagram.`

### **Deleting objects from the model**

{% hint style="danger" %}
This action cannot be undone.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F16pz1lRVYvnFYtDNK7tP%2Fdelete-object.gif?alt=media&#x26;token=85dc7b85-3155-4aae-b6a2-449e660c841f" alt=""><figcaption><p>Deleting model objects in IcePanel</p></figcaption></figure>

1. Select the object or objects you wish to delete.
2. Click the 3 dot menu at the top right.
3. Click `Delete object` .
4. You will see a list of all things that will be permanently deleted.

This will delete the object from the model, all diagrams it was in, all connections in and out, diagrams that the object owns, and any details about it.
