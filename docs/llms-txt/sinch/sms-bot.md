# Source: https://docs.sinch.com/sms/sms-bot.md

# SMS BOT

### **What is a BOT?**

BOTS are robots structured through an intelligence to automate and standardize human care in a pre-determined task or exercise.

### **Example of a BOT?**

On the platform itself, you can view and use a few BOT templates to collect users’ Opt-in via SMS or perform NPS searches, but BOTS can be used for many other purposes according to your business.

### **How Does an SMS BOT Work?**

The SMS BOT works actively, i.e., you need to send a message with the desired BOT to start it all.

After sending the message, the BOT records and acts in the messages replied to by the recipients for up to 7 days; after that, you need to send a new message from the same BOT or a different BOT so that recipients that have not interacted can reply.

(If a user is in the middle of the flow and you send them a new BOT, the previous flow will be interrupted and the user will go to the flow of the new BOT).

Below we have a few terms that are used when we talk about building an SMS BOT:

* Steps are the different messages that make up the BOT’S flow and can be sent or not to recipients according to the replies received by the BOT.
* Message Text is the text that the person will actually receive in the message, in that step.
* Replies are Keywords that the BOT recognizes in the replies it received from users and through which it triggers new messages or performs actions in the flow.
* Mnemonics or Synonyms are different spellings for a same reply that a step accepts. For example, if a step accepts the reply YES, you can set up the BOT to recognize different ways of spelling YES, such as Y, Sin, Yeah, Si, Yup, Yea, etc.
* "Name on Report" is the way in which different mnemonics are grouped to be recorded in reports. You can determine the name you wish for a group of Mnemonics accepted in one of the replies of a step of the BOT’S flow to be recorded in the reports.

### **How to Build an SMS BOT?**

To create an SMS BOT, just access **messaging** with your login and password and follow the step by step below:

1. Expand the **Flow Builder** option under the menu on the left of the screen and click on “SMS BOT”:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F6mVBXGDP5CQkRftAPBKf%2Fimage.png?alt=media\&token=4d3de940-70b6-4522-bb8b-bc1168b7e5d6)

2\. To create a new BOT, click the “+New SMS BOT” button, which is in the upper right corner of the screen

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPYWyqNTaU3ksjFhPAOOt%2Fimage.png?alt=media\&token=ed182ed6-22c2-48f5-8c87-d5423424e581)

3\. Then you will see a screen such as the one shown in the image below, where you can use templates for NPS Searches, Opt-in, and create a new BOT with the flow you want:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fh4uD6xffiNy2f4yK6GZl%2Fimage.png?alt=media\&token=696e9219-7f33-4e71-a31e-fc5c1e1cbecb)

4\. By clicking to create a blank flow, you can make a few settings such as: **adding a step and the replies expected from users.**

* **You will have 70 characters to set up your messages.**
* **Remember not to use accentuations.**

***To the side, you can view a drawing of how the decision tree is looking for the bot you are creating.***

6\. Create a new step and give it a name. Then include the question that will be sent via SMS in the field “Message text”.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FOCH4OJkWywpVTooHwKxF%2Fimage.png?alt=media\&token=e11ce31d-c07d-4dd0-8a64-661b4eaa7b09)

In the “replies” field, you must include potential user replies.

In the “Terms for reports” field, you must include an intuitive name that will show up in the report on that reply.

In the “Actions” field, you must include which action the bot should take if the user’s reply is the one included above.

**7.** After these steps, you can include as many steps as you deem necessary for your BOT to fulfill its purpose.

It is very important that, after building the entire desired flow, you click the button “Create” on the lower right corner of your screen to save your BOT.

{% hint style="warning" %}
**Important: It is still not possible to change an SMS BOT after it is created, therefore, if you need to edit an SMS BOT, you must create a NEW SMS BOT based on the existing BOT.**
{% endhint %}
