# Source: https://docs.portainer.io/2.33-lts/admin/environments/access-groups.md

# Manage access to environment groups

{% hint style="info" %}
Environments can be [grouped](https://docs.portainer.io/2.33-lts/admin/environments/groups) for organizational purposes. If an environment and an individual user are in the same group, users will be tagged with `inherited` on the **Manage access** page. This means that the user is inheriting their access from the group, not the environment.

If you manually assign a user to an environment, and they are already assigned to it via a group, they will be tagged with `override` on the **Manage access** page, indicating that their individual access will override that of the group for this one environment. You can then modify their access in this special case.
{% endhint %}

From the menu expand **Environment-related** then select **Groups**. Locate the environment group you want to give users access to then select **Manage access** at the end of the row.

<figure><img src="https://3850702872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXI7douejaBgpZ6CP2zJf%2Fuploads%2Fgit-blob-99c9e3dbc4ad64c9d99bf9aa1290b89042d4fa93%2F2.20-environments-access-groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

Next, select the users or teams you want to add using the dropdown. Then use the **Role** dropdown to select the role you want this user or team to have.

<figure><img src="https://3850702872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXI7douejaBgpZ6CP2zJf%2Fuploads%2Fgit-blob-2bcbd3e30b7b489ff9eb3c559623c4b6b0bbbae6%2F2.20-environments-access-groups-create.png?alt=media" alt=""><figcaption></figcaption></figure>

Once all have been selected, click **Create access**.
