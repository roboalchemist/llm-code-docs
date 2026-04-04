# Source: https://docs.zapier.com/platform/build/basicauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add authentication with Basic Authentication

> APIs using Basic Authentication will authenticate users with a username and password. In your Zapier integration using Basic Auth, Zapier includes the username and password credentials in the API request bundle every time Zapier polls an API endpoint for new data or posts new data to an API endpoint.

<Frame caption="Example Basic Auth screen for users inside Zapier">
  <img src="https://cdn.zapier.com/storage/photos/8987788036a5a70072c9e75c4911ff6a.png" />

  {" "}
</Frame>

Use Basic Auth if your API requires a username and password or other basic fields, needs no special configuration, and specifically if your API leverages “[HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)”. For further customization of your login flow or to request additional data from users, [API Key authentication](https://platform.zapier.com/docs/apikey) may be a better fit.

## 1. Build an input form

* Open the *Authentication* tab in Zapier visual builder and select *Basic Auth*.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=76c5a71655c5f40258ba5d9e30633475" data-og-width="1663" width="1663" data-og-height="995" height="995" data-path="images/a8f5698b7c1fd2556eb6b6dc0a983155.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=dfbd1b55221e5cd875ef0e5d28fac975 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=419df885d9602bba3caf69d437fbadb3 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=bf20681013dbd135e5382d272b95dd7f 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f35d9793fce655d45dd6cb370b0c98c7 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=083b09beb5fb2e5f153bab7974dc362a 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a8f5698b7c1fd2556eb6b6dc0a983155.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=63c9483cf30bd1c83d8853f3fab8811f 2500w" />

    {" "}
  </Frame>

* The pre-built input form for Basic Authentication includes a username and password field already.

* Add additional fields if your API documentation requires it by selecting *Add Fields* and fill in the details for your field. Add the most commonly needed fields first, in the order users expect, as you cannot reorder fields once added.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b13d1e91b4e3a365ef224be2bdf3aa4f" data-og-width="1660" width="1660" data-og-height="805" height="805" data-path="images/c17e6838cf27ed5704f561c75625864f.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=5a8c8dbbb0b2f9dffbde08cf8b2c2db3 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=6c3ef65a75f0306d445b0cb3f533735b 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e57dc5368febee56d46ad0f0d94cdb5e 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d45feea4d09bd12c03432d072ad98945 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b20b0253ec343709b32a94f88db4106f 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/c17e6838cf27ed5704f561c75625864f.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=653af986eb2022502e05eb01396fd9e0 2500w" />

  {" "}
</Frame>

* Add the required *Key*, the name your API uses to reference this field.

* Fill in the optional fields, as appropriate, especially the *Label*:

– **Label**: A human-friendly name for this field that will be shown to users in the authentication form.

– **Required? (checkbox)**: Check if this field is required for successful authentication.

– **Type**: All input fields use the `string` text field by default; select `password` instead if you would like to obscure the data as users enter it.

– **Help Text**: Include details to assist users in authenticating with your app, especially if they may be unsure where to find the data needed within your app. Format text with [Markdown](https://zapier.com/blog/beginner-ultimate-guide-markdown/), and include a hyperlink if needed.

– **Input Format**: (optional) Help users figure out exactly what piece of data you need them to enter. For example, for [a subdomain](/platform/build/subdomain-validation), [https://.yourdomain.com/](https://.yourdomain.com/).

– **Default Value**: Include a value for this field to be used as a fallback. For optional fields, the default value is set on initial connection creation and used in the API call instead of missing or null values every time the Zap runs. For required fields, this value is used during connection creation, but not when the Zap runs (Zapier raises an error for missing/null values instead).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=7d9d8a384472618cdbf2ff3b1f994b62" data-og-width="812" width="812" data-og-height="943" height="943" data-path="images/f4346b3456ea0080862db2eae7108050.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f1b3464bd717e7596ae64f85b41d45d6 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=0aac8df9619442b597369699c37c0f50 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=1ea199e9b3997369fd05f59d16c44180 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f82e648f09a4a85e112f3693d1532bd1 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=74c5cbc08789e3185e4c0a61a4a3c089 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f4346b3456ea0080862db2eae7108050.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=4cda2d815fbfb39931c97a217c7cb687 2500w" />

  {" "}
</Frame>

* Input fields marked as password and all authentication fields with sensitive, private data such as both username and password from Basic Auth are automatically censored at runtime. These values are stored in the Auth bundle and used in API calls, but are replaced in Zapier's logs with a censored value like this `:censored:6:82a3be9927:`. Due to this, it is not possible to view the exact tokens or keys in Zapier's logs. To verify that the same token as was returned by the authentication, is being used in subsequent API calls; you can compare censored value characters, for example `:censored:6:82a3be9927:` would have the same value ending in 9927 when used in a subsequent call.

* Computed fields are not applicable to Basic Authentication and are only used with OAuth v2 and Session Auth.

* Each input field is listed with its label, key, type, and required status in your authentication settings. Click the field to edit it, or click the gear icon and select *Delete* to remove a field.

  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3bad5c9e07efa54da259d47ed44204ee" data-og-width="1657" width="1657" data-og-height="879" height="879" data-path="images/a207e9be179e401dadfa9d5422e4df5c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2ac26769f1354eeaf1b563c347cea0c5 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a3ae18a6822b670124171b5b08e5fd8a 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a747ac16a5de360cf8ee1971f850449c 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a4462a0abfcd668ccca724e1e4d72213 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=284260b2b534688cc6f2c39e42908a47 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a207e9be179e401dadfa9d5422e4df5c.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c6f196d0397126bcfbbac8f0e3b3b550 2500w" />

    {" "}
  </Frame>

* Once you've added all the input fields to your authentication form, select *Continue*

## 2. Add a Test API Request

* Add an API call to your API that requires no configuration, typically a `/user` or `/me` call. Add the URL for the API call, and set the call type, typically a `GET`. This will test the user-entered credentials to ensure it enables a successful API call to your app.

* The username and password input fields are automatically included in the URL Params and the HTTP Headers. Click *Show Options* to remove the details where they are not needed. It is typically not recommended to pass any sensitive information such as the password in the URL Params. Passing it through the headers or even the body is preferable.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=33aa28bec80a965147478f6aa2cf5399" data-og-width="1119" width="1119" data-og-height="481" height="481" data-path="images/a910a8114e18b545a93bf1e2e735e5a1.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c7d62c73275d6d8cb373b74bb073afc4 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f46b5c04999cfd6c2c6b45db155ff854 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=98da3a58548a93a176ad121cc97205a8 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=70108b24e63cf9fcd217e8103f9698da 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6dd2dbb0ff6f9b98d13773e135623fba 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/a910a8114e18b545a93bf1e2e735e5a1.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6afefd2e600afc467930c44f3a2d65dc 2500w" />

  {" "}
</Frame>

* To customize the test API request, select *Switch to Code Mode* and write custom JavaScript code to handle your test API call and the response parsing as needed. The first time you click the toggle, Zapier will convert your API call to code. If you switch back to Form Mode though, Zapier will not convert your code changes to the Form Mode, nor will any subsequent changes in the form be added to your code.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=6b3989129c365ec47a9160a2c0fa2fa4" data-og-width="1105" width="1105" data-og-height="526" height="526" data-path="images/6ec17f1acd3def0addad6dfc9167acec.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7e19cb3ef64210cee3ed562e73afdd91 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3227f531df0f438157bdc604d22cfadd 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f56325e79bc9d0861c8b3e4fb50722a7 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=e7915b454a6d6aff680947f4c790cac6 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b1fcc092565a1d50b3d13546e9359ae3 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/6ec17f1acd3def0addad6dfc9167acec.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=5309233a82c942b7863c143853f6e72b 2500w" />

    {" "}
  </Frame>

## 3. Configure a Connection Label

Review [connection label documentation](/platform/build/connection-label) to optionally differentiate the app accounts users connect.

## 4. Test your authentication

Connect a valid user account to [test authentication](/platform/build/test-auth).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
