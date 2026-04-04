# Source: https://docs.upsun.com/projects/delete-project.md

# Delete a project

To delete a project, you must be an organization owner or have the [manage plans permission](https://docs.upsun.com../administration/users.md#organization-permissions).

To delete an Upsun project, including all data, code, and active environments:

 - Run the following command:

```bash {}
upsun project:delete --project <PROJECT_ID>
```

 - Read the consequences to deletion and enter ``y``.

 - Enter the project title to confirm.

You are billed only for the portion of a month when the project was active.

When you remove all your projects from your user account,
you stop being charged.

