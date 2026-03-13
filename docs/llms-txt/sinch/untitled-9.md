# Source: https://docs.sinch.com/ia-conversational/untitled-9.md

# Adding content to your bot

## The basics of bot building <a href="#the-basics-of-bot-building" id="the-basics-of-bot-building"></a>

In this lesson, we are going to add intents to our Choo Choo bot. We will learn about the NLP engine, how to update the NLP in your bot, and how to link intents and messages.

## The NLP engine <a href="#the-nlp-engine" id="the-nlp-engine"></a>

Before we create some more dialogs, we'd like to tell you about the NLP engine first. You see, the Natural Language Processing (NLP) engine is the underlying algorithm that allows the bot to understand what the user is saying. And as each language has its own words and grammar, we have a separate NLP engine for each language!

> Understanding language isn't easy: it takes us humans about 6 years and hundreds of examples to understand the most common 20,000 words. It's not so different for computers either. To train an NLP engine, we need huge amounts of data. Luckily, we rely on pre-trained models that have a lot of smarts built in already.

## Step 3: Adding an intent <a href="#step-3-adding-an-intent" id="step-3-adding-an-intent"></a>

An intent is a specific question from your user or an action they can do. Users will type their question in the bot, which can be recognised by the NLP engine and linked to an intent. For example: an intent can be a question, a statement, an answer to a question, or a greeting. Each intent can be expressed in many different ways, which is why we call them **expressions**.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MMLfRKntn78RIWIaRVc%2F-MMLhtEtPGu04ZiKva0K%2FUntitled-1.png?alt=media\&token=8002aa84-62dd-49d0-81e7-c24ca47686ac)

In the example above, the user intent is "How do I sign up for a free trial?". This is then recognised by the NLP engine, which triggers the correct response.

Here are some more examples of intents and expressions:

* **Intent: book train ticket** Expressions:
  * I want to book a train ticket
  * I need to go from Antwerp to Brussels
  * Can I order a ticket here?
* **Intent: who are you?** Expressions:
  * What is your name?
  * What can you do?
  * What should I call you?
* **Intent: yes** Expressions:
  * Looks good
  * Yes
  * Ok, confirm
* **Intent: I want to speak to a human** Expressions:
  * Can I speak to a real person?
  * human please
  * I want to talk to a human

For this tutorial, we want to give Choo Choo the ability to answer basic questions about itself. To get started, we will create an intent for the question: `Who are you?`

* On the left side of the screen in the navigation menu, click on `NLP` to navigate to the NLP module. Click the `Intents` submenu.

The NLP menu

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvLhwGB21_S9e9PXt%2Fimage.png?alt=media\&token=ca534e84-78f8-49d7-b754-df6dedea15e1)

* Click on `Add Intent` and name it `who are you`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvU5y_2CuizhTLXI5%2Fimage.png?alt=media\&token=f3ce5eb7-f2d3-44f4-a57b-eb199d99203c)

* Click on `Create`
* Now you see that the intent is successfully created, without any expressions added to it (that is what the '0' means below the language)

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTpDBTkDjv_iNirTsD0%2F-MTpMyT4l1QZp__fbVRH%2Fimage.png?alt=media\&token=2c0f2655-64b8-4011-bada-ac3c314b451e)

## Step 4: Adding expressions <a href="#step-4-adding-expressions" id="step-4-adding-expressions"></a>

Now we have to make sure the NLP recognises this intent. We do this by adding expressions. Expressions are different ways your users will express one intent. In botbuilding, as in real life, there are more ways to say something or ask a question.

{% hint style="info" %}
Expressions are another word for what is sometimes called 'Utterances'
{% endhint %}

The more expressions you add to an Intent, the more accurately it will be recognised. It is crucial for an intent to have a wide variety of expressions to give accurate results. The more expression you can think of, the better the result of the NLP will be and the 'smarter' your bot will appear.

* Select the `who are you` intent in the **Intents** pane on the left hand side
* The **Expressions** pane will open in the right. Click on `Add Expression`
* Enter `Who are you?` in the open text field
* Click on `Create`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvezDjMYOxHfNKeHa%2Fimage.png?alt=media\&token=f5dbc509-c670-4e7e-959d-7cade2784d0e)

Add some more expressions by clicking `Add Expression`:

* What is your name?
* Can I know your name?
* Tell me more about yourself
* Please, I'd like to know who I am talking to
* How should I call you?
* Who is Choo Choo?
* Tell me what your name is
* Who are ya?
* What do people call you?
* Are you a train?
* Do you have a name?

{% hint style="info" %}
After you have finished your first expression, press Shift + Enter to save that Expression and immediately add a new one
{% endhint %}

This will result in the following screen:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGw2QlGzo2yVENGcU1%2Fimage.png?alt=media\&token=c802326d-460e-4e66-a65a-5c9cebc74bbf)

Again, the more expressions you have, the more accurate your bot will be able to respond. Later on we'll see how we can make sure that our bot gets smarter over time; by looking at actual user input once the bot has been made public.

Let's try adding another intent and expressions:

Add another intent, like `Greeting` and add some expressions:

* Hi
* Hello
* Hey
* Hi there
* Good morning

We have defined two intents now: who are you & greeting.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGw8lRwZ0SGxDiG01p%2Fimage.png?alt=media\&token=7b49d96a-b497-4fbf-9687-adc3f2ad1f54)

However, if we were now to say 'Good morning' to the bot emulator, nothing will happen. That is because the NLP is not trained yet, and the intent is not yet linked to a bot dialog. We will work on that in the next steps.

## Step 5: Training the model <a href="#step-5-training-the-model" id="step-5-training-the-model"></a>

To update the bot, we now need to re-train the NLP. Updating the NLP means that the newly added intents and expressions will be recognised by the bot so we can use them in a conversation.

{% hint style="info" %}
To successfully train the NLP, you need to have at least two intents with a minimum of 5 expressions each.
{% endhint %}

* Click the `Update NLP` button in the top right corner of the screen:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LM6YZRQL3d1aj7P433Y%2F-LM6pLiFLy6DJ3kAACH5%2Fimage.png?alt=media\&token=bf3b849b-497d-4351-abfd-9aa2959cdd32)

Select the language you used to add the expressions. You can view the status of the NLP update for each language by clicking on the Update NLP icon.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGwEH13mHjwe97F7Ak%2Fimage.png?alt=media\&token=16f3d14e-4a09-48b0-ba28-45824c232729)

Click on `Update` to start the training. This can take a couple of minutes to one hour depending on the size of your chatbot. The more complex, the longer it'll take.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGwSqHxCVYb7No4T1M%2Fimage.png?alt=media\&token=357dd3c1-6dd9-4a70-8b42-b38337b9530e)

That was a great first step to use the 'Greeting' and 'How are you' intent. The next step is to link these intents in the bot dialogs.

## Step 6: Linking the intent and defining a response <a href="#step-6-linking-the-intent-and-defining-a-response" id="step-6-linking-the-intent-and-defining-a-response"></a>

You have now taught the NLP to understand your intents and expressions, congrats! The only thing left to do is teaching Choo Choo how to respond. This means we are going to choose what the response (or flow) should be for each intent. You can do this by adding a new Bot dialog.

* Click on Bot Dialogs menu item in the navigation pane
* Open the General flow
* Click on the grey button on top `+ Bot message`
* Enter `who are you` as the name
* Choose the `introduction` dialog state as the parent (in the Settings tab)
* Link the intent to the bot dialog in the bot dialog NLP tab as follows:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGx-k-YWMcDYuMfw2y%2Fimage.png?alt=media\&token=cb5c4390-8a4d-47ff-b612-d55091eb9862)

* Go to `Bot Message` tab and add a text message that says:

> I am Choo Choo, your personal assistant for booking train tickets

Your screen should look like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGx7LadIEUWwl8Zmy-%2Fimage.png?alt=media\&token=61f43605-73dc-47cf-8d1f-32a43af39afd)

* Click on `Create`
* This will result in the folowing overview in the flow:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MMGJDynLKF2rk_VX1en%2F-MMGLSNh8OIL0boHToUU%2Fimage.png?alt=media\&token=2af6f418-fdd7-4393-8884-afeb1f2622bb)

The image below means that a certain intent is linked to that bot dialog.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTpQO-OQuFYJUtB4w02%2F-MTpZtA9-iJ0Gz1fQsxW%2Fimage.png?alt=media\&token=d965d756-f802-44a3-8275-222946b316f3)

If you now say 'Who are you' in the emulator, you immediately get the response that is typed in the 'Who are you' bot dialog.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGxDxHjCKSswPByq6q%2Fimage.png?alt=media\&token=6d1d4026-145c-4a26-898f-7a8833446957)

We have defined the `introduction` bot dialog as the parent dialog state in the `who are you` bot dialog. Parent bot dialogs do not limit or define the possible flow of the dialogue. They are a visual tool to structure the conversational flow and keep an overview, which makes it easier to create complex conversational flows. Bot dialogs can be reached from any point in the conversation by linking a bot dialog to an intent, although you can restrict them too by using Contexts. This mimics the way humans talk, jumping from one subject to another.

## Step 7: Testing your bot <a href="#step-7-testing-your-bot" id="step-7-testing-your-bot"></a>

Time to Choo Choo! Click on `Test your bot` at the bottom right to test your conversational flow. To get a feel of your bot's performance, ask the same question a couple times, including different ways of asking the question that are different to the expression you used to train. If a question is not correctly recognized, you'll have to go back to the `NLP` tab, add the questions as an expression, and retrain the NLP model. You can do this as many times as needed, the model will just keep on improving.

{% hint style="info" %}
The 'Test your bot' feature is also referred to as the 'emulator'.
{% endhint %}

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Now, you have a bot with the following configuration:

* 2 intents ('Greeting' and 'Who are you') and their expressions
* A bot message 'Who are you', with the intent 'Who are you' and four text messages in it.

You should now be familiar with:

* Adding an intent to a bot dialog
* Creating intents and expressions
* Training the NLP to use these intents and expressions
* Adding multiple text messages in one bot message
* Testing your intent and messages in the emulator

If any of these topics are difficult for you, revisit them in the tutorial or search on the page in the top right search bar to learn more about a topic.

In the next tutorial we'll be gathering user input. Choo Choo will ask the user for input, needed for booking a train ticket.
