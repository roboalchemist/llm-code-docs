# Source: https://docs.logrocket.com/reference/stack-traces-android.md

# Android Stack Traces

Learn how to upload a mapping file to unminify Android stack traces

LogRocket displays captured [errors](https://docs.logrocket.com/reference/android-capture-errors) , [exceptions](https://docs.logrocket.com/reference/android-capture-exceptions) and crashes in the [Logs pane](https://docs.logrocket.com/docs/session-replay#logs) of the session replay Developer tab. If your application code is minified, you will need to upload the mapping file from your app build to see decoded symbol names in the associated stack traces.

## Upload debug files to LogRocket

**Self hosted instances require additional steps, and should follow the[ documentation here](https://docs.logrocket.com/docs/mobile-stack-trace-deobfuscation#/).**

To upload files you will need to install the LogRocket command line tool (requires version 0.14.0 or above):

```shell
npm install -g logrocket-cli
```

Unlike for javascript sourcemaps, it is not necessary to create a release through the CLI before uploading mobile debug files. However, you must provide a release identifier that matches your app build's [versionName](https://developer.android.com/studio/publish/versioning#versionvalues).

When an Android application is minified with ProGuard or R8, a mapping file is generated that LogRocket can use to decode application stack traces (generally named `mapping.txt`). To upload this file to LogRocket, use the following command:

```shell
logrocket upload-mobile  
    --platform android  
    --release="release_identifier"  
    --apikey="your:api:key"  
    ./path/to/mapping.txt
```

You can find your API key in LogRocket under Settings > General Settings > Development.

The provided path should point to a specific mapping file, which the cli will attempt to upload. Once the file is uploaded, it will be used for deminifying incoming stack traces from sessions using the specified release version.

For more information on obfuscating and decoding stack traces in Android, see official documentation [here](https://developer.android.com/build/shrink-code#retracing).

## Mobile stack traces in Issues

Stack traces are available within an Android exception/error's Issue Details view below event previews.