# Source: https://docs.icepanel.io/future-state-design/drafts.md

# Drafts

{% hint style="success" %}
Multiple drafts are only available on the Growth plan. Archiving drafts is a Scale Plan feature only.
{% endhint %}

Architecture design doesn’t end once you’ve modelled the current state — it’s a continuous, collaborative process. Ideas are proposed, reviewed, and approved, and decisions need to be tracked for context and learning.

**Drafts** let you explore future changes to your architecture without impacting the live model. Drafts exist in isolation, so edits don’t affect anything outside until merged. With drafts, you can group multiple diagrams and model updates into a single update for cohesive change management.

## <sup>A quick run-through of how drafts work:</sup> <a href="#a-quick-run-through-of-how-drafts-work" id="a-quick-run-through-of-how-drafts-work"></a>

[<sup>Watch the walk-through directly on Youtube.</sup>](https://www.youtube.com/watch?v=O9s_JMWqlG4)

{% embed url="<https://www.youtube.com/watch?v=O9s_JMWqlG4>" %}

## Future state architecture <a href="#future-state-architecture" id="future-state-architecture"></a>

In software development, documenting and diagramming your current architecture helps teams understand how things work today. But progress requires proposing and discussing future changes.

Communicating the **future state** of your system(s) provides a shared vision of where the team is headed and how technical decisions align with business goals. Even as designs evolve, this clarity helps everyone understand the technical journey toward achieving those goals.

## How to create Drafts

There are 2 ways to create a new Draft:&#x20;

1. Inside a diagram, select the *Draft* button and hit 'New Draft'.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fm8IkXXuWAkE5JyoZKyj4%2FClipboard-20251030-230339-102.gif?alt=media&#x26;token=5901d81d-9cf8-46f7-92c6-d9686db0eacd" alt=""><figcaption><p>How to create a new draft</p></figcaption></figure>

2. From the Draft table, select the *New Draft* button, name it and select the Diagram you want to modify.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FDjRzWBaNHOpk3RRIaOe8%2FClipboard-20251030-230707-294.gif?alt=media&#x26;token=840b3322-b096-4bcb-b291-d275d81861c4" alt=""><figcaption><p>How to create a new draft</p></figcaption></figure>

## Modifying a diagram with Drafts

Once you have created your draft, you can start making changes to the diagram, the model objects, tags or flows. Modify anything you'd like. Edits on model objects, connections, and diagrams (including layout edits) are treated as draft changes. Changes in a draft will default to `future` state.

Changes are added to the Diagram and Model summary at the top. Any changes should be visible in the top menu.

{% hint style="success" %}
Drafts also work with Flows and Tags, meaning you can show the effects on user flows based on the changes you're making; you can propose new flows and highlight technology, risk, cost etc.&#x20;
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FIbjyeZxpUdJ4PDVKXNTd%2FClipboard-20251103-212128-775.gif?alt=media&#x26;token=52bfd0a3-8370-4809-ba2c-b60c6acab842" alt=""><figcaption><p>Modiyfing a diagram in drafts</p></figcaption></figure>

{% hint style="danger" %}
You are currently not able to change the **Type** of an object or the **Parent** inside a draft.
{% endhint %}

## Model-based (multi-diagrams) drafts

Within the same draft, you can modify as many diagrams as you'd like.&#x20;

From the Diagram view, select the Diagram button and click 'View all diagrams'. This will let you navigate to another diagram to make changes.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F3LY2cLgk7wOuZV5IWrUn%2FClipboard-20251031-212153-113.gif?alt=media&#x26;token=381ac8be-0bef-4426-adbd-d4d04d4faac6" alt=""><figcaption><p>Adding multiple diagrams to the same draft</p></figcaption></figure>

Edited diagrams are automatically added to the *Diagrams change* list at the top left of the navigation. See all model object changes in the draft under the new *Model* tab.

## Creating multiple drafts in the same diagram

You can create as many drafts as you'd like with the same diagram. This can help you compare proposals with each other and your current design. Keep in mind that these drafts don't interact with each other. There are separate forks from the current model.

## Drafts table

In the drafts table, you find a summary of all the drafts open and their statuses: `In-progress`, `Merged` and `Archived`.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F6JWgNefhil5Q2S0fKlaL%2Fimage.png?alt=media&#x26;token=1aacb1bc-d9d9-47b3-b696-a114690e76d2" alt=""><figcaption></figcaption></figure>

From this table, you can:&#x20;

* View Drafts
* Create a new draft
* Archive or delete a draft

## Review Changes

Once you're happy with your changes, you can review them by selecting the *Changes* drop-down. If you're in the diagram, clicking on a change will bring up that object if it's present.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F77z4jwZI1rM1gxMDu1Zy%2FClipboard-20251031-215339-355.gif?alt=media&#x26;token=bf46d89f-a42b-487f-8c2b-0edc96a1d5bc" alt=""><figcaption><p>Review changes</p></figcaption></figure>

You can also view all the model changes in the *model* tab.&#x20;

## Merge changes

Merge your draft when you agree to the proposed changes. A modal will appear with a list of changes and who proposed them.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FtrhOVoQyV1sZGOGtZaJE%2FClipboard-20251103-214105-347.gif?alt=media&#x26;token=41b7adad-8aa3-46d5-8651-fd8d59393afe" alt=""><figcaption><p>Merges changes</p></figcaption></figure>

Merging a draft will automatically create a new version of your model.&#x20;

## Conflicts

You will not be able to merge your draft if there are any conflicts. In that case, you will see a red *Merge conflicts* button.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FXb8KV2UVqv4h9usBg1vb%2FClipboard-20251103-214444-791.gif?alt=media&#x26;token=d38db02c-2a53-4eaa-bebf-dd78f04f4dc5" alt=""><figcaption><p>Conflicts in drafts</p></figcaption></figure>

Fix the conflicts first and then merge again.

***

Happy drafting! 🧊
