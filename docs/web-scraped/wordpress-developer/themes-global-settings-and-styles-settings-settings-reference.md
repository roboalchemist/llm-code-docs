# Settings Reference

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/settings-reference/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/settings-reference/)

## In this article

Table of Contents- Appearance Tools

- Border
- Color
- Custom
- Dimensions
- Layout
- Lightbox
- Position
- Shadow
- Spacing
- Typography
- Use Root Padding Aware Alignments

↑Back to top

The document is a reference to the available settings properties that you can configure via thesettingsobject intheme.json. Each of the settings has an in-depth guide on how to use it within theSettings documentation.

## Appearance Tools

settings.appearanceToolsis a top-level property with no sub-properties nested beneath it. It is documented atSettings: Appearance Tools.

PropertyTypeDefault`appearanceTools`boolean`false`

## Border

settings.borderis an object that supports the nested properties listed in the below table. It is documented atSettings: Border.

PropertyTypeDefault`color`boolean`false``radius`boolean`false``style`boolean`false``width`boolean`false`
Enabling any one of thecolor,style, orwidthsettings will automatically enable the other two since the properties are linked together.

## Color

settings.coloris an object that supports the nested properties listed in the below table. It is documented atSettings: Color.

PropertyTypeDefaultProps`background`boolean`true`—`custom`boolean`true`—`customDuotone`boolean`true`—`customGradient`boolean`true`—`defaultDuotone`boolean`true`—`defaultGradients`boolean`true`—`defaultPalette`boolean`true`—`duotone`array <object>`array``colors`, `name`, `slug``gradients`array <object>`array``gradient`, `name`, `slug``link`boolean`false`—`palette`array <object>`array``color`, `name`, `slug``text`boolean`true`—

## Custom

settings.customis an object that supports any number of nested custom properties, as shown in the below table. It is documented atSettings: Custom.

PropertyTypeDefault`custom.<custom>`any—

## Dimensions

settings.dimensionsis an object that supports the nested properties listed in the below table. It is documented atSettings: Dimensions.

PropertyTypeDefault`minHeight`boolean`false`

## Layout

settings.layoutis an object that supports the nested properties listed in the below table. It is documented atSettings: Layout.

PropertyTypeDefault`contentSize`string`""``wideSize`string`""`

## Lightbox

settings.lightboxis an object that supports the nested properties listed in the below table. It is documented atSettings: Lightbox.

PropertyTypeDefault`allowEditing`boolean`true``enabled`boolean`false`
This setting is only available as of WordPress 6.4 and is specific to the core Image block (core/image).

## Position

settings.positionis an object that supports the nested properties listed in the below table. It is documented atSettings: Position.

PropertyTypeDefault`sticky`boolean`false`

## Shadow

settings.shadowis an object that supports the nested properties listed in the below table. It is documented atSettings: Shadow.

PropertyTypeDefaultProps`defaultPresets`boolean`true``presets`array <object>`array``name`, `shadow`, `slug`

## Spacing

settings.spacingis an object that supports the nested properties listed in the below table. It is documented atSettings: Spacing.

PropertyTypeDefaultProps`blockGap`boolean|null`null`—`customSpacingSize`boolean`true`—`margin`boolean`false`—`padding`boolean`false`—`spacingScale`object`object``operator`, `increment`, `steps`, `mediumStep`, `unit``spacingSizes`array <object>`array``name`, `size`, `slug``units`array <string>`[ "px", "em", "rem", "vh", "vw", "%" ]`—

## Typography

settings.typographyis an object that supports the nested properties listed in the below table. It is documented atSettings: Typography.

PropertyTypeDefaultProps`customFontSize`boolean`true`—`dropCap`boolean`true`—`fontFamilies`array <object>`array``fontFace`, `fontFamily`, `name`, `slug``fontSizes`array <object>`array``fluid`, `name`, `size`, `slug``fontStyle`boolean`true`—`fontWeight`boolean`true`—`fluid`boolean`false`—`letterSpacing`boolean`true`—`lineHeight`boolean`false`—`textColumns`boolean`false`—`textDecoration`boolean`true`—`textTransform`boolean`true`—`writingMode`boolean`false`—

## Use Root Padding Aware Alignments

settings.useRootPaddingAwareAlignmentsis a top-level property with no sub-properties nested beneath it. It is documented atSettings: Use Root Padding Aware Alignments.

PropertyTypeDefault`useRootPaddingAwareAlignments`boolean`false`
This setting works together withstyles.spacing.paddingintheme.json. If enabled,styles.spacing.paddingmust be an object that defines thetop,right,bottom, andleftstyles separately.

First published

October 17, 2023

Last updated

October 14, 2025

[PreviousUse Root Padding Aware AlignmentsPrevious: Use Root Padding Aware Alignments](https://developer.wordpress.org/themes/global-settings-and-styles/settings/use-root-padding-aware-alignments/)
[NextStylesNext: Styles](https://developer.wordpress.org/themes/global-settings-and-styles/styles/)
