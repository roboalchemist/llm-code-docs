# Source: https://docs.rundeck.com/docs/learning/

Title: Learning Rundeck

URL Source: https://docs.rundeck.com/docs/learning/

Markdown Content:
1.   [Rundeck | Runbook Automation Documentation](https://docs.rundeck.com/docs/)
2.   [Learning Rundeck](https://docs.rundeck.com/docs/learning/)

[Learning Rundeck](https://docs.rundeck.com/docs/learning/#learning-rundeck)
----------------------------------------------------------------------------

PagerDuty provides three different process automation versions. The open source version is Rundeck. Previously, the commercial version was referred to as Rundeck Enterprise, since renamed as Runbook Automation Self-Hosted for the traditional on premise product and Runbook Automation SaaS available as a hosted cloud platform.

The Learning section includes _[Tutorials](https://docs.rundeck.com/docs/learning/tutorial/)_, a _[Getting Started section](https://docs.rundeck.com/docs/learning/getting-started/)_ and _[How to Guides](https://docs.rundeck.com/docs/learning/howto/)_ that help new users quickly become productive with the Rundeck server and tools. Instructions are provided for both Enterprise and Community versions of Rundeck.

The _[Tutorials](https://docs.rundeck.com/docs/learning/tutorial/)_ are practical step-by-step guides for getting Rundeck installed, configured and running on your system. They are built around our Welcome Project and provide product simulations for the open source Rundeck, Runbook Automation Self-Hosted and Runbook Automation versions.

The [How To Guides](https://docs.rundeck.com/docs/learning/howto/) provide step by step instructions for accomplishing specific tasks using Runbook Automation and where applicable, Rundeck. New How To guides are developed and added periodically as our team realizes a need for them.

[Where to Begin](https://docs.rundeck.com/docs/learning/#where-to-begin)
------------------------------------------------------------------------

### [Essential Concepts](https://docs.rundeck.com/docs/learning/#essential-concepts)

Several essential concepts underly and drive the Rundeck system. Understanding them will help you more effectively use and integrate Rundeck into your environment. New users are encouraged to review the concepts provided in the [Getting Started section](https://docs.rundeck.com/docs/learning/getting-started/jobs/) and the terms in the [Terminology](https://docs.rundeck.com/docs/learning/tutorial/terminology.html) section.

### [Using Rundeck](https://docs.rundeck.com/docs/learning/#using-rundeck)

If a running Rundeck instance isn't already available to you, there are a couple ways you can try it.

#### [Welcome Projects](https://docs.rundeck.com/docs/learning/#welcome-projects)

Both the commercial (Runbook Automation) and open source (Rundeck) versions have a companion set of code at the following links. These code bases allow running automation in a Docker environment with the Welcome Project preloaded.

*   Runbook Automation: [https://github.com/rundeckpro/welcome-project](https://github.com/rundeckpro/welcome-project)
*   Rundeck: [https://github.com/rundeck/welcome-project-community](https://github.com/rundeck/welcome-project-community)

Use the [Welcome Projects Starter How To guide](https://docs.rundeck.com/docs/learning/howto/welcome-project-starter.html) to learn how to get started with these environments.

License Required

Note: The Runbook Automation Self-Hosted version will require a license file. If you are not currently a Runbook Automation customer and you’re interested in using that please [contact us here](https://www.rundeck.com/see-demo).

Warning

It is possible to run the Welcome Projects in other environments, but some exercise steps will need to be adjusted for your specific environment

#### [Download and Install](https://docs.rundeck.com/docs/learning/#download-and-install)

Get the latest release at our [download](https://download.rundeck.com/) site and install the Rundeck software. There are several package formats. Choose the one that best suits the target infrastructure.

After installation, be sure Rundeck has been started.

Tips

See [Startup](https://docs.rundeck.com/docs/administration/maintenance/startup.html) to learn how to startup and shutdown rundeck.

The default port for the web interface is `4440`. If you installed Rundeck on your local machine, go to this URL: `http://localhost:4440`

### [Login](https://docs.rundeck.com/docs/learning/#login)

Rundeck requires every user to login. The default installation defines an "admin" user with access to perform all actions. Use "admin" for username and password.

![Image 1: Login form](https://docs.rundeck.com/docs/assets/img/fig0202.png)

Login form
