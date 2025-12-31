# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/date-and-time.md

# Date and time

You can use date and time in the card input to provide a date picker for the user.&#x20;

### Syntax

The following is the syntax to add a picklist response in the card input:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191 character limit for all the user-defined text fields.
* **format** and **disable\_weekends** attributes are not supported in the Microsoft Teams channel due to the limitations on the channel's side.&#x20;
* In the MS Teams channel, only the "date" type is supported due to the limitations on the channel's side.&#x20;
* See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.&#x20;
  {% endhint %}

```yaml
"card": {
 "inputs": [{
 "title": "<<cardTitle>>",
 "type": "date_time/date",
 "uuid": "<<secure_random_uuid>>",
 *"disable_weekends": true/false,
 *"default_value": "<<default_value>>",
 *"min_date": "<<min_date_value>>",
 *"max_date": "<<max_date_value>>",
 *"should_validate": true/false,
  "format": "<<date format>>",
 }]
}
* - Indicates optional parameter
```

<table><thead><tr><th width="201.33333333333331">Attribute</th><th width="409.7804878048781">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of the card.</td><td>String</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the date and time entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p><p></p><p>Date selected by the user is available in the context.last_message.</p><p></p><p>Syntax: <code>context.last_message.&#x3C;&#x3C;uuid>></code></p></td><td>String</td></tr><tr><td>disable_weekends</td><td><p>Indicates if weekends must be disabled in the date picker or not. This is an optional attribute. </p><p></p><p>This attribute is not supported in the Microsoft Teams channel due to the limitations on the channel's side. See <a href="../../../../../../../build-agents/configure-agents/deploy/microsoft-teams-ms-teams#microsoft-teams-compliance">Microsoft Teams Compliance</a>, for more information.</p></td><td>Boolean</td></tr><tr><td>default_value</td><td><p>Indicates the default value displayed in the date</p><p>picker in the format - MM/DD/YYYY HH:MM. If you</p><p>are using only Date, then you can skip specifying</p><p>HH:MM. This is an optional attribute.</p></td><td>String</td></tr><tr><td>min_date</td><td><p>Indicates the minimum date or the start date</p><p>displayed in the date picker in the format -</p><p>MM/DD/YYYY HH:MM. If you are using only Date,</p><p>then you can skip specifying HH:MM. This is an</p><p>optional attribute.</p></td><td>String</td></tr><tr><td>max_date</td><td><p>Indicates the maximum date or the end date</p><p>displayed in the date picker in the format -</p><p>MM/DD/YYYY HH:MM. If you are using only Date,</p><p>then you can skip specifying HH:MM. This is an</p><p>optional attribute.</p></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not before submitting. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>format</td><td><p>Indicates the date formats.<br>By default, it is "DD-MM-YYYY HH:mm"</p><p>You can change the format accordingly Like </p><ul><li>MM-DD-YYYY</li><li>DD-MM-YYYY</li></ul></td><td>String</td></tr></tbody></table>

### **Examples**

**Example 1**: The following is a sample JS to provide a date picker in the card input without default values:

```yaml
return {
  "card": {
    "inputs": [
      {
        "title": "Date of Birth",
        "type": "date_time",
        "uuid": "2025383e-9127-4091-b565-6a01a3701911"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKMS0v4QYAhPordP41mR1%2Fimage.png?alt=media\&token=92035c89-19cc-46fa-8c3a-f269916312bc)

You can use `context.last_message.<<uuid>>`to get the date selected by the user.

**Example 2**: The following is a sample JS to provide a date picker in the card input with default values and other options:

```yaml
return {
  "card": {
    "inputs": [
      {
        "title": "Date of Birth",
        "type": "date_time",
        "uuid": "2025383e-9127-4091-b565-6a01a3701911",
        "disable_weekends": true,
        "default_value": "12/01/2019 10:00",
        "min_date": "12/01/2019 10:00",
        "max_date": "12/31/2019 10:00",
        "format": "DD-MM-YYYY HH:mm"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FR0WXnzq9eZaJrUeldgKJ%2Fimage.png?alt=media\&token=e25501b5-3a88-4133-8356-9f78423c4b98)

Note that the date from the date picker is displayed in the specified format. You can use `context.last_message.<<uuid>>` to get the date selected by the user.

**Example 3**: The following is a sample JS to provide a date picker in the card input with only Date:

```yaml
return {
  "card": {
    "inputs": [
      {
        "title": "Date of Birth",
        "type": "date",
        "uuid": "2025383e-9127-4091-b565-6a01a3701911",
        "disable_weekends": true,
        "default_value": "12/30/2019",
        "min_date": "12/01/2019",
        "max_date": "12/31/2019"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSC9PF94VB644r8sGASwk%2Fimage.png?alt=media\&token=abaacec5-bcf5-4330-b1d2-df40e5fd46d2)

You can use `context.last_message.<<uuid>>` to get the date selected by the user.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
