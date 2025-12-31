# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/disambiguation.md

# Disambiguation

When the response to a user query is found in more than one member agent (more than one member agent has the same intent), the Universal agent disambiguates between the responses by listing the member agents that have the response - the names of the first two member agents are displayed; the **More Options** link lists the names of the other member agents that have a response.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRjxcC3OxXbwBYr9L6q1Q%2F6.1-disambiguation.png?alt=media\&token=f7e12c7d-9deb-410e-bbe4-4a4c743dd946)

Once the member agent responds, all subsequent queries in the workflow (regardless of whether intents span over more than one agent) are answered by the same member agent. This is applicable even in the case of disambiguation. If subsequent query results in disambiguation, then disambiguation options also are within the context of the member agent that is currently in the transactional flow. This setup allows the Universal agent to keep the conversation within the context of a member agent when there are shared intents between member agents.&#x20;

Similarly, when a member agent has more than one response (more than one intent is available for the response), disambiguation options are provided for the user to select the context for the response.
