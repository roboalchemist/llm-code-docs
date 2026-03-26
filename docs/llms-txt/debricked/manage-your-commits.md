# Source: https://docs.debricked.com/product/administration/repositories/manage-your-commits.md

# Manage your commits

After creating several commits or adding a repository with existing commits, it might be important to be able to look back and see the history of the changes. To see a list of all your commits and manage them:

1. Click **Repository Settings** on the left side menu.
2. Go to the **Commits** tab.
3. Click the repository you are interested in.

In this view, you can find a list of all your commits, along with the details:

* Name - The name of the commit.
* Commit Date - The date and time the commit was created.
* Repository - The repository the commit belongs to.
* Branch - The branch the commit was added to.
* Added by - The user by whom the commit was added.

> You can export the filtered and visible data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### **Delete a commit**

If you decide you no longer want to see data from a specific repository and remove it, or if you revert a commit on your end, it might be useful to delete a commit from the list to clean up your data. To do so, click the **trashcan** icon on the far-right column.

### **Retention time of commit data**

Unless you delete the commit data manually, non-default branches will be retained for 30 days, while default branches (*main*, *master*) have an unlimited retention period.

Additionally, enterprise users can tag selected commits as a release by adding the flag `--tag-commit-as-release=true` to the `scan` command in OpenText Core SCA CLI. Storing the commit data indefinitely (they can still be manually removed).

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FhrfcgDkACIZdmJXvRv5g%2Fimage.png?alt=media&#x26;token=f308ec57-58e2-4420-95c7-cb1e01b60a10" alt=""><figcaption></figcaption></figure>
