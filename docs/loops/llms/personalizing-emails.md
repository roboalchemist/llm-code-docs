# Source: https://loops.so/docs/creating-emails/personalizing-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Personalizing emails

> Add context and personalization to emails.

Every email you send from Loops can contain dynamic content connected to the contact you're sending to or the event that triggered the email.

A common example of using dynamic content is to personalize an email greeting by using a contact's first name, or by including a customer's plan details in a subscription reminder.

## Types of dynamic content

The three [email types](/types-of-emails) in Loops have different dynamic content available to them:

* **Campaign emails** can contain **contact properties**.
* **Emails within Loops** can contain **contact properties** and **event properties**.
* **Transactional emails** can contain **data variables**.

The three types of dynamic content are:

* **Contact properties** are pieces of data related to each [contact](/contacts/properties) in your audience. There are a set of default properties like name and source, but you can also add any number of custom contact properties. If you sync contact data to Loops with the API, an integration or with CSV uploads, you can include that data in your email.
* **Event properties** are pieces of data that can be sent along with every [event](/events) (which are used to trigger loop emails) via integrations or API calls.
* **Data variables** are pieces of data included in [transactional emails](/transactional), which are populated in the API call. You can utilize [optional data variables](/transactional#optional-data-variables) to make your transactional emails more dynamic.

## Add dynamic content to emails

<Warning>
  If you want to add dynamic content to a [custom MJML
  email](/creating-emails/uploading-custom-email), check the [Dynamic tag
  syntax](#dynamic-tag-syntax) section below.
</Warning>

To add dynamic content to your emails, type "\{" anywhere in the editor or click the `{}` dynamic content icon in the email editor toolbar. Using either of these options will open the dynamic content menu, a filterable list of all available properties you can insert.

<img src="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=27c73e902ab6b876bc16065bd09134aa" alt="Dynamic content menu appearing after typing the opening brace" data-og-width="2280" width="2280" data-og-height="1532" height="1532" data-path="images/brace-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=280&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=9326c62f97de7ca37bfb6c4dffc72710 280w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=560&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=af2601f9d01a08e404831c2a893c3c12 560w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=840&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=0866e9e7523a4a775fc6eda747d79288 840w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=1100&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=9234e4574c66ff73ac822d6a99a3affb 1100w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=1650&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=f066015663842e0fc26e5bc0e46b5b6f 1650w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu.png?w=2500&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=8f5f1e9f81626bf456c0f5ad49e03d65 2500w" />
<img src="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=50f73381c384e4ff6ed919d81630cbe9" alt="Adding a contact property" data-og-width="2280" width="2280" data-og-height="1035" height="1035" data-path="images/basic-merge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=280&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=18814146da18de5f13e391fa12a20c0e 280w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=560&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=11778fb9f17dcc74d2d8cc3862188dd0 560w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=840&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=1d9873614099f8e8a8bf03a6737d6784 840w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=1100&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=2edecb2194d57f86bc98b4f265381631 1100w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=1650&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=f516cbbf3856e25d5583034ff6b9319c 1650w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=2500&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=1e7b6b3fcaf7193246b46cbfe703f4d2 2500w" />

These two options are also available in all of the sending setting fields above the editor. An icon appears on the right when you hover over each field, or you can start typing "\{".

<img src="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=37b70af55b0d61afc08c872745d1b9e2" alt="Adding a contact property to sending details" data-og-width="2280" width="2280" data-og-height="782" height="782" data-path="images/sending-setting-dynamic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=280&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=6088b36fcf1e713c869e055cf147b33a 280w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=560&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=db4539b239ee71d4a106fc64580b4374 560w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=840&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=ab4f65f5e9c0533896fc23c99cf74af3 840w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=1100&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=4ea5e673494eec2d5f88062da328bdfc 1100w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=1650&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=5fa462779d862577d2cc532b8bc1ed90 1650w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/sending-setting-dynamic.png?w=2500&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=60fd0559b6f494ad8450565b5ba84459 2500w" />

Depending on whether you're editing a campaign, loop or transactional email, the menu shows different content based on your email type (explained above).

To use the dynamic content menu

1. Type `{` or hit the `{}` icon in any editor field
2. Continue typing to filter results: `{fir` shows "firstName"
3. Use `↑/↓` to navigate, `Enter` to select, `Escape` to close

When the email is sent, the dynamic content will be replaced with actual values from the contact, event or data variable.

Once you've selected something from the menu in a campaign or loop email, you will be prompted to enter a fallback value. This ensures emails still send even when data is missing.

<Tip>
  If you send an email and the dynamic content is missing a value, the email
  will not be sent. Make sure to add fallback values to avoid missed sends.
  [Read more below](#fallback-values).
</Tip>

## Fallback values

Fallback values are important for campaign and loop emails. If a contact doesn't have a value for a property, or an event property is missing, the email won't send.

When you insert a contact or event property using the dynamic content menu, you'll be prompted to enter a fallback. This default text ensures your email still sends even when data is missing.

<img src="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=14a23c9ea6f430b1403f18ed8cc3d2d8" alt="Fallback input appearing after selecting a property" data-og-width="2280" width="2280" data-og-height="1022" height="1022" data-path="images/brace-menu-fallback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=280&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=e08b96ac8d5163eeea9af6de694b658a 280w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=560&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=dcd410fc43511f6219516a7a2cf4f272 560w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=840&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=b5712f25c8d4ba12d39f741e69bd8754 840w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=1100&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=21325639147d7e986ce23ab4b3504a44 1100w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=1650&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=79d59203e2c483fdacdc3d465ebe12ad 1650w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-fallback.png?w=2500&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=8762cb1d91e21721196a2e1e0a3d5bc3 2500w" />

Common fallback examples:

| Example                    | Fallback     | Result                  |
| :------------------------- | :----------- | :---------------------- |
| Hey `{firstName}`          | there        | Hey there               |
| Welcome to `{companyName}` | your company | Welcome to your company |

This keeps your emails feeling personalized even when specific data isn't available.

Your fallback is saved and will auto-fill if you insert the same property again.

You can edit the fallback value later on from the editor panel.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=4b91e6489b2078ab1781baad90f79aac" alt="" data-og-width="2280" width="2280" data-og-height="1206" height="1206" data-path="images/fallback-variable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=50b412565789d33c35b45d66a86b891b 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=3766af743187e7fc8ff71e146c0532b4 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=35ddfb6cd9a1f9301f0a5aadd1a6929b 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=779f04210710adbe3a58aaed73e7afff 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=527451499c851ca38443b73bbda2a21d 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/fallback-variable.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a9516ad14f895bc61203394aacc55c61 2500w" />

## Data variables in transactional emails

In transactional emails, dynamic tags work slightly differently: you can create new data variables in your email as you type.

<img src="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=88c2687bfef5c47a5aee0a27a5a15e97" alt="Creating a new data variable with the dynamic content menu" data-og-width="2280" width="2280" data-og-height="1217" height="1217" data-path="images/brace-menu-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=280&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=58ac79702032bb4f41e97b6dce0b9fd1 280w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=560&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=2a8e2868c31996f9fc364103f611c12e 560w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=840&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=d200cf3d7528ee3c75e3e1177ff238be 840w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=1100&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=d30a28c50dbefd5d8810e7187a217ac7 1100w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=1650&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=46e4115ba3039aac4035bdc7b9fe6e4b 1650w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/brace-menu-variables.png?w=2500&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=987497422bbb9687b0d6a70367e266a4 2500w" />

1. Type `{orderTotal` (using a new name that doesn't exist).
2. Select **Create "orderTotal"** from the menu or press `Enter`.
3. The variable is created and you can edit it from the editor panel (change the name or change to an [optional variable](/transactional#optional-data-variables)).

## Dynamic tag syntax

As well as using the dynamic content menu, you can write dynamic content "tags" directly in the email body. This is especially useful when [uploading custom emails](/creating-emails/uploading-custom-email).

These tags are the only way to add dynamic content in [custom MJML emails](/creating-emails/uploading-custom-email).

### Contact properties

If you have a custom contact property named `teamName` that you want to add to a campaign, you can write it surrounded by curly brackets in the email:

```
{teamName}
```

When the email is sent, the `teamName` value for each contact will be added to the email.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1362c358de9832b19a7d84d9ba1db93a" alt="" data-og-width="2280" width="2280" data-og-height="830" height="830" data-path="images/merge-tag-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=edf17ec24a1f9739f90d7a4f708709c9 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b5e5f42dbc475292c399f57c3c2905f8 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=85588ebf9d0eadd50214a0bf164d8a96 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=810700b1a37df7b0a997163b8007e6b1 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2936ecb81ce7654397c9b79ecabfa7f2 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag-0.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=6ff2cebb9b2be2ca5aa3360da9bfdf5e 2500w" />

For a list of all of your contact properties, visit the [API Settings](https://app.loops.so/settings?page=api) page. The **API Name** is the name you use within the brackets in your email, for example `{firstName}`, `{lastName}`, `{email}`, etc.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c0581243e45c04d5f31d488bdee17632" alt="Contact properties table" data-og-width="2280" width="2280" data-og-height="1661" height="1661" data-path="images/merge-tag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=919fef61dcdf3796ef642d43c97f01f5 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b05f90401381a632b776179697eb71e7 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e8fb02e7dd793aa68fb0147c00fdfe36 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b5025738d6dc57556ecf70e05022cbca 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9883ab1e0cd3081bd13c216019b31306 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/merge-tag.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=6ac25923487f0e604a644280c07812ac 2500w" />

### Event properties

To add dynamic data to emails within loops using event properties, the tag requires an `EVENT_PROPERTY:` prefix:

```
{EVENT_PROPERTY:firstName}
```

### Data variables

To add data variables in transactional emails, the tag requires a `DATA_VARIABLE:` prefix:

```
{DATA_VARIABLE:firstName}
```

<Tip>
  It is important to use the right names in your tags, for example contact
  property names from [API settings](https://app.loops.so/settings?page=api) and
  event property names from the [Events
  settings](https://app.loops.so/settings?page=events) page. If you have any
  questions about how to format your tags, reach out to us!
</Tip>
