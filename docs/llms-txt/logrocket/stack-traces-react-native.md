# Source: https://docs.logrocket.com/reference/stack-traces-react-native.md

# React Native Stack Traces

Learn how to upload debug files to decode exception stack traces for React Native apps

LogRocket displays captured session errors, exceptions, and crashes in the [Logs pane](https://docs.logrocket.com/docs/session-replay#logs) of the session replay Developer tab. If your application code is minified or obfuscated, you will need to upload debug files from your app build to see decoded symbol names in the associated stack traces.

The `react-native bundle` command can be used to generate bundle and sourcemap files for the JavaScript code in your app's Android and iOS builds:

```shell Android
npx react-native bundle \
  --entry-file index.js \
  --dev false \
  --platform android \
  --bundle-output index.android.bundle
  --sourcemap-output index.android.bundle.map
```

```shell iOS
npx react-native bundle \
  --entry-file index.js \
  --dev false \
  --platform ios \
  --bundle-output index.ios.bundle
  --sourcemap-output index.ios.bundle.map
```

The resulting files can be uploaded via the process outlined for web sourcemaps [here](https://docs.logrocket.com/docs/stacktraces#uploading-source-maps-to-logrocket) (requires logrocket-cli version 0.14.1 or higher). Note that a release will need to be created before the upload command.

For more information on sourcemaps for React Native applications, see official documentation [here](https://reactnative.dev/docs/0.71/sourcemaps).