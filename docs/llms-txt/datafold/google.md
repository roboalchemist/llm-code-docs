# Source: https://docs.datafold.com/security/single-sign-on/saml/examples/google.md

# Google

## Google as a SAML Identity Provider

Enable SAML in your Google Workspace. Check [Set up your own custom SAML app](https://support.google.com/a/answer/6087519?hl=en) for more details.

<Warning>
  **CAUTION**

  You need to be a **super-admin** in the Google Workspace to configure a SAML application.
</Warning>

* Go to `Google`, click on **Download Metadata** in the left sidebar and **copy** the XML.
* Select **Email** as the Name ID format.
* Select **Basic Information > Primary email** as the Name ID.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8d366ab86b7b5ea4da4f28610f663a7a" data-og-width="1036" width="1036" data-og-height="1092" height="1092" data-path="images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=031e650d4205833f3c37804f02f91163 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e95a625f8140fa3eb94acc2d3bcd046 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5eadb572afb12e36279b4bb353f883d1 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e0b07aa098ee8c5109e157716a701447 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2f3e3605ac2301683f9b01f410ee8835 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_settings-22d5c2a5018e3bd88139f63f41aeb5a8.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8405af2810d95e13cb7cf2b851817f82 2500w" />
</Frame>

* Go to `Datafold` and create a new SSO integration. Navigate to **Settings** → **Integrations** → **Add new integration** → **SAML**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

* Copy the read-only field **Service Provider ACS URL**, go to `Google` and paste it into **ACS URL**.
* Copy the read-only field **Service Provider Entity ID**, go to `Google` and paste it into **Entity ID**.
* Paste the **copied** XML into `Datafold`'s **Identity Provider Metadata XML** field.
* Click **Save** to create the integration.
* (Optional step) Configure the attribute mapping as follows:
  * **First Name** → `first_name`
  * **Last Name** → `last_name`

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab8e093dd14d4ee27f8ace796fcbde82" data-og-width="710" width="710" data-og-height="454" height="454" data-path="images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7dd71eaebd2d6367b7b5ac4b4caeb567 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=86be5fdb3065ef5eeacdd5b5a8bfe13f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fc03a15b3ddf993248d758df5923d659 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ee4c189d5fde064c7c7ec80ede0214c 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a2aa8ce965eb043a66b51cad1fe75b4 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_google_mappings-60f0f4105c1debd2b14a95aa982727fa.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=300534eb2e002dbeef1036a2c7a21bb0 2500w" />
</Frame>
