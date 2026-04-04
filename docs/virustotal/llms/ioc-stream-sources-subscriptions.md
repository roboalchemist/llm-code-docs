# Source: https://virustotal.readme.io/docs/ioc-stream-sources-subscriptions.md

# Sources Subscriptions

The IOC Stream view is an evolution to the previous Livehunt Notifications view. This view allows users to digest the incoming VT flux into relevant threat feeds that you can study here or easily export to improve detection in your security technologies.

You can personalise your threat landscape by subscribing to collections and threat actors. All new IoCs tied to them will flow into your [IoC Stream view](https://www.virustotal.com/gui/ioc-notifications/files?order=date-).

You need to access to the [threat landscape](https://www.virustotal.com/gui/threat-landscape) view: 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_subscribethreatcards_202311021.png",
        null,
        "IOC Stream Subscribe Threat Cards"
      ],
      "align": "center"
     }
  ]
}
[/block]

To subscribe to collections, you need to select them, click on the Actions menu and then on Subscribe:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_subscribecollections_202311021.png",
        null,
        "IOC Stream Subscribe Collections"
      ],
      "align": "center"
     }
  ]
}
[/block]

You can do the same with Threat Actors:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_subscribethreatactors_202311021.png",
        null,
        "IOC Stream Subscribe Threat Actors"
      ],
      "align": "center"
    }
  ]
}
[/block]

You can also manage your sources in the [IoC notifications](https://www.virustotal.com/gui/ioc-notifications/files?order=date-) view:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_managesources_202311021.png",
        null,
        "IOC Stream Manage Sources"
      ],
      "align": "center"
    }
  ]
}
[/block]

In the manage sources view you have 3 different tabs: Collections, Threat actors and Hunting rulesets.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_managesourcesview_202311021.png",
        null,
        "IOC Stream"
      ],
      "align": "center"
    }
  ]
}
[/block]

In each of these tabs you can search by name or description, see the number of matches and unsubscribe any of the sources.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_managesourcesthreatactors_202311021.png",
        null,
        "IOC Stream"
      ],
      "align": "center"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/images/iocstream_managesourceshuntingrulesets_202311021.png",
        null,
        "IOC Stream"
      ],
      "align": "center"
    }
  ]
}
[/block]