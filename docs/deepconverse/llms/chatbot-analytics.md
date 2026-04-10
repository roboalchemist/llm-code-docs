# Source: https://docs.deepconverse.com/product-docs/analytics/chatbot-analytics.md

# Chatbot Analytics

The analytics page for a chatbot provides insights into how the chatbot is performing. It also includes details around the answers being used, resolutions, guides and feedback being given from customers. We walk through the different analytics sections.

{% tabs %}
{% tab title="Overview" %}
The overview tab gives a high level picture of your chatbot performance it includes the following metrics.

| Metric                       | Definition                                                                                                                                                                                                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sessions                     | Number of chat conversations that were started                                                                                                                                                                                                              |
| Self Service Rate            | (Number of conversations without agent handover / Total number of conversations) x 100                                                                                                                                                                      |
| Confirmed Resolutions        | Number of conversations with confirmed helpful feedback and no handoff to agents                                                                                                                                                                            |
| Informed                     | Number of conversations where an answer was presented to inform the customer                                                                                                                                                                                |
| Agent Handovers              | Number of conversations with request to speak with an agent or escalation                                                                                                                                                                                   |
| Time in widget               | Time spent by the customer in chat (in seconds)                                                                                                                                                                                                             |
| Conversation Count over Time | <p>Visualization showing:<br></p><p><strong>X axis</strong> - shows date of conversation </p><p><strong>Y axis - N</strong>umber of conversations</p>                                                                                                       |
| Top Level Metrics over time  | <p>Combined visualization showing:<br><br><strong>X axis</strong> - shows date of conversation <br><strong>Y axis</strong> <br><br>- Conversations<br>- Agent Handoffs<br>- Resolved Conversations<br>- Successful Conversations<br>- Self Service Rate</p> |

### Chat Widget

| Metric            | Definition                                                         |
| ----------------- | ------------------------------------------------------------------ |
| Locale Breakdown  | Visualization showing the top locales                              |
| Device Breakdown  | Visualization showing the devices used to interact with the widget |
| Browser Breakdown | Visualization showing the browser used to interact with the widget |

### Flows

Top flows being used in chat conversations&#x20;
{% endtab %}

{% tab title="Answer Performance" %}
Answer performance tab looks at the various answers being provided and their feedback from customers.

| Metric                                        | Definition                                                                                                                                                        |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sessions                                      | Number of chat conversations that were started                                                                                                                    |
| Self Service Rate                             | (Number of deflected conversations  / Total number of conversations) x 100                                                                                        |
| Informed                                      | Number of conversations where an answer was presented to inform the customer                                                                                      |
| Confirmed Resolution                          | Number of conversations with confirmed helpful feedback and no handoff to agents                                                                                  |
| Conversations leading to Confirmed Resolution | The visualization shows a waterfall of the number of conversations and how many were informed (shown an answer) and times people confirmed it helped.             |
| Types of Answers Presented                    | <p>Breakdown of the answer presented <br>- Link<br>- Article<br>- Guide<br>- Flow</p>                                                                             |
| Top Answers                                   | This table provides a list of the Answer titles, url and number of times it is presented in a conversation and number of distinct times its used in conversations |
| Answer Feedback                               | This table provides a list of the answers and times customers said provided helpful (positive) and not helpful (negative) feedback.                               |
| Top Answers to review                         | Answers which customers have indicated are not helpful.                                                                                                           |
| Top Links Clicked                             | URLs clicked by customers in answers and in the chatbot                                                                                                           |

### Guides in Chat Conversations

If you are using Guides in the chatbot you will see the interactions feedback here.

| Metric                      | Definition                                                                                      |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| Guides used in Conversation | Shows the Guide names, url and the number of times it is used in conversations                  |
| Guide Feedback              | Shows the number of times customers said Guide was helpful (positive) or not helpful (negative) |
|                             |                                                                                                 |
| {% endtab %}                |                                                                                                 |

{% tab title="Customer Satisfaction" %}
If you are capturing feedback from customers interacting with the chatbot you can view it here.&#x20;

| Metric                   | Definition                                                                                                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overall CSAT             | Shows the overall CSAT for the chatbot on the scale of 1-5                                                                                                                                   |
| Number of Responses      | Total number of csat responses                                                                                                                                                               |
| Rating Distribution      | Breakdown of rating by number of conversations                                                                                                                                               |
| CSAT Responses           | <p>Responses given by the customers. Each response can include:<br><br>Rating (1-5)<br>Feedback (Tags)<br>Comments (Free text comment)<br>Outcome (Issue resolved / Issue not resolved) </p> |
| Avg. CSAT over time      | CSAT Rating over time                                                                                                                                                                        |
| Outcome Distribution     | Breakdown of the outcome                                                                                                                                                                     |
| Positive Feedback Detail | <p>Breakdown of the positive feedback:<br><br>- Efficient Chat<br>- Friendly<br>- Helpful Resolutions<br>- Knowledgeable Support<br>- Understood by needs</p>                                |
| Negative Feedback Detail | <p>Breakdown of the positive feedback:<br><br>- Did not understand<br>- Technical issues<br>- Took too long<br>- Unfriendly<br>- Unhelpful answers</p>                                       |
| {% endtab %}             |                                                                                                                                                                                              |
| {% endtabs %}            |                                                                                                                                                                                              |

### Filtering

In order to drill down further you have the following filters available:

| Filter              | Definition                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| Date Range          | Select the time period for which you would like to view the analytics. (Defaults to last week)         |
| Conversation Action | See analytics based on the specific action in the analytics                                            |
| Dimensions          | You can track custom dimensions such as product, utm params etc. and filter analytics to drill deeper. |

### Timezone

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FadpnN3mO22NPMYlp44O1%2Fimage.png?alt=media&#x26;token=f9e40dee-d444-48eb-a7cd-c4aaa022516b" alt=""><figcaption></figcaption></figure>

You can change the timezone from the top right dropdown.

### Exports

You can use the right most **Export** button to export the current view as a PNG or PDF to share.
