# Source: https://docs.zapier.com/platform/build/apikeyauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add authentication with API Key

> API Key authentication passes along a user-entered API Key with every API call. In your Zapier integration using API Key authentication, the API key—and optionally any other data your API needs—is included every time a Zap step runs.

<Frame caption="_Example API Key auth screen for users inside Zapier_">
  <img src="https://cdn.zapier.com/storage/photos/19467b7d1852276b766b373373fd069c.png" />

  {" "}
</Frame>

Use API Key authentication if your API primarily uses an API key to identify accounts, especially with apps for weather, maps, content verification, file conversion, and other data tools that require a key for access to the service but do not contain user-specific content.

Since API Key authentication allows you to create a custom input form, you can use it for any custom authentication type with username and password-based logins that don't fit other authentication scheme types.

## 1. Build input form

* Open the *Authentication* tab in Zapier visual builder and select *API key*.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2e5d137f8601b55d85f058ffafa55227" data-og-width="1663" width="1663" data-og-height="989" height="989" data-path="images/283f4595d4e25caee8256b2727eebb6d.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=575cb1b107ea9a2aaa6279803eb37bf7 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2abb10d7365855e43c74955c05eceb92 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=e247e65aded8e4d037e5972e4e47f83a 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=00a3f9f783ecda3a9e108bf338bb265c 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3a438e6ba2f826c7dbc3be7ba5cc42e3 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/283f4595d4e25caee8256b2727eebb6d.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f84498d84b10c1858e97dfe841e33294 2500w" />

    {" "}
  </Frame>

* Add authentication input fields where users will enter their API key and any other required authentication details. Check your API documentation for what fields are required, including user or account names, domains, and more. Note any details users may need on how to find that data in your app. API keys especially are often hidden under settings menus and you'll need to include those details in your input form's help text.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f5d9f5418a6aa2ebb8915f4a5554c0de" data-og-width="1662" width="1662" data-og-height="861" height="861" data-path="images/8de37a192b7d50162a7a115281d4a388.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b476e0649595ba1d2d8a29c32e2c828b 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3b9dc6cc3061e8db63d13c2cee93ab92 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3ee75154a9e608bb64702f5877344b02 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a9fcf927fee32fefe2a070d0cad48d26 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=09e84f4e1691a206a7989414b08c2b0e 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8de37a192b7d50162a7a115281d4a388.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4200f4c491bf9ccf2b6c98d59b1541fa 2500w" />

    {" "}
  </Frame>

* Click the *Add Fields* button and fill in the details for your field. Add the most commonly needed fields first, in the order users expect, as you cannot reorder fields once added.

* Add the required *Key*, the name your API uses to reference this field.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=68565e8f3b9dd930f567d18bc3c10695" data-og-width="809" width="809" data-og-height="953" height="953" data-path="images/d122ac64a68b926bacd5b4e0954ead2c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=22596829701be303d5359c1cf4599db3 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=1afb9b044cd259599431321e5e8ec07f 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=6443ffd82142ce4b212bef31bf9c66ef 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3c33306ac09985c02c82d65d0c91bbbc 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=77fae4039bc613818f1b903f1e37cd9b 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d122ac64a68b926bacd5b4e0954ead2c.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7c3d08b6bbda231e5a15460170dedcda 2500w" />

  {" "}
</Frame>

* Fill in the optional fields, as appropriate, especially the *Label*:

– **Label**: A human-friendly name for this field that will be shown to users in the authentication form.

– **Required? (checkbox)**: Check if this field is required for successful authentication.

– **Type**: All input fields use the `string` text field by default; select `password` instead if you would like to obscure the data as users enter it.

– **Help Text**: Include a direct URL formatted with [Markdown](https://zapier.com/blog/beginner-ultimate-guide-markdown/) where users can obtain their API key from your app. If there is no direct link, include as clear of directions as possible to help users find the API key.

– **Input Format**: (optional) Help users figure out exactly what piece of data you need them to enter. For example, for [a subdomain](/platform/build/subdomain-validation), [https://.yourdomain.com/](https://.yourdomain.com/).

– **Default Value**: Include a value for this field to be used as a fallback. For optional fields, the default value is set on initial connection creation and used in the API call instead of missing or null values every time the Zap runs. For required fields, this value is used during connection creation, but not when the Zap runs (Zapier raises an error for missing/null values instead).

* Input fields marked as password and all authentication fields with sensitive, private data such as API keys from API Key auth are automatically censored at runtime. These values are stored in the Auth bundle and used in API calls, but are replaced in Zapier's logs with a censored value like this `:censored:6:82a3be9927:`. Due to this, it is not possible to view the exact tokens or keys in Zapier's logs. To verify that the same token as was returned by the authentication, is being used in subsequent API calls; you can compare censored value characters, for example `:censored:6:82a3be9927:` would have the same value ending in 9927 when used in a subsequent call.

* Computed fields are not applicable to API Key authentication and are only used with OAuth v2 and Session Auth.

* Each input field is listed with its label, key, type, and required status in your authentication settings. Click the field to edit it, or click the gear icon and select *Delete* to remove a field.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=846d103968c6022f385d3d34d4224eef" data-og-width="1661" width="1661" data-og-height="934" height="934" data-path="images/b27d364f2dd6ef2c1701c8b094a7ada0.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0161594ae93a743406a38f153b88a564 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=54ead4faf2960803ef3894fb4f628c91 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=60f26394a067ab3c8438193c9cb5ea14 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=46c366c9bacddf829282938d104a1a2e 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=08de3b4f9f82ae3703d30737ec327e84 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b27d364f2dd6ef2c1701c8b094a7ada0.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3ebb3fa89d278b42ae4b48d2f50ae2a8 2500w" />

  {" "}
</Frame>

* Once you've added all the input fields to your authentication form, select *Continue*

## 2. Add a Test API Request

* Add an API call to your API that requires no configuration, typically a `/user` or `/me` call. Add the URL for the API call, and set the call type, typically a `GET`. This will test the user-entered API key and any other credentials to ensure it enables a successful API call to your app.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=54479020e92ff9fed161d6ffdfd839bf" data-og-width="1193" width="1193" data-og-height="662" height="662" data-path="images/c4c58979ddcf7eb8a462ac5ff7a37348.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=af88d59468aae26d047f0dd13f273d0c 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8b6315db68b24526d85ad3d1c130b204 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ca64b9cc52f500967c346e4536e2d66a 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=52407188adaebe1dfe5ceba7c1fd10f4 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=568516103832627742de762afea26e24 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c4c58979ddcf7eb8a462ac5ff7a37348.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7c8115146e0622ff63eea930b81d1d85 2500w" />

    {" "}
  </Frame>

* The API key and any additional input fields are automatically included in the URL Params and the HTTP Headers. Click *Show Options* to remove the details where they are not needed. It is typically not recommended to pass any sensitive information such as the API key in the URL Params. Passing it through the headers or even the body is preferable.

* To customize the test API request, select *Switch to Code Mode* and write custom JavaScript code to handle your test API call and the response parsing as needed. The first time you click the toggle, Zapier will convert your API call to code. If you switch back to Form Mode though, Zapier will not convert your code changes to the Form mode, nor will any subsequent changes in the form be added to your code.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=60b00e6f53911bfec11f6e2fb18b17fc" data-og-width="1189" width="1189" data-og-height="713" height="713" data-path="images/b5f336f8d8642f04d99d584f04c4e334.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=e4b7e88c8acd2cd7f07ff16974fc39e3 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=684ee45846eb9529ba51da5c4e201d55 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5c7423ec453d147d5d3377ff89c35c74 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5c9f7cc51efc474fd0963e85e3fb77a8 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=fbcf2bc30090f2899adc36624f4da4de 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b5f336f8d8642f04d99d584f04c4e334.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b0015e518c10df592394e314ef9734b1 2500w" />

  {" "}
</Frame>

## 3. Configure a Connection Label

Review [connection label documentation](/platform/build/connection-label) to optionally differentiate the app accounts users connect.

## 4. Test your authentication

Connect a valid user account to [test authentication](/platform/build/test-auth).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
