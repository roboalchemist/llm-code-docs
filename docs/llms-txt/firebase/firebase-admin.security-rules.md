# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.md.txt

# firebase-admin.security-rules package

Security Rules for Cloud Firestore and Cloud Storage.

## Functions

|                                                                 Function                                                                 |                                                                                                                                                                                                    Description                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getSecurityRules(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.md#getsecurityrules_8a40afc) | Gets the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service for the default app or a given app.`admin.securityRules()` can be called with no arguments to access the default app's `SecurityRules` service, or as `admin.securityRules(app)` to access the `SecurityRules` service associated with a specific app. |

## Classes

|                                                                            Class                                                                            |                   Description                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [Ruleset](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#ruleset_class)                                     | A set of Firebase security rules.               |
| [RulesetMetadataList](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadatalist.md#rulesetmetadatalist_class) | A page of ruleset metadata.                     |
| [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class)                   | The Firebase `SecurityRules` service interface. |

## Interfaces

|                                                                      Interface                                                                      |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RulesetMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadata_interface) | Required metadata associated with a ruleset.                                                                                                                                                                                                                                                                                                                                                   |
| [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface)                   | A source file containing some Firebase security rules. The content includes raw source code including text formatting, indentation and comments. Use the [SecurityRules.createRulesFileFromSource()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulescreaterulesfilefromsource) method to create new instances of this type. |

## getSecurityRules(app)

Gets the [SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class) service for the default app or a given app.

`admin.securityRules()` can be called with no arguments to access the default app's `SecurityRules` service, or as `admin.securityRules(app)` to access the `SecurityRules` service associated with a specific app.

**Signature:**  

    export declare function getSecurityRules(app?: App): SecurityRules;

### Parameters

| Parameter | Type |                                                        Description                                                        |
|-----------|------|---------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app to return the `SecurityRules` service for. If not provided, the default `SecurityRules` service is returned. |

**Returns:**

[SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrules_class)

The default `SecurityRules` service if no app is provided, or the `SecurityRules` service associated with the provided app.

### Example 1

    // Get the SecurityRules service for the default app
    const defaultSecurityRules = getSecurityRules();

### Example 2

    // Get the SecurityRules service for a given app
    const otherSecurityRules = getSecurityRules(otherApp);