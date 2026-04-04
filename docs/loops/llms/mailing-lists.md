# Source: https://loops.so/docs/contacts/mailing-lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List management

> Organise contacts and offer a subscriber preference center with mailing lists.

Mailing lists are useful when you want to organise contacts in more public groups and when you want contacts to be able to opt in and out of specific lists.

Using Lists will automatically generate a branded Preference Center for contacts in your audience, allowing them to easily manage their subscription preferences.

Lists can be public or private and contacts can belong to many, one, or no lists.

For organising contacts for your own use, we suggest using [filters and segments](/contacts/filters-segments) instead.

<Tip>
  Lists are an optional feature. You can use Loops without lists but if you'd
  like finer-grained control over your contacts and the types of communication
  they receive, lists are available on any plan tier.
</Tip>

## List types

Each list you create can be **Public** or **Private**.

By default lists are private, meaning they are only shown to their subscribed contacts (non-subscribers won't be able to see or subscribe to private lists in the Preference Center).

If you want to allow general opt-in to a list, you can set the list visibility to `Public`. Public lists will be shown to all contacts in the Preference Center.

You can also sign up new subscribers to public lists with [Forms](/forms).

<Note>
  Both private and public lists are visible within your Loops admin and can be
  used for filtering contacts when sending campaigns and loops.
</Note>

## Preference Center

The Preference Center allows your contacts to manage their own subscription preferences.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=cf719759d833e3e94d0e0a5a9fd36130" alt="Preference Center" data-og-width="2280" width="2280" data-og-height="1673" height="1673" data-path="images/mailing-lists/preference-center.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=54f84b23175c139e84e220a29ad28f03 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8d8d0fd2ca57cbd0004859b28b19fb9d 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e62d3bed909ec7e446b91fe3c3dbb133 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=00361e18f79c6c4db9690839578a7b5f 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=28c7642f1271c5e5fcbc7d71c757ca94 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/preference-center.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=83cc6532f2acc5df75d487ac44f753eb 2500w" />

A link to the contact-specific Preference Center is automatically added to each marketing email sent from Loops. You can link to the Preference Center in MJML emails by using the `{unsubscribe_link}` [dynamic tag](/creating-emails/personalizing-emails#dynamic-tag-syntax).

You can upload a company icon to brand your Preference Center. This option is shown just below your mailing lists in the [Lists settings page](https://app.loops.so/settings?page=lists).

<Tip>
  You can brand your unsubscribe page with a company icon even if you do not use
  the lists features.
</Tip>

Within the Preference Center, contacts will see:

* your company icon (if uploaded)
* the names and descriptions of all public lists
* the names and descriptions of all private lists they are subscribed to
* the option to unsubscribe from each list they are subscribed to

## Email footers

When sending campaigns and loops emails to specific lists, the [email footer](/creating-emails/editor#footer-content) will include the name of the list the email was sent to. This is useful for contacts to see which list the email was sent to, as well as unsubscribe from a certain list.

<img src="https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=9b9508a973cb272cf103cf5b42cc0e36" alt="Mailing list in the email footer" data-og-width="2280" width="2280" data-og-height="830" height="830" data-path="images/mailing-lists/mailing-list-footer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=280&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=3d54a455106056b445b35a42a4e939dc 280w, https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=560&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=2e818ee06e660e2c5bbd10f91d02b6bf 560w, https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=840&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=751c99a64acc516b0a17d865c39e8635 840w, https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=1100&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=0a103204e915ca08e8ff79ae2b0b01d6 1100w, https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=1650&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=2b089933b0195c6ad406ebfd8b76dce5 1650w, https://mintcdn.com/loops/iUrWW0OJWaMuDi53/images/mailing-lists/mailing-list-footer.png?w=2500&fit=max&auto=format&n=iUrWW0OJWaMuDi53&q=85&s=73691d799482d107644b89b46a97466f 2500w" />

## Create a list

Go to [Settings -> Lists](https://app.loops.so/settings?page=lists).

<Steps>
  <Step title="Create">
    Click on the **Create a list** button.

        <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b7952371789ad1a52a4a6fedfc07568d" alt="Create a new list" data-og-width="2280" width="2280" data-og-height="1332" height="1332" data-path="images/mailing-lists/create-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=12eed83beb5bb0941b4676dc86464fb3 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f9061adede12e87257c1492a7e691fe4 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=42ac8153b6bdac11311f2a2a862c77b8 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=bc308c4b7202be509eb8f40ad15e012a 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=64f8c1b0f0287390584be51f5163a48b 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/create-list.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=cb4124091a90b1f6e916b96375537580 2500w" />

    A new mailing list will appear. Enter a name for your list and optionally, a description.

    You can also choose a color to easily identify the list inside your Loops account.
  </Step>

  <Step title="Set visibility">
    <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6e8284ce89c7c91a7f5d9460e31f32ad" alt="Visibility toggle" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/mailing-lists/lists-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=69937b91710bda3e290297a9d6e5b932 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=2bf89665e64795c1a9fb056da73681dc 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4e61d93072b68e3fe480ce9967225498 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9482d7889fb99612f28a44c817a3fffb 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=974096be4984b6310992468a993c9049 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f4a60fa8fcf76668baa23d4ef88a098c 2500w" />
    Choose between `Private` or `Public` ([see above](#list-types)).
  </Step>

  <Step title="Save">
    Click **Save changes** to finalize the creation of the list.
  </Step>
</Steps>

## Edit a list

To edit an existing list, go to [Settings -> Lists](https://app.loops.so/settings?page=lists).

Edit the name, description, visibility and color.

Click **Save changes** to apply the changes.

<Note>
  After saving your changes, the updated list data will be instantly available
  to your contacts in their Preference Centers.
</Note>

## Delete a list

You can delete lists by clicking on a list's `•••` menu icon and selecting **Delete**.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=47bd285087095cc2b7efed2fc442d997" alt="Delete list" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/mailing-lists/delete-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ad629e2ec6200e1f336afc34d6f58dbf 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ff6504b6346c6498b88f2505b6ff895b 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=286e4d2b54a5f113e47e019f3e19eda2 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a494928efb95aa0e0832edde253489ae 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c4063796b4d983327e863c3c51787e72 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/delete-list.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9230ae14939f032bdfddb9977d96cb63 2500w" />

You cannot delete a list that:

* has been [sent a campaign](#send-campaigns-to-a-list), or has a sending or draft campaign
* is selected in the "Contact added to list" trigger [in a loop](#trigger-a-loop-when-a-contact-is-added-to-a-list)
* has been [applied to a loop](#send-loops-to-a-list)
* is being used in a [form](/forms)

Lists that cannot be deleted will show an "In use" badge. Hover over the badge to see a list of the campaigns, loops and forms that are stopping the list from being deleted.

## Utilizing lists

Here are a few ways you can use lists to send emails and organise contacts.

### Send campaigns to a list

Instead of sending campaigns to your whole audience, you can send emails to a specific list.

<Steps>
  <Step title="Choose a campaign">
    [Create a campaign](https://app.loops.so/campaigns) or edit an existing one.
  </Step>

  <Step title="Select the list">
    On the [Audience page](https://app.loops.so/audience), select the list you want to send to.

        <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1c7b4a93cbfb887681d919d541cb75ac" alt="Select a mailing list" data-og-width="2280" width="2280" data-og-height="822" height="822" data-path="images/mailing-lists/campaign-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=987afc3bb93e5dd4e518923ffbb30335 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=82ab7a4d27443098418d27b09b1a05ce 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ddebb97faf8e4060f9981a04d597adbc 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0dfaee4c6a2f0becb8bbc76b0459cc64 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=58d1111bf5a8ea84987ff5b0e5422bd2 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/campaign-list.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=2ce7720065a2b1c1ab5a22bb9954bedc 2500w" />

    Users not subscribed to the selected list will not receive the campaign.
  </Step>

  <Step title="Apply additional filters">
    Optionally, you can apply additional [filters or segments](/contacts/filters-segments) to further refine your audience.
  </Step>
</Steps>

### Send loops to a list

You can configure loops to only send to contacts in a specific list (this applies to all triggers).

<Steps>
  <Step title="Choose a loop">
    [Create a loop](/loop-builder) or edit an existing one.
  </Step>

  <Step title="Select the list">
    Select the list you want to trigger the loop. <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=de793fd41330f4a5b8f37bc1e1ed7e19" alt="Select the
    list" data-og-width="2280" width="2280" data-og-height="629" height="629" data-path="images/mailing-lists/select-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=51e65dc69cc136551244cd1c3969500a 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=003a97ba60189d7c670893da2764df39 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f783ab9022eadd514438e13043da44f1 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=5562e3020301284fed6642bdcbe2c28e 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8fa96216dc1ca85d0e559a3c0714d44c 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/select-list.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=85fb6e50a8569606b182dab29fefc24e 2500w" />
  </Step>

  <Step title="Start the loop">
    Start the loop. Only contacts from the selected list will be entered into
    the loop.
  </Step>
</Steps>

### Trigger a loop when a contact is added to a list

This example is a typical use case of sending an email sequence to new contacts when they are added to a specific list.

<Steps>
  <Step title="Choose a loop">
    [Create a loop](/loop-builder) or edit an existing one.
  </Step>

  <Step title="Set the trigger">
    Set the Loop trigger to "Contact added to list".
  </Step>

  <Step title="Select the list">
    Select the list you want to trigger the loop. <img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c11112f223f7e2d248b78f6a7d5e973d" alt="Select
    trigger" data-og-width="2280" width="2280" data-og-height="1427" height="1427" data-path="images/mailing-lists/set-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=91eeb6f2988b4d8f50c4dab868bfeb82 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=d710c6c665342ddd650ff7b619d6849a 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=faa236e8e66eab033ce1724e5cd35780 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0eab82562a746c1203ab75c4c017f398 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ee92b8fd19caa122da61c6c88883744d 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/mailing-lists/set-trigger.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=891d92916570cf12062a2b1f11ffbd24 2500w" />
  </Step>

  <Step title="Start the loop">
    Start the loop. When a contact is added to the selected list, the loop will
    be triggered.
  </Step>
</Steps>

### Manually add contacts to lists

How to add existing contacts to your different mailing lists within Loops.

<Warning>
  You cannot add contacts to mailing lists if they are unsubscribed from your audience.\
  Likewise, if a contact unsubscribes from a list via the
  Preference Center, they cannot be resubscribed by your team.
</Warning>

#### Individual contacts

<Steps>
  <Step title="Go to Contacts">
    Go to your [Audience page](https://app.loops.so/audience).
  </Step>

  <Step title="Select a contact">Click on the contact you want to manage.</Step>

  <Step title="Manage subscriptions">
    In the contact details page, click on **Subscribed** to reveal the mailing
    list dropdown.
    <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f4447232b13e743e0208a4b1c34c74af" alt="Manage subscriptions" data-og-width="2280" width="2280" data-og-height="909" height="909" data-path="images/mailing-lists/manage-contact-subscriptions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=417595f8d295f80316cb3af197c65d16 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=300fd89ccb270adf9a13c76bb29e4590 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3d51ed2f9486fa9a7b03c83b83d807ce 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ec360ea0c95fc65df23924b0445311a5 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ae10029bb8634ad0837c2cc22392a0f9 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/manage-contact-subscriptions.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ab68abf583ffe75eff5f4ded6151ecf4 2500w" />
    Toggle each list on or off as needed. Click **Save changes** in the top
    right to apply the changes.
  </Step>
</Steps>

#### Bulk contacts

You can easily add any filtered group of contacts to a specific list on the Audience page.

<Steps>
  <Step title="Go to Audience">
    Go to your [Audience page](https://app.loops.so/audience).
  </Step>

  <Step title="Filter your audience">
    Add filters to segment your audience into the group of contacts you'd like
    to add to a list.
  </Step>

  <Step title="Add contacts to a list">
    Click the `•••` menu icon on the far right-hand side of the audience
    filters, select **Add to mailing list** and then select the list(s) you want
    to add the contacts to. <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=eec10551d5edc79f977a762bf7d23930" alt="Add to
    list" data-og-width="2280" width="2280" data-og-height="1080" height="1080" data-path="images/mailing-lists/bulk-assign-to-lists.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=acd4abdceac46dbc01d8f31d03d81188 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d064c383262a24865d8113d2c04dd829 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9afba87a2a02cf1848dc9f45eae89d37 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c39d61ecb46de29ed6f78d881d4d5137 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0912588dd8abf41b397777368d9421d7 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/bulk-assign-to-lists.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=dd068888e6474c03e27e4ed58e548f70 2500w" />
  </Step>
</Steps>

### Upload a CSV to a list

If you want to import contacts to a list in bulk you can use our [CSV importer](/add-users/csv-upload).

In the final stage of the form you can select a list, which will add all contacts (new or existing) in the CSV file to that list.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=55ae51a5859674615f2f6ba81f3fb40d" alt="" data-og-width="2280" width="2280" data-og-height="1059" height="1059" data-path="images/mailing-lists/csv-upload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a1b8e984c1a785edb32b477ca35d7487 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=12ed8d7706956426c1fbc766823741f9 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=345a813d2943c0f825300b79d0a578a6 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=72d74ccb6869fa7b57f291e7ccae2dfd 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8cfbba1c39838f635a25de76213bbaf5 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/csv-upload.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6a92dc326c32ab7245570f17ad391df0 2500w" />

### Add contacts to lists with the API

Utilizing the [Loops API](/api-reference) you can programmatically add and remove contacts to and from Lists.

<Warning>
  You cannot add contacts to mailing lists if they are unsubscribed from your audience.\
  Likewise, if a contact unsubscribes from a list via the
  Preference Center, they cannot be resubscribed by your team.
</Warning>

When [creating a contact](/api-reference/create-contact), [updating a contact](/api-reference/update-contact), or [sending an event](/api-reference/send-event) with the API, you can include a `mailingLists` object in the payload.

This `mailingLists` object is a key-value pair of list IDs and a subscription status. The subscription status can be `true` or `false`.

```json  theme={"dark"}
{
  "email": "loopy-loop@example.com",
  "mailingLists": {
    "cm06f5v0e45nf0ml5754o9cix": true,
    "cm16k73gq014h0mmj5b6jdi9r": false
  }
}
```

In this example, the contact would be subscribed to `cm06f5v0e45nf0ml5754o9cix` and unsubscribed from `cm16k73gq014h0mmj5b6jdi9r`.

Mailing list IDs can be found [in the app](https://app.loops.so/settings?page=lists) (click the ID to add it to your clipboard) or by using the [API](/api-reference/list-mailing-lists).

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6e8284ce89c7c91a7f5d9460e31f32ad" alt="Visibility toggle" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/mailing-lists/lists-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=69937b91710bda3e290297a9d6e5b932 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=2bf89665e64795c1a9fb056da73681dc 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4e61d93072b68e3fe480ce9967225498 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9482d7889fb99612f28a44c817a3fffb 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=974096be4984b6310992468a993c9049 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/lists-toggle.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f4a60fa8fcf76668baa23d4ef88a098c 2500w" />

### Add contacts to lists with forms

If you use a [form](/forms/simple-form) on your website you can subscribe contacts to specific lists.

When exporting HTML from the [Forms page](https://app.loops.so/forms) in Loops, choose a list from the **Settings** tab.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=eeb0bd57ca9ec2627db111c6c9becf13" alt="Select a list from the form settings" data-og-width="2280" width="2280" data-og-height="1118" height="1118" data-path="images/mailing-lists/form-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1b374aa83397f8b06896fd10b82c8bd5 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9a2001cd9c103a9c7f4552b2a55f0578 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a5dff6cc70281a41bbd2ba567edb0408 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ee956ffaea247fb28316bbff530f2b04 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=25f67dd16bd1078bafa9041f80309ff7 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/mailing-lists/form-settings.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1590b82d032ef3b144faa9af3ff1007d 2500w" />

<Note>
  Adding contacts to a list via a form only works with public lists. The option
  to select a list will only appear in the form settings if you have at least
  one public list.
</Note>

If you already have a form in place or are using a [custom form](/forms/custom-form) you can add a `mailingLists` parameter to the form body with the value a comma-separated list of mailing list IDs.

<CodeGroup>
  ```html HTML example {3} theme={"dark"}
  <form>
    <input type="email" name="email" required />
    <input type="hidden" name="mailingLists" value="cm06f5v0e45nf0ml5754o9cix,cm16k73gq014h0mmj5b6jdi9r" />
  </form>
  ```

  ```javascript JavaScript example {4} theme={"dark"}
  fetch(formEndpointUrl, {
    method: "POST",
    body:
      "mailingLists=cm06f5v0e45nf0ml5754o9cix,cm16k73gq014h0mmj5b6jdi9r" +
      "&email=" + encodeURIComponent(emailInput.value),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  ```
</CodeGroup>
