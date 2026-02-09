# Source: https://docs.datadoghq.com/error_tracking/frontend/mobile/unity.md

---
title: Unity Crash Reporting and Error Tracking
description: Learn how to track Unity errors with Error Tracking.
breadcrumbs: >-
  Docs > Error Tracking > Frontend Error Tracking > Mobile Crash Reporting >
  Unity Crash Reporting and Error Tracking
---

# Unity Crash Reporting and Error Tracking

## Overview{% #overview %}

Enable Crash Reporting and Error Tracking to get comprehensive crash reports and error trends with Real User Monitoring.

Your crash reports appear in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

## Setup{% #setup %}

If you have not set up the Datadog Unity SDK for yet, follow the [in-app setup instructions](https://app.datadoghq.com/rum/application/create) or see the [Unity setup documentation](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/unity/setup/#setup).

### Forward uncaught exceptions from Unity logs{% #forward-uncaught-exceptions-from-unity-logs %}

Unity forwards all uncaught exceptions to its logger using `Debug.LogException`. To report these exceptions to Datadog, check the option in Datadog's project settings labeled "Forward Unity Logs".

### Native crash reporting{% #native-crash-reporting %}

Native crash reporting is enabled for all Datadog Unity SDK projects.

If your application suffers a fatal crash, the Datadog Unity SDK uploads a crash report to Datadog *after* your application restarts. For non-fatal errors or exceptions, the Datadog Unity SDK uploads these errors with other RUM data.

## Get deobfuscated and symbolicated stack traces{% #get-deobfuscated-and-symbolicated-stack-traces %}

Mapping files are used to deobfuscate and symbolicate stack traces, which helps in debugging errors. Using a unique build ID that gets generated, Datadog automatically matches the correct stack traces with the corresponding mapping files. This ensures that regardless of when the mapping file was uploaded (either during pre-production or production builds), the correct information is available for efficient QA processes when reviewing crashes and errors reported in Datadog.

### File and line mapping with IL2CPP{% #file-and-line-mapping-with-il2cpp %}

When using the IL2CPP backend (the default for iOS), C# stack traces from Unity lack any file or line information. This information can be retrieved from the native symbol files and an IL2CPP mapping file, provided the C# stack traces are mapped to native stacks. To enable this, check the "Perform Native Stack Mapping" option in your Unity project settings under the Datadog section and upload your symbol and IL2CPP mapping files as described below.

**Note**: Even when checked, Native Stack Mapping is only enabled in non-development builds.

### Upload symbol files to Datadog{% #upload-symbol-files-to-datadog %}

Native crash reports are collected in a raw format and mostly contain memory addresses. To map these addresses into legible symbol information, Datadog requires that you upload iOS `.dSYM` files, NDK `.so` files, Android Proguard Mapping files, and / or a IL2CPP mapping file, which are generated in your application's build process.

The [@datadog/datadog-ci](https://www.npmjs.com/package/@datadog/datadog-ci) command line tool supports uploading all of the necessary files (dSYMs, sos, Android Proguard Mapping, and IL2CPP Mapping files) in one command.

First, install the `datadog-ci` tool from the instructions above and create a `datadog-ci.json` file at the root of your project, containing your API key and (optionally) your Datadog site:

```json
{
  "apiKey": "<YOUR_DATADOG_API_KEY>",
  "datadogSite": "datadoghq.eu"  // Optional if you are using datadoghq.com
}
```

Because this file contains your API key, it should not be checked into version control.

Alternately, you can set the `DATADOG_API_KEY` and `DATADOG_SITE` environment variables.

Then, you can use the following command to upload all the necessary files for symbolication and deobfuscation of your crash reports:

```sh
# From your build output directory
datadog-ci unity-symbols upload --ios
```

For Android, export an Android project (instead of building the APK directly) and build using the exported project. You can then run datadog-ci from the exported project directory:

```sh
# From your exported project directory
datadog-ci unity-symbols upload --android
```

**Note**: Re-uploading a source map does not override the existing one if the build id has not changed.

For a full list of options, see the `datadog-ci` [Unity Symbols documentation](https://github.com/DataDog/datadog-ci/tree/master/packages/datadog-ci/src/commands/unity-symbols).

### List uploaded symbol files{% #list-uploaded-symbol-files %}

See the [RUM Debug Symbols](https://app.datadoghq.com/source-code/setup/rum) page to view all uploaded symbols.

## Limitations{% #limitations %}

Mapping files are limited in size to **500 MB** each, while dSYM files can go up to **2 GB** each.

## Test your implementation{% #test-your-implementation %}

To verify your Unity Crash Reporting and Error Tracking configuration, issue an error in your application and confirm that the error appears in Datadog.

1. Ensure you are not running a development build. Uncheck the "Development Build" box in Unity's build settings.

1. Run your application on a simulator, emulator, or a real device. If you are running on iOS, ensure that the debugger is not attached. Otherwise, Xcode captures the crash before the Datadog SDK does.

1. Execute code containing an error or crash. For example:

   ```cs
   void ThrowError() {
    throw new Exception("My Exception")
   }
   ```

1. For obfuscated error reports that do not result in a crash, you can verify symbolication and deobfuscation in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

1. For crashes, after the crash happens, restart your application and wait for the Unity SDK to upload the crash report in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

## Further reading{% #further-reading %}

- [dd-sdk-unity Source code](https://github.com/DataDog/dd-sdk-unity)
- [Learn about Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking/)
