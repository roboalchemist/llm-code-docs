# Source: https://developers.webflow.com/data/v1.0.0/reference/collection_item_created.mdx

***

title: Collection Item Created
slug: data/reference/collection\_item\_created
description: The information about the collection item that was created
hidden: false
-------------

## Trigger Type

`collection_item_created `

## Properties

| Field        | Type    | Description                                                                                                          |
| :----------- | :------ | :------------------------------------------------------------------------------------------------------------------- |
| `_archived ` | Boolean | Boolean determining if the Item is set to archived                                                                   |
| `_draft `    | Boolean | Boolean determining if the Item is set to draft                                                                      |
| `_id `       | string  | Unique identifier for the Item                                                                                       |
| `_cid `      | string  | Unique identifier for the Collection the Item belongs within                                                         |
| `name `      | string  | Name given to the Item                                                                                               |
| `slug `      | string  | URL structure of the Item in your site. Note: Updates to an item slug will break all links referencing the old slug. |

## Example

```json
{
    "_archived": false,
    "_draft": false,
    "color": "#a98080",
    "name": "Exciting blog post title",
    "post-body": "<p>Blog post contents...</p>",
    "post-summary": "Summary of exciting blog post",
    "main-image": {
        "fileId": "580e63fe8c9a982ac9b8b749",
        "url": "https://dev-assets.website-files.com/580e63fc8c9a982ac9b8b744/580e63fe8c9a982ac9b8b749_1477338110257-image20.jpg"
    },
    "slug": "exciting-post",
    "author": "580e640c8c9a982ac9b8b778",
    "updated-on": "2016-11-15T22:45:32.647Z",
    "updated-by": "Person_5660c5338e9d3b0bee3b86aa",
    "created-on": "2016-11-15T22:45:32.647Z",
    "created-by": "Person_5660c5338e9d3b0bee3b86aa",
    "published-on": null,
    "published-by": null,
    "_cid": "580e63fc8c9a982ac9b8b745",
    "_id": "582b900cba19143b2bb8a759"
}
```
