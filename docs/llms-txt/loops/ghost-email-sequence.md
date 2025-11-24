# Source: https://loops.so/docs/guides/ghost-email-sequence.md

# Set up a welcome email sequence for new Ghost members

> Send automated email sequences to new Ghost subscribers using Zapier and Loops.

This guide helps you set up email sequences that get sent to all new subscribers to your Ghost site.

With Loops, you can set up sophisticated sequences called "[loops](/loop-builder)", allowing you to send a range of welcome emails to your members over a period of time.

Using [Zapier](https://zapier.com), we can automatically add every new member who signs up on your Ghost site to your Loops audience.

## Set up the Zapier Trigger

The first step is to connect your Ghost site to Loops using Zapier.

Sign up to Zapier and create a new Zap using Ghost's **Member Created** Trigger.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a4065f83654edae063dbf52907024c92" alt="Add Ghost trigger" data-og-width="2280" width="2280" data-og-height="1221" height="1221" data-path="images/zapier-ghost-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=b756111e90a94d24fda212530c3c6145 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=71802b8c498076c69b3006ee2d62a7c8 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=71a70a491d255ba90077f3246d2bd520 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=479d9fd9b7329823c78a2af6d1f80711 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f5bc879ca09959a0a29f715502cb069c 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-trigger.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a829236ce86db983c76ea68eb5da07e2 2500w" />

This creates an automation that will trigger every time a new member is created in Ghost. Zapier will then send the contact's information over to Loops.

Now connect Ghost from the Trigger by clicking **Account** then **Sign in** and then pasting in your Ghost API key and API URL. To find these, go to Settings in your Ghost admin, search for "Integrations" and click on **Zapier**.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=75eac779a122ec0f687c04ed8fdcc0ac" alt="Sign in to Ghost" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/zapier-sign-in-ghost.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=239cd26ee5846f037e5bd127add1a232 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=d82ffede642c0f0d14fe8ea0f5a69c82 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=ed05c37406e586b9ad0c4aec1291bf62 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f35ff9a36753ff6355096b714a1844b6 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=eadc362bec392651e01ce0cd69030beb 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-ghost.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=31a1d7e21db37b92ec3acdac5250174b 2500w" />

## Set up the Zapier Action

Next you need to link up Loops as the Action. Click the **Action** node, search for Loops and select the **Send Event** option in the Event dropdown.

Click **Continue**, then **Sign in** and paste in your Loops API key (which you can find from your [API Settings page](https://app.loops.so/settings?page=api)).

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=57d92c4753c574e79e46bb270d02386c" alt="Sign in to Loops" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/zapier-sign-in-loops.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=4629ee6674e5fe86dddec4cf02b9d893 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=98685da373144a21943bd707f9a8e4fa 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=4a7188fb83a430c35a7201a62b862b2d 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e01eca081bfc93d6573aa9d0e79451bd 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=2837614807c1e00506a74ad1b4ba6b2b 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-sign-in-loops.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=31b3c4a2e996f630003494bc21edf2a3 2500w" />

<Tip>
  Instead of using an event for the loop trigger, you could also choose to send the loop to every new contact created in your audience.\
  We choose the event trigger in this example as you may add other contacts to your audience from other sources than Ghost.
</Tip>

Now click **Continue** to move to the **Action** tab. This is where you can configure which Ghost data is sent to Loops.

As you click each field, you can select the different Ghost-provided data.

In **Email**, select the Email field. In **User ID**, select the ID field.

In the **Event Name** field, write something like `newMember`. This is the name we'll use in Loops to trigger the email sequence. You can use any name, but make it descriptive. You'll need this name in the next step inside Loops.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=ed607ea08137b7a3c70e127f430d5e7a" alt="Adding an event name" data-og-width="2280" width="2280" data-og-height="1604" height="1604" data-path="images/zapier-ghost-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=cc294fd0c083ff471b01df68a651b475 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=c72178015bd327b4ba0f3072e7e72e6b 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=330a36298c0b20b39703f90727d56112 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=54672a6d616b697ce8c650b8d7d746a1 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=c9999942e67f66c2af4a4008c48c0641 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-email.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=df921a6d499c1106c8a6d14138eb80ec 2500w" />

If you want to include contact-related information in your emails you can use [event properties](/events/properties). To do this, add more Ghost data in the **Event Properties** field. For example, if you want to include the user's name, subscribed status, member status or your newsletter's name, you can add these properties here. Click the `+` button to add new properties each time.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=8f6bbb28e56215563b9fe002ade48369" alt="Adding event properties" data-og-width="2280" width="2280" data-og-height="1581" height="1581" data-path="images/zapier-ghost-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=33991b6a1ec86e6c32ed97725116bce9 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=7e1c7cc6c6c27556f497f8a871a65960 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=39299f7b5d0c82a4d699389139f3eeca 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=97e5bcba9dffe3205ca3d19656c1fb42 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=375104cac73ba187b013a708a1725b07 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/zapier-ghost-properties.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=5ad20b197df92338e4a6db7726ae58ea 2500w" />

Click **Continue** to see an overview of the event and its data that you'll send to Loops. Here you can test the action works by clicking **Test Step**. This will send actual data to Loops, which you will see in the Event Log section on the [Events page](https://app.loops.so/settings?page=events).

When you're happy everything is set up properly, click **Publish**.

<Tip>
  If you ever change the event properties sent from Zapier, you need to update the event data in Loops to match. You can do this from [Settings -> Events](https://app.loops.so/settings?page=events). Click on the event and edit the listed properties. [More info](/events/properties#editing-event-properties)
</Tip>

## Create an email sequence

Now that the connections are set up, you can create the email sequence "loop" in Loops.

Go to Loops and click on **Loops** in the sidebar.

Click **New**, which will create a new loop and show the [loop builder](/loop-builder).

Select the **Event is fired** trigger option.

Click on the **Event received** trigger in the loop builder and enter the name you entered in Zapier in the previous step (in this example, `newMember`).

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9095164e936346f76239ffdd0b92ff57" alt="Select the event trigger" data-og-width="2280" width="2280" data-og-height="1893" height="1893" data-path="images/member-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f30c42c1374a412e82f2ce0494636c0e 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5d92a81f9ca5faf23f0f7ec0890a0e34 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=67e6c9233f740e9e9244ecd38c3011d4 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e0dc26d9e2de1ec4eaae75afd34b261d 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c45f855b9835900b2e29243686f407e3 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/member-trigger.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ec2e14a0936595958f6e0c0e37213d39 2500w" />

You can edit the **Timer** node if you want to add a delay between the event being received by Loops and the email being sent to your Ghost members.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=df736d0a34d27cfa70bd42a5109cf2d1" alt="Set a timer delay" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/timer-3-days.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=68a68605d04f63bcb471d659c1540509 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=aef3495dc1be1601336bc41dd27bcc59 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e78a77a3aeee5c0f213289dbd62e4676 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=9fbf79e8767c796ccdd899f82ae04608 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e2f35b63251a0de08b55675627ce9512 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/timer-3-days.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=fa6f7ee24d417ad3e05a6ed828ed2502 2500w" />

You can also add a filter to the audience for this loop, if you want to limit sending to a certain sub-group of your members. If you want the loop to send to all new Ghost members, just leave it as "All contacts".

Lastly, click the **Send email** node and then **Create email**. You'll see the [email editor](/creating-emails/editor) open, where you can create your email.

If you opted to send event properties from Zapier, you can add them to your email by clicking the `⚡️` button above the editor (1) and then configuring in the **Event Property** editor panel (2).

<img src="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=fb1eb41c4043168c67219248413abf68" alt="Adding event properties in the editor" data-og-width="2280" width="2280" data-og-height="1596" height="1596" data-path="images/scheduled-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=280&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=1ef06da3b015974424b33b606fcbea9e 280w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=560&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=09f2cd64215e8a41434f9eb793ef2763 560w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=840&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=5383aa9d6e0f65363495d715799e3203 840w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=1100&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=b90362052ff0d7b02bbdf69483e8aa1a 1100w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=1650&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=8f8e5fd8e214b51792467e6fd3ab6c73 1650w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=2500&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=13502dc0a70bf1a57382741b897e1ede 2500w" />

Once your first email is complete, you can add more Timer and Email nodes to your loop to complete your email sequence. Just click on the `+` icon between nodes to add new ones.

## Learn more

<CardGroup columns="2">
  <Card title="Loop Builder" icon="arrows-rotate" href="/loop-builder">
    Read more about triggering emails with events.
  </Card>

  <Card title="Creating emails in the editor" icon="keyboard" href="/creating-emails/editor">
    Learn how to create stylized emails and add personalization.
  </Card>

  <Card
    title="Zapier"
    icon={
    <svg
      viewBox="0 0 256 256"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlnsXlink="http://www.w3.org/1999/xlink"
    >
      <g>
        <path
          d="M128.080089,-0.000183105 C135.311053,0.0131003068 142.422517,0.624138494 149.335663,1.77979593 L149.335663,1.77979593 L149.335663,76.2997796 L202.166953,23.6044907 C208.002065,27.7488446 213.460883,32.3582023 218.507811,37.3926715 C223.557281,42.4271407 228.192318,47.8867213 232.346817,53.7047992 L232.346817,53.7047992 L179.512985,106.400063 L254.227854,106.400063 C255.387249,113.29414 256,120.36111 256,127.587243 L256,127.587243 L256,127.759881 C256,134.986013 255.387249,142.066204 254.227854,148.960282 L254.227854,148.960282 L179.500273,148.960282 L232.346817,201.642324 C228.192318,207.460402 223.557281,212.919983 218.523066,217.954452 L218.523066,217.954452 L218.507811,217.954452 C213.460883,222.988921 208.002065,227.6115 202.182208,231.742607 L202.182208,231.742607 L149.335663,179.04709 L149.335663,253.5672 C142.435229,254.723036 135.323765,255.333244 128.092802,255.348499 L128.092802,255.348499 L127.907197,255.348499 C120.673691,255.333244 113.590195,254.723036 106.677048,253.5672 L106.677048,253.5672 L106.677048,179.04709 L53.8457596,231.742607 C42.1780766,223.466917 31.977435,213.278734 23.6658953,201.642324 L23.6658953,201.642324 L76.4997269,148.960282 L1.78485803,148.960282 C0.612750404,142.052729 0,134.946095 0,127.719963 L0,127.719963 L0,127.349037 C0.0121454869,125.473817 0.134939797,123.182933 0.311311815,120.812834 L0.36577283,120.099764 C0.887996182,113.428547 1.78485803,106.400063 1.78485803,106.400063 L1.78485803,106.400063 L76.4997269,106.400063 L23.6658953,53.7047992 C27.8076812,47.8867213 32.4300059,42.4403618 37.4769335,37.4193681 L37.4769335,37.4193681 L37.5023588,37.3926715 C42.5391163,32.3582023 48.0106469,27.7488446 53.8457596,23.6044907 L53.8457596,23.6044907 L106.677048,76.2997796 L106.677048,1.77979593 C113.590195,0.624138494 120.688946,0.0131003068 127.932622,-0.000183105 L127.932622,-0.000183105 L128.080089,-0.000183105 Z M128.067377,95.7600714 L127.945335,95.7600714 C118.436262,95.7600714 109.32891,97.5001809 100.910584,100.661566 C97.7553011,109.043534 96.0085811,118.129275 95.9958684,127.613685 L95.9958684,127.733184 C96.0085811,137.217594 97.7553011,146.303589 100.923296,154.685303 C109.32891,157.846943 118.436262,159.587052 127.945335,159.587052 L128.067377,159.587052 C137.576449,159.587052 146.683802,157.846943 155.089415,154.685303 C158.257411,146.290368 160.004131,137.217594 160.004131,127.733184 L160.004131,127.613685 C160.004131,118.129275 158.257411,109.043534 155.089415,100.661566 C146.683802,97.5001809 137.576449,95.7600714 128.067377,95.7600714 Z"
          fill="#FF4A00"
          fillRule="nonzero"
        ></path>
      </g>
    </svg>
  }
    href="/integrations/zapier"
  >
    Manage contacts and send emails from thousands of other platforms.
  </Card>
</CardGroup>
