# Source: https://virustotal.readme.io/docs/collections-introduction.md

# VirusTotal Collections Introduction

A collection is a live report which contains a title, a group of IoCs (file hashes, URLs, domains and IP addresses) and an optional description. Collections are open to our VirusTotal Community (registered users) and they will be enhanced with VirusTotal analysis metadata providing the latest information we have for the IoCs, along with some aggregated tags. 

[IoC Collection creation](#ioc-collection-creation)

[Collection report](#ioc-collection-report)

[Own Collection Dashboard](#own-ioc-collection-dashboard)

[IoC Collections visibility](#ioc-collections-visibility)

[On quota exceeded](#on-quota-exceeded)

[API Usage](#api-usage)

# IoC Collection creation

***

## Create collection.

You can create a collection through the home view by clicking on the "create an IoC collection" link as shown below:

![Link to create a collection](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_createlink_20231108.png)

You need to add a name, a list of IoCs (file hashes, URLs, domains and IP addresses) and then click on Create collection.

![Collection Details](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_details_20231108.png)

Other places from where you can create IoC collections in the same way are:

* From the **Threat Landscape** module, on the **IoC Collections** tab you will find the **Create IoC Collection** button
* From the user **Profile**, on the **COLLECTIONS** tab you will find the **Create IoC Collection** button

## Create collection from a list of IoCs.

You can create a collection directly with a list of IoCs from a result page, click on "Tools" and "Add to Collection" and "Add to a new collection"

![](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_addtocollection_20241008.png)\
![](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_addtocollection_new_20241008.png)

# IoC Collection report

***

After your collection is created, you'll see a report that looks like this.

![Collection Report](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_report_20231108.png)

We've numbered the elements in the screenshot above for easy reference. They are:

1. Follow the collection for get notifications on new IoCs added.
2. You can share the collection permanent link or post it to Twitter.
3. The collection provides exporting capabilities in STIX, JSON and CSV formats.
4. Open the IoCs in a Graph.
5. You can add more IoCs.
6. Delete the collection.
7. See commonalities between all the IoCs of the collection.
8. See telemetry of all the IoCs of the collection.
9. You can search for IoCs of an specific type to filter the results.
10. You can sort the IoCs by several attributes.
11. Edit IoCs of an specific type: you can add more IoCs or delete selected ones.
12. You can export IoCs of an specific type in STIX, JSON and CSV formats. You can also copy to clipboard. For files you can download a selection of them.
13. Different Tools for the selected IoCs depending on the IoC type: Send to Diff, Open in Graph, Calculate commonalities or Add to another collection.

## Add more IoCs directly from a result page.

When you get a list of IoCs, as a result page, you can select some or all of these IoCs and add them to an already existant collection.

* Check the IoCs you want to add
* Click on Tools
* Click on Add to collection
* Select the collection you want these IoCs to be added to.

![](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_addtocollection_20241008.png)\
![](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_addtocollection_selected_20241008.png)

# Own IoC Collection Dashboard

***

Users can see their created collections in their profile page, as they currently do for graphs and comments.\
![](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_dashboard_20231108.png)

# IoC Collections Visibility

***

You can set the visibility of your collections so they can be stablished as:

* Public
* Private - only you see the collection
* Private - with expanded visibility
  * Internally accessible - only you and the members of your group see the collection
  * Externally accessible - shared with external groups or other selected members

Note only collection owners can change the visibility.

> 🚧 Special privileges required
>
> This feature is only available to users with special privileges.

## Setting IoC collections visibility

### On creation

You can select the visibility when creating an IoC collection using this dropdown in the bottom of the creation dialog:

![Collections X Integration](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_visibility_creation_20240111.png)

### From IoC collection report

You can modify the visibility of an IoC collection owned by you, by clicking on the Share & Visibility icon of your collection:

![Collections share button](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_own_collection_share_20240111.png)

As you can see, you can control the users / groups you stablish as editors / viewers, also set the private / public status of the collection, so this gives the collections owner full control on visibility.

![Collections Custom Visibility](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_custom_visibility_20240111.png)

#### Collaborator types

Collaborators can be groups or users playing one of the following roles:

* Viewer: Can see the collection, but cannot modify
* Editor: Can see the collection, also add / delete IoCs and description.

Collaborators cannot delete collections, neither modify the visibility. Only the owner can perform those actions.

## Public IoC collections

All **public** collections are available in VT under the Associations section of an IoC and also the Threat Landscape section. This way our users benefit from other analysis investigations.

![](https://files.readme.io/148fb54628a436ff88cc797f4249c9ea7c093b00efab0cc552807ee45fda630a-collections_visibility_20260122.png)

<br />

### X Integration

Security community is very active using X to promote their investigations. Public IoC Collections can be shared on X using the share link in the collections report header:

![Collections X Integration](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_share_collection_20240111.png)

The VT IoC Collection report shows the following card on X.

![Collections X Integration Card](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_twitter_20231108.png)

## Private IoC collections

**Private** IoC collections can be found in VirusTotal on the [Threat Landscape section](https://www.virustotal.com/gui/threat-landscape/ioc-collections) or listed on the "Associations" tab of IoCs reports, and they can be identified through the "Private" tag.

A private IoC collection will usually be accessible to its owner or users who belong to the same VT group, as configured at creation time.\
However, private collections can be shared with external groups or specific members while maintaining their private status.

Tipically, they are used for work-in-progress collections, then these collections may be shared with the desired scope. Check the [Collections Visibility](#ioc-collections-visibility) section for more details on how to create a private collection.

> ⚠️
>
> Unlike with public collections, IoCs added to a private collection will not automatically generate a report if they are not already part of our existing database.\
> To provide the IoC report, the IoC must be scanned then made searchable and its report available to all Google TI users. So users must scan those IoCs separately to prevent potential leaks.

# On quota exceeded

***

Public users will have a quota of 20 Collections per month, if you reach the limit you would find the following message.

![Collections Quota exceeded message](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/collections_quotaexceeded_20231108.png)

 

# API usage

***

As usual we have also most of the functionality available using our API v3. You can check the API documentation in our [API Reference](https://virustotal.readme.io/reference/collections-create) page.