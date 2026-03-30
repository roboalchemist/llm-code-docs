# Source: https://docs.sinch.com/ia-conversational/untitled-10.md

# Creating a new bot

*Are you working on an existing project? Then you don't need to set up a new one. Feel free to skip ahead to the next tutorial:* [Adding content to your bot/tutorials/tutorial-adding-content](https://docs.chatlayer.ai/tutorials/tutorial-adding-content)

## Creating a new bot <a href="#creating-a-new-bot" id="creating-a-new-bot"></a>

What better way to learn how to build a bot than building one! To help you get started, we'll go through a bot-building tutorial together. In this tutorial, you will create a bot called Choo Choo: a digital assistant that can help people book train tickets.

{% hint style="warning" %}
To get started, you need a Chatlayer account. **Don't have an account yet?** [Create a trial account here](https://chatlayer.ai/try-now/)**.** Have a problem with your account? Contact our support team [here](mailto:support@chatlayer.ai).
{% endhint %}

1.Go to <https://app.chatlayer.ai/> and log in using your credentials

2\. To build a new bot, click the blue `+ Add bot` button:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtYkFkZ-E07BxtJ63%2Fimage.png?alt=media\&token=bb7eac66-47f1-403d-b130-20ee6a26570b)

3\. Choose "Start from scratch". You can add template bots to your account later

<div align="center"><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzwNGl7eJPFCnIqd2Qi9E%2Fimage.png?alt=media&#x26;token=c31fc342-eb52-4155-8667-3e7d25ef3af6" alt=""></div>

4\. Now enter `Choo Choo + your first name` as the name of the bot, so you can easily find it again after

5\. Then select your primary language. This is the language that your bot will use. If you'd like to create a multilingual bot, you can add extra languages.

6\. Now click `Create` to create your new bot!

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FiCNOGZn4Iy6iUEBAJheo%2Fimage.png?alt=media\&token=99aea785-4a22-4178-ad4b-872572c683aa)

## Creating bot dialogs <a href="#creating-bot-dialogs" id="creating-bot-dialogs"></a>

1.In the menu on the left, click on Bot dialogs

2\. Then go to the Generalflow by clicking the green flow icon:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtstupWqpA_B3LB38%2Fimage.png?alt=media\&token=facd58a8-b045-4cb4-b9e5-a452bde0ca30)

{% hint style="info" %}
**Flows** are a way to group bot dialogs that are about the same topic or use case. You will learn more about them later.
{% endhint %}

3\. In the 'general' flow, you will see an overview of all the bot dialogs that are part of this flow. When creating a new bot, you always start with a few predefined dialogs:

* Not understood
* Introduction
* Offloading open
* Offloading closed
* Bot disabled
* Error occurred
* ...

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtz69wusVWRNC4orB%2Fimage.png?alt=media\&token=2b392ab7-673b-426a-b6ab-368992253415)

{% hint style="info" %}
To navigate the screen, you can zoom in or out by using the scrolling wheel, or with your trackpad. You can also click and drag to move through the dialog tree.
{% endhint %}

## Step 1: Adding an introduction <a href="#step-1-adding-an-introduction" id="step-1-adding-an-introduction"></a>

The first thing you'll need to do is create an introduction. This is the first message your users will see, the dialog your bot will use to introduce itself and help users understand its functionalities. Introductions are an important way to set the proper expectations of a bot.

* You can edit the introduction by clicking the `introduction` bot dialog.

{% hint style="info" %}
**What is a bot dialog?** A bot dialog is a something that the bot will say or do when triggered by a user [intent](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp#intent) or user message. This can be anything: from a message to a user to connecting to an external system, giving a message back and jumping to a different dialog in the flow. We will come back to the [four different types](https://docs.chatlayer.ai/bot-answers/dialog-state) of bot dialogs.
{% endhint %}

{% hint style="warning" %}
Chatlayer.ai supports multiple media types. Depending on the channel your bot will use (Facebook, Slack, Skype, Google Home, ...) these will be rendered slightly differently. For now that is not a problem, but check out [this page](https://docs.chatlayer.ai/channels/multi-channel/) when you start building your 'real' bot.
{% endhint %}

Since this is our first bot and our first message, let's start with a simple text message:

* Delete the predefined greeting message by selecting the following text:

> Hello. Please configure the introduction dialog state with a meaningful message.

* Replace it with the following text:

> Hello there, I'm Choo Choo, your digital assistant

* Click on `Text` in the section 'Add bot message' to add a second message and enter the following text:

> How can I help you today?

The result will be:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzErRIbDRlAaz8qGaymqZ%2Fimage.png?alt=media\&token=b64c1a9c-b721-4ea7-b7ff-b6062b99a6a7)

Just like in normal conversations, your users will find it odd if your bot always replies with the exact same message. That's why we support random messages. A random message means that the different messages will be alternated, so sometimes the first message will show, sometimes the second one.

In the Text Message block, you can add multiple versions of the same message. The bot will randomly pick one of these messages to show to the user, making your dialogue more natural and human-like.

* To add a random message, click on `+ Add random message` and enter the following text:*"What can I do for you?"*

Tip: you can add as many random messages as you like.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTonj9dhkngmb4YfuD6%2F-MTp8yVHh7mRlG-262u-%2Fimage.png?alt=media\&token=6a8468c1-fe76-41dc-ab71-503ae83adf27)

* Click on `Save` to save your `introduction` bot dialog.

## Step 2: Testing your greeting <a href="#step-2-testing-your-greeting" id="step-2-testing-your-greeting"></a>

Time to check if we configured everything correctly. You can test your bot by using our built-in emulator.

* Click on the Emulator icon in the lower right corner to test your bot:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGuuHsF2WqAfMVtLQa%2Fimage.png?alt=media\&token=ff295c92-3daf-48bc-a966-eff6640bb805)

If you have configured everything correctly, Choo Choo will now start the conversation with the introduction you just created. *PS: You can ignore the debug button on the left for now, though this will be useful a little later, when you want to debug more complicated flows.*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGv8qHhUPXH7lELdb_%2Fimage.png?alt=media\&token=d62ebbd8-503a-4e15-8aed-01d26274b919)

Congrats, you just created your first bot dialog! 🥳

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

You now have the done the following:

* Created your own tutorial bot
* Changed the introduction message
  * Added a new message and a random message

You should now know:

* How to change a bot message
* What the emulator is, and how to check your bot message in the emulator

In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-adding-content), you will learn to set up questions which the user may ask the bot, and how to create a bot response.
