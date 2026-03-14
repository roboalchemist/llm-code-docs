# Source: https://virustotal.readme.io/docs/misp-connector.md

# MISP

MISP connector guide for VirusTotal

This guide provides instructions on how to activate the MISP connector within VirusTotal. Once activated, VirusTotal reports will display threat intelligence information about IoCs (Indicators of Compromise) sourced from the events found in your configured MISP instance.

### Prerequisites

Before you can begin the connector set up, ensure that you have the following prerequisites in place:

1. **Access to MISP**: You must have access to a running instance of MISP, either self-hosted or via a trusted organization.

2. **API Key**: Obtain an API key from your MISP instance. This key will be required for authentication during the integration setup.

### Getting the MISP API key

Follow these steps to get the MISP API key:

1. **Access to the MISP instance**: Log in to the MISP instance.

2. **Navigate to your user profile**: If you don't find it navigate directly to the url `/users/view/me`.

3. **Add a new auth key**: Under `Auth keys` click on the `+ Add authentication key`.

4. **Configure it**: Leave the `Allowed IPs` empty and mark the `Read only` checkbox.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/misp-get-creds_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Adding the connector

Before you can view MISP events information in VirusTotal reports, you must set up the MISP connector and provide your API key. Follow these steps:

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

2. Click on `Add a connector"`. A dialog will guide you through configuring the connector in two straightforward steps.

3. Select the MISP connector.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/misp-step1_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

4. Provide a name, the API key and the url of your MISP instance.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/misp-step2_20231005.png",
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

Once completed, all members of your group will have access to the MISP information in the IoC reports.

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

Once the MISP connector is configured, all members of your group will start seeing additional context in the reports.

For each IoC, you will receive, the MISP events ids and descriptions that contains the IoC, and the tags and the severity of each event.

### Support

This connector is officially suported by VirusTotal, please [contact us](https://www.virustotal.com/gui/contact-us/technical-support) if you have any question.