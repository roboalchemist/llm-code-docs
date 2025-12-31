# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md.txt

# Ruleset class

A set of Firebase security rules.

**Signature:**  

    export declare class Ruleset implements RulesetMetadata 

**Implements:** [RulesetMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadata_interface)

## Properties

|                                                            Property                                                            | Modifiers |                                                                 Type                                                                  |                                                                                                                                                                                                     Description                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#rulesetcreatetime) |           | string                                                                                                                                | Creation time of the `Ruleset` as a UTC timestamp string.                                                                                                                                                                                                                                                                                                                                                            |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#rulesetname)             |           | string                                                                                                                                | Name of the `Ruleset` as a short string. This can be directly passed into APIs like [SecurityRules.getRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetruleset) and [SecurityRules.deleteRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesdeleteruleset). |
| [source](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.ruleset.md#rulesetsource)         |           | [RulesFile](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfile_interface)\[\] |                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Ruleset.createTime

Creation time of the `Ruleset` as a UTC timestamp string.

**Signature:**  

    readonly createTime: string;

## Ruleset.name

Name of the `Ruleset` as a short string. This can be directly passed into APIs like [SecurityRules.getRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetruleset) and [SecurityRules.deleteRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesdeleteruleset).

**Signature:**  

    readonly name: string;

## Ruleset.source

**Signature:**  

    readonly source: RulesFile[];