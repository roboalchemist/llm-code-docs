# Source: https://plivo.com/docs/number-masking/concepts/how-it-works.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Number Masking Works

> Visual walkthrough of the number masking call flow

This guide walks through how number masking connects two parties while keeping their real phone numbers private.

## Call Flow

Suppose you have a web or mobile application that needs to connect two participants in a voice call.

<Steps>
  <Step title="Collect phone numbers">
    Your application collects the phone numbers of two participants whose numbers you want to mask.

    <Frame caption="Collecting party phone numbers">
      <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-agent.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=e334fb76e2157be923da8edcd9451a04" width="889" height="477" data-path="images/number-masking/number-masking-api-agent.png" />
    </Frame>
  </Step>

  <Step title="Create a masking session">
    Your application sends these phone numbers to Plivo's Number Masking API.

    <Frame caption="Sending numbers to Plivo">
      <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-party-number.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=359c276d84167b7656edc2a218d3edbe" width="889" height="477" data-path="images/number-masking/number-masking-api-party-number.png" />
    </Frame>
  </Step>

  <Step title="Receive virtual number">
    Plivo creates a session and assigns a virtual phone number from your account.

    <Frame caption="Virtual number assignment">
      <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-virtual-number.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=0c8772a2b92d479f1f22b34b29e384a4" width="889" height="477" data-path="images/number-masking/number-masking-api-virtual-number.png" />
    </Frame>
  </Step>

  <Step title="Connect the parties">
    Display the virtual number to both participants. When either party calls it, they're automatically connected to the other party. The caller ID shows the virtual number, masking real numbers from both sides.

    <Frame caption="Masked call connection">
      <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-customer.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=7620f6fa418e23e64ce31677295510a4" width="889" height="477" data-path="images/number-masking/number-masking-api-customer.png" />
    </Frame>
  </Step>
</Steps>

## Prerequisites

To use Number Masking:

1. **Plivo account** - [Sign up](https://cx.plivo.com/signup) with your work email if you don't have one
2. **Voice-enabled phone numbers** - Rent numbers from the [Numbers page](https://cx.plivo.com/phone-numbers) or via the [Numbers API](/numbers/account-phone-numbers)

## Click-to-Call Scenario

In a click-to-call flow:

1. User taps a call button in your app
2. Your app displays the virtual phone number
3. User dials the virtual number
4. Plivo connects them to the other party
5. Both parties see only the virtual number as caller ID

**Testing**: From the first party phone, dial the virtual number. The second party phone should ring with the virtual number as caller ID. Try calling from the second party phone as well. Calls from unregistered numbers won't connect (unless PIN authentication is enabled).

## Request-a-Call Scenario

In a request-a-call (or "call me") flow:

1. User clicks a "Call Me" button and provides their phone number
2. Plivo calls that number (first party)
3. When answered, Plivo calls the second party
4. Both calls are bridged together
5. Both parties see the virtual number as caller ID

This scenario is useful when:

* Customers are roaming and can't make outbound calls
* You want to absorb call costs rather than having customers pay

**Testing**: Click the Call Me button and provide a phone number. Plivo should call that number showing the virtual number as caller ID. When you answer, the second party's phone should ring with the same virtual number displayed.

## Next Steps

* [Create a Session](/number-masking/api/session#create-a-session) - API reference for creating masking sessions
* [PIN-based Authentication](/number-masking/concepts/pin-based-authentication) - Allow calls from unregistered numbers
* [Virtual Number Allocation](/number-masking/concepts/virtual-number-allocation) - Calculate your number inventory
