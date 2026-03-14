# Source: https://virustotal.readme.io/docs/mandiant-connector.md

# Mandiant Advantage - Threat Intelligence

Mandiant connector guide for VirusTotal

This guide provides instructions on how to activate the Mandiant connector within VirusTotal. Once activated, VirusTotal reports will display threat intelligence information about IoCs (Indicators of Compromise) sourced from the Mandiant Advantage platform.

### Getting the Mandiant credentials

To use this connector, you must have access to the [Mandiant Advantage - Threat Intelligence](https://advantage.mandiant.com/) platform. You will need the following credentials provided by Mandiant:

* Key ID
* Secret ID

You can locate these credentials in the Mandiant Advantage - Threat Intelligence platform by following these steps:

1. Navigate to the Settings tab.
2. Scroll down to the APIv4 Access and Key section.
3. Copy the provided credentials.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/mandiant-get-creds_20231004.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Adding the connector

Before you can view Mandiant's threat intelligence information in VirusTotal reports, you must set up the Mandiant connector and provide your credentials. Follow these steps:

1. Access the `Technology Integrations` page via the left menu and then click on the `Connectors (Third party to VT)`. This page serves as the hub for all your configured connectors.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/all-empty_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Here you can perform different actions described in details in the `Manage the connector` section.

2. Click on `Add a connector`. A dialog will guide you through configuring the connector in two straightforward steps.

3. Select the Mandiant connector.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/mandiant-step1_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

4. Provide a name and the authentication details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/mandiant-step2_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

5. Save the connector.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/mandiant-done_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Once completed, all members of your group will have access to Mandiant information in the IoC reports.

### Managing the connector

The user who adds the connector and the admins of the group to which it belongs, has the authority to edit or delete the connector.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/all-contextual-menu_20231004.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Additionally, all users within your group can enable or disable the connector, this action affects individually to the user.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/all-enable_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Viewing Mandiant Information

Once the Mandiant connector is configured, all members of your group will start seeing additional context in the reports. Here are some examples to explore:

* [3891a99f05bb166044e7ec11ed04f651bf2a0c48a76691258546b8dbc5620c58](https://www.virustotal.com/gui/file/3891a99f05bb166044e7ec11ed04f651bf2a0c48a76691258546b8dbc5620c58)
* [77e82c3d5fea369f6598339dcd97b73f670ff0ad373bf7fc3a2d8586f58d9d32](https://www.virustotal.com/gui/file/77e82c3d5fea369f6598339dcd97b73f670ff0ad373bf7fc3a2d8586f58d9d32)
* [mobile-sessionid.customize-identity.info](https://www.virustotal.com/gui/domain/mobile-sessionid.customize-identity.info)

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/mandiant-report_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

For each IoC, you will receive, at a minimum, the Mandiant IC Score. Additionally, Mandiant may provide information about Malware Families or Threat Actors related to the IoC, which will be displayed as clickable tags that allow you to pivot to the Mandiant platform for more details.

### Support

This connector is officially suported by VirusTotal, please [contact us](https://www.virustotal.com/gui/contact-us/technical-support) if you have any question.