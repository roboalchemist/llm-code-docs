# Source: https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle.md

# Plan your development process (Agent life cycle)

Typically, any agent goes through different stages in its life cycle from inception to production  - Development, Testing, Staging, and Production. You can leverage the Avaamo Platform to iteratively design and build agents through all these different stages of the life cycle followed in any enterprise product development. This approach enables:

* **Structured release management process**: You can develop, test, stage, and then deploy the agents in different environments within the Avaamo Conversation AI Platform. Based on your roles and permission, you can promote an agent from one stage to another in its life cycle. When an agent is promoted, an exact clone of the agent is created in the promoted environment. Users with the required roles can work on the agent in the promoted environment without affecting the agent in other stages. See [Stages in agent lifecycle](#stages-in-agent-life-cycle), for more information.&#x20;
* **Different teams to participate and collaborate:** This approach also allows different teams to participate and collaborate in different stages of the agent life cycle. See [Roles in the agent life cycle](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions#roles-in-agent-life-cycle), for more information on how to assign the required roles and permissions for users in different stages of an agent life cycle.

The following illustration depicts the life cycle of an agent in the Avaamo Platform:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-E1v0tKiEsDCVWTkux%2F-M-EPdPAlSqQi_xLOWXH%2Fhowto-agent-life-cycle-flow.png?alt=media\&token=9165049f-356f-4b1c-b3dd-872f55e965b6)

See [How does it work?](#how-does-it-work) to understand the completed workflow of an agent life cycle.

## Stages in the agent life cycle

The agent life cycle is comprised of various stages in which an agent is deployed and executed within the Avaamo Conversation AI Platform:

* **Development**: This is the environment in which the development team originally develops

  &#x20;the agents, skills, and configurations around agents.<br>
* **Testing:** This is the environment in which the testing team perform either manual testing or&#x20;

  automated checks using a tool like regression testing to test and certify the functionality (new and changed) of the agents and skills.<br>
* **Staging**: This is an environment for testing that exactly resembles a production environment. It seeks to mirror an actual production environment as closely as possible and may connect to other production services, using production or other pre-production integrations system configurations. <br>
* **Production**: The production environment is also known as live, as it is the environment that users directly interact with. Deploying agents to production is the most sensitive step and mostly done by very specific teams with access to a production system where the Avaamo agent is integrated. A production environment includes sensitive access information with which agents are integrated such as API access token of other production systems, system username password of other production systems.&#x20;

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-E1v0tKiEsDCVWTkux%2F-M-ENN7ioY98XDG8l0uc%2Fhowto-agent-life-cycle.png?alt=media&#x26;token=e6d6eb44-ad16-407e-a4d4-b3d0914c8182" alt=""></div>

## How does it work?

Broadly, the following lists a typical workflow in an agent life cycle:

{% hint style="info" %}
**Note**: See [Design agents](https://docs.avaamo.com/user-guide/how-to/build-agents/design-agents), for more information on best practices for building agents in the Avaamo Platform.
{% endhint %}

### Create users and roles

Identify a team of people responsible for working in different stages of an agent's life cycle. Create users and assign required roles to collaborate and participate in different stages such as Development, Testing, Staging, and Production. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LvdsyQnqj-6R0oBub2_%2F-Lvdwh3B9Ny0mueeenMT%2Fhowto-agent-life-cycle-roles.png?alt=media\&token=d5791ac2-9eae-43bb-aeca-a923f232a28b)

### **Development**&#x20;

The following illustration depicts a typical workflow of an agent in the development stage:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LveKBEU41s0n5R-xGYq%2F-LveKbyhxdl-73wOztxL%2Fhowto-agent-life-cycle-dev.png?alt=media\&token=7d442cd1-f56e-4ac5-a8cd-558c3d38e671)

* Gather all the requirements for developing an agent. Start and plan from a small definitive set of requirements.
  * Developers can start designing the agent by learning all the best practices. See [Design agents](https://docs.avaamo.com/user-guide/how-to/build-agents/design-agents), for more information.
  * Build the agent either from scratch or by importing from sample agents. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
  * Developers must ensure to test their agents incrementally using Simulator. See [Simulator](https://docs.avaamo.com/user-guide/build-agents/test-agents#simulator), for more information.&#x20;
  * Developers can use debugging tools such as Debug logs, JSErrors, or Conversation history to analyze and fix defects. See [Debug agents](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents), for more information. Individual skills can also be debugged using insights and logs provided at the skill level.
* Once the first iteration of development is completed, the developer notifies a tester and provides at least view permission for the agent to the tester. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

{% hint style="success" %}
**Key points (Development)**:

* Involve only Developers during agent development.
* Perform unit testing at each stage as you develop agents.
  {% endhint %}

### **Testing**&#x20;

The following illustration depicts a typical workflow of an agent in the testing stage:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LveKBEU41s0n5R-xGYq%2F-LveKSyqkUkp1337Q9zr%2Fhowto-agent-life-cycle-testing-stage.png?alt=media\&token=df26056a-3aa5-479c-9b7e-f697bc7fe872)

* The tester promotes the agent from development to testing stage,
  * A tester can use manual checks or automated checks tools such as Regression testing to test the agents. See [Regression Testing](https://docs.avaamo.com/user-guide/build-agents/test-agents#regression-testing), for more information.&#x20;
  * During testing, testers communicate with the developers to fix issues and defects. The developer fixes these issues in the development stage that can be pulled by the tester using the **Pull updates** option. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-E1v0tKiEsDCVWTkux%2F-M-EOeAyQ_tqHIwU0T85%2Fhowto-agent-life-cycle-development.png?alt=media\&token=9e1f4e88-4bfc-4c23-87a8-952920bad3d5)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Et-YgBlovDtNxbYEy%2F-M-F7X4mtRIwpCtCvJ3X%2Fuser-role-testing.png?alt=media\&token=6cb547de-1db4-481c-b689-eea9fbb031b6)

* Once the testing is completed and certified, the tester notifies a staging user and provides at least view permission for the agent to the staging user.

{% hint style="success" %}
**Key points (Testing)**:

* Involve only Testers in the Testing phase.
* Perform thorough regression testing on your agents.
  {% endhint %}

### **Staging**

The following illustration depicts a typical workflow of an agent in staging:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LveLF1DonWpxWi6e3t_%2F-LveSsGyBFfxlMCy_xrx%2Fhowto-agent-life-cycle-staging-stage.png?alt=media&#x26;token=475fde36-0fdc-4a98-8e12-a583cacb3440" alt=""></div>

* The staging user promotes the agent from testing to the staging stage.&#x20;
  * During staging, a staging user may connect to other production services, using production or other pre-production integrations system configurations.&#x20;
  * Similar to the testing stage, the staging user communicates with the developers to fix issues and defects. The developer fixes these issues in the development stage that can be pulled into testing and then staging using the Pull updates option. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Et-YgBlovDtNxbYEy%2F-M-F8CQSDOQfB0M0QBk-%2Fhowto-agent-life-cycle-testing.png?alt=media\&token=8166b5b8-4a62-4ff2-9d95-c1dabece322a)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Et-YgBlovDtNxbYEy%2F-M-F8plzymcD7KaGbH7a%2Fuser-role-staging.png?alt=media\&token=842062de-07e5-42e5-aa74-c602f2774e59)

* Once the staging environment is stable, the staging user tester notifies a production user and provides at least view permission for the agent to the production user.

{% hint style="success" %}
**Key points (Staging)**:

* The staging environment must be an exact replica of your production environment.
* Perform thorough testing on your agent before moving to production.
  {% endhint %}

### **Production**

The following illustration depicts a typical workflow of an agent in production:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LvkMQtZ4QfmGfHJalPO%2F-LvkOIFlsh0D8qSwVJtA%2Fhowto-agent-life-cycle-production.png?alt=media&#x26;token=6a0693d3-0850-4565-99ea-07de62d4cc61" alt=""></div>

* The production user promotes the agent from staging to the production stage.
  * This is where the agent is live, as it is the environment that users directly interact with.
  * Any defects or issues that require hotfixes can be implemented in the production environment itself. However, a production user must ensure to communicate the same to the developer working on the same agent in the development environment. This ensures that the changes are implemented in the development instance and any pull's from the development does not overwrite the changes to the production hot-fixes.
  * If there are any major changes required, then it is recommended that the agent goes through the complete cycle beginning from the development stage.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Et-YgBlovDtNxbYEy%2F-M-F9Q_IJ4J-BQ3qI57_%2Fhowto-agent-life-cycle-staging.png?alt=media\&token=b97c2e13-758e-4d67-a381-162a7fb0f541)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Et-YgBlovDtNxbYEy%2F-M-FAg-OSZ8PGp09vu8H%2Fuser-role-production.png?alt=media\&token=d9e8ae6d-e2eb-4dd4-84d0-8fa2dc114962)

Improvements and enhancements to an agent is an iterative process and the cycle from development to production continues. Avaamo Platform provides several tools and roles to monitor the performance of the agents. These can be used to continuously improve the agent to provide a better user experience. See [Monitor agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze), for more information.

{% hint style="success" %}
**Key points (Production)**:

* Do not perform any testing or debugging in the production environment.
* Do not perform any load or regression testing in the production environment. Such testing must be done in the staging or testing environment.
  {% endhint %}

## Key points

It is recommended to make a note of the following key points applicable to the agent life cycle:

* An agent can be promoted from one stage to another only once. Once promoted, you cannot revert the operation. However, you can delete the promoted agent and promote it again from its previous stage.
* When an agent is promoted to the next stage,
  * The user who promoted the agent is the owner of the agent in the promoted stage. As an owner of the agent, the owner can also add other team members as required.
  * The first step as an owner of the agent in any stage is to configure the agent with variables specific to the environment. See [Define environment variables](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-environment-variables), for more information.
  * An exact clone of the agent is created in the promoted environment. Users with the required roles can work on the agent in the promoted environment without affecting the agent in other stages.&#x20;
* The user in the promoted environment can use the Pull updates option available for each promoted agent to pull the updates from the previous stage.&#x20;
* Note that not all agent details are promoted or pulled from one stage to another when you promote or pull updates. See [What are not promoted or pulled?](https://docs.avaamo.com/user-guide/build-agents/manage-agents/promote-and-pull-updates#what-are-not-promoted-or-pulled) for more information.
* Currently, all the notification process between stages is outside the scope of the platform and must be handled externally.
