# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/custom-settings/sdk-customization/ui-color-and-theme.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/custom-settings/sdk-customization/ui-color-and-theme.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/custom-settings/sdk-customization/ui-color-and-theme.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/sdk-customizations/ui-color-and-theme.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/sdk-customization/ui-color-and-theme.md

# UI Color & Theme

### SDK Themes

The SDK UI has two color themes: light and dark.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FmGIXcWZ2BWuvJ4Qhbny5%2Fimage.png?alt=media&#x26;token=b3203bac-93d8-4040-a788-c27a770de234" alt=""><figcaption></figcaption></figure>

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FHHjzn1eJ4xzf2Juo6xdu%2Fimage.png?alt=media&#x26;token=100b976a-0a32-434a-bab7-d77dfe01ced4" alt=""><figcaption></figcaption></figure>

You can set which theme to use with the following method.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setColorTheme(.dark)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setColorTheme:LCQColorThemeDark];
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Primary Color, Fonts, and Backgrounds

You can also further customize the SDK to match your brand’s design and identity by utilizing the API below. This API offers to set the color of UI elements that indicate interactivity, Font color, types and styles, background color, and call-to-action colors.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let theme = Theme()
theme.primaryColor = UIColor.yellow //  Color of UI elements that indicate interactivity (Links, or Call To Action)
theme.backgroundColor = UIColor.systemGray

theme.titleTextColor = UIColor.systemGreen
theme.subtitleTextColor = UIColor.systemCyan

theme.primaryTextColor = UIColor.systemBlue
theme.secondaryTextColor = UIColor.blue
theme.callToActionTextColor = UIColor.cyan

theme.headerBackgroundColor = UIColor.systemBrown
theme.footerBackgroundColor = UIColor.systemTeal
theme.rowBackgroundColor = UIColor.systemPink
theme.selectedRowBackgroundColor = UIColor.systemBrown

let menlo = UIFont(name: "menlo", size: 10)!
theme.primaryTextFont = menlo
theme.secondaryTextFont = menlo
theme.callToActionTextFont = menlo

theme.rowSeparatorColor = UIColor.systemGreen

Luciq.theme = theme
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQTheme *theme = [[LCQTheme alloc] init];
theme.primaryColor = UIColor.yellowColor; //  Color of UI elements that indicate interactivity (Links, or Call To Action)
theme.backgroundColor = UIColor.systemGrayColor;

theme.titleTextColor = UIColor.systemGreenColor;
theme.subtitleTextColor = UIColor.systemCyanColor;

theme.primaryTextColor = UIColor.systemBlueColor;
theme.secondaryTextColor = UIColor.blueColor;
theme.callToActionTextColor = UIColor.cyanColor;

theme.headerBackgroundColor = UIColor.systemBrownColor;
theme.footerBackgroundColor = UIColor.systemTealColor;
theme.rowBackgroundColor = UIColor.systemPinkColor;
theme.selectedRowBackgroundColor = UIColor.systemBrownColor;

UIFont *menlo = [UIFont fontWithName:@"menlo" size:10];
theme.primaryTextFont = menlo;
theme.secondaryTextFont = menlo;
theme.callToActionTextFont = menlo;

theme.rowSeparatorColor = UIColor.systemGreenColor;

Luciq.theme = theme;
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters Mapping

| Report Description                                                                                                    | Prompt Menu                                                                                                              | Visited Screens                                                                                                                  | Thank You Message                                                                                                                    | Chats List                                                                                                             | Chats Messages                                                                                                                 | Attachments                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| ![Report Description](https://files.readme.io/209efee7693ef807cefd578e8f52355e59a55a897513902907712c7f2524ffed-1.png) | ![Prompt Menu](https://files.readme.io/143e249189f30283f3bb86ef1d015c350dd547aa7e0880989a5ee117412a46a8-Prompt_Menu.png) | ![Visited Screens](https://files.readme.io/33e1410562fb7007a39f99e7d562ec27b576ce0c797addf718bd37ff8d07672b-Visited_Screens.png) | ![Thank You Message](https://files.readme.io/4b8b36830d5488307bc5b1de0865fe902f12fa785d15f3723818a2c818b5dba9-Thank_you_Message.png) | ![Chats List](https://files.readme.io/cebbaf341adb8baadfcb95a81c7cc4d03215cc79bf143f7d061cc7c0aa5ea8e8-Chats_List.png) | ![Chats Messages](https://files.readme.io/57246b82d6a59ad6a3cae026ece9ee2e44668ec90b41397251989961deaae125-Chats_Messages.png) | ![Attachments](https://files.readme.io/0da02d2953fd77b9b95f9604e3ae0c82cbf8f7b8e83069e05cb1a807d3e7bd33-Attachments.png) |

#### Floating Button Position

If your [invocation event](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-bug-reporting/showing-luciq) is a floating button, you can set its position in your app. The `CGRectMaxXEdge` will add the button to the right edge of the screen. The `CGRectMinXEdge` will add it to the left edge. The `TopOffset` specifies its position on the y-axis.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
BugReporting.floatingButtonEdge = .maxXEdge
BugReporting.floatingButtonTopOffset = 48
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQBugReporting.floatingButtonEdge = CGRectMaxXEdge;
LCQBugReporting.floatingButtonTopOffset = 48;
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Video Recording Button Position

If you've enabled video recordings as attachments, you can change the position of the red recording button displayed in the screenshot below. The default position of the button is **bottom right**.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FZETbVquIObJXkSd9ASaQ%2Fimage.png?alt=media&#x26;token=0b060654-6ded-4776-b92b-de9e4c9cd5ab" alt=""><figcaption><p><br><em>An example of the video recording button placed in the bottom right of an app.</em></p></figcaption></figure>

Use this method below to set the position of the video recording button.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
BugReporting.videoRecordingFloatingButtonPosition = .topLeft
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQBugReporting.videoRecordingFloatingButtonPosition = LCQPositionTopLeft;
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are the possible values:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
.topLeft
.topRight
.bottomLeft
.bottomRight
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQPositionTopLeft
LCQPositionTopRight
LCQPositionBottomLeft
LCQPositionBottomRight
```

{% endcode %}
{% endtab %}
{% endtabs %}
