# Source: https://docs.neuron.world/node-builder-software/tutorial-3-replace-human-consultant-with-ai.md

# Tutorial 3: Replace human consultant with AI

:octagonal\_sign: These tutorials are for Neuron Beta OGs, if you don't have Beta OG status in discord then you will not be able to complete this tutorial.

In the previous tutorial [buy-consultancy-via-chat](https://docs.neuron.world/node-builder-software/buy-consultancy-via-chat "mention")we designed a chat UI to reply to chat messages from a connected peer and act as consultants. In this tutorial we do something similar, the difference is that we will allow an AI agent to supply the seller's messages instead. This flow is slightly more complicated thus if you haven't followed the previous tutorial [do so now](https://docs.neuron.world/node-builder-software/buy-consultancy-via-chat) and make sure you [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world) to be able to continue. \\

### Action 1 : Import the AI seller consultant template

* Goto "template"
* Select the template
* Click import
* Open the newly appeared tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FgQyc7pq0L0CSAB7LIUb5%2F11.gif?alt=media&#x26;token=cb1a1ee0-5872-4c1a-b6e3-97839fd9a107" alt=""><figcaption></figcaption></figure>

You should end up with this flow.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2F68XJbl0ap79RwLcFOtH4%2Fimage.png?alt=media&#x26;token=59c4b3fe-ad11-4025-a0e5-df88d4bf4d23" alt=""><figcaption></figcaption></figure>

### Action 2. Setup the "Consultant Seller config" and "Neuron P2P Out"

Setup the <mark style="background-color:blue;">Consultant seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, go to [your-first-program-hello-world](https://docs.neuron.world/node-builder-software/your-first-program-hello-world "mention") . Remember to hit deploy and wait for connection to become active.

Note that creating new configuration sets up new hedera and topic accounts, which costs network fees. To avoid these, prefer to reuse existing configurations by selecting one you have previously generated. You will find them in the dropdown unless these are used already in other tabs. As seen below, when selecting an existing configuration the deitals of the config are prefilled for you. Don't forget to hit the red done button to make the config stick.

![alt text](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-de31c19bfc6d9e9ab15f446721d9b8adcf3e004f%2Fimage-2.png?alt=media)

You are now ready to send data into your seller via a peer to peer connection.

### Action 3: Create an account with OpenRouter and obtain a key

Go to [OpenRouter](https://openrouter.ai/) and get a free key; make sure you understand the terms and remember this is a tutorial and you should not use these examples in a production environment. Then enter they key by double clicking on the "My AI Model" node.

* Hit Done
* Hit Deploy

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FNyTequ3ig6f440rQp3JH%2Fimage.png?alt=media&#x26;token=087ad7d5-63c0-41ba-8dd4-0e743e88cd66" alt="" width="375"><figcaption></figcaption></figure>

### Action 4: Open a new browser tab at localhost:1880/ui

We will be using this chat window to monitor messages that are sent between AI agent and the buyer, but don't need to write anything in it.

### Action 5: Communicate our EVM address to the buyer in discord

* copy your EVM address by clicking the "Consultant Seller Config" node. Here's a[ reminder on how to do that.](https://docs.neuron.world/your-first-program-hello-world#action-5-communicate-our-evm-address-to-the-other-side-the-buyer)
* Goto #node-builder-builders on Discord <https://discord.gg/4APVGrwM>​ Note : the channel is a public channel and messages you send will be visible to other BetaOGs!
* Type the following message:`/tech-support test my seller <my-evm-address>`
* Click on the message thread and type in the following messages
  * Let us start chatting
  * What is your name?
* Observe the UI at localhost:1880/ui and note that the AI bot is replying to the messages received from discord! You can ask more questions by entering them on discord, just remember to give your local agent some time to have a chance to process the request and reply. \\

In the video clip, you can see the final sequence of actions unfold.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FyMA2vFIrY8E3ch1YMLCX%2F12.gif?alt=media&#x26;token=10d2742a-2be4-4c8d-8a5c-e869261b4341" alt=""><figcaption></figcaption></figure>
