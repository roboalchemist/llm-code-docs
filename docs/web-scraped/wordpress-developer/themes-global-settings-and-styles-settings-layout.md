# Layout

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/layout/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/layout/)

## In this article

Table of Contents- Layout settingsContent sizeWide Size

↑Back to top

Thesettings.layoutproperty intheme.jsonis an object that stores layout-related settings that you can configure. At the moment, it is used for setting “content” and “wide” widths, but it could also be used for other settings in the future.

In this document, you will learn what thelayoutproperty is used for and how you can use it in your theme.

## Layout settings

layoutis an object that’s nested directly within the top-levelsettingsproperty intheme.json. Within that object, you can define two settings:

- contentSize: A valid CSS length value for defining the default width for content. It is typically used for controlling the width of the post content and related areas on the page.
- wideSize:A valid CSS length value for defining the default wide alignment width, which is generally between the content size and full viewport width.

Take a look at thelayoutproperty in the context of atheme.jsonfile with its default values:

```json
{
    "version": 2,
    "settings": {
        "layout": {
            "contentSize": "",
            "wideSize": ""
        }
    }
}
```

### Content size

Thesettings.layout.contentSizeproperty is primarily useful for defining the width of a site’s content area. Think of this as the default width of your site. You can break outside of this by applying the “wide” (below) or “full” width to a block. The content width is merely the foundation.

In almost any design, you will want to limit this width to something that is comfortable to read, especially if the content is going to include text. This is a value that you will need to determine for yourself, but a good rule of thumb is that you should have 45-75 characters of text per line (though some guidelines differ slightly on the number range). Of course, your default font-family and font-size are crucial pieces to figuring this out.

Try configuring a content size in yourtheme.jsonfile:

```json
{
    "version": 2,
    "settings": {
        "layout": {
            "contentSize": "40rem"
        }
    }
}
```

If you open a template in theSite Editor, you can use it to define the layout for various blocks. In the screenshot below, you can see that the Post Content block has theInner blocks use content widthoption selected under theLayouttab:

What this setting does is tell WordPress that any nested blocks within the Post Content block should be set to the40remvalue defined forsettings.layout.contentSizeintheme.json.

### Wide Size

Thesettings.layout.wideSizeproperty defines a width for “wide” blocks. To be useful, wide blocks must be nested within a block that is telling WordPress that its inner blocks should be limited to the “content” size. Wide-aligned blocks are meant to “break outside” of their parent block.

Not every theme will benefit by having a wide size. Depending on the design, a theme’s layout may simply not have additional room for blocks to break out of their container. In those cases, you do not need to set this value.

For theme designs that can accommodate wide blocks (typical of sidebar-less designs), you will want to set this to a value that is greater thansettings.layout.contentWidth. But it shouldn’t stretch to the width of the full screen (e.g.,100vw). WordPress has a separate full-width setting that you can use for that.

Try adding a customsettings.layout.wideSizeto yourtheme.jsonfile (remember, you need a set content size for this to be useful):

```json
{
    "version": 2,
    "settings": {
        "layout": {
            "contentSize": "40rem",
            "wideSize": "64rem"
        }
    }
}
```

Now open yourSite Editorin the WordPress admin and edit a template. First, add aGroupblock with theInner blocks use content widthoption enabled. Then, stick another block within it and select theWide widthoption.

In the screenshot below, you can see the Post Featured Image block nested within a Group block. It breaks out of its parent container but the other post-related blocks are limited to the content width:

First published

October 17, 2023

[PreviousDimensionsPrevious: Dimensions](https://developer.wordpress.org/themes/global-settings-and-styles/settings/dimensions/)
[NextLightboxNext: Lightbox](https://developer.wordpress.org/themes/global-settings-and-styles/settings/lightbox/)
