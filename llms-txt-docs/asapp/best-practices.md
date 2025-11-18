# Source: https://docs.asapp.com/messaging-platform/virtual-agent/best-practices.md

# Best Practices

## Designing your Virtual Agent

### 1. Focus on Customer Problems

The most important thing to keep in mind when designing a good flow is whether it is likely to resolve the intent for most of your customers. It can be easy to diverge from this strategy (perhaps because a flow is designed with containment top of mind; perhaps because of inherent business process limitations). But it's the best way you can truly allow customers to self-serve.

### (a) Understanding the Intent

Since flows are invoked when ASAPP classifies an intent, understanding the intent in question is key to successfully designing a flow. The best way to do this is to review recent utterances that have been classified to the intent and categorizing them into more nuanced use cases that your flow must address. This will ensure that the flow you design is complete in its coverage given how customers will enter the flow.

These utterances are accessible through ASAPP Historical Reporting, in the First Utterance table.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=35d6596fed1596d42b5210219d9877ba" data-og-width="1999" width="1999" data-og-height="931" height="931" data-path="image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=42d81df6dfd1178f7b36ff77b6563d9e 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ab1306ef880ef4a1bbe825e64b1d76fb 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=edd8bca1ef391565412a2445e201f5d4 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8d475570b07450920e47a6baa77e824e 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a10faa3c32af0b13210026787cdb244a 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a89adeb3-7316-62c2-c885-910d111a7d8a.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=6206213f24e5011d983fcc696dbdf20b 2500w" />
</Frame>

### (b) Ongoing Refinement

Every flow you build can be thought of as a hypothesis for how to effectively understand and respond to your customers in a given scenario. Your ability to refine those hypotheses over time--and test new ones--is key to managing a truly effective virtual agent program that meets your customers needs.

We recommend performing the following steps on a regular basis--at least monthly--to identify opportunities for flow refinement, and improve effectiveness over time.

#### Step 1: Identify opportunity areas in particular flows

1. **Flows with relatively high containment, but a low success rate:** This indicates that customers are dropping out of the flow before they receive useful information.
2. **Flows with the highest negative EndSRS rates:** This indicates that the flow did not meet the customer's needs.

#### Step 2: Determine Likely Causes for Flow Underperformance, Identify Remedies

Once you've identified problematic flows, the next step is to determine why they are under-performing. In most cases you'll quickly identify at least one of the following issues with your flow by reviewing transcripts of issueIDs from Conversation Manager in Insights Manager:

**1. General unhelpfulness or imprecise responses**

Oftentimes flows break down when the virtual agent responds confidently in a manner that is on-topic but completely misses the customers' point. A common example is customers reaching out about a difficulty to log in, only to be sent to the same "forgot your password" experience they were experiencing issues with in the first place. Issues of this type typically receive a negative EndSRS score from the customer, who doesn't believe their problem has been solved.

The key to increase the performance of these flows is to configure the virtual agent to ask further, more specific questions before jumping to conclusions. Following the example above, you could ask "Have you tried resetting your password yet?". Including this question can go a long way to ensure that the customer receives the support they're looking for.

**2. Unrecognized customer responses**

This happens when the customer says or wants to say something that the virtual agent is unable to understand.

In free-text channels, this will result in classification errors where the virtual agent has re-prompted the customer to no avail, or has incorrectly attempted to digress to another intent. You can identify these issues by searching for re-prompt language in transcripts where customers have escalated to an agent from the flow in question. Looking at the customers' problematic response, you can determine how best to improve your flow. If customers' response is reasonable given the prompt, you can introduce a new response route in the flow and train it to understand what the customer is saying. Even if it's a path of dialog you don't want the virtual agent to pursue, it's better for the virtual agent to acknowledge what they said and redirect rather than failing to understand entirely.

**Don't:**

* "Which option would you prefer?"
* "Let's do both"
* "Sorry I didn't understand that. Could you try again?"

**Do:**

* "Which option would you prefer?"
* "Let's do both"
* "Sorry, but we can only accommodate one. Do you have a preference?"

Another option for avoiding unrecognized customer responses in free-text channels, is to rephrase the prompt in a manner that reduces the number of ways that a customer is likely to respond. This is often the best approach in cases where the virtual agent prompt is vague or open-ended.

**Don't:**

* "What issue are you having with your internet?"
* "I think maybe my router is broken"
* "Sorry I didn't understand that. Could you try again?"

**Do:**

* "Is your internet slow, or is it completely down?"
* "It's completely down"

In SDK channels (web or mobile apps), which are driven by quick replies, the concern here is to ensure that customers have the opportunity to respond in the way that makes sense given their situation. A common example failing to provide an "I'm not sure" quick reply option when asking a "yes or no" question. Faced with this situation, customers will often click on "new question" or abandon the chat entirely, leaving very little signal on what they intended. The best way to improve quick reply coverage is to maintain a clear understanding of the different contexts in which a customer might enter the flow---how they conceive of their issue, what information they might or might not have going in, etc. Gaining this perspective is helped greatly by reviewing live chat interactions that relate to the flow in question, and determining whether your flow could have accommodated the customer's situation.

**3. Incorrect classification**

This issue is unique to free-text use cases and happens when the virtual agent thinks the customer said one thing, when in fact the customer meant something else. One example would be a response like "no idea" being misclassified as "no" rather than the expected "I'm not sure."

Another example might be a response triggering a digression (i.e., a change of intent in the middle of a conversation), rather than an expected trained response route. This can happen in flows where you've trained response routes to help clarify a customer's issue but their response sounds like an intent and thus triggers a digression instead of the response route you intended. For example:

```
"I need help with a refund"
"No problem. What is the reason for the refund?"
"My flight got cancelled"
"Are you trying to rebook travel due to a cancelled flight?"\<\< Digression
"No, I'm asking about a refund"
```

While these issues tend to occur infrequently, when you do encounter them, the best place to start is revising the prompt to encourage responses that are less likely to be classified incorrectly. For example, instead of asking an open-ended question like "What is the reason for your refund?"---to which a customer response is very likely to sound like an intent---you can ask directly ("Was your flight cancelled?") or ask for more concrete information from which you can infer the answer ("No problem! What's the confirmation number?").

Alternatively, you can solve issues of incorrect classification by training a specific response route that targets the exact language that is proving problematic. In the case of the unclear "I'm not sure" route, a response route that's trained explicitly to recognize "no idea" might perform better than one that is broadly trained to recognize the long tail of phrases that more or less mean "I'm not sure." In this case, you can point the response route to the same node as your generic "I'm not sure" route to resolve the issue.

**4. Too much friction**

Another cause for underperformance is too much friction in a particular flow. This happens when the virtual agent is asking a lot of the customer.

One type of friction is authentication. Customers don't always remember their specific login or PINs, so authentication requests should be used only when needed. If customers are asked to find their authentication information unnecessarily, many will oftentimes abandon the chat.

Another type of friction is repetitive or redundant steps--particularly around disambiguating the customer. While it's helpful to clarify what a customer wants to do to adequately solve their need, repetitive questions that don't feel like they are progressing the customer forward often lead to a feeling of frustration--and abandonment.

#### Step 3: Version, improve, and track the impact of flow changes

Once you've identified an issue with a specific flow, create a new version of it in AI-Console with one of the remedies outlined above. After you have implemented a new version, you can save and release the new version to a lower environment to test it, and subsequently to production. Then, track the impact in Historical Reporting in Insights Manager by looking at the Flow Success Rate for such flow on the Business Flow Details tab of the Flow Dashboard.

### 2. Know your Channels

Messaging channels have advantages and limitations. Appreciating the differences will help you optimize virtual agents for the channels they live on, and avoid channel-specific pitfalls.

To illustrate this, look at a single flow rendered in Apple Messages for Business vs the ASAPP SDK:

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2b09c5623464a16c8206fd68742b556b" data-og-width="1999" width="1999" data-og-height="1939" height="1939" data-path="image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4b8ee3b85d2bade63d218fa56d20b6a1 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=de409081c6bda786c183ed0f67e00163 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b65a4ee58b2076687f34cb46cfbe9e18 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7ab84e04d66555df3a2ee9ba69369388 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=55abc8b9fddf33074069e788339be8e3 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1292d466-63c5-f625-2003-effbc90135a4.jpg?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=70fb79a9845473d594ea05919a7f66ea 2500w" />
</Frame>

<Note>
  The ASAPP SDK has quick replies, while Apple Messages for Business supports list pickers.
</Note>

#### (a) General rules of thumb

* Be aware of each channel's strengths and limitations and optimize accordingly--these are described below.
* Pay particular attention to potentially confusing interface states, and compensate by being explicit about how you expect customers to interact with a flow (e.g., "Choose an option below ...")
* Be sure to test the flow on the device/channel it is deployed to in a lower environment.

#### (b) Channel-specific considerations

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1261d70d837f7027dba0a958a41a33f8" data-og-width="48" width="48" data-og-height="48" height="48" data-path="image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=fcee6e061f7150df6ee37d90b21564d3 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2533676a572f711cd0e2277922b7a4d3 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e6a0c93b49595341c5b5afc3c142d87a 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b130b81eae56efab88b6df020ba97980 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d52de4e3a6b2bef7d85d26ba591f0c73 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c2c43557-dc9f-4bed-0af4-634b9d0a2a63.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a261a996855bbaf041fc5a95874bd9c7 2500w" />
</Frame>

##### ASAPP SDK

The ASAPP SDKs (Web, Android, and iOS) have a number of features that help to build rich virtual agent experiences.

Strengths of SDKs:

1. Quick Replies - surface explicit text options to a customer to tap/click on, and route to the next part of a flow.
2. Authentication / context - with the authentication of customers, the SDK allows for a persistent chat history which provides seamless continuity. Additionally, authentication allows for the direct calling of APIs (e.g. retrieving a bill amount).

Limitations:

* Not as sticky of an experience (i.e. it's not an application the customer has top of mind/high visibility), so the customer may abandon the chat. One cause for this is the lack of guaranteed push notifications -- particularly in the Web SDK.

How to optimize for ASAPP SDKs:

* We encourage you to build more complicated, multi-step flows, leveraging quick replies that keep customers on the rails.

### 3. Promote Function over Form

First and foremost, your virtual agent needs to be effective at facilitating dialog. It may be tempting to prioritize focus on virtual agent tone and voice but that can ultimately detract from virtual agent's functional purpose. Next we'll offer examples that illustrate effective or ineffective dialogs that will help you when building out your flows.

#### (a) It's OK to sound Bot-like

The virtual agent **is** a bot, and it primarily serves a functional purpose. It is much better to be explicit with customers and move the conversation forward, rather than making potential UX sacrifices to sound friendly or human-like. Customers are coming to a virtual agent to solve a specific problem efficiently. Here is a positive example of a greeting that, while bot-like, is clear and effective:

```
"Hello! How can I help you today? Choose from a topic below or type a specific question."
```

#### (b) Tell People How to Interact

Customers interact with virtual agents to solve a problem and/or to achieve something. They benefit from explicit guidance with how they are supposed to interact with the virtual agent. If your flow design expects the customer to do something, tell them upfront. Here is a positive example of clear instructions telling a customer how to interact with the virtual agent:

```
"Please choose an option below so we can best help"
```

#### (c) Set Clear Expectations for Redirects

The virtual agent can't always handle a customer's issue. When you need to redirect the customer to self-serve on a website, or even on a phone number, set clear expectations for what they need to do next. You never want a customer to feel abandoned. Here are two positive examples of very clear instructions about what the customer will need to do next, and what they can expect:

```
"To process your payment and complete your request, you'll need to call us at 1-800-555-5555. **Agents are available** from 8am to 9pm ET, Monday through Friday"
"You can check the status of your order on website by either **entering your order number** or **logging in**".
```

#### (d) Acknowledge Progress & Justify Steps

Think of a bot like a standard interaction funnel -- a customer has to go through multiple steps to achieve an outcome. Acknowledging progress made and justifying steps to the customer makes for a better user experience, and makes it more like for the customer to complete all of the steps (think of a breadcrumb in a checkout flow). The customer should have a sense of where they are in the process. Here's a simple example of orienting a customer to where they are in a process:

```
"We're happy to help answer questions about your bill, but will need you to sign in so we can access your account information."
```

#### (e) Be careful with Personification

Over-personifying your virtual agent can make for a frustrating customer experience:

* **Do** frame language in a more impersonal "we"
* **Don't** make the virtual agent "I"
* **Do** frame the virtual agent as a representative for your company.
* **Don't** give your virtual agent a name / distinct personality.
* **Do** give your virtual agent a warm, action-oriented tone.
* **Don't** give your virtual agent an overly friendly, text-heavy tone.
* **Do** "Great! We can help you pay your bill now. What payment method would you like to use?"
* **Don't** "Great, thank you so much for clarifying that! I am so happy to help you with your bill today."

#### (f) Affirm What Customers Say, Not What the Flow Does

Affirmations help customers feel heard, and they help customers understand what the virtual agent is taking away from their responses. When drafting a virtual agent response, ensure that you match the copy to the variety of customer responses that may precede it -- historical customer responses can be viewed in the utterance table in historical reporting.

If there is a broad set reasons for a customer to end up on a node or a flow, your affirmation should likewise be broad:

* **Do** "We can help with that"
* **Do** "We can help you with your bill"
* **Don't** "We can help you pay your bill online"

Similarly, if there is a narrow set of reasons for a customer to end up in a node or a flow, your affirmation should likewise be narrow. Even then, it's important to not phrase things in such a way that you're putting words in the mouth of the customer, so they don't feel frustrated by the virtual agent.

* **Do** "To set up autopay ..."
* **Don't** "It sounds like you want to set up autopay"
* **Don't** "Okay, so autopay"

In some cases where writing a good affirmation feels particularly tricky, feel free to err on the side of not having one. It's all good so long as the virtual agent responds in an expected manner given what the customer just said.

### 4. Reduce Friction

If interacting with your virtual agent is confusing or hard, people will revert to tried and true escalation pathways like shouting "agent" or just calling in. As you are designing flows, be mindful about the following friction points you could potentially introduce in your flows.

#### (a) Be Judicious with Deep Links

Deep links are used when you link a customer out of chat to self-serve. It is tempting to leverage existing web pages, and to create dozens of flows that are simple link outs. But this often does not provide a good customer experience.

A virtual agent that is mostly single step deep links will feel like a frustrating search engine. Wherever possible, try to solve a customer's problem conversationally within the chat itself. Don't rely on links as a default.

But, when you **do** rely on a deep link, make sure to:

1. Validate the link actually solves the customers intent and is accessible to all customers (e.g. not behind an authentication wall, or only accessible to certain types of customers).
2. Leverage native app links where possible.
3. Be clear about what the customer needs to do when they go to the link and leave the chat experience.

#### (b) Avoid All-or-Nothing Flow Requirements

Be careful with "all or nothing" requirements in a flow; if you want a customer to sign in to allow you to access an API, that's great, but give customers an alternative option at that moment too. Some customers might not remember their password.

When you are at a point in a flow where there is a required step or just one direction a customer can go, think about what alternative answer there could be for a customer. If you don't, those customers might just abandon the virtual agent at that point.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=66d3d7bc66965dfff78b94be8ebc8230" data-og-width="846" width="846" data-og-height="1496" height="1496" data-path="image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9323f4e3db8f0fff8889bb1b4a79efda 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=28402f03b1d9d6b9d9f5a0aeea73d7aa 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=fc547b5b679a11feb5fc565d03ac4b07 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=53af680de5ede15541d50edae31311a6 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0aba0710e11027cb071633675b97a935 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1faaf89d-b0f3-5849-3819-f1d713cc91d7.jpg?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ee63570a3f11a872f1a078cf2c29ba93 2500w" />
</Frame>

### 5. Anticipate Failure

It's tempting to design with the happy path in mind, but customers don't always go down the flow you expect. Anticipate the failure points in a virtual agent, and design for them explicitly.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=13eb83ea5b584bbc59c2be380d06862b" data-og-width="854" width="854" data-og-height="836" height="836" data-path="image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=daf78b02b0d398bc3df45504298419f6 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2133cd13beeaa5d047c0c28f3e085c6b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=476921eeed05a3c0f11b7fe73ee86491 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=eb36cd84b014a1d586a38b7303389b54 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=4a124eea75668df6536d49f82fe4bbf0 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-becca11d-1103-3bc9-0136-314e9c37e768.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=fdd2ec4901132cee35e3512d4de2b8fb 2500w" />
</Frame>

#### (a) Explicit Design for Error Cases

Always imagine something will go wrong when asking the customer to do something:

* When asking customer to complete something manually, give them a response route or a quick reply that allows them to acknowledge it's not working (e.g. the speed test isn't working).
* When asking the customer to self-serve on a web page or in chat: allow them to go down a path in case that doesn't work (e.g. login isn't working).
* When designing flows that involve self-service through APIs: explicitly design for what happens when the API doesn't work.

#### (b) Consider Free Text Errors

In channels where free text is always enabled (i.e.. AMB, SMS), the customer input may not be recognized. We recommend writing language that guides the customer to explicitly understand the types of answers we're expecting. Leverage "else" conditions in your flows (on Response Nodes).

**Don't:**

* "What issue are you having with your internet?"
* "I think maybe my router is broken"
* "Sorry I didn't understand that. Could you try again?"
  **Do:**
* "Is your internet slow, or is it completely down?"
* "I think maybe my router is broken"
* "Sorry I didn't understand that. Is your internet slower than usual, or is your internet completely off?"

## Measuring Virtual Agents

### 1. Flow Success

Containment is a measure of whether a customer was prevented from escalating to an agent; it is the predominant measure in the industry for chatbot effectiveness. ASAPP, however, layers a more stringent definition called "Flow success," which indicates whether or not a customer was actually helped by the virtual agent.

### Important

When you are designing a new flow or modifying an existing flow, be sure to enable flow success when you have provided useful information to the customer.

"Flow success" is defined as when a customer arrives at a screen or receives a response that:

1. Provides useful information addressing the recognized intent of the inquiry.
2. Confirms a completed transaction in a back-end system.
3. Acknowledges the customer has resolved an issue successfully.

With flow success, chronology matters. If a customer starts a flow, and is presented with insightful information (i.e. success), but then escalates to an agent in the middle of a flow (i.e. negation of success), that issue will be recorded as not successful.

### How It Works

Flow success is an event that can be emitted on a [node](/messaging-platform/virtual-agent/flows#node-types "Node Types").

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3c138f6f290497d892e37749288efaee" data-og-width="973" width="973" data-og-height="1999" height="1999" data-path="image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=941b7de05375a34cbc491993a7e9ab36 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b29ff59b969b4c48a15b8d56b2a8daf5 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=11584f7c6fced35373f6979a56b2901b 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7729d8c09535f034f6496238852dddb5 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=726a4478c9b1afcac096a70fb534140c 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13212102-24e9-2e15-aef8-86c92ff5f2a5.jpg?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7648c220dc96e32831076f15186459fe 2500w" />
</Frame>

It is incumbent on the author of a flow to define which steps in the flow they design could be considered successful.

Default settings:

* **Response Nodes:** When flow reporting status is **on**, the **success** option will be chosen by default.
* **Agent Node:** When flow reporting status is **on**, the **failure** option will be chosen.
* **End & Redirect:** Flow success is not available in the tooling. By default, the End Node question will emit or not emit flow success depending on the customer response.

### 2. Assessing a Flow's Performance

You're able to track your flows' performance on the "Automation Success" report in historical reporting. There you can assess containment metrics and flow success which will help you determine whether a flow is performing according to expectations.

## Tactical Flow Creation Guide

### 1. Naming Nodes

Flows are composed of different node types, which represent a particular state/act of a given flow. When you create a flow, you create a number of different nodes.

We recommend naming nodes to describe what the node accomplishes in a flow. Clear node names will make the data more readable going forward. Here are some best practices to keep in mind:

* Response node (no prompt): name is by the content (e.g. "NoBalanceMessage")
* Response node (with prompt): name by the request (e.g. "RequestSeatPreferences")
* Any node that takes an action of some sort should start with the action being taken and end with what is being acted upon (e.g. "ResetModem")

### 2. Training Response Routes

When you create a Response Node that is expected to classify free text customer input (e.g. "Would you like a one way flight or a round trip flight?"), you need to supply training utterances to train a response route. There are some best practices you should keep in mind:

* Be explicit where possible.
* Vary your language.
* More training utterances is almost always better.
* Keep neighboring routes in mind -- what are the different types of answers you will be training, and how will the responses differ between them?

### 3. Designing Disambiguation

Sometimes customers initiate conversations with vague utterances like "Help with bill" or "Account issues." In these cases the virtual agent understands enough to classify the customer's intent, but not enough to immediately solve their problem.

In these cases, you are able to design a flow that asks follow-up questions to disambiguate the customer's particular need. Based on the customer's response you can redirect them to more granular intents where they can better be helped.

Designing effective disambiguation starts with reviewing historical conversations to get a sense of what types of issues customer's are having related to the vague intent. Once you've determined these, you'll want to optimize your prompt and response routes for the channel your designing for:

#### (a) ASAPP SDKs

These channels are driven by quick replies only, meaning that the customer can only choose an option that is provided by the virtual agent. Here, the prompt matters less than the response branches / quick replies you write. Just make sure they map to things a customer would say---even if multiple response routes lead to the same place. For example:

```
We're happy to help! Please choose an option below:
-   Billing history
-   Billing complaint
-   Billing question
-   Something else
```

#### (b) Free-Text Channels, with Optional Quick Replies (Post-iOS 15 AMB)

These channels offer quick replies, but do not prevent customers from responding with free text. The key here is optimizing your question to increase the likelihood that customers choose a quick reply.

```
We're happy to help! Please tap on one of the options below:
-   Billing history
-   Billing complaint
-   Billing question
-   Something else
```

#### (c) Free-Text-Only Channels (Pre iOS 15 AMB, SMS )

These channels are often the most challenging, as the customer could respond in any number of ways, and given the minimal context of the conversation it's challenging to train the virtual agent to adequately understand all of them. Similar to other channels, the objective is to prompt in a manner that limits how customers are likely to respond. The simplest approach here is to list out options as part of your prompt:

```
Please tell us more about your billing needs. You can say things like "Billing history" "Question" "Complaint" or "Something else"
```

### 4. Message Length

Keep messages to be short and to the point. Walls of text can be intimidating. Never allow an individual message to exceed 400 characters (or, even less if there are spaces)..

An example of something to avoid:

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d972bc858c847f686dd65ed439a3a35a" data-og-width="846" width="846" data-og-height="1496" height="1496" data-path="image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4fa1fb1c7193d8242951fd81ca1b27b5 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=29b3c9720f113b771ab5f8a5ba6c3d18 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a0b8aec96427b76e45f29191a4d2adcd 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=272898359c386896d081af0f3335b595 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=18950decc8a5bcf857e25d6c5554dd3f 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d7b8258c-b614-ff7a-ad5a-f94c488d6a9d.jpg?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2cd7cd75a4e65e41ba66839bcb3ddff3 2500w" />
</Frame>

### 5. Quick Replies

Quick Replies should be short and to the point. Some things to keep in mind when writing Quick Replies:

* Avoid punctuation
* Use sentence case capitalization, unless you're referring to a specific product or feature.
* Keep to at least two and up to five quick replies per node.
  * While this is generally best practice, it is required for Quick Replies in Apple Messages for Business.
  * If there are more than 3 Quick Replies, the list will be truncated to the first 3 in WhatsApp Business
* External channels have character limits and any Quick Replies longer than these limits will be truncated:
  * Apple Messages for Business: 24 characters maximum
  * WhatsApp Business: 20 characters maximum
