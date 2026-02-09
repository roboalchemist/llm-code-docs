# Source: https://www.quo.com/docs/mdx/pricing-support/pricing-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Pricing overview

> Welcome to Quo's simple and transparent API pricing structure.

## Our pricing philosophy

At Quo, we believe in transparent and fair pricing. Sometimes it can be hard to understand the true cost of something when it's buried in the fine print. We are committed to helping you clearly understand and manage your costs when using our platform.

## Core pricing model

Our pricing is based on message segments, making it easy to calculate costs:

<CardGroup cols={2}>
  <Card title="Local (US and Canada) SMS" icon="location-pin">
    <p>\$0.01 per segment</p>
  </Card>

  <Card title="International SMS" icon="globe">
    <p>\$0.01 + country-specific rate per segment</p>
    <p className="text-sm">Rates vary by destination country</p>
  </Card>
</CardGroup>

<Info>
  For detailed international rates by country, see our [International Pricing Guide](https://www.openphone.com/rates).
</Info>

## Understanding message segments

A **segment** is the basic unit we use to calculate SMS billing. Every message you send is divided into one or more segments based on two factors:

1. **Message length** (character count)
2. **Character type** (standard or special characters)

## How character types affect segment size

### Standard GSM characters

Messages using only standard GSM-7 characters fit **up to 160 characters per segment**.

Standard characters include:

* Letters (A-Z, a-z)
* Numbers (0-9)
* Spaces
* Basic punctuation (. , ! ? - etc.)

### Special/Non-GSM characters

<Info>
  **If your message contains even one special character, the entire message is billed at the 70-character limit** — not just the portion with special characters. This often results in more segments and higher costs than you might expect.
</Info>

Messages containing **any** special characters fit only **up to 70 characters per segment**.

Special characters include:

* Accented letters (é, ñ, ü)
* Curly/smart quotes (" " ' ')
* Emojis (😊, 🚀, ✨)
* Many international characters

## Tools and optimization

### Segment calculator

Use our [Segment Calculator](https://twiliodeved.github.io/message-segment-calculator/) tool to estimate costs before sending messages. This helps you optimize your message length and content to avoid unexpected charges.

### Smart encoding

The Quo API automatically enables **smart encoding** to minimize segment usage and reduce costs wherever possible. This feature works behind the scenes to choose the most efficient encoding for your messages.

## API message types

You're only charged for outgoing API-powered messages, which include:

<CardGroup cols={2}>
  <Card title="Direct API Usage" icon="code">
    Messages sent through direct API calls
  </Card>

  <Card title="Integration Messages" icon="puzzle-piece">
    Messages sent via applications built with our API
  </Card>
</CardGroup>

## How our billing works

We use a credit-based system for all API messaging charges:

<Steps>
  <Step title="Purchase credits">
    Add funds to your account through the "Plans & Billing" tab
  </Step>

  <Step title="Automatic deduction">
    Credits are automatically deducted when messages are sent
  </Step>

  <Step title="Credit management">
    Monitor your balance and enable auto-recharge to prevent service interruptions
  </Step>
</Steps>

## Important service notes

### Requirements & limitations

1. An active Quo subscription is required for API access.
2. MMS is not supported in the current API version.
3. Partial credits cannot be used for sending messages; the API will return an error.

<Warning>
  If your credit balance is insufficient for a message's full cost, the API will return an error and the message won't be sent.
</Warning>

### Support & assistance

<Info>
  Need help understanding our pricing or managing your costs? Our team is here to help. Email us at [support+developers@quo.com](mailto:support+developers@quo.com) with any questions.
</Info>
