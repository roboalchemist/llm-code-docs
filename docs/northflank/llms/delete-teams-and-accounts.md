# Source: https://northflank.com/docs/v1/application/collaborate/delete-teams-and-accounts.md

# Delete teams and accounts

You can permanently delete teams, organizations, and user accounts from their settings pages. Deletion is irreversible and removes all associated data.

To delete a team, organization, or user account, you must be the **owner**. Other team members or organization members cannot delete these entities.

## Delete a team

To delete a team:

1. Navigate to [Team Settings](https://app.northflank.com/s/team/settings)

2. Scroll to the **Danger zone** section

3. Click **Delete team**

4. Confirm the deletion

5. Click **Confirm deletion**

All projects, services, databases, and resources within the team will be permanently deleted.

## Delete an organization

To delete an organization:

1. Navigate to [Organization Settings](https://app.northflank.com/s/teamOrOrg/settings)

2. Scroll to the **Danger zone** section

3. Click **Delete organization**

4. Confirm the deletion

5. Click **Confirm deletion**

All teams, billing information, and organization data will be permanently deleted.

## Delete your user account

To delete your user account:

1. Navigate to [Account Settings](https://app.northflank.com/s/account/settings/profile)

2. Scroll to the **Danger zone** section

3. Click **Delete account**

4. Confirm the deletion

5. Click **Confirm deletion**

Your account, all teams you own, and all associated data will be permanently deleted.

## Important warnings

**Deletion is permanent and irreversible**

Once deleted, you cannot recover:

- Projects, services, and databases

- Backups and data

- Billing history

- Team or organization settings

- Custom domains and configurations

**Active resources**

Ensure all running services, databases, and workloads are stopped before deletion. Active resources may continue to incur charges until fully terminated.

**Team and organization ownership**

If you're the only owner:

- Transfer ownership to another member before deletion, or

- Delete the team/organization entirely

If there are other owners, they can continue managing the team/organization after you leave.

## Before deleting

**Backup your data:**

- Export any important data from databases

- Save configuration files and templates

- Download logs and metrics if needed

**Review invoices or usage:**

- Any pending invoice will have to be paid

- Any remaining usage will be billed on account deletion

Ensure there are no remaining questions regarding billing before proceeding.

**Notify team members:**

- Inform team members if you're deleting a shared team or organization

- Give them time to backup data they need

## Next steps

- [Build from a Git repository: Start building from your linked Git repositories in minutes.](/v1/application/build/build-code-from-a-git-repository)
- [Run an image continuously: Deploy a built image as a continuously-running service.](/v1/application/run/run-an-image-continuously)
