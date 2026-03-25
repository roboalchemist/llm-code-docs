# Source: https://plivo.com/docs/messaging/concepts/encoding-and-concatenation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Encoding and Concatenation

> SMS character encoding, GSM vs Unicode, message concatenation, and segment limits

This page discusses the types of SMS character encoding Plivo uses and explains how messages are handled when message sizes increase beyond a certain limit.

## Message units

Plivo charges for SMS messages based on the number of message units each message contains. The SMS protocol specifies a length of exactly 140 bytes for each message. If message text is longer than that, the message will be split into multiple message units. The way a message is split depends on the type of character encoding applied to your message text. Different kinds of characters use different character encoding and use different numbers of bytes per character.

## Encoding types

Plivo encodes SMS messages based on the characters used in the message text. We support two types of character encoding: GSM (GSM 03.38) and Unicode (UCS-2).

### GSM 03.38

* GSM 03.38 encoding applies when characters used in the message text are from within the [standard GSM-7 and extended character sets](https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38), which handle English characters and those of most Western European languages.
* GSM-7 characters are seven-bit characters. The calculation of the characters for one SMS message unit is:
  * *1 unit of SMS = 140 bytes*
  * *1 byte = 8 bits*
  * *(140 bytes \* 8 bits)/7 bits = 160 characters*

### UCS-2

* When the characters are not from the GSM-7 and extended character sets, Plivo uses [UCS-2 character encoding](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) for the entire message.
* UCS-2 characters are 16-bit characters. Therefore, the calculation of the characters for one SMS message unit is:
  * *1 unit of SMS = 140 bytes*
  * *1 byte = 8 bits*
  * *(140 bytes \* 8 bits)/16 bits = 70 characters*

## Concatenation

When you send an SMS message longer than 140 bytes (that is, longer than 160 or 70 characters, depending on the character encoding), the message is split into multiple units that must be assembled (concatenated) into a single message at the receiving end. To accomplish this, Plivo adds segmentation information to each message unit’s User Data Header (UDH), a data structure in the message payload that specifies how the message should be formatted and processed.

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/concatenated_sms.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=8572162509cfe5aeaad8731f08b8db06" alt="concatenated_sms" width="859" height="775" data-path="images/concatenated_sms.png" />
</Frame>

## Character limits

The character limit of the whole message is based on the type of encoding applied for the message text.

### GSM

Messages that contain only GSM 03.38 7-bit characters have a maximum limit of 1,600 characters. Messages longer than 160 characters are split into multiple message units, each unit consisting of 153 characters plus a UDH.

* *1 unit of SMS: 140 bytes*
* *User Data Header: 6 bytes*
* *140 bytes - 6 bytes = 134 bytes = 1,072 bits*
* *GSM characters: 7 bits*
* *1072/7 = 153 characters*

### Unicode

Messages containing one or more UCS-2 16-bit Unicode characters have a maximum limit of 737 characters. Messages longer than 70 characters are split into multiple message units, each unit consisting of 67 characters plus a UDH.

* *1 unit of SMS: 140 bytes*
* *User Data Header: 6 bytes*
* *140 bytes - 6 bytes = 134 bytes = 1,072 bits*
* *Unicode characters: 16 bits*
* *1072/16 = 67 characters*

<Note>
  Note:

  Two-way SMS-enabled virtual numbers provided by Plivo support SMS concatenation by default. This means that when an SMS message sent to your virtual number consists of more than one unit, it’s automatically concatenated back into a single message.
</Note>

Check your character count and message units using tools like - [CharacterCount](https://charactercounter.com/sms)
