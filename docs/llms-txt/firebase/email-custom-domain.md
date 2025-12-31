# Source: https://firebase.google.com/docs/auth/email-custom-domain.md.txt

If you use a custom domain in your project, consider also using your custom domain in the emails sent for authentication events, such as email verification, address change, and password recovery flows. You can configure your project to use your custom domain in the emails'`From`field and action links.

By configuring custom domains for authentication emails, users will see the same domain for your web address and the user management emails.

There are broadly two steps to setting this up:

- Add the domain to your email templates in theFirebaseconsole.
- Verify your domain by adding DNS records in your domain registar.

## Adding the domain to your email templates

1. In theFirebaseconsole, open the[Templates page](https://console.firebase.google.com/project/_/authentication/emails)of theAuthenticationsection.

2. For each email template, do the following:

   1. Click the edit icon (edit).
   2. Click**customize domain**.
   3. Enter the domain you want to use.

You'll then see a table of DNS records to add to your domain registrar to verify that you own the domain.

## Verify the domain

Add or update the TXT and CNAME DNS records given in theFirebaseconsole. The procedure for doing so depends on the registrar.

You can have only one`v=spf1...`TXT record for a particular domain. If you need to specify multiple email addresses, combine them into one record.
| **Note:** If you've used GoDaddy as your registrar, customers have reported that they're unable to add a record that only includes the apex domain, and instead need to use`@`in place of the apex domain.

It can take up to 24 hours for the domain to be verified. When it is, the Templates page in theFirebaseconsole will show a green "Verification complete" message. Then, you can click the**Apply Custom Domain**button to put your changes into effect.

## Multi-tenant projects

If you have upgraded toFirebase Authenticationwith Identity Platformand enabled[multi-tenancy](https://cloud.google.com/identity-platform/docs/multi-tenancy-authentication), you need to update[the tenant metadata](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants#inheritance)to allow the tenant to inherit custom domains, email templates, and custom SMTP settings. Otherwise, users still receive emails from the default domain even if the custom domain is successfully verified and applied.

You can check if multi-tenancy is enabled by examining the URL included in Auth email messages. If the URL includes a`tenant`parameter, you need to update your project's tenant metadata.

To do so, run the following command:  

    curl -X PATCH -d "{'inheritance':{'emailSendingConfig': true}}" \
      -H "X-Goog-User-Project: <var translate="no">PROJECT_ID</var>"                          \
      -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
      -H 'Content-Type:application/json'                            \
      https://identitytoolkit.googleapis.com/v2/projects/<var translate="no"><span class="devsite-syntax-n">PROJECT_ID</span></var>/tenants/<var translate="no"><span class="devsite-syntax-n">TENANT_ID</span></var>?updateMask=inheritance.emailSendingConfig