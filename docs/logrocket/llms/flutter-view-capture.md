# Source: https://docs.logrocket.com/reference/flutter-view-capture.md

# View Capture

Capture Flutter visuals Session Replay

## LogRocketWidget

View Capture of Flutter screens requires some additional setup. In order to start capturing visuals of a session, add the `LogRocketWidget` above the top level of your app that you would like captured.

```dart Flutter
import 'package:logrocket_flutter/logrocket_flutter.dart'; 

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return LogRocketWidget(
      child: MaterialApp(
        ...
      ),
    ),
  }    
}
```

## Redaction

* **[Sanitize View Data](https://docs.logrocket.com/reference/flutter-configure-view-redaction#/)**
* **[Pause View Capture](https://docs.logrocket.com/reference/flutter-configure-view-redaction#pause-view-capture)**