# Source: https://virustotal.readme.io/docs/graph-nodes.md

# Nodes

Each node in the graph represents an entity. There are 5 basic entity types:

**Files**. Represented as a rectangular shape with a representation of the file inside.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_exeicon_20231113.png",
        null,
        "VTGraph exe icon"
      ],
      "align": "left",
      "sizing": "40px"
    }
  ]
}
[/block]

`__MAGIC_BLOCK_1__` <br/><br/>

**Domains**. 

Represented using the domain favicon, if available.

![VTGraph domain icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_domainicon_20231113.png)

**Urls**. Represented using the icon below.

![VTGraph URL icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_urlicon_20231113.png)

**IP Addresses**. Represented using the flag for its country. If we can’t detect the country from which the IP address is from, we’ll represent it as a black rectangle.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_usflagicon_20231113.png",
        null,
        "VTGraph US flag icon"
      ],
      "align": "left",
      "sizing": "40px"
    }
  ]
}
[/block]

`__MAGIC_BLOCK_3__` <br/><br/>

**Relationship nodes**. Represented with a circle containing a representative icon inside.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_resolutionsicon_20231113.png",
        null,
        "VTGraph resolutions icon"
      ],
      "align": "left",
      "sizing": "40px"
    }
  ]
}
[/block]

`__MAGIC_BLOCK_5__` <br/><br/>

The example below is a connection of contacted ip between hash abcde1234 and ip address 1.1.1.1

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_iprelation_20231113.png",
        null,
        "VTGraph ip relations"
      ],
      "align": "center",
      "sizing": "240px"
    }
  ]
}
[/block]

More than one ip address was related to abcde1234 file.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_multiplesipsrelations_20231113.png",
        null,
        "VTGraph Multiple ip relations"
      ],
      "align": "center",
      "sizing": "240px"
    }
  ]
}
[/block]

## Advanced node types

***

In addition to the entity node types, VT Graph also offers these some advanced node types you can use to enrich your investigation with:

`__MAGIC_BLOCK_8__` <br/>Actor<br/>

`__MAGIC_BLOCK_9__` <br/>Department<br/>

`__MAGIC_BLOCK_10__` <br/>Email<br/>

`__MAGIC_BLOCK_11__` <br/>Victim<br/>

`__MAGIC_BLOCK_12__` <br/>Device<br/>

`__MAGIC_BLOCK_13__` <br/>Port<br/>

`__MAGIC_BLOCK_14__` <br/>Service<br/>

`__MAGIC_BLOCK_15__` <br/>SSL Certificate<br/>

`__MAGIC_BLOCK_16__` <br/>Wallet<br/>

These nodes are only available for customers with the Private Graph add on. Contact our team if you are interested in our premium features, [here](https://www.virustotal.com/gui/contact-us/premium-services).

## Color coding of nodes and edges

***

VT Graph use color coding to represent extra information about nodes and their connections.

VirusTotal contains **verdicts** for files and urls. Graph represents files and urls that have 1 or more detections using red icons. Otherwise, the color black is used.

`__MAGIC_BLOCK_17__` <br/>0 detections<br/>

`__MAGIC_BLOCK_18__` <br/>1+ detections<br/>

`__MAGIC_BLOCK_19__` <br/>selected<br/>

`__MAGIC_BLOCK_20__` <br/>can be expanded<br/>

Nodes that have not been **expanded** yet are represented with a black circle in top right corner. Double clicking on unexpanded nodes will automatically trigger an auto-expansion on that node.

**Selected nodes** are represented using blue circle. The edges of their direct connections are also represented in blue.

VT Graph uses a kind of node to represent relationships. Arrow edges are used to represent the **direction of the relationship**.

## Actions

***

After a node or relationship is selected, different actions can be performed. Furthermore, bulk actions can be performed over multiple nodes when selected.

## Node

***

Once a node is selected, the left panel will show the relevant information related to it. From there, you will be able to expand relationships, find detection verdicts, comments, etc.

![VTGraph left panel](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_leftpanel_20231113.png)

There are actions that can be performed over the selected node. Doing right click over a node will show a contextual menu with the same actions that can be performed from the left panel.

`__MAGIC_BLOCK_21__` <br/>**Edit Label**<br/>

Allows to edit the node label. To delete the label, just leave it empty. By default, the initial will be labeled with the file name if we have it, “Root node” otherwise. For urls, domains and ip, we’ll use the display value as label.

`__MAGIC_BLOCK_22__` <br/>**Add new node**<br/>

Opens the panel which guides you to add a new connected node to the selected node. Links connecting nodes that have been manually added are represented with a dotted line.

`__MAGIC_BLOCK_23__` <br/>**Center node**<br/>

Center the node in the screen

`__MAGIC_BLOCK_24__` <br/>**Pin node / Remove pin**<br/>

Removes the animation or gravity from the graph. By default, the nodes can be dragged but they'll return to a stable graph representation after the click.

When we pin the node, it will stick to the position where we drag it. If we want the node to recover their default behaviour we can "remove pin" from the node.

`__MAGIC_BLOCK_25__` <br/>**Highlight**<br/>

Big graphs contains a lot of nodes and edges and they are complicated to understand. To help with this problem we can highlight a node, this will hide the nodes that are not directly connected to the highlighted node. You can remove the highlight by clicking somewhere else in the graph.

`__MAGIC_BLOCK_26__` <br/>**Select children**<br/>

Select the list of nodes that are children of the selected node

`__MAGIC_BLOCK_27__` <br/>**Select parents**<br/>

Select the list of nodes that are parents of the selected node

`__MAGIC_BLOCK_28__` <br/>**Delete node**<br/>

Deletes the selected nodes and its edges. 

`__MAGIC_BLOCK_29__` <br/>**Full expansion**<br/>

Expands by all the available expansions for the selected node. It performs the same action as clicking individually in each expansion in the expansion section. By default the first node in the investigation will be expanded using all their available expansions.

`__MAGIC_BLOCK_30__` <br/>**Open public report**<br/>

Opens the VirusTotal public report for the selected node.

## Relationship node

***

Relationship nodes are special as they are represented as a single node that group other nodes. Because that, it merges actions from both single and multiple node selection.

![VTGraph relationship nodes menu](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_relationshipnodesmenu_20231113.png)

`__MAGIC_BLOCK_31__` <br/>**Edit Label**<br/>

Allows to edit the node label. To delete the label, just leave it empty. By default, the initial will be labeled with the file name if we have it, “Root node” otherwise. For urls, domains and ip, we’ll use the display value as label.

`__MAGIC_BLOCK_32__` <br/>**Add connected node**<br/>

Opens the panel which guides you to add a new connected node to the selected node. Links connecting nodes that have been manually added are represented with a dotted line.

`__MAGIC_BLOCK_33__` <br/>**Center node**<br/>

Center the node in the screen

`__MAGIC_BLOCK_34__` <br/>**Pin node / Unpin node**<br/>

Removes the animation or gravity from the graph. By default, the nodes can be dragged but they'll return to a stable graph representation after the click.

When we pin the node, it will stick to the position where we drag it. If we want the node to recover their default behaviour we can "remove pin" from the node.

`__MAGIC_BLOCK_35__` <br/>**Download CSV**<br/>

Opens a menu with all the entity ids grouped by the selected relationship node.

`__MAGIC_BLOCK_36__` <br/>**Select children**<br/>

Select the list of nodes that are children of the selected node

`__MAGIC_BLOCK_37__` <br/>**Select parents**<br/>

Select the list of nodes that are parents of the selected node

`__MAGIC_BLOCK_38__` <br/>**Align children vertically**<br/>

Align the children of the relationship node vertically

`__MAGIC_BLOCK_39__` <br/>**Align children horizontally**<br/>

Align the children of the relationship node horizontally

`__MAGIC_BLOCK_40__` <br/>**Delete**<br/>

Deletes the selected nodes and its edges. 

`__MAGIC_BLOCK_41__` <br/>**Calculate commonalities**<br/>

Find common features and patterns for the children nodes of the relationship node. The results will be shown in the left panel. More info related to that process below.

## Multiple node selection

***

Multiple nodes can be selected at the same time. There are two ways to select multiple nodes.

The first one is doing click at the same time you press the *shift* key on your keyboard. The left panel will be updated with the information related to the selection.

![VTGraph mutiple nodes menu](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_multiplenodesmenu_20231113.png)
 

You can also select multiple nodes by pressing shift and click-dragging in the canvas. The same way you are used to select multiple files in any operating system.

These are the actions available:

`__MAGIC_BLOCK_42__` <br/>**Edit label**<br/>

Allows to edit the node label. To delete the label, just leave it empty. By default, the initial will be labeled with the file name if we have it, “Root node” otherwise. For urls, domains and ip, we’ll use the display value as label.

`__MAGIC_BLOCK_43__` <br/>**Pin node / Remove pin**<br/>

Removes the animation or gravity from the graph. By default, the nodes can be dragged but they'll return to a stable graph representation after the click.

When we pin the node, it will stick to the position where we drag it. If we want the node to recover their default behaviour we can "remove pin" from the node.

`__MAGIC_BLOCK_44__` <br/>**Center node**<br/>

Center the selected nodes in the screen

`__MAGIC_BLOCK_45__` <br/>**Download CSV**<br/>

**Opens a menu with all the entity ids for the nodes selected.**

`__MAGIC_BLOCK_46__` <br/>**Align Children Vertically**<br/>

Align the selected nodes vertically

`__MAGIC_BLOCK_47__` <br/>**Align Children Horizontally**<br/>

Align the selected nodes horizontally

`__MAGIC_BLOCK_48__` <br/>**Delete node**<br/>

Deletes the selected nodes and its edges. 

`__MAGIC_BLOCK_49__` <br/>**Full expansion**<br/>

Expands by all the available expansions for one of the selected nodes. It performs the same action as clicking individually in each expansion in the expansion section. By default the first node in the investigation will be expanded using all their available expansions.

`__MAGIC_BLOCK_50__` <br/>**Calculate commonalities**<br/>

Find common features and patterns for the selected nodes. The results will be shown in the left panel. More info related to that process below.

## Submissions

***

The submission box gives you a graphical representation of the submissions made for the selected file, grouped by country or by upload date.

![VTGraph submissions](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphnodes_submissions_20231113.png)