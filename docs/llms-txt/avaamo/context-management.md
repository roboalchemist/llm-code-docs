# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/context-management.md

# Context management

Universal agents allow switching of intents mid-way through a dialog from one member agent to another. When multiple-member agents are participating in a conversation, the Universal agent can switch the conversational flow back and forth between the member agents based on the context of the conversation and the requirement of the user - without losing track of the flow.&#x20;

This ability of the Universal agent to switch contexts between member agents without losing the flow of the conversation and produce the desired outcome is called **Intent switching**.

In the following illustration, a user starts a conversation with a request to update the address.&#x20;

* This is a Dialog skill in Acme HR agent which is a part of the Universal agent Acme Enterprise.
* However, in the middle of the conversation, the user switches to another intent asking about employee Id. This is a Q\&A skill in Acme IT agent which is also a part of the Universal agent Acme Enterprise.&#x20;
* You can observe, how the conversations switch seamlessly based on the user intent, and later when the user switches back with the Employee ID, the conversation resumes with the Dialog skill flow in the Acme HR agent.&#x20;
* The conversation and context are retained without losing track of the flow.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoqD4r1CImNmDxrwQW45e%2Fcontext-management.png?alt=media\&token=901a64eb-70d7-4e33-9b5c-f7003a524159)
