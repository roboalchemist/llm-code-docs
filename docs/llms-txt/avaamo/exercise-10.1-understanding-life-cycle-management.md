# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-10-life-cycle-management-and-agent-permission/exercise-10.1-understanding-life-cycle-management.md

# Exercise 10.1: Understanding Life-Cycle Management

Typically the agent goes through different stages in its lifecycle right from the time of its inception to the time it is pushed into production. Agents typically follow Development, Testing, Staging, and production. In the new Avaamo 5.0, you can create users with different roles for collaborating in each stage of the agent lifecycle. This allows teams to develop, test, stage, and deploy agents in a different environment, thereby providing the required compliance.

**10.1.1** **Development**

Users with development roles gather requirements, configure the development environment, start designing and developing agents and skills as well as agents. The developers can also create copies of the agent and then prepare the agent for testing for the testing team.

**10.1.2** **Testing**

Users with a testing role testers can promote agents from development to testing environment, configure the test environment, test the agent’s functionality, and report bugs and issues. Once testing is complete they notify the staging users, to promote the bot from testing to staging.

**10.1.3** **Staging**

Users with the staging role can promote the agents from testing to staging, configure the staging environment, test the agent’s functionality by replicating production instance, report bugs, and issues. Staging users can also pull updates from testing to staging for re-testing the issues reported.

**10.1.4** **Production**

Users with the production role can promote agents from staging to the production environment. Production users can configure the production environment and report bugs and issuers in the live production instance. Production users can also pull updates from staging to production and also apply hot-fixes to the production if and when necessary.

**10.1.5** **Reference Documentation**

See [Plan your development process agent life cycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle), for more information.

Along with these stages, you can assign different roles to the users, to assign different roles:

* Log in to the user profile
* Grant roles such as Development, Testing, Staging, and Production

![](https://lh6.googleusercontent.com/FsTz32cxrkBvVPqnLqOZL6NYZL2ZuubuCp8eBlMWPMN0Nfhwk9BWidBsTFpTsEwIBJVXepVbse8vAOvQZt7ZHefUKiu3F0TY_vrRt8PoIuqLw-hgwd4kJy3LuC2sDnmkhYX_9aE_)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FO3CqSoWSYO2KC3G3cfcz%2FScreenshot%2020-08-2024%20at%2019.15%20\(1\).png?alt=media\&token=46d1b148-bf03-4f4a-81e5-0187770e2c95)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FktmjwatZZwrm78RvaB5R%2FScreenshot%2021-08-2024%20at%2010.25.png?alt=media\&token=af0cd633-bb9e-40cb-9e25-0f89f6ba3bde)

{% hint style="info" %}
**Note:** You can only give access to the users if you have the setting role assigned. If you don’t have the setting role then contact your admin.
{% endhint %}
