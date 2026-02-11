# Source: https://docs.icepanel.io/core-features/landscape.md

# Landscapes

## What is a landscape?

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FEtkD98h8xzpYIHCE3APO%2Fpricing_landscape.png?alt=media&#x26;token=e43358ed-93aa-4821-ae4f-6bd8f2805ccf" alt=""><figcaption></figcaption></figure>

A landscape is the parent object for:

* The shared model (Domains, Objects and connections)
* Set of diagrams&#x20;
* Tags & flows

Consider a landscape to be the world you work in, referencing everything that interacts with each other in the real world - These should all be in 1 landscape.

## When to split a landscape

{% hint style="warning" %}
We recommend staying in 1 landscape as much as you can
{% endhint %}

The power of a landscape is the shared model, diagrams that can be drawn from the model and syncing updates across the whole landscape.

There are, however, a few reasons you may want to split out your landscapes. For example:

1. There is a clear separation of systems and they never/rarely interact
2. Regulatory reasons - keeping teams/people separate
3. Consultants - Separating customer-specific designs to share with them
4. Sandbox - Duplicating to "play" with the design or play with the features of IcePanel

Objects in separate landscapes are not linked in any way, so if you reference a system from another landscape, we recommend that you use the "External system" setting, so people know not to add the main details here. Updates will not be reflected if you edit these referenced objects.

## Large or complex systems?

If you are struggling to organize your model because of a large and complex architecture (e.g., hundreds of apps/stores, and many diagrams), we recommend using Domains to split out your systems into logical business areas.

These systems and child objects remain in a single model and can be shared and synced from other domains, but it reduces the amount you see on the diagrams and model view. This allows you to focus your conversations and sections of your model on business areas, logical system groupings, segregation of external and internal systems, etc., with the reusability of a model.

## Overview section

The overview section helps you access important diagrams and flows in your landscape or domain. It also contains insights on diagram activity and action items to keep your model up to date.

In the overview section, you can:

* View and manage pinned diagrams or flows
* See your recently viewed or edited diagrams or flows
* See most viewed or edited diagrams over time in the entire landscape or domain
* See action items in Health check (inaccurate comments, questions, unresolved comments, recommendations)

{% hint style="info" %}
Selecting a domain will filter the overview section to that specific domain.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FkvjQl7fq6WuEEykTKBrV%2FOverview-section.gif?alt=media&#x26;token=66cdffca-cec8-4cf4-9a1e-9971ea8d6be7" alt=""><figcaption></figcaption></figure>

### How to pin a diagram or flow

You can pin items from the overview or diagrams/flows sections (see [diagrams-section](https://docs.icepanel.io/core-features/diagramming/diagrams-section "mention") and [flows-section](https://docs.icepanel.io/visual-storytelling/flows/flows-section "mention")).

To pin something from the overview section:

1. Click on the `...` menu beside the diagram or flow
2. Click on `Pin` diagram or flow button

To remove a pin, click the pin icon on the top left of the item in the pinned section.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F3Zkmi29z2L8mtsXt3SbP%2FPin-diagram.gif?alt=media&#x26;token=9e5c5ed9-99bb-4939-9c1a-a10995d25329" alt=""><figcaption><p>Pinning items in the overview section</p></figcaption></figure>

## Duplicating a landscape

For the most part, we recommend using 1 landscape - as explained above.

If you need to copy, here's how you can duplicate an existing landscape:

### Duplicating a landscape in the same organization

If you want to copy your work in the same organization, follow these steps:

{% hint style="info" %}
You need to be an **admin** to duplicate a landscape.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FbokHOBMYqa0hWEgDQa5v%2FScreenshot%202024-10-02%20at%203.23.56%E2%80%AFPM.png?alt=media&#x26;token=e2b6bd59-971b-481e-a55e-7ccb90730b53" alt=""><figcaption><p>Duplicating a landscape in the same organization</p></figcaption></figure>

1. Navigate to the overview screen.
2. Click the dropdown at the top left of the screen.
3. Select the `...` menu next to the landscape you want to duplicate.
4. Select **Duplicate landscape.**
5. You'll auto-navigate to the duplicated landscape.
6. Your duplicate landscape name will have the word "Duplicate" at the end.

### Duplicating a landscape to another organization

{% hint style="info" %}
You need to be an admin user in **both** organizations to do this. You also need a paid plan in the organization you're migrating to.&#x20;
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F103kIb6cjxlogdow3zpk%2Fimage.png?alt=media&#x26;token=af567b7b-77dc-469a-a74e-16045bc1d864" alt=""><figcaption><p>Duplicating landscape to another organization</p></figcaption></figure>

If you want to move your work to someone else's organization, follow these steps:

1. Be invited to the other organization to which you want to copy your work.
2. Ensure you are an admin user in both organizations.
3. From the home screen, click the dropdown at the top left.
4. Select **Switch Landscape**.
5. Select the `...` menu next to the landscape you want to duplicate.
6. Select **Duplicate to another organization.**
7. Select the other organization and click **Duplicate.**
8. You'll auto-navigate to the duplicate landscape in the other organization.
9. Your duplicated landscape name will have the word "Duplicate" at the end.

## Copying to another landscape in the same organization

{% hint style="info" %}
You need to be an **admin** user to copy to another landscape.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F8T22veLyDrCGCi3dTvEx%2Fimage.png?alt=media&#x26;token=e9ed448e-7c4a-446d-9e25-6f0001a62ac6" alt=""><figcaption><p>Copying model/diagrams to between landscapes</p></figcaption></figure>

If you want to move your work to another landscape in the same org, follow these steps:

1. From the home screen, click the dropdown at the top left.
2. Select **Switch Landscape**.
3. Select the `...` menu next to the landscape you want to duplicate.
4. Select **Copy model/diagram between landscapes.**
5. Select the landscape you wish to merge with.
6. Click **Copy.**

This adds the landscape as a new Domain. You can then move the object(s) from this new domain to where they make sense in your merged landscape.

### Merging landscapes across organizations

1. Follow these steps: [Duplicate the landscape to another organization](#moving-or-duplication-a-landscape-to-another-organization).
2. Then, follow these steps to [Copy to another landscape in the same organization](#copying-to-another-landscape-in-the-same-organization).

### Copying object(s) to another landscape

Currently, we don't support single-object copying between landscapes, only landscape based copying. However, if you want to move a system to another landscape, including the objects inside, you can use this workaround.

1. Follow these steps: [Duplicating a landscape in the same organization](#duplicating-a-landscape-in-the-same-organization)
2. Navigate to the Model objects list.
3. Select all objects (`CMD` + `A` or `CTRL` + `A`).
4. **De-select** the objects you want to move.
5. Use the `...` menu to delete the remaining selected objects.
6. Confirm the deletion (If it's a large model, this might take time).
7. If you see some objects that should have been removed, try refreshing the browser and see if they're still there.
8. Then, follow these steps to [Copy to another landscape in the same organization](#copying-to-another-landscape-in-the-same-organization).

### Switching between landscapes

If you're part of multiple landscapes, you can switch between them by selecting the drop-down menu in the top left.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FgvI0cgD6arIlrwfeZCVm%2Fimage.png?alt=media&#x26;token=393b529c-4fc3-4708-89e4-9c3c73bd89b7" alt=""><figcaption><p>Switch between landscapes</p></figcaption></figure>
