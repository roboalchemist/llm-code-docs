# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/customization.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/customization.md

# Customization

## Styling

The SDK uses color attributes defined in the ASAPP theme, as well as extra style configuration options set via the style configuration class.

### Themes

To customize the SDK theme, extend the default ASAPP theme in your `styles.xml` file:

```xml  theme={null}
<style name="ASAPPTheme.Chat">
   <item name="asapp_primary">@color/custom_asapp_primary</item>
</style>
```

<Note>
  You must define your color variants for day and night in the appropriate resource files, unless night mode is disabled in your application.
</Note>

ASAPP recommends starting by only customizing `asapp_primary` to be your brand's primary color, and adjusting other colors when necessary for accessibility. `asapp_primary` is used as the message bubble background in most buttons and other controls. The screenshot below shows the default theme (gray primary - center) and custom primary colors on the left and right.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1dcfef0ea19c78e0e4e1db0fc02d52e7" data-og-width="1760" width="1760" data-og-height="1040" height="1040" data-path="image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8463c425d3b8f1a39fab332b586ecbc8 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=4ca454f0ee5d3d4efabda0b8727a9dc5 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5f1f6336033c338eff294a550c1d2010 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b3a11b97a6355fe43cb067969c807484 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=efe61210c2e6471c001101439ea05dc0 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bc80c9b7-254f-61fd-8b21-9d9221c32d2e.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8a8600019e287a6bbf0648ea5783686a 2500w" />
</Frame>

There are two other colors you may consider customizing for accessibility or to achieve an exact match with your app's theme: `asapp_on_background` and `asapp_on_primary`. `asapp_on_background` is used by other elements that might appear in front of the background. `asapp_on_primary` is used for text and other elements that appear in front of the primary color.

### More Colors

Besides the colors used for [themes](#themes "Themes"), you can override specific colors in a number of categories: the toolbar, chat content, messages, and other elements. You can override all properties mentioned below in the `ASAPPTheme.Chat` style.

The status bar color is `asapp_status_bar` and toolbar colors are `asapp_toolbar` (background), `asapp_nav_button`, `asapp_nav_icon`, and `asapp_nav_text` (foreground).

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7da409cf58b97f9cc87fb04e621f81a6" data-og-width="704" width="704" data-og-height="276" height="276" data-path="image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=fb32ac94b3efcb2d91a7fb38a0a9f72f 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c78096f1308ef3656b69d8e066534d48 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5bad236fa79601f492d53d6761274035 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e8afea2e14279de92183076dee2dd9b9 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6b59f4c7cc1518730de3d4c04523153e 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-937231b0-dc0e-173c-2bef-603a6825a599.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=275a58ec3a02dec0caa2c7c2780a2a74 2500w" />
</Frame>

**General chat content colors**

* `asapp_background`
* `asapp_separator_color`
* `asapp_control_tint`
* `asapp_control_secondary`
* `asapp_control_background`
* `asapp_success`
* `asapp_warning`
* `asapp_failure`

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=185b903ac2b8ff060db512a12f2dd565" data-og-width="742" width="742" data-og-height="440" height="440" data-path="image/uuid-a857e313-e965-8a94-be01-52765205c61c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e9813b2497a3c4b26c059ba154b293c5 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f5bad2bf2d3cb7fb21fc667db042ce36 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=784e863c80f64de436acf7e3cfaa6110 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a511cf01ac45b9286b6b176018ac8e4a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d430d38fd87c0504010284360c7c12e9 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a857e313-e965-8a94-be01-52765205c61c.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d9ba5ca68a81032d40f3f3cfa257a1f4 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=486f4c6fb9b1e275231ef33fe2d479a1" data-og-width="560" width="560" data-og-height="368" height="368" data-path="image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6fe9007c14873cf3abc32b0f2c8ab250 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2f399b60f4580348ab1cdc5b04f8a1a5 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7fddb54cee78ede558e127e426c33b74 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a19d2193252dbbac1db95a6014411e17 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c5c8d509c87be071d2b1bb5dfc84437f 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2e85b80-0e60-e1ee-333c-51a766d98e20.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=772e74ec79f0b17085d171f163c6bc98 2500w" />
</Frame>

**Message colors**

* `asapp_messages_list_background`
* `asapp_chat_bubble_sent_text`
* `asapp_chat_bubble_sent_bg`
* `asapp_chat_bubble_reply_text`
* `asapp_chat_bubble_reply_bg`

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c8a7d5538e72fa97868c6adb65dc9007" data-og-width="742" width="742" data-og-height="503" height="503" data-path="image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3101bc5ab9ef1104ac88413c356a2300 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a52815588bf670bccd7e5afba482b58b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=202828e6952cc979e35dca2d55c98907 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e1eb8a223f6c8462545d3e3220a29bab 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=50ecd4627a23e06a19df41cda4e1cf5c 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c290271b-9669-616e-4e39-5054d68d2f17.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=da034a577b9726a02fe1b611ce70a792 2500w" />
</Frame>

### Text and Buttons

To customize fonts and colors for both text and buttons, use the `ASAPPCustomTextStyleHandler`. To set this optional handler use `ASAPPStyleConfig.setTextStyleHandler`. Use the given `ASAPPTextStyles`

object to:

* Set a new font family with `updateFonts`. If no new fonts are set, the system default will be used instead.
* Override font sizes, letter spacing, text colors, and text casing styles. You can also customize the font family for each text style individually, if needed.
* Override button colors for normal, highlighted and disabled states.

Example:

```kotlin  theme={null}
ASAPP.instance.getStyleConfig()
   .setTextStyleHandler { context, textStyles ->
       val regular = Typeface.createFromAsset(context.assets, "fonts/NH-Regular.ttf")
       val medium = Typeface.createFromAsset(context.assets, "fonts/Lato-Bold.ttf")
       val black = Typeface.createFromAsset(context.assets, "fonts/Lato-Black.ttf")
       textStyles.updateFonts(regular, medium, black)
       textStyles.body.fontSize = 14f
       val textHighlightColor = ContextCompat.getColor(context, R.color.my_text_hightlight_color)
       textStyles.primaryButton.textHighlighted = textHighlightColor
   }
```

See `ASAPPTextStyles` to see all overridable styles.

<Note>
  `setTextStyleHandler` is called when an ASAPP activity is created. Use the given `Context` object if you access resources to make sure that all customization uses correct resource qualifiers.

  For example: if a user is in chat and toggles Night Mode, the SDK automatically triggers an activity restart. Once the new activity is created, the SDK calls `setTextStyleHandler` with the new night/day context, which will retrieve the correct color variants from your styles.
</Note>

## Chat Header

The chat header (toolbar in the chat activity) has no content by default, but you can add text or icon using `ASAPPStyleConfig`.

### Text Title

To add text to the chat header, pass a String resource to `setChatActivityTitle`. By default, the title will be aligned to start. For example:

```kotlin  theme={null}
ASAPP.instance.getStyleConfig()
    .setChatActivityTitle(R.string.asapp_chat_title)
```

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c6d1abc5c59b6fc47912ea2598860d4b" data-og-width="704" width="704" data-og-height="162" height="162" data-path="image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=db55df42fe2ec548376eff8a625b9663 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=560e03a3f22d11f450ad8f87e9bf9c9c 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=97ac074c39cbf8b0dd15acaacc6469d8 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=809d0df975b291118bf4c812749ce3cb 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=471dce8b0fc8b2f658b2f4b11679f63b 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9d4fbc9-cc8a-9acf-070a-47b39d43905f.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1e2928842f027342cf1a99447c905559 2500w" />
</Frame>

### Drawable Title

To add an icon to the chat header use: `setChatActivityToolbarLogo`. You can also center the header content by calling `setIsToolbarTitleOrIconCentered(true)`. For example:

```kotlin  theme={null}
ASAPP.instance.getStyleConfig
    .setChatActivityToolbarLogo(R.drawable.asapp_chat_icon)
    .setIsToolbarTitleOrIconCentered(true)
```

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=81a08f13f56a5835e5b1237909d37242" data-og-width="704" width="704" data-og-height="162" height="162" data-path="image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c1f4115422d97e80e06f2cd6408c3efb 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=f83aba9d1477d32fb4d4122b3df981ad 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a65c9f59f7201b0710c353c6e45a7ad9 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8d32fe4ce96d00d8b08dc4ac9b2f2358 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e63d193479fdfc4d4aa077745510b6d0 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2f5e134a-27bf-81f4-9bf8-cd9c277e25d2.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ee2465bbbbb2af14f4f707aa1adbe00a 2500w" />
</Frame>

<Caution>
  Icons will have priority in the chat header. If you add both text and icon, only the icon will be used.
</Caution>

## Dark Mode

Android 10 (API 29) introduced Dark Mode (a.k.a night mode, dark theme), with a system UI toggle that allows users to switch between light and dark modes. ASAPP recommends reading the [developer documentation](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) for more information.

The ASAPP SDK theme defines default colors using the system resource "default" and "night" qualifiers, so chat will react to changes to the system night mode setting.

<Note>
  The ASAPP SDK does not automatically convert any color or image assets in Dark Mode, you must define night variants for each custom asset as described in [Android >Styling>Theming](#themes "Customization").
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7bd7f6f7608237aedbd9c021eda4c0bc" data-og-width="832" width="832" data-og-height="1071" height="1071" data-path="image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=4da340eef12387161f2b36d8bfcb8111 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2743c2c69dd74b5e2c94530007a23e9b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=aef667c2d1b96f593781eaab925451a9 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=69e3c07723df24656c0947d9e6743cba 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=6d32bd12f74142a1f64701042148899e 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b890e869-884e-07ad-b0d9-a564b0550f47.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c25cc971630bf9a63e34d9e1b0c70784 2500w" />
</Frame>

### Disable or Force a Dark Mode Setting

To disable Dark Mode, or to force Dark Mode for Android API levels below 29, ASAPP recommends using the [AppCompatDelegate.setDefaultNightMode](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setDefaultNightMode\(int\)) AndroidX API. This function changes the night mode setting throughout the entire application session, which also includes ASAPP SDK activities.

For example, it is possible to use Dark Mode on Android API 21 with the following:

```kotlin  theme={null}
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
```

## Atomic Customization

To customize the styles at an atomic level, you can use the `setAtomicViewStyleHandler` to update viewStyles. Customizing at the atomic level will **override any default style** that is being set on the UI views. Use it only if general styling is not sufficient, and you need further customization. This is optional, and in most cases, you won't need it. Use with caution.

```kotlin  theme={null}
ASAPP.instance.getStyleConfig()
    .setAtomicViewStyleHandler { context: Context, viewStyles: ASAPPCustomViewStyles ->
        // Update viewStyles as needed
    }
```

### Custom Theming Example

Following code snippet is an example of how to apply an atomic customized theme.

```kotlin  theme={null}
private fun setCustomStyling() {
        val orangeColor = "#ea7024"
        ASAPP.instance.getStyleConfig(reset = true)
            .setChatActivityToolbarLogo(0)
            .setChatActivityTitle(R.string.asapp_toolbar_custom_title)
            .setIsToolbarTitleOrIconCentered(true)
            .setAtomicViewStyleHandler { context: Context, viewStyles: ASAPPCustomViewStyles ->
                val iconWidthInDp = 24
                val iconWidthInPx = (context.resources.displayMetrics.density * iconWidthInDp).toInt()
                val customRegularTypeface = Typeface.createFromAsset(
                    context.assets,
                    "fonts/Lato-Regular.ttf"
                )
                val customMediumTypeface = Typeface.createFromAsset(
                    context.assets,
                    "fonts/Lato-Medium.ttf"
                )
                val customBoldTypeface = Typeface.createFromAsset(
                    context.assets,
                    "fonts/Lato-Bold.ttf"
                )

                with(viewStyles.connectionBar.success) {
                    container.backgroundColor = Color.GREEN
                    icon.src = R.drawable.nav_check_24px
                    primaryText.color = Color.RED
                    primaryText.typeface = customRegularTypeface
                    icon.src = R.drawable.nav_check_24px
                    icon.tintColor = ContextCompat.getColor(context, R.color.asapp_error_red)
                    icon.width = iconWidthInPx
                }
                with(viewStyles.connectionBar.warn) {
                    container.backgroundColor = Color.YELLOW
                    primaryText.color = Color.WHITE
                    primaryText.typeface = customMediumTypeface
                }
                with(viewStyles.connectionBar.error) {
                    container.backgroundColor = Color.RED
                    icon.src = R.drawable.asapp_img_icon_x
                    primaryText.fontSize = 18f
                    primaryText.typeface = customBoldTypeface
                    icon.tintColor = ContextCompat.getColor(context, R.color.asapp_error_red)
                }
                with(viewStyles.bottomSheetConfirmationDialog) {
                    confirmButtonBar.button.width = MATCH_PARENT
                    cancelButtonBar.button.width = MATCH_PARENT

                    confirmButtonBar.button.radius = Int.MAX_VALUE
                    cancelButtonBar.button.radius = Int.MAX_VALUE

                    confirmButtonBar.button.typeface = Typeface.DEFAULT_BOLD
                    confirmButtonBar.button.textNormal = Color.WHITE
                    confirmButtonBar.button.backgroundNormal = Color.DKGRAY

                    cancelButtonBar.button.typeface = Typeface.DEFAULT_BOLD
                    cancelButtonBar.button.textNormal = Color.DKGRAY
                    cancelButtonBar.button.backgroundNormal = Color.WHITE
                    cancelButtonBar.button.borderNormal = Color.DKGRAY
                }
                with(viewStyles.quickRepliesViewGroup) {
                    container.maxHeight = 600
                }
                viewStyles.titleBar = ASAPPCustomViewStyles.TitleBar.newInstance().apply {
                    primaryText.color = Color.DKGRAY
                    primaryText.fontSize = 14.0f
                    primaryText.typeface = Typeface.DEFAULT
                    icon.width = WRAP_CONTENT
                    actionBackButton.color = Color.parseColor(orangeColor)
                    actionMoreButton.color = Color.parseColor(orangeColor)
                }
                with(viewStyles.ewtBar) {
                    progressBar.visibility = View.VISIBLE
                    progressBar.progressColor = Color.parseColor("#eeeeee")
                    progressBar.backgroundColor = Color.parseColor(orangeColor)
                    btnLeave.textNormal = Color.parseColor("#006fd6")

                    txtEwtTitle.color = Color.DKGRAY
                    txtEwtTitle.fontSize = 16.0f
                    txtEwtValue.color = Color.DKGRAY
                    txtEwtValue.fontSize = 22.0f
                }
                with(viewStyles.chatComposerBar) {
                    btnSend.color = Color.parseColor(orangeColor)
                }
            }
    }
```

### Customization Details

Support for the following customizations are available:

#### Send Button Color

```kotlin  theme={null}
with(viewStyles.chatComposerBar) {
                    btnSend.color = Color.parseColor(orangeColor)
    }
```

#### TitleBar customizations

```kotlin  theme={null}
    viewStyles.titleBar = ASAPPCustomViewStyles.TitleBar.newInstance().apply {
        primaryText.color = Color.DKGRAY
        primaryText.fontSize = 14.0f
        primaryText.typeface = Typeface.DEFAULT
        icon.width = WRAP_CONTENT
        actionBackButton.color = Color.parseColor(orangeColor)
        actionMoreButton.color = Color.parseColor(orangeColor)
    }
```

#### Quick Reply Max Height

```kotlin  theme={null}
    with(viewStyles.quickRepliesViewGroup) {
        // Using Dp
        container.maxHeight = ASAPPStyleConfig.dpToPx(context, 600)
        // Or Using Pixel
        container.maxHeight = 600
    }
```

#### Estimated Wait Time (EWT) Bar Customization

```kotlin  theme={null}
    with(viewStyles.ewtBar) {
                    progressBar.visibility = View.GONE // Or VISIBLE
                    progressBar.progressColor = Color.parseColor("#eeeeee")
                    progressBar.backgroundColor = Color.parseColor(orangeColor)
                    btnLeave.textNormal = Color.parseColor("#006fd6")

                    txtEwtTitle.color = Color.DKGRAY
                    txtEwtTitle.fontSize = 16.0f
                    txtEwtValue.color = Color.DKGRAY
                    txtEwtValue.fontSize = 22.0f
    }
```

#### Connection Status Bar with customized Success/Warning/Error

```kotlin  theme={null}
    with(viewStyles.connectionBar.success) {
        container.backgroundColor = Color.GREEN
        icon.src = R.drawable.nav_check_24px
        primaryText.color = Color.RED
        primaryText.typeface = customRegularTypeface
        icon.src = R.drawable.nav_check_24px
        icon.tintColor = ContextCompat.getColor(context, R.color.asapp_error_red)
        icon.width = iconWidthInPx
    }
    with(viewStyles.connectionBar.warn) {
        container.backgroundColor = Color.YELLOW
        primaryText.color = Color.WHITE
        primaryText.typeface = customMediumTypeface
    }
    with(viewStyles.connectionBar.error) {
        container.backgroundColor = Color.RED
        icon.src = R.drawable.asapp_img_icon_x
        primaryText.fontSize = 18f
        primaryText.typeface = customBoldTypeface
        icon.tintColor = ContextCompat.getColor(context, R.color.asapp_error_red)
    }
```

#### Modal Button Styling Customization

```kotlin  theme={null}
    with(viewStyles.bottomSheetConfirmationDialog) {
        confirmButtonBar.button.width = MATCH_PARENT
        cancelButtonBar.button.width = MATCH_PARENT

        confirmButtonBar.button.radius = Int.MAX_VALUE
        cancelButtonBar.button.radius = Int.MAX_VALUE

        confirmButtonBar.button.typeface = Typeface.DEFAULT_BOLD
        confirmButtonBar.button.textNormal = Color.WHITE
        confirmButtonBar.button.backgroundNormal = Color.DKGRAY

        cancelButtonBar.button.typeface = Typeface.DEFAULT_BOLD
        cancelButtonBar.button.textNormal = Color.DKGRAY
        cancelButtonBar.button.backgroundNormal = Color.WHITE
        cancelButtonBar.button.borderNormal = Color.DKGRAY
    }
```
