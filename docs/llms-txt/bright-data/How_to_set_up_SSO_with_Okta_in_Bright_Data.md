# Source: https://docs.brightdata.com/general/authentication/How_to_set_up_SSO_with_Okta_in_Bright_Data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up SSO with Okta in Bright Data?

**Requirements**

* An Okta organization account with admin permission
* A Bright Data account with admin permission

**Steps:**

1. On your Okta admin dashboard, choose '**Applications > Applications**'

```sh  theme={null}
https://[your_domain]-admin.okta.com/admin/apps/active
```

2. Click '**Create App Integration**'

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_1.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=9c88a47073231f08f33b8d6e97e886cc" alt="mceclip0.png" width="612" height="234" data-path="images/general/authentication/okta_1.png" />

3. Select '**OIDC - OpenID Connect**' as the Sign-in method,

4. Select'**Web Application**' as the Application type and click '**Next**'

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_2.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=275fe6ce09b617f586dc79559457cde5" alt="mceclip1.png" width="853" height="739" data-path="images/general/authentication/okta_2.png" />

5. At this point you should be redirected to a new web app integration page. Here you can name your app integration (we recommend to use "**Bright Data Control Panel**" name).

6. At ‘Grant type’ select **Implicit** along with **Authorization Code**

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_3.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=fe054b4f09534d4de9d13e2c3cd05133" alt="mceclip0.png" width="932" height="554" data-path="images/general/authentication/okta_3.png" />

7. Go to Bright Data [Control Panel](https://brightdata.com/cp/setting)

8. Open OKTA configuration dialog

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_4.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=0790d6403ef95ffe2d77e93bbf0cd74a" alt="mceclip1.png" width="460" height="420" data-path="images/general/authentication/okta_4.png" />

9. Copy **"Sign-in redirect URI"**

**<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_5.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=f5b83f126deb32d37c7ffd9fecc44186" alt="mceclip2.png" width="630" height="630" data-path="images/general/authentication/okta_5.png" />**

10. Paste it to according field in New App setup in OKTA

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_6.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=0ce165928cb01f9cfc2f8f218c1b0c66" alt="mceclip3.png" width="964" height="625" data-path="images/general/authentication/okta_6.png" />

11. Repeat the same for **"Sign-out URI"**

12. At ‘Assignments’, select an access level as you want

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_7.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=cae78e0c2b87db8dec485ca530a1850b" alt="mceclip6.png" width="894" height="291" data-path="images/general/authentication/okta_7.png" />

13. Click '**Save**'

14. Now, you should land on your new app integration settings page.

Copy your **Client ID**, **Client Secret**, and **Okta domain** to OKTA setup dialog in your Bright Data Control Panel. 

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_8.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=761e24f4afc2fa876a4d005c6fb326f7" alt="mceclip4.png" width="769" height="582" data-path="images/general/authentication/okta_8.png" />

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_9.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=cb2fd84fa749c12e4f6a34dbcfbdf32d" alt="mceclip5.png" width="613" height="630" data-path="images/general/authentication/okta_9.png" />

15. Click **"Activate"**.

Skip step 16 if you selected "Allow everyone to access"

16. Go to **"Assignments"** tab and assign users allowed to use this integration

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_10.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=0bed46e1f0c61b97f75d5ed18808344c" alt="mceclip6.png" width="767" height="721" data-path="images/general/authentication/okta_10.png" />

17. Go to Bright Data Settings page and make sure all required users presented.

We're working on users provisioning support, at the moment - you should manage it manually.

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_11.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=56b354fea4124fe66df680ec9da80f54" alt="mceclip7.png" width="829" height="547" data-path="images/general/authentication/okta_11.png" />

***The following steps are optional. They are for enabling your users to launch authentication from their dashboard or the Okta Chrome extension.***

18. Scroll down to ‘General Settings’ and click **Edit**

19. Set these settings:

* Login initiated by: **Either Okta or App**
* Application visibility: **Display application icon to users**
* Login flow: **Redirect to app to initiate login (OIDC Compliant)**
* Copy Initiate login URI from Control Panel

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_12.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=3372d294b3f1bbec2d112d50d283b2ba" alt="mceclip8.png" width="619" height="632" data-path="images/general/authentication/okta_12.png" />

<img src="https://mintcdn.com/brightdata/JpbB64sgI_r6D502/images/general/authentication/okta_13.png?fit=max&auto=format&n=JpbB64sgI_r6D502&q=85&s=a47e4e28dab76cae75ae7c3b6de330a5" alt="mceclip9.png" width="771" height="609" data-path="images/general/authentication/okta_13.png" />

20. Save changes. **Now the integration is ready to work.**

**Notes**

* Okta Domain should be the one that appears in your app integration settings (**yourcompany.okta.com**), NOT the one you are seeing as an admin (yourcompany-admin.okta.com)

* Make sure the **Credentials** provided to Bright Data are correct, we cannot check them on our side.

-  **Sign-in Redirect URI** is a must in order to make the SSO feature work correctly\
-  **Initiate login URI** is needed if the you wants to be able to use the feature from the Okta Chrome extension or the Okta dashboard
