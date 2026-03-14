# Source: https://docs.logrocket.com/reference/flutter-error-messages.md

# Capture Error Messages

Capture Flutter error messages in LogRocket

Use `captureMessage()` to manually report an error message. This messages will appear as an Error Issue within LogRocket.

```dart Flutter
var event = LogRocketMessageBuilder('error message');

event.putTagString('subscription', 'Pro');
event.putTagDouble('value', 246.01);
event.putTagBool('isSuccess', false);
event.putTagInt('count', 3);
event.putExtraString('stuff', 'things');
event.putExtraDouble('funds', 123.45);
event.putExtraBool('isEnabled', true);
event.putExtraInt('integer', 8);
```

Add tag and extra fields to send extra metadata about the message. String, boolean, int, and double tag and extra types are supported. Tags and extra data will appear with the error in the LogRocket dashboard Issue view.