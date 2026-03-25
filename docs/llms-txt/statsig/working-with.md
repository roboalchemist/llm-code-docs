# Source: https://docs.statsig.com/dynamic-config/working-with.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Dynamic Config

> Learn how to use configuration parameters to control your application behavior in near real-time.

A dynamic config allows you to use configuration parameters to control the behavior of your application in near real-time.

In the example below,
the dynamic config called **localization** allows you to retrieve localized strings for users in different countries.
Users in Spanish speaking countries see Spanish strings, while users in French and Korean speaking countries see French and Korean strings respectively.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/working-with/129110998-d2d1cb31-cd87-4f93-81f0-21ab64565763.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=86778df9801a6789408fc2e43d83d975" alt="Dynamic config localization interface" width="1006" height="1074" data-path="images/dynamic-config/working-with/129110998-d2d1cb31-cd87-4f93-81f0-21ab64565763.png" />
</Frame>

A sample JSON payload for French speakers is also shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/working-with/129111399-c3f0354e-f55d-43fc-b49c-f74eac89bc11.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=6eb0220e8d97700f3608bd3c71f7c294" alt="JSON payload example for French localization" width="604" height="536" data-path="images/dynamic-config/working-with/129111399-c3f0354e-f55d-43fc-b49c-f74eac89bc11.png" />
</Frame>

The following tutorials show you how to perform common tasks with dynamic configs.

#### Tutorials

* [Create a dynamic config](/dynamic-config/create-new)
* [Create a rule for a dynamic config](/dynamic-config/add-rule)
* [Use a language specific Statsig SDK to implement a dynamic config in your application](/sdks/getting-started)


Built with [Mintlify](https://mintlify.com).