# Source: https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md.txt

# SnapshotListenOptions interface

An options object that can be passed to [onSnapshot()](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_0312fd7) and [QuerySnapshot.docChanges()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotdocchanges) to control which types of changes to include in the result set.

**Signature:**  

    export declare interface SnapshotListenOptions 

## Properties

|                                                                        Property                                                                         |                                           Type                                           |                                             Description                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [includeMetadataChanges](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptionsincludemetadatachanges) | boolean                                                                                  | Include a change even if only the metadata of the query or of a document changed. Default is false. |
| [source](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptionssource)                                 | [ListenSource](https://firebase.google.com/docs/reference/js/firestore_.md#listensource) | Set the source the query listens to. Default to "default", which listens to both cache and server.  |

## SnapshotListenOptions.includeMetadataChanges

Include a change even if only the metadata of the query or of a document changed. Default is false.

**Signature:**  

    readonly includeMetadataChanges?: boolean;

## SnapshotListenOptions.source

Set the source the query listens to. Default to "default", which listens to both cache and server.

**Signature:**  

    readonly source?: ListenSource;