# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.clientinfo.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.clientinfo.md.txt

# testLab.ClientInfo interface

Information about the client which invoked the test.

**Signature:**  

    export interface ClientInfo 

## Properties

|                                                                    Property                                                                    |           Type           |                  Description                  |
|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------|
| [client](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.clientinfo.md#testlabclientinfoclient)   | string                   | Client name, such as "gcloud".                |
| [details](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.clientinfo.md#testlabclientinfodetails) | Record\<string, string\> | Map of detailed information about the client. |

## testLab.ClientInfo.client

Client name, such as "gcloud".

**Signature:**  

    client: string;

## testLab.ClientInfo.details

Map of detailed information about the client.

**Signature:**  

    details: Record<string, string>;