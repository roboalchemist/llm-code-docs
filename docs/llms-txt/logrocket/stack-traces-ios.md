# Source: https://docs.logrocket.com/reference/stack-traces-ios.md

# iOS Stack Traces

Learn how to upload debug files for decoding obfuscated stack traces

LogRocket displays [captured session errors](https://docs.logrocket.com/reference/capture-error-messages) and crashes in the [Logs pane](https://docs.logrocket.com/docs/session-replay#logs) of the session replay Developer tab. If your application code is minified or obfuscated, you will need to upload debug files from your app build to see decoded symbol names in the associated stack traces.

## Upload debug files to LogRocket

**Self hosted instances require additional steps, and should follow the[ documentation here](https://docs.logrocket.com/docs/mobile-stack-trace-deobfuscation#/).**

To upload files you will need to install the LogRocket command line tool (requires version 0.14.0 or above):

```shell
npm install -g logrocket-cli
```

Unlike for JavaScript source maps, it is not necessary to create a release through the CLI before uploading mobile debug files. However, you must provide a release identifier that matches your [CFBundleVersion](https://developer.apple.com/documentation/bundleresources/information_property_list).

LogRocket uses the dSYM files generated when an application is built to symbolicate iOS stack traces. To upload these files for use by LogRocket, use the following command:

```shell
logrocket upload-mobile  
    --platform ios  
    --release="release_identifier"  
    --apikey="your:api:key"  
    ./path/to/debug/files/myApplication.app.dSYM/
```

You can find your API key in LogRocket under Settings > General Settings > Development.

The cli will recursively scan the contents of the provided directory for relevant files and attempt to upload them (the --verbose flag can be used to see the full list of matching files). Multiple paths can be passed to the command if necessary. Once the files are uploaded, they will be used for symbolicating incoming stack traces from sessions using the specified release version.

For more information on iOS stack traces and debug files, see official documentation [here](https://developer.apple.com/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report#Locate-a-dSYM-using-Spotlight).

## Mobile stack traces in Issues

Stack traces are available within an iOS exception/error's Issue Details view below event previews.