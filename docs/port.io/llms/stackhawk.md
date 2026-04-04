# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/stackhawk.md

# StackHawk

In this example, you are going to create a webhook integration between [StackHawk](https://www.stackhawk.com/) and Port, which will ingest application vulnerabilities into Port. This integration will involve setting up a webhook to receive notifications from StackHawk whenever an application is scanned for vulnerabilities, allowing Port to ingest and process the vulnerability entities accordingly.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Create the following blueprint definitions and webhook configuration:

StackHawk vulnerability blueprint

Create in Port

```
{
  "identifier": "stackHawkVulnerability",
  "description": "This blueprint represents a StackHawk vulnerability in our software catalog",
  "title": "StackHawk Vulnerability",
  "icon": "StackHawk",
  "schema": {
    "properties": {
      "severity": {
        "type": "string",
        "title": "Severity",
        "description": "The criticality of the finding",
        "enum": ["Low", "Medium", "High"],
        "enumColors": {
          "Low": "green",
          "Medium": "yellow",
          "High": "red"
        }
      },
      "host": {
        "type": "string",
        "format": "url",
        "title": "Host",
        "description": "The web application host that was scanned"
      },
      "category": {
        "type": "string",
        "title": "Category",
        "description": "What vulnerability category this corresponds to"
      },
      "url": {
        "type": "string",
        "format": "url",
        "title": "Finding URL",
        "description": "Link to the StackHawk Platform for this finding's overview"
      },
      "totalCount": {
        "type": "number",
        "title": "Total Count",
        "description": "How many scanned paths correspond with this finding"
      },
      "tags": {
        "type": "array",
        "title": "Tags"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

StackHawk webhook configuration

Remember to update the `WEBHOOK_SECRET` and `AUTH_SIGNATURE_HEADER` with the real secret and header value you provided when subscribing to the webhook in StackHawk.

```
{
  "identifier": "stackHawkMapper",
  "title": "StackHawk Mapper",
  "description": "A webhook configuration to map StackHawk vulnerability to Port",
  "icon": "StackHawk",
  "mappings": [
    {
      "blueprint": "stackHawkVulnerability",
      "itemsToParse": ".body.scanCompleted.findings",
      "entity": {
        "identifier": ".body.scanCompleted.scan.application + \"-\" + .item.pluginId | gsub(\"[^a-zA-Z0-9@_.:\\/=-]\"; \"-\") | tostring",
        "title": ".item.pluginName",
        "properties": {
          "severity": ".item.severity",
          "host": ".item.host",
          "totalCount": ".item.totalCount",
          "category": ".item.category",
          "url": ".item.findingURL",
          "tags": ".body.scanCompleted.scan.tags"
        }
      }
    }
  ],
  "enabled": true,
  "security": {
    "secret": "WEBHOOK_SECRET",
    "signatureHeaderName": "AUTH_SIGNATURE_HEADER",
    "signatureAlgorithm": "plain",
    "signaturePrefix": ""
  }
}
```

### Create the StackHawk webhook[â](#create-the-stackhawk-webhook "Direct link to Create the StackHawk webhook")

1. Go to [StackHawk](https://app.stackhawk.com) and select the account you want to configure the webhook for.

2. Navigate to **Integrations** in the left navigation bar and click on **Generic Webhook**.

3. Click on **Add Webhook** and provide the following information:

   <!-- -->

   1. `Name` - enter a name for your webhook.
   2. `Description` - provide a detailed description for your webhook.
   3. `Scan Data For` - choose the application(s) you want to receive webhook events for or choose `Select All` if you want to configure a global webhook for all your applications.
   4. `Scan Events` - choose `Scan Completed` event type.
   5. `Webhook Endpoint URL` - enter the value of the `url` key you received after [creating the webhook configuration](/build-your-software-catalog/custom-integration/webhook/.md#configuring-webhook-endpoints).
   6. `Auth Header Name` - enter the name of the HTTP header that will contain your auth token/key. For example, you can enter `x-stackhawk-port-webhook`.
   7. `Auth Header Value` - enter the secret authentication token that will be added to your webhook payload.

4. Click **Create and Test** to create your webhook.

tip

In order to view the different events available in StackHawk webhooks, [look here](https://docs.stackhawk.com/workflow-integrations/webhook.html)

Done! Any changes that happen to your applications in StackHawk will trigger a webhook event to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Test the webhook[â](#test-the-webhook "Direct link to Test the webhook")

This section includes a sample webhook event sent from StackHawk when an application is scanned. In addition, it also includes the entity created from the event based on the webhook configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure sent to the webhook URL when an application is scanned:

Webhook event payload

```
{
  "service": "StackHawk",
  "scanCompleted": {
    "scan": {
      "id": "c30e848d-35a7-4357-a113-35ce3392e967",
      "hawkscanVersion": "3.1.0",
      "env": "Development",
      "status": "COMPLETED",
      "application": "Python App",
      "startedTimestamp": "2023-06-23T11:01:18.273Z",
      "scanURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967",
      "tags": ["test-application"]
    },
    "scanDuration": "72",
    "spiderDuration": "49",
    "completedScanStats": {
      "urlsCount": "2",
      "duration": "121",
      "scanResultsStats": {
        "totalCount": "5",
        "lowCount": "7",
        "mediumCount": "4",
        "highCount": "0",
        "lowTriagedCount": "0",
        "mediumTriagedCount": "0",
        "highTriagedCount": "0"
      }
    },
    "findings": [
      {
        "pluginId": "10021",
        "pluginName": "X-Content-Type-Options Header Missing",
        "severity": "Low",
        "host": "https://example.com",
        "paths": [
          {
            "path": "",
            "method": "GET",
            "status": "NEW",
            "pathURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10021/path/769898/message/4"
          }
        ],
        "pathStats": [
          {
            "status": "NEW",
            "count": 1
          }
        ],
        "totalCount": "1",
        "category": "Information Leakage",
        "findingURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10021"
      },
      {
        "pluginId": "10035",
        "pluginName": "Strict-Transport-Security Header Not Set",
        "severity": "Low",
        "host": "https://example.com",
        "paths": [
          {
            "path": "/robots.txt",
            "method": "GET",
            "status": "NEW",
            "pathURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10035/path/769897/message/7"
          },
          {
            "path": "/sitemap.xml",
            "method": "GET",
            "status": "NEW",
            "pathURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10035/path/769896/message/6"
          },
          {
            "path": "",
            "method": "GET",
            "status": "NEW",
            "pathURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10035/path/769898/message/4"
          }
        ],
        "pathStats": [
          {
            "status": "NEW",
            "count": 3
          }
        ],
        "totalCount": "3",
        "category": "Information Leakage",
        "findingURL": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10035"
      }
    ]
  }
}
```

### Mapping result[â](#mapping-result "Direct link to Mapping result")

The combination of the sample payload and the webhook configuration generates the following Port entities (in the sample above, multiple entities will be generated because the `findings` array contains multiple objects):

```
{
  "identifier": "Python-App-10020-1",
  "title": "Missing Anti-clickjacking Header",
  "blueprint": "stackHawkVulnerability",
  "properties": {
    "severity": "Medium",
    "host": "https://example.com",
    "totalCount": 1,
    "category": "Information Leakage",
    "url": "https://app.stackhawk.com/scans/c30e848d-35a7-4357-a113-35ce3392e967/finding/10020-1",
    "tags": ["test-application"]
  },
  "relations": {}
}
```
