# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-onelogin-saml.md

# Single Sign-On (SSO) through OneLogin (SAML)

{% hint style="info" %}
*This feature is currently only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

You can set up Security Assertion Markup Language (SAML) Single Sign-On (SSO) with OneLogin to let users authenticate through their organization’s identity provider rather than maintaining separate application credentials. Once configured, users can securely access the application using their corporate accounts, while administrators retain centralized control over authentication and access management.

### Supported features

* Single Sign-On (SAML) initiated through OneLogin
* Automatic account creation in OpenText Core SCA on initial sign-on

### Requirements <a href="#requirements" id="requirements"></a>

* The OneLogin Single Sign-On integration is only available for the Enterprise customers.
* To complete the integration, you must:
  * Have a OneLogin account with administrator rights.

### Configuration <a href="#configuration" id="configuration"></a>

To configure your SSO integration with OneLogin, follow these steps:

#### Service Provider (SP) details

Enter the following details in OneLogin when setting up the SAML application:

| Parameter                    | Value                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Single Sign-On URL (ACS URL) | *<https://debricked.com/app/sso/saml/acs>*                                                                                           |
| Audience URI (Entity ID)     | *<https://debricked.com/app/sso/saml/metadata/{Employer\\_id}> (Refer to the OpenText Core SCA's metadata file for the employer ID)* |
| Application username         | Email                                                                                                                                |

#### Configure the application in OneLogin

1. In the OneLogin admin page, click the Applications **tab**.
2. Click **Add App**.
3. Search for **SAML Custom Connector (Advanced)**.
4. Enter an application name, then click **Next**.
5. Under **Configuration**, enter the **ACS URL** and **Entity ID**.
6. Save the application.

#### Configure SAML parameters

Navigate to the **Parameters** section and create the following mappings:

| Field | Value      |
| ----- | ---------- |
| email | Email      |
| fname | First Name |
| lname | Last Name  |

{% hint style="info" %}
Set the email as **NameID** if required.
{% endhint %}

#### **Retrieve Identity Provider metadata**&#x20;

After creating the app:&#x20;

1. In the Onelogin admin page, open the newly created application.&#x20;
2. Navigate to the **SSO** tab.&#x20;
3. Locate the **SAML 2.0 Endpoint (HTTP)** section.&#x20;
4. Click **View Details**.&#x20;
5. Download the **IdP Metadata XML** file.&#x20;

Share this metadata into the Support team or use the *<https://debricked.com/api/1.0/open/sso/saml/request>* API endpoint to post the request along with the other required details.

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

If you run into issues while setting up or signing in with OneLogin, try the following checks:

#### Verify configuration

* Make sure the ACS (Assertion Consumer Service) URL matches exactly with the value provided in OpenText Core SCA.
* Confirm the Entity ID or Audience URI matches the value expected by OpenText Core SCA.
* Verify that the correct users or groups are assigned to the application in OneLogin.
* Make sure the SAML binding is set to HTTP-POST.

{% hint style="info" %}
Even small inconsistencies such as extra slashes, an incorrect employer ID, or a mismatched domain can cause SAML authentication to fail.
{% endhint %}

#### Check email matching

* The email in the SAML assertion (NameID or mapped email attribute) must exactly match the user’s email in OpenText Core SCA.
* Verify case sensitivity.
* Ensure the user is in the correct organization.
* Confirm the email domain is verified in OpenText Core SCA.

{% hint style="info" %}
Most “Unauthorized” errors stem from email mismatches.
{% endhint %}

#### Review attribute mapping

Ensure the required SAML attributes are properly mapped in OneLogin.

**Required attributes**

* `email`
* `fname`
* `lname`

**Recommended configuration**

* **NameID Format:** Email Address
* **NameID Mapping:** Email

**Common issues**

* Username sent instead of email
* Missing required attributes
* Incorrect attribute names

#### Inspect the SAML assertion

If the configuration looks correct, verify the actual SAML response:

* Use a browser SAML tracing extension to capture and inspect the SAML assertion.
* Check the following values in the SAML response:
  * NameID
  * Audience
  * Destination or ACS URL
  * Signature validity
  * Attribute values
* Review relevant events in OneLogin under **Activity → Events**.

#### Common errors and resolutions

**Typical Message**

“You do not have access to this application.”

**Possible causes**

* User not assigned to the OneLogin application
* Email mismatch
* Domain not verified
* User belongs to another organization

**Resolution**

* Assign the user or group to the application in OneLogin.
* Verify NameID or email mapping.
* Confirm domain verification.
* Ensure the user exists in the correct organization.

***❌ Invalid ACS URL***

**Typical message**

* “Invalid ACS URL”
* “Destination mismatch”

**Possible causes**

* Incorrect Assertion Consumer Service URL
* Wrong environment (staging vs production)
* Incorrect Entity ID
* RelayState misconfiguration

**Resolution**

* Copy the ACS URL directly from OpenText Core SCA’s metadata file.
* Verify Entity ID matches exactly.
* Remove trailing spaces or slashes.
* Save configuration and retry login.

#### 📩 Still facing issues?

When contacting support, include:

* Screenshot of the full error
* Timestamp of the failed login
* User email address
* OneLogin event logs (**Activity → Events**)
* Captured SAML response (if available)

Providing complete diagnostic details will significantly speed up resolution.
