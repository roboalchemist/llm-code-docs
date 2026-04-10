# Source: https://docs.deepconverse.com/product-docs/chatbots/advanced-functionality/channel-specific-functionality/calendly.md

# Calendly

DeepConverse now supports integrating with the calendly app with our chatbots which enables the user to be able to schedule an event or a meeting right from the chatbot without having to go to their calendly account. \
\
\
**Here's how to integrate Calendly with DeepConverse chatbot:** \
\
1\) In oder to Integrate Calendly with DeepConverse Chatbot, once has to have an account on calendly. If you do not have one, please create an account. \
\
2\) Once the account is created on Calendly, the home page looks something like this ![Screenshot\_2022-03-10\_at\_5.14.31\_PM.png](https://help.deepconverse.com/hc/article_attachments/4678272822548/Screenshot_2022-03-10_at_5.14.31_PM.png)

&#x20;

3\) Click on the gear icon next to the "New Event Type" and copy the meeting URL for your profile where the scheduled events can be tracked and managed. \
\
4\) On the flow builder, select calendly add-on and paste the calendly URL which you copied in the above step and it should look like this:&#x20;

&#x20;

![Screenshot\_2022-03-10\_at\_5.22.17\_PM.png](https://help.deepconverse.com/hc/article_attachments/4679520822164/Screenshot_2022-03-10_at_5.22.17_PM.png)

&#x20;

5\) Add a rule with two options where one is for a successful event generation and the other one is for an unsuccessful one, looking something like this: \
\
![Screenshot\_2022-03-10\_at\_6.54.49\_PM.png](https://help.deepconverse.com/hc/article_attachments/4679709849492/Screenshot_2022-03-10_at_6.54.49_PM.png)

&#x20;

6\) Click on the edit icon on one of the events created, to assign conditions for the above to trigger based on a successful or failed event creation. \
\
![Screenshot\_2022-03-10\_at\_6.57.40\_PM.png](https://help.deepconverse.com/hc/article_attachments/4679764280468/Screenshot_2022-03-10_at_6.57.40_PM.png)

Here, we have added a condition where we took **calendlyPayload** as a field to check for the event generation information and if the same is empty, it means an event is not created and if it's not empty that means an event is generated and the payload has the information related to the event. \
\
\
7\) Once the above steps are performed, the chatbot successfully integrated with **Calendly** will open up a calendar within the chatbot for the user to select a date and time and then enter the basic details like the username and email id so that the event invite will be forwarded to the same. \
\
![Screenshot\_2022-03-10\_at\_7.02.22\_PM.png](https://help.deepconverse.com/hc/article_attachments/4679909218580/Screenshot_2022-03-10_at_7.02.22_PM.png)\ <br>

&#x20;

Here's an example of a flow which was created which depicts the details about the calendly integration with the chatbot.&#x20;

&#x20;

![Screenshot\_2022-03-10\_at\_5.10.58\_PM.png](https://help.deepconverse.com/hc/article_attachments/4679968249492/Screenshot_2022-03-10_at_5.10.58_PM.png)
