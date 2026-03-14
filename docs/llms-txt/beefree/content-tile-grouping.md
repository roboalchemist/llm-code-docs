# Source: https://docs.beefree.io/beefree-sdk/other-customizations/appearance/content-tile-grouping.md

# Content Tile Grouping

{% hint style="info" %}
This feature is available on Beefree SDK [Superpowers plan](https://developers.beefree.io/pricing-plans) and above. Upgrade a [development application](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications) at no extra charge to explore features from higher plan tiers. **Note:** Usage on a development application still counts toward [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) and limits.
{% endhint %}

## Grouping Content Tiles <a href="#grouping-content-tiles" id="grouping-content-tiles"></a>

The Content Tile Grouping option allows the host application to group content tiles in the editor’s sidebar. This allows the host application to display the content blocks into distinct groups.

Content Tile Grouping supports:

* Text labels
* Special Characters
* Emojis

{% hint style="info" %}
Please note that emoji support may be determined by the OS or browsers used. Some browsers do not support, or may display emojis incorrectly.
{% endhint %}

To display custom groups, the application must pass the groups settings in the configuration at initialization, like so:

```javascript

modulesGroups: [
  {
    label: "Text ✏️",
    collapsable: false,
    collapsedOnLoad: false,
    modulesNames: [
      "List",
      "Paragraph",
      "Heading"
    ]
  },
  {
    label: "Media",
    collapsable: true,
    collapsedOnLoad: false,
    modulesNames: [
      "Video",
      "Image"
    ]
  },
  {
    label: "AddOns",
    collapsable: true,
    collapsedOnLoad: true,
    modulesNames: [
      "Stickers",
      "Gifs"
    ]
  }
]

```

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FDlITQL5cZzK0wG4Xuvw5%2FScreenshot-2022-09-29-at-12.40.43.png?alt=media&#x26;token=8b5338ca-8d71-4f30-9376-09b8d2eeaad3" alt=""><figcaption></figcaption></figure>

Custom groups can be collapsed and opened by default by changing the `collapsable` and `collapsedOnLoad` values.\
Ungrouped tiles will be gathered at the bottom of the list under a group with no label.

Duplicated tiles are not allowed, e.g., you can’t have a tile twice in the sidebar.\
An `onWarning` notification is triggered whenever an unknown tile is added to the configuration.

## Full List of Content Tiles <a href="#full-list-of-content-tiles" id="full-list-of-content-tiles"></a>

```

1. Heading (Title)
2. Paragraph
3. List
4. Image
5. Button
6. Divider
7. Spacer
8. Social
9. DynamicContent
10. Html
11. Video
12. Form
13. Icons
14. Menu
15. Carousel
16. Text
17. ---- AddOns ----

```

If you want to organize or include AddOns, and Custom AddOns under a custom group, mention the name used in the Beefree SDK Console.

Please note, the AddOn needs to be enabled to appear in the sidebar.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FI6VvuNw3lwyCku71gKqS%2FCleanShot%202025-03-13%20at%2014.53.06.png?alt=media&#x26;token=941ae6e0-4bfc-443a-ae59-17782bbbb3c7" alt=""><figcaption></figcaption></figure>
