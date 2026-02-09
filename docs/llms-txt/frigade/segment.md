# Source: https://docs.frigade.com/integrations/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment

Frigade supports bidirectional reads and writes from Segment. This guide shows you how to get started in a few minutes.

## Sending Segment data to Frigade

You can set up Frigade as a destination for Segment identify, group, and track calls by using [Webhooks as a destination](https://segment.com/docs/connections/destinations/catalog/webhooks/).

<Steps>
  <Step title="Add webhook destination">
    Log in to your Segment account, open workspace, and select source. Click on **Add Destination** and search and select **Webhooks**.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6c5d04e248ea13e47275a49a41d29b99" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1809bc76e0407eca23b3fc89d23f9bba 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e5cedf6f3d7a1fa47f679c768187ab11 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f92f058339b662308b2fc1eeae887477 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5e92d1218c6d1f7f7377063d32916b94 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a876572c6528a045de75b9e97d76ba77 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fb053803703463dd26ebd6232369df61 2500w" />
  </Step>

  <Step title="Create mapping">
    Next after creating the destination, click the **Mappings** tab and add a new mapping:

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37908f8bb79f582c9e09cf06ee257573" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fdbe0c9849b0bb87c413ff69c2f7113c 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=140fc5f0d2a17cca32d2636a9f53eb61 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=79b87d5c14113ccfd3cbe2a0f1c514c0 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8b2d1b25ba3c476fb2e7e528de875422 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1f7e8a2a6f829efa815a8ba014e4982d 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=bb0c2606c3750e1215ccf9566ad1b790 2500w" />
  </Step>

  <Step title="Select event types to send to Frigade">
    Select the event types you want to send to Frigade. In this example we select identify, group, and track, but you can select any event type you want to send to Frigade.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8f7a0d6cbeec26ee36566068af74cdcd" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=737ff2bc8a46d8b326f38aebf09eba03 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=091c97443415b8686caf731536872b8e 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=38e705746f29870c376ad8bbe0ceeea8 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b31e9bdc9e3bda73861deb8bae47f888 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7168293f36ca38d1b9597a8d2bed660a 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e6be6b484bf9752db845ac18c858d920 2500w" />
  </Step>

  <Step title="Add Frigade Webhook URL">
    Fill out the **Select mappings** as shown below using:

    * `https://api.frigade.com/v1/thirdParty/cdp/segment` as the URL
    * `POST` as **Method**
    * `100` as **Batch Size**. Note: if you send fewer than 500 events per day, it is recommended to set this to a lower value to avoid delays in sending events to Frigade.
    * Your secret Frigade API key (it will be the one prefixed with `api_private`). This key can be found in the dashboard under [API Keys](https://app.frigade.com/developer). Make sure to prefix it with `Bearer` as shown in the screenshot below.
    * `Authorization` as the key

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=dc4edba3b13ba6b5c78facb695706ac5" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=74c8ef7d60b93c3a77e2a8e72e57c768 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c752865c5f981c719b6fcd8358301150 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e355f97b587b1ee887105712ace02e36 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=313bfb747eccb7239f0a9b0ca324ffdb 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3731190ba1ab9fb5e5bef057d8fdbc16 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a328960feef324359131c4894139c1ba 2500w" />

    Finally, set **Enable Batching?** to **Yes**. Optionally, you can send a test event to verify that the webhook is working. Click **Save** to save the webhook.
  </Step>

  <Step title="Turn on the webhook">
    Finally, turn on the webhook by turning on the mapping you just created. Then, open the **Settings** tab and enable the Destination.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1f8e9228b06b13d248042ad2d3064ca1" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=4d4e3aded498252853a59f92ca437269 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9ef86f56b3385aaba37429d2615a5967 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=86604375a57fe8b11099a243ce1db124 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7c2c1e857ba5620c295b5c7549d6f29c 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6e8d62ed25f1d4c4800355861a6b40f2 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1a3151c991056b55895ae3dc409dab08 2500w" />

    Congratulations! You have successfully set up Frigade as a destination for Segment. You can now use Frigade's [Targeting](/platform/targeting) with your Segment data to create personalized experiences for your users.
  </Step>
</Steps>

## Sending Frigade data to Segment

Frigade also supports sending user and organization events from Frigade Flows to Segment.

<Steps>
  <Step title="Add your Segment write key">
    To send events to your Segment instance, select **Add Source** and then **HTTP API**. Then, copy your Segment write key.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c6d0bb8874625bae5100bbbcd37596c7" className="rounded" data-og-width="3976" width="3976" data-og-height="2282" height="2282" data-path="images/segment-write.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=478cc2c4994e76c9879a4b2123c84e1f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7124659f327b2de8af844101e1593afb 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e9a846fa67a615b34254c6cc6fc06912 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7ee00f7a5c677aabc22a60bf39be3681 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=73821ba39d63f4a511f571c3f6353ac4 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0a1b0fafef7df29475bfbd44efcd06a3 2500w" />
  </Step>

  <Step title="Add Segment in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Segment**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=15a5d94a542b9074e18bf200613df52c" data-og-width="3160" width="3160" data-og-height="2036" height="2036" data-path="images/integrations/segment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b372f84acf63933f73b99946fd5c60d1 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=60e74e8a80fbd827ec58e9522c5c3f45 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7e1ef4f3354da4f62617489b4585047e 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac150e42e3b3a0361afb8d1829804b00 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6357afa214216430b3ef6c1b043f1d9c 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3f1c04a320032462800ced06002a1bdd 2500w" />

    You will be asked to enter your Segment write key. Click **Connect** to save the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>
</Steps>
