# Source: https://virustotal.readme.io/docs/splunk-connector.md

# Splunk

Splunk connector guide for VirusTotal

This guide provides instructions on how to activate the Splunk connector within VirusTotal. Once activated, VirusTotal reports will display threat intelligence information about IoCs (Indicators of Compromise) sourced from the events found in your Splunk instance.

### Prerequisites

Before you can begin the connector set up, ensure that you have the following prerequisites in place:

1. **Access to Splunk**: You must have access to a instance of Splunk, either Enterprise or Cloud.

2. **Access token**: Obtain a access token from your Splunk instance. This token will be required for authentication during the integration setup.

### Getting the Splunk access token

Follow these steps to get the Splunk access token:

1. **Access to the Splunk instance**

2. **Navigate to the Tokens page**: Open `Settings` top menu and click on `Tokens` under `USERS AND AUTHENTICATION` section.

3. **Enable Token Authentication**: Token authentication is disabled by default, enable it cliking on the button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-token1_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

4. **Create a new token**: Click on `New Token` and fill the \`Audience\`\` field, create and copy the token.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-token2_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Adding the connector

Before you can view Splunk events information in VirusTotal reports, you must set up the Splunk connector and provide your access token. Follow these steps:

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

3. Select the Splunk connector.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-step1_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

4. Provide a name, the access token, a list of Splunk sourcetypes to filter the events and the URL of your instance.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-step2_20231005.png",
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
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-done_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Once completed, all members of your group will have access to the Splunk events information in the IoC reports.

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

### Viewing Splunk Information

Once the Splunk connector is configured, all members of your group will start seeing additional context in the reports.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/integrations/connectors/__img__/splunk-report_20231005.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

For each IoC, you will receive some information related to the Splunk event, the date host, source and sourcetype.

### Support

This connector is officially suported by VirusTotal, please [contact us](https://www.virustotal.com/gui/contact-us/technical-support) if you have any question.