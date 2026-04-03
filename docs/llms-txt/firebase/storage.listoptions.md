# Source: https://firebase.google.com/docs/reference/js/storage.listoptions.md.txt

# ListOptions interface

The options `list()` accepts.

**Signature:**  

    export interface ListOptions 

## Properties

|                                                 Property                                                 |      Type      |                                                    Description                                                    |
|----------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| [maxResults](https://firebase.google.com/docs/reference/js/storage.listoptions.md#listoptionsmaxresults) | number \| null | If set, limits the total number of `prefixes` and `items` to return. The default and maximum maxResults is 1000.  |
| [pageToken](https://firebase.google.com/docs/reference/js/storage.listoptions.md#listoptionspagetoken)   | string \| null | The `nextPageToken` from a previous call to `list()`. If provided, listing is resumed from the previous position. |

## ListOptions.maxResults

If set, limits the total number of `prefixes` and `items` to return. The default and maximum maxResults is 1000.

**Signature:**  

    maxResults?: number | null;

## ListOptions.pageToken

The `nextPageToken` from a previous call to `list()`. If provided, listing is resumed from the previous position.

**Signature:**  

    pageToken?: string | null;