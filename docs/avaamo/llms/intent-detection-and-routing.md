# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/intent-detection-and-routing.md

# Intent detection and routing

Universal agents detect the intent and route the conversation to the appropriate member that can fulfill the user’s request in the best possible way. It leverages the training imparted to the individual members for intent detection and hence no duplication of training is required. This provides a seamless experience to the user.

Agent routes requests to the appropriate member agent for simple Q\&A or multi-turn conversations, renders member responses inline, and also manages the conversation context. See [Context management](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/context-management), for more information.

{% hint style="success" %}
**Key point**: When you are in the transactional flow with a member agent and a user query is posted, then&#x20;

* The user query is routed to the current member agent first for intent detection.&#x20;
* If the user's intent does not match the current member agent's intent, only then it is routed to the rest of the member agents for further intent matching.&#x20;
* If the conversation is already in a transactional flow and a query results in disambiguation, then the disambiguation options also are within the context of the member agent that is currently in the transactional flow. This setup allows the Universal agent to keep the conversation within the context of a member agent when there are shared intents between member agents. See [Disambiguation](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/disambiguation), for more information.
  {% endhint %}

The following illustration depicts an "Acme Enterprise" Universal agent linked with independent virtual agents such as - Acme HR, Acme IT, and Acme Finance.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Foy1A5o7xqQ0qHH6XBq4S%2Fintent-detection-routing.png?alt=media\&token=1e2c7072-603c-41e4-af3a-c22478389095)

Each agent is trained independently. For example, the Acme HR agent has a Q\&A skill with intents and responses.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPdZdiYFLP8YihQdykMpw%2Facme-hr.png?alt=media\&token=62c90d11-9870-4b67-a580-a15815e1e41d)

When a user query such as "When is the bonus paid this year?" is posted to the Acme Enterprise Universal agent, the Universal agent routes the user's intent to the appropriate member agent, Acme HR in this case, and renders the response in the Acme Enterprise assistant itself.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FqcusUHxDagBePLpqmiMp%2Facme-hr-response.png?alt=media\&token=73cf0ec0-8b8b-48bc-93ee-db067bdaaf72)
