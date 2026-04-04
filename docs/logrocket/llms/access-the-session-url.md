# Source: https://docs.logrocket.com/reference/access-the-session-url.md

# Access the Session URL

Access the LogRocket Session URL in your Flutter application

There might be scenarios in which you want to handle the generated URL of a LogRocket session, for example by logging it to a third-party service as context. In the Flutter SDK, you can supply a callback with access to the session URL at initialization as part of the `LogRocketWrapConfiguration`. When a LogRocket session has been accepted, your callback will be invoked with the session URL. This generally occurs within 1-5 seconds from SDK initialization.

```dart Flutter
import 'package:logrocket_flutter/logrocket_flutter.dart';

void main() {
  LogRocket.wrap(
    LogRocketWrapConfiguration(
      getSessionUrl: (sessionUrl) {
        // Handle session URL here
      },
    ),
    () {
      runApp(MyApp());
    },
  );
}
```