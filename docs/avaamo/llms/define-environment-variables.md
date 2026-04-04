# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-environment-variables.md

# Environment variables

You can define environment variables from the **Configuration -> Environment variables** option. These are constants that can be accessed anywhere in the agent and are global to all users of the agent. **Examples**: External service access credentials like web service login credentials, webservice\_username, webservice\_password.&#x20;

The environment variables are used to configure the environment details when an agent is promoted from one stage to another.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can configure an agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the **Configuration -> Environment variables** tab, specify the **name** and **value** of the environment variable and click **Add.**

{% hint style="success" %}
**Key point**: You must specify the variable names according to the Javascript variable standards. See [JavaScript Variables](https://www.w3schools.com/js/js_variables.asp), for more information.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mcx7GfFrAnBqKQZUIuq%2F-Mcx8XFhR57ak3jKffF2%2F5.7-env-variable.png?alt=media\&token=dfc10cfd-62b0-46aa-bb5d-0aaf2f0cb776)

* You can add multiple environment variables as required. Use **Delete** option in the Actions column to delete an environment variable.
* Click **Save.**

{% hint style="info" %}
**Note**: You can also access the environment variable in the JS code. See[ Get environment variables](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-environment-variables), for an example.
{% endhint %}
