# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/advanced-administration/integrating-projects-with-compass.md

# Integrating projects with Compass

Monitoring your Atlassian Compass can be done using the SonarQube Cloud Quality Gate application to add scorecards and metric cards to any of your [components](https://developer.atlassian.com/cloud/compass/components/what-is-a-component/) in Compass. These cards will tell you what the current status of your quality gate.

A scorecard is a set of criteria that you apply to a component to measure its health. The SonarQube Cloud Quality Gate scorecard tells you whether your project’s quality gate is passing (100% score) or failing (0%), prompting you to address the root cause of the failure of your project.

### Integrating your project with Atlassian Compass <a href="#integrating-your-project-with-atlassian-compass" id="integrating-your-project-with-atlassian-compass"></a>

The SonarQube Cloud Quality Gate app is already listed in the Atlassian Compass App Catalog.

Configuration of the app takes place within Atlassian Compass itself. Here are the main steps you need to complete setup of your project:

* Create a user token in SonarQube Cloud to authenticate SonarQube Cloud to Atlassian Compass
* Start the configuration process of the app
* Add the token to complete authentication within Compass
* Add your SonarQube Cloud project to your Compass component

### Generating a SonarQube Cloud user token <a href="#generating-a-sonarcloud-user-token" id="generating-a-sonarcloud-user-token"></a>

First of all, you need to create a user token in SonarQube Cloud for which will be used to authenticate SonarQube Cloud Quality Gate app to Atlassian Compass. To generate a token, to go **Account** > **My Account** > **Security.** There you can see a list of your existing tokens.

Enter a name for your token, for example, *My Compass Token*, and select **Generate Token**. Make sure to copy the token and save it immediately before you dismiss the notification or leave this screen. Otherwise, you may have to start the process again. You will need to enter this token during the configuration process later in Compass.

### Configuring the SonarQube Cloud Quality Gate app in Compass <a href="#configuring-the-sonarcloud-quality-gate-app-in-compass" id="configuring-the-sonarcloud-quality-gate-app-in-compass"></a>

{% hint style="info" %}
Note that these steps take place within Atlassian Compass. For more details on how Compass works, see the [Atlassian Compass](https://developer.atlassian.com/cloud/compass/getting-started/get-started-using-Compass/) help center.
{% endhint %}

1. Go to your Atlassian Compass account.
2. Select **Apps** from the top navigation bar in Compass. Search for the SonarQube Cloud Quality Gate app.
3. Select **Configure**. This takes you to the configuration page.
4. Select ***Allow Access***. This takes you to the authorization screen to allow SonarQube Cloud access to your Atlassian account.
5. Select **Accept**. The configuration screen appears.
6. Enter the user token you created and saved earlier in SonarQube Cloud in the **Access Token** field and click **Connect**.

You can now add your projects to your Compass components.

### Integrating SonarQube Cloud projects with Atlassian Compass <a href="#integrating-sonarcloud-projects-with-atlassian-compass" id="integrating-sonarcloud-projects-with-atlassian-compass"></a>

You now need to go to your SonarQube Cloud account and copy the URL of the project that you want to integrate with Compass.

Then, go to **Atlassian Compass** > **Components** and select your component.

On your team’s dashboard on the right hand side, enter the URL saved in the project field, along with a text to display as the name of your project. Then refresh your screen.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e2844dd01454ec6cbd646f6d1afd12975addf621%2F96f640c5000c14bfa8f2f1de77c929bd461e3a8e.png?alt=media" alt="Add your SonarQube Cloud URL to the project list in Compass." width="266"><figcaption></figcaption></figure></div>

Once you have refreshed your screen, you can view the Scorecard and Metric for your project. The status of your project will be updated every hour and you’ll receive a warning if your quality gate has failed in SonarQube Cloud.

To remove an existing SonarQube Cloud project from Atlassian Compass, just click on the **X** button to the right of the project field (highlighted above).

You can also view the current ratings of your components under the **Health** tab in Compass. Under Health, there are sub-tabs for both Scorecards and Metrics. There you can see a list of your apps and the components that the apps are applied to.
