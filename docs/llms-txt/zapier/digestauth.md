# Source: https://docs.zapier.com/platform/build/digestauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add authentication with Digest Authentication

> Digest Auth prompts users to enter their username and password, optionally along with any additional data your API requires for authentication. Zapier makes an unauthenticated API call to get the nonce from your server, and uses it to encrypt and pass the authentication data to your server with each API call.

<Frame>
  <img src="https://cdn.zapier.com/storage/photos/3c842632d017aa50ba6470201d02f416.png" />

  {" "}
</Frame>

Use Digest Auth if your API uses the [RFC 7616](https://tools.ietf.org/html/rfc7616) authentication standard, where users enter their username and password to be passed encrypted to your API with the nonce key your app sends to Zapier on the first API call.

## 1. Build an input form

* Open the *Authentication* tab in Zapier visual builder and select *Digest Auth*.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3f585eb99a48c5832e835e2823ab1c0a" data-og-width="1661" width="1661" data-og-height="993" height="993" data-path="images/fccd6ab8ba9c837158907d39eef1f288.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=27a2f9a68f117cfe0c58dd948f0b1d3e 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ccfc3d72f9f0caefa2294564cd75a0e0 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=22dc2a6eb8fe4f2101613da9456a2fd7 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e161e9ab46018ca461368cdd7a150fe9 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=87a5277b7695c77302c3639469dc484d 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fccd6ab8ba9c837158907d39eef1f288.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=26173de2a8b7a0316b98b1feb4e1009c 2500w" />

    {" "}
  </Frame>

* The pre-built input form includes username and password fields already.

* Add additional fields if your API documentation requires it by selecting *Add Fields* and fill in the details for your field. Add the most commonly needed fields first, in the order users expect, as you cannot reorder fields once added.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f69ac0b41f6aa42af69513ca4b40b129" data-og-width="809" width="809" data-og-height="953" height="953" data-path="images/680696e6c2d79b837600c5d1e32c9d40.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=92007cae1f0799a8544613b66bfc8920 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8e039221cc7384f7038357975b817383 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9d91b56b455ff5afc79de88a1c4957e2 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=04d82f7040e37b665115700c7d6d21d8 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b8723568708fe2aec259c9f08726fec5 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/680696e6c2d79b837600c5d1e32c9d40.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=1399d89b0a5c42b708512868c40aa3f3 2500w" />

    {" "}
  </Frame>

* Add the required *Key*, the name your API uses to reference this field.

* Fill in the optional fields, as appropriate, especially the *Label*:

  **Label**: A human-friendly name for this field. Enter what this value is called inside your app's UI.

  **Is this field required**: Check this box for the API key field, and any other fields your API requires to authenticate.

  **Type**: All input fields use the `string` text field by default; select `password` instead if you would like to obscure the data as users enter it.

  **Help Text**: Include details to assist users in authenticating with your app, especially if they may be unsure where to find the data needed within your app. Format text with [Markdown](https://zapier.com/blog/beginner-ultimate-guide-markdown/), and include a hyperlink if needed.

  **Default Value**: Include a value for this field to be used as a fallback. For optional fields, the default value is set on initial connection creation and used in the API call instead of missing or null values every time the Zap runs. For required fields, this value is used during connection creation, but not when the Zap runs (Zapier raises an error for missing/null values instead).

* Input fields marked as password and all authentication fields with sensitive, private data such as both username and password from Digest Auth are automatically censored at runtime. These values are stored in the Auth bundle and used in API calls, but are replaced in Zapier's logs with a censored value like this `:censored:6:82a3be9927:`. Due to this, it is not possible to view the exact tokens or keys in Zapier's logs. To verify that the same token as was returned by the authentication, is being used in subsequent API calls; you can compare censored value characters, for example `:censored:6:82a3be9927:` would have the same value ending in 9927 when used in a subsequent call.

* Computed fields are not applicable to Basic Authentication and are only used with OAuth v2 and Session Auth.

* Each input field is listed with its label, key, type, and required status in your authentication settings. Click the field to edit it, or click the gear icon and select *Delete* to remove a field.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7d77c58be665b908cc11ba28ce254e6c" data-og-width="1661" width="1661" data-og-height="831" height="831" data-path="images/573a3eb19a884c44fd67b9fa421c3bf4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=192e251bc9eac88d52825ada905efbf8 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=41fdcb1646d53e372674cc1d213df4e7 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3be67df472e84c135d4d606f707db3fb 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f6e4e765b67db7abdfbdf190175d9746 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=04fec4258fc45c1987426186437a5dbf 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/573a3eb19a884c44fd67b9fa421c3bf4.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=26adb2cacbf9c46a4899561759efb039 2500w" />

  {" "}
</Frame>

## 2. Add a Test API Request

* Add an API call to your API that requires no configuration, typically a `/user` or `/me` call. Add the URL for the API call, and set the call type, typically a `GET`. This will test the user-entered credentials to ensure it enables a successful API call to your app.

* The Digest input fields you configured earlier are automatically included in the URL Params and the HTTP Headers. Click *Show Options* to remove the details where they are not needed or add any custom URL params or HTTP headers your API requires. It is typically not recommended to pass any sensitive information such as the password in the URL Params. Passing it through the headers or even the body is preferable.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=44196d010c89f7ac616a81974d0b329a" data-og-width="1193" width="1193" data-og-height="435" height="435" data-path="images/503eeb14514aa854ae06ba956b6c572c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=173af93a32933cf95e45db3e77a37c7c 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=209531223f0058d729b41e992ba8695b 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=57d105450123557a1e50822f2fb6beba 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a6982a8df0dc31a0562ac385a8860933 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b97a8df21162e0cda304d6903dda876d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/503eeb14514aa854ae06ba956b6c572c.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e7061aff48205e358d984b932cf51b3c 2500w" />

  {" "}
</Frame>

* To customize the test API request, select *Switch to Code Mode* and write custom JavaScript code to handle your test API call and the response parsing as needed. The first time you click the toggle, Zapier will [convert your API call to code](/platform/build/code-mode). If you switch back to Form Mode though, Zapier will not convert your code changes to the Form Mode, nor will any subsequent changes in the form be added to your code.

## 3. Configure a Connection Label

Review [connection label documentation](/platform/build/connection-label) to optionally differentiate the app accounts users connect.

## 4. Test your authentication

Connect a valid user account to [test authentication](/platform/build/test-auth).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
