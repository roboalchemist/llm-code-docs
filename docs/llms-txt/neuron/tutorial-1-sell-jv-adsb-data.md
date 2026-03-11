# Source: https://docs.neuron.world/node-builder-software/tutorial-1-sell-jv-adsb-data.md

# Tutorial 1: Sell JV ADSB data

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Connected to a real IoT data source (Jetvision AirSquitter)
* ✅ Built a seller that streams live aviation data
* ✅ Created your own local aircraft tracking map
* ✅ Sold structured JSON data to remote buyers

## Before You Start

Make sure you have:

* ✅ Completed the [installation tutorial](https://docs.neuron.world/node-builder-software/installation) and [hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)
* ✅ Access to a Jetvision AirSquitter device
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Discord account with Beta OG status
* ✅ About 30 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

In this tutorial we will be connecting to a local data source, a Jetvision AirSquitter, and sell aviation data to data buyers. You don't need to worry about finding buyers as we have one setup for you who lives as a bot in discord and is willing to consume your data.

To speed things up, we have a ready made solution (flow) that you can load into your builder.

### Action 1: Get a ready made template

You will need to know how to configure Seller nodes and link them up with Neuron P2P nodes. If you haven't done so already, [complete the installation tutorial](https://docs.neuron.world/node-builder-software/installation) first and then [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)

* Exit any previous NodeBuilder instances and start with a clean canvas. Check if any process is lingering from previous runs and kill it.
* Click on templates
* Select "jetvision-seller-tcp"
* Highlight the newly generated tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FfxphACDPNjkoHBcWflEO%2F1.gif?alt=media&#x26;token=b842170e-c1ec-4451-975b-3838806b5fc9" alt=""><figcaption></figcaption></figure>

Alternatively you can import code directly from Github or code that is shared from other users:

* visit <https://github.com/NeuronInnovations/neuron-node-builder/raw/refs/heads/master/templates/jetvision-seller-tcp/flow.json>
* copy into your clipboard the flow code
* right click on your canvas and open the import menu (Insert > Import)

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FF35KooEQV2nQ0h83qCR4%2Fimage.png?alt=media&#x26;token=7773d09f-41aa-4394-8bf5-8a58cd9b23bf" alt="" width="375"><figcaption></figcaption></figure>

* paste your clipboard into the resulting screen

You have now a ready made flow imported and are ready to start handling ADSB data.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fm85L13uvJOfKU5Y1m9l4%2Fimage.png?alt=media&#x26;token=c8321501-04b4-4436-8f44-f2be69ac5f8f" alt=""><figcaption><p>If you read the flow from left to right, you will find that the data is coming from a tcp connection at port 30002. The address of that connection is your local-jv-address, the one that you'll find displayed on your red box. That data is chucked JSON data as it comes out of you AirSquitter and travels down two paths: one is a local map and the other one is any potential buyer</p></figcaption></figure>

### Action 2: Setup the "Jetvision seller config" and "Neuron P2P out"

Setup the <mark style="background-color:blue;">Jetvision seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, refer to [Action 1 and Action 2 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). Remember to hit deploy and wait for connection to become active.

You are now ready to send data into your seller via a peer to peer connection.

### Action 3: Double click the "tcp" node to set the correct AirSquitter address

* Get your local-jv-address from the red box
* Enter it in the address in the tcp node
* Click Done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fl0pgMfR727VD6QOfxRZD%2F7.gif?alt=media&#x26;token=11499488-f65b-4a5c-a6b1-da3a5eeaf949" alt=""><figcaption></figcaption></figure>

### Action 4: Visit <http://localhost:1880/worldmap> in a new tab

You should be seeing the planes that your own sensor is seeing on your very own map!

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FFrNi3LY3EPYFJeo74Twa%2Fimage.png?alt=media&#x26;token=333beb9a-d410-4e5f-b4ee-01c49fc4d6a8" alt="" width="563"><figcaption></figcaption></figure>

However, let's check if our buyers are getting the JSON data too so that they can display it too on their own solutions.

### Action 5: Get the buyer bot to consume your data

This part is identical to [Action 5 and Action 6 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world) where you:

1. Communicate the EVM address to the bot
2. Check with the bot if you are setup
3. Instruct the bot to test your seller

If you need help refreshing your knowledge on how to do so then follow [Action 5 and Action 6 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world).

However, this time you should be getting structured ADSB data in JSON format from the remote bot!

You are now prepared to send a wide range of IoT data to remote peers.

## What You Just Accomplished

🎉 **Congratulations!** You've successfully:

* Connected to a real IoT data source (AirSquitter)
* Built a live aviation data streaming system
* Created your own aircraft tracking map
* Sold structured JSON data to remote buyers
* Learned how to work with TCP data sources

## Common Problems & Solutions

**Problem:** No planes showing on the map

* **Solution:** Check your AirSquitter is powered on and the TCP address is correct

**Problem:** Bot gets no data or old data

* **Solution:** Verify the TCP connection is working and you clicked "Deploy"

**Problem:** Can't find the local-jv-address

* **Solution:** Look for the red box in your flow - it displays your AirSquitter's IP address

## Next Steps

Ready for more advanced tutorials? Continue to:

* [Tutorial 2: Sell Consultancy with Chat](https://docs.neuron.world/node-builder-software/tutorial-2-sell-consultancy-with-chat) - Build interactive services
