# Source: https://plivo.com/docs/number-masking/concepts/single-party-sessions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Party Sessions

> Create masking sessions when only one party's number is known

## Introduction

You can now create number masking sessions with a single party number. Single-party number masking sessions are ideal for customers who only know one party's number. They allow everyone to connect securely while maintaining privacy for every member of the call.

## Use cases

### Logistics

In logistics, when a package arrives at a warehouse, the only available information is often the customer's phone number. Delivery agents are typically assigned only after the parcel is ready to be handed over. In such scenarios, companies may opt to initiate a session using the customer's phone number initially and update the session details once a delivery agent is assigned. This approach ensures seamless communication without exposing personal phone numbers.

### Cooking Instructions at Restaurants

Restaurants frequently receive online orders that include specific cooking instructions. Since various chefs may handle these instructions, it may not be practical to create sessions using a central number, like that of a restaurant admin. Instead, creating sessions with the customer's phone number allows any chef to contact the customer directly, regardless of the originating phone number, while keeping both parties' numbers anonymous. This setup ensures that instructions are clearly communicated and privacy is maintained.

## When to use single-party sessions

Customers can create single-party number masking sessions using Plivo's API and setting `create_session_with_single_party` to true during session creation. A value for either `first_party` or `second_party` is required.

Please note the following:

* If the session is created without PIN authentication (`is_pin_authentication` set to false), any party calling the virtual number will be connected directly to the `first_party` or `second_party` number provided during session creation.
* If the session is created with a single party number and PIN authentication is enabled (`is_pin_authentication` set to true), successful PIN authentication is required before any party can be connected to the virtual number.
* If the missing party details are not updated and an interaction is initiated with the registered party in a session, any call made by the registered party (either the first or second party) to the virtual number will be routed based on the last interaction. For example, if only the customer number is used to create a session, an agent calling from number X to the virtual number will be directly connected with the customer (the registered party in the session). If the customer calls back to the virtual number, Plivo will route the call to the agent's number X based on the last interaction.

Updating the active session with either `first_party` or `second_party` numbers is only applicable if the session was created with `create_session_with_single_party` set to true.

## Next Steps

* [Create a Session](/number-masking/api/session#create-a-session) - Learn how to implement single-party sessions using the API
* [PIN-Based Authentication](/number-masking/concepts/pin-based-authentication) - Add an extra layer of security to your sessions
