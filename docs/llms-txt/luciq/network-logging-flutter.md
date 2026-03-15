# Source: https://docs.luciq.ai/references/report-data/logging/network-logging-flutter.md

# Network Logging - Flutter

In order to configure Network Logging on Flutter, you'll first need to attach all your network requests to the reports being sent to the dashboard.

### Enabling the Network Logging

To enable the feature when using the dart:io package HttpClient, use the custom Luciq client.

```dart
LuciqCustomHttpClient client = LuciqCustomHttpClient();
```

### Using the Network Logger

You can then continue to use the package normally to make your network requests like in this example.

```dart
client.getUrl(Uri.parse(URL)).then((request) async {
      var response = await request.close();
});
```

We also support the packages http and dio. For details on how to enable network logging for these external packages, refer to the [Luciq Dart Http Adapter](https://github.com/Luciq/Luciq-Dart-http-Adapter) and the [Luciq Dio Interceptor](https://github.com/Luciq/Luciq-Dio-Interceptor) repositories.
