# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-okta-saml.md

# Single Sign-On (SSO) through Okta (SAML)

{% hint style="info" %}
*This feature is currently only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

You can set up Security Assertion Markup Language (SAML) Single Sign-On (SSO) with Okta to let users authenticate through their organization’s identity provider rather than maintaining separate application credentials. Once configured, users can securely access the application using their corporate accounts, while administrators retain centralized control over authentication and access management.

### Supported features

* Single Sign-On (SAML) initiated through Okta
* Automatic account creation in OpenText Core SCA on initial sign-on

### Requirements <a href="#requirements" id="requirements"></a>

* The Okta Single Sign-On integration is only available for the Enterprise customers.
* To complete the integration, you must:
  * Have an Okta account with administrator rights.

### Configuration <a href="#configuration" id="configuration"></a>

To configure your SSO integration with Okta, follow these steps:

#### Service Provider (SP) configuration

Enter the following details in Okta when setting up the SAML application:

| Parameter                    | Value                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Single Sign-On URL (ACS URL) | *<https://debricked.com/app/sso/saml/acs>*                                                                                           |
| Audience URI (Entity ID)     | *<https://debricked.com/app/sso/saml/metadata/{Employer\\_id}> (Refer to the OpenText Core SCA's Metadata file for the employer ID)* |
| NameID format                | EmailAddress                                                                                                                         |
| Application username         | Email                                                                                                                                |

#### Configure the application in Okta

1. In the Okta admin page, click the **Applications** tab.
2. Click **Create App Integration**.
3. Select **SAML 2.0** as the sign-in method.
4. Enter an application name, then click **Next**.
5. In **SAML Settings**, enter the **ACS URL** and **Entity ID** provided above.
6. Set the **Name ID** **format** to *EmailAddress*.
7. Continue through the setup wizard and create the application.

#### Map the attributes

Configure the following attribute statements:

| Attribute | Required | Value          |
| --------- | -------- | -------------- |
| email     | Yes      | user.email     |
| fname     | Yes      | user.firstName |
| lname     | Yes      | user.lastName  |

{% hint style="info" %}
Email addresses must be unique and immutable to ensure consistent and reliable account linking.
{% endhint %}

#### Retrieve Identity Provider metadata

After creating the application:

1. In the Okta admin page, open the newly created application.
2. Navigate to the **Sign On** tab.
3. Scroll to the **SAML Signing Certificates** section.
4. Copy the **Identity Provider Metadata URL** or download the **metadata XML** file.

Share this metadata with the support team or use the *<https://debricked.com/api/1.0/open/sso/saml/request>* API endpoint to post the request along with the other required details.

**Sample payload**

```
curl --request POST \
  --url https://debricked.com/api/1.0/open/sso/saml/submit-saml-configuration \
  --header 'authorization: Bearer {YOUR-TOKEN}' \
  --header 'content-type: multipart/form-data' \
  --form 'file=@{FILE_PATH}\metadata.xml' \
  --form 'emailDomains[]=testdomain.com' \
  --form 'emailDomains[]=testdomain1.com' \
  --form fnameAttribute=fname \
  --form lnameAttribute=lname \
  --form emailAttribute=email
```

### Troubleshooting

If you run into issues while setting up or signing in with Okta, try the following checks:

#### Verify configuration

* Make sure the ACS (Assertion Consumer Service) URL matches exactly with the value provided in OpenText Core SCA.
* Confirm that the Audience URI (SP Entity ID) is identical to the value expected by OpenText Core SCA.
* Check that you are configuring the correct environment (Production vs. Staging).
* Ensure SAML 2.0 is selected as the sign‑on method.
* Verify that the application is assigned to the appropriate users or groups\
  \&#xNAN;*(Applications → Your App → Assignments).*

{% hint style="info" %}
Even minor discrepancies such as an extra space or a trailing slash in the ACS URL or Audience URI can cause authentication to fail.
{% endhint %}

#### Validate email and NameID configuration

Okta does not automatically ensure that the NameID equals the user’s email address. Confirm the following settings:

* The Application username format is set to Email.
* The NameID format is configured as EmailAddress.
* The NameID value sent by Okta exactly matches the user’s email in OpenText Core SCA.
* Email case and domain match perfectly (no mismatches such as uppercase/lowercase or `@company.com` vs `@sub.company.com`).
* The user exists in the correct OpenText Core SCA organization.
* The email domain is verified in OpenText Core SCA.

**Common issue:**

* Okta sends the username instead of the email as NameID.

#### Review attribute statements

Navigate to **Applications** → **Your App** → **Sign On** → **Edi**t → **Attribute Statements** and ensure these attributes are correctly configured:

* `email` → `user.email`
* `fname` → `user.firstName`
* `lname` → `user.lastName`
* `email` → `user.email`
* `fname` → `user.firstName`
* `lname` → `user.lastName`

**Common issues:**

* Missing attribute statements
* Incorrect attribute names
* Username sent instead of email
* Attribute values resolving to `null`

#### Inspect the SAML assertion

Use one of the following to inspect the SAML response:

* Okta System Log
* A browser SAML tracer extension

In Okta, navigate to **System Log** → **Filter by user email or event types:**

* `app.auth.sso`
* `app.auth.sso.failed`
* `user.authentication.failed`

Check the SAML response for:

* Correct NameID value
* Valid Audience URI
* Correct Destination (ACS URL)
* Signature validity
* Accurate attribute values

#### Common errors and resolutions

**❌&#x20;*****You don’t have access to this app***

**Cause**

* User or group not assigned
* Email or NameID mismatch

**Resolution**

* Go to **Applications → Assignments**.
* Assign the required user or group.
* Ensure NameID or email matches the value expected by OpenText Core SCA.

**❌&#x20;*****The audience is invalid***

**Cause**

* Audience URI mismatch
* Extra or trailing slash
* Wrong environment (staging vs production)

**Resolution**

* Copy the Audience URI directly from OpenText Core SCA metadata.
* Remove trailing spaces or slashes.
* Save changes and retry.

**❌&#x20;*****The recipient is invalid  or destination mismatch***

**Cause**

* Incorrect ACS URL

**Resolution**

* Copy the ACS URL exactly from Core SCA metadata.
* Check for hidden whitespace.
* Confirm the correct environment is used.
