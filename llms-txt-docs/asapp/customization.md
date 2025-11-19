# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/messaging-platform/integrations/android-sdk/customization.md

# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/customization.md

# Customization

## Styling

### Themes

There is one main color that you can set to ensure the ASAPP chat view controller fits with your app's theme: `ASAPP.styles.colors.primary`.

ASAPP recommends starting out only setting `.primary` to be your brand's primary color, and adjusting other colors when necessary for accessibility.

`.primary` is used as the message bubble background and in most buttons and other controls.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=25d6637df526646b7d4f8a74b9a465b0" alt="Themes" data-og-width="1960" width="1960" data-og-height="1156" height="1156" data-path="image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a01affe38440cc25bcf2aeb0d186c3de 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0c2f21df29cdee0f7090a2f089aa1cfa 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=777989bbd90af2e86b7cfde3f19fefb1 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=79b9645a07b49bf2ef88d46059519a34 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9e504a14afb2e0b8dd63df98c7308ec1 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9d0baf87-860b-2383-b391-bdf5bac8d426.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=eff1b5c5ff1ef76e232dd6f8c8a970c2 2500w" />
</Frame>

There are two other colors you may consider customizing for accessibility or to achieve an exact match with your app's theme: `ASAPP.styles.colors.onBackground` and `.onPrimary`. `.onBackground` is used for most other elements that might appear in front of the background. `.onPrimary` is used for text and other elements that appear in front of the primary color.

### Fonts

The ASAPP SDK uses the iOS system font family, SF Pro, by default. To use another font family, pass an `ASAPPFontFamily` to `ASAPP.styles.textStyles.updateStyles(for:)`. There are two `ASAPPFontFamily` initializers: one that takes font file names and another that takes `UIFont` references.

```json  theme={null}
let avenirNext = ASAPPFontFamily(
    lightFontName: “AvenirNext-Regular”,
    regularFontName: “AvenirNext-Medium”,
    mediumFontName: “AvenirNext-DemiBold”,
    boldFontName: “AvenirNext-Bold”)!
ASAPP.styles.textStyles.updateStyles(for: avenirNext)
```

## Overrides

The ASAPP SDK API allows you to override many aspects of the design of the chat interface, including [colors](#colors "Colors"), [button styles](#buttons "Buttons"), [navigation bar styles](#navigation-bar-styles "Navigation Bar Styles"), and various [text styles](#text-styles "Text Styles").

### Colors

Besides the colors used for themes, you can override specific colors in a number of categories:

* Navigation bar
* General chat content
* Buttons
* Messages
* Quick replies
* Input field.

All property names mentioned below are under `ASAPP.styles.colors`.

Navigation bar colors are .`navBarBackground`, `.navBarTitle`, `.navBarButton`, and `.navBarButtonActive`.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5539fa4baba7117851f1451e485c788c" alt="Navigation Bar Colors" data-og-width="660" width="660" data-og-height="308" height="308" data-path="image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7a70a863a52b9f2da0f90bb396b31635 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1f1675a0945660271fa0a65fe60865ff 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=071aa400370c4f80a389207351cac46d 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8f2175223a4313dfe97383f1836ad3f4 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7909c36ee4fe933adedc238f9ea4e8a5 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-639758e9-7260-7b8b-e6e9-9cd67b1c4da7.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=b0e4b8082d8c84c2b56f3997402340b2 2500w" />
</Frame>

General chat content colors are `.background`, `.separatorPrimary`, `.separatorSecondary`, `.controlTint`, `.controlSecondary`, `.controlBackground`, `.success`, `.warning`, and `.failure`.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d71ae49214be48245629c5b3208cdaeb" alt="General Chat Content Colors" data-og-width="660" width="660" data-og-height="500" height="500" data-path="image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=3734a1188c9dae119ac5be0fded7b9f8 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=40e259981547c50c74f42d7659f41fae 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=086f217eb5432567b2306bb662f651b1 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d3f48855907f4caa25ab590e1acd0241 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2a31be4883464dbcf9b5d9935f235716 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-78754833-105d-5aad-0c69-ca3fa2bb6043.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4827e86545ba3eb337c23e919b3699c5 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=fd2f8c64caec3459bafdb95802099130" alt="General Chat Content Colors" data-og-width="660" width="660" data-og-height="600" height="600" data-path="image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=43867e4b2e6a7c37bdb1f7f26c4570b3 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9f2f8e6fdb660a588b274752ca8de81c 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=94959c7c57801aaa493f7e4521b422f3 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=38d525063e4707df9e3d8a4ca0194962 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=61dc8ebe0e55fff4fa9822c76d9b9a2f 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a57aa919-bbe4-4282-e384-a044374ce33d.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0f06e6a8eeab8276d6c71b050004bc11 2500w" />
</Frame>

Buttons use sets of colors defined with an `ASAPPButtonColors` initializer. You can override `.textButtonPrimary`, `.buttonPrimary`, and `.buttonSecondary`.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0cb38af7a5db3e9814b45e6fb32cc21f" alt="Buttons" data-og-width="580" width="580" data-og-height="361" height="361" data-path="image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e7d9fed7d8b8cc24ce8677819040af14 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=eb5c976f42e2ed1dc2ba3db3f804e2ef 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d4d4faf714ecce454df1ab8c79ce8839 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=bef4181b09bf263a9d7cda14f8da88db 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5ac3633ce957c1e6bc7da634bf4a5e8e 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-93c9f7d7-4d6c-e37c-1816-883e33edce1f.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=04f3cc3c8af81a0e20cdf826c9d9ae9c 2500w" />
</Frame>

Message colors are `.messagesListBackground`, `.messageText`, `.messageBackground`, `.messageBorder`, `.replyMessageText`, `.replyMessageBackground`, and `.replyMessageBorder`.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2d64c2a540dbccdb26bcddc76d512d4d" alt="Message Colors" data-og-width="660" width="660" data-og-height="600" height="600" data-path="image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=10aa7ec1f522c7af87b0e1cf4fbcd465 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fb8662038cc7a47df9addaa66f3b7cdd 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fdf23b64f5d3850f95f326bd5457ac87 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=eff409589597af4f6b62a9ba90e84382 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a718ad346ed62af427ccaec9e1d9509d 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3ba6e44f-0d6a-4e78-df3f-9bf866f4c692.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a0a127911f7bcf58e8e7b37962977259 2500w" />
</Frame>

Quick replies and action buttons also use `ASAPPButtonColors`. You can override `.quickReplyButton` and `.actionButton`.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=14e13d7271e0152a1d489cf7a45eecc6" alt="Quick Replies and Action Buttons" data-og-width="660" width="660" data-og-height="405" height="405" data-path="image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e687dff5aeac756b2dc6c07d5d6d0f6a 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=cc1e0be33beeb6c8fd4096588e14602f 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b4fd666caa7ac6582b092747b8f8eb18 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=12028ca6bb432c6d56c7d4363c6f5e4a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7ec6565205c0858921b64009dfee746c 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b2a23eeb-86b6-0032-f726-a9220f8b0291.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b74ee17350d0a1656b23c2417fc8dc4b 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c9fcd1dbf4ac41ee522935e50bd7bdf9" alt="Quick Replies and Action Buttons" data-og-width="660" width="660" data-og-height="700" height="700" data-path="image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=22754bae100ababfbb3e22826c9a57b1 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2a1580f57f42ca3f8fecbe0c5c88f5d0 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=fdade4df69328ef021f85ed8ee348a8c 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d34492b4ef30f279f0ad707603902856 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1ef4b8d3ac6763c80f9f869c0df02ea0 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6b969a64-d5bc-0067-4f7f-2b160a493f68.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=222776cfc3503b28712610e94e920519 2500w" />
</Frame>

The chat input field uses `ASAPPInputColors`. You can override `.chatInput`.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7236f959abb22e4634e209b80b1f39b0" alt="Chat Input Field" data-og-width="660" width="660" data-og-height="310" height="310" data-path="image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=10beb1760d871bfde1d59fdc375a727b 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2af4e9cdc5c5e223027615381a3800f7 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=89d51aa3092c713539461dd91bf38178 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8c82cfd2dd1387bc2a71349300cf43ce 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=52523d90faf0eac52da6377cf4599ec1 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bf5cc2e4-5f01-607e-a718-9b640bb8d519.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5d87ef8f33c4485f344406f5a745a1c3 2500w" />
</Frame>

### Text Styles

ASAPP strongly recommends that you use one font family as described in the [Fonts](#fonts) section. However, if you need to, you may override: `ASAPP.styles.textStyles.navButton`, `.button`, `.actionButton`, `.link`, `.header1`, `.header2`, `.header3`, `.subheader`, `.body`, `.bodyBold`, `.body2`, `.bodyBold2`, `.detail1`, `.detail2`, and `.error`. To update all but the first four with a color, call `ASAPP.styles.textStyles.updateColors(with:)`.

### Navigation Bar Styles

You can override the default `ASAPP.styles.navBarStyles.titlePadding` using `UIEdgeInsets`.

### Buttons

The shape of primary buttons in message attachments, forms, and other dynamic layouts is determined by the value of `ASAPP.styles.primaryButtonRoundingStyle`. The default value is `.radius(0)`. You can set it to a custom radius with `.radius(_:)` or fully rounded with `.pill`.

## Images

### Navigation Bar

There are three images used in the chat view controller's navigation bar that are overridable: the icons for the **close ✕**, **back ⟨**, and **more ⋮** buttons. Each is tinted appropriately, so the image need only be a template in black with an alpha channel. ASAPP displays only one of the **close** and **back** buttons at a time; the former is used when the chat view controller is presented modally, and the latter when pushed onto a navigation stack.

```json  theme={null}
ASAPP.styles.navBarStyles.buttonImages.close
ASAPP.styles.navBarStyles.buttonImages.back
ASAPP.styles.navBarStyles.buttonImages.more
```

Use the `ASAPPCustomImage(image:size:insets:)` initializer to override each:

```json  theme={null}
ASAPP.styles.navBarStyles.buttonImages.more = ASAPPCustomImage(
    image: UIImage(named: “Your More Icon Name”)!,
     size: CGSize(width: 20, height: 20),
     insets: UIEdgeInsets(top: 14, left: 0, bottom: 14, right: 0))
```

### Title View

To use a custom title view, assign `ASAPP.views.chatTitle`. If you set a custom title view, it will override any string you set as `ASAPP.strings.chatTitle`. The title view will be rendered in the center of the navigation bar.

## Quick Reply View Height

To set quick reply view height, assign value to 'maxQuickReplyViewHeight' variable which is part of the class 'ASAPPCustomViewStyles'. We have added a safe height value calculation based on the value provided to 'maxQuickReplyViewHeight' and the quick replies contents data. We should not allow any random higher value to maxQuickReplyViewHeight. The quickReplies height view should not increase to the middle of the iPhone as the chat conversation list view contents visibility will be reduced. Hence we have added a safe height value calculation logic to avoid such UI issues. You can try different values like 180, 240, 300 etc to check the UI. You can set the preferred tint color to 'titleBar.actionBackButton'

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.maxQuickReplyViewHeight = 300
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
     tintColorNormal: UIColor.orange
)
ASAPP.views.customViewStyle = customViewStyle
```

## Banner Theme

To set customised theme to sucess, warning and failure banners.

```json  theme={null}
func setBannerTheme() {
    let customViewStyle = ASAPPCustomViewStyles()
    let successImageObj = UIImage(named: "PlusIcon")
    let warningImageObj = UIImage(named: "PlusIcon")
    let successFontInfo = UIFont(name: "BrutalType-Light", size: 14)!
    let failureFontInfo = UIFont(name: "BrutalType-Black", size: 14)!
    //Success
    customViewStyle.connectionBar.success = ConnectionBar(
        container: OptionalViewTypeConfig(
            backgroundColor: FeedbackType.error.getBackgroundColor()
        ), primaryText: OptionalTextTypeConfig(
            typeface: failureFontInfo,
            letterSpacing: 0,
            color: .white
        ), icon: OptionalImageViewTypeConfig(width: 22, height: 22, src: warningImageObj)
    )
    
    //Warning
    customViewStyle.connectionBar.warn = ConnectionBar(
        container: OptionalViewTypeConfig(
            backgroundColor: FeedbackType.warning.getBackgroundColor()
        ), primaryText: OptionalTextTypeConfig(
            typeface: UIFont.systemFont(ofSize: 14),
            letterSpacing: 0,
            color: .black
        ), icon: OptionalImageViewTypeConfig(width: 22, height: 22, src: warningImageObj
        )
    )
    
    //Error
    customViewStyle.connectionBar.error = ConnectionBar(
        container: OptionalViewTypeConfig(
            backgroundColor: FeedbackType.error.getBackgroundColor()
        ), primaryText: OptionalTextTypeConfig(
            typeface: failureFontInfo,
            letterSpacing: 0,
            color: .white
        ), icon: OptionalImageViewTypeConfig(width: 22, height: 22, src: warningImageObj)
    )
    
    customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
        tintColorNormal: UIColor.orange
    )
    ASAPP.views.customViewStyle = customViewStyle
}
```

## Modal Button Styling

To set the bottom sheet alert button title, body text UI, confirmation and cancel buttons UI

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.blue
)
customViewStyle.bottomSheetConfirmationDialog.title = OptionalTextTypeConfig(typeface: UIFont.systemFont(ofSize: 16, weight: .bold), color: UIColor.black)
customViewStyle.bottomSheetConfirmationDialog.bodyText = OptionalTextTypeConfig(typeface: UIFont.systemFont(ofSize: 14, weight: .regular), color: UIColor.red)
customViewStyle.bottomSheetConfirmationDialog.confirmButtonBar.button = OptionalButtonTypeConfig(width: ButtonWidthType.matchParent.rawValue, margin: 40)
customViewStyle.bottomSheetConfirmationDialog.cancelButtonBar.button = OptionalButtonTypeConfig(width: ButtonWidthType.matchParent.rawValue, margin: 40)

ASAPP.views.customViewStyle = customViewStyle
```

## Leave Button Text And Progress Bar

To set the leave button, your position text UI and progress bar UI.

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.orange
)
customViewStyle.ewtBar.progressBar = OptionalProgressBarTypeConfig(isVisible: true, backgroundColor: UIColor.red, progressColor: UIColor.lightGray)
customViewStyle.ewtBar.btnLeave = OptionalButtonTypeConfig(typeface: UIFont.systemFont(ofSize: 18.0, weight: .regular), textColorNormal: UIColor.red)
customViewStyle.ewtBar.txtEwtTitle = OptionalTextTypeConfig(typeface: UIFont.systemFont(ofSize: 16), color: UIColor.darkGray)
customViewStyle.ewtBar.txtEwtValue = OptionalTextTypeConfig(typeface: UIFont.systemFont(ofSize: 22.0), color: UIColor.darkGray)
ASAPP.views.customViewStyle = customViewStyle
```

## New Question Text Style

To set custom UI for New Question text font, text color and highlighted color etc.

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.orange
)
customViewStyle.restartButtonBar.primaryText = OptionalButtonTypeConfig(typeface: UIFont.systemFont(ofSize: 18), textColorNormal: UIColor.darkGray, textColorHighlighted: UIColor.green)
customViewStyle.restartButtonBar.icon = OptionalImageViewTypeConfig(src: UIImage(named: "PlusIcon"), tintColor: UIColor.orange)

ASAPP.views.customViewStyle = customViewStyle
```

## Send Button Theme

To set custom UI for chat text Send button theme

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.purple
)
customViewStyle.chatComposerBar.btnSend = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.purple
)
ASAPP.views.customViewStyle = customViewStyle
```

## Title Bar Theme

To set custom back button, title bar icon, title bar More button themes.

```json  theme={null}
let customViewStyle = ASAPPCustomViewStyles()
customViewStyle.titleBar.actionBackButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.systemPink
)
customViewStyle.titleBar.actionMoreButton = OptionalButtonTypeConfig(
    tintColorNormal: UIColor.systemPink
)
let warningImageObj = UIImage(named: "PlusIcon")
customViewStyle.titleBar.primaryText = OptionalTextTypeConfig(typeface: UIFont.systemFont(ofSize: 18, weight: .bold), color: UIColor.orange)
customViewStyle.titleBar.icon = OptionalImageViewTypeConfig(width: 16, height: 16, src: warningImageObj, tintColor: UIColor.systemPink)
ASAPP.views.customViewStyle = customViewStyle

let strings = ASAPPStrings()
strings.chatTitle = "Chat Test"
ASAPP.strings = strings
```

## Dark Mode

Apple introduced Dark Mode in iOS 13. Please see Apple's [Supporting Dark Mode in Your Interface](https://developer.apple.com/documentation/xcode/supporting_dark_mode_in_your_interface) documentation for an overview.

The ASAPP SDK does not automatically convert any colors for use in Dark Mode; you must define dark variants for each custom color at the app level, which the SDK will use automatically when the interface style changes.

ASAPP recommends that you add a Dark Appearance to colors you define in color sets in an asset catalog. Please see [Apple's documentation](https://developer.apple.com/documentation/xcode/supporting_dark_mode_in_your_interface#2993897) for more details. Once you have defined a color set, you can refer to it by name with the `UIColor(named:)` initializer, which was introduced in iOS 11. After you have defined a dark variant for at least the primary color, be sure to set it and flip the Dark Mode flag:

```json  theme={null}
ASAPP.styles.colors.primary = UIColor(named: "Your Primary Color Name")!
ASAPP.styles.isDarkModeAllowed = true
```

<Note>
  ASAPP highly recommends adding a Dark Appearance for any color you set. Please don't forget to define a Dark Appearance for your custom logo if you have set `ASAPP.views.chatTitle`.
</Note>

If your app does not support Dark Mode, ASAPP recommends that you do not change the value of `ASAPP.styles.isDarkModeAllowed` to ensure a consistent user experience.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ff0bba2c174329cfc81e3d8f1c19bfc4" alt="Dark Mode" data-og-width="1310" width="1310" data-og-height="1524" height="1524" data-path="image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=848f3566d85261e130c5dea870d3466a 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d42c3e1c26fa7ce5ac002f9467a538c1 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e0b71b200908a635816fb02fbc850def 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=3383e1493f8923ab9934da0cc180fce7 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=175e7427d6d678b39fe274ad1b376916 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-60f54608-b0ae-cfae-e5f1-8aeaa67fd66a.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=be55c8168c82172feec5f7d90711a679 2500w" />
</Frame>

## Orientation

The default value of `ASAPP.styles.allowedOrientations` is `.portraitLocked`, meaning the chat view controller will always render in portrait orientation. To allow landscape orientation on an iPad, set it to `.iPadLandscapeAllowed` instead. There is currently no landscape orientation option for iPhone.

## Strings

Please see the class reference for details on each member of `ASAPPStrings`.
