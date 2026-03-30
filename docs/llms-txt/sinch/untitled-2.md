# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/untitled-2.md

# TTL - Time to Live

## Messaging with TTL (Time to Live - The HSM’s lifespan before being delivered)

**Feature Description:**

### From v2.21.3 **(**[**https://developers.facebook.com/docs/whatsapp/changelog#app**](https://developers.facebook.com/docs/whatsapp/changelog#app)**) onwards**, you can inform the TTL (in days) for the delivery of your messages to expire (i.e., their Time to Live).

* Companies can use this to ensure messages aren’t delivered on dates later than what was set.
* Currently, TTL **can only be set for HSM messages (**[**access HSM information**](https://docs.wavy.global/whatsapp/hsm-template)**).**
* If a message is not delivered to the customer before the period set as limit, i.e. it expires, then the message will no longer be delivered.
* A status notification (CallBack) will be sent by WA.
* The status notification can be sent to our customers so long as it is configured.

{% hint style="warning" %}
**IMPORTANT: setting a TTL has the following limitations:**

* Only HSM messages
* minimum 1 day (24 hours) from the time the message is sent
* maximum 30 days
* default 7 days. (Currently, this value can be altered)
* the TTL is effective from the moment your message is sent, that is, if a message is scheduled, the TTL will be attributed by adding the value to the date when it was triggered.
* If a message receives a value of less than 1 day or greater than 30 days, our platform will, at the time of delivery, attribute values within the permitted limit.
* This behavior has been implemented to prevent us from having issues when delivering messages, as, if there is an attempt to deliver a message that does not observe the minimum and maximum TTL values, this message will be denied by the container.
  {% endhint %}

## Call for Messaging via **FTP with TTL**

Messaging exampl&#x65;**:** 2019-01-18;11:0;11:15;HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company;**2** phone;name;company 5519998873499;mozart;wavy 5519981794226;diego;wavy The information that represents the **TTL** is at the end of the first line, after the **HSM** parameter&#x73;**.**

This information will be an **INTEGER** that is represented in number of days. That is, we will have a 2-day **TTL**. This means that, after 2 days from the date and time the message is sent, if the recipient has not received the message, this message **WILL NO LONGER BE DELIVERED.**

## **Call for Messaging via API with TTL**

```
{
 "destinations": [{
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }],
 "message": {
 "ttl": 1,
 "hsm": {
 "namespace": "namespace",
 "elementName": "elementName",
 "parameters":[
 "MyParam1",
 "MyParam2"
 ]
 }
 }
 }
```
