# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-5-building-a-dialog-skill/exercise-5.2-creating-a-conversation-flow.md

# Exercise 5.2: Creating a conversation flow

We will be using a sample ServiceNow instance for my integration here. The mandatory fields to create a ticket are Short description, Description and Urgency.&#x20;

* Our first node will be used to capture the short description, let us create the first node:

![](https://lh4.googleusercontent.com/D6Tx5I45z8ydJsekHZgta0RuQ-FjZqp2jcsKCk_k37j0ncXcXmD4lzWWPmWqFG-TOhCYoQCmvs6Wm25Vptf-8-CZlGgWRVYqQrWzV1uRR3l0tkoTj3YCXm2SCA6ln8gK814DChNk)

* Our Second node will be used to capture a detailed description of the issue reported. Let us create node 2.

![](https://lh5.googleusercontent.com/lJsnAzZ38ixftUBF7NmX-7lO21t7pGeyKbLYqvBJeYeYR55c3VVz7phjFDiTC74URMmFCWFhSsLa87BrcLVWBaSxhKdgP3jiHiaEs-uAYpiKR3JkNj7RH6LYKCfUGJ3mlN5EOxBU)

* Our third node will be used to capture the urgency of the ticket. Lets use a quick reply to show the urgency. The buttons will be:
  * High
  * Medium
  * Low
* Select the post message option for each of the buttons added to a quick reply.

![](https://lh5.googleusercontent.com/k06U1Wmfmd7vm84Ej5Y3KaQ3EWTuaG7Bb5ro0HMPFTp5r1r2yxaskaENmESytexJW8UIyDWV73biPads47IThgMVmfr0qIdhk0sUxBBNWW1jOU2oikGLwRDbxptyoqQ5d5969ljC)

![](https://lh4.googleusercontent.com/HLeufFeZl0L-S1DXEYXoE_s95XISnVbLJ7VNYiGOeVpvHPLhKbXCiQ7iDBJvFay6jOrRvxciPg5EC289X7KJipNPYF3mjDHZwe-Rns9ZEXk7oAfAm8eeeN-SGrJWjuKLUdLYc7_T)

* At the end your conversation tree will look like above. Create a blank node 4, will be used to integrate with the service desk.

{% hint style="info" %}
**Tip**: It is good to have validation for each node, for example, you can check if the short description is too short, or you can even check if the user entered the right urgency. You can use your validation code in post-processing.
{% endhint %}

Documentation that describes how to create a new dialog is found at this link: [Create a new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill)
