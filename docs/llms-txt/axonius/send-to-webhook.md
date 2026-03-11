# Source: https://docs.axonius.com/docs/send-to-webhook.md

# HTTP Server - Send to Webhook

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action was formerly named Web Server Information - Send to Webhook.
</Callout>

**HTTP Server - Send to Webhook** serializes the entities retrieved from the saved query supplied as a trigger (or entities selected in the asset table) as JSON. This JSON data is sent to a configured webhook. When used with a saved query as a trigger, only the fields configured in the saved query are added to the JSON.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Webhook URL** - Specify the webhook URL.

* **Custom format for body (use `{\$BODY}` as keyword)** *(default: `{"entities": {$BODY}}`)* - You can customize the webhook body.
  * Use `{\$BODY}` to include the entities found in the saved query supplied as a trigger (or entities that have been selected in the asset table) data.
  * Use `{\$BODY_ESCAPED}` instead of `{$BODY}` if you want to escape JSON characters so that the JSON is sent as a string instead of an object. The following example shows how to use the $BODY\_ESCAPED option in this Enforcement Action's Dynamic Value statement.

```
device all
then form.custom_format
set_value concat (
"{\n", 
"    \"subject\": \"Axonius Test Message\",\n", 
"    \"message\": {$BODY_ESCAPED},\n",
"    \"issueType\": \"IT - Reports\",\n", 
"    \"subIssueType\": \"Problem\",\n", 
"    \"email\": {\n",  
"        \"to\": \"customera@companya.com\"\n", 
"    },\n",
"    \"source\": {\n", 
"        \"name\": \"Axonius Enforcement: alerthandler_ec2-uptime>60-days\",\n",
"        \"time\": \"2024-08-20T20:54:08.219Z\"\n",
"    }\n",
"}"
)
```

* **Connection timeout (seconds)** *(default: 10 seconds)* - Define the number of seconds before the attempt to connect to the webhook is considered to be timed out. As a result, the enforcement action execution will fail.
* **Writing data to webhook timeout (seconds)** *(default: 1200 seconds)* - Define the maximum number of seconds before the attempt of completing sending the data to the webhook is considered to be timed out. As a result, the enforcement action execution will fail.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Authorization header user name** and **authorization header password** *(default: empty)* - Specify authorization header user name and password, if required.
  * If supplied, Axonius passes the specified authorization header information along with the Webhook URL.
  * If not supplied, Axonius does not pass any additional information along with the Webhook URL.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTP proxy** - When a proxy is supplied, Axonius uses the proxy instead of the direct URL, when connecting to the HTTP **Webhook URL**.
* **Additional headers** \*(default:

```json
{"Content-type": "application/json"}
```

)\* - Add Customized Headers to be Sent with Request. For Example:

`{"Content-type":"application/json","Accept":"application/json","Authorization":"Bearer "}`

* **Max retry attempts** - Enter the number of times you want to retry running the action before reporting a failure.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).