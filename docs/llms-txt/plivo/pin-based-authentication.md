# Source: https://plivo.com/docs/number-masking/concepts/pin-based-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PIN-based Authentication

> Learn how PIN-based authentication enables secure connections when callers use unregistered numbers in number masking sessions.

## Overview

Plivo's number masking solution uses an intermediary virtual number to preserve the anonymity of both parties during a call. Customers can initiate a number masking session with pre-registered first and second-party numbers. However, situations may arise where a caller might use a number not previously included in the masking session. To accommodate such instances, Plivo introduces PIN verification as a means to authenticate and seamlessly connect these callers.

## How PIN-based authentication works

To see how number masking with PIN authentication works, suppose you have a web or mobile application with which you want to connect two participants in a voice call.

1. The application collects the phone numbers of the two parties whose numbers you wish to mask.
   <Frame caption="Number Masking API Agent">
     <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-agent.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=e334fb76e2157be923da8edcd9451a04" width="889" height="477" data-path="images/number-masking/number-masking-api-agent.png" />
   </Frame>
2. The application makes a Number Masking API request to Plivo with the phone numbers and authentication parameters.
   <Frame caption="Number Masking API Party Number">
     <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-party-number.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=359c276d84167b7656edc2a218d3edbe" width="889" height="477" data-path="images/number-masking/number-masking-api-party-number.png" />
   </Frame>
3. Plivo creates a number masking session and assigns to it a virtual phone number from your Plivo account.
   <Frame caption="Number Masking API Virtual Number">
     <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-virtual-number.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=0c8772a2b92d479f1f22b34b29e384a4" width="889" height="477" data-path="images/number-masking/number-masking-api-virtual-number.png" />
   </Frame>
4. Both parties receive the virtual phone number, along with unique PIN codes that both parties will use to enter the call if calling from an unknown number.
5. If either party calls the virtual phone number from a registered number, they will automatically be connected. The caller ID is set to the virtual phone number, masking the real phone numbers of both parties from each other.
   <Frame caption="Number Masking API Customer">
     <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-masking-api-customer.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=7620f6fa418e23e64ce31677295510a4" width="889" height="477" data-path="images/number-masking/number-masking-api-customer.png" />
   </Frame>
6. If either party dials the virtual phone number from an unknown number, they will be prompted to enter the PIN. Once the authentication is successful, they will be connected.
   <Frame caption="PIN-Based Authentication">
     <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/pin-based-authentication.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=e00377e9568055ad3b65d645e15eff5e" width="1600" height="802" data-path="images/number-masking/pin-based-authentication.png" />
   </Frame>

## Session

Plivo's session object assigns unique PINs to both call participants. If an unregistered caller dials the virtual number, the Number Masking API prompts this caller to verify their identity using a PIN. The caller is connected once the PIN is successfully authenticated.

Participants have two options for setting PIN numbers:

* They can set their own unique PINs, or
* Allow Plivo's Number Masking API to generate and assign PINs

For more details on PIN-related parameters, refer to the [session object](/number-masking/api/session).

## Interaction

When a registered caller dials the virtual number, Plivo seamlessly connects the call without requiring further authentication. However, if a caller dials the virtual number from an unregistered number, Plivo prompts the caller to enter their PIN for authentication purposes. This authentication is necessary for Plivo to connect the caller to the call. If the entered PIN matches the first party's PIN, the call is connected to the second party, and vice versa.

## Callbacks

For improved tracking and asynchronous updates, Plivo sends PIN authentication status callbacks to your application server. This record allows you to monitor successful and failed interactions. PIN authentication callbacks also provide visibility into the percentage of interactions occurring from registered and unregistered numbers for further analysis. Refer to [session callbacks](/number-masking/api/session#session-callbacks) for more details on PIN authentication status-related callback attributes.

## Next steps

* [Create a session](/number-masking/api/session#create-a-session) — Implement PIN-based authentication in your application
* [Number Masking overview](/number-masking/concepts/overview) — Learn more about number masking concepts
