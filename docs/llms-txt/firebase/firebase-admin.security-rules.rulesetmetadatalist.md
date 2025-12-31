# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadatalist.md.txt

# RulesetMetadataList class

A page of ruleset metadata.

**Signature:**  

    export declare class RulesetMetadataList 

## Properties

|                                                                           Property                                                                           | Modifiers |                                                                          Type                                                                           |                                 Description                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [nextPageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadatalist.md#rulesetmetadatalistnextpagetoken) |           | string                                                                                                                                                  | The next page token if available. This is needed to retrieve the next batch. |
| [rulesets](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadatalist.md#rulesetmetadatalistrulesets)           |           | [RulesetMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadata_interface)\[\] | A batch of ruleset metadata.                                                 |

## RulesetMetadataList.nextPageToken

The next page token if available. This is needed to retrieve the next batch.

**Signature:**  

    readonly nextPageToken?: string;

## RulesetMetadataList.rulesets

A batch of ruleset metadata.

**Signature:**  

    readonly rulesets: RulesetMetadata[];