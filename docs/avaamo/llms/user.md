# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user.md

# user

Context user contains the details of the user interacting with the agent. The following functions are supported:&#x20;

* [context.user.getDevice()](#getdevice); function to detect the device used by the user interacting with the agent.
* [context.user.getChannel()](#getchannel); function to get the channel details used by the user interacting with the agent.&#x20;

### Attributes

The following is a sample JSON of user details in the context object:

```yaml
"user": {
 "phone": null,
 "layer_id": "dashboard_admin_test_user_696",
 "last_name": "C",
 "first_name": "John",
 
 "custom_properties": {}
 },
```

<table><thead><tr><th width="208.02177752508936">Attribute</th><th width="411.02783035697814">Description</th><th>Type</th></tr></thead><tbody><tr><td>phone</td><td>Indicates an array of phone numbers of the user interacting with the agent.</td><td>Array</td></tr><tr><td>layer_id</td><td>Indicates a unique user identifier internally used by the Avaamo platform.</td><td>String</td></tr><tr><td>last_name</td><td>Indicates the last name of the user interacting with the agent.</td><td>String</td></tr><tr><td>first_name</td><td>Indicates the first name of the user interacting with the agent.</td><td>String</td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties specified when sending requests to the agent. </p><p></p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept": "quality"</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>call_sid</td><td>Indicates the unique ID for any incoming or outgoing voice call successfully created in the C-IVR channel.</td><td>String</td></tr><tr><td>user_phone_number</td><td>Indicates the phone number used by the user for connecting to the C-IVR channel.</td><td>String</td></tr><tr><td>agent_phone</td><td>Indicates the phone number used by the agent assigned for connecting to the C-IVR channel. You can view the agent's phone number in the C-IVR channel settings. See <a href="../../../../../build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone">Conversational IVR</a>, for more information.</td><td>String</td></tr><tr><td>sso_token</td><td><p>Indicates the user access token </p><p></p><p>This is set only when the agents are deployed in MS Teams channel with user access token enabled. See <a href="../../../../../build-agents/configure-agents/deploy/microsoft-teams-ms-teams">Microsoft Teams (MS Teams)</a>, for more information.</p></td><td>String</td></tr></tbody></table>

### getChannel

You can use **context.user.getChannel()** to get channel details used by the user interacting with the agent. The following is a sample **context.user.getChannel()** JSON object:

{% hint style="success" %}
**Key point**: Use await when you wish to assign the result to a variable and use it later.

`var channel = await(context.user.getChannel());` &#x20;

`return channel.name;`
{% endhint %}

```json
{
  "name": "MacPizza External Channel",
  "uuid": "8d93923c-d774-443c-b8cb-896f0db38781",
  "type": "web"
}
```

<table><thead><tr><th width="150">Attribute</th><th width="471.6431757359501">Description</th><th>Type</th></tr></thead><tbody><tr><td>name</td><td>Indicates the name of the channel with which the user is interacting with the agent. </td><td>String</td></tr><tr><td>uuid</td><td>Indicates a unique identifier of the channel.</td><td>String</td></tr><tr><td>type</td><td>Indicates the type of channel with which the user is interacting with the agent such as C-IVR, web, Facebook, SMS, voice, WhatsApp.</td><td>String</td></tr></tbody></table>

### getDevice

You can use **context.user.getDevice()** to get device details used by the user interacting with the agent. The following is a sample **context.user.getDevice()** JSON object:

{% hint style="success" %}
**Key point**: Use await when you wish to assign the result to a variable and use it later.

`var device = await(context.user.getDevice());` &#x20;

`return device;`
{% endhint %}

```json
{
  "device_uuid": "30809947-ec9a-4408-93ac-c7523d1f3058",
  "os_name": "web",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
  "zone_offset": 5.5,
  "utc_offset": 19800,
  "time_zone": null,
  "location_info": {
    "ip": "xx.xxx.xx.xx"
  },
  "locale": "en-US",
  "last_visited_page": "https://cx.avaamo.com/",
  "last_visited_page_title": "Mac Pizza skill - skill - Avaamo Dashboard",
  "channel": "web"
}
```

<table><thead><tr><th width="202.32491146502443">Attribute</th><th width="346.7868020304569">Description</th><th>Type</th></tr></thead><tbody><tr><td>device_uuid</td><td>Indicates a unique identifier of the device </td><td>String</td></tr><tr><td>os_name</td><td>Indicates the operating system of the device with which the user is interacting with the agent.</td><td>String</td></tr><tr><td>user_agent</td><td>Indicates the browser’s user agent, applicable only for the web channel.</td><td>String</td></tr><tr><td>zone_offset</td><td>Indicates the time zone offset from GMT for the user.</td><td>Decimal</td></tr><tr><td>utc_offset</td><td>Indicates the time zone offset from UTC for the user.</td><td>Decimal</td></tr><tr><td>location_info</td><td>Indicates the IP address of the user machine, applicable only for the web channel.</td><td>JSON key-value pairs</td></tr><tr><td>locale</td><td>Indicates the locale used by the browser, applicable only for the web channel.</td><td>String</td></tr><tr><td>last_visited_page</td><td>Indicates the URL of the platform application last visited by the user, applicable only for the web channel.</td><td>String</td></tr><tr><td>last_visited_page_title</td><td>Indicates the title of the last page visited by the user, applicable only for the web channel.</td><td>String</td></tr><tr><td>channel</td><td>Indicates the type of channel with which the user is interacting with the agent such as C-IVR, web, Facebook, SMS, voice, WhatsApp.</td><td>String</td></tr></tbody></table>
