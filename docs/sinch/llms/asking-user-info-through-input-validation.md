# Source: https://docs.sinch.com/ia-conversational/untitled-9/asking-user-info-through-input-validation.md

# Asking user info through input validation

To complete our Choo Choo bot, we need to ask the following information from the user:

1. Origin
2. Destination
3. Departure date
4. Departure time
5. Class

This works great when the users says, for example:

* **Tomorrow**, I need to go from **Amsterdam** to **Brussels** at **2pm** in **second** class

But right now, our bot can only detect this information when the user gives all this information in a single sentence. Of course, in a lot of cases, this will not always be the case, so we 'll need to ask this information from the user. The dialog to ask for this info is called the **Input Validation dialog**.

## Step 15: working with input validation <a href="#step-15-working-with-input-validation" id="step-15-working-with-input-validation"></a>

Until now, we have only worked with the bot dialog type `Bot Message`. One of the other [four bot dialogs](https://docs.chatlayer.ai/bot-answers/dialog-state) types is `Input validation`. With an input validation, you can ask specific information from a user and save the answer directly in a variable. Let's start with origin and destination.

#### Text input  <a href="#text-input" id="text-input"></a>

We are going to create new input validations. This can be done in the main flow overview with the green `+Input validation` button, but can also be created directly in another bot dialog.

* Open the `book train ticket` bot dialog
* Change your bot message text here to: 'So I have a request for a train ticket'.
* In the Bot Message tab, scroll down to `Go to`
* Type `destination` in the Go to field, and click `Create Input Validation 'destination'`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU4leF2pmBkjy6PCJVw%2F-MU4srj_NrF2syL8B7F_%2Fimage.png?alt=media\&token=8e5df79b-0576-4192-852f-ce29143f1121)

{% hint style="info" %}
In every bot dialog, there is a `Go to` option. This means that the conversation flow will automatically go to that next bot dialog if the current one is finished, or if that specific input is given. With the current set-up, the bot will automatically go to the input validation if the first bot message for the `Book train ticket` intent is finished.
{% endhint %}

* Save the `book train ticket` bot dialog

You can see that the newly created dialog turns red. This means it's not finished yet. Let's finish it so it turns green:

* Open the newly created `destination` input validation
* In the `Input Validation` tab, under 'Question', add a new text message "Where do you want to go?"
* In the 'Save user input as 'pane, select `Any` as the format type under 'Check if response matches'

{% hint style="info" %}
Input validation can automatically detect certain types of data, like dates, addresses, numbers, hours, currencies, ... This will convert the users response into a more structured format.

In this example, we just want to know the city of destination, which can take on any format. So, we'll use input type 'Any' which will accept any value as valid input.

You can find more info about plugin parser types [here](https://docs.chatlayer.ai/bot-answers/dialog-state/user-input-bot-dialog#input-types).
{% endhint %}

* Type `destination` as the variable. The input from each user will be saved under this variable name.
* Type `Confirm booking` in the 'Go to' field. Because the `Confirm booking` bot dialog doesn't exist, you get the option to create a new one. Pick `Create Bot Message 'Confirm booking'`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9PxMzC40ywMyeD4w2%2Fimage.png?alt=media\&token=b695b616-96da-4336-b98e-e942715121dc)

The end result should look like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9QJfEHny2q0nOk8sW%2Fimage.png?alt=media\&token=1281cc2e-4b70-45db-aa0c-06debd0a8cf7)

#### NLP & input plugin <a href="#nlp-and-input-plugin" id="nlp-and-input-plugin"></a>

You want to make sure your users don't get stuck in a loop where the bot keeps asking them for input. That's why we make sure that if an intent is detected in the answer to the input plugin, users automatically leave the input plugin and go to the relevant part of the conversation.

Our Choo Choo bot doesn't have a mature NLP model yet, which increases the likelihood of false intent matches. So for now, it's best to select the 'Disable NLP' checkbox in the input plugin.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9RU4aotcmUFmvmEzD%2Fimage.png?alt=media\&token=9e826e3d-52d0-45b2-8db1-4625e8bd4843)

Once created you will see the following flow:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9QXlqXRcX8GeSljhF%2Fimage.png?alt=media\&token=c029f2cb-07e9-48e9-8cc6-3f7b6a97df8d)

{% hint style="warning" %}
The parent-child relation between dialog state nodes is only a visual representation, it has no functional meaning. Always link your bot dialogs using Go to's.
{% endhint %}

#### Using user input in text messages <a href="#using-user-input-in-text-messages" id="using-user-input-in-text-messages"></a>

As can be seen in the image above, the bot message is red. This means it is not completed yet. Let's complete it so it will turn grey (the colour of all Bot messages). All the session variables are stored in the user session. To access a variable in any displayed text, you can put the variable name between curly brackets.

* Open the `Confirm booking` bot dialog
* Enter a new text message `Okay you want to go to {destination}. We can do that.`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9R7gO9zO9mEKiJJ_q%2Fimage.png?alt=media\&token=7448e6a2-1e7b-4720-b837-df740fcd01d7)

Time for a test!

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU9RkNyhP4QN1UQ6dwH%2F-MU9UbuO_rOONaD01OtC%2Fimage.png?alt=media\&token=533ba19f-6984-4b36-9afd-11daac9c3d4c)

{% hint style="info" %}
If you forget to define the 'Go to' and you test your conversation flow, the flow will just stop. The conversation will only continue if you correctly set the 'Go to' for each dialog state.
{% endhint %}

That looks great! If you are getting a message with empty spaces in the first bot message ('So I have a request for a train ticket'), make sure you have changed that bot message accordingly for our newest set-up. If the destination is not captured correctly, make sure that you save the variable as 'destination' in the Input validation and you use '{destination}' in the bot message.

## Step 16: Completing the booking flow with the remaining input validations <a href="#step-16-completing-the-booking-flow-with-the-remaining-input-validations" id="step-16-completing-the-booking-flow-with-the-remaining-input-validations"></a>

Repeat the previous steps for the the other pieces of information you'd like to get from your users:

* Origin: Where are you leaving from?
* Departure time: At what time do you want to leave?
* Departure date: Which day would you like to take the train?

This means you need to create three extra Input Validations, just like the `destination`Input Validation. You can change the current `destination`Input Validation to make sure the `origin` is asked next:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO1Zdl3Cz7ul2TcJKE%2F-MWO33qVHR2oxFRZoKe1%2Fimage.png?alt=media\&token=d7db512e-ae66-4b71-9633-15908a9ce843)

Create the Input Validation. Save the variable under 'origin' and choose 'Check if response matches > any'. Once this is created you will see this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO1Zdl3Cz7ul2TcJKE%2F-MWO3SNlz9WclAYqUiEx%2Fimage.png?alt=media\&token=bffe583d-696a-4e58-aa38-a8906bc653fe)

This is because the `Confirm booking`Bot Message still has `destination` as parent. No worries, this will be fixed later. Add 'Where are you leaving from?' as text in the Input validation and save the input under 'origin' variable. Make sure that the next Input Validation after this one will be `departure time.`

* Now, create the other Input Validations:
  * 'departure-time' variable, with text: 'At what time do you want to leave?'. Save under 'Check if response matches > any'. Go to: departure date. Disable the NLP.
  * 'departure-date' variable, with text: 'Which day do you want to take the train?'. Save under 'Check if response matches > any'. Go to: confirm booking. Disable the NLP.

Make sure all of these input validations follow a consecutive flow, and end up in the `Confirm booking` bot dialog:

1. `Book train ticket`
2. `Destination`
3. `Origin`
4. `Departure time`
5. `Departure date`
6. `Confirm booking`

{% hint style="info" %}
You will see, once you open `departure date` Input validation, that the go to is `confirm booking` but this does not show in the flow overview. That is because the parent of `confirm booking` is still destination. You can change this by opening `confirm booking` > Setting tab > change parent to `departure date`.
{% endhint %}

This means the end result will look like the following:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO6M8HjaakuDW7YtVO%2F-MWO7ksNgYfl1JK1enjS%2Fimage.png?alt=media\&token=2ede2494-82eb-4a78-9444-1d0cf30fad98)

If any of your bot dialogs are red - check if the bot dialog is complete with a text and saved under the correct variable. If you do not have a consecutive flow, please check if all parents are set correctly and the go-tos in the dialogs are saved correctly.

We now have a great train booking flow! Try it out a couple of times.

In the emulator with the debugger tab you can see if the variables are saved correctly. In this tab you can see all the variables stored in that specific session. If you scroll down you can see something like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWOYSBxsXVVKc1L5Irj%2F-MWOYxfyqkQOrZpuiUTs%2Fimage.png?alt=media\&token=fb4fccb1-9c6e-4d26-95c9-b8cf05e743aa)

This is a great start when you need to debug. Here you can see if you made a typo in a certain variable or if the user input is correctly stored in the variable.

## Step 17: Combining user input with buttons <a href="#step-17-combining-user-input-with-buttons" id="step-17-combining-user-input-with-buttons"></a>

In the tutorial above, we requested user input by sending a text message. However, in an `input validation`, we can also ask for the user's input by click, but it is also possible to use buttons, lists, carousels and other UI components to support user input as text or clicks.

This is especially useful and user friendly to have when there are only a few options to choose from, as described [here](https://docs.chatlayer.ai/tips-and-best-practices/chatbot-checklist) in the Conversation Design Chatbot Checklist.

Let's use buttons to request the user their preferred train class.

* In the `Departure date` input validation, type `Class` in the Go to field and create a new input validation
* Under Question, add Buttons
* Enter the text message: "Which class do you want to travel in?"
* Add two buttons, choose the Go to option, "First class" and "Second class," both going to the `Confirm booking` bot dialog
* In both buttons add a variable `class` and value `first` and `second`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO8Gz9pphhnIm1m8oP%2F-MWOU3azKsdwgVasGI4e%2Fimage.png?alt=media\&token=0a95a8e9-ee60-428f-9bcd-1205add5a7d7)

* Select format type `Any`, enter `class` as variable, and go to `Confirm booking`

{% hint style="info" %}
It's important to use an identical variable name for the input variable, the NLP entity and the button variable.
{% endhint %}

Depending on the user input, different actions will be executed:

1. If a user writes an expression that contains an entity that matches with the variable in an input validation, this input validation is skipped. This way we can avoid asking things from the user which they've already said.
   * For example: when the user says `I need a first class train ticket` which belongs to intent `book train ticket` and includes an entity `class`, the 'class' variable is stored in the user session with a value 'first' and the input validation 'class' is skipped because the value for the input variable is already available in the user session.
2. When the user is asked to give his preferred train class and he says 'first', this value will be added in the input variable 'class' in the user session.
3. When the user clicks the button 'First class', the value 'first' will be added to the variable 'class' in the user session.

This gives a lot of freedom to the user; no matter where they give their input (in an input validation, expression, or button) this is all saved in the correct variable.

Try it out in the emulator!

## Step 18: Finishing up <a href="#step-18-finishing-up" id="step-18-finishing-up"></a>

Now that you have all this extra information, it's time to show all the data you've gathered in the input validations to the user:

* Open the `Confirm booking` bot dialog
* Replace the existing text message with "I have a train ticket for you from {origin} to {destination} on {departure-date} at {departure-time}h, in {class} class."
* Change the parent to `class`

Now test your newly created bot to see if it works!

If you run into any issues,

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Now, you have a bot with:

* A flow to book a train ticket with 2 bot messages and 5 input validations
* The ability to recognize both variables given in expressions or via input validations
* A final bot message summarizing all variables given by the user

You should now be familiar with:

* Creating an input validation and storing the user input in a variable
* Creating a button and storing the input from the button click in a variable
* Linking bot dialogs to each other with the go to option in a bot dialog, and creating a new bot dialog from the go to option
* Changing the parent of a bot dialog
* Using the debugger tab to see how user input is stored

In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-conditional-flow-navigation), you will learn how you can steer the conversation in a certain direction based on known variables.
