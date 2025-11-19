# Source: https://loops.so/docs/integrations/framer.md

# Framer

> Enable signups from your Framer site using an in-built or custom Loops component.

Collect new subscribers from your Framer site. There are a few ways to set this up.

1. [Framer Form component](#framer-form-component)\
   This uses the native Form component in Framer and gives good flexibility for extra form fields.
2. [Framer Loops component](#framer-loops-component)\
   This simplest method. A simple drop-in form with an email address input.
3. [Custom component with code](#advanced-integration)\
   Ths most flexible but complex option, using custom code.

<Tip>
  Our form submission endpoint has rate limiting, so you will see an error in testing if you
  submit more than once per minute or submit the same email twice.
</Tip>

## Framer Form component

Use [Framer Forms](https://www.framer.com/features/forms/) to easily create a form on your site.

### Insert the Form Component

From **Insert -> Forms** drag the **Form builder** component into your page. This will add an example form.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d0426c13908ad170efc970c2ce94017d" alt="Framer Form component" data-og-width="1520" width="1520" data-og-height="1192" height="1192" data-path="images/framer-form-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a15694dcb6ebf01c5b45c34004287346 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c70c0acb121fdc1a06bfbf87efa81f6e 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a6648586ffc781837c434c7c58d2e201 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1eceaa5d0015a85192f01f96047f8daa 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=09d89be07681f8d4cc78768ab041aff2 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-component.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=514116f52b88559731371515da9e500e 2500w" />

### Edit the form fields

Edit the fields in the form to match the data you want to collect from new subscribers.

An email field is required. Make sure to toggle the **Required** option to **Yes** for your email field.

You need to edit the **Name** value of each field to match the [contact properties' "API name"](/contacts/properties) in Loops.

For example, the **Name** value must be "email" for the email address field.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=35e2be920b979df45dd80139b126ee9d" alt="Email form field" data-og-width="2280" width="2280" data-og-height="1356" height="1356" data-path="images/framer-email-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=7efddaf6ac1388ba4dc775cf40d86b65 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=edd0f1fc90e02c4f90811c6869cded0d 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=13223896ecd8651f73c2e9031702802e 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f7e866a9e5e6a24b9b5045d87b32b836 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=70c1f1a688f6ce807a99b9336aa3bcac 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-email-field.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c0081f4e57a1d39b53140e15cdb3162c 2500w" />

You can add hidden fields to populate data like `mailingLists`, `userGroup` and `source` in Loops yet ensure they don't show up in the form.

You may have to click the `+` button to show the **Value** and **Hidden** options.

<Tip>
  To add subscribers to specific [mailing lists](/contacts/mailing-lists), add a field with **Name** `mailingLists`. The **Value** can be a single mailing list ID or a comma-separated list of IDs.
</Tip>

<Warning>
  Mailing lists need to be marked **Public** in your [Lists settings](https://app.loops.so/settings?page=lists) in order for them to work in forms.
</Warning>

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=48c9c39a6c3501490a28ead141aa48c8" alt="Hidden form field" data-og-width="2280" width="2280" data-og-height="1356" height="1356" data-path="images/framer-form-hidden.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e09e5518a9b0bee8b6d9bfeb0ac786a4 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0826a8ddd572b6ca4b0d61b6796a1545 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3bb00074f53b5386c8c4082d0eef001e 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c8d4a751136fcd10be8de009d0889310 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=efb4fae4b127380edf58248992abf164 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-hidden.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=efa691cf86bf1330dd6de21f19e8a1e1 2500w" />

### Configure the form

The final step is to set the endpoint to your Loops form URL.

1. Go to the [Forms page](https://app.loops.so/forms) in your Loops account.
2. Click on the **Settings** tab.
3. Copy the **Form Endpoint**.
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c44978586df98ffbb59edc5208d5fc39" alt="Form endpoint" data-og-width="2280" width="2280" data-og-height="1389" height="1389" data-path="images/form-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=fa3193dddf8fc5f6fbb03097e90c28ee 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=97d23f7cf388dd355a93a3cdf4629320 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=48384da872ccdafe15fef4fa521a4748 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=badc4b16efe927447068e6e3610baab6 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=81888b8b2c46441883d70dbc0f662b25 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c04bebe574485c7fef2c7ad5e4b573a8 2500w" />
4. Back in Framer, select your form. In the **Send To** option, select "Webhook". Then paste the URL from Loops into the **API** field.
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6cb4ce32e76b6d971829df8fde014bcc" alt="Framer form webhook" data-og-width="2280" width="2280" data-og-height="1356" height="1356" data-path="images/framer-form-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=aebab791f507b1864df88db422af26dd 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d80723ea22e99f7a0a9cced67b36b839 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=41c8335ec5f8a86ff4feaa390b77ed99 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b5e6baf22f067ba99539c3cff3d518b1 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0364b94da8f69ccd5cb7ca359e2db7a5 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-form-webhook.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8a5a448de5e0b97ade6da946491e9c69 2500w" />

Now your form is all set up and can start receiving new subscribers.

### Set up a confirmation message

By default a "Thank you" message is shown inside the form button when the form is submitted successfully.

You can opt to use a redirect instead. You can add a confirmation message on another web page and use the **Redirect** option in the form settings.

## Framer Loops component

Framer has a built-in Loops option for creating simple signup forms with an email address field.

### Insert the Loops Component

From **Insert -> Forms** drag the **Loops** component into your page. This will add an example form.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8806edaec1877f6bbf9cd73f337d58fb" alt="Framer Loops component" data-og-width="1520" width="1520" data-og-height="1247" height="1247" data-path="images/framer-loops-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6fcb0343492abaaf76a1a69e77c3219b 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3d52c8ecfe2db32d29304bfa5f1dca61 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=13b4c6c1263127920012776d8ca64424 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=92106aa0dedab50b4dc428f833ba18a5 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=7d4676c6892fae13d60e17544bacec18 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-loops-component.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4e4198b8bc508cf0b5f0f9dbca38c79b 2500w" />

### Configure the form

Next, you need to add your Loops form ID to the **ID** field.

1. Go to the [Forms page](https://app.loops.so/forms) in your Loops account.
2. Click on the **Settings** tab.
3. Copy the **Form ID**.
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0caa3484e77ee805990c12cdf7b62ae9" alt="Form ID" data-og-width="2280" width="2280" data-og-height="1389" height="1389" data-path="images/form-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4abf62f9a866051c3588e1c21e5d6f0c 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c079526c79a6141101f925e8784b17da 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=389b8a262a1740e34280be3eef77a4ac 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=54ada79c91305906e74a292e31ea5864 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=5d261769a879dd66c220122fa869b37b 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-id.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b837cd464b542952c37bb8c86b526cdb 2500w" />
4. Paste this ID into the **ID** field in the Framer component.
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0ee89de4b2c208ad4a2eb6ee2b65e8b2" alt="Loops form ID" data-og-width="2280" width="2280" data-og-height="1688" height="1688" data-path="images/framer-property-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=998d54b7f6d0eeeb7da10532a65987c5 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9c5bca07392090de3e1fb8b774f1ee38 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=782d5a76781939a9fc570bad1e02ee3e 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=ba93695aa13b984a9dd2d30c16df5c91 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=02b5a4f057b08b67e878ee0adeded5cf 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-property-panel.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=51fa226002f0d2d76d22dabc38af0773 2500w" />
5. Framer offers two extra fields in the component:
   * **User Group** populates the contact's `userGroup` value in Loops.
   * **Mailing list** can be used to subscribe contacts to your [mailing lists](/contacts/mailing-lists). Add here one or more mailing list IDs separated by commas.
     <Warning>
       Mailing lists need to be marked **Public** in your [Lists settings](https://app.loops.so/settings?page=lists) in order for them to work in forms.
     </Warning>

### Set up a confirmation message

Make sure to also set up a confirmation message by clicking on the **Success** dropdown.

You can choose to show a message in an overlay with the "Show Overlay" option or redirect the user to another web page with the "Open Link" option.

To add an overlay message, click on the **Overlays** section header in the right-hand panel, choose between "Relative" and "Fixed" and make sure the **Show On** selection is "Submit".

## Advanced integration

This option adds a custom component into your Framer site [using form code](/forms/custom-form) generated by Loops

### Generate the form code

1. Go to the [Forms page](https://app.loops.so/forms) in your Loops account.
2. Click on the **Settings** tab.
3. Select “JSX” from the **Generate Form Code** dropdown (1), then copy the code snippet (2).

   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e220637047302e7c59969a531b231bff" alt="" data-og-width="2280" width="2280" data-og-height="1440" height="1440" data-path="images/jsx-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=df4ed118fa8ee16bd50a317e250c1067 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=bf0e5d64dc31b8a6adb1981e768fbf03 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6b83d745bad2b2b6c3e3587193f78061 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=364fc556ce8a233b5fa71139a01283a5 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9ef00bf3219fd4a353000afbfb8dd4ea 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/jsx-form.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=87b8b93dec8b3dbd8a66973da4681dc7 2500w" />

### Embed the component in Framer

1. Create a new component. Toggle over to **Assets** in the Framer side panel then click the `+` button.

   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=dd174a81bd62bfbf14e0f9edd0221b16" alt="" data-og-width="1520" width="1520" data-og-height="607" height="607" data-path="images/framer-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=572be599bfc1f09c72e3a579f25bfe46 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3d86fa9f4f93de43d217502a991e3e4c 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f12407f44d7d6d897002e3856f542b4a 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=782eeb97705be10c249353552dc04178 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=70a7ab0b27eb9bab0bec718e3bbd89ae 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-1.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8f90ef835add67df7a0ff99e22414a3a 2500w" />

2. Give your New Component a title.

   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=577c8d23d7013beb94d27eec20ccd0ef" alt="" data-og-width="1520" width="1520" data-og-height="808" height="808" data-path="images/framer-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=66a11ee58f167102a7ad131fe41489f3 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=406d218f7b02cfac32fd40a6131bc907 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c7b61d8dc4c4b3df78b0378c0a55a324 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=889021ddace602cd7d8f039e9024014f 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b362344674abfbb097bde1c09142850a 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-2.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=42371df26ee6ec9fd6f7be9ff29b1147 2500w" />

3. Finally, paste the code copied in from Loops into the code editor. You should see the Preview on the right fill in with a preview of your component.

   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e16eb14c62eb830c95fe0deecf3708e7" alt="" data-og-width="1520" width="1520" data-og-height="939" height="939" data-path="images/framer-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=22f47904ad0bde46c12f050f72cd3ef8 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=408167a2720876706a4c87d4ff98382d 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9814bab76021b6c7cc8b68d14cd785fc 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6041ab89fbd675d377b4fc3ce2927611 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=56087f97912139681f9748ee633d50ed 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/framer-3.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b54203e1b51b88da6e8a9b9513ae54de 2500w" />

4. Drag and drop your new asset anywhere on your page to use it :)
