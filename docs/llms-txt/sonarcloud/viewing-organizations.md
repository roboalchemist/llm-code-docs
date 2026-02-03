# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations.md

# Retrieving your organizations

You can view any free or paid plan organization if you’re a member.

### Listing all your organizations <a href="#listing-organizations" id="listing-organizations"></a>

This procedure explains how to open your account’s **Organizations** page.

{% hint style="info" %}
From the Organizations page, you can leave an organization. With the appropriate permissions, you can also create, delete, or upgrade an organization.
{% endhint %}

To list your organizations:

1. Select your account menu in the top right corner of the SonarQube Cloud interface.
2. In the menu, select **View all** in front of **My Organizations**.&#x20;
3. The **Organizations** page opens with the list of organizations you’re a member of.
4. The `Admin` tag indicates that you're an admin of the organization.

![](broken-reference)

### Retrieving and viewing your organization <a href="#viewing" id="viewing"></a>

To retrieve your organization, you can:

1. Select your account menu in the top right corner of the SonarQube Cloud interface. In the menu, under **My Organizations**, select the organization you want to view.
2. Alternatively, open the **My Projects** page and select the organization hyperlink in the projects list.

<figure><img src="broken-reference" alt="Your organizations are clearly displayed in different parts of the SonarQube Cloud UI, where appropriate."><figcaption></figcaption></figure>

The organization record opens as illustrated below:

1. Organization's avatar and name. \
   The avatar is a small image representing the organization. As an organiziation admin, you can add one, see [#change-details](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings#change-details "mention").
2. Button to navigate to the [bound DevOps organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop).&#x20;
3. Organization's navigation bar.
4. Organization key.
5. Organization's subscription plan.

<figure><img src="broken-reference" alt="The top of the SonarQube Cloud Projects page shows you the organization&#x27;s name, icon of the DevOps platform the organization is bound to, if it&#x27;s a public or private organization, and your organization&#x27;s Key."><figcaption></figcaption></figure>

You can navigate through the different pages by using the Organization's navigation bar (some pages require specific access permission) :

* **Projects**: This page lists the [projects](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/projects "mention") belonging to the organization and to which you have access.
* **Quality Profiles**: This page allows authorized users to manage the quality profiles available by language for the organization’s projects. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/introduction "mention") for more information.
* **Rules**: This page allows the retrieval of [rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules "mention") available in the organization through its quality profiles.
* **Quality Gates**: This page allows authorized users to manage the quality gates available for the organization’s projects. See [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention") for more information.
* **Members**: This page lists the organization's members and allows the organization admins to manage them. See [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more information.
* **Billing & Upgrade**: This page allows the organization admins to manage the organization's subscription. See Managing your subscription [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/introduction "mention") for more information.
* **Administration**: This menu allows the organization admins to access various administration menus.

### Retrieving any free organization <a href="#free-organization" id="free-organization"></a>

* If you know the organization key, go to `sonarcloud.io/organizations/<YourOrganizationKey>.`
* Otherwise, in the top navigation bar of the SonarQube Cloud UI, select **Explore** or go to [`sonarcloud.io/explore/projects`](http://sonarcloud.io/explore/projects), and select an organization.
