# Source: https://plivo.com/docs/messaging/concepts/sender-id-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sender ID

> Sender ID types, country-specific rules, and how to configure your messaging identity

Sender ID is the name or number that is displayed as the sender of the SMS message to the receiver of the SMS message. This can be either alphanumeric (for example, PLIVO) or numeric (for example, a mobile phone number). Sender IDs identify your business and help your customers recognize and recall your brand.

These are the different types of sender IDs your company might utilize.

## Long code sender ID

Long code sender IDs are normal phone numbers used to send and receive SMS messages. These are ten-digit numbers that enable you to have a conversation with your customers.

<Note>
  <strong>Note:</strong> For SMS messaging in the US and Canada, long codes are meant for person-to-person (P2P) communication, or conversational SMS, and don’t work well for high-volume one-directional application-to-person (A2P) messaging use cases.
</Note>

## Short code sender ID

Short code sender IDs are six-digit phone numbers (for example, 123456) used to send and receive SMS messages. There are no restrictions on the number of SMS messages you can send per day, per short code sender ID. This allows you to communicate with your customers on a large scale.

<Note>
  <strong>Note: </strong>In the US and Canada, enterprises use short codes for business-critical SMS messaging, because they offer the best possible reliability at the highest possible scale (100 SMS messages per second).
</Note>

## Toll-free sender ID

Toll-free phone numbers in the US can be provisioned to send and receive SMS messages. Plivo is one of the few toll-free phone number providers that also have the capability to provision toll-free numbers for SMS. Best suited for official business communication as people already perceive toll-free numbers as business lines. Plivo can also enable your existing toll-free phone numbers to handle SMS.

## Alphanumeric sender ID

Alphanumeric sender IDs are a combination of alphabetic characters and numbers that can be used to identify your business. In some countries, alphanumeric sender IDs need to be preregistered with a local carrier — refer to our [list of country requirements for sender IDs](https://support.plivo.com/hc/en-us/articles/360041448032) for details.

The following details are required for registering an alphanumeric sender ID:

* **Sender ID:** the sender ID that you want to register must be between six to 11 characters in length, depending on the destination. It cannot contain spaces or hyphens. The sender ID can include numbers, alphabetic characters, or a combination of both.

  <Note>
    <strong>Note:</strong>

    * Messages to the US and Canada cannot be sent using alphanumeric sender IDs and must originate from an SMS-enabled Plivo phone number.
    * The sender ID for India must be exactly six alphabetical characters.
  </Note>

* **Company name:** the name of your company.

* **Sample message:** a sample of the messages you plan to send.

* **Use case:** either transactional (for example, sending verification codes to customers) or promotional (for example, messages related to offers).

* **Company website:** a link to the website of your company

* **Destination countries:** a list of the top five countries, except the US and Canada, where your SMS traffic is anticipated to be high.
