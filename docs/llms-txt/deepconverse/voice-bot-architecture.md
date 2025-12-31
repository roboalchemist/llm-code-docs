# Source: https://docs.deepconverse.com/product-docs/voice-bot/voice-bot-architecture.md

# Voice Bot Architecture

The voice bot is geared towards handling inboung voice calls. When a customer calls the business phone number they will be routed to the voice bot. The voice bot then handles the request and if needed escalates it to a human agent.

## Architecture

The voice bot architecture comprises of the following components that integrate together.&#x20;

1. **Contact Center** - The contact center provides the support agents and handles the overall functionality related to IVR, routing, forwarding and assignment. It may also serve as the system of record holding the call recordings and associated analytics.&#x20;
2. **DeepConverse Platform** - The DeepConverse platform provides the orchestration of the conversation, executes the business logic and handles the AI and Automation components.&#x20;
3. **Cloud Speech Processing** - This component is responsible for the Speech-to-Text and the Text-to-Speech layer.&#x20;

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FymOxMGUUe3s5SdiZB9s8%2FVoice.jpg?alt=media&#x26;token=f1ddffc3-439d-4778-aa10-1c7b23735d80" alt=""><figcaption></figcaption></figure>

## Call Workflow

1. The call is received by the Contact Center configured phone number. The call and metadata is setup.
2. Based on the business logic the call is forwarded to the preconfigured **Twilio** phone number which is connected to the DeepConverse platform.
3. Using the webhook DeepConverse identifies the chatbot and the initiates the conversational flow.
4. The conversation continues till the customer shows an intent to escalate or end the call.
