# Source: https://docs.axonius.com/docs/exporting-roles-and-permissions-to-csv.md

# Exporting Roles and Permissions to CSV

You can export a list of all existing roles and what permissions each role has to a CSV file. Exporting to a CSV aids in compliance as the date-stamped file indicates the roles and permissions granted at a specific date and time.

Each column in the CSV represents a permission. Each row represents a different role. For each role, the table lists whether the permission is "Allowed" or "Denied".

* **Allowed** - The role is granted the permission.
* **Denied** - The role is NOT granted the permission.

The CSV file name is "roles\_TIMESTAMP.csv". The timestamp includes the date in the YYYY-MM-DD format and the time in the hh:mm:ss format with the time zone. For example: `roles_2024-12-09T11-56-40UTC.csv`.

**To export roles and permissions to CSV:**

* From the Roles page, click **Export to CSV**. The file is downloaded to your default downloads folder.
  ![Roles-ExportToCSV.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Roles-ExportToCSV.png)

This is an example of the output:

![Roles-ExportToCSVResults.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Roles-ExportToCSVResults.png)