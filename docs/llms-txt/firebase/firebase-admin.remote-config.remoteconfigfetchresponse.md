# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigfetchresponse.md.txt

# RemoteConfigFetchResponse class

Represents a fetch response that can be used to interact with RC's client SDK.

**Signature:**  

    export declare class RemoteConfigFetchResponse 

## Constructors

|                                                                                              Constructor                                                                                              | Modifiers |                            Description                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------|
| [(constructor)(app, serverConfig, requestEtag)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigfetchresponse.md#remoteconfigfetchresponseconstructor) |           | Constructs a new instance of the `RemoteConfigFetchResponse` class |

## Methods

|                                                                           Method                                                                            | Modifiers | Description |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigfetchresponse.md#remoteconfigfetchresponsetojson) |           |             |

## RemoteConfigFetchResponse.(constructor)

Constructs a new instance of the `RemoteConfigFetchResponse` class

**Signature:**  

    constructor(app: App, serverConfig: ServerConfig, requestEtag?: string);

### Parameters

|  Parameter   |                                                                   Type                                                                    |                        Description                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| app          | App                                                                                                                                       | The app for this RemoteConfig service.                     |
| serverConfig | [ServerConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfig_interface) | The server config for which to generate a fetch response.  |
| requestEtag  | string                                                                                                                                    | A request eTag with which to compare the current response. |

## RemoteConfigFetchResponse.toJSON()

**Signature:**  

    toJSON(): FetchResponseData;

**Returns:**

[FetchResponseData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md#fetchresponsedata_interface)

JSON representation of the fetch response that can be consumed by the RC client SDK.