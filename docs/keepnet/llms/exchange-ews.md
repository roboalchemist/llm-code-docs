# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations/exchange-ews.md

# Exchange (EWS)

You can integrate your EWS environment with the Incident Responder product by following the steps below.

First, you must have or create a Microsoft user identity with either impersonation or delegation permission.

{% hint style="warning" %}
The user must have exchange admin permissions to configure these options.
{% endhint %}

Please refer to this [document](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide) for information on how to create a service/admin user.

{% hint style="warning" %}
The impersonation option is recommended for setting up email server integration.
{% endhint %}

## Impersonation

Impersonation gives one service account access to every mailbox in a database. This enables quick and easy investigation and response to an incident.

Restrictions may also be designated for the impersonation account, depending on the policies of the organization.

The following command can be used in the Exchange Management Shell to grant the impersonation privilege to a service account. This example assigns the service account **<service@company.com>** full access permission to all user mailboxes in the company.com organization.

```
[PS] C:\Windows\system32> Get-Mailbox -ResultSize unlimited -Filter "(RecipientTypeDetails -eq 'UserMailbox') -and (Alias -ne 'Admin')" | Add-MailboxPermission -User admin@company.com -AccessRights FullAccess -InheritanceType All
```

## Delegation

The delegation privilege requires that permissions be added individually to each mailbox. The platform can access the mailboxes within the Exchange designated by the organization.

Restrictions may also be designated for the account, depending on the policies of the organization.

The following command can be used in the Exchange Management Shell to grant delegation privilege to a service account. This example assigns the service account user **<service@company.com>** full access permission to the specified ‘TargetUserName’ user mailbox.

```
[PS] C:\Windows\system32> Add-MailboxPermission -Identity "TargetUserName" -User "service@company.com" -AccessRights FullAccess 
```

## Test the Integration

To make sure that the integration is working, you can test it on the platform. Go to **Incident Responder > Mail Configurations** on the left sidebar menu of the dashboard and then click **+ NEW** and choose the mail provider - in this case, Exchange EWS. Complete the following fields in the configuration table:

The integration details are:

<table><thead><tr><th width="154.20164126611957"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of the configuration</td></tr><tr><td>Service URL</td><td>Exchange URL information</td></tr><tr><td>Exchange Version</td><td>Exchange version information</td></tr><tr><td>Account Type</td><td>Account type of the service user</td></tr><tr><td>Username</td><td>Username of the service user</td></tr><tr><td>Password</td><td>Password of the service user</td></tr><tr><td>Test Email Address</td><td>An active email address to be used for testing purposes</td></tr><tr><td>X-Anchor Mail Box Header</td><td>Check this box if the platform needs to use the X-Anchor MailBox header in connections to the Exchange server.</td></tr><tr><td>Target Groups</td><td><p>Selection of the users to be subjects of investigation</p><p><strong>All Groups:</strong> All user inboxes</p><p><strong>Specific User</strong> <strong>Groups:</strong> Selected group of user inboxes</p></td></tr><tr><td>Test Connection</td><td>Perform a test of the configuration</td></tr></tbody></table>

The new configuration will now appear in the list of mail configurations if the test was successful.

{% hint style="warning" %}
If an X appears, it indicates there was a problem and the email server integration failed; please review the instructions.
{% endhint %}

## Throttling Policy Configuration

### What is Throttling Policy?

Throttling policy is a control mechanism designed to preserve server reliability and functionality by limiting the resources consumed by a single user or application.

The Microsoft Exchange throttling policy is a default setting that restricts users on various client access protocols, such as MAPI, Activesync, OWA, POP3, etc., intended to prevent a potential crash or denial of service (DoS) via repeated requests.

{% hint style="info" %}
The default throttling policy is always active if a user has not specified an alternate throttling policy.
{% endhint %}

A successful integration between Exchange and the Incident Responder will lead to hundreds of connections on the Exchange server when an investigation begins.

The investigation may be obstructed by the throttling policy. Therefore, the default throttling policy rights of the service user defined in the Incident Responder product should be expanded to avoid this problem.

### Choose a Throttling Policy

You can use the command below in Exchange Management to view all of the available throttling policies.

```
Get-ThrottlingPolicy | where-object {$_.IsDefault -eq $true}
```

### Add a New Throttling Policy

Open the Exchange Management Shell and use the command below to create a new throttling policy.

```
New-ThrottlingPolicy KeepnetUnlimitedPolicyName
```

### Configure Authorizations for the Throttling Policy

Once you have added a new throttling policy, please enter the following command to set the permissions of the new policy.

```
Set-ThrottlingPolicy KeepnetUnlimitedPolicyName -RCAMaxConcurrency Unlimited -Exchange EWSMaxConcurrency Unlimited -Exchange EWSMaxSubscriptions Unlimited -CPAMaxConcurrency Unlimited -Exchange EWSCutoffBalance Unlimited -Exchange EWSMaxBurst Unlimited -Exchange EWSRechargeRate Unlimited -Exchange EWSFindCountLimit Unlimited
```

### Assign Throttling Policy to a Service

User Use the command below to assign a throttling policy to a specific user. Replace **“<service@company.com>”** with the service user you designated in the Incident Responder.

```
Set-Mailbox “service@company.com" -ThrottlingPolicy KeepnetUnlimitedPolicyName
```
