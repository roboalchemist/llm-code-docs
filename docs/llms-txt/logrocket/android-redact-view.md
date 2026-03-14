# Source: https://docs.logrocket.com/reference/android-redact-view.md

# Sanitize View Data

Redact individual views or disable capture altogether

## Redact views in Jetpack Compose

To redact views in Jetpack Compose, see our [Jetpack Compose Documentation.](https://docs.logrocket.com/reference/jetpack-compose-about)

## Redact Android Views

By default the SDK will automatically skip capturing any view with a tag set to the string `"lr-hide"`. Additional tags can be added when configuring the SDK with the `options.addRedactionTag(Object tag)` method. A non-String Object can be provided for programmatic checks on tags, our SDK will run `tagObject.equals(view.getTag())` against this object.

### `options.addRedactionTag(Object tag)`

Add additional View Tags that should be redacted when capturing the screen. The `lr-hide` tag will always redact views.

## Allow subviews of redacted Android views

In order to capture certain subviews of a redacted Android view, assign the views tag to either `"lr-show"`or another tag specified during SDK configuration using the `options.addAllowTag(Object tag)`method. Allow tag comparison is checked in the same way as redaction tags.

### `options.addAllowTag(Object tag)`

Add additional View Tags that should be allowed when capturing the screen. The `lr-show` tag will always allow views.

## Prevent capturing touch events on redacted views

In order to prevent touches on redacted views from appearing in session replay, the following option must be provided. An example of when this would be useful is if your app redacts a PIN pad

### `options.setCaptureRedactedViewTouches(false)`

## Disable image capture entirely

### `options.setEnableBitmapCapture(boolean enable)`

Disable image capture completely by setting this to `true`.

## Pause View Capture

To completely disable the view capture system call `SDK.pauseViewCapture()`. If a capture is already in progress it will not be stopped, but no view captures will be created until the system is resumed with `SDK.unpauseViewCapture()`.

## Directly Redact / Allow Individual Views

In situations where using tags is not practical (such as if they are procedurally generated) you can individually allow and redact views using the `SDK.redactView(View)` and `SDK.allowView(View)` functions.

```java
public View onCreateView(
  ...
  TextView viewRedactedText = rootView.findViewById(R.id.viewRedactedHeader);
  TextView viewAllowedText = rootView.findViewById(R.id.viewAllowedHeader);

  SDK.redactView(viewRedactedText);
  SDK.allowView(viewAllowedText);
)
```