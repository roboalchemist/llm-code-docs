# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md.txt

# analytics.ExportBundleInfo class

Interface representing the bundle these events were uploaded to.

**Signature:**  

    export declare class ExportBundleInfo 

## Constructors

|                                                                               Constructor                                                                               | Modifiers |                        Description                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [(constructor)(wireFormat)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md#analyticsexportbundleinfoconstructor) |           | Constructs a new instance of the `ExportBundleInfo` class |

## Properties

|                                                                                   Property                                                                                    | Modifiers |  Type  |                                 Description                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------------------------------|
| [bundleSequenceId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md#analyticsexportbundleinfobundlesequenceid)           |           | number | Monotonically increasing index for each bundle set by the Analytics SDK.    |
| [serverTimestampOffset](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md#analyticsexportbundleinfoservertimestampoffset) |           | number | Timestamp offset (in milliseconds) between collection time and upload time. |

## analytics.ExportBundleInfo.(constructor)

Constructs a new instance of the `ExportBundleInfo` class

**Signature:**  

    constructor(wireFormat: any);

### Parameters

| Parameter  | Type | Description |
|------------|------|-------------|
| wireFormat | any  |             |

## analytics.ExportBundleInfo.bundleSequenceId

Monotonically increasing index for each bundle set by the Analytics SDK.

**Signature:**  

    bundleSequenceId: number;

## analytics.ExportBundleInfo.serverTimestampOffset

Timestamp offset (in milliseconds) between collection time and upload time.

**Signature:**  

    serverTimestampOffset: number;