# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/listing-message-templates.md

# Listing Message Templates

Request <https://apigw.wavy.global/api/v1/whatsapp_message_templates?page=1&page_size=999> **The request can contain the following parameters in the query string**

| Field         | Required | Description                                                         |
| ------------- | -------- | ------------------------------------------------------------------- |
| page          | no       | Page index beginning at 1                                           |
| page\_size    | no       | Page results. 10 by default                                         |
| element\_name | no       | Search for templates containing element\_name as part of their name |

## Response Example

```
{
 "data" : [
 {
 "message_type" : "RESERVATION_UPDATE",
 "customer_id" : 6364,
 "messages" : [
 {
 "buttons_type" : null,
 "id" : 33732,
 "buttons" : {
 "payload" : null
 },
 "language" : "EN",
 "last_modified" : "2020-06-04T14:52:39.674403",
 "placeholders" : ["data"],
 "header" : "",
 "text" : "Hello, you have an appointment with us for *{{1}}*.\nReply *YES* to confirm or *NO* to cancel.",
 "header_type" : "none",
 "status" : "approved",
 "footer" : ""
 }
 ],
 "sub_account_id" : 11486,
 "last_modified" : "2020-06-04T14:52:39.665449",
 "id" : 22045,
 "element_name" : "appointment_reminder_datetime",
 "namespace" : "whatsapp:hsm:ecommerce:movile",
 "template_type" : "header_footer",
 "languages" : ["EN"]
 },
 {
 "messages" : [
 {
 "status" : "approved",
 "footer" : "",
 "text" : "You have an appointment with us!",
 "header_type" : "none",
 "header" : "",
 "language" : "EN",
 "placeholders" : [],
 "last_modified" : "2020-06-02T18:46:01.386517",
 "buttons" : {
 "payload" : null
 },
 "id" : 33649,
 "buttons_type" : null
 }
 ],
 "sub_account_id" : 11486,
 "customer_id" : 6364,
 "message_type" : "RESERVATION_UPDATE",
 "template_type" : "header_footer",
 "languages" : ["EN"],
 "namespace" : "whatsapp:hsm:ecommerce:movile",
 "id" : 21964,
 "element_name" : "appointment_reminder",
 "last_modified" : "2020-06-02T18:46:01.384862"
 }
 ]
}
​
```

&#x20;

The response returns a list of message templates with the following fields

| Field                       | Details                                                                                                                                                                                                                                                                                                                                                                                                 | Tipo      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| languages                   | Languages this template is available in                                                                                                                                                                                                                                                                                                                                                                 | \[String] |
| namespace                   | Template namespace. Must be used in the messaging API                                                                                                                                                                                                                                                                                                                                                   | String    |
| element\_name               | Template name. Must be used in the messaging API                                                                                                                                                                                                                                                                                                                                                        | String    |
| message\_type               | <p>Template category type. Possible values are</p><p>ACCOUNT\_UPDATE, PAYMENT\_UPDATE, PERSONAL\_FINANCE\_UPDATE, SHIPPING\_UPDATE, RESERVATION\_UPDATE, ISSUE\_RESOLUTION, APPOINTMENT\_UPDATE, TRANSPORTATION\_UPDATE, TICKET\_UPDATE, ALERT\_UPDATE, AUTO\_REPLY</p>                                                                                                                                 | String    |
| template\_type              | <p>Template type. Possible values are</p><p>header\_footer or body\_only</p>                                                                                                                                                                                                                                                                                                                            | String    |
| messages\[]                 | List containing information on each template translation. The size of this list is equivalent to the number of supported languages in languages                                                                                                                                                                                                                                                         | \[Object] |
| messages\[].status          | <p>Template status. Possible values are:</p><p>in\_analysis, approved, disapproved, error</p><p>In order for a template to be approved, its content must follow Facebook’s guidelines.</p><p>​<a href="https://developers.facebook.com/docs/whatsapp/message-templates/guidelines"><https://developers.facebook.com/docs/whatsapp/message-templates/guidelines></a>​</p>                                | String    |
| messages\[].header\_type    | <p>Header type. Possible values are</p><p>video, location, text, document, image or none</p>                                                                                                                                                                                                                                                                                                            | String    |
| messages\[].header          | Text contained in the text header. Only used when header\_type = text                                                                                                                                                                                                                                                                                                                                   | String    |
| messages\[].text            | Text contained in the body                                                                                                                                                                                                                                                                                                                                                                              | String    |
| messages\[].footer          | Text contained in the footer                                                                                                                                                                                                                                                                                                                                                                            | String    |
| messages\[].buttons\_type   | <p>Button type. Possible values are</p><p>quick\_reply or call\_to\_action</p>                                                                                                                                                                                                                                                                                                                          | String    |
| messages\[].placeholders    | Description of placeholders present in the body text, represented as {{1}}, {{2}}, etc. in the text field                                                                                                                                                                                                                                                                                               | \[String] |
| messages\[].buttons.payload | <p>Button content in JSON format serialized as a string.</p><p>Quick reply buttons will be in {"payload": \[{"text": "button text"}]} format</p><p>Call-to-action buttons will be in</p><p>{"payload": \[{"url": "https:wavy.global/en", "text": "Access our website", "type": "url"}, {"text": "Call us", "type": "phone\_number", "country\_code": "55", "phone\_number": "11900000000"}]} format</p> | String    |

## Message Template Examples

Template with a text header, body and footer:

Template with an image header, body and no footer:

Template with 2 parameters:
