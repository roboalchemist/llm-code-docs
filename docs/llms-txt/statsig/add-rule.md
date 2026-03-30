# Source: https://docs.statsig.com/segments/add-rule.md

# Source: https://docs.statsig.com/dynamic-config/add-rule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Rules

> Learn how to add targeting rules to dynamic configs to control which users receive specific configurations

## Add a rule to a dynamic config

To add new user targeting rules to a dynamic config,

* Log into the Statsig console at [https://console.statsig.com](https://console.statsig.com)

* On the left-hand navigation panel, select **Dynamic Configs**

* Select the dynamic config where you want to add a rule

* Click the **Add Targeting** button

* Click the **Add New Rule** button

* Select the criteria for identifying the users you want to target:

  * You can target users based on common attributes such as their operating system as shown below

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/add-rule/129112226-51978083-d007-4697-88b5-f3a080eabf48.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=b066fbe0537d6083f727ff73cbf67e92" alt="Operating system targeting rule configuration" width="500" height="448" data-path="images/dynamic-config/add-rule/129112226-51978083-d007-4697-88b5-f3a080eabf48.png" />
  </Frame>

  * You can target users in a defined [segment](/segments) as shown below

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/add-rule/129112427-27351aaf-074e-4997-91d8-6e1e7941b991.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=adeacdbc4a4f139534d76148dc2d7d1d" alt="User segment targeting rule configuration" width="500" height="446" data-path="images/dynamic-config/add-rule/129112427-27351aaf-074e-4997-91d8-6e1e7941b991.png" />
  </Frame>

  * You can target users who are eligible for a specific feature gate as shown below; this ensures that the dynamic config is activated only for users who're exposed to the target feature gate

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/add-rule/129112612-d881981c-4fc6-4e95-a9c5-18319c02d6f2.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=aff9fe0829f374137e365a2154d8863d" alt="Feature gate targeting rule configuration" width="498" height="448" data-path="images/dynamic-config/add-rule/129112612-d881981c-4fc6-4e95-a9c5-18319c02d6f2.png" />
  </Frame>

* To complete the dynamic config, click on the **Edit** link to open the JSON configuration editor. In the editor, type the configuration parameters and values that your application should receive and click **Confirm**

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/dynamic-config/add-rule/129113189-30e7e7da-7559-4d3a-8bd3-74a6ccb7afe2.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=8baf1b3f452707ff687c59eea98616d7" alt="JSON configuration editor interface" width="600" height="536" data-path="images/dynamic-config/add-rule/129113189-30e7e7da-7559-4d3a-8bd3-74a6ccb7afe2.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).