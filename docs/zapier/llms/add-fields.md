# Source: https://docs.zapier.com/platform/build/add-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add input fields to triggers and actions

> When building in the Platform UI, you'll use the Input Designer to create the form users will input data into, to send to your app's API.

The Input Designer works similarly to other form builder tools, building a form that lives inside the Platform UI. Add fields to your form for each bit of data your app needs from users. Use the same name for items as used in your app's UI. Configure each field's settings, then reorder them to match the logical order users would add or view data in your app.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=53af2bb246c983285df12df9d692f093" data-og-width="1194" width="1194" data-og-height="881" height="881" data-path="images/524b9300c044809eb13eb732d7a50f9d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=161054f9c705b011b1f6bbfc0a1ba21f 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c2b497d76f609b6746dcf5b82590849d 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=06df16a57648f0fc29cb44c92b196673 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=121ff5a88087dcc16f05d2a7f617ce74 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9c8a212301baedb4d8f7b27ee3c02da6 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/524b9300c044809eb13eb732d7a50f9d.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=907660a32928726fcb4954f906ff4bc7 2500w" />

  {" "}
</Frame>

Actions require an input form, as they always need a way for users to send data to your app's API to find, update, or create a new object. An input form is optional for triggers.

In this guide we will cover:

* Add an input field to a trigger or action
* Set field options
* Reorder input fields
* Remove input fields

## Add an input field to a trigger or action

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Build* section in the left sidebar, click on your **trigger** or **action**.
4. Click the **Input Designer** tab.
5. For triggers, click **Add User Input Field**. For actions, click **Add** and select **Input Field**.
6. In the Form editor, add in details about your input field:

* **Key**: A unique identifier for the field, without spaces, ideally with the same key as your API, such as `first_name`.
* **Label**: A user friendly name for the field, such as `First Name`.
* **Help Text**: (optional) A 20 character or longer description that appears under the field label, with [Markdown](https://zapier.com/blog/beginner-ultimate-guide-markdown/) formatting. Do not include redundant help text in input fields that repeats the name of the field. Use field help text to tell users what to do, for example “Choose the directory to watch for new files”. Always use active voice.
* **Type**: From the dropdown menu, select type of data you want user's to enter. Learn more in [field definitions and types](/platform/build/field-definitions):
  * String
  * Text
  * Integer
  * Number
  * Boolean
  * DateTime
  * Password
  * Dictionary
* **Default Text**: (optional) Value to include in the field if the user leaves it blank; only include if this value would work for API requests made to every user's account.
* **Options** (optional):
  * Select the **Required** checkbox to make it mandatory for users to add data into this input field.
  * Select **Allows Multiples** checkbox if you want users to add multiple enteries into the same input field.
  * Select **Alters Dynamic Fields** to have Zapier automatically recompute any dynamic fields any time this field is changed.
  * Select **Dropdown** 7. Once you've finished adding details for your input field, click **Save**.

## Setting field options

### Required

An email app like MailChimp requires an email address to add a new email subscription, and a calendar app like Google Calendar requires an event title, date, and time to add new events.

Check the *Required* option on those fields if your trigger or action step requires any data to make the API request. Zapier will show a red `(required)` label beside the field name in the Zap editor, and will not let users complete the Zap step without adding data to that field.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=d356c0f27a97db67d250c7dfa8ef71e7" data-og-width="1197" width="1197" data-og-height="130" height="130" data-path="images/f8d0fd74582dc7c5997248516ad50d4f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=737b237913aad346fa4211fa03478019 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=0c6eef365f77db31c6cb9c21e5a94cdc 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=49d1b0056849829e5ca4a46d35dd0f74 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a1476ead555a8b45db720d79334cd116 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a0bd3616462cb7e7ca66fc6c3c582758 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f8d0fd74582dc7c5997248516ad50d4f.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=00e21c7f260a4d21e7207f4d536c407f 2500w" />

  {" "}
</Frame>

Include a description on required fields to let users know exactly what type of data they should add to this field. Never mark fields as required if the integration could work without them.

### Allows multiples

If users could add multiple entries in the same field, check the *Allows Multiples* option.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e59bd33504a8edd9c7feb73048573a1d" data-og-width="1207" width="1207" data-og-height="194" height="194" data-path="images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=c58be0cb90e1aa285aab1d2c10864a6c 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7bc3ea5bc778edceee9dbfb69cc311f1 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d74004cf53886b4a2a6ac9c347bca16f 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3100e961e2e265401f01c9a8bf326e56 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8185fcd41cbf0385254df39549c6e86c 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4c2a6ad55c12f6e3079e50f5d38e6c.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=f64aa424b90c702814aa6873e4090d29 2500w" />

  {" "}
</Frame>

That will add another entry row to allow the user to input another entry for that field. An [array containing a comma separated list of entries](/images/95938b473edfee13663161ee3c8e5ea4.webp) is sent in the API request. Never ask users to type in a comma separated list, rather use this functionality.

### Alters dynamic fields

For each [dynamic field](/platform/build/dynamic-field) in your integration, Zapier runs code to decide whether to show a field or what to show in a field.

Check the *Alters Dynamic Fields* option, to have Zapier automatically recompute any dynamic fields in your Zapier integration anytime this field is changed. Do not check the *Alters Dynamic Fields* option unless the field is needed for your integrations' dynamic fields.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=bfaabf3eedbd28f78c1d98b5287c5752" data-og-width="1864" width="1864" data-og-height="230" height="230" data-path="images/f89ed93d7233d0473b435156b31a1a8a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=943e4b1948de205565a25e6360934793 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=35b997d4ed2c258668c8434ee46938a4 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=4ef300c72a51893a79691ce3de6a033a 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=92e32efc1c0f17e96c7b48c8c2f8b195 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=da47657e5f6225cfbf170056c58e948c 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f89ed93d7233d0473b435156b31a1a8a.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=8e50038c3d537903907cfc4ab013538a 2500w" />

  {" "}
</Frame>

Only dropdowns support *Alters Dynamic Fields*.

### Dropdown

#### Static Dropdown

To offer users pre-set options to choose from in a field, set your field type as `String`, then check the *Dropdown* option.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=141731b49bd37638fc7be93aae78b2de" data-og-width="1197" width="1197" data-og-height="609" height="609" data-path="images/4f65bd28634d7709cac0ba84f2fa73d3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=2b1e53d74e5bee0de2482bf910c39f11 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=500c6a457986accd52e36922932f2cc1 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d92282972abd15c5102d3ee641b81a1b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=61d198d528c056569c54ef88bd50fa05 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=630cb15e240473affacd2b6f4f90d9bc 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f65bd28634d7709cac0ba84f2fa73d3.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=89a58301d00c2c9a0cc1d54897e22b2c 2500w" />

  {" "}
</Frame>

You'll see the default *Static* selected, or *Dynamic*. To add a Static menu of choices, type the options in a comma separated list, with quotes around each item and square brackets around the set, such as:

`["one", "two","three"]`

Enter the fields as used in your API, as Zapier will pass the exact value users select to your app. Zapier will capitalize each item in your dropdown menu in the Zap Editor, and will add spaces instead of any underscores, so an option like `first_name` would show in the menu as `First Name` to users.

**Static Dropdown with Key Value Pairs**

If your API requires different values for the field than the text you want to show to users inside the dropdown menu in Zapier, make a key value pair that includes the value to send to your API, the sample value to show users ([should be the same as the value](https://github.com/zapier/zapier-platform/blob/master/packages/schema/docs/build/schema.md#fieldchoicewithlabelschema)), and a user-friendly label.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=fd8037a8df8f5258abe7c3faf7f7ed53" data-og-width="1187" width="1187" data-og-height="714" height="714" data-path="images/101618614c22bd4bd453c365db753db9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b9bfdb0c46d475c79e01900f784303dc 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=861bca6782362d70429e986351f2cba1 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=7bce78a4e07ec78f49f8f864680ffe19 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3904c3adc808f38f48c11dbbae9771f0 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=185825fb4a23a4007a9020e0ee9067bd 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/101618614c22bd4bd453c365db753db9.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=ffb5087fee491cbdd74db6add1f43697 2500w" />

  {" "}
</Frame>

To do that, add each menu item inside an object (curly brackets); with the sample, value, and label comma separated. List the item first and the value second, both wrapped in quotes. Separate each menu item with commas, and wrap the whole set in an array (square brackets).

For example, if your API expects a value of `1` or `2`, but `1` actually means `pork` and `2` actually means `fish` to a user, you could use the following code to add the dropdown menu pictured:

```JSON  theme={null}
[
  {
    "sample": "1",
    "value": "1",
    "label": "Pork"
  },
  {
    "sample": "2",
    "value": "2",
    "label": "Fish"
  }
]
```

Alternatively, you can also use the syntax of `value:label`, which shows to users as follows:

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=efe0445cc3a0071f6a07e2ed33e99966" data-og-width="569" width="569" data-og-height="311" height="311" data-path="images/b1892fb8ea92e7d21ec0b356f7e3330b.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a4e11b463883d633be37837e70072b7f 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a608204bcbbc2354a6725afc2dfc21a6 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=34b55a7ee181cde584b4a1ec51f7050e 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8b20ab03278deadf6b36543ccff80bda 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=49d561de3f8ace2c63c7de134894ce51 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b1892fb8ea92e7d21ec0b356f7e3330b.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f998a7740749a9eabd7f6b7f6a4aaa84 2500w" />

  {" "}
</Frame>

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e196304e185e26651ccb9f504f072cab" data-og-width="595" width="595" data-og-height="494" height="494" data-path="images/886425bb6592ab9e4141b15e3cc001ec.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=de6c97f3ae60284af77ed4c8d9cb7c15 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4f757bb9e91188ded3d3bcd5174b69c4 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=98d0906d0f7a8ed6a158e47e3e79a2b8 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=777c1b71ab6b74250b30b1d51b96ba7a 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2aae3382a9f4cd1585ab17e28b96b268 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/886425bb6592ab9e4141b15e3cc001ec.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=238b36ad8975f128cae31d99d364f884 2500w" />

  {" "}
</Frame>

#### Dynamic Dropdown

If users need to select data from their account in your app — such as a project, folder, team member, or other user-specific detail with a corresponding ID — then you would use a dynamic dropdown. For dynamic dropdowns, Zapier first fetches data from your API and then displays it in a menu. Never make users type in an ID number, rather use this functionality or [add a search action](/platform/build/search) to find the ID number automatically.

The best way to make a dynamic dropdown is to use a dedicated trigger to fetch the values for the menu.

**1. Build a trigger to fetch dynamic dropdown data**

Create a new trigger, with a key, name, and noun. This trigger is usually configured to not be seen by users but you may wish to include a description for your internal team's awareness. In the *Visibility in Editor* field, select `Hidden` to hide this trigger from your app's trigger list in Zapier.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a8c18a735b6775e091bed85a6384b6c3" data-og-width="2016" width="2016" data-og-height="1106" height="1106" data-path="images/36d19e02a566c61c3df00e7b6987daf1.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8d31dfe7ca7b8885b58d634505081d89 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4678c5d6ed15ba8442cb153c2f6cf05b 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c3770e203a8f05d094be1c779e10cae9 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8f1c95ade8d2f804ca322a748e7f9b8a 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=17bbb15a3d7a1677cd22dff04122bb7c 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/36d19e02a566c61c3df00e7b6987daf1.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9787277be8bae3d43c665f93f03ae4c2 2500w" />

  {" "}
</Frame>

You can also use an existing, visible trigger to power a dynamic dropdown if applicable.

Skip the *Input Designer* tab, as the dynamic dropdown cannot require any user input.

Select the *API Configuration* tab, and add the API call where Zapier can fetch the data from your API. For standard Zapier triggers, you would use an API call that fetches new or updated items. For dynamic dropdowns, instead use an API call that pulls in a list of the items that the user can select from.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=152db0774ce38f004a80ee7ffc0d6a42" data-og-width="2012" width="2012" data-og-height="1171" height="1171" data-path="images/e7dd5bf7e40caa03989e754ca518d14c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=9d891f34546a3371fdf07be4fe15f46b 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=6a3087907ddaffe9b11ba885b2d2304e 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=4309e550b996e59a866cc8dcd8e9e240 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e71226f8e1d9404af84ea9c2ec671f65 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=4c520c1a2c79e98a34274a0be40c81ed 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e7dd5bf7e40caa03989e754ca518d14c.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=1f715377d2aa10c818137a2324deff97 2500w" />

  {" "}
</Frame>

API calls will usually require additional configuration to pull in data in the order that makes most sense in your menu. You may want to sort options in the order they were added or updated, or want to have the API fetch more items at once than the default. Set these parameters from the *Show Options* menu.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d194412471d7e04f93bf45b2dbad1da7" data-og-width="1110" width="1110" data-og-height="736" height="736" data-path="images/81be9d8ede3b19a8d4b5f58125575076.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b2a8dc28d92d4edd0bcf15395b6ba679 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=25809e894a044e2adf480529ca2ec295 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=09002ee599a5a1f8ca9e86284856c091 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=82f524fc6be3fa77f104f2a47354a812 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=660650fd343671ecc5f640a4555dbec1 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/81be9d8ede3b19a8d4b5f58125575076.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5699942173cd58d953410831f94d2fac 2500w" />

  {" "}
</Frame>

If your API supports pagination, you can allow users to load additional data in
the menu by checking the *Support Paging* box. The first API call might pull in
20 items; if the user requests additional items, Zapier would call the API again
and request the second page for the next 20 items. *per\_page* and *limit* are
common parameters to indicate how many items to pull (controlling the page
size). Confirm which parameter to use from your API's documentation.

Customize the pagination using [Code Mode](/platform/build/code-mode). Learn more about [how to use pagination in triggers](/platform/build/trigger#how-to-use-pagination).

Zapier shows the data in the dropdown menu in the order your API sends it to Zapier. If your API sends the data in alphabetical order, or numerical order, it will show as such in your drop-down menu. If your API call supports sorting, include the sorting parameter in your API call that would return data in the order you want it to show in your drop-down.

Define the fields from this hidden trigger that you need to use in the dynamic dropdown input field. To do so, test your trigger and identify the output fields needed, adding them to the *Output Fields* list at the end of your settings page. Include at least a field with the data that Zapier needs to send to your API in the action (for example `id`), along with a field that includes a user-friendly `name` for the data in that field.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c9bcf29c1ac7656817105bd18648c2c4" data-og-width="1192" width="1192" data-og-height="819" height="819" data-path="images/3023ea97191fbcf90222dcf42a46035d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a41031c9bd0c581ada3b9479d4a6c14f 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=6de7662c6f5cb34479ad3b7b699f5e2c 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=0f4e6b7bc60703ffeb0732001a484c0b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=79dfd930604b53e0484e51060c0eba3c 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=53f5c3ab3d8ac9c0e4918d0672eb1424 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3023ea97191fbcf90222dcf42a46035d.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=07a88164ebb1d393a0e8b2ddaf08b81a 2500w" />

  {" "}
</Frame>

**2. Add an input field with dynamic fields**

To use the data from the hidden trigger you've configured, add a new input field to the trigger/action you're working on, and set the label, key, and other details as normal. Check the *Dropdown* box and select the *Dynamic* toggle. Choose the hidden trigger you've configured for this menu in the *Dropdown Source* option.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=8acc17f999ff42fa3bcb4432efb273dc" data-og-width="1661" width="1661" data-og-height="987" height="987" data-path="images/f2a8c7071bf4e96e5a44073999b4ccf5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=d5cb30f3e44b987fd5869441d28e77ec 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=44424fa6dd4d0243e9d56d0b8cf0d7ee 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=81424aea75266a58628de4374b08f77e 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ddf4e7228255c091e519cbf1987dde61 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=4e85144c6b8bbc1e2ca5e51534474b9a 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f2a8c7071bf4e96e5a44073999b4ccf5.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=9bff94747e7b0948c9ca5afbbc14aadf 2500w" />

  {" "}
</Frame>

Select the field with the data your API needs for this action in the *Field Name* menu, and the field with a human-friendly name for the data in the *Field Label* menu. The [preview will indicate the presence of the field](/images/4780bb34f2f3d24062d2eb556ed1e3a9.webp), but you will need to use your trigger/action in a Zap to test the menu and pull in real data.

When this trigger/action is selected in a Zap, the user will see a dropdown as Zapier polls your API for the data from that hidden trigger, parse the entries and extract the fields you specified, showing them in a user-friendly dropdown menu. The human-friendly name will be in larger, darker text, and the value to be sent to the API in smaller, lighter text.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=28d976949d4cfda846e23158f8fa460d" data-og-width="946" width="946" data-og-height="571" height="571" data-path="images/afacb9fb44654908ec3d9e6803b728ee.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a3d0da3226fc669690c1debf8124f401 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=dc41ee9d0a861a01c9eff52b3825fbe7 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e62fbfcabd7f9c6f7c29e84a39204c85 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=63290ab58b4b7b7cf55baeb32c36abdb 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d8bd20b30ac154e26480e25ad5c2e039 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/afacb9fb44654908ec3d9e6803b728ee.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=be1d37c40dd3a9b472459e43ead0aefe 2500w" />

  {" "}
</Frame>

It is important to provide the API value (example `id`) for users to know what type of data the field expects. Users can also choose to [enter a custom value](/images/f72a12759a3b3b391025f6500f6c7904.webp)
and map data from other Zap steps into this field. Being able to see what type of value to map is extremely helpful.

**3. Add search to a dynamic field (optional)**

Dynamic Dropdown menus can optionally include an additional *Add a Search Step* button beside the dropdown menu. This lets users dynamically select the correct item from a dynamic field based on input from previous Zap steps.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8d184cb309a33716984c7fcc9967a193" data-og-width="1663" width="1663" data-og-height="965" height="965" data-path="images/51ef24ac9ee90dd393e695ec75601532.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9c563c7f2d0f704799030305e7b6c421 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8598e08d9d527e0905c7f9b4d3ec8832 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d34457951b8dd95cebb65013723e14a1 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d6a49180bead4e375b14c9262184c25d 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3fc90c8db3cf60541d88465d82e0760d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/51ef24ac9ee90dd393e695ec75601532.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=f625c77b9ab73e3b66363f9c2d225558 2500w" />

  {" "}
</Frame>

You'll need to add a [Search Action](/platform/build/action#how-to-add-a-search-action) to find the items used in this dropdown menu. Then check the *Add a search to this field* option under the dynamic dropdown you've built, choose that action, and enter the ID of the field from that trigger that Zapier needs to pass with this API call (which should include the same data as the *Field Name* you selected before for the dynamic menu).

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=8d17c93d9ada402bc484f523c16f35a2" data-og-width="1194" width="1194" data-og-height="1133" height="1133" data-path="images/3f6203d975653bcd004dccb5f15424ed.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ed33ec6a5e35767a79f83929e5749d58 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=abf794a0b70267f5f159f2a764636053 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7fd0196454a22e428c5ab709ab58c5c1 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=76d80b10bf5e435ad37a4e67d019a0ad 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c994a53e5407f9ce2dc0a0440d1d22c8 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f6203d975653bcd004dccb5f15424ed.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9ef46add0bc4ad81f6da8ad118c4507b 2500w" />

  {" "}
</Frame>

When users click or add a search step in their Zap, Zapier will add a new search step before this action step.

<video controls src="https://cdn.zappy.app/b6a7e1ac915b668e12c53b0d08f8330c.mp4" />

This allows the user to enter the details to search for the item they need, and Zapier will automatically map the correct output value from that search to this dynamic dropdown field [as a custom value](https://help.zapier.com/hc/en-us/articles/8496241696141-Add-custom-values-to-dropdown-menu-fields-in-Zaps#01H7FR09FBWT481ZJ77VVR0HBR).

We have a video tutorial on Dynamic Dropdowns which you can view here:

<video controls src="https://cdn.zappy.app/3fe97302eb51e6059bc56bf974c29916.mp4" />

## Reorder input fields

Reordering input fields in triggers or actions can help improve readability and usability.

List the most important, required fields first, with less important, optional fields near the bottom. Have related fields (such as first and last name) near each other. Ordering fields in Zapier similar to the order of fields in any input forms in your app will increase ease of use.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=6e3ec9a86e764dc12c5f1a902de18567" data-og-width="2197" width="2197" data-og-height="1155" height="1155" data-path="images/08bf5a61391edb66c9a5f5bad37e2889.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=698470d469adc15aa3a5a4849a9c2f4a 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3777b02df778e9f0c1e3045ae6db3c8f 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f412f5862b8ff5274ef3b145f55cae56 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a0cdb3406d949f67224b070395415bda 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=d0aa44840264d78852c4f421ae9a47ca 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/08bf5a61391edb66c9a5f5bad37e2889.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=926758cae21a740ee7c5a0ce840fc158 2500w" />

  {" "}
</Frame>

In your trigger or action settings:

1. Click the **Input Designer** tab.
2. In the *Sort* column, click the **up**
   <Frame>
     {" "}

     <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=c5f4cf239bd59432a1e52ed39a71b4c1" data-og-width="75" width="75" data-og-height="75" height="75" data-path="images/7b756b685e0e7f9759e8f7e1ed700aca.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9f995580f7b996df5fd14446ae90d3cc 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=cae3be8b53c3d1e0048c517672e5746f 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f9bd0a9c4b64b4b0a4e9dbdda8c26020 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b7321130eec0989a1b004b08514eee7f 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=248c4a8be1e1b7d0b52bb69267347d82 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/7b756b685e0e7f9759e8f7e1ed700aca.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=0e95d97288c2d7b3e999f8b496b8e2f6 2500w" />

     {" "}
   </Frame>
   or **down**
   <Frame>
     {" "}

     <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=70382b05424873bf651df7de5105ea69" data-og-width="75" width="75" data-og-height="75" height="75" data-path="images/f596f26128d01efe179c4340f0d17f84.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f79517c6a6fbd2235370e7bda2036a80 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=6688c813893f7fe9a6fd0e08d9073a85 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=da6eb43e730f7edfde78134c9be95312 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=1cd98ad27ee7577ff90829ca295c0098 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=c939d7457b0cf6a61b40a4cbb50455c2 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f596f26128d01efe179c4340f0d17f84.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=6b479c6dde793f84b8d26cc6207e5100 2500w" />

     {" "}
   </Frame>
   arrow to move the fields to the order you want in the Form Editor screen.
3. The preview on the right shows how the finished form looks to users inside Zapier.
4. A pop-up message will appear to confirm your changes have been saved.

## Remove input fields

Make sure to delete only unnecessary fields, as a previous version of the input form cannot be restored. You cannot remove input fields from public integrations; you must [create a new version of your integration](/platform/manage/versions) before changing input fields and [consider the impacts of the change](/platform/manage/planning-changes#changing-form-field-keys).

In your trigger or action settings:

1. Click the **Input Designer** tab.
2. Click the **gear icon** <Frame> <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=90f5100da9529e84d415ac118dbe3ba4" data-og-width="75" width="75" data-og-height="75" height="75" data-path="images/1397c67b31689803185dca4e04858e37.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f6a28bb7d3f02d06c8ec6e5eee086018 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a249b9d107827460d1449f9328d58b2b 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=01a8e4d9dd4cdc819e8f5a5b093b33a0 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5b670584405d27dd0c5868c718d3aeeb 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=77d8736dedefb49555363e4746c9a8f2 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1397c67b31689803185dca4e04858e37.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=eeaa01759e7362f58cbc1a8c4ddd633f 2500w" /> </Frame> beside the input field you want to delete.
3. Click **Delete**.
4. Click **Confirm** to remove the input field from your integration.
5. A pop-up message will appear to confirm your changes have been saved.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
