# Source: https://www.jenkins.io/doc/book/blueocean/getting-started/

Title: Getting started with Blue Ocean

URL Source: https://www.jenkins.io/doc/book/blueocean/getting-started/

Published Time: Sat, 14 Mar 2026 05:15:53 GMT

Markdown Content:
Getting started with Blue Ocean
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
    *   [Getting started with Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/)
    *   [Creating a Pipeline](https://www.jenkins.io/doc/book/blueocean/creating-pipelines/)
    *   [Dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard/)
    *   [Activity View](https://www.jenkins.io/doc/book/blueocean/activity/)
    *   [Pipeline Run Details View](https://www.jenkins.io/doc/book/blueocean/pipeline-run-details/)
    *   [Pipeline Editor](https://www.jenkins.io/doc/book/blueocean/pipeline-editor/)

*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

[⇑ Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)[Index](https://www.jenkins.io/doc/book/)

[Creating a Pipeline ⇒](https://www.jenkins.io/doc/book/blueocean/creating-pipelines)

Getting started with Blue Ocean
===============================

Table of Contents

*   [Installing Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/#installing-blue-ocean)
    *   [On an existing Jenkins controller](https://www.jenkins.io/doc/book/blueocean/getting-started/#on-an-existing-jenkins-controller)
    *   [As part of Jenkins in Docker](https://www.jenkins.io/doc/book/blueocean/getting-started/#as-part-of-jenkins-in-docker)

*   [Accessing Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/#accessing-blue-ocean)
*   [Navigation bar](https://www.jenkins.io/doc/book/blueocean/getting-started/#navigation-bar)
*   [Switching to the classic UI](https://www.jenkins.io/doc/book/blueocean/getting-started/#switching-to-the-classic-ui)

This section describes how to get started with Blue Ocean in Jenkins. It includes instructions for [setting up Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/#installing-blue-ocean) on your Jenkins controller, how to [access the Blue Ocean UI](https://www.jenkins.io/doc/book/blueocean/getting-started/#accessing-blue-ocean), and [returning to the Jenkins classic UI](https://www.jenkins.io/doc/book/blueocean/getting-started/#switching-to-the-classic-ui).

Blue Ocean status

Blue Ocean will not receive further functionality updates. Blue Ocean will continue to provide easy-to-use Pipeline visualization, but it will not be enhanced further. It will only receive selective updates for significant security issues or functional defects.

[](https://www.jenkins.io/doc/book/blueocean/getting-started/#installing-blue-ocean)Installing Blue Ocean
---------------------------------------------------------------------------------------------------------

You can install Blue Ocean using the following methods:

*   As a suite of plugins on an [existing Jenkins controller](https://www.jenkins.io/doc/book/blueocean/getting-started/#on-an-existing-jenkins-instance).

*   As a part of [Jenkins in Docker](https://www.jenkins.io/doc/book/blueocean/getting-started/#as-part-of-jenkins-in-docker).

### [](https://www.jenkins.io/doc/book/blueocean/getting-started/#on-an-existing-jenkins-controller)On an existing Jenkins controller

When Jenkins is installed on most platforms, the [Blue Ocean](https://plugins.jenkins.io/blueocean) plugin and all necessary dependent plugins, which compile the Blue Ocean suite of plugins, are not installed by default.

Plugins can be installed on a Jenkins controller by any Jenkins user who has the **Administer** permission. This is set through **Matrix-based security**. Jenkins users with this permission can also configure the permissions of other users on their system. Refer to the [Authorization](https://www.jenkins.io/doc/book/security/managing-security/#authorization) section of [Managing Security](https://www.jenkins.io/doc/book/security/managing-security/) for more information.

To install the Blue Ocean suite of plugins to your Jenkins controller:

1.   Ensure you are logged in to Jenkins as a user with the **Administer** permission.

2.   From the Jenkins home page, select **Manage Jenkins** on the left and then **Plugins**.

3.   Select the **Available** tab and enter `blue ocean` in the **Filter** text box. This filters the list of plugins based on the name and description.

![Image 1: Available Blue Ocean plugins after being filtered list.](https://www.jenkins.io/doc/book/resources/blueocean/intro/blueocean-plugins-filtered.png) 
4.   Select the box to the left of **Blue Ocean**, and then select either the **Download now and install after restart** option (recommended) or the **Install without restart** option at the bottom of the page.

*   It is not necessary to select other plugins in this list. The main **Blue Ocean** plugin automatically selects and installs all dependent plugins, composing the Blue Ocean suite of plugins.

    *   If you select the **Install without restart** option, you must restart Jenkins to gain full Blue Ocean functionality.

Refer to the [Managing Plugins](https://www.jenkins.io/doc/book/managing/plugins) page for more information. Blue Ocean does not require additional configuration after installation. Existing Pipelines and projects will continue to work as usual.

The first time you [create a Pipeline in Blue Ocean](https://www.jenkins.io/doc/book/blueocean/creating-pipelines) for a specific Git server, Blue Ocean prompts you for your Git credentials to allow you to create Pipelines in the repositories. This is required since Blue Ocean can add a `Jenkinsfile` to your repositories.

### [](https://www.jenkins.io/doc/book/blueocean/getting-started/#as-part-of-jenkins-in-docker)As part of Jenkins in Docker

The Blue Ocean suite of plugins is not bundled with the official Jenkins Docker image, [`jenkins/jenkins`](https://hub.docker.com/r/jenkins/jenkins/), which is available from the [Docker Hub repository](https://hub.docker.com/).

Read more about running Jenkins and Blue Ocean inside Docker in the [Docker](https://www.jenkins.io/doc/book/installing/#docker) section of the installing Jenkins page.

[](https://www.jenkins.io/doc/book/blueocean/getting-started/#accessing-blue-ocean)Accessing Blue Ocean
-------------------------------------------------------------------------------------------------------

Once a Jenkins environment has Blue Ocean installed and you log in to the Jenkins classic UI, you can access the Blue Ocean UI by selecting **Open Blue Ocean** on the left side of the screen.

![Image 2: Open Blue Ocean link](https://www.jenkins.io/doc/book/resources/blueocean/intro/open-blue-ocean-link.png)

Alternatively, you can access Blue Ocean directly by appending `/blue` to the end of your Jenkins server’s URL. For example `https://jenkins-server-url/blue`.

If your Jenkins controller:

*   Already has existing Pipeline projects or other items present, the [Blue Ocean Dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard) displays.

*   Is new or does not have projects or other items configured, Blue Ocean displays a **Welcome to Jenkins** pane with a **Create a new Pipeline** button. You can select this to begin creating a new Pipeline project. For more information, refer to the [Creating a Pipeline](https://www.jenkins.io/doc/book/blueocean/creating-pipelines) page for more information on creating a Pipeline project in Blue Ocean.

![Image 3: Welcome to Jenkins - Create a New Pipeline message box](https://www.jenkins.io/doc/book/resources/blueocean/creating-pipelines/create-a-new-pipeline-box.png) 

[](https://www.jenkins.io/doc/book/blueocean/getting-started/#navigation-bar)Navigation bar
-------------------------------------------------------------------------------------------

The Blue Ocean UI has a navigation bar along the top of its interface, allowing you to access the different views and features.

The navigation bar is divided into two sections:

*   A common section along the top of most Blue Ocean views.

*   A contextual section below.

The contextual section is specific to the current Blue Ocean page you are viewing.

The navigation bar’s common section includes the following buttons:

*   **Jenkins**: Selecting the Jenkins icon takes you to the [Dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard) or reloads this page if you are already viewing it.

*   **Pipelines**: This also takes you to the Dashboard. If you are already on the Dashboard, this option reloads the page. This button serves a different purpose when you are viewing a [Pipeline run details](https://www.jenkins.io/doc/book/blueocean/pipeline-run-details) page.

*   **Administration**: This takes you to the **[Manage Jenkins](https://www.jenkins.io/doc/book/managing)** page of the Jenkins classic UI. This button is not available if you do not have the **Administer** permission. Refer to the [Authorization](https://www.jenkins.io/doc/book/managing/security/#authorization) section of the Managing Security page for more information.

*   **Go to classic** icon: This takes you back to the Jenkins classic UI. Read more about this in [Switching to the classic UI](https://www.jenkins.io/doc/book/blueocean/getting-started/#switching-to-the-classic-ui).

*   **Logout**: This logs out your current Jenkins user and returns you to the Jenkins login page.

Views that use the common navigation bar add another bar below it. This second bar includes options specific to that view. Some views replace the common navigation bar with one specifically suited to that view.

[](https://www.jenkins.io/doc/book/blueocean/getting-started/#switching-to-the-classic-ui)Switching to the classic UI
---------------------------------------------------------------------------------------------------------------------

Blue Ocean does not support some legacy or administrative features of Jenkins that are necessary to some users.

If you need to access these features, select the **Go to classic** icon at the top of a common section of Blue Ocean’s [navigation bar](https://www.jenkins.io/doc/book/blueocean/getting-started/#navigation-bar).

![Image 4: Go to classic icon](https://www.jenkins.io/doc/book/resources/blueocean/intro/go-to-classic-icon.png)

Selecting this button takes you to the equivalent page in the Jenkins classic UI or the most relevant classic UI page that parallels the current page in Blue Ocean.

* * *

[⇑ Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)[Index](https://www.jenkins.io/doc/book/)

[Creating a Pipeline ⇒](https://www.jenkins.io/doc/book/blueocean/creating-pipelines)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/blueocean/getting-started/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
