# Source: https://docs.luciq.ai/organization-settings/user-management/scim-provisioning/advanced-scim-provisioning.md

# Advanced SCIM Provisioning

{% hint style="info" %}
To enable role and app access mapping during user provisioning, you will need to create a custom attribute for Instabug application integration on OKTA.
{% endhint %}

### Setting up custom attributes

{% stepper %}
{% step %}

#### Login to OKTA admin console

{% endstep %}

{% step %}

#### Navigate to Directory > Profile Editor

Click Instabug User

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fn7R0cDKMthODBUGh79V0%2Fimage.png?alt=media&#x26;token=f04d563c-3c1a-4b41-93ae-0a439342542a" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Click on +Add mappings

{% endstep %}

{% step %}

#### Create a custom attribute for role mapping

Follow the following configurations:

1. Data type = String
2. Display name = Instabug Role
3. Variable name = instabugRole
4. Check the “Enum” box
5. Add a list of Instabug roles

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FnNFCPCBFGjXvDOiv9SL0%2Fimage.png?alt=media&#x26;token=54264029-ca71-4a09-9b8c-2ee377254ba9" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Create a custom attribute for application access

Follow the following configurations:

1. Data type = String
2. Display name = Instabug Applications
3. Variable name = instabugApplications
4. \[Optional] Check the “Enum” box
5. \[Optional] Add a list of your Luciq app names – Must be exact names

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FJg3upXuOVx9DOiaJPIpL%2Fimage.png?alt=media&#x26;token=291bc075-f7e5-4b20-9023-3c7b0a3b2087" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Configure attribute mappings for Luciq user:

1. After clicking Save
2. Click Mappings
3. Then click OKTA User to Instabug

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FOzIsZkMIWEQYIqKT0byE%2Fimage.png?alt=media&#x26;token=c68319ca-db7a-4b25-a2ed-f786801d97e8" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### From the drop-down – Choose InstabugRole

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F7lfprZbFSCfsQh0myBSQ%2Fimage.png?alt=media&#x26;token=422e570a-5bb9-43f9-a8bc-7bf39686e0d3" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Repeat the previous step for InstabugApplications

{% endstep %}
{% endstepper %}

***

### Assigning Roles and App Access To Users

* After completing the configuration successfully, when you add a new user to Luciq for provisioning, you will be prompted to select the Role and Application access for each user.
* These attributes will be optional.
* Go to Applications
* Select Instabug
* Click on Assign > Assign to People
* Select a user to add then click assign
* Select Role from dropdown
* Select Apps to assign to the user

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FKASJrzx2k9ux4CKoNxP8%2Fimage.png?alt=media&#x26;token=3f89905a-00a1-4e7a-90e3-625aec5c199f" alt=""><figcaption></figcaption></figure>
