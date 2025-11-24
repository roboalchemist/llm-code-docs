# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/adfs.md

# ADFS Identity Provider

Connect ConfigCat with Active Directory Federation Services (ADFS) via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with ADFS as a SAML Identity Provider.

## 1. Collect SAML Metadata from ConfigCat[​](#1-collect-saml-metadata-from-configcat "Direct link to 1. Collect SAML Metadata from ConfigCat")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/adfs_name.png)

* From the next section of the dialog, copy the following values and save them for further use.

  * `Entity ID`

  * `Assertion Consumer Service`

    ![ConfigCat SAML configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png)

## 2. Configure a Relying Party Trust[​](#2-configure-a-relying-party-trust "Direct link to 2. Configure a Relying Party Trust")

* Open the ADFS Management console, and click `Add Relying Party Trust`.

  ![ADFS add relying party trust](/docs/assets/saml/adfs/2_add_relying_party.png)

* Make sure the `Claims aware` option is selected, and click `Start`.

  ![ADFS claims aware](/docs/assets/saml/adfs/3_claims_aware.png)

* Select the `Enter data about this relying party manually` option, and click `Next`.

  ![ADFS manual relying party setup](/docs/assets/saml/adfs/4_manual_metadata.png)

* Type a descriptive `Display name`, and click `Next`.

  ![ADFS display name](/docs/assets/saml/adfs/5_name.png)

* No action required on the `Configure Certificate` pane, click `Next`.

  ![ADFS certificate configuration](/docs/assets/saml/adfs/6_configure_cert.png)

* Select the `Enable support for the SAML 2.0 WebSSO protocol` option, and paste the value of `Assertion Consumer Service` from [Step 1](#1-collect-saml-metadata-from-configcat) into the `Relying party SAML 2.0 SSO service URL` field.<br /><!-- -->Then, Click `Next`.

  ![ADFS acs URL](/docs/assets/saml/adfs/7_acs_url.png)

* Paste the value of `Entity ID` from [Step 1](#1-collect-saml-metadata-from-configcat) into the `Relying party trust identifier` field, and click `Add`.<br /><!-- -->Then, click `Next`.

  ![ADFS entity ID](/docs/assets/saml/adfs/8_add_entity_id.png)

* No action required on the `Choose Access Control Policy` pane, click `Next`.

  ![ADFS Access Control Policy](/docs/assets/saml/adfs/9_access_control_policy.png)

* Review the changes, then click `Next`.

  ![ADFS add trust](/docs/assets/saml/adfs/10_ready_to_add_trust.png)

* The Relying Party Trust is now successfully added, make sure the `Configure claims issuance policy for this application` option is checked, and click `Close`.

  ![ADFS finish configuration](/docs/assets/saml/adfs/11_finish_party.png)

## 3. Configure Claims Issuance Policy[​](#3-configure-claims-issuance-policy "Direct link to 3. Configure Claims Issuance Policy")

* After adding the Relying Party Trust, the following dialog should appear.<br /><!-- -->Click `Add rule`.

  ![ADFS edit claims](/docs/assets/saml/adfs/12_edit_claims.png)

* Select `Send LDAP Attributes as Claims` as the `Claim rule template`, and click `Next`.

  ![ADFS LDAP claims](/docs/assets/saml/adfs/13_ldap_claims.png)

* Apply the following, and click `Finish`.

  * Add a descriptive `Claim rule name`.
  * Select `Active Directory` as `Attribute store`.
  * Select `User-Principal-Name` as `LDAP Attribute`.
  * Select `Name ID` as `Outgoing Claim Type`.

  ![ADFS unc to nameid](/docs/assets/saml/adfs/14_unc_to_nameid.png)

* Click `OK`.

  ![ADFS finish claims](/docs/assets/saml/adfs/15_finish_claims.png)

## 4. Configure ConfigCat with SAML Details from ADFS[​](#4-configure-configcat-with-saml-details-from-adfs "Direct link to 4. Configure ConfigCat with SAML Details from ADFS")

You can choose one of the following options to configure ConfigCat with SAML Identity Provider metadata.

* Metadata URL
* Manual Configuration

- Select `Endpoints`, and copy the URL Path of the `Federation Metadata` endpoint.

  ![ADFS metadata url path](/docs/assets/saml/adfs/metadata_url.png)

- Type the URL into the `Metadata URL` field at ConfigCat in the following format: `https://[ADFS-DOMAIN]/[FEDERATION-METADATA-URL-PATH]`.

  ![ADFS metadata url](/docs/assets/saml/adfs/cc_metadata_new.png)

- Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

- Click on `Save`.

* Select `Endpoints`, and save the URL Path of the `SAML 2.0/WS-Federation` endpoint.

  ![ADFS SAML verification](/docs/assets/saml/adfs/login_url.png)

* Select `Certificates`, then select the `Token Signing` certificate, and click `View Certificate`.

  ![ADFS certificates](/docs/assets/saml/adfs/view_cert.png)

* On the `Details` tab click `Copy to File`.

  ![ADFS cert details](/docs/assets/saml/adfs/copy_cert_to_file.png)

* Click `Next`.

  ![ADFS cert wizard](/docs/assets/saml/adfs/cert_wizard.png)

* Select the `Base-64 encoded X.509 (.CER)` option, and click `Next`.

  ![ADFS export base64](/docs/assets/saml/adfs/cert_export_base64.png)

* Browse the location where the certificate should be exported, and click `Next`.

  ![ADFS cert name](/docs/assets/saml/adfs/cert_name.png)

* Click `Finish`.

  ![ADFS finish cert](/docs/assets/saml/adfs/cert_finish.png)

* Click `OK`.

  ![ADFS cert OK](/docs/assets/saml/adfs/cert_export_ok.png)

* Type the `SAML 2.0/WS-Federation` endpoint into the `Sign-on URL` field in the following format: `https://[ADFS-DOMAIN]/[WS-FEDERATION-URL-PATH]`. Then, paste the exported `Token Signing` certificate into the `X.509 Certificate` field.

  ![ConfigCat manual configuration](/docs/assets/saml/adfs/cc_manual_new.png)

* Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click on `Save`.

## 5. Sign In[​](#5-sign-in "Direct link to 5. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com/auth/login) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to the ADFS sign in page. Type your credentials, and click `Sign in`.

  ![ADFS log in](/docs/assets/saml/adfs/login.png)

* You should be redirected to ConfigCat signed in with your company account.

## 6. Next Steps[​](#6-next-steps "Direct link to 6. Next Steps")

* Configure the [auto-assignment of users](https://configcat.com/docs/docs/advanced/team-management/auto-assign-users/.md).
