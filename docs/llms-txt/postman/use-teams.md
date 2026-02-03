# Collaborate with your team in Postman

Collaborate with others in Postman using internal workspaces. You can [find a team](#find-teams-within-your-organization) within your organization or [join by other means](#join-a-team) enabled by your organization. If you sign up for a Postman free plan as an individual user, you can create a team during Postman onboarding or later, where up to three users can work together at no cost.

When you join a team in Postman, you can either move your workspaces and transfer ownership to the team or keep your workspaces separate and maintain ownership in your account.

The decision to join a team affects your account in the following ways:

- When you move your workspaces to a team, your account will no longer exist. You'll have the option to switch between teams, rather than work in an account.
- When you keep your workspaces, you'll retain your account. You can switch between the team and your account at any time.

In certain cases, your workspaces and the data within them automatically transfer when you join a team. For more information, see [Join a team](#join-a-team).

When you [leave a team](#leave-a-team), a [Postman account](/docs/getting-started/account/overview/) is created for you, if you don't already have one. If you're deactivated through [SCIM (System for Cross-domain Identity Management)](/docs/administration/scim-provisioning/scim-provisioning-overview/) but are a member of other teams, you'll keep access to your account and other teams to which you belong. If you aren't a member of any other team and don't have an account, you won't be able to authenticate and will need to [contact support](https://www.postman.com/support/).

## Find teams within your organization

When you first join Postman using your company email address on a Free, Basic, or Professional plan, Postman lists the teams you can join within your organization. Select **Show More** to see the full list of teams.

![Join a team from your organization](https://assets.postman.com/postman-docs/v10/join-team-discovery-v10.15.jpg)

Thereafter, your Postman homepage will show discoverable teams you can join. Select **View all teams** to see the full list of teams.

![Join a team from your homepage](https://assets.postman.com/postman-docs/v11/join-team-discovery-homepage-v11.28.jpg)

You can also view all discoverable teams from your profile settings, under **Teams**.

![Discover teams in your profile settings](https://assets.postman.com/postman-docs/v11/discoverable-teams-v11.28.jpg)

Select **Join** next to a team. If a Team Admin has set a mandatory question, answer the question and select **Submit**.

![Request to join team](https://assets.postman.com/postman-docs/v11/request-to-join-team-team-discovery-v11.28.jpg)

When the Team Admins approve your request, you'll be able to access the team and collaborate on API projects within it.

## Join a team

There are several ways you can join a Postman team:

- **Email invite** - Select **Join Team** in the email invite. Create a new Postman account or sign in to an existing one. After signing in, you'll be redirected to your new team.
- **Invite link** - Open the link and select **Accept Invite**. Create a new Postman account or sign in to an existing one. After signing in, you'll be redirected to your new team.
- **Team discovery** - You can [find teams to join within your organization](#find-teams-within-your-organization).
- **Team Request for Access (RFA)** - If you access a link to a resource (for example, a collection or request) from a team you aren't a member of, you can select to request access to that team. An Admin will need to approve your request. If enabled in the team settings on Free, Basic, and Professional plans, you can automatically join a team using a shared link. For more information, see [Manage team access through shared resources](/docs/collaborating-in-postman/requesting-access-to-elements/#manage-team-access-through-shared-resources).
- **SSO automatic provisioning** - If a team in your organization has [automatic provisioning](/docs/administration/sso/admin-sso/#automatically-add-new-users) enabled in their SSO configuration, you can join the team by [signing in to Postman with SSO](/docs/administration/sso/user-sso/).
- **SCIM provisioning** - If your organization has enabled [SCIM provisioning](/docs/administration/scim-provisioning/scim-provisioning-overview/), you may be added to your organization's Postman team and receive an email invite. Select **Join Team** in the email and [sign in to Postman with SSO](/docs/administration/sso/user-sso/).
- **Domain capture** - If your organization has configured [domain capture](/docs/administration/domain-verification-and-capture/domain-capture-overview/) and you use or create an account associated with a verified domain, Postman will [notify](/docs/administration/domain-verification-and-capture/enable-domain-capture/#user-experience) you when you next sign in that your account is managed by your organization.

You can be a member of up to ten Postman teams, regardless of whether they're on the free, Basic, Professional, or Enterprise plan. However, if an Enterprise team within your organization implements domain capture, you won't be able to remain on or join extra Postman teams with your captured accounts.

If you have an account and join a team, you can choose to transfer your workspaces and the data within them to the team or keep them separate. In the following cases, your workspaces and the data within them automatically transfer when you join a team:

- If you [request to join a team](/docs/collaborating-in-postman/use-teams/#join-a-team) and are approved by a Team Admin.
- If the team has [SCIM provisioning](/docs/administration/scim-provisioning/scim-provisioning-overview/) enabled.
- If the team has [domain capture](/docs/administration/domain-verification-and-capture/domain-capture-overview/) enabled.

When you join an Enterprise team, [Super Admins](/docs/administration/roles-and-permissions/#team-roles) have access to all workspaces you transfer over and any you create within the team moving forward.

When you leave a team, your workspaces within the team and their data will remain with the team and no longer be available to you in some situations. See [Leave a team](#leave-a-team) for details. Workspaces in a team refers to workspace visibility and not data ownership.

## Switch between teams

If you belong to multiple teams, you can sign in to them at the same time with your Postman account. To switch between teams, select your avatar in the top right. Select a team to open.

![Switch teams](https://assets.postman.com/postman-docs/v11/team-account-switcher-v11.jpg)

If you're a member of two or more teams, you can also select \[img alt="Add icon" src="https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon"\] **Create Team** to create a new team.

If you have an account, switch to it by selecting your avatar in the top right. Then select your avatar and username labeled **Individual**.

![Switch accounts](https://assets.postman.com/postman-docs/v11/individual-account-switcher-v11.jpg)

## Leave a team

You can leave a Postman team by selecting your avatar in the top right, then **Settings**. Select **Teams** on the left.

Select **Leave** to the right of a team to leave it. If you're a member of an Enterprise team that has [SCIM configured](/docs/administration/scim-provisioning/scim-provisioning-overview/), you must contact a Team Admin to remove you from the team.

![Leave team](https://assets.postman.com/postman-docs/v11/dashboard-teams-leave-team-v11.67.png)

When you leave a team, you no longer have access to the team's workspaces or any of the elements in them. However, you can keep any workspaces you created for your access only in a new team that'll be created for you. If you don't have an individual non-team account, then an individual non-team account is created for you.

![Keep personal workspaces after you leave team](https://assets.postman.com/postman-docs/v11/leave-team-personal-v11.67.png)

If you're a member of an Enterprise team, you must reassign your team workspaces to a remaining team member before leaving.

![Leave team and keep personal data](https://assets.postman.com/postman-docs/v11/leave-team-keep-personal-data-confirmation-v11.67.png)

If you were on a Free, Basic, or Professional team, and you don't have an account, when you leave a team, you can choose to move your workspaces and the associated data to a new account.

![Leave team and keep personal data](https://assets.postman.com/postman-docs/v11/leave-team-keep-personal-data-confirmation-v11.67.png)

If you're the last member to leave a team, the team will be deleted. You'll no longer have access to the team's workspaces, including workspaces set to be accessed by you only, or any elements in them. Team Admins or Super Admins can [export a data dump](/docs/getting-started/importing-and-exporting/exporting-data/) prior to leaving the team to retain the data.