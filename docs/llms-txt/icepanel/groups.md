# Source: https://docs.icepanel.io/core-features/modelling/groups.md

# Groups

{% hint style="info" %}
Groups used to be called "Areas" and are available on all plans.
{% endhint %}

## What are groups?

Groups are used to overlay additional information around model objects in a diagram. You can assign any model object, except another group, to 1 or many groups. This information is stored in the model.

Groups auto-size around objects assigned to them and resize around other groups to ensure easily readable diagrams with less overlap. You cannot manually edit the size of a group when you have assigned model objects to it.

A group with no child objects can be used as a flexible visual overlay or bounding box without storing the objects inside.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FzW4qrhpyFtgdQQ4cKwgl%2FGroups%20showcase.gif?alt=media&#x26;token=e99bdb21-b64d-43b9-9478-8197a0d24de2" alt=""><figcaption><p>Groups can be used to show a collection/group of model objects</p></figcaption></figure>

## Use cases for Groups

Groups can be used in many ways to show a collection of objects as additional information.&#x20;

Some examples of when to use groups:

* **Deployment group** - showing how objects are deployed together
* **Microservice** - for example, an API with a data store, making a Microservice
* **Environment information** - for showing what lives in Production vs Development
* **Domains** - show your domains as a physical bounding box
* **Technology choices** - such as cloud providers in a multi-cloud solution
* **Tags** - Show a bounding box for any tag group, team, status, etc.

## Creating a new group

To create a group in a diagram:

1. Hover over the  `+ Add` button in the left-hand toolbar
2. Click the `Group` option, and a new group will be added to the diagram
3. Name your new group

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F372TRiH9L8lkAmgCQBLF%2FCreating%20a%20group.gif?alt=media&#x26;token=4532d81e-6647-4779-ae57-91c43c132289" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Double-click anywhere in the diagram canvas to create existing or new objects.
{% endhint %}

## Deleting a group

1. In the diagram view or model view, select a group
2. Go to the 3 dot menu top right
3. Select `Delete object`
4. Confirm the deletion of this group by clicking `Delete from model`

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FCf26W2Om0CiuVLI4l0GI%2FDeleting%20a%20group.gif?alt=media&#x26;token=602f1e18-bae2-4a55-9943-f41ac85697bf" alt=""><figcaption></figcaption></figure>

## Assigning objects to groups

Objects can be assigned to 1 or many groups. A group can store any object type except other Groups.

### How to assign an object to a group:

1. Select the object you wish to add to a group
2. Click the Group dropdown in the right-hand panel
3. Click on the `+ Add to group` button
4. Search and select the group(s) you want to add these objects to

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FQqOmuMX6KYZRRVSARZbd%2FAssinging%20a%20group%20to%20an%20object.gif?alt=media&#x26;token=b6b14512-efee-4a7d-9514-7c22c4235564" alt=""><figcaption><p>Assinging objects to a group</p></figcaption></figure>

### Multi-select assigning groups to objects

You can multi-select and add multiple objects to groups at once.

1. Multi-select objects using `Shift` key + click objects
2. Select the Groups dropdown
3. Select the Groups you want to assign them to

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FaPqi6eQmhygisjVDAnCr%2FMulti%20selecting%20groups.gif?alt=media&#x26;token=29394092-d85b-4add-8448-6eec30b29d6a" alt=""><figcaption><p>Assinging multiple objects to a group</p></figcaption></figure>

{% hint style="info" %}
Adding an object to a group in the diagram will auto-resize it to fit the containing objects. If the group isn't in the diagram, you'll need to add it from the left-hand options or by double-clicking in the diagram.
{% endhint %}

### How to unassign objects from a group:

1. Select the object or objects you wish to remove from a group
2. Click the group dropdown in the right-hand panel
3. Deselect the group(s) you want to remove these objects from

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FxjFng0dY2OL3cmHWdXhD%2FUnassinging%20groups.gif?alt=media&#x26;token=e361f09b-e28d-4ae5-8565-89ae4dc15af3" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
When you unassign a group from the last object, they won't be removed from the diagram. You may need to clean up the diagrams they're in.
{% endhint %}

## Unassigned Groups

Groups without any model objects assigned are considered unassigned, meaning they're flexible bounding boxes that can be placed anywhere. These do not resize around objects and can be manually resized.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FDNzY2X5kKXUuiW3HUwc2%2FUnassigned%20group.gif?alt=media&#x26;token=bebdcdbc-d9f8-4a50-8e1d-d19b1207b5b3" alt=""><figcaption><p>Unassigned groups can be used as flexible overlays</p></figcaption></figure>

## Nested Groups

You can nest groups inside each other, which is especially helpful for visualizing hierarchical structures like a deployment diagram. For example, one group might represent a cloud region, with nested groups for individual services or components—this kind of hierarchy helps clarify how different parts of the system relate and are organized logically.

To nest a group inside another group, select the group you want to nest and hit the *In* drop-down. Find the group that you would like to use and confirm by selecting *Change Parent*.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FWojUIqZcYRCVAZbLVUPn%2FClipboard-20251119-000939-632.gif?alt=media&#x26;token=36a57cef-7091-4e12-b9d5-127708fd6a2f" alt=""><figcaption><p>Nest a group inside another group</p></figcaption></figure>
