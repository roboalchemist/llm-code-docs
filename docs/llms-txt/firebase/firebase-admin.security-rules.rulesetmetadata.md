# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md.txt

# RulesetMetadata interface

Required metadata associated with a ruleset.

**Signature:**  

    export interface RulesetMetadata 

## Properties

|                                                                    Property                                                                    |  Type  |                                                                                                                                                                                                     Description                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadatacreatetime) | string | Creation time of the `Ruleset` as a UTC timestamp string.                                                                                                                                                                                                                                                                                                                                                            |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesetmetadata.md#rulesetmetadataname)             | string | Name of the `Ruleset` as a short string. This can be directly passed into APIs like [SecurityRules.getRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetruleset) and [SecurityRules.deleteRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesdeleteruleset). |

## RulesetMetadata.createTime

Creation time of the `Ruleset` as a UTC timestamp string.

**Signature:**  

    readonly createTime: string;

## RulesetMetadata.name

Name of the `Ruleset` as a short string. This can be directly passed into APIs like [SecurityRules.getRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesgetruleset) and [SecurityRules.deleteRuleset()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulesdeleteruleset).

**Signature:**  

    readonly name: string;