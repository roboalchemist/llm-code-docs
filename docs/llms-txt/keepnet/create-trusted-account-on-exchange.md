# Source: https://doc.keepnetlabs.com/next-generation-product/platform/email-threat-simulator/create-trusted-account-on-exchange.md

# Create Trusted Account on Exchange

Our [E-Mail Threat Simulator](https://keepnetlabs.com/products/email-threat-simulator) requires a test account for making and reporting the tests listed here. This document contains sample configurations for making possible security and reliability checks with this test account.

The test account will only receive email and will not be able to send mail to any internal or external email address except us. This is a safe configuration option that will prevent potential violations.

## Create Test Account

Customers who use an Exchange email server must create a restricted email account. Customers who use Google Workspace, Microsoft 365, or other services may skip this step.

Use the Exchange Server PowerShell administrative interface to create a test account with the command below.

{% hint style="warning" %}
Organization administrator permissions are required to use the Exchange Management Shell.
{% endhint %}

{% code overflow="wrap" %}

```
New-Mailbox -UserPrincipalName “UserPrincipalName” -Alias “Mail Alias” -Name “Mailbox Account Name” -Database “Database Name” -OrganizationalUnit “” -ResetPasswordOnNextLogon $false –password (ConvertTo-SecureString -String “Password” -AsPlainText -Force)
```

{% endcode %}
