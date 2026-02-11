# Source: https://docs.icepanel.io/visual-storytelling/flows.md

# Flows

## What are Flows?

Your systems architecture doesn't live in a static world, without interactions and data flows, so neither should your diagrams have to. With IcePanel Flows, you can show and explain the sequence of messages that run through your systems by each use case and focus on the objects and connections used. Flows can be adapted to show a range of interactions, from business use cases (how does our e-commerce system support a purchase?) to technical processes in your system (how do we authenticate users?).

This step-by-step approach will show you how to create and present different flows over the same diagrams seamlessly.

## Flow step types

There are 8 step types:

### 🟢 Introduction

The <mark style="color:green;">`Introduction`</mark> step shows all steps in the current flow before showing each step at a time.

You can add details to explain what the flow is about as a way to set the scene before moving into each individual step.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F7JvIK0Lzl9tbpmqT2S9i%2Fimage.png?alt=media&#x26;token=1b025f49-dedf-4a75-b429-353901391519" alt=""><figcaption></figcaption></figure>

### ➡️ Message

The `Message` step shows a message between 2 objects using an existing connection in the diagram.

{% hint style="info" %}
Connection direction doesn't matter for flow steps. You can show responses by flipping the direction of the connection just for the step.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F5HFHSDo2Lm54qY25wVoU%2Fimage.png?alt=media&#x26;token=e967d32e-f2f4-41b5-b1d6-db9477151341" alt=""><figcaption></figcaption></figure>

### 🔄 Process

The <mark style="color:blue;">`Process`</mark> steps show when a single model object does something.

Use the Process flow step for:

* Technical process you don't need the details for such as when an external object processes something for you and just returns the result such as "Process fraud check"
* Business processes such as "Ensure the new user is successfully onboarded"
* Actor actions that happen outside of your solution, such as "Send physical mail" or "Contact Brian from accounting".

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F9OkAaqIV47T4lCPurHvm%2Fimage.png?alt=media&#x26;token=e82a81e9-0339-4f0a-b937-a12b57eb5c8a" alt=""><figcaption></figcaption></figure>

### ◆ Alternate paths

The <mark style="color:yellow;">`Alternate paths`</mark> step allows you to split a flow and show different paths depending on a decision. This is to show `OR` decisions, when A or B or C ... are true compared to the others.

This is useful to show True / False decisions&#x20;

It's also useful to show multiple options, such as:

* Authentication methods
* Payment methods
* Web app vs Android app vs Apple app
* etc.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fh1oVYL3RV4PT40wBMwvE%2Fimage.png?alt=media&#x26;token=57ddbbc3-34b4-40ec-8b9d-02c976bfbde7" alt=""><figcaption></figcaption></figure>

### 🛣️ Parallel paths

The <mark style="color:yellow;">`Parallel paths`</mark> step allows you to show multiple steps happening in parallel or synchronously. This is to show `AND` decisions, when A and B and C ... are true alongside the others.

This is useful to show:

* Events/message broker with Producers with many consumers.
* Sending notifications to multiple systems
* Any asynchronous process

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FLeIgf5DhOabTrYi3apTa%2Fimage.png?alt=media&#x26;token=fb54fdd2-e390-4d1f-ba37-d5373a89269e" alt=""><figcaption></figcaption></figure>

### ↱ Go to another flow

The <mark style="color:blue;">`Go to another flow`</mark> step allows you to link multiple flows together. Use this to send people to another flow in the same or another diagram.

This is helpful to have high-level flows that have more detail lower down to tell a full story across multiple C4 model levels.

When you go to another flow, you get the option to return back to that step during or at the end of the other flow.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FdaMlnBW8dz7LaQJMBDhb%2Fimage.png?alt=media&#x26;token=8436635b-86f2-4e14-83c9-8b1e9108a063" alt=""><figcaption></figcaption></figure>

### ℹ️ Information

The <mark style="color:purple;">`Information`</mark> steps allow you to show important information that is not tied to any object or connection. Use this to add details to a flow that don't tie into anything in the diagram.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FTXetjRiwgg67W2SgX28u%2Fimage.png?alt=media&#x26;token=d234d949-dc30-49e2-8196-ced1755c3d59" alt=""><figcaption></figcaption></figure>

### 🏁 Conclusion

The <mark style="color:red;">`Conclusion`</mark> step is to show the flow has ended and shows all steps in the flow. It allows you to add some closing context to the end of the flow.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FkJ5mW0UaBLKDl9mC0Jr3%2Fimage.png?alt=media&#x26;token=80e1e93a-1022-4123-b634-05617ca07893" alt=""><figcaption></figcaption></figure>

## Creating a Flow

{% hint style="info" %}
You can create up to 3 Flows on the Free plan, and unlimited on Growth and Isolation plans.
{% endhint %}

To create a new flow in a diagram:

1. Click on flow dropdown at the top left of the screen
2. Click `New flow`&#x20;
3. Edit the flow name by clicking on the pencil icon in the list view

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fqz6cxPE4weyJcoHNaTas%2FCreating%20a%20flow.gif?alt=media&#x26;token=05fe2e45-d8e0-463a-9f7a-2123df5c3b61" alt=""><figcaption><p>Creating a flow</p></figcaption></figure>

## Adding steps to a Flow

To add steps to a flow:

1. Make sure you're in edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Click the `+ Step` button in your flow
3. The default step is a Message type between 2 objects. Click the Message button to change this.
4. Select the object you want to start the step from
5. Select the object that’s connected to your first selected object (the list will only show connected objects to the one you selected in step 2)
6. If there is only 1 connection between those objects, it will be auto selected. If you more than 1, select the connection you want to use for that step (the list will only show connections between those 2 objects in the current diagram)
7. Add a title to describe what happens in that step. Your title will be added with the step number to the current diagram, highlighting when that step is in focus. *(optional)*
8. Optional - You can also add more details for this step too - good for longer pieces of text of technical details.

{% hint style="info" %}
**Tip**: We recommend labels on connections to convey high-level technical choices (at level 2 & 3) or business relationships (at level 1). Then use Flows to identify how that technical connection is used in realistic scenarios between your users, objects and external Systems or Apps.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FOWZ96uhTG28A6u4Mx7O5%2FAdding%20a%20step.gif?alt=media&#x26;token=718c1185-1c98-4cb2-808b-4b4a3990c38a" alt=""><figcaption><p>Adding a step to a flow</p></figcaption></figure>

### Intelligent flow selection

Select an object or connection before adding a step to automatically fill the details of a step.&#x20;

To do this:

1. Make sure you're in edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Select a connection for a `Message` step type will be added with the objects, connection and title auto-filled. &#x20;
3. Select the sender object and `SHIFT` select the receiever object for a `Message` step type will be added with the objects, connection and title auto-filled. This works in either direction of a conection.
4. Select an object for a <mark style="color:blue;">`Process`</mark> step type will be added with the objects, connection and title auto-filled.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F83aYtijihoue9frYJbWV%2FIntelliegnt%20adding%20a%20step.gif?alt=media&#x26;token=470b8de6-2c73-4fbe-84f3-903d9507902f" alt=""><figcaption><p>Selecting an object and adding a step</p></figcaption></figure>

## Reordering steps

You can reorder by dragging the grip icon by the number of the step card.

1. Make sure you're in the edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Click and drag the grip handle to the left of a step card to the desired location.
3. A blue line will appear where the step will be placed when you let go.

To place in a path, drop on the path itself. The path will turn grey, indicating you're hovering on the right place.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FgCKAqwL3m2eP9ddRloi6%2FReordering%20steps.gif?alt=media&#x26;token=5dd54c82-9fc4-48bd-b266-6ba2179987ad" alt=""><figcaption><p>2 ways to reorder steps in a flow</p></figcaption></figure>

## Duplicating a step

To duplicate a step:

1. Make sure you're in the edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Hover on the step you want to duplicate
3. Click the `…` menu item on the top right of the step
4. Click `Duplicate step`

## Deleting steps

To delete a step:

1. Make sure you're in the edit mode (The play button will be visible)
2. Hover on the step you want to delete
3. Click the `…` menu item on the top right of the step
4. Click `Delete step`

## Adding paths to a Flow

{% hint style="info" %}
Paths are only available on Growth and Isolation plans.
{% endhint %}

Paths allow you to communicate more complex logical steps in your flow. There are 3 types of paths in IcePanel — **Alternate** **paths,** **Parallel paths,** and **Go to another flow**.

### Alternate paths

Alternate paths show steps based on a choice or scenario. For example, you may want to show different paths for a success or failure scenario. Think of these as *OR* scenarios.

To add an *Alternate path*:

1. Make sure you're in the edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Click the `+ Step` button
3. Change the step type to `Alternate path`
4. Add a first step by clicking on the `+ Step in path` button nested in the path
5. To add more steps to the path, select a step before and click on the `+ Step in path` button under that step.
6. You can edit the path name by first clicking on the dropdown menu at the top of the path, then on the pencil icon of the path

To add another path in the alternate path:

1. Click on the dropdown menu at the top of the path
2. Click on the `Add path` button

The group of paths also has a title, which you can use to explain the decision being made and use each path names to explain the choices.

{% hint style="info" %}
Changing an existing step to a path will add that step to the first path.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fh4eDJfy18DaVXj31Pf1z%2FAlternate%20paths.gif?alt=media&#x26;token=47b921d6-fc50-4e1f-8e6c-b0b1626e5b9d" alt=""><figcaption><p>Creating an alternate path</p></figcaption></figure>

### Parallel paths

Parallel paths are useful for showing asynchronous steps, for example, a messaging queue or any scenario with parallelization. Think of these as *AND* scenarios.

To create a *Parallel path*:

1. Make sure you're in the edit mode (The play button will be visible, `CMD/CTRL` + `E`)
2. Click the `+ Step` button
3. Change the step type to `Parallel path`
4. Add a first step by clicking on the `+ Step in path` button nested in the path
5. To add more steps to the path, select a step before and click on the `+ Step in path` button under that step.
6. You can edit the path name by first clicking on the dropdown menu at the top of the path, then on the pencil icon of the path.

To add another path in the parallel path:

1. Click on the dropdown menu at the top of the path
2. Click on the `Add path` button

The group of paths also has a title, which you can use to explain the decision being made and use each path names to explain the choices.

{% hint style="info" %}
Changing an existing step to a path will add that step to the first path.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FmPacMbMRSGtWfAzTyANL%2FParallel%20paths.gif?alt=media&#x26;token=3fba07f2-08fd-4b54-9353-42382f9440ac" alt=""><figcaption><p>Creating a parallel path</p></figcaption></figure>

### Go to flow

Once you have many flows across different diagrams in your domain, you can connect them to communicate even richer stories.

To add a *Go to another flow* step:

1. Click the `+ Step` button under the active step&#x20;
2. Change step type to  `Go to another flow`
3. Click on the `Select flow` dropdown
4. Select the flow you want to link

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fwlj6veIOYQWQhFZrBPqa%2FGo%20to%20flows.gif?alt=media&#x26;token=a4d9b696-6552-4a37-8336-accfd83e09c3" alt=""><figcaption><p>Creating a Go to flow step</p></figcaption></figure>

## Duplicating a path

1. Click on the paths dropdown&#x20;
2. Click on the `…` menu item on the right of the path you want to duplicate
3. Click on the `Duplicate path` button

## Deleting paths

To delete a single path:

1. Click on the paths dropdown&#x20;
2. Click on the `…` menu item on the right of the path you want to duplicate

To delete all paths:

1. Click on the `…` menu at the top of the paths
2. Click the `Delete` button

## Presenting flows

Presenting flows is a powerful way to focus attention on the topic you want to discuss in your System design. IcePanel allows you to navigate chronologically or non-linearly across your flow, depending on what you want to communicate.

There are a few ways to go through a flow:

* Press play to present the flow (we recommend hiding details until they're needed)
* Use the `Back` and `Next` buttons at the top of the Flow editor
* Use the ⬅️ or ⬆️ (back) and ➡️ or ⬇️ (next) arrow keys on the keyboard
* Click each step in the Flow steps dropdown
* Click the step on a connection directly in the diagram

{% hint style="info" %}
**Tip:** Combining Flows with Tags on IcePanel is a useful way to layer on relevant attributes for a particular use case. For example, if you want to go through a flow while also highlighting specific levels of risk or cost across different objects, you can use IcePanel’s *pin tag* feature. Play around with different tags to facilitate different conversations with stakeholders.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FcdwEnlkeSrWqNqp3tn4z%2Fpinned%20tags%20with%20flows.gif?alt=media&#x26;token=8a2cde75-d4a7-47ce-a4c1-1a788ff97ba6" alt=""><figcaption><p>Presenting a flow with pinned tags</p></figcaption></figure>

### Flows with paths

Here are a few things to keep in mind when you present flows with paths:

* For Alternate Paths, the flow will highlight the *first path created* by default in the diagram. Use the **⇥** button on the right of the path area to navigate through the different paths
* For Parallel Paths, *the first step* of each path will be highlighted by default. For example, if you have 3 different paths in a parallel path, the first step of each will be highlighted when you navigate to the path. Afterwards, the flow will navigate through the first path created by default
* For Go to flow paths, the `Next` button will change to `Go to flow` and navigate to that flow by default. You can skip this by clicking the `Skip flow` button at the bottom of the step.

You can rearrange path orders by clicking on the dropdown menu in the path and using the draggable area on the left of each path.

### Visual options

Flows also come with a few additional visual customizations when presenting:

1. First, click on the `…` menu item on the right of the Flow editor
2. To show all connection names in the diagram, click the checkbox next to that option (this is turned off by default)
3. To show all steps in the flow, click the checkmark next to that option (by default, flows will only show the descriptions of the previous and next steps). If this is turned on, step titles for each step will appear in your diagram

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FPYMHSddclQafTahmTpbP%2Fflow%20visual%20settings.gif?alt=media&#x26;token=e99dbf39-d907-4820-be78-bc42415ba8d3" alt=""><figcaption><p>Adjusting visual settings for Flows</p></figcaption></figure>

## Duplicate a Flow

To duplicate a flow:

1. Open the flow you want to duplicate or the list of flows in the dropdown
2. Click on the `…` menu item on the right of the Flow editor
3. Click on the `Duplicate flow` button

## Deleting a Flow

To delete a flow:

1. Open the flow you want to delete or the list of flows in the dropdown
2. Click on the `…` menu item on the right of the Flow editor
3. Click on the `Delete flow` button
4. Click on the `Delete` button to confirm

## Exporting a Flow

IcePanel supports exports in a few formats if you plan on sharing images/PDFs of your diagrams or want to visualize them as sequence diagrams.

### Copy flow as text

This will copy your steps chronologically with object names, step types, step title, connection names, and paths. This can be useful to append to an image or PDF of your diagram.

To copy a flow as text:

1. Open the flow you want to copy or the list of flows
2. Click on the `…` menu item on the right of the flow editor
3. Click on the `Copy flow as Text` button

*Example output:*

```yaml
Introduction: Notes about this flow
- Step 1: User: This happens first
- Step 2: User -> API service: Thing happens via Request PNG or PDF export
- Step 3: API service -> Export topic: Then this happens via Publish export request
```

### Copy flow as code

To export your flow as code to create a sequence diagram:

1. Open the flow you want to copy or the list of flows
2. Click on the `…` menu item on the right of the Flow editor
3. Click on the `Copy flow as PlantUML` button
4. Paste the code in a UML tool like PlantUML or [WebSequenceDiagrams](https://www.websequencediagrams.com/)

{% hint style="info" %}
At this moment, IcePanel doesn’t support sequence diagram imports to flow
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FTQkS68JMZ9ETwy2wOndI%2Fcopy%20flow%20as%20code.gif?alt=media&#x26;token=0741d12e-1da4-4b67-984d-a07aa42daeb5" alt=""><figcaption><p>Exporting a flow to a sequence diagram</p></figcaption></figure>

### Copy flow as Mermaid

To export your flow as Mermaid to create a sequence diagram:

1. Open the flow you want to copy or the list of flows
2. Click on the `…` menu item on the right of the Flow editor
3. Click on the `Copy flow as Mermaid` button
4. Paste the code into Mermaid

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FosKAXvR6eQkT0AkixJ0z%2Fimage.png?alt=media&#x26;token=7aefb0ad-1d86-452f-a340-eb297366db9e" alt=""><figcaption><p>Copy flow as Mermaid</p></figcaption></figure>
