# Source: https://docs.sinch.com/ia-conversational/untitled-9/detecting-information-in-expressions.md

# Detecting information in expressions

You will learn how to detect valuable information, mentioned by a user in an intent, using **contextual entities**. Entities are important pieces of information that are extracted from an expression.

There are four types of entities. You can find more information about them here: [Entities/understanding-users/natural-language-processing-nlp/synonym-entities](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/synonym-entities)

In this tutorial we will focus on one entity type: contextual entities. Contextual entities use machine learning to identify entities in sentences by learning what type of word your entity is, where it's placed in the sentence, and what the specific context is.

You want to store these contextual entities in a separate variable so you can re-use them later on. Read more about the difference between entities and variables [here](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/synonym-entities#the-difference-between-entities-variables-and-values). In the next tutorial, you will learn how you can ask explicitly for missing information.

Let's say we have an intent that tells us the user wants to book a train ticket. A few different expressions could be:

* I want a train ticket
* I need a ticket
* Can I book a train ticket here?

This assures the bot dialog, linked to the corresponding intent, to be triggered when the user says one of these expressions.

But what would happen if the user says:

* I want a train ticket to **Amsterdam**
* I need to go to **Antwerp tomorrow**
* Can I book a train ticket to **Brussels** please?

These expressions contain valuable information. We want to make sure we capture that information, in this case the destination and time, and save it as **entities**. We then have expressions with an entity in them.

We are now going to create a new intent with some expressions for booking a train ticket. Some of these expressions will contain a contextual entity, but some will not.

## Step 9: Creating contextual entities <a href="#step-9-creating-contextual-entities" id="step-9-creating-contextual-entities"></a>

Not all users will immediately mention their destination, so let's make sure we train our intent without those specific entities as well:

* Go to `NLP` > `Intents`
* Click on `Add Intent`
* Add a new intent called `book train ticket`
* Add some simple expressions, like:
  * I want a train ticket
  * I need a ticket
  * Can I book a train ticket, please?

{% hint style="info" %}
If you have trouble doing this, please read the [previous tutorial](https://docs.chatlayer.ai/tutorials/tutorial-adding-content).
{% endhint %}

Next, it's time to add a contextual entity.

* Go to `Intents` and select your `book train ticket` intent
* Click on `+ Add expression` to create a new expression
* Enter an expression that contains an entity, for example:

> I want to book a ticket from Brussels to Paris

* Select `Brussels` in this sentence

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGxxv8SOeFMIFvsE7c%2Fimage.png?alt=media\&token=004b7ae3-6de6-400a-b0d8-39ff6e062252)

* Click on the '+ entity' icon in the bottom right of the expression box to create a new contextual entity for 'Brussels'

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyCH7wsvcaDFBmzaV%2Fimage.png?alt=media\&token=24d67668-28c8-4bac-8527-8cbde0db440a)

* Brussels is the location the user wants to depart from, so we will name this entity `origin`
* Type `origin` in the `Create new entity` field and click on 'Create new entity' to confirm

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyJxX0IFrM96GU68X%2Fimage.png?alt=media\&token=77862567-721f-4704-917a-95eefc1eafcc)

* Brussels will be added to the list of possible values for the @origin variable
* Do the same thing for `Paris` as a 'destination' entity

You will then have the following set-up for this expression:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyV2A2i5z-N9Bjko2%2Fimage.png?alt=media\&token=4ad66920-83d0-4a9b-935e-0a823ab6fa23)

We now save added the expression 'I want to book a ticket from @origin to @destination', where 'Brussels' is a value for @origin and 'Paris' is a value for the entity @destination.

* Add some other values to the 'origin' and 'destination' entities in the expression field. These will be saved for all future expressions. You can add these in the 'Create new value' box and pressing enter.
* Add more expressions that contain the entities **origin** and **destination**

Once you have added more Entity values, these will also show up in the menu `Entities` > `Contextual Entities`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTtSJzh0IZmA5tu3CIt%2F-MTtUS1oKy_IOQmi5o0r%2Fimage.png?alt=media\&token=8db10598-73a6-4d7f-9c52-359dfe861b2d)

* Now, let's add some more expressions to our `Book train ticket` intent. Some ideas for expressions:

  * Can I book a train from Cologne to Brussels?
  * I need to be in Rotterdam
  * I need a train to London
  * I want to travel to Lyon
  * I want to buy a ticket from Moscow to Vladivostok
  * I need a ticket from New York to Baltimore

  ​

{% hint style="info" %}
When typing a new expression, you can add entities and entity values in two ways:

1. Typing @ and then the name of the entity, for example @origin. You can add a new value in the box below with 'Create new value'
2. Selecting an entity value and clicking the +entity value button. For example, select 'Cologne', click the +button. This will result in 'Cologne' being changed into @origin and 'Cologne' will be a value of @origin
   {% endhint %}

* Make sure you retrain the NLP model by clicking the `Update NLP` button in the right upper corner.

This will now result some expressions for the `Book train ticket` intent, and entity values, like so:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGzbGNWNnq3K523Ulr%2F-MkGzyb8SE__tYj3dfE0%2Fimage.png?alt=media\&token=39186f8a-7c8f-4d85-9303-cb1a0653322c)

To make it easier for you to add new expressions fast, we have built the expressions generator. Head over to [this page](https://docs.chatlayer.ai/understanding-users/expression-generator) for more information.

## Step 10: Testing contextual entities <a href="#step-10-testing-contextual-entities" id="step-10-testing-contextual-entities"></a>

After we have retrained our model, let's see if its good enough to recognise the destination entity.

* Go to `NLP` >`Test` to open the testing console
* Write 'I would like to go to Brussels from Amsterdam' as the expression to be tested
* Click on `Test`

You'll see that the entity gets recognized with a 99.93% confidence. The results will be different based on your training set. If the entity is not recognized correctly, you can add it here as a training expression immediately by clicking `+Add expression`.

{% hint style="warning" %}
Make sure you retrain the NLP model before testing newly added expressions
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH15--aKH17tP9HGHH%2Fimage.png?alt=media\&token=ad4d3c89-61ee-49c2-bdbf-cd49bc93d818)

Now we know how to add intents, create expressions and entities, however we still need to create a conversation so the user can talk to Choo Choo and our bot replies accordingly. Let's add some bot messages in the next step.

## Step 11: Using variables in messages <a href="#step-11-using-variables-in-messages" id="step-11-using-variables-in-messages"></a>

When a user says something containing an entity, and the entity is successfully detected, our tool will automatically store the entity as a **variable** for that specific user.

At the moment, when you test your bot, the user is stuck after giving the information about the ticket:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH1CUu58sorl5kmWxV%2Fimage.png?alt=media\&token=d1af8e0a-8938-43be-8ba4-d12ec80c81cd)

However, we do see some positive items, namely that the 'origin' and 'destination' are stored correctly as variables. You can see this by opening the debugger by clicking 'Debugger' (with the magnifying glass icon) in the emulator. In the 'Debugger' tab, you can scroll down and you see this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU2TVa1AuMzEh_EOnYY%2F-MU2VeSiba5oLsepO84p%2Fimage.png?alt=media\&token=44d3181f-b11c-4dd4-bc4d-55fc1fa86aeb)

So even though the sentence did give an error message, these entities are correctly recognized in the user input. This means the variable 'origin' is now saved with a variable value 'Brussels' and the variable 'destination' with the value 'Paris'. Also, in the ''NLP Result' tab we see that the intent was recognised correctly, that's great! Let's now work on removing that error message first.

The error message is caused by the fact that the intent `Book train ticket` does not have a bot dialog linked to it. So even though it is correctly recognised, we are not telling the bot what to do when that intent is recognised.

We can change that by adding a new Bot message:

* In the menu Bot dialogs, open the 'General' flow, create a bot dialog of the type 'Bot message' `book train ticket`. Open the 'NLP' tab, and choose the `Book train ticket` intent in the 'Intent' dropdown.
* In the 'Settings' tab, name the bot message `Book train ticket`
* Add a new text message with the text "So you want to go to `{destination}`, I can help you with that!"
* Click `Create` to save this bot message.

{% hint style="info" %}
To reuse the variable later on in the conversation, you can put it in between curly brackets like this: `{variable_name}`

When writing this message to the users, Chatlayer will automatically substitute `{variable_name}` with the value of the variable. If the variable is empty, an empty space will be shown.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH1PrdzbeTf9tu68sF%2Fimage.png?alt=media\&token=7c8f42e4-4d7b-4558-b519-2fd051b6e447)

We have now linked the `Book train ticket` to this bot message, great job! This means that, when a user says something that triggers the `Book train ticket` intent, this bot message will show.

## Step 12: Testing entities in the emulator <a href="#step-12-testing-entities-in-the-emulator" id="step-12-testing-entities-in-the-emulator"></a>

Now that we have linked everything, we are ready to test if everything is configured correctly by using the emulator.

* Open the emulator (the `Test your bot` tool on the bottom right)
* If needed, clear the last conversation by clicking 'Clear conversation' on the top right. This starts a new conversation
* Enter "I want to go to Amsterdam" and click on submit
* Open the debugger

In the tab 'NLP Result' you can now see if the entity was recognized correctly:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH3SXFOwX2uPCsNuP2%2F-MkH4NrTG2-cY0ooVsXM%2Fimage.png?alt=media\&token=c8010d53-7fad-4041-979f-7d2925f1f0d6)

{% hint style="info" %}
When creating new bot dialogs, you don't need to re-train the NLP
{% endhint %}

If you do not get the result as stated above, please check the following items in your bot:

* If your entity is recognised by the NLP but doesn't show up in with `{destination}` it did not pass the threshold of 80%. Try adding that value to your entity and re-train your model, or choose another destination
* If you get 'Sorry I didn't understand that', double check if your intent is linked to the Bot message and this is saved correctly.
* If your intent or expression is not recognised, try re-training your NLP again.

Now we already have a great start with linking the intent and giving a response to the expression the user says. However, we want more information from the user. Let's add more expressions and entities.

## Step 13: Multiple entities in one expression <a href="#step-13-multiple-entities-in-one-expression" id="step-13-multiple-entities-in-one-expression"></a>

You can add as many entities as you want to one expression. For Choo Choo, we want to more information from the user than just the destination and origin, to give a complete train-booking experience. Let's add more contextual entities!

* Go to the `Expressions` menu
* Click 'Add Expression'
* Select the `Book train ticket` intent

Create the following expression:

* I want to go from **Antwerp** to **Brussels** **tomorrow** at **9am** in **first** **class**

And create the following entities:

* origin: Antwerp
* destination: Brussels
* departure-date: tomorrow
* departure-time: 9am
* class: first class

*If you are having trouble adding these, scroll back to step 9 in this tutorial to read all about it.*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH3SXFOwX2uPCsNuP2%2F-MkH525pu7JX-S69BFna%2Fimage.png?alt=media\&token=bf9e6fe8-55f3-472b-a331-de6789211512)

#### Additional suggestions for expressions <a href="#additional-suggestions-for-expressions" id="additional-suggestions-for-expressions"></a>

* I need to be in Paris next Thursday
* I need to be in New York on Friday
* I want to go to Brussels on Monday
* Friday I want to go from Antwerp to Amsterdam
* I want to travel in second class from Ghent to Brussel on Friday
* I want to travel in first class from Antwerp to Aalst on Thursday
* I like to book a first class ticket from Aalst to Brussels at nine o'clock
* Tomorrow I want to go from Antwerp to Brussels on the train from 9:00 in first class

{% hint style="info" %}
Keep in mind that NLP techniques are probabilistic in nature. When you try to capture five expressions in one sentence, it might not be able to recognise all of them correctly. As a general rule of thumb, you can start to expect reasonable results for one entity when the NLP was given at least 30 expression to learn from.
{% endhint %}

Add more expressions with the new contextual entities to the intent. Ensure you have around 20 expressions for `Book train ticket` in total.

## Step 14: Missing entities <a href="#step-14-missing-entities" id="step-14-missing-entities"></a>

Let's test out your newly created expressions:

Update the wording in the `book train ticket` dialog to correctly display the entities:

*I need a ticket from Antwerp to Brussels tomorrow at 9am in first class*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH8YKAwriN4PC7GJ0n%2Fimage.png?alt=media\&token=c5e2d9cc-b3f7-450b-9324-4ecd2380ec50)

{% hint style="warning" %}
If you try to update your NLP and you get an error message about 5 example entities, it means you need to add more entity values to some of your newly created entities. To do so, go to NLP > Entities > Contextual entities and make sure that that entity has at least 5 values.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH9WVdq97GEU-ttmps%2Fimage.png?alt=media\&token=dac2c47a-3e4b-4dd9-81d0-ca0d8f301738)

Uh oh, this isn't really what we expected. As you can see, not all variables were recognized correctly. So, what's the issue? Lets have a look at the NLP results in the debugger:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH9TzgUC7RuJYHHDo7%2Fimage.png?alt=media\&token=677387f2-a43a-4d3c-ada8-d28cb0906025)

`origin`, `destination`, `time_departure` and `class` were found correctly, but only `time_departure` and `class` have a confidence score higher than 80%. `Origin` and `destination` score much lower, so they weren't processed as variables.

{% hint style="info" %}
In the [NLP treshold settings](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/settings) of our bot, we put a threshold of 80%, so anything underneath that won't be recognized correctly.
{% endhint %}

How can you fix this issue? By adding more expressions! Try adding more expressions and retrain your NLP model to see if the variables now show up correctly in the bot. You can also choose to lower the NLP score, but be careful as this can impact the overal accuracy of your bot in the long run.

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Your bot now has the following configuration:

* 3 intents with around 35 expressions in total
* 5 contextual entities
* A bot message, linked to the `Book train ticket` intent, confirming the user input in the message

You now know how to:

* Create contextual entities and entity values
* Use variables in a bot message
* Use multiple contextual entities in an expression
* Test your input in the debugger

Not every user will give all the entities you need. In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-request-and-use-information-using-input-plugins), you will learn how to check if a user has already provided certain information, and ask for what's missing.
