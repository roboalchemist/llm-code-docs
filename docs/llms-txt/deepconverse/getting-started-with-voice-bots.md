# Source: https://docs.deepconverse.com/product-docs/voice-bot/getting-started-with-voice-bots.md

# Getting Started with Voice Bots

In this section you will learn how to build bots that can be deployed on the voice / phone channel. The voice bots are capable of handling calls, providing answers and executing complex workflows using AI and Automation.

Voice bots are built using the same core building blocks as the chatbots.&#x20;

{% hint style="warning" %}
This is feature is in **ALPHA**. For more information contact the DeepConverse team.
{% endhint %}

### Importance of voice bots

Voice bots built on the DeepConverse platform integrate with the business's contact center. Once a voice bot has been set up, customers can interact in human like conversations. The voice bots make use of:

1. **Speech to text (STT)** module to listen to the request of the customer, transcribe it and provide it to DeepConverse platform.
2. DeepConverse platform handles the **Natural language understanding** performing the relevant actions and composing a reply.
3. **Text to speech (TTS)** module to take the reply and convert it to human voice to be played back to the customer.&#x20;

### Considerations

1. Currently voice bots are optimized for handling support calls in English
2. Many of the platform blocks are interoperable between the voice and chat channels. That said due to the difference in the channel and expectation from customers certain channel specific behavoirs are introduced. This helps handle complex use cases better within the conversation.
