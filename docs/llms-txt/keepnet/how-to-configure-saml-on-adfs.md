# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings/how-to-configure-saml-on-adfs.md

# How to Configure SAML on ADFS

This document explains the steps of integrating the Microsoft AD FS (Microsoft Active Directory Federation Service) identity provider with the platform over SAML to log in to the platform by using your ADFS account.

{% hint style="warning" %}
Ensure that ports 80 and 443 communicate between the platform and the identity provider. If the required ports are not open between the identity provider and the platform, an error will occur in the authentication step.
{% endhint %}

## How to Configure SAML

Log in to the platform with the privileged user who can access the SAML settings on the platform and then follows up on the document [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/saml-settings) to fill up the required fields under the ‘SAML Configuration For Platform’ section.

### Adding a Relying Party

Please follow the steps below to add the platform to the relying party trusts.

* Open the ADFS console
* Click **Relying** **Party** **Trust** option on the left and then click **Add** **Relying** **Party** **Trust** button on the right.
* Click the **Start** button in the **Add Relying Party Trust Wizard** window
* Select the **Claims** **Aware** option and click the **Next** button.
* On the **Select Data Source** page, click on **Import data about the relying party from a file**. In the **Federation metadata file location field** section, select the metadata file you downloaded from the platform.
* Specify a display name on the **Specify Display Name** page for display purposes, and click the **Next** button.
* On the **Access Control Policy** page, select the **Permit Everyone** option and click the **Next** button.
* Click the **Next** and then **Close** buttons to complete the process.

### Adding a Claims Rule

* Add a rule.
* Click on **Relying Party Trusts** in the left menu to open the **Edit Claim Rules** page, then right-click on the configuration with the display name specified in the steps above and click on **Edit** **Claim** **Rules**.
* Click **Add Rule** on the **Issuance** **Transform** **Rules** tab.
* On the **Select Rule Template** page, select **Send LDAP Attributes as Claims** and click the **Next** button.
* Specify a name in the **Claim Rule Name** field and select **Active Directory in the Attribute Store** field.
* Add the following attributes to the outgoing claim types table.

| LDAP Attribute (select or type to add more) | Outgoing Claim Type (select or type to add more) |
| ------------------------------------------- | ------------------------------------------------ |
| Given-Name                                  | firstname                                        |
| Surname                                     | lastname                                         |
| Telephone-Number                            | phonenumber                                      |
| User-Principal-Name                         | Name ID                                          |
| spRole                                      | CompanyAdmin                                     |

* And then click the **Finish > Apply > OK** buttons to close the wizard.

{% hint style="warning" %}
The **spRole** depends on your configuration. The point could be CompanyAdmin, Reseller or created Custom Roles.
{% endhint %}

{% hint style="warning" %}
The **Name** **ID** is equal to the **Email Address** field on the platform. The system user must be created on the platform with the email address hosted in the **User-Principal-Name** attribute on ADFS and must log in to the platform with that email address.
{% endhint %}

### Reviewing Relying Party Configuration

* Open the ADFS console
* Click **Relying Party Trust** option on the left and then click the **Edit** of already created relying party trust rule.
* On the **Properties** menu, go to the **Advanced** menu and then choose the **SHA-1** hash algorithm.
* On the **Properties** menu, go to the **Signature** menu and then ask for the platform certificate from the support team or download it from the SAML settings menu on the platform for verification.
* Click **Apply** to save changes.

## Additional AD FS SAML Documents

Please see more information about AD FS SAML configuration in the following documents with screenshots.

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F5ULEwSmsSYZwa2I5dbdj%2FComponentSpace%20ADFS%20Claims%20Provider%20Integration%20Guide.pdf?alt=media&token=d8a03788-c26f-413f-a1f3-a44f17418cdc>" %}
ComponentSpace ADFS Claims Provider Integration Guide.pdf
{% endfile %}

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FtARmgpz18HLTcJKrOSZA%2FComponentSpace%20ADFS%20Relying%20Party%20Integration%20Guide.pdf?alt=media&token=9a352b5a-4968-47b0-86b4-b7a167e59d37>" %}
ComponentSpace ADFS Relying Party Integration Guide.pdf
{% endfile %}

## **How to Test SAML Configuration**

After you have completed the SSO requirements, you can log in to the platform by following the steps below to make sure SSO works successfully.

* Make sure the admin who will log in to the platform over SAML is created in the platform under the Company > System Users page.
* Access the platform's login page.
* In the **Username** **or** **Email** field, enter the user email address of the domain defined for AD FS SAML. You will then be directed to your company's AD FS SSO page in the SAML definition where you can log in to the platform with your active directory account.

## FAQ

### Q: Is the two-factor authentication (2FA) of users valid for a SAML log in?

A: No. The platform automatically disables the 2FA for a SAML log-in.
