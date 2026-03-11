# Source: https://docs.neuron.world/node-builder-software/your-first-program-hello-world.md

# Your first program: Hello World!

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Built your first working Neuron program
* ✅ Created a "seller" that sends data to buyers
* ✅ Connected with a buyer bot on Discord
* ✅ Seen real peer-to-peer data exchange in action

## Before You Start

Make sure you have:

* ✅ Completed the [installation](https://docs.neuron.world/node-builder-software/installation "mention") tutorial
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Your Hedera credentials saved and ready
* ✅ Discord account (you'll need Beta OG status)
* ✅ About 20 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

We'll create a simple program that "sells" timestamps (current time) to any buyer who wants to purchase them. Think of it as your first digital vending machine!

✅ You should now be at 127.0.0.1:1880 in your default browser, where your local installation resides. Upon the initial installation, the system will prompt you to enter the credentials you noted down earlier

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FnCwycg93j4hJgMxcui6i%2F2.png?alt=media\&token=c35acda3-12a4-47a2-ae1f-982776e4e205)

You're expected to see an empty canvas to start writing your very first hello world using the neuron builder.

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fadk0VpsMextthanPt3zq%2F3.png?alt=media\&token=962842bc-bb49-4f01-9412-e160f44b6f88)

🚀 Let's do it: Setup the backbone

We shall write a minimal program that "sells" a random string (a timestamp) to a potential buyer. We'll do that by configuring a few nodes on this screen and then we'll go to discord to ask for a buyer to "buy" our message in a peer-to-peer manner and no intermediaries involved.

### Action 1: Drag a neuron "seller config" node into the canvas

* <mark style="color:blue;">Double click</mark> it and simply set up some basic info in the provided form. Feel free to enter any random information in here.
* Hit done.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FNtHu5NqbEtw9WYyhvvYy%2F2.gif?alt=media&#x26;token=628b0cf6-3538-4da0-a5ef-239c88cabb27" alt=""><figcaption></figcaption></figure>

This node is holding basic configuration data and is a one off process you have to do. What it does is setting up account information for that particular node which is separate to your main account (the one you created earlier upon registration)

### Action 2: Drag a "neuron p2p" node into the canvas

1. <mark style="color:blue;">Double click</mark> on it and select the previously created neuron seller to reference it.
2. Hit done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FBps3yL0unQ3jCTF9HUlR%2F2.gif?alt=media&#x26;token=7cc7ec1a-22f7-490e-9562-22b31dce7352" alt=""><figcaption></figcaption></figure>

This node is referencing the configuration node from above and is responsible for communicating direct with other nodes

🎉 You have now coded your seller's backbone to start selling information.

<mark style="color:orange;">Your program is not running yet</mark>, it will do so when you hit the deploy button; you don't need to do this as we have not connected any data sources.

🚀 Let's do it. We shall now connect data to sell

### Action 3: Drag an "inject node" into the canvas and create a connection

* Double click, and select an interval of 5 seconds
* Hit done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Forw7MoHCfEfeg47HrwCn%2F3.gif?alt=media&#x26;token=3768b83b-c23d-4071-a2ea-ca3c2121d991" alt=""><figcaption></figcaption></figure>

This is a basic node that simply injects (creates) a string or timestamp as a one off message or can be set to be done in an interval. By default it sends out timestamps and you can leave it like that.

The program's purpose is to send a timestamp via peer-to-peer (p2p) communication to any entity connected to the Seller node specified by the p2p node.

In our setting, it's important to distinguish between connecting and communicating. Imagine the Seller node as a telephone switchboard in a call center. It establishes and maintains all active connections, ensuring the lines stay connected while handling the complex tasks involved. Peers use their devices (p2p nodes) to communicate over these pre-established lines without worrying about maintaining the connections. Currently, the protocol between the p2p node and the switchboard assumes that if a p2p node doesn't specify a destination, the data is broadcast to all connected peers.

### 🚀 Action 4: hit the Deploy button

A blue dot on your flow-tab indicates that your actions are not committed. To commit actions you need to hit the deploy button. Notice that any change in the UI or node properties requires a new deploy.

Once you have done so

* wait for the Seller status to display the message "Active...". This means that a device is created and an EVM address is available to use as a communication reference.

### Action 5: Communicate our EVM address to the other side, the buyer.

We need to find our EVM address to communicate it to a potential buyer. To do so click the "Seller" node and copy the EVM address into your clipboard.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FQrU9xTjcu9uA9CqHSjzZ%2F4.gif?alt=media&#x26;token=e0fe458e-b73f-4c01-ac7d-e5c00aa801bd" alt=""><figcaption></figcaption></figure>

In the current scenario, we need a buyer or several buyers interested in purchasing our data. Fortunately, there's an enthusiastic buyer, a bot, eager to consume your information—be it a timestamp or a string you're sending out. All we need to do is share our EVM address, and this bot, which is just another neuron peer controlled by AI on Discord and Slack, will acquire your data. In addition to purchasing your data, the bot will also monitor your vitals.

:point\_right: Goto #node-builder-builders on Discord <https://discord.gg/4APVGrwM>

:red\_circle: <mark style="color:red;">Note: the channel is a public channel and messages you send will be visible to other BetaOGs!</mark>

Type the following message:

`/tech-support can you check my heartbeat status <my-evm-address>`

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FAeJn7TfkNTwtcdXe8DHY%2Fimage.png?alt=media&#x26;token=1246d135-cce4-4b67-8032-c21a4fb233d4" alt=""><figcaption></figcaption></figure>

If you get a heartbeat that's recent to a couple seconds then you're all fully set up.

### Action 6: Instruct the bot to buy your data

`/tech-support test my Seller: <my-evm-address>`

You should see the timestamp or string you have been sending out as a response in discord!

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fc5ifkRzACTlys59OhqXO%2F5.gif?alt=media&#x26;token=b67e454e-35d9-4889-adac-e3a4e7dab258" alt=""><figcaption></figcaption></figure>

At the same time you will see your node being connected to one other peer.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FRYjfacR9TMvaibeh1ARl%2Fimage.png?alt=media&#x26;token=fa773343-5685-475a-96a9-d844d914f7a5" alt=""><figcaption></figcaption></figure>

## What You Just Accomplished

You've built a complete peer-to-peer commerce system! Your program automatically:

* Generates fresh timestamps every 5 seconds
* Advertises them for sale on the Neuron network
* Handles buyer connections and data delivery

## Common Problems & Solutions

**Problem:** Bot says "No heartbeat" or shows old timestamp

* **Solution:** Make sure you clicked "Deploy" and see "Active" status on your seller node

**Problem:** Bot doesn't respond to commands

* **Solution:** Check your EVM address is copied correctly (no extra spaces)

**Problem:** NodeBuilder shows "Connecting..." forever

* **Solution:** Check your internet connection, try refreshing the browser, kill the process and restart

**Problem:** Can't find the Discord channel

* **Solution:** Make sure you have Beta OG status and joined the correct server

## Next Steps

[Tutorial 1: Sell ADS-B Aviation Data](https://docs.neuron.world/node-builder-software/tutorial-1-sell-jv-adsb-data) - Connect real IoT sensors

In the previous section, you observed how a local peer communicates basic data to a remote peer. Next, we'll explore how to enhance this example to transmit more complex data, such as ADS-B aviation information, to a buyer.
