# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md.txt

# RulesFile interface

A source file containing some Firebase security rules. The content includes raw source code including text formatting, indentation and comments. Use the [SecurityRules.createRulesFileFromSource()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.securityrules.md#securityrulescreaterulesfilefromsource) method to create new instances of this type.

**Signature:**  

    export interface RulesFile 

## Properties

|                                                           Property                                                           |  Type  | Description |
|------------------------------------------------------------------------------------------------------------------------------|--------|-------------|
| [content](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfilecontent) | string |             |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.security-rules.rulesfile.md#rulesfilename)       | string |             |

## RulesFile.content

**Signature:**  

    readonly content: string;

## RulesFile.name

**Signature:**  

    readonly name: string;