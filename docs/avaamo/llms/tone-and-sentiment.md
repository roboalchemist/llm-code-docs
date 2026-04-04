# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/tone-and-sentiment.md

# Tone and sentiment

When a user query is posted to the Avaamo Platform, it inspects the query to detect tones such as (anger, fear, and happiness) and sentiment (positive, negative, neutral) in the user query. The platform has a set of default platform handlers for these emotions to respond back to the user appropriately. The tone is the emotion of the user expressed in the query. Sentiment explores attitudes, feelings, and expressed opinions of the user with respect to your agent.&#x20;

Tone and sentiment can be used to build dialog strategies to adjust the conversation accordingly and hence improves user experience. It can be used to:

* **Enhance Customer Service:** You can monitor customer conversations so you can respond to your customers appropriately and at scale. Use Tone & Sentiment detection to improve your agent's conversational flows by analyzing which flows are leaving your customers happy or frustrated.&#x20;
* **Switch to Live Agent:** The platform can auto-recognize user requests to talk to an agent or if it is not able to successfully handle user requests multiple times or if the user explicitly requests to auto-transfer to a live agent.
* **Build "tone-based" dialog strategies:** Re-direct your customers to the appropriate dialog strategy based on their detected tone & sentiment. For example, a customer who is having a negative experience can be re-directed to a reward or upgrade flow, a survey, or simply switched to a live agent.
* **React with a "human" touch:** At times based on the user's reactions, say anger, you can drive the agent to react with a sad emoji, an encouraging quote, or a friendly message. This gives a human touch to your agent.

Additionally, you can also utilize these sentiment analyzers for analyzing the conversations to either change flows or respond with appropriate messages as per your business requirement. See [Programmatically handling tone/sentiment](#programmatically-handle-tone-sentiment), for more information.

### Tone and Sentiments

Avaamo Platform can detect the following tones from the user query:

| Tone      | Example                                   |
| --------- | ----------------------------------------- |
| Anger     | I am having the worst experience with you |
| Fear      | I am worried my card will be misused      |
| Happy     | You are perfect!                          |
| Sad       | this is depressing                        |
| Surprised | Oh my! that is good to know               |
| Urgency   | Hurry up! I wanted it yesterday           |

Avaamo Platform can detect the following sentiments from the user query:

| Sentiment | Example                   |
| --------- | ------------------------- |
| Positive  | I like this agent         |
| Negative  | I hate this agent         |
| Neutral   | I want to open an account |

You can view the detected tone and sentiment in the message insights. Click the **eye icon** below the user query to know the tone and sentiment of the query:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU5oToQ9vVoJ2U7RGrHGW%2Fimage.png?alt=media\&token=26f8459f-bb63-477f-9042-2c875da25b43)

### Core skills and sentiment analysis

Avaamo's NLU engine comes bundled with a set of Core skills that can syntactically and semantically analyze user messages and automatically categorize these user messages into appropriate behavior buckets.&#x20;

Some examples of sentiments and user tone that the core skills can understand are:

* **Greeting Phrases**:  Avaamo's NLU engine can auto-recognize and respond to greeting messages such as "Hi", "Hello", "Good morning", "GM" and many variants of greetings.
* **Thank You**: Avaamo's NLU engine can auto-recognize and respond to various user messages to mean "Thank you" and several of its variants
* **Transfer to Agent:** The platform can auto-recognize the user request to talk to an agent or if it is not able to successfully handle user requests multiple times or if the user explicitly requests to auto-transfer to a live agent.
* **Frustration:** The platform can auto-recognize various frustration-related phrases as well as the tone that can indicate that the user is frustrated and you can choose to either send the user through an appropriate flow or pass the user to an agent to respond to the user.&#x20;

### Programmatically handle tone/sentiment

In addition to these core skills, Avaamo also allows developers for analyzing the conversations to either change flows or respond with appropriate messages as per your business requirement. Examples:&#x20;

* You can create Smalltalk skills that can handle a lot of mundane, rhetorical, and simple questions that users might ask, allowing the agent to respond without having to trigger a flow.&#x20;
* User tone and sentiment can also be programmatically utilized within the flow. This information is available in the context insights (`context.insights.tone, context.insights.sentiment`) and accessible via JavaScript in the flow.&#x20;

See [Detect user tone and sentiment](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/detect-user-tone-and-sentiment), for an example.
