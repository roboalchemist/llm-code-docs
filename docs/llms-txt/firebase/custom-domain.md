# Source: https://firebase.google.com/docs/hosting/custom-domain.md.txt

# Source: https://firebase.google.com/docs/app-hosting/custom-domain.md.txt

<br />

You don't have to give up your unique, brand-centric domain names for apps deployed onFirebase App Hosting. You can use a custom domain (like`example.com`or`app.example.com`) instead of a Firebase-generated domain for your Firebase-hosted site.Firebase App Hostingprovisions an SSL certificate for each of your domains.

The rest of this document walks you through the steps to connect a custom domain in one of these ways:

- [Migrate a domain](https://firebase.google.com/docs/app-hosting/custom-domain#migrate-domain)
- [Connect a new domain](https://firebase.google.com/docs/app-hosting/custom-domain#connect-new)

To ensure uninterrupted service, your DNS records must be updated in a certain order. Follow the instructions to[migrate a domain](https://firebase.google.com/docs/app-hosting/custom-domain#migrate-domain)to prevent downtime for your app.

If downtime isn't a concern, such as when you are connecting a domain that is new to your web app, follow the instructions to[connect a new domain](https://firebase.google.com/docs/app-hosting/custom-domain#connect-new).
| **Note:** This guide assumes that you've completed the basic[App Hostingsetup](https://firebase.google.com/docs/app-hosting/get-started)tasks so that you have aFirebase App Hostingbackend in your Firebase project. We have provided some fundamendals about record types and information on common inputs from popular providers for your reference, but make sure to see your domain provider's documentation for detailed instructions on provider-side setup.

## Before you begin: DNS record types

TheApp Hosting**Set up domain** wizard could ask you to add or remove 1 to 5 DNS records, depending on your domain's current configuration. A record's**Type** determines its function. These are the types of recordsApp Hostingmight ask for:

|   Type    |                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                              |     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| **A**     | These records contain IPv4 values (e.g. 8.8.8.8), which tell browsers what address to use when attempting to contact your domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes |
| **AAAA**  | These records contain IPv6 values (e.g. 2001:4860:4860::8888), a different type of address record with roughly the same function as A records.App Hostingdoesn't currently use AAAA records, but will ask you to remove any existing ones from our domain, if present.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes |
| **CNAME** | These records contain a separate domain name that should be used instead of your current domain to resolve DNS queries. CNAME records are only allowed on subdomains (e.g. www.example.com).App Hostinguses CNAME records for two reasons: - **Easy onboarding:** When possible,App Hostingasks you to CNAME to a preconfigured domain that starts with`_custom-domain...`. - **SSL certificate verification:** App Hostinguses Cloud Certificate Manager to provision SSL certificates for your Custom Domain. A CNAME record on an`_acme-challenge...`subdomain allows Certificate Manager to create and renew certificates for you. After onboarding,**this record*must not be removed*or your certificate coverage will lapse.** | Yes |
| **TXT**   | These records allow you to attach arbitrary metadata to your domain.App Hostingallows you to use a specific format of TXT record,`fah-claim=[UUID]`, to indicate which Custom Domain it should serve on your domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No  |
| **CAA**   | These records function as an allowlist for specifying Certificate Authorities that are authorized to mint SSL certificates for your domain.App Hostingonly requests CAA records if it's otherwise blocked from minting certificates for your domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No  |

## Before you begin: your custom domain name

When adding or editing DNS records, different domain providers expect you to enter different inputs for the**Host** (or**host name** ) field within their DNS management sites. TheApp Hostingcustom domain wizard requires you to input this same value in the**Name**field.

We've compiled common inputs from popular providers below.**Refer to your domain provider's documentation for detailed instructions**.

|   Domain type   |                                                                                                      Custom domain name                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Apex domain** | Common inputs include: - `@` - The apex domain name (for example,<var translate="no">example</var>`.com`) - Leaving the**Host**field blank                                                                                   |
| **Subdomain**   | Common inputs include: - The full subdomain name (for example,`app.`<var translate="no">example</var>`.com`) - Only the subdomain portion (for example,`app`only, and leaving out`.`<var translate="no">example</var>`.com`) |

### Common domain providers

Here are some common domain providers and the types of input each might require. This information is kept up-to-date as much as possible, but**refer to your domain provider's documentation for detailed instructions**.
| **Note:** At any point you can check whether your DNS records have updated correctly with the Google Admin Toolbox[Dig service](https://toolbox.googleapps.com/apps/dig/#A/). Note that even if your records have updated, more time may be needed for propagation or provisioning of the SSL certificate.

#### Cloudflare

|                                                                  |                               |
|------------------------------------------------------------------|-------------------------------|
| <var translate="no">example.com.<var translate="no"></var></var> | <var translate="no">@</var>   |
| <var translate="no">www.example.com.</var>                       | <var translate="no">www</var> |

#### Google Cloud DNS

|                                                                      |                               |
|----------------------------------------------------------------------|-------------------------------|
| <var translate="no">example.com.<var translate="no"></var></var>     |                               |
| <var translate="no">www.example.com.<var translate="no"></var></var> | <var translate="no">www</var> |

#### NameCheap

|                                                                  |                               |
|------------------------------------------------------------------|-------------------------------|
| <var translate="no">example.com.<var translate="no"></var></var> | <var translate="no">@</var>   |
| <var translate="no">www.example.com.</var>                       | <var translate="no">www</var> |

#### Squarespace

|                                                                  |                               |
|------------------------------------------------------------------|-------------------------------|
| <var translate="no">example.com.<var translate="no"></var></var> | <var translate="no">@</var>   |
| <var translate="no">www.example.com.</var>                       | <var translate="no">www</var> |

## Migrate a domain

If you want to transfer your domain from another provider toApp Hostingwithout any downtime, you can use the**Migrate a domain** flow in the Firebase Console. That flow guides you through a two-step process that preparesApp Hostingto serve content on your domain before directing traffic toApp Hostingservers.

### Step 1: Add custom domain

1. Open your project's[App Hostingpage](https://console.firebase.google.com/project/_/apphosting).
2. Select anApp Hostingbackend using the**View Dashboard**option.
3. Select the**Settings** tab, then click**Add custom domain**.
4. Enter the custom domain name that you'd like to connect to yourApp Hostingsite.
5. *(Optional)* Check the box to redirect all requests on the custom domain to a second specified domain (such that`example.com`and`www.example.com`redirect to the same content).
6. Click**Continue to setup**to configure your DNS records and finish setting up your custom domain.

### Step 2: Prepare domain

1. Select the**Migrate a domain** tab of the**Set up domain**wizard.
2. Follow the instructions in the first step,**Prepare domain** , which includes the set of changes necessary forApp Hostingto serve your preferred backend and establish secure TLS connections for your domain. Add, remove, and save records from your domain in your DNS provider with the following inputs for the required records:
   - **Name** : Enter your[custom domain name](https://firebase.google.com/docs/app-hosting/custom-domain#domain-key)for the records. The host you indicate is the domain on which you want to serve content; this domain can be an apex domain or subdomain. Your domain provider may list this term as "Host Name", "Name", or "Domain"
   - **Record type**: Add the provided DNS record.
   - **Value**: Assign the provided value to your records. Your domain provider may list this term as "Data", "Points To", "Content", "Address", or "IP Address". The content of the value field varies by record type; for example, TXT records are strings.
3. Select**Verify records** .App Hostingwill attempt to detect the changes you have made in your domain provider. It can take up to 24 hours for changes to propagate. You can check the[status](https://firebase.google.com/docs/app-hosting/custom-domain#status-descriptions)in the**Settings \> Domains**view in the backend dashboard.

### Step 3: Direct toApp Hosting

1. AfterApp Hostingverifies the record updates from the previous step, the wizard advances to the final**Direct toApp Hosting** step. This step displays the record updates you must make to direct your domain's traffic toApp Hostingservers. As before, add, remove, and save records from your domain in your DNS provider with the following inputs for the required records:
   - **Name** : Enter your[custom domain name](https://firebase.google.com/docs/app-hosting/custom-domain#domain-key)for the records. The host you indicate is the domain on which you want to serve content; this domain can be an apex domain or subdomain. Your domain provider may list this term as "Host Name", "Name", or "Domain"
   - **Record type**: Add the provided DNS record.
   - **Value**: Assign the provided value to your records. Your domain provider may list this term as "Data", "Points To", "Content", "Address", or "IP Address". The content of the value field varies by record type; for example, TXT records are strings.
2. Select**Verify records** .App Hostingwill attempt to detect the changes you have made in your domain provider. It can take up to 24 hours for changes to propagate. You can check the[status](https://firebase.google.com/docs/app-hosting/custom-domain#status-descriptions)in the**Settings \> Domains**view in the backend dashboard.

| **Important:** Make sure to remove any A records or CNAME records that point to other providers. If any of these record types exist, Firebase cannot provision an SSL certificate.

## Connect a new Domain

If downtime isn't a concern, such as when you are connecting a domain that is new to your web app, follow the instructions in this section.

## Step 1: Add custom domain

1. Open your project's[App Hostingpage](https://console.firebase.google.com/project/_/apphosting).
2. Select anApp Hostingbackend using the**View Dashboard**option.
3. Select the**Settings** tab, then click**Add custom domain**.
4. Enter the custom domain name that you'd like to connect to yourApp Hostingsite.
5. *(Optional)* Check the box to redirect all requests on the custom domain to a second specified domain (such that`example.com`and`www.example.com`redirect to the same content).
6. Click**Continue to setup**to configure your DNS records and finish setting up your custom domain.

### Step 2: Verify DNS records

1. The**Set up domain** wizard of the Firebase console will show the necessary records that need to be updated to point your page to Firebase App Hosting. Add, remove, and save records from your domain in your DNS provider with the following inputs:
   - **Name** : Enter your[custom domain name](https://firebase.google.com/docs/app-hosting/custom-domain#domain-key)for the records. The host you indicate is the domain on which you want to serve content; this domain can be an apex domain or subdomain. Your domain provider may list this term as "Host Name", "Name", or "Domain"
   - **Record type**: Add the provided DNS record.
   - **Value**: Assign the provided value to your records. Your domain provider may list this term as "Data", "Points To", "Content", "Address", or "IP Address". The content of the value field varies by record type; for example, TXT records are strings.
2. Select**Verify records** .App Hostingwill attempt to detect the changes you have made in your domain provider. It can take up to 24 hours for changes to propagate. You can check the[status](https://firebase.google.com/docs/app-hosting/custom-domain#status-descriptions)in the**Settings \> Domains**view in the backend dashboard.

| **Important:** Make sure to remove any A records or CNAME records that point to other providers. If any of these record types exist, Firebase cannot provision an SSL certificate.

## Wait for SSL certificate provisioning

App Hostingcan take up to a few hours to provision an SSL certificate for your domain after you update your DNS records. In some cases, it could require up to 24 hours after you point your DNS toFirebase App Hosting.

You can view this certificate using the browser's security tools. While the domain is provisioning, you might see an invalid certificate or have issues connecting to your domain. This is a normal part of the process and will resolve after your domain's certificate is available.

**Note:** Firebase App Hostingautomatically reprovisions SSL certificates, as needed, for custom domains.

## Status descriptions for custom domains

|         Status          |                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Needs setup**         | You may need to change a configuration with your DNS records. - In most cases, your DNS A records haven't propagated from your domain name provider toFirebase App Hostingservers. Troubleshooting tip: If it's been more than 24 hours, check that you've pointed your records toFirebase App Hosting. - In rarer cases, SSL challenges might be failing because your DNS records have A records or CNAME records that point to other hosting providers. Troubleshooting tip: Check that your A records point only toFirebase App Hosting, and remove all CNAME records. |
| **Pending**             | You correctly set up your custom domain, butFirebase App Hostinghasn't provisioned an SSL certificate. Occasionally, excessively restrictive CAA records can stall the minting of an SSL certificate for a custom domain. Ensure that the certificate authorities \`letsencrypt.org\` and \`pki.goog\` are allowed to create SSL certificates for your domain.                                                                                                                                                                                                            |
| **Minting Certificate** | An SSL certificate is being produced for your domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Connected**           | Your custom domain has the proper DNS records and has an SSL certificate. You can serve your site's content.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

*[Input]: Your domain provider might call this field Host, Host Name, Name, or Domain
*[Exclusive]: If a record Type is Exclusive that means you can only have App Hosting records of that type on your domain, and must delete any others
*[Host]: The **Name** value provided by the Firebase console
*[.example.com.]: Google Cloud DNS pre-populates its DNS name field with your apex domain.