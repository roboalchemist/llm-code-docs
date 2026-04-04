# Source: https://loops.so/docs/integrations/webflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webflow

> Enable signups from your site using a native Webflow form.

<Warning>
  This integration requires a paid Webflow plan to allow embedding custom
  scripts into your site.
</Warning>

To allow sign ups to your audience from your Webflow site, you can utilise a native Webflow form plus some drop-in JavaScript.

## Add a custom form script to your Webflow site

<Tip>
  If you do not add the custom script in the correct place, the form may not
  work properly.
</Tip>

To submit data to Loops seamlessly from your Webflow site we provide some JavaScript, which can be added to your site.

<CardGroup>
  <Card title="Get the script" icon="file" href="https://gist.github.com/askkaz/44ba29cf1898c60e3eb03903e63e2cc4">
    Use this script in your Webflow page.
  </Card>
</CardGroup>

### Where to add the script

* If you have a Loops form on every page of your site, add this code to the "Footer code" section in your Site settings ([read how in the Webflow docs](https://university.webflow.com/lesson/custom-code-in-the-head-and-body-tags#custom-code-in-site-settings)).
* If you have a Loops form on only one page, add this code to the "Before \</body> tag" section in your Page setting ([read how in the Webflow docs](https://university.webflow.com/lesson/custom-code-in-the-head-and-body-tags#before-the-\<-body>-tag)).

## Add a form to your page

Next you need to create a form in your Webflow page. Use the "Input" and "Button" elements.

When you add new fields, make sure the “Name” value in the field's settings panel matches the name of the field in Loops: `email`, `firstName`, etc. You can check the full list of your available properties from your [API Settings](https://app.loops.so/settings?page=api) page.

<Tip>
  Please make sure these contact properties already exist in your Loops account.
  You can add new contact properties in [API
  Settings](https://app.loops.so/settings?page=api), with a [CSV
  import](/add-users/csv-upload) or [using the API](/api-reference).
</Tip>

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=c89a5d084758404721dbacb04c2d6ef6" alt="" data-og-width="2280" width="2280" data-og-height="1662" height="1662" data-path="images/webflow-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f9c91f1f4904529976e1a4e6f8e58576 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=4ded7499455601ff421bc0a1c01f49a2 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=d5f17f5de2d8725fe12d4d4041d5ac06 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=1a3efb3d098075b13738a8a9a341e1f3 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=5f16d0e9ec1ae67078a3413c0276e853 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-field.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=13fa3f2c45a03f1c9709fafb0245aead 2500w" />

### How to add hidden fields

You may want to assign a property to all contacts that submit the form (for example, `source` or `userGroup`).

For this add an "Embed" component *inside your form* on the same level as your input and button elements.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=0947d420946a92c030c643808786b9c4" alt="" data-og-width="2280" width="2280" data-og-height="1662" height="1662" data-path="images/webflow-hidden-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e3352a43c05d22c3ec71a52f6e19a80b 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a3ea14cf8bf4af0502bd403587f44f40 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=3a4853964f841ed5d57f1ea30750c1b4 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=c5cce2cf6da4831dc250988f0d94a17a 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=07589be3780944edb79ff3efd7c2db9a 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-hidden-field.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=198ae135497ab6d291f0ddb5d8b5e00b 2500w" />

In this Embed element add a hidden text field that passes on the custom value to Loops (make sure the `name` values match the "API Name" values in your [API Settings](https://app.loops.so/settings?page=api)).

```html  theme={"dark"}
<input type="hidden" name="mailingLists" value="cly2xnjbn002z0mme68uog1wk, cly4xnjbn002x0mme28uog1wk" />

<input type="hidden" name="source" value="Webflow" />

<input type="hidden" name="userGroup" value="Some User Group" />

<!-- This also works with other default contact properties... -->
<input type="hidden" name="firstName" value="Barbara" />

<!-- ... and custom contact properties -->
<input type="hidden" name="signupPageUrl" value="https://yourdomain/this-page-url" />
```

<Warning>
  Mailing lists need to be marked **Public** in your [Lists settings](https://app.loops.so/settings?page=lists) in order for them to work in forms.
</Warning>

Here's how it looks in the Webflow editor:

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=4f56a8ef8bebe032977da1a09197d361" alt="" data-og-width="2280" width="2280" data-og-height="639" height="639" data-path="images/webflow-embed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=3f1c69513f759dd29ee243c57c6c7ae3 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=1c704f08e28e80c2fa282d58ed1b9e42 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=90e153e8095da2a4789ec83118c20b38 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=85b6898f105457f2393aea57976a3b33 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=febe16b332b04d65d516c626b4460055 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-embed.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f051b19e7f9a1d1778ea525ec0abf958 2500w" />

## Add your Loops form endpoint URL

The last step is to make sure your form submits data to Loops. You do this by adding a Loops form endpoint as the form's "Action" value.

1. Go to the [Forms page](https://app.loops.so/forms) in your Loops account.
2. Click on the **Settings** tab.
3. Copy the URL shown in the **Form Endpoint** field.
   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c44978586df98ffbb59edc5208d5fc39" alt="" data-og-width="2280" width="2280" data-og-height="1389" height="1389" data-path="images/form-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=fa3193dddf8fc5f6fbb03097e90c28ee 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=97d23f7cf388dd355a93a3cdf4629320 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=48384da872ccdafe15fef4fa521a4748 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=badc4b16efe927447068e6e3610baab6 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=81888b8b2c46441883d70dbc0f662b25 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c04bebe574485c7fef2c7ad5e4b573a8 2500w" />
4. In Webflow, click on your Form Block, go to the Settings panel and paste the URL into the **Action** field.
   <img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=585823061a0e327495f131396b83a33b" alt="" data-og-width="2280" width="2280" data-og-height="1662" height="1662" data-path="images/webflow-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=bbfa32c7c6642c2a8dcc429d6abc459b 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=0c66a6e2a7260f2601f1d1cf020e255b 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=619e03264b2a783f980c0c6c477a2434 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=dacd9da75819b9d9cbb656336004a473 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e73ea557f555979cd1f84802a9f35a01 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webflow-action.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=89e06e0f58444313ea2cc1e5801d67de 2500w" />

<Tip>
  Our form submission endpoint has rate limiting, so you will see an error in
  testing if you submit more than once per minute or submit the same email
  twice.
</Tip>
