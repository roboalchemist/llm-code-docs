# Source: https://docs.mailtrap.io/account-and-organization/management/sso/jumpcloud.md

# JumpCloud

## Overview

This guide walks you through configuring SAML-based Single Sign-On (SSO) between JumpCloud and Mailtrap.

## On JumpCloud side

{% stepper %}
{% step %}
Navigate to **SSO** in JumpCloud and click the **+** button to add new application.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPntsKTlcTtng1YBaTto2%2Fsetup-sso-with-jumpcloud-1.png?alt=media&#x26;token=a6b02484-96c9-4029-99cb-4ee53c218ba0" alt=""></div>
{% endstep %}

{% step %}
Search for **SAML** and choose **Custom SAML App**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FNtvxNc6EJJCyTYofRIzc%2Fsetup-sso-with-jumpcloud-2.png?alt=media&#x26;token=32574ce5-2fae-438a-a6b6-848408ae98f7" alt="" width="563"></div>
{% endstep %}

{% step %}
Specify the application name and proceed to the **SSO** tab.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FW4TauYRY2jNg89BTmN4f%2Fsetup-sso-with-jumpcloud-3.png?alt=media&#x26;token=3393f400-113c-4c5c-bb83-393f7514ca1a" alt="" width="563"></div>
{% endstep %}

{% step %}
Provide the following SAML Provider details to JumpCloud from Mailtrap:

* **SP Entity ID** → Entity ID from Mailtrap
* **ACS URL** → Assertion Consumer Service URL from Mailtrap

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FYR5gRptvqSOT6ty2sIBn%2Fsetup-sso-with-jumpcloud-4.png?alt=media&#x26;token=e04bc6f7-0e0a-4412-9c66-b5918dd1be7f" alt=""></div>

Additional SAML settings:

* **SAMLSubject NameID** should be `email`
* **SAMLSubject NameID Format** leave default value
* **Signature Algorithm** leave default value
  {% endstep %}

{% step %}
If you want to use role mapping, specify **User Attributes** for role mapping:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F1rmxJkX2M3rZFf6H5a88%2Fsetup-sso-with-jumpcloud-5.png?alt=media&#x26;token=8d46ea9a-42c1-44db-ab7a-7da45f156e7b" alt="" width="375"></div>
{% endstep %}

{% step %}
Click **Activate**, then click **Save** after successful activation. Then, download the certificate from the **IDP Certificate Valid** section.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRisztekNtnlE8qIxh4mU%2Fsetup-sso-with-jumpcloud-6.png?alt=media&#x26;token=eac66f1a-9a02-4700-a9e1-25d7f13de6ad" alt="" width="188"></div>
{% endstep %}
{% endstepper %}

## On Mailtrap side

After configuration is ready on JumpCloud side, you can set up the configuration on Mailtrap side.

{% stepper %}
{% step %}
Provide the following to Mailtrap from JumpCloud:

* **IdP Entity ID** (Identity Provider Issuer) → IdP Entity ID from JumpCloud
* **Single Sign-on URL** → IDP URL from JumpCloud
* **X509 Certificate** → Value from the downloaded certificate

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FCc4pY7kBXOmyeYBRgmeC%2Fsetup-sso-with-jumpcloud-7.png?alt=media&#x26;token=a1b8ea34-b9a1-4bf0-9957-72ec3bf92880" alt=""></div>
{% endstep %}

{% step %}
Click **Save** in Mailtrap SSO configuration. For role mapping, configure additional settings as described in the [SSO Guide](https://github.com/mailtrap/mailtrap-docs/blob/main/guides-and-tips/sso/sso-guide.md#step-5-role-mapping).

Your SAML configuration is now complete.
{% endstep %}
{% endstepper %}
