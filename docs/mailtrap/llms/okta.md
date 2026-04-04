# Source: https://docs.mailtrap.io/account-and-organization/management/sso/okta.md

# Okta

This guide walks you through setting up SSO integration between Okta and Mailtrap using SAML 2.0, including optional role mapping configuration.

## On Okta side

{% stepper %}
{% step %}
Navigate to **Applications** and click **Create App Integration**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FpUG3o3V9tmhTJOicwG94%2Fsetup-sso-with-okta-1.png?alt=media&#x26;token=55f0ee1d-3d7a-421d-a43f-6b44b45ebf88" alt="" width="375"></div>
{% endstep %}

{% step %}
Select the **Web Platform** and **SAML 2.0** as the Sign on method.
{% endstep %}

{% step %}
Enter app name and click on **Next**.
{% endstep %}

{% step %}
Provide the following **SAML Provider details** to Okta:

* **Entity ID** = Audience URI (SP Entity ID)
* **Assertion Consumer Service URL** = Single sign on URL
* **Name ID format** should be set to `EmailAddress`
* **Application username** should be set to `email`

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWs9FsHc41F0sDyaInTmc%2Fsetup-sso-with-okta-2.png?alt=media&#x26;token=cb775362-20cd-431b-84c6-dc5ee23029c5" alt="" width="563"></div>
{% endstep %}

{% step %}
To apply role mapping please add used for mapping attribute in **Attribute Statements (optional)**
{% endstep %}

{% step %}
Click **Next** and **Finish**.
{% endstep %}
{% endstepper %}

## Mailtrap configuration

After configuration is ready on Okta side, next step would be to setup Mailtrap.

In Okta, you will see info that "**SAML 2.0** is not configured until you complete the setup instructions"

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FOISU6Lrc26EL3z95zM6x%2Fsetup-sso-with-okta-3.png?alt=media&#x26;token=b70147c7-11b2-4fa4-9a47-40e3a94baed2" alt="" width="375"></div>

{% stepper %}
{% step %}
Click **"View Setup Instructions"**

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FXRyU1eHhpNu6IpGrWKvf%2Fsetup-sso-with-okta-4.png?alt=media&#x26;token=b4c6a7c8-2590-43ea-a930-f320d842fd36" alt=""></div>
{% endstep %}

{% step %}
Provide the following to Mailtrap from Okta:

* **IdP Entity ID (Identity Provider Issuer)** = Identity Provider Issuer
* **Single Sign-on URL** = Identity Provider Single Sign-On URL
* **X509 Certificate** = X509 Certificate
  {% endstep %}

{% step %}
Click **Save** in Mailtrap SSO configuration.
{% endstep %}

{% step %}
For **Role mapping** there is additional configuration, please find more details in the SSO Guide Step 4: Role mapping section
{% endstep %}
{% endstepper %}

## SAML role mapping

There are different ways how you can configure your Okta to provide needed `attribute` to Mailtrap.

Mailtrap allows you to configure role attributes mapping (it's name and value). So you can configure will Mailtrap receive a role name from Okta or `true|false` as a value.

* **Example of receiving boolean values in Attribute value**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FE53BdL6K3wk2zNN6CS83%2Fsetup-sso-with-okta-5.png?alt=media&#x26;token=833880e3-0580-434b-84ef-1e64d27fa668" alt="" width="375"></div>

* **Example with Role name in Attribute value**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FQTpDGsAQkU9Wa5xvUKMD%2Fsetup-sso-with-okta-6.png?alt=media&#x26;token=7675846a-9677-47ea-908d-4c07953379f2" alt="" width="563"></div>

{% hint style="info" %}
There are several ways to do it in Okta. The best way is to consult with your team with help with configuration.
{% endhint %}

### Map Okta group names to Mailtrap permissions

{% stepper %}
{% step %}
Create groups in Okta:

* "MT Admin Group"
* "MT Viewer Group"

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgtHvI9iVJzRsZ4CGw2gQ%2Fsetup-sso-with-okta-7.png?alt=media&#x26;token=ce0304f9-6b58-4057-88dd-30af34c97a27" alt="" width="375"></div>
{% endstep %}

{% step %}
Add users to groups
{% endstep %}

{% step %}
Update Okta application SAML attributes mapping

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FpKNAgp0yjI8enALZVuSg%2Fsetup-sso-with-okta-8.png?alt=media&#x26;token=bcf98023-0b9d-46f0-a7e7-8f359bd5c2dc" alt="" width="375"></div>
{% endstep %}

{% step %}
Update attribute statements to return new SAML attributes:

* `isMailtrapAdmin` with value `isMemberOfGroupName("MT Admin Group")`
* `isMailtrapViewer` with value `isMemberOfGroup("00ggiqham4LuYTBPL5d7")`
  * `isMemberOfGroup` accepts group id. Group id can be taken from URL when visiting group page
* More about Okta expressions language [here](https://developer.okta.com/docs/reference/okta-expression-language/)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FQqz08fE5W2FKgKwtanrg%2Fsetup-sso-with-okta-9.png?alt=media&#x26;token=2eb3f22c-a7ff-45cc-80a7-bb44ecdeff89" alt="" width="375"></div>
{% endstep %}

{% step %}
Add SAML attributes mapping in Mailtrap with same attribute names

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FFwXxBQpgNzDZlUV0Oaez%2Fsetup-sso-with-okta-10.png?alt=media&#x26;token=1b7c5798-0daa-464c-aad0-ca67603e4c6a" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

## Debugging Okta integration

You can use [SAML tracer](https://developer.okta.com/docs/guides/saml-tracer/main/) to debug your SAML integration with Mailtrap.

You need to see a proper Attribute Name and Attribute Value in SAML request from Okta and they should match the ones you specified in Mailtrap SSO settings.
