# Source: https://docs.neuron.world/node-builder-software/tutorial-2-sell-consultancy-with-chat.md

# Tutorial 2: Sell consultancy with chat

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Built a bidirectional communication system
* ✅ Created an interactive chat-based service
* ✅ Learned how to receive messages from buyers
* ✅ Provided real-time consultancy services via P2P chat

## Before You Start

Make sure you have:

* ✅ Completed the [installation tutorial](https://docs.neuron.world/node-builder-software/installation) and [hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Discord account with Beta OG status
* ✅ About 25 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

In this tutorial, we'll demonstrate how information can flow bidirectionally. Once again, you'll take on the role of a data seller, but we'll diverge from previous tutorials where the information producer was the seller.

Here you'll take the role of being a consultant, e.g. a tax expert or psychologist that sells consultancy services via chat.

In this example, your buyer will be a bot that initiates the chat, asks you questions by sending p2p messages directly into your seller p2p node and you will be seeing these and replying using a chat UI.

### Action 1: Get a ready made template

You will need to know how to configure Seller nodes and link them up with Neuron P2P nodes. If you haven't done so already, [complete the installation tutorial](https://docs.neuron.world/node-builder-software/installation) first and then [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). The hello world tutorial contains instructions on how to use a remote bot to act as a buyer thus, don't skip it.

To speed things up, we have a ready made solution (flow) that you can load into your builder.

* Exit any previous NodeBuilder instances and start with a clean canvas. Check if any process is lingering from previous runs and kill it.
* Click on templates
* Select "p2p-chat"
* Highlight the newly generated tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FInixfu0oTzE7sRs0vfKC%2F5.gif?alt=media&#x26;token=ffc67a83-3817-496d-910b-a119338ca03b" alt=""><figcaption></figcaption></figure>

Alternatively,

* visit <https://raw.githubusercontent.com/NeuronInnovations/neuron-node-builder/refs/heads/master/templates/p2p-chat/flow.json>
* copy into your clipboard the flow code
* right click on your canvas and open the import menu

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FF35KooEQV2nQ0h83qCR4%2Fimage.png?alt=media&#x26;token=7773d09f-41aa-4394-8bf5-8a58cd9b23bf" alt="" width="375"><figcaption></figcaption></figure>

* paste your clipboard into the resulting screen

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fl5tJ2Q7LwUiWpXAnfoFz%2Fimage.png?alt=media&#x26;token=e2279119-0084-4a20-ab2a-ded66906c8c8" alt="" width="375"><figcaption></figcaption></figure>

You have now a ready made flow imported and are ready to setup a few things.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FjvGa1RC4Ol3ZsP2MMEfh%2Fimage.png?alt=media&#x26;token=2027eaa6-e3a9-46a0-a37b-dcb1628248c0" alt=""><figcaption></figcaption></figure>

### Action 2: Setup the "Chat seller config" and "Neuron P2P out"

Setup the <mark style="background-color:blue;">Chat seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, refer to [Action 1 and Action 2 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). Remember to hit deploy and wait for connection to become active.

Note that creating new configuration sets up new hedera and topic accounts, which costs network fees. To avoid these, prefer to reuse existing configurations by selecting one you have previously generated. You will find them in the dropdown unless these are used already in other tabs. As seen below, when selecting an existing configuration the deitals of the config are prefilled for you. Don't forget to hit the red done button to make the config stick.

![alt text](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-de31c19bfc6d9e9ab15f446721d9b8adcf3e004f%2Fimage-2.png?alt=media)

### Action 3: Visit localhost:1880/ui in a new tab

The template loads a chat UI which will allow you to directly talk to the bot that is installed in our discord channel.

### Action 4: Copy and communicate your EVM address

* Double click the "Chat seller config"
* Copy the EVM address into your clipboard

If you need help with this, refer to [Action 5 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world).

### Action 5: Go to the discord bot and send chat messages back and forth

* Goto `#node-builder-builders` on Discord <https://discord.gg/4APVGrwM>
* Type the following message:

  `/tech-support test my seller <my-evm-address>` and observe the reply thread
* Type `let us start` in the message thread and then type `All OK?` or some other message of your choice. NOTE: You need type in the message thread and not in the main chat window, otherwise the message is not procecced.
* Observe the message appearing in `localhost:1880/ui`
* Goto the UI and send messages back to discord.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FaDh5qrEendPeXuLyC33s%2F10.gif?alt=media&#x26;token=91834818-daba-4405-9310-7aa6e4a07df4" alt=""><figcaption></figcaption></figure>

:red\_circle: <mark style="color:red;">Note: the discord channel is a public channel and messages you send will be visible to other BetaOGs!</mark>

It's important to note that while Discord messages are public due to the presence of a bot acting as a neuron node, this setup allows for public interaction. However, it's entirely possible to host other neuron nodes where the communication is bidirectional, private, and encrypted, ensuring secure interactions.

## What You Just Accomplished

🎉 **Congratulations!** You've successfully:

* Built a bidirectional communication system
* Created an interactive chat-based consultancy service
* Learned how to receive and respond to buyer messages
* Experienced real-time P2P chat communication
* Understood how services can be interactive, not just data streams

## Common Problems & Solutions

**Problem:** Chat UI doesn't load at localhost:1880/ui

* **Solution:** Make sure you deployed the flow and the template loaded correctly

**Problem:** Messages don't appear in the chat UI

* **Solution:** Check that your seller is "Active" and the bot is connected

**Problem:** Can't send messages back to Discord

* **Solution:** Restart the discord sequence and write the first two messages in discord. The first one simply wakes up the bot while the second one should appear in the chat. Only type messages in the UI after messages are received from discord.

**Problem:** Bot doesn't respond to initial command

* **Solution:** Check your EVM address is copied correctly (no extra spaces), check heartbeat status.

## Key Differences from Previous Tutorials

This tutorial introduced several new concepts:

* **Bidirectional communication**: Unlike previous tutorials where you only sent data, here you both send and receive
* **Interactive services**: The service responds to buyer inputs in real-time
* **Chat interface**: You interact through a web UI rather than just automated data generation
* **Service-based selling**: You're selling your expertise/time rather than just data

## Next Steps

Ready for more advanced tutorials? Continue to:

* [Tutorial 3: Replace Human Consultant with AI](https://docs.neuron.world/node-builder-software/tutorial-3-replace-human-consultant-with-ai) - Automate your consultancy with AI
