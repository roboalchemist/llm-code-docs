# Source: https://virustotal.readme.io/docs/graph-commonalities.md

# Commonalities and Hunting

# Find commonalities

***

Find common patterns is very important to achieve a successful investigation. VirusTotal Graph gives you the opportunity to find common patterns in a selection of nodes or even the nodes within a relationship.

There is a toolbar in the right side of the graph. That toolbar shows you in real time the status of the commonalities depending on the node selection.

* If there are more than one node selected, it shows the commonalities for the selected nodes
* If there are one or zero nodes selected, it shows the commonalities for all the nodes in the graph.

![VTGraph commonalities icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_icon_20231113.png)

You can also get the commonalities for all the children of a relationship node:

* Right-click the relationship node and select "Calculate commonalities" in the contextual menu
* Select a relationship node, and click "Calculate commonalities" in the left drawer panel

![VTGraph commonalities contextual menu link](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_contextualmenulink_20231113.png)![VTGraph commonalities left panel link](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_leftpanellink_20231113.png)

# Analyze commonalities

***

Once you calculate the commonalities manually or once you click the commonality icon in the toolbar in the right side, the commonalities drawer will show up. This drawer allows you to interact with the graph and its commonalities.

Select a list of commonalities and click the button "Search and add to the graph" to performa a VTI search and aggregate the nodes to the graph.

![VTGraph commonalities add to graph](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_addtograph_20231113.png)

### Commonality contextual menu

All the commonalities have a contextual menu with actions to execute.

* **Show node list:** Open the list nodes that matches this commonality.
* **Add a relationship node:** Create a commonality relationship node to connect all the nodes that matches this commonality.
* **Launch VT search & add to graph:** For the selected commonality, perform a search in VTI and add the result to the graph.
* **Create Yara Rule using this attribute:** Open a new YARA rule with this attribute

![VTGraph commonalities contextual menu](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_contextualmenu_20231113.png)

# Hunting and retrohunt

***

New virus total graph allows you tu integrate your hunting and retrohunt jobs with graph. Open it using the icon in the toolbar placed in the right side of the graph:

![VTGraph commonalities hunting icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_huntingicon_20231113.png)

### Hunting

In this drawer you have your list of rulesets. You can interact with them:

* Load results on graph: Load the next twenty matches of this ruleset in the graph as nodes
* Open results on hunting
* Launch retrohunt: Open this ruleset in a new window to create a retrohunt job
* Delete rule

![VTGraph commonalities hunting options](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_huntingoptions_20231113.png)

### Retrohunt

In this drawer you have the list of retrohunt jobs. The different status of the jobs are

* Starting
* Running
* Aborted
* Aborting
* Finished

The different actions to make with the jobs are:

* Load results on graph: Load the next twenty matches of the job in the graph as nodes
* Open results on hunting
* Download: Download the list of matches
* Delete retrohunt

![VTGraph commonalities retrohunt options](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphcommonalities_retrohuntoptions_20231113.png)