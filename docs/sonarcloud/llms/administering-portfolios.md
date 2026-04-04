# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios.md

# Administering portfolios

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

A portfolio is a set of projects within an enterprise that enables an aggregate view of its state through various lenses, including releasability, security, reliability, and maintainability.

{% hint style="info" %}
Before you can view the Enterprise-level reports, your organization must be added to an enterprise. For more information, see [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention").
{% endhint %}

### Permissions <a href="#permissions" id="permissions"></a>

To create a portfolio or a portfolio permission template, you must first be granted access by an Enterprise administrator. The permissions to administer, edit, or view a portfolio are granted by the portfolio administrator in the portfolio settings.

#### Create Portfolios permission <a href="#create-portfolios-permission" id="create-portfolios-permission"></a>

The Enterprise administrator permission is required to grant the **Create Portfolios** permission to users.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6cf8dcf836c6b6c4efb70274703d9fa6ef9c41e1%2Fcreate-portfolio-permission.png?alt=media" alt="Navigate to the Enterprise permissions page to assign the Create Portfolios permission."><figcaption></figcaption></figure>

1. Retrieve your enterprise. See [retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention").
2. Go to **Administration** > **Enterprise Permissions** to access a list of members in all of your organizations.
3. Use the toggle switch to add the **Create Portfolios** permission for the enterprise **Admins** and **Creators**.

#### Administer, edit, and view permissions <a href="#administer-edit-and-view-permissions" id="administer-edit-and-view-permissions"></a>

As an administrator of a portfolio, you can assign users and groups permission to **Administer**, **Edit**, and **View** portfolios to selected users and groups.

* **View**: Users can view the portfolio’s **Overview**, **Portfolio** **Breakdown**, and **Measures** tabs. On the **Portfolio** **Breakdown** page, users can only view the projects they have access to (Browse permission).
* **Edit**: Users can change the portfolio definition (add or remove projects) and delete a portfolio. However, they can only add or remove projects they have access to (Browse permission).
* **Administer**: Users can change the portfolio’s permissions.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a8656066d0e86caedcaa771274ac941717954508%2Fe1d315a4bcb6a5b7ebafee4ed8089bd3dd3dd293.png?alt=media" alt="Each member can be granted Administrator, Edit, or View permissions on the Portfolio Permissions page."><figcaption></figcaption></figure></div>

1. Go to **My Portfolios** in the top navigation and select your enterprise from the drop-down menu.
2. Select the portfolio you want to add the permissions to from the Portfolios home page
3. Go to **Settings** > **Permissions**
4. Assign users and groups the **Administer**, **Edit**, and **View** permissions or select **Apply Permission Template**. The Filters sidebar allows you to find users by **Type**, **Role**, and **Organization**.

### Portfolio permission templates <a href="#permission-templates" id="permission-templates"></a>

Portfolio permission template defines the portfolio-related permissions granted to groups and members of your enterprise. Enterprise administrators can define several permission templates in your organization including a default template. Using permission templates allows you to:

* Grant or revoke different sets of permissions to users or groups.
* Set a default template for new portfolios.

#### Creating portfolio permission templates <a href="#creating-permission-templates" id="creating-permission-templates"></a>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-942173906be4b9bdf9927bd28e64512a8029a588%2F19c7ec259c988b509a0b65f2118e6b2e53471688.png?alt=media" alt="It is possible to create Portfolio Permissions templates that can be assigned to users."><figcaption></figcaption></figure></div>

The Enterprise administrator permission is required to create permission templates:

1. Retrieve your enterprise. See [retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention").
2. Select **Administration** > **Portfolio Permission Templates**.
3. Select **Create new template** at the top right of the page.
4. Enter the **Template Name** and **Description** in the modal.
5. Assign users and groups the **Administer**, **Edit,** and **View** permissions. The Filters sidebar allows you to find users by **Type**, **Role**, and **Organization**.

#### Editing portfolio permission templates <a href="#editing-permission-templates" id="editing-permission-templates"></a>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-8ac92f00f9808186a57169f6b0701d2980ebbcec%2F1fb10a38c8582f7cb4c7a98f71a45514beb95b50.png?alt=media" alt="Select the three-dots to manage and edit an individual Portfolio Permissions template."><figcaption></figcaption></figure></div>

To edit an existing permission template:

1. Go to **My Portfolios** in the top navigation and select your enterprise from the drop-down menu.
2. Select **Administration** > **Portfolio Permission Templates**.
3. From your permission template’s **Actions** menu you can set the template as default for new portfolios, edit permissions, update name and description or delete the template.

{% hint style="info" %}
If you update a portfolio permission template, the changes are not reflected in any previously created or updated portfolios using that template.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention")
* [viewing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-portfolios "mention")
* [managing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios "mention")
