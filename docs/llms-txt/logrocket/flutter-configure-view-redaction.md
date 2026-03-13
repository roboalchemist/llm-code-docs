# Source: https://docs.logrocket.com/reference/flutter-configure-view-redaction.md

# Sanitize View Data

Sanitize and Redact Flutter view screenshots

## Visual Redaction

In Flutter session replay, widgets can be redacted from session replay by wrapping them in the `LogRocketRedact` widget. When widget is redacted, it appears in Session Replay as a dark grey box. This visual redaction is performed client side, so no redacted information is ever sent to LogRocket.

```dart Flutter
import 'package:logrocket_flutter/logrocket_flutter.dart'; 

class MyCheckoutPage extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children:[
        LogRocketRedact(
          child: MyAddressForm(),
        ),
        ...
      ],
    ),
  }    
}
```

## Touch Redaction

By default, LogRocket will still capture touch events on redacted elements. This means that session recordings will show the location of any user interactions with redacted elements, but will not include specific details about the element, such as any text it contains. If you prefer that the session does not show touches on a redacted element, simply add the `preventsTouchCapture: true` property to that `LogRocketRedact` widget.

```dart Flutter
LogRocketRedact(
  preventsTouchCapture: true,
  child: MyPINPad(),
),
```

## Pause View Capture

To pause and unpause view capture, the following LogRocket calls can be used:

```dart
import 'package:logrocket_flutter/logrocket_flutter.dart';

LogRocket.pauseViewCapture();
LogRocket.unpauseViewCapture();
```