# Source: https://loops.so/docs/integrations/carrd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Carrd

> Enable sign ups to Loops using a native Carrd form.

### Add a form to your Carrd site

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8be4a67237a40cd87b091981a5424721" alt="carrd image" data-og-width="1520" width="1520" data-og-height="918" height="918" data-path="images/carrd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d1fe0ab24c97aafb16a589d20c93ecff 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cc24ec4e9087888a1fb7591e3086c830 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1f817eb63d4dacef66a3b6990725733e 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=fe2a8c51e94423a6b2eb80182dff35e6 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0941dddbd2696df9c8eec86c3ed86de2 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/carrd.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5cdf110647088ecb4e19b04f34aa5bf8 2500w" />

1. Add a form to your site and select the **Custom** option.
2. Select **Send to URL** and paste in your form endpoint from the [Forms page in Loops](https://app.loops.so/forms).
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c44978586df98ffbb59edc5208d5fc39" alt="form endpoint" data-og-width="2280" width="2280" data-og-height="1389" height="1389" data-path="images/form-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=fa3193dddf8fc5f6fbb03097e90c28ee 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=97d23f7cf388dd355a93a3cdf4629320 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=48384da872ccdafe15fef4fa521a4748 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=badc4b16efe927447068e6e3610baab6 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=81888b8b2c46441883d70dbc0f662b25 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c04bebe574485c7fef2c7ad5e4b573a8 2500w" />
3. Paste the form endpoint you copied from into the **URL** input in Carrd.
4. Change the **Method** to "AJAX" and the **Format** to "JSON".

<Tip>
  Our form submission endpoint has rate limiting, so you will see an error in testing if you
  submit more than once per minute or submit the same email twice.
</Tip>

### Customizing the form

In addition to collecting the email address, you can also collect any other contact property you want.

1. Follow Carrd's documentation to [add a new field to your form](https://carrd.co/docs/forms/setting-up-a-custom-form)
2. Determine your preference:
   * A hidden field that is set to a static value
   * A value that your user can set
3. Assign the field an "ID" matching the Loops API property name that you want to set. You can check the full list of your available properties from your [API Settings](https://app.loops.so/settings?page=api) page.

For example, if you want to set the User Group property, you would add a hidden field and set the ID to `userGroup`.

To add subscribers to specific [mailing lists](/contacts/mailing-lists), add a field with an ID `mailingLists`. The **Value** can be a single mailing list ID or if you want to add subscribers to multiple lists, a comma-separated list of IDs.

<Warning>
  Mailing lists need to be marked **Public** in your [Lists settings](https://app.loops.so/settings?page=lists) in order for them to work in forms.
</Warning>
