# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects.md

# Retrieving projects

You can view any public project. You can view a private project of your organization provided you have the corresponding permission.

### Retrieving any public or private project <a href="#any-project" id="any-project"></a>

In the top right corner, select the magnifier icon. The **Search for projects…** box is displayed along with a list of pre-selected projects as illustrated below. the project name (1) is followed by the respective organization name (2). The yellow star (3) indicates that the project belongs to your favorite projects.

<figure><img src="broken-reference" alt="When searching for a project in SonarQube Cloud, a list of project appears showing you the project name, organization to which it belongs, and notes if it&#x27;s marked as a favorite project."><figcaption></figcaption></figure>

You can enter a part of the project name in the box to filter the search and select the project in the list. The project opens as illustrated below:

1. Project's avatar and name.
2. Project's visibility ([public or private](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/projects)).
3. Icon of the DevOps platform to which the project is [bound](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop). You can select it to navigate to the bound DevOps platform repository.
4. Project's navigation bar.

<figure><img src="broken-reference" alt="SonarQube Cloud project record"><figcaption></figcaption></figure>

### Retrieving the projects of your organization <a href="#organization-projects" id="organization-projects"></a>

1. Retrieve your organization:
   1. Select your account menu in the top right corner of the SonarQube Cloud interface.
   2. In the menu, under **My Organizations**, select your organization. The organization’s **Projects** page opens.
2. In the left sidebar, you can define filter conditions.
3. Above the list, you can use the search box to search by project name.
4. Click the project name hyperlink to open the project.

### Retrieving your favorite projects <a href="#your-projects" id="your-projects"></a>

To mark a project as favorite, see the instructions on the [managing-your-project-as-developer](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/managing-your-project-as-developer "mention") page.

To retrieve your favorite projects:

1. In the top navigation bar, select **My Projects**. Your favorite projects are listed on the page.
2. In the left sidebar, you can define filter conditions.
3. Above the list, you can use the search box to search by project name.
4. Click the project name hyperlink to open the project.

### Exploring open-source projects <a href="#any-public-project" id="any-public-project"></a>

To explore open-source projects:

* Select **Explore** in the top navigation bar of the SonarQube Cloud UI.
* Or go to `sonarcloud.io/explore/projects`.

### Viewing and copying project information <a href="#viewing-project-information" id="viewing-project-information"></a>

1. Retrieve the project as explained above.
2. In the left navigation bar, select **Information** to open the page.

The **Information** page displays:

* The quality gate currently being used for your project.
* The quality profiles currently being used for your project. If the project contains multiple languages, the profile for each language is shown.
* The project and organization keys; you can copy them for pasting.
* The last analysis method: the method used for this project’s most recent analysis. If the last analysis was done by automatic analysis, this section will display *Analyzed by SonarQube Cloud*. If the last analysis was done by CI-based analysis, the CI system used will be indicated.

See these articles for tasks you can complete while on the **Information** page:

* [#subscribing-to-notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-project-as-developer#subscribing-to-notifications "mention")
* [#using-project-badge](https://docs.sonarsource.com/sonarqube-cloud/managing-your-project-as-developer#using-project-badge "mention")
