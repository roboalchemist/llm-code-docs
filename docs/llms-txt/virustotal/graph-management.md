# Source: https://virustotal.readme.io/docs/graph-management.md

# Management

<style>
.tbd {  
  background-color: lightgray;  
}  
table {  
  width: 100%;  
  padding: 5px 2px 11px 4px;  
  font-size: 12px;  
  vertical-align: top;  
}  
table td:first-child {  
  max-width: 100px;  
}  
table td:nth-child(2) {  
  max-width: 100px;  
  text-align: center;  
}  
table td:nth-child(3) {  
  max-width: 100px;  
 text-align: center; 
}  
table td:nth-child(4) {  
  max-width: 100px;  
 text-align: center;   
}  
table td:nth-child(5) {  
  max-width: 100px;  
 text-align: center;   
}  
</style>

# GRAPHS MANAGEMENT

It is essential that when you are working in an investigation you are able to stop today and resume your investigation tomorrow. At the same time, you might want to share the graph with you colleagues so they can add their insights to the graph and, finally, publish it once you have finished working on it, if you decide to. All of these cases are covered by VirusTotal Graph.

In summary, you can:

* Edit graphs.
* Share graphs with other users or groups.
* Set graphs private.
* Embed your graphs in any webpage.

## Create

***

You can save the progress you made on your graph doing click on the “Save graph” button or clicking the "File-->Save" menu item.

![VirusTotal Graph save icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_saveicon_20231113.png)

Note: If your premium package includes private graphs and you have not exhausted the quota, all saved graphs are made PRIVATE by default. This means that nobody can see your investigation unless you give them access or making the graph public. If you would like to set you graphs PUBLIC, see the section below.

## Collaborate

***

The sharing panel gives you the opportunity to include other users as viewers or editors of the graph.

Click the shared/embedded button to open the shared modal.

![VirusTotal Graph share button](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_sharebutton_20231113.png)

Viewers will get read-only access to the graph. In the case of editors, they will be able to modify and save the graph, add more collaborators or set the graph public/private. Although, only graph owners can delete graphs.

|            |      |                     |                   |              |
| ---------- | ---- | ------------------- | ----------------- | ------------ |
| Role       | Read | Expand/Delete nodes | Add collaborators | Delete graph |
| **Owner**  | Yes  | Yes                 | Yes               | Yes          |
| **Editor** | Yes  | Yes                 | Yes               | No           |
| **Viewer** | Yes  | No                  | No                | No           |

To add a user or group as editor or viewer you just need to type the user identifier in the collaborators input, select from the dropdown if the user is editor or viewer and finally click on the add button to save the changes.

![VirusTotal Graph add user button](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_adduserbutton_20231113.png)

## Private graphs

***

As part of the premium package, you can set graphs private to collaborators, so only viewers or editors can find and access the graph.

The visibility of the graph can be changed at anytime by the graph owner.

![VirusTotal Graph visibility button](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_visibilitybutton_20231113.png)

To make a graph public or private you just need to click on the button of the same name in the sharing panel.

## Embed

***

Once an investigation has been finished, often you want to share the result of the investigation with other researchers or publish it on your website.

VirusTotal Graph allows you to embed public graphs in web pages thanks to our graph viewer that loads a lighter and read-only version of the graph.

Same way other resources are embedded on the internet nowadays, VirusTotal Graph is embedded using iframes. To add the graph in your website you just need to copy the html snippet from the embed graph panel as described below and paste it in your webpage.

![VirusTotal Graph embed html](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_embedhtml_20231113.png)

## Main menu

***

You have a main menu that allows you to interact with the graph and with the different nodes within the graph.

* **File**: Management of the graph
* **Edit**: Interactions with all the nodes of the graph
* **View**: Management of the visible information of the nodes within the graph
* **Selection**: Interactions with the selected nodes of the graph
* **Visualization**: Different visualizations

![VirusTotal Graph main menu](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_mainmenu_20231113.png)

## Graph toolbar

***

Type 3 characters or more in the input box to perform a search within the nodes of the current graph.

![VirusTotal Graph input box](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_inputbox_20231113.png)

Use the icons in the toolbar to:

![VirusTotal Graph add node icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_addnodeicon_20231113.png): Add a new node to the graph

![VirusTotal Graph undo icon](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_undoicon_20231113.png): Undo the latest nodes added or removed to the graph

![VirusTotal Graph redo icont](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphmanagement_redoicon_20231113.png): Redo the latest nodes added or removed to the graph