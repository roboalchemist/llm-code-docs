# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/application-credentials.md

# Application Credentials

## Overview

The Application Credentials page gives developers a dedicated way to support how their APIs can be given access to the system.&#x20;

Application Credential records can be created by an individual user logged into Builder. In creating such a record, the logged-in user effectively grants *their own user account's access levels* to the Application Credential record, to allow third party systems using that record subsequently to act on this user's behalf. However the user may not wish to grant the access which is available to all of the roles they occupy, so as part of the record creation they can specify a subset of roles which this Application Credential would have the power to use.

Using this Application Credential approach for granting API access has some advantages over using standard user accounts:

* A single set of application credentials can have multiple concurrent sessions active.
* You can select specific levels of access to grant each set of application credentials, keeping permissions only as expansive as they need to be.
* Allows a more appropriate support for system-to-system communication.
* Gives better tracking of which APIs are accessed by third party applications.

## Technical Specifics

In technical terms, this feature allows Builder admin users to create sets of credentials, specifically 'OAuth Client Credentials' to access Enate & call APIs. Enate uses OAuth2.0 (Open Authorization) for token-based authentication and authorization. For more information on OAuth2.0, please refer to this link <https://oauth.net/2/>.&#x20;

The approach is as follows:

1. An Enate user logs into Builder and creates an application Credential record (a specific 'ClientID & SecretKey' record, which is effectively a username & password).&#x20;
2. External to Enate, you must call the Enate /Auth/OAuth/Token API passing the client id and client secret to obtain a token (specifically a '[Bearer Token](#undefined)').
3. Ensure this Token is included in each API call which is made into the Enate system.

### Bearer Tokens

The integration approach uses a type of tokens called 'Bearer Tokens' to access the Enate APIs. These Bearer tokens use HTTPS security, and the request is not signed or encrypted: possession of the bearer token is considered authentication. For more about OAuth 2.0 access tokens, refer to this link <https://oauth.net/2/access-tokens/>.

Note that the bearer token will expire if it is not used to make an API call for the length of time set in the 'Idle Session Timeout' setting in the General Settings section of Enate Manager.

If the bearer token does expire, the application credentials can be re-authenticated by using the '**/Auth/OAuth/Token**' Enate API to generate a new bearer token.

Additionally, any changes made to a user's roles (i.e. if a user gets assigned a new role or they are removed from a role) will cause the bearer token to expire.

If a bearer token does expire, the application credentials can be re-authenticated by using the '**/Auth/OAuth/Token**' Enate API to generate a new bearer token. Note that revoked roles will not get assigned to a new bearer token.

## Creating a new Application Credentials Record

To support this feature we've added a new section in the User Management section of Builder to help manage different sets of Application Credentials you may wish to create:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FilfEnXya8BRu8VVQGNxp%2Fimage.png?alt=media&#x26;token=179d512a-8f6b-4c6c-a775-41ae77fe0c17" alt=""><figcaption></figcaption></figure>

The resulting screen will show a list of any existing Application Credentials which the logged-in user created before (Application Credentials created by other users are not displayed), including the roles the role(s) assigned to the user and the expiry date.&#x20;

To create a new credential record, click on the '+' link, and fill out the details in the resulting popup:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FG3aKRvYURVpXHEgDIHIA%2Fimage.png?alt=media&#x26;token=80e10e07-a49d-48aa-a14f-1ea0f9f1391f" alt=""><figcaption></figcaption></figure>

Enter a name for the credential and add an expiration date. Then select the Operational Role you want the credential to have. If you want the credential to access Builder, select a Builder role too. These roles determine the various access options that a user will have access to.

Then click to generate a key. This will create:

* A Client ID
* A Secret Key

You should copy these two pieces of data at this point, for use in subsequent steps to create a Bearer Token outside of Enate.

{% hint style="info" %}
Note: You will only be able to access this secret key once, at this point. Once the pop-up window is closed you will no longer have access to it, and if you have not taken a note and subsequently wish to use this client ID, you would need to generate a new secret key.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7ZlN0BHrtMildffybilQ%2Fimage.png?alt=media&#x26;token=9764ffb1-4c2f-4617-a2dc-32c88a097aad" alt=""><figcaption></figcaption></figure>

Once the Credential record has been generated, it will be saved and stored in the Application Credentials page. You, as the creator of the record, can subsequently edit its name and expiry date and generate a new secret key for it. Credential records can also be deleted if desired.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fxmbw0ZZPym6OF7Fganph%2Fimage.png?alt=media&#x26;token=8a43f67c-4c7f-4398-a55b-3779fc798238" alt=""><figcaption></figcaption></figure>

## Generating the Bearer Token - Sample

You should use the copied Client ID and Secret Key as inputs into your third party system, for example the Postman API testing tool. From example above, this would be:

**Client ID:** eba59171-ac3a-4527-939a-830494c2c5f6

**Secret Key:** 3\@rn0i+0y5jRB8\_n

The Third-party system should be making a POST API call to the '**/Auth/OAuth/Token**' Enate API to generate the bearer token.&#x20;

\
For the API request, select '**x-www-form-urlencoded**' in the body section to pass the three parameters below while making the API call to generate the token.&#x20;

* grant\_type - client\_credentials
* client\_id - 0f6c907b-00f4-4e12-8d75-41454b777533
* client\_secret - TLd55KNez61niSXO

Example:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoBD9S3Fjt5A46ogkRWbs%2Fimage.png?alt=media&#x26;token=30e11611-4651-458e-b399-95386d87adb5" alt=""><figcaption></figcaption></figure>

This generates the Bearer token, which is then used to get authorization for API calls to Enate.

## Using the Bearer Token

To make a new API call to Enate, select Type as ‘Bearer Token’ in the Authorization section of the API request, pass your generated bearer token and the request URL for the specific API you're looking for.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFJcUCJPEoHRAGNbXfK0E%2Fimage.png?alt=media&#x26;token=4f546dfe-c611-4998-94b2-d2c2ce461c27" alt=""><figcaption></figcaption></figure>
