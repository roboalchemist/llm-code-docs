# Source: https://docs.sinch.com/send-a-message/correlation-id.md

# Correlation ID

The “correlation ID” information will **not** be included in the message text, it will be hidden and used subsequently by the customer to identify the message sent.

* In order for it to work, a column must be included in the file intended for the correlation ID.

| destination    | name   | info    | ... | correlationid |
| -------------- | ------ | ------- | --- | ------------- |
| 55199999999999 | Wavy   | company | ​   | campaign\_X   |
| 55199999999999 | Movile | company | ​   | campaign\_X   |
| 55199999999999 | 1B     | company | ​   | campaign\_X   |

{% hint style="warning" %}
**Note:** All rows of the Correlation ID column must be filled.
{% endhint %}

### **Names that Will Be Interpreted as correlation ID:**

"correlationid", "correlationId", "CorrelationId", "CorrelationID", "correlationID", "Correlationid", "CORRELATIONID","correlation\_id", "correlation\_Id", "Correlation\_Id", "Correlation\_ID", "correlation\_ID", "Correlation\_id", "CORRELATION\_ID"
