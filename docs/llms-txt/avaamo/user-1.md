# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user-1.md

# live\_agent\_user

Context live\_agent\_user contains the details of the live agent interacting with the user.&#x20;

{% hint style="info" %}
**Note:** The `context.live_agent_user` object is available only within quick response templates in the Live Agent console. See [Quick response template](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/quick-responses#create-a-new-quick-response), for more information.
{% endhint %}

### Attributes

The following is a sample JSON of user details in the context object:

```json
"live_agent_user": {
 "phone": null,
 "layer_id": "dashboard_admin_test_user_696",
 "last_name": "C",
 "first_name": "John",
 "custom_properties": {}
 },
```

<table><thead><tr><th width="208.02177752508936">Attribute</th><th width="411.02783035697814">Description</th><th>Type</th></tr></thead><tbody><tr><td>phone</td><td>Indicates an array of phone numbers of the user interacting with the agent.</td><td>Array</td></tr><tr><td>layer_id</td><td>Indicates a unique user identifier internally used by the Avaamo platform.</td><td>String</td></tr><tr><td>last_name</td><td>Indicates the last name of the user interacting with the agent.</td><td>String</td></tr><tr><td>first_name</td><td>Indicates the first name of the user interacting with the agent.</td><td>String</td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties specified when sending requests to the agent. </p><p></p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept": "quality"</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>call_sid</td><td>Indicates the unique ID for any incoming or outgoing voice call successfully created in the C-IVR channel.</td><td>String</td></tr><tr><td>user_phone_number</td><td>Indicates the phone number used by the user for connecting to the C-IVR channel.</td><td>String</td></tr><tr><td>agent_phone</td><td>Indicates the phone number used by the agent assigned for connecting to the C-IVR channel. You can view the agent's phone number in the C-IVR channel settings. See <a href="../../../../../build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone">Conversational IVR</a>, for more information.</td><td>String</td></tr><tr><td>sso_token</td><td><p>Indicates the user access token </p><p></p><p>This is set only when the agents are deployed in MS Teams channel with user access token enabled. See <a href="../../../../../build-agents/configure-agents/deploy/microsoft-teams-ms-teams">Microsoft Teams (MS Teams)</a>, for more information.</p></td><td>String</td></tr></tbody></table>
