# Source: https://docs.firehydrant.com/docs/user-administration.md

# User Administration

FireHydrant works best when your entire incident response team has access to create, update, and manage incidents together. Inviting your team is simple and can be done via the UI. All new users will have <Glossary>Member</Glossary> access. For a primer on FireHydrant's access roles, visit [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).

## Who should be on FireHydrant?

At FireHydrant, we believe that **reliability is a company-wide metric**. To that end, FireHydrant is a strong fit for most members of your organization who either respond to incidents or need to be aware of incidents.

We recommend starting with your engineering, SRE, or other teams participating in on-call rotations and responding to incidents. From there, many FireHydrant customers tend to provide access to Support and Success personnel, who often need to communicate incident updates to customers.

Users also provide access to upper leadership who may want access to [Analytics](https://docs.firehydrant.com/docs/analytics-basics) and stay in the loop on severe incidents.

## Inviting team members

If you have [configured SSO](https://docs.firehydrant.com/docs/sso-with-saml), provisioning new users in your IDP will automatically provision team members according to application access. In addition, FireHydrant also supports [SCIM](https://docs.firehydrant.com/docs/scim-configuration) for deeper automation and identity management.

The following instructions are for organizations not using SSO and authenticating via email.

1. Go to **Settings** > **Users**.
2. Click on the "+ Invite user" button. This takes you to a different page where you can enter the email address of whoever you want to invite to the FireHydrant organization.

   <Image alt="Inviting a user via UI/email" align="center" width="650px" src="https://files.readme.io/d3a5dd6ed485653217169e80ac2b25702434b3bc08889c829fa8454a611d8976-CleanShot_2025-01-13_at_17.15.21.png">
     Inviting a user via UI/email
   </Image>
3. Provide the user's email address, select their starting access role, and click **Send invite**.
   * After you invite a user, they'll receive an email invitation.
   * When users click **Accept My FireHydrant Invitation**, they're prompted to provide their name and email, create a password, and accept the privacy policy. Then, they can accept the invitation and join your FireHydrant organization.

<Image alt="Example invitation email" align="center" width="650px" src="https://files.readme.io/8118b5d-user-invite-email.png">
  Example invitation email
</Image>

> 🚧 Note:
>
> Make sure your team members accept your email invitation **instead of signing up separately on the website**. Signing up on the website creates a new organization and account. FireHydrant enforces unique email addresses system-wide, so if someone accidentally registers on their own, they will need to reach out to Support to disable the duplicate account/email before they can accept your invitation.

## Manually Disable a FireHydrant User

<Image alt="Disabling a user via web UI" align="center" width="650px" src="https://files.readme.io/d641fe2-CleanShot_2024-08-13_at_16.57.51.png">
  Disabling a user via web UI
</Image>

Sometimes, teammates move on or change roles, and you want to ensure they can no longer access FireHydrant. You can automate deprovisioning if you are using [SCIM Configuration](https://docs.firehydrant.com/docs/scim-configuration). If not, then aside from [reaching out to support](https://support.firehydrant.io/hc/en-us/requests/new), you can also do this yourself in the UI (**requires<Glossary>Owner</Glossary> permissions**).

1. Navigate to **Settings> Users** and locate the user you want to disable.
2. Click on the user, and scroll down to the "Disable user" section of the individual user details page. You can then choose to disable by selecting "Temporarily disable user." This is a reversible action, so have no fear! Disable away.

## Filtering Users List

<Image alt="Users page with filters expanded" align="center" width="650px" src="https://files.readme.io/bda2727-CleanShot_2024-08-13_at_17.00.47.png">
  Users page with filters expanded
</Image>

On the **Users** page, you can search for specific users and filter users by a few different parameters.

1. Navigate to **Settings> Users**.

2. Click on the **Filter users** dropdown or type into the search bar and hit 'Enter' to filter and search.

FireHydrant supports the following filters for showing users:

* **Without Notification Settings** - Shows users who do not have the specified notification method(s) configured
* **With Notification Settings** - Shows users who have the specified notification method(s) configured
* **Status** - Shows users who are enabled/disabled. By default, the interface only shows active/enabled users
* **Role** - Shows users with the specified [access roles](https://docs.firehydrant.com/docs/role-based-access-controls)
* **Incident access** - Shows users with public/private/both incident access

## Automating User Administration

We recommend automating user provisioning and de-provisioning with [SSO](https://docs.firehydrant.com/docs/sso-with-saml) and [SCIM](https://docs.firehydrant.com/docs/scim-configuration) when possible, as most enterprise companies will use an IDP to manage access to all of their applications.

In addition, FireHydrant does [provide direct APIs](https://developers.firehydrant.com/#/operations/postV1ScimV2Users) to manage users via SCIM, in case you do not use an IDP but still want to manage users programmatically.

## Next Steps

* As mentioned above, look at our [SSO](https://docs.firehydrant.com/docs/sso-with-saml) and [SCIM](https://docs.firehydrant.com/docs/scim-configuration) docs or [the API](https://developers.firehydrant.com/#/operations/postV1ScimV2Users) to see how you can automate FireHydrant account provisioning as part of your IDP workflows
* Read about [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls) on FireHydrant and how to assign the right roles for your users
* Learn more about [Team Management](https://docs.firehydrant.com/docs/team-management) as well as how to [assign users and teams](https://docs.firehydrant.com/docs/adding-responders) to incidents