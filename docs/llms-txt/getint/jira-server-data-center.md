# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/getting-started-with-the-platform-deployment-options-getint-for-jira-data-center-jira-server/jira-server-data-center.md

# Getint for Jira Data Center / Jira Server - Architecture

Jira Server / DC apps are basically installed on the target Jira Server / DC and loaded up within a Jira system, which makes them accessible for the Jira end users. Those Jira Server / DC apps are written mainly in Java with support of Atlassian plugins framework.

Because, as stated on Architecture page, getint.io is a standalone, separate platform, there is still a need to have an instance of getint.io platform installed somewhere. It can be either hosted still by getint.io or installed (as on-premise) on customers owned Linux/Windows servers.

Below diagram, shows simplified architecture of how getint.io cooperates with Jira Server, when getint.io is installed as **On-Premise** software.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MSvBbkykpjkiLXBC9CU%2F-MSvEWSSpsI4x-94BCnt%2FJira_Server_DC_Architecture_OnPremise.png?alt=media\&token=a912db17-dee1-4887-83d2-589e3fd13214)

Components overview

* Getint.io Jira App - its a one of our apps available on Atlassian Marketplace. When its clicked from *Mange Apps* menu, Jira Server / DC will try to load up (Request 1) an iframe with a source from the getint.io platform. \
  Except administration panel (UI), Jira app  is used also for License verification purposes.
* Request 1 - it's a request sent by Jira Cloud in order to load up content within an iframe. That iframe will contain an administration panel of the app where all integrations can be managed as well as whole reporting and other system informations can be accessed. When request is successfully authenticated, UI is loaded up
* All the configurations and reporting data is stored **on the owned by customers servers**&#x20;
* Request 2 - getint.io platform to perform data integration is using standard Jira REST Api. Because all of the requests to Jira REST Api must be authenticated, during integration setup user is asked to provide user credentials (username and password)

{% hint style="info" %}
As can be noticed on the above diagram, with a on-premise deployment mode, getint.io platform and Jira apps are not trying to connect with any servers, including getint.io servers. **That means it is possible to work totally behind firewall.**
{% endhint %}
