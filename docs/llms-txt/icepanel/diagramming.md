# Source: https://docs.icepanel.io/core-features/diagramming.md

# Diagramming

Diagrams are at the centre of IcePanel. Combined with the C4 model, you can effortlessly show how your systems fit together at different levels of detail. Go from a high-level overview of your system to the apps and components that make it work. Add tags and flows to communicate different stories about your system. IcePanel's model-based philosophy enables you to create reusable objects across different diagrams, leading to greater consistency.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fo2ZBDJ5JDRUrgw01cM6v%2Fdiagramming-1.gif?alt=media&#x26;token=52b54803-f39a-4ff2-ba2f-835c443305f7" alt=""><figcaption><p>IcePanel diagrams are based on the C4 model</p></figcaption></figure>

## Diagram basics

### Creating a diagram

The diagram hierarchy in IcePanel is based on the [C4 model](https://docs.icepanel.io/core-features/modelling), with 3 levels of connected diagrams (instead of Level 4 diagrams, we allow you to [link objects to reality](https://docs.icepanel.io/integrations/linking-to-reality)). There are 2 ways to create diagrams.

#### On the landscape page

1. Go to the Diagrams section.
2. Click on the `Create diagram` button.
3. Select the diagram type and parent object.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FNNtZAYgRItmDiCeWHnB0%2FScreenshot%202025-02-20%20at%201.02.58%E2%80%AFPM.png?alt=media&#x26;token=1cd6aa5f-b8d4-463a-8caa-b926f88b0f7d" alt=""><figcaption><p>Creating a diagram from the diagrams section</p></figcaption></figure>

#### In a diagram

1. Navigate to the top left and click on the `Diagrams` dropdown
2. Click on the `New diagram` button

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FPLWwlJtA0MmRBFVRW1Th%2Fadd-diagram.png?alt=media&#x26;token=951bb8b8-e9c4-4d2d-b3b6-6bad1e4e7d2c" alt=""><figcaption><p>Creating a new diagram from the diagram dropdown</p></figcaption></figure>

{% hint style="info" %}
Diagram groups are only available on Growth and Isolation plans.
{% endhint %}

### The top-level navigation

The top-level navigation bar shows where you are in the C4 hierarchy, allows you to navigate across and up levels, and view diagram details.

Use this section to:

* See which diagram you're in and at which level.
* Go back to where you were previously.
* Navigate between different diagrams at a level.
* Navigate to a diagram at a higher level.
* View and edit diagram details (name, description).
* See who last edited the diagram.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FbxgY6LokUSfiqnxu5K20%2Fdiagramming-2.gif?alt=media&#x26;token=467dd463-87e5-41ab-ab27-c27cbcea1a12" alt=""><figcaption><p>Using the top-level navigation for wayfinding</p></figcaption></figure>

### Creating new objects

Adding an object to a diagram creates it in the model.  This means you can **reuse** the same objects across different diagrams or make a single edit (to its name, for example) to change it everywhere. There are 3 ways to add new objects to a diagram.

#### Creating from the left toolbar

1. Navigate to the left toolbar and hover on the `+` button. A list of object types will appear.
2. Select the object type you want to add and place it in the diagram.&#x20;

{% embed url="<https://studio.saltfish.ai/demo-share/demo_1770249741716_qwd47jgxu>" %}

#### Creating in the canvas

1. Double-click in the diagram area.
2. Click on the object type you want to add.
3. Name your object.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FrvVtqISu8C01BvQBjpYy%2Fadd-object.png?alt=media&#x26;token=ca338baf-a3ed-4c9b-bffb-eb96ef8e477e" alt="" width="375"><figcaption><p>Double-click in a canvas to add a new object</p></figcaption></figure>

#### **Using keyboard shortcuts**

* Create a new system: `Shift + S`
* Create a new actor: `Shift + P`
* Create a new Group: `Shift + G`
* Create a new app: `Shift + A`
* Create a new store: `Shift + D`
* Create a new component: `Shift + X`

See all [hotkeys](https://docs.icepanel.io/other-information/hotkeys "mention")

{% hint style="success" %}
You can duplicate any existing object by simply right clicking the object and selecting the *Duplicate Object* option. You can multi-select them to duplicate multiple at a time!&#x20;

Use shortcut `CMD/Ctrl + D` to duplicate quickly.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FBnqPuBm5yaNdxxdAY55O%2Fimage.png?alt=media&#x26;token=52802f7e-2ff0-4470-8d0f-47d67fe02066" alt=""><figcaption><p>Duplicating an object in the Canvas</p></figcaption></figure>

### Adding existing objects

There are 2 ways to add existing objects to a diagram.

#### Searching from the left toolbar

1. Navigate to the left toolbar and click on the  button `+` .
2. Search for objects by name.
3. Click on the object you want to add to the diagram or drag and drop.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FJnTs5DOQ3VqsfpaFJqtE%2FScreenshot%202025-02-20%20at%201.07.37%E2%80%AFPM.png?alt=media&#x26;token=a9926d28-8293-4ac6-a9a9-d0d390fedea3" alt="" width="375"><figcaption><p>Add objects from your model</p></figcaption></figure>

#### Searching in the canvas

1. Double-click in the diagram area.
2. Search for the object by name or select the object from the dropdown list.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FV5NazetKa6YqieVj5WVo%2Fadd-model-objects.png?alt=media&#x26;token=5841b2de-b474-4b41-89a8-eabca4af7efc" alt="" width="375"><figcaption><p>Double-click and add objects in your model</p></figcaption></figure>

### Searching for objects

You can search for objects in a diagram by clicking the `+` button and using the filters. You can filter to view only objects in the diagram or the parent object. If you click on an object in the list that exists in the diagram, the canvas will move and focus on it.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FCxDJll4ItHC6ztei4gzK%2FScreenshot%202025-02-20%20at%201.09.39%E2%80%AFPM.png?alt=media&#x26;token=bf55ae37-3843-46e2-8565-d80284276bf3" alt="" width="375"><figcaption><p>Finding objects in a diagram</p></figcaption></figure>

{% hint style="info" %}
Use CMD/CTRL + F to open the search menu with the in current diagram filter selected.
{% endhint %}

### Editing object details

Click on an object to view or edit properties on the right-hand menu, such as:

* Icon
* Object name
* Editable permissions (only available on Growth and Isolation plans)
* Object type
* Parent
* Status (Live, Future, Deprecated, Removed)
* Groups it belongs to
* Owners
* Diagrams the object is in
* Flows the object is in
* Tags
* Displayed description
* Technology
* Links
* Detailed description
* Connections to and from the object
* History of changes to the object

{% hint style="warning" %}
Any changes you make will affect the model and all diagrams the object is in.&#x20;
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FI9n3D7NbKWdYsBHkIkVx%2FScreenshot%202024-04-19%20at%204.01.42%E2%80%AFPM.png?alt=media&#x26;token=58ba7c42-fa66-422a-90a8-5d4570a51cce" alt="" width="305"><figcaption><p>Object details panel</p></figcaption></figure>

### Navigating across diagrams

There are a few ways to navigate across diagrams:

1. Clicking the 🔎 icon at the top-left of an object in a diagram. A numeric indicator will show how many objects are nested within the object. If there are no nested objects, a blank diagram will be created at a lower level when you click on it.
2. Selecting a diagram from the object dropdown at the top-level nav.
3. Selecting a diagram from the diagrams list from the right-hand objects details panel.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F1QJhh4iLvNFvYjFzofoG%2Fdiagramming-3.gif?alt=media&#x26;token=ea7692b3-3d51-4523-a004-a8c447e4ab9e" alt=""><figcaption><p>Navigating across diagrams in IcePanel</p></figcaption></figure>

### Custom zooming

By default, when you zoom into an object, you will land on the top diagram in the list of possible diagrams within that object. For example, zooming into a system will land on the first Level 2 App diagram within that system.&#x20;

You can select a custom landing point for your zoom action, based on the diagram you're in when you zoom. This helps to keep context when lower diagrams are focused on the same concepts higher up. This will only change the zoom behaviour of an object for the current diagram you're in.

For example,  you can set it up so that when someone is in `Context diagram 1`  when you zoom into `Core System` you will land on `App diagram 1` . Separately, you can set it up so when you're in `Context diagram 2` , and you zoom into `Core System` you will land on `App diagram 2` instead.

To set up custom zooming:

1. Go to the diagram you want to customize the zooming for.
2. Hover on the zoom icon of the object that owns the diagram you want to land on.
3. Click the `...` menu on the diagram you want to land on.
4. Click "Set as custom landing diagram."
5. Now, when you zoom into this object from that diagram, it will navigate to your custom set location.

To remove custom zooming and set back to default:

1. Go to the diagram that has the customized zooming.
2. Hover on the zoom icon of the object that owns the diagram that's set up.
3. Click the `...` menu on the diagram with "Custom" next to it.
4. Click "Remove custom landing diagram."
5. To confirm it worked, check by seeing "Default" next to the top diagram in the list
6. Now, when you zoom into this object from that diagram, it will navigate to your default (top of the list) diagram.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F4CmSAdDUgNsUCX2xy2v0%2FCustom%20zoom%20landing%20diagram.gif?alt=media&#x26;token=5e43442f-0e3d-4395-bd50-f154d7ac7ea6" alt=""><figcaption><p>Setting a custom zoom landing diagram.</p></figcaption></figure>

## Connections

### Adding connections

Connections are stored in the model as relationships. This means you can reuse those connections in other diagrams between the same object, keeping changes in sync and even allowing you to use connections from lower levels at higher levels as *"implied"* connections.

To connect model objects:

1. Use the + circular buttons on the edge of each object to drag a connection to another object.
2. If an existing connection exists in the model, it'll appear in a dropdown over the connection.
3. Name the connection and press `Enter` or the `+ New connection` button.

{% hint style="info" %}
Blank connections are not added to your model until you give it a name.
{% endhint %}

Each object has 12 unique connection points, except for actors, which have 6. For legibility, we recommend sending and receiving connections from unique points instead of overlapping.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fl4gKQq9kcIvtrKf38AGf%2Fconnection-points.png?alt=media&#x26;token=7e8f24b2-5e24-46af-bf73-19c70d136d77" alt="" width="343"><figcaption><p>App object with connection points</p></figcaption></figure>

### Editing connections

Click on a connection to view/edit things such as:

* Name
* Team edit permissions (only available on Growth and Isolation plans)
* Sender
* Receiver
* Status (Live, Future, Deprecated, Removed)
* Direction -  Outgoing *(default),* No direction, and Bidirectional
* Line shape - Curved line *(default)*, Straight line and Square edge line
* Label position
* Diagrams list
* Flows list
* Tags
* Technology
* Links
* Detailed description

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FoKONh6k1bPH4AVQFIija%2FScreenshot%202024-04-19%20at%204.02.52%E2%80%AFPM.png?alt=media&#x26;token=cba60514-bad0-4f75-a7d1-c9df5adf6271" alt="" width="304"><figcaption><p>Connections panel</p></figcaption></figure>

{% hint style="info" %}
You can also multi-select connections to edit their status, line shape, tags, and technologies.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FP03slRVUx0Kcwxr44HuE%2Fconnections-1.gif?alt=media&#x26;token=96b7b4fb-1bfc-4a75-8fc8-f1268543ad14" alt=""><figcaption><p>Mult-seclect objects to batch edit</p></figcaption></figure>

### Viewing dependencies and connections of an object

To view an object's dependencies and connections:

1. Click on an object and navigate to the `Connections` tab in the object details panel.
2. You'll see a list of incoming and outgoing connections, along with a breakdown of direct and lower connections. Use the filters to toggle viewing direct, lower, incoming, and outgoing connections in the list.
3. To view dependencies, Click on the `View dependencies` at the top to see the incoming and outgoing dependencies of the object.&#x20;
   * More details can be found here - [dependencies-view](https://docs.icepanel.io/core-features/dependencies-view "mention")

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F8nQcAvnwANKKoW9qPQCP%2Fconnections-2.gif?alt=media&#x26;token=b51bc03c-bdc2-4cb6-aa51-84f349eb3f09" alt=""><figcaption><p>Using the connections tab and viewing dependencies</p></figcaption></figure>

### Using lower connections

Existing connections from lower levels in the C4 model can be reused at higher levels. These are called *lower connections* and will sync changes in the original connection. These connections will show if a relationship has been created between objects inside (child objects) of those 2 objects previously.

When the original connection is updated, the lower connections will also update, including the sender and receiver of the connection in all diagrams in which it is located and the flows that the connected objects are in.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FmYltibNcKJsMM2vIuQGs%2Fconnections-3.gif?alt=media&#x26;token=b2ab3b68-dbcf-416f-8e9e-cad0e397e930" alt=""><figcaption><p>Adding a lower connection at Level 1</p></figcaption></figure>

### Showing relationships from another scope

Using the expand option, you can show apps inside a system talking directly to an app inside another system.

To do this:

1. Go to a Level 2 (app) or 3 (component) diagram.
2. Add an external system or app,
3. Select the `Expand`option in the object details menu.
4. Create new objects and change the parent to the external object.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FAHWeNxfqughQPVXX8zif%2Fexpand-system.gif?alt=media&#x26;token=a1775550-68e7-4393-a83f-c91b235d40c9" alt=""><figcaption><p>Expand systems to connect objects across multipel systems</p></figcaption></figure>

### Change connection to another object

To change the connection in the model to another object, click and drag the start or end of the connection to another object.

You'll see a modal to select either "New connection" or "Change connection in model":

* **New connection:** This creates a duplicate new connection for that change with the same name (it does not copy over documentation).
* **Change connection in model:** This will change the connection in the model and sync with the diagrams in which the old and new connections belong.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FNHDBFSGSmlpIEZFqbirb%2FScreenshot%202024-02-15%20at%204.11.14%E2%80%AFPM.png?alt=media&#x26;token=8b21310a-0021-41a5-984b-e741c8433489" alt=""><figcaption><p>Changing a connection to another object</p></figcaption></figure>

### Connection Via Property

You can attach a **Via Property** to any connection by clicking the *Via* field and selecting the relevant object. Once selected, the object will appear directly on the connection. This is particularly useful for event-driven flows using topics and queues (e.g. Kafka, RabbitMQ).

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FJkIseHEMHZVz2EnzBDR1%2Fimage.png?alt=media&#x26;token=bafdbf3a-2213-4e24-9e3f-d00f82ef521c" alt=""><figcaption><p>Adding a 'Via Property' to a Connection</p></figcaption></figure>

{% hint style="info" %}
The dependencies view also reflects the connections added *Via Property*. This way, you get an easy understanding of any of your queues.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FohonBatxOxvoeVFvzcCZ%2Fimage.png?alt=media&#x26;token=331fb0c3-6889-43bd-be1c-e1285fdba1ea" alt=""><figcaption><p>Dependencies view with Via Property Connections</p></figcaption></figure>

### Connections table

The Connections table show all the connections you have created. You are able to filter based on any of the filters available.&#x20;

{% hint style="success" %}
The *Via Property* filter allows you to show the connections that have a *Via Property*.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FRGjbXrFp09705GY13qPn%2Fimage.png?alt=media&#x26;token=3dce079c-a59f-433a-8b9d-c02999e71f68" alt=""><figcaption><p>Filtering Connections with the Via Property filer</p></figcaption></figure>

### Diagram vs model changes

You can think of diagrams as a visual representation of a model. You can visualize the same model through different diagrams depending on what you want to communicate. When you update or delete your model objects, the changes will be made globally, wherever that object exists. This saves you time from manually going to each object and updating it.

{% hint style="danger" %}
Using the delete key in a diagram does not remove objects from your model. To permanently remove objects from your model, delete them from the object details menu or the Model objects tab (on the landscape page).
{% endhint %}

## Diagram best practices

Here are some tips when creating diagrams:

* Name all of your diagrams.
* Name all of your objects (including connections).
* Add icons to every object.
* Add *display descriptions* to each object.
* Create separate diagrams at the same level to reduce complexity.
* Use the right level of complexity at each level (Level 1 should have fewer objects than Level 2).
* Use the same connection type in a diagram (avoid mixing curves and straight lines).
* Only use bidirectional connections for open connections like websockets. Otherwise, show the request connection and use Flows to show the response.
* For legibility, avoid overlapping connections in a diagram.

***

## Continue your IcePanel journey 🚀

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Tags</strong></td><td>Organize your objects</td><td></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fr8sKbRP6ZXIeUE0tpnJb%2FTags.png?alt=media&#x26;token=1e1a9b4b-4121-4430-a28c-2cc9e313d118">Tags.png</a></td><td><a href="../visual-storytelling/perspective-tags">perspective-tags</a></td></tr><tr><td><strong>Flows</strong></td><td>Show different use cases</td><td></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FpFKifwmbJc2Vx3uM4FMy%2FFlows.png?alt=media&#x26;token=0ccd6157-d452-4491-88c6-9aea0f93fe7b">Flows.png</a></td><td></td></tr><tr><td><strong>Linking to reality</strong></td><td>Connect objects to code</td><td></td><td><a href="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FSZlPidwYBA1ucc4WnHxI%2FLinking%20to%20reality%20-%20banner.png?alt=media&#x26;token=3be5b71f-4a84-4eec-be60-2590e3e497b4">Linking to reality - banner.png</a></td><td></td></tr></tbody></table>
