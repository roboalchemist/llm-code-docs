# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md.txt

# SecurityRules class

The Firebase `SecurityRules` service interface.

**Signature:**  

    export declare class SecurityRules 

## Properties

|                                                           Property                                                           | Modifiers | Type | Description |
|------------------------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesapp) |           | App  |             |

## Methods

|                                                                                                Method                                                                                                | Modifiers |                                                                                                                                                                                                             Description                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createRuleset(file)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulescreateruleset)                                               |           | Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface).                                                                                                                                              |
| [createRulesFileFromSource(name, source)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulescreaterulesfilefromsource)               |           | Creates a [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface) with the given name and source. Throws an error if any of the arguments are invalid. This is a local operation, and does not involve any network API calls.                                                                                                                              |
| [deleteRuleset(name)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesdeleteruleset)                                               |           | Deletes the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) identified by the given name. The input name should be the short name string without the project ID prefix. For example, to delete the `projects/project-id/rulesets/my-ruleset`, pass the short name "my-ruleset". Rejects with a `not-found` error if the specified `Ruleset` cannot be found. |
| [getFirestoreRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetfirestoreruleset)                                       |           | Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) currently applied to Cloud Firestore. Rejects with a `not-found` error if no ruleset is applied on Firestore.                                                                                                                                                                                       |
| [getRuleset(name)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetruleset)                                                     |           | Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) identified by the given name. The input name should be the short name string without the project ID prefix. For example, to retrieve the `projects/project-id/rulesets/my-ruleset`, pass the short name "my-ruleset". Rejects with a `not-found` error if the specified `Ruleset` cannot be found.  |
| [getStorageRuleset(bucket)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetstorageruleset)                                     |           | Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) currently applied to a Cloud Storage bucket. Rejects with a `not-found` error if no ruleset is applied on the bucket.                                                                                                                                                                               |
| [listRulesetMetadata(pageSize, nextPageToken)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityruleslistrulesetmetadata)                |           | Retrieves a page of ruleset metadata.                                                                                                                                                                                                                                                                                                                                                                                                |
| [releaseFirestoreRuleset(ruleset)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesreleasefirestoreruleset)                        |           | Applies the specified [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) ruleset to Cloud Firestore.                                                                                                                                                                                                                                                            |
| [releaseFirestoreRulesetFromSource(source)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesreleasefirestorerulesetfromsource)     |           | Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given source, and applies it to Cloud Firestore.                                                                                                                                                                                                                                      |
| [releaseStorageRuleset(ruleset, bucket)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesreleasestorageruleset)                    |           | Applies the specified [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) ruleset to a Cloud Storage bucket.                                                                                                                                                                                                                                                     |
| [releaseStorageRulesetFromSource(source, bucket)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesreleasestoragerulesetfromsource) |           | Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given source, and applies it to a Cloud Storage bucket.                                                                                                                                                                                                                               |

## SecurityRules.app

**Signature:**  

    readonly app: App;

## SecurityRules.createRuleset()

Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface).

**Signature:**  

    createRuleset(file: RulesFile): Promise<Ruleset>;

### Parameters

| Parameter |                                                               Type                                                                |                 Description                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| file      | [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface) | Rules file to include in the new `Ruleset`. |

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills with the newly created `Ruleset`.

## SecurityRules.createRulesFileFromSource()

Creates a [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface) with the given name and source. Throws an error if any of the arguments are invalid. This is a local operation, and does not involve any network API calls.

**Signature:**  

    createRulesFileFromSource(name: string, source: string | Buffer): RulesFile;

### Parameters

| Parameter |       Type       |                                                  Description                                                   |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------|
| name      | string           | Name to assign to the rules file. This is usually a short file name that helps identify the file in a ruleset. |
| source    | string \| Buffer | Contents of the rules file.                                                                                    |

**Returns:**

[RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface)

A new rules file instance.

### Example

    const source = '// Some rules source';
    const rulesFile = admin.securityRules().createRulesFileFromSource(
      'firestore.rules', source);

## SecurityRules.deleteRuleset()

Deletes the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) identified by the given name. The input name should be the short name string without the project ID prefix. For example, to delete the `projects/project-id/rulesets/my-ruleset`, pass the short name "my-ruleset". Rejects with a `not-found` error if the specified `Ruleset` cannot be found.

**Signature:**  

    deleteRuleset(name: string): Promise<void>;

### Parameters

| Parameter |  Type  |           Description            |
|-----------|--------|----------------------------------|
| name      | string | Name of the `Ruleset` to delete. |

**Returns:**

Promise\<void\>

A promise that fulfills when the `Ruleset` is deleted.

## SecurityRules.getFirestoreRuleset()

Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) currently applied to Cloud Firestore. Rejects with a `not-found` error if no ruleset is applied on Firestore.

**Signature:**  

    getFirestoreRuleset(): Promise<Ruleset>;

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills with the Firestore ruleset.

## SecurityRules.getRuleset()

Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) identified by the given name. The input name should be the short name string without the project ID prefix. For example, to retrieve the `projects/project-id/rulesets/my-ruleset`, pass the short name "my-ruleset". Rejects with a `not-found` error if the specified `Ruleset` cannot be found.

**Signature:**  

    getRuleset(name: string): Promise<Ruleset>;

### Parameters

| Parameter |  Type  |            Description             |
|-----------|--------|------------------------------------|
| name      | string | Name of the `Ruleset` to retrieve. |

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills with the specified `Ruleset`.

## SecurityRules.getStorageRuleset()

Gets the [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) currently applied to a Cloud Storage bucket. Rejects with a `not-found` error if no ruleset is applied on the bucket.

**Signature:**  

    getStorageRuleset(bucket?: string): Promise<Ruleset>;

### Parameters

| Parameter |  Type  |                                                                          Description                                                                          |
|-----------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bucket    | string | Optional name of the Cloud Storage bucket to be retrieved. If not specified, retrieves the ruleset applied on the default bucket configured via `AppOptions`. |

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills with the Cloud Storage ruleset.

## SecurityRules.listRulesetMetadata()

Retrieves a page of ruleset metadata.

**Signature:**  

    listRulesetMetadata(pageSize?: number, nextPageToken?: string): Promise<RulesetMetadataList>;

### Parameters

|   Parameter   |  Type  |                                     Description                                      |
|---------------|--------|--------------------------------------------------------------------------------------|
| pageSize      | number | The page size, 100 if undefined. This is also the maximum allowed limit.             |
| nextPageToken | string | The next page token. If not specified, returns rulesets starting without any offset. |

**Returns:**

Promise\<[RulesetMetadataList](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadatalist.md#rulesetmetadatalist_class)\>

A promise that fulfills with a page of rulesets.

## SecurityRules.releaseFirestoreRuleset()

Applies the specified [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) ruleset to Cloud Firestore.

**Signature:**  

    releaseFirestoreRuleset(ruleset: string | RulesetMetadata): Promise<void>;

### Parameters

| Parameter |                                                                             Type                                                                              |                                   Description                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ruleset   | string \| [RulesetMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadata_interface) | Name of the ruleset to apply or a `RulesetMetadata` object containing the name. |

**Returns:**

Promise\<void\>

A promise that fulfills when the ruleset is released.

## SecurityRules.releaseFirestoreRulesetFromSource()

Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given source, and applies it to Cloud Firestore.

**Signature:**  

    releaseFirestoreRulesetFromSource(source: string | Buffer): Promise<Ruleset>;

### Parameters

| Parameter |       Type       |      Description       |
|-----------|------------------|------------------------|
| source    | string \| Buffer | Rules source to apply. |

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills when the ruleset is created and released.

## SecurityRules.releaseStorageRuleset()

Applies the specified [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) ruleset to a Cloud Storage bucket.

**Signature:**  

    releaseStorageRuleset(ruleset: string | RulesetMetadata, bucket?: string): Promise<void>;

### Parameters

| Parameter |                                                                             Type                                                                              |                                                                                                                              Description                                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ruleset   | string \| [RulesetMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadata_interface) | Name of the ruleset to apply or a `RulesetMetadata` object containing the name.                                                                                                                                                                                        |
| bucket    | string                                                                                                                                                        | Optional name of the Cloud Storage bucket to apply the rules on. If not specified, applies the ruleset on the default bucket configured via [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface). |

**Returns:**

Promise\<void\>

A promise that fulfills when the ruleset is released.

## SecurityRules.releaseStorageRulesetFromSource()

Creates a new [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class) from the given source, and applies it to a Cloud Storage bucket.

**Signature:**  

    releaseStorageRulesetFromSource(source: string | Buffer, bucket?: string): Promise<Ruleset>;

### Parameters

| Parameter |       Type       |                                                                                                                              Description                                                                                                                               |
|-----------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| source    | string \| Buffer | Rules source to apply.                                                                                                                                                                                                                                                 |
| bucket    | string           | Optional name of the Cloud Storage bucket to apply the rules on. If not specified, applies the ruleset on the default bucket configured via [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface). |

**Returns:**

Promise\<[Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)\>

A promise that fulfills when the ruleset is created and released.