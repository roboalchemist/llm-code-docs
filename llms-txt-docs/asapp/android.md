# Source: https://docs.asapp.com/messaging-platform/integrations/chat-instead/android.md

# Android

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6c090683e346494299829f92a2b504f7" data-og-width="1080" width="1080" data-og-height="813" height="813" data-path="image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=f85b5bfd2f13a4b1a7f193f53a7163b0 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=81684b834413f1e53f9816459382fe7e 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e4f6883a5424c1c5ddb27e24cc966a59 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a58ec12605c7ad41614fa4e2616c752b 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=cf763010f156fc2f3867ebc3bce1e05c 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b0545f1-bbc3-d676-aebd-2e478cc8406f.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1c4d51a5398a028841cf3d7583d7a6cb 2500w" />
</Frame>

## Requirements

Chat Instead requires ASAPP Android Chat SDK 8.0.0 or later, and a valid phone number. Before you proceed, make sure you configure it [correctly](/messaging-platform/integrations/android-sdk).

## Phone Formats

Chat Instead accepts a wide variety of formats. See [tools.ietf.org/html/rfc3966](https://tools.ietf.org/html/rfc3966) for the precise definition. For example, it will accept: "+1 (555) 555-5555" and "555-555-5555".

## Getting Started

There are two ways to add Chat Instead. The easiest way is to add the `ASAPPChatInsteadButton` to the layout and call the `ASAPPChatInsteadButton.init`. Alternatively, you can manage the lifecycle yourself.

### 1. Add an ASAPPChatInsteadButton

You can add this button to any layout, like any other [AppCompatButton](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatButton).

```json  theme={null}
<com.asapp.chatsdk.views.ASAPPChatInsteadButton
    android:id="@+id/button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/button_chat_instead"
    />
```

After that, be sure to call the `ASAPPChatInsteadButton.init` method. Only the phone number is mandatory. Optionally, you can overwrite the `ASAPPChatInsteadButton.onChannel` and the `ASAPPChatInsteadButton.onError` properties of the button.

### 2. Manual Setup of ASAPPChatInstead

1. Initialize Chat Instead
   Somewhere after the `ASAPP.init` call:
   ```json  theme={null}
   val chatInstead = ASAPPChatInstead.create(phoneNumber)
   ```
   to initialize Chat Instead. Depending on cache, this will trigger a network call so channels are "immediately" available to the user once the fragment is displayed.
   Along with an optional header and a chat icon, you can pass callbacks to be notified when a channel is tapped or an error on a channel happens.
   ASAPP makes both callbacks after Chat Instead has tried to act on the tap.
2. Display Channels
   With the instance returned by `ASAPPChatInstead.init`, call `ASAPPChatInstead.show` whenever you want to display the [BottomSheetDialogFragment](https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialogFragment?hl=en). Depending on cache, this might show a loading state.
3. Clear Chat Instead (optional)
   You can interrupt the Chat Instead initial network call, if you call `ASAPPChatInstead.clear`. ASAPP advises you to add the call `onDestroy` for Activities and `onDetachedFromWindow` for Fragments.
   If you call `ASAPPChatInstead.clear` after you create the [BottomSheetDialogFragment](https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialogFragment?hl=en) view, it will have no effect.

## Error Handling and Debugging

In the case of problems, look for logs with the "ASAPPChatInstead" tag. Be sure to call `ASAPP.setDebugLoggingEnabled(true)` to enable the logs.
Alternatively, you can set callbacks with `ASAPPChatInstead.init`.

### Troubleshoot Chat Instead Errors

#### Crash Caused by UnsupportedOperationException when Displaying the Fragment

This occurs whenever `asapp_primary` is not defined in the style used by the calling Activity. Please refer to **Customization > Colors**.

#### "Unknown Channel" in the Log or the onError Callback

Talk to your Implementation Manager at ASAPP. ASAPP's Backend sent a channel we don't know how to handle. You might need to upgrade the Android SDK version.

#### "Unknown Error" in the Log

Talk to your Implementation Manager at ASAPP. This might be a bug. Please attach logs and reproduction steps.

#### "Activity Context Not Found" in the Log

It means you are not sending the right context at `ASAPPChatInstead.show`.

## Tablet and Landscape Support

Chat Instead supports these configurations seamlessly.

## Customization

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=630132c05c04f33c84714367d4bd72e7" data-og-width="787" width="787" data-og-height="444" height="444" data-path="image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ff37463439149ff8a48ceadda22fdd0b 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=21ead88e20b2c3408a4010fdd1bdd2db 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=723951b7f9222a8a5336b12cc4c54a0e 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a499276136e948897ef97e8a7eb221a8 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2fcd3423e637c8cf0af23b03bf5cee32 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7c077e80-61e2-93a7-1d0f-240e32c91769.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8a4417148ddfff804d21a2dce53ed457 2500w" />
</Frame>

### Header

By default it will use the text in `R.string.asapp_chat_instead_default_header`. You can send a different string when initializing Chat Instead, but it's important to know the ASAPP Backend will overwrite it if the call is successful.

### Chat Icon

You can customize the SDK Chat channel icon. By default it will be tinted with `asapp_primary` and `asapp_on_primary`.

<Note>
  If you customize the icon, make sure to test how it looks in Night Mode (a.k.a. Dark Mode).
</Note>

### Colors

Chat Instead uses the ASAPP text styles and colors. For more information on how to customize, go to [Customization](../android-sdk/customization "Customization").

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=08f250e85d10a7979f7ef92c473a33fc" data-og-width="1247" width="1247" data-og-height="466" height="466" data-path="image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=fde51846e401412ed942f0370456a66a 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c4b26e6e792ae11db7c8efb2fd918334 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ea0bee984513d473ba1c7ae565a9b9e5 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9b26f8326af0d37c8fa2c8e8237521b8 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ab8a200fc995c06329b762e5ca7b5324 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-961a0a3b-ce7b-5e66-626b-9d8c94629478.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9c100435e6f5da981436544c6eb24d1f 2500w" />
</Frame>

## Remote settings

Chat Instead receives configuration information from ASAPP's Backend (BE), in addition to the channels to display. The configuration enables/disables the feature and selects the device type (mobile, tablet, none). Contact your Implementation Manager at ASAPP if you have any questions.

<Note>
  It's important to know how the BE affects customization. If you provide a header, the BE will overwrite it. On the other hand, the BE cannot overwrite the phone number.
</Note>

## Cache

Chat Instead will temporarily cache the displayed channels to provide a better user experience. The cache is warmed at instantiation. The information will persist through phone restarts. As usual, it won't survive an uninstall or a "clear cache" in App info.
