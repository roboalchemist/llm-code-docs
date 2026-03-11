# Source: https://docs.envzero.com/changelogs/2023/03/pr-comments-plan-and-apply-role-based-access.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔏 PR Comments With Role Based Access

> With env0, you can restrict the permissions of your organization's users through role-based access controls. You also have the ability to trigger Plan and Apply directly from your PR, however, one drawback is that the VCS provider sets your user's permissions. By default, anyone with comment permission on your repository can run a Plan or an Apply on your environments. Using our new Role Based Access feature for PR comment plan and apply, you can map your VCS provider user to your env0's custom roles, and enforce their permissions while using the PR comment flow. that way having comment permission on your VCS provider won't be enough to deploy an env0 environment.

With env0, you can restrict the permissions of your organization's users through role-based access controls. You also have the ability to trigger Plan and Apply directly from your PR, however, one drawback is that the VCS provider sets your user's permissions. By default, anyone with comment permission on your repository can run a Plan or an Apply on your environments.

Using our new Role Based Access feature for PR comment plan and apply, you can map your VCS provider user to your env0's custom roles, and enforce their permissions while using the PR comment flow. that way having comment permission on your VCS provider won't be enough to deploy an env0 environment.

## ✨ Enforce PR Commenter Permissions ✨

To apply your env0 permissions to your VCS users you can navigate to Organization Settings > Policies and check the`Enforce PR commenter permissions on env0` option

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/03/68aa314-screen_shot_2023-02-28_at_10.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=daa7bc9b592c521977b6afa18cb63043" alt="Feature demonstration screenshot showing new functionality" width="949" height="828" data-path="images/changelogs/2023/03/68aa314-screen_shot_2023-02-28_at_10.png" />
</Frame>

## ✨ Setting Your VCS User Id on env0 ✨

Now that the feature is turned on, it is mandatory for every user across the organization who would like to use the PR comments flow, to set up a mapping of their VCS provider user.\
click on the avatar image in the top right corner, and click on `Personal Settings` to enter your profile page.\
In the `Profile` tab, enter your VCS Provider Id (see [our docs](/guides/admin-guide/environments/plan-and-apply-from-pr-comments#map-vcs-provider-user) to learn how to find it)`VSC Provider User ID` textbox and click on the `Save` button.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/03/896236b-screen_shot_2023-02-23_at_14.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=9e2d5082d480991d40063a3955f22bef" alt="Feature demonstration screenshot showing new functionality" width="3436" height="1564" data-path="images/changelogs/2023/03/896236b-screen_shot_2023-02-23_at_14.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
