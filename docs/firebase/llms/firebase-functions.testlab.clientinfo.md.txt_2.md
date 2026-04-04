# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.clientinfo.md.txt

# testLab.ClientInfo class

Information about the client which invoked the test.

**Signature:**

    export declare class ClientInfo 

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [details](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.clientinfo.md#testlabclientinfodetails) |   | { \[key: string\]: string; } | Map of detailed information about the client which invoked the test. |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.clientinfo.md#testlabclientinfoname) |   | string | Client name, e.g. 'gcloud'. |

## testLab.ClientInfo.details

Map of detailed information about the client which invoked the test.

**Signature:**

    details: {
            [key: string]: string;
        };

## testLab.ClientInfo.name

Client name, e.g. 'gcloud'.

**Signature:**

    name: string;