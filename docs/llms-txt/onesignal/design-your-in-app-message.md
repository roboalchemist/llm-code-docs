# Source: https://documentation.onesignal.com/docs/en/design-your-in-app-message.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Design in-app messages with drag-and-drop

> Use OneSignal's visual composer to build high-converting in-app messages with blocks, layouts, carousels, and personalization.

OneSignal's drag-and-drop editor lets you build in-app messages using modular blocks—no coding required. If you prefer markup, see [Design In-App Messages with HTML](./design-your-in-app-message-with-html).

<Frame caption="In-app message drag-and-drop editor">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/iam-block-create.gif?s=f3a6e2388fc6855a2fc8378fb5ce51b1" alt="Creating an in-app message using the drag-and-drop editor" width="780" height="589" data-path="images/iam/iam-block-create.gif" />
</Frame>

## Prerequisites

* You installed and initialized the OneSignal SDK in your app.
* You're on recommended SDKs for the latest editor features:
  * iOS 5.1.5+
  * Android 5.1.9+
* If not uploading images to OneSignal, then your images should be hosted on a fast, publicly accessible URL (CDN recommended) and sized appropriately for mobile screens.

<Warning>
  Make sure to use the latest version of the OneSignal SDK in your app.
  Older versions may still display the message, but with fallback styling (for example, default margins or default overlays). Use **Preview** and **device testing** to confirm behavior on your minimum supported SDK versions.
</Warning>

***

## Start from a pre-built template

Pre-built templates help you launch quickly with layouts that are designed for conversion (including permission prompts). Choose a template, then update the copy, colors, and actions to match your brand.

<Note>
  **Device testing:** Pre-built designs have been tested on Pixel 6+, iPhone (iOS 14+), Huawei Nova 9, Huawei P50 Foldable, and iPad (10th gen+). These templates are optimized for portrait orientation and may not display as intended in landscape mode.
</Note>

***

## Choose a message layout

Message layout controls how the in-app appears on screen.

| Message type | Best for                                       | How it behaves                                         |
| ------------ | ---------------------------------------------- | ------------------------------------------------------ |
| **Top**      | Slim announcements and confirmations           | Slides down from the top                               |
| **Center**   | Most marketing and product prompts             | Expands from the center and partially fills the screen |
| **Bottom**   | Snackbars, consent prompts                     | Slides up from the bottom                              |
| **Full**     | Onboarding flows, multi-step offers, carousels | Expands to fill the screen (with optional margins)     |

<Frame caption="In-app message layout types">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a675b8f-Type.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=e04ab2110fcd37eb6481db3dd8c63ece" alt="Top, Center, Bottom, and Full in-app message layouts" width="1115" height="788" data-path="images/docs/a675b8f-Type.png" />
</Frame>

### Build multi-screen flows with carousels

Carousels let you create multi-screen in-app experiences like onboarding, feature tours, or multi-step offers.

1. Select the **Full** message type.
2. Click **Create Carousel**.
3. Add up to 10 cards (screens).
4. Customize each card with any combination of blocks.

<Frame caption="Carousel example">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/carousel.gif?s=0ebac15f1b7b55229705970a84bda5be" alt="Example carousel with multiple in-app message cards" width="900" height="800" data-path="images/iam/carousel.gif" />
</Frame>

### Orientation support

In-app messages support portrait and landscape, but layouts (especially templates) may need adjustments to look great in both.

<Frame caption="Portrait and landscape in-app message examples">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e2b95e5-IAM-portrait-landscape.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=25028bc942075b84814ae5ee850bf458" alt="In-app message displayed in portrait and landscape orientations" width="1279" height="564" data-path="images/docs/e2b95e5-IAM-portrait-landscape.png" />
</Frame>

<Note> If you expect frequent landscape usage (tablets, games, video apps), test your message in landscape before publishing. Wide layouts often need smaller text sizes, tighter spacing, or fewer stacked blocks. </Note>

***

## Use blocks and spacing for clean layouts

Everything is placed on the Background block (your canvas). Use:

* **Padding** on the **Background** for space between your content and the message edges.
* **Margin** on individual blocks for space between elements (headline → image → button).

**Quick rules for consistent layouts**

1. Use **Padding** to control distance from the message edges.
2. Use **Margin** to separate blocks vertically.
3. Avoid stacking large padding and margins on the same side.
4. Prefer centered, flow-based layouts over tight/edge-aligned designs.
5. Always use **Preview** on multiple device sizes before publishing.

<Frame caption="Padding vs. margin in the editor">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/padding-margin.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=f328dfed369bb0369a825818cb264802" alt="Background padding and block margin controls in the in-app editor" width="1536" height="1024" data-path="images/iam/padding-margin.png" />
</Frame>

***

## Block reference

Use these blocks to build your message. Each block supports styling and (in most cases) an optional click action.

### Text block

Use for headlines, descriptions, disclaimers, or personalized copy.

**What you can customize**

* **Responsive sizing**: Width/height in percentages.
* **Fonts**: Google Fonts.
* **Formatting**: Bold, italic, underline.
* **Color**: Hex or RGBA (supports transparency).
* **Alignment**: Left, center, right.
* **Size**: Adjustable font size.

**Advanced**

* **Margins**: Space around the block.

**Tips**

* Localize with language-based segments or [using Liquid syntax](./using-liquid-syntax).
* Personalize with [data tags](./message-personalization).

<Frame caption="Text block">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a556236-Screenshot_2022-12-10_at_5.45.53_PM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=cec5db0519c7ec85ddce8bcc9e4b190f" alt="Text block configuration options in the editor" width="1004" height="836" data-path="images/docs/a556236-Screenshot_2022-12-10_at_5.45.53_PM.png" />
</Frame>

### Image block

Use images to reinforce the offer, show a feature, or add branding.

**Supported formats and limits**

* `.jpg`, `.png`, `.gif`
* Maximum file size: 5MB

**Tips & recommendations**

* Use common aspect ratios like `16:9`, `4:3`, or `3:2`.
* You can dynamically swap links and image URLs using server-hosted paths. See [Dynamic URLs](./links#dynamic-urls).
  * Example: `https://example.com/images/{{ tag_key }}.png`

**What you can customize**

* **Image URL**: Hosted is recommended for performance.
* **Click action**: Optional (link, deep link, tag, outcome, prompt).

**Advanced**

* **Dismiss on click**
* **Margins**: Space around the block.

<Frame caption="Image block">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0cc2179-Screenshot_2022-12-10_at_5.46.27_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=440933533b6d5985256b0ef45a5802a6" alt="Image block configuration options in the editor" width="1004" height="718" data-path="images/docs/0cc2179-Screenshot_2022-12-10_at_5.46.27_PM.png" />
</Frame>

<Warning> If an image URL is slow, blocked, or returns an error, your message can render with broken or empty media. Host images on a reliable CDN and verify they load quickly on mobile networks. </Warning>

### Button block

Use buttons for primary actions like navigation, collecting feedback, or permission prompts.

**What you can customize**

* Button text and font styling
* Background color, size, and corner radius
* Optional icon/image
* Click action (tagging, outcomes, prompts, deep links)

**Advanced**

* Dismiss on click
* Margins
* Borders and shadows

**Tips**

* Personalize button text or destinations using tags.
* You can make an image-only button by setting the background opacity to 0.
* Use subtle shadows (low opacity, higher blur) to lift the primary CTA.

<Frame caption="Button block settings">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/49beca3-Screenshot_2022-12-10_at_5.48.17_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=f3bce4770825e17bae48c4f5f7d8b385" alt="Button block configuration options in the editor" width="996" height="1578" data-path="images/docs/49beca3-Screenshot_2022-12-10_at_5.48.17_PM.png" />
</Frame>

### Close button block

The close button controls whether users can dismiss the message using an "X" icon.

**What you can customize**

* Enable/disable visibility
* Custom icon (`.jpg`, `.png`, `.svg`, `.gif`)
* Recommended size: `10x10px`
* Optional click action

**Advanced**

* Margins

<Warning>
  If you disable the close button, make sure users still have a clear way to exit (for example, a **dismiss action** on a button or background, or a close timer if your experience uses one). Otherwise, you risk trapping users in the message.
</Warning>

<Frame caption="Close button settings">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c07a30b-Screenshot_2022-12-10_at_5.49.22_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=acdcebb3ae4e83df14dab2d82753f2bf" alt="Close button configuration options in the editor" width="990" height="732" data-path="images/docs/c07a30b-Screenshot_2022-12-10_at_5.49.22_PM.png" />
</Frame>

### Background block

The background is the canvas that holds your layout.

**What you can customize**

* Background color (RGBA supported)
* Background image (`.jpg`, `.png`, `.gif`)
* Optional click action

**Advanced**

* Padding (default `24px`)
* Dismiss on click

<Frame caption="Background block settings">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9a441fd-Background_Controls.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=04a65877dc5e9818147ba15975cc5e92" alt="Background block controls for color, image, padding, and actions" width="1071" height="806" data-path="images/docs/9a441fd-Background_Controls.png" />
</Frame>

***

## Personalization & localization

You can personalize in-app messages using [data tags](./add-user-data-tags) including inside text, button labels, and URLs.

For localization, see [Multi-langauge messages](./multi-language-messaging#send-messages-in-different-languages).

<Check>
  A good personalization test is to send the message to a small internal segment with known tag values and confirm:

* The text and images render with the expected substitutions
* Links resolve correctly
* Buttons fire the expected click outcomes/tags
</Check>

***

## FAQ

### Can I remove the gray overlay or drop shadow from top/bottom banner in-apps?

Yes—update your SDKs and add the config below.

**iOS 5.1.5+**

```xml iOS Info.plist theme={null}
<key>OneSignal_in_app_message_hide_drop_shadow</key>
<true/>
<key>OneSignal_in_app_message_hide_gray_overlay</key>
<true/>
```

**Android 5.1.9+**

```xml Android Manifest.xml theme={null}
<meta-data android:name="com.onesignal.inAppMessageHideGrayOverlay" android:value="true"/>
<meta-data android:name="com.onesignal.inAppMessageHideDropShadow" android:value="true"/>
```

***

## Next steps

* Learn about [In-App Click Actions](./iam-click-actions) to customize what happens when users click elements in your message.
* Try different [In-App Message Triggers](./iam-triggers) to control when messages appear.
* Need more customization? Try [Design In-App Messages with HTML](./design-your-in-app-message-with-html).

***

Built with [Mintlify](https://mintlify.com).
