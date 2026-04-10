# Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/admin-permissions/discord-limitations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Discord Limitations

> This is how to properly integrate roles created by Drip Rewards into your Discord

Drip Rewards allows communities to create roles or delegate custom roles to team members, allowing them to use features such as the `/create` command. However, you must "tell" Discord that Drip is allowed to do this within Discord Integration Settings.

If you haven't done so already, be sure to assign/create admin [Admin Permissions](/admin-settings/admin-dashboard/admin-settings/admin-permissions) as seen below:

<Frame caption="Create/Assign Admin roles">
  <img src="https://docs.drip.re/~gitbook/image?url=https%3A%2F%2F2728597434-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxUaE8LDXTeS85PkKxJJa%252Fuploads%252FE6ipKaqBGT2MPE1yil6p%252F%2523%25F0%259F%259B%25A0%25E2%2594%2586admin%2520Drip%2520Documentation%2520-%2520Discord%25202024-02-08%2520at%252011.12.40%2520AM.jpg%3Falt%3Dmedia%26token%3D6fb0cbce-58fd-4860-aa90-3aa161a1bb35&width=768&dpr=4&quality=100&sign=51a5df0f&sv=1" />
</Frame>

### Integrating Admin Roles

Navigate to Server Settings in your Discord community by choosing `Server Settings` in the dropdown menu at the top of your channels list

<Frame caption="Click on Server Settings">
  <img src="https://mintcdn.com/driprewards/C8C-yxJTuKgUzgAP/images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_10caa2.png?fit=max&auto=format&n=C8C-yxJTuKgUzgAP&q=85&s=6fc4909faa7eaefd0d0240d423a30e9d" width="323" height="472" data-path="images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_10caa2.png" />
</Frame>

Click on `Integrations` in the Apps category then navigate to Drip and click on `Manage`

<Frame caption="Click on Integrations > Drip > Manage">
  <img src="https://mintcdn.com/driprewards/C8C-yxJTuKgUzgAP/images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_dee9c6.png?fit=max&auto=format&n=C8C-yxJTuKgUzgAP&q=85&s=2e6e8eb3a6d38a69c03ba0ac347d884d" width="1028" height="529" data-path="images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_dee9c6.png" />
</Frame>

Click on `/create` to override which roles can use this command

<Frame caption="Click on /create">
  <img src="https://mintcdn.com/driprewards/C8C-yxJTuKgUzgAP/images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_9c01bc.png?fit=max&auto=format&n=C8C-yxJTuKgUzgAP&q=85&s=caf2d9b888695729a3f385813b0ff680" width="952" height="483" data-path="images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_9c01bc.png" />
</Frame>

Add the roles that should be able to use this permission by clicking the `Add Roles or Members` button

<Frame caption="Add the Roles/Members you want">
  <img src="https://mintcdn.com/driprewards/C8C-yxJTuKgUzgAP/images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_722ec9.png?fit=max&auto=format&n=C8C-yxJTuKgUzgAP&q=85&s=0a7d52afc0fe2b4e868adc1e2f154af5" width="761" height="607" data-path="images/admin-settings/admin-dashboard/admin-settings/admin-permissions/img_722ec9.png" />
</Frame>

<Check>Be sure to save your settings and you are all set!</Check>

Built with [Mintlify](https://mintlify.com).
