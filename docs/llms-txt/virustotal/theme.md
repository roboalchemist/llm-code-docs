# Source: https://virustotal.readme.io/reference/theme.md

# Theming

VT Augment can be themed to match your product/application's style.

The widget's theme is based on four HTML colours, two for backgrounds (bg1, bg2), one for primary typography (fg1) and the last one for borders, lines and icons.

The color should be passed as a query parameter with its RGB hex value without the hash symbol (i.e: ?bg1=fgfgfg\&bg2=ffffff). All colours are optional and you can pass whatever number of them. The style parameters should be passed to the initial [/widget/url](https://virustotal.readme.io/reference/widgeturl) call.

The default theme is:

* bg1: ffffff
* bg2: f9f9f9
* fg1: 4d4d4d
* bd1: e6e6e6

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/69a4e8d-theming.png",
        "theming.png",
        967,
        500,
        "#828694"
      ],
      "caption": "Theme colours in the widget"
    }
  ]
}
[/block]