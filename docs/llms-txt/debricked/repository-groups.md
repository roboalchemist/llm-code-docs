# Source: https://docs.debricked.com/product/administration/repositories/repository-groups.md

# Repository groups

It can be difficult to get a quick overview of all your repositories, especially if you have a lot of them. To make your life a bit easier, the OpenText Core SCA tool enables you to group repositories together, allowing you to organize your projects, e.g. based on team structure.

A group can consist of multiple repositories, but also other groups. It is also possible for one group to exist as a sub-group in multiple parent groups. Keep in mind that changes made to a group will have an effect in all places the group exists.&#x20;

You can create groups from the repository view under **Repositories.** To create groups:

1. Go to **Repositories** on the left side menu.

   <figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FMHJxvnifXd4dPSTmU4Nw%2FRepository1.png?alt=media&#x26;token=bdec8442-f1a5-4625-875e-0653b6fa3a91" alt=""><figcaption></figcaption></figure>
2. Click **+ New** and select **Group**.

   <figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2F6uo2b2bsjwVjwJxHk4gk%2Fimage.png?alt=media&#x26;token=862dc281-ad1b-44dd-917e-3a5360d99ea1" alt=""><figcaption></figcaption></figure>
3. On the **New group** window:
   1. Enter the **Group name**.
   2. Select the repositories for the group. You can associate multiple repositories to the group by selecting repositories from **Choose repositories** drop-down and creating new rows by clicking the plus button.
   3. Select the default branch for the repository. You can allocate default branch to the repository by selecting branch from **Default branch** drop-down in each row only if a repository is selected in that row. This option is disabled if you select multiple repositories in a row. If you do not manually select the default branch, the system will automatically choose it based on the last commit.
4. Select the relevant **Groups**.
5. Click **Create**.

Once created, the group will be shown with the name and aggregation of vulnerabilities in the linked repositories and groups. You can also view the default branch details in the repositories tab of repo groups.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2Fb5Wa1s9zUMj4wkGnknkX%2FRepository2.png?alt=media&#x26;token=3ed5986d-c0ed-4f3d-ab82-b60280c47032" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;'AUTO' is displayed only if the system has selected the default branch.&#x20;
{% endhint %}

### **Delete or edit a repository group**

You can edit or delete a specific group by clicking on the three dots next to the group’s name. Clicking **Edit** will open the same view as when creating the group, enabling you to select or deselect repositories or groups included in the group. Keep in mind that if you delete a group, all groups that exist solely within this group will also be deleted.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2Fbx5tcVfhxhMkjwihmlko%2Fimage%20(3).png?alt=media&#x26;token=25136128-e13f-492f-a2fd-72ba92528bbe" alt=""><figcaption></figcaption></figure>

### Export repository group table data

You can export the filtered and visible data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*
