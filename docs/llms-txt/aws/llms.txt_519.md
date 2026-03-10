# Source: https://docs.aws.amazon.com/lex/latest/dg/llms.txt

# Amazon Lex V1 Developer Guide

> This is the official Amazon Web Services (AWS) documentation for Amazon Lex. Amazon Lex is an AWS service for building conversational interfaces for applications using voice and text. Amazon Lex provides the deep functionality and flexibility of natural language processing and automatic speech recognition so that you can build highly engaging user experiences with lifeline, conversational interactions. This documentation is offered for free here as a Kindle book or you can read it online or in PDF format at https://aws.amazon.com/documentation/lex/.

- [What Is Amazon Lex?](https://docs.aws.amazon.com/lex/latest/dg/what-is.html)
- [Versioning and Aliases](https://docs.aws.amazon.com/lex/latest/dg/versioning-aliases.html)
- [Document History](https://docs.aws.amazon.com/lex/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/lex/latest/dg/glossary.html)

## [How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html)

- [Supported Languages](https://docs.aws.amazon.com/lex/latest/dg/how-it-works-language.html): Amazon Lex V1 supports a variety of languages and locales.
- [Programming Model](https://docs.aws.amazon.com/lex/latest/dg/programming-model.html): A bot is the primary resource type in Amazon Lex.
- [Managing Messages](https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html)

### [Managing Conversation Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html)

Conversation context is the information that a user, your application, or a Lambda function provides to an Amazon Lex bot to fulfill an intent.

- [Setting Intent Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-active-context.html): You can have Amazon Lex trigger intents based on context.
- [Using Default Slot Values](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-default.html): When you use a default value, you specify a source for a slot value to be filled for new intents when no slot is provided by the userâs input.
- [Setting Session Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-session-attribs.html): Session attributes contain application-specific information that is passed between a bot and a client application during a session.
- [Setting Request Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-request-attribs.html): Request attributes contain request-specific information and apply only to the current request.
- [Setting the Session Timeout](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-session-timeout.html): Amazon Lex retains context informationâslot data and session attributesâuntil a conversation session ends.
- [Sharing Information Between Intents](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-cross-intent.html): Amazon Lex supports sharing information between intents.
- [Setting Complex Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt-complex-attributes.html): Session and request attributes are string-to-string maps of attributes and values.
- [Using Confidence Scores](https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html): Learn how to use intent confidence scores to improve the accuracy of your bot.

### [Conversation Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs.html)

Learn how to use Amazon Lex to log conversations with your users.

- [IAM Policies for Conversation Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-policies.html): Depending on the type of logging that you select, Amazon Lex requires permission to use Amazon CloudWatch Logs and Amazon Simple Storage Service (S3) buckets to store your logs.
- [Configuring Conversation Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-configure.html): You enable and disable conversation logs using the console or the conversationLogs field of the PutBotAlias operation.
- [Encrypting Conversation Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-encrypting.html): You can use encryption to help protect the contents of your conversation logs.
- [Viewing Text Logs in Amazon CloudWatch Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-cw.html): Amazon Lex stores text logs for your conversations in Amazon CloudWatch Logs.
- [Accessing Audio Logs in Amazon S3](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-s3.html): Amazon Lex stores audio logs for your conversations in an S3 bucket.
- [Monitoring Conversation Log Status with CloudWatch Metrics](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-monitoring.html): Use Amazon CloudWatch to monitor delivery metrics of your conversation logs.
- [Managing Sessions](https://docs.aws.amazon.com/lex/latest/dg/how-session-api.html): When a user starts a conversation with your bot, Amazon Lex creates a session.
- [Deployment Options](https://docs.aws.amazon.com/lex/latest/dg/chatbot-service.html): Currently, Amazon Lex provides the following bot deployment options:

### [Built-in Intents and Slot Types](https://docs.aws.amazon.com/lex/latest/dg/howitworks-builtins.html)

To make it easier to create bots, Amazon Lex allows you to use standard built-in intents and slot types.

### [Built-in Intents](https://docs.aws.amazon.com/lex/latest/dg/howitworks-builtins-intents.html)

For common actions, you can use the standard built-in intents library.

- [AMAZON.CancelIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-cancel.html): Responds to words and phrases that indicate the user wants to cancel the current interaction.
- [AMAZON.FallbackIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html): When a user's input to an intent isn't what a bot expects, you can configure Amazon Lex to invoke a fallback intent.
- [AMAZON.HelpIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-help.html): Responds to words or phrases that indicate the user needs help while interacting with your bot.

### [AMAZON.KendraSearchIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-kendra-search.html)

To search documents that you have indexed with Amazon Kendra, use the AMAZON.KendraSearchIntent intent.

- [Example: Creating a FAQ Bot for an Amazon Kendra Index](https://docs.aws.amazon.com/lex/latest/dg/faq-bot-kendra-search.html): This example creates an Amazon Lex bot that uses an Amazon Kendra index to provide answers to users' questions.
- [AMAZON.PauseIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-pause.html): Responds to words and phrases that enable the user to pause an interaction with a bot so that they can return to it later.
- [AMAZON.RepeatIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-repeat.html): Responds to words and phrases that enable the user to repeat the previous message.
- [AMAZON.ResumeIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-resume.html): Responds to words and phrases the enable the user to resume a previously paused intent.
- [AMAZON.StartOverIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-start-over.html): Responds to words and phrases that enable the user to stop processing the current intent and start over from the beginning.
- [AMAZON.StopIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-stop.html): Responds to words and phrases that indicate that the user wants to stop processing the current intent and end the interaction with a bot.

### [Built-in Slot Types](https://docs.aws.amazon.com/lex/latest/dg/howitworks-builtins-slots.html)

Amazon Lex supports built-in slot types that define how data in the slot is recognized and handled.

- [AMAZON.Airport](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-airport.html): Provides a list of airports.
- [AMAZON.AlphaNumeric](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-alphanumeric.html): Recognizes strings made up of letters and numbers, such as APQ123.
- [AMAZON.City](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-city.html): Provides a list of local and world cities.
- [AMAZON.Country](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-country.html): The names of countries around the world.
- [AMAZON.DATE](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-date.html): Converts words that represent dates into a date format.
- [AMAZON.DURATION](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-duration.html): Converts words that indicate durations into a numeric duration.
- [AMAZON.EmailAddress](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-email.html): Recognizes words that represent an email address provided as username@domain.
- [AMAZON.FirstName](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-first-name.html): Commonly used first names.
- [AMAZON.LastName](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-last-name.html): Commonly used last names.
- [AMAZON.NUMBER](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-number.html): Converts words or numbers that express a number into digits, including decimal numbers.
- [AMAZON.Percentage](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-percent.html): Converts words and symbols that represent a percentage into a numeric value with a percent sign (%).
- [AMAZON.PhoneNumber](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-phone.html): Converts the numbers or words that represent a phone number into a string format without punctuation as follows.
- [AMAZON.SpeedUnit](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-speed.html): Converts words that represent speed units into the corresponding abbreviation.
- [AMAZON.State](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-state.html): The names of geographical and political regions within countries.
- [AMAZON.StreetName](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-street-name.html): The names of streets within a typical street address.
- [AMAZON.TIME](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-time.html): Converts words that represent times into time values.
- [AMAZON.WeightUnit](https://docs.aws.amazon.com/lex/latest/dg/built-in-slot-weight.html): Converts words that represent a weight unit into the corresponding abbreviation.
- [Custom Slot Types](https://docs.aws.amazon.com/lex/latest/dg/howitworks-custom-slots.html): For each intent, you can specify parameters that indicate the information that the intent needs to fulfill the user's request.
- [Slot Obfuscation](https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html): Amazon Lex enables you to obfuscate, or hide, the contents of slots so that the content is not visible.
- [Sentiment Analysis](https://docs.aws.amazon.com/lex/latest/dg/sentiment-analysis.html): You can use sentiment analysis to determine the sentiments expressed in a user utterance.

### [Tagging Resources](https://docs.aws.amazon.com/lex/latest/dg/how-it-works-tags.html)

Learn how to use tags to manage Amazon Lex resources.

- [Tagging Resources (Console)](https://docs.aws.amazon.com/lex/latest/dg/tags-console.html): You can use the console to manage tags on a bot, a bot alias, or a bot channel resource.
- [Tagging Resources (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/tags-cli.html): You can use the AWS CLI to manage tags on a bot, a bot alias, or a bot channel resource.


## [Getting Started](https://docs.aws.amazon.com/lex/latest/dg/getting-started.html)

- [Step 1: Set Up an Account](https://docs.aws.amazon.com/lex/latest/dg/gs-account.html): Set up an AWS account for testing Amazon Lex.
- [Step 2: Set Up the AWS CLI](https://docs.aws.amazon.com/lex/latest/dg/gs-set-up-cli.html): Set up the AWS CLI to test Amazon Lex.

### [Step 3: Getting Started (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-console.html)

Use the Amazon Lex console to create your first bot.

### [Exercise 1: Create a Bot Using a Blueprint](https://docs.aws.amazon.com/lex/latest/dg/gs-bp.html)

Use the Amazon Lex console to create a bot by using a blueprint.

- [Step 1: Create an Amazon Lex Bot (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-create-bot.html)

### [Step 2 (Optional): Review the Details of Information Flow (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-details-two-runtime-apis.html)

This section explains the flow of information between a client and Amazon Lex for each user input in our example conversation.

- [Step 2a: Information Flow (PostContent API)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-details-postcontent-flow.html): This section explains the flow of information between the client and Amazon Lex when the client uses speech to send requests.
- [Step 2b: Information Flow (PostText API)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-details-part1.html): This section explains flow of information between client and Amazon Lex in which the client uses the PostText API to send requests.
- [Step 3: Create a Lambda Function (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-create-lambda-function.html): Create a Lambda function (using the lex-order-flowers-python blueprint) and perform test invocation using sample event data in the AWS Lambda console.
- [Step 4: Add the Lambda Function as Code Hook (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-create-integrate.html): In this section, you update the configuration of the OrderFlowers intent to use the Lambda function as follows:
- [Step 5 (Optional): Review the Details of the Information Flow (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-details-after-lambda.html): This section explains the flow of information between the client and Amazon Lex for each user input, including the integration of the Lambda function.
- [Step 6: Update the Intent Configuration to Add an Utterance (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-utterance.html): The OrderFlowers bot is configured with only two utterances.
- [Step 7 (Optional): Clean Up (Console)](https://docs.aws.amazon.com/lex/latest/dg/gs-bp-cleaning-up.html): Now, delete the resources that you created and clean up your account.

### [Exercise 2: Create a Custom Bot](https://docs.aws.amazon.com/lex/latest/dg/getting-started-ex2.html)

Use the Amazon Lex console to create a custom bot.

- [Step 1: Create a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/gs2-prepare.html): First, create a Lambda function which fulfills a pizza order.

### [Step 2: Create a Bot](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot.html)

In this step, you create a bot to handle pizza orders.

- [Create the Bot](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-create.html): Create the PizzaOrderingBot bot with the minimum information needed.
- [Create an Intent](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-intent.html): Now, create the OrderPizza intent , an action that the user wants to perform, with the minimum information needed.
- [Create Slot Types](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-slot-types.html): Create the slot types, or parameter values, that the OrderPizza intent uses.
- [Configure the Intent](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-configure-intent.html): Configure the OrderPizza intent to fulfill a user's request to order a pizza.
- [Configure the Bot](https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-configure-bot.html): Configure error handling for the PizzaOrderingBot bot.
- [Step 3: Build and Test the Bot](https://docs.aws.amazon.com/lex/latest/dg/gs2-build-and-test.html): Make sure the bot works, by building and testing it.
- [Step 4 (Optional): Clean up](https://docs.aws.amazon.com/lex/latest/dg/gs2-clean-up.html): Delete the resources that you created and clean up your account to avoid incurring more charges for the resources you created.
- [Exercise 3: Publish a Version and Create an Alias](https://docs.aws.amazon.com/lex/latest/dg/gettingstarted-ex3.html): In Getting Started Exercises 1 and 2, you created a bot and tested it.

### [Step 4: Getting Started (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-cli.html)

Create your first Amazon Lex bot using the AWS CLI.

### [Exercise 1: Create a Bot](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create.html)

In general, when you create bots, you:

- [Step 1: Create a Service-Linked Role](https://docs.aws.amazon.com/lex/latest/dg/gs-create-role.html): Amazon Lex assumes AWS Identity and Access Management service-linked roles to call AWS services on behalf of your bots.

### [Step 2: Create a Custom Slot Type](https://docs.aws.amazon.com/lex/latest/dg/gs-create-flower-types.html)

Create a custom slot type with enumeration values for the flowers that can be ordered.

- [FlowerTypes.json](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-flower-types-json.html): The following code is the JSON data required to create the FlowerTypes custom slot type:

### [Step 3: Create an Intent](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-order-flowers.html)

Create an intent for the OrderFlowersBot bot and provide three slots, or parameters.

- [OrderFlowers.json](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-order-flowers-json.html): The following code is the JSON data required to create the OrderFlowers intent:

### [Step 4: Create a Bot](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-order-flowers-bot.html)

The OrderFlowersBot bot has one intent, the OrderFlowers intent that you created in the previous step.

- [OrderFlowersBot.json](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-order-flowers-bot-json.html): The following code provides the JSON data required to build the OrderFlowers Amazon Lex bot:

### [Step 5: Test a Bot](https://docs.aws.amazon.com/lex/latest/dg/gs-create-test.html)

To test the bot,you can use either a text-based or a speech-based test.

- [Test the Bot Using Text Input (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-create-test-text.html): To verify that the bot works correctly with text input, use the operation.
- [Test the Bot Using Speech Input (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-create-test-speech.html): To test the bot using audio files, use the operation.
- [Exercise 2: Add a New Utterance](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-update-utterance.html): To improve the machine learning model that Amazon Lex uses to recognize requests from your users, add another sample utterance to the bot.
- [Exercise 3: Add a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-update-lambda.html): Add a Lambda function that validates user input and fulfills the user's intent to the bot.

### [Exercise 4: Publish a Version](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-publish.html)

Now, create a version of the bot that you created in Exercise 1.

- [Step 1: Publish the Slot Type (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-publish-slot-type.html): Before you can publish a version of any intents that use a slot type, you must publish a version of that slot type.
- [Step 2: Publish the Intent (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-publish-intent.html): Before you can publish an intent, you have to publish all of the slot types referred to by the intent.
- [Step 3: Publish the Bot (AWS CLI)](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-publish-bot.html): After you have published all of the slot types and intents that are used by your bot, you can publish the bot.
- [Exercise 5: Create an Alias](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-create-alias.html): An alias is a pointer to a specific version of a bot.
- [Exercise 6: Clean Up](https://docs.aws.amazon.com/lex/latest/dg/gs-cli-clean-up.html): Delete the resources that you created and clean up your account.


## [Using Lambda Functions](https://docs.aws.amazon.com/lex/latest/dg/using-lambda.html)

- [Lambda Function Input Event and Response Format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html): This section describes the structure of the event data that Amazon Lex provides to a Lambda function.
- [Amazon Lex and AWS Lambda Blueprints](https://docs.aws.amazon.com/lex/latest/dg/lex-lambda-blueprints.html): The Amazon Lex console provides example bots (called bot blueprints) that are preconfigured so you can quickly create and test a bot in the console.


## [Deploying Bots](https://docs.aws.amazon.com/lex/latest/dg/examples.html)

### [Deploying an Amazon Lex Bot on a Messaging Platform](https://docs.aws.amazon.com/lex/latest/dg/example1.html)

This section explains how to deploy Amazon Lex bots on the Facebook, Slack, and Twilio messaging platforms.

- [Integrating with Facebook](https://docs.aws.amazon.com/lex/latest/dg/fb-bot-association.html): This exercise shows how to integrate Facebook Messenger with your Amazon Lex bot.

### [Integrating with Kik](https://docs.aws.amazon.com/lex/latest/dg/kik-bot-association.html)

This exercise provides instructions for integrating an Amazon Lex bot with the Kik messaging application.

- [Step 1: Create an Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/kik-bot-assoc-create-bot.html): If you don't already have an Amazon Lex bot, create and deploy one.
- [Step 2: Create a Kik Bot](https://docs.aws.amazon.com/lex/latest/dg/kik-bot-assoc-create-kik-bot.html): In this step you use the Kik user interface to create a Kik bot.
- [Step 3: Integrate the Kik Bot with the Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/kik-bot-assoc-create-assoc.html): Now that you have created an Amazon Lex bot and a Kik bot, you are ready to create an channel association between them in Amazon Lex.
- [Step 4: Test the Integration](https://docs.aws.amazon.com/lex/latest/dg/kik-bot-assoc-test.html): Now that you have created an association between your Amazon Lex bot and Kik, you can use the Kik app to test the association.

### [Integrating with Slack](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-association.html)

This exercise provides instructions for integrating an Amazon Lex bot with the Slack messaging application.

- [Step 1: Create an Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-bot.html): If you don't already have an Amazon Lex bot, create and deploy one.
- [Step 2: Sign Up for Slack and Create a Slack Team](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-team.html): Sign up for a Slack account and create a Slack team.
- [Step 3: Create a Slack Application](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-app.html): In this section, you do the following:
- [Step 4: Integrate the Slack Application with the Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-assoc.html): Now that you have Slack application credentials, you can integrate the application with your Amazon Lex bot.
- [Step 5: Complete Slack Integration](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-back-in-slack-console.html): In this section, use the Slack API console to complete integration of the Slack application.
- [Step 6: Test the Integration](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-test.html): Now use a browser window to test the integration of Slack with your Amazon Lex bot.
- [Integrating with Twilio SMS](https://docs.aws.amazon.com/lex/latest/dg/twilio-bot-association.html): This exercise provides instructions for integrating an Amazon Lex bot with the Twilio simple messaging service (SMS).
- [Deploying an Amazon Lex Bot in Mobile Applications](https://docs.aws.amazon.com/lex/latest/dg/example2.html): Using AWS Amplify, you can integrate your Amazon Lex bots with mobile or web applications.


## [Importing and Exporting](https://docs.aws.amazon.com/lex/latest/dg/import-export.html)

### [Exporting and Importing in Amazon Lex Format](https://docs.aws.amazon.com/lex/latest/dg/import-export-lex.html)

To export bots, intents, and slot types, from Amazon Lex with the intention of reimporting into Amazon Lex, you use create a JSON file in Amazon Lex format.

- [Exporting in Amazon Lex Format](https://docs.aws.amazon.com/lex/latest/dg/export-to-lex.html): Export your Amazon Lex bots, intents, and slot types to a format that you can import to an AWS account.
- [Importing in Amazon Lex Format](https://docs.aws.amazon.com/lex/latest/dg/import-from-lex.html): After you have exported a resource to a JSON file in the Amazon Lex format, you can import the JSON file containing the resource into one or more AWS accounts.
- [JSON Format for Importing and Exporting](https://docs.aws.amazon.com/lex/latest/dg/import-export-format.html): The following examples show the JSON structure for exporting and importing slot types, intents, and bots in Amazon Lex format.
- [Exporting to an Alexa Skill](https://docs.aws.amazon.com/lex/latest/dg/export-to-alexa.html): You can export your bot schema in a format compatible with an Alexa skill.


## [Bot Examples](https://docs.aws.amazon.com/lex/latest/dg/additional-exercises.html)

### [Schedule Appointment](https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt.html)

Getting started exercise that uses the Amazon Lex console.

- [Step 1: Create an Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt-create-bot.html): In this section, you create an Amazon Lex bot using the ScheduleAppointment blueprint, which is provided in the Amazon Lex console.
- [Step 2: Create a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt-create-lambda-function.html): In this section, you create a Lambda function using a blueprint (lex-make-appointment-python) that is provided in the Lambda console.
- [Step 3: Update the Intent: Configure a Code Hook](https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt-create-integrate.html): In this section, you update the configuration of the MakeAppointment intent to use the Lambda function as a code hook for the validation and fulfillment activities.
- [Step 4: Deploy the Bot on the Facebook Messenger Platform](https://docs.aws.amazon.com/lex/latest/dg/ex-sch-appt-fb-integration.html): In the preceding section, you tested the ScheduleAppointment bot using the client in the Amazon Lex console.
- [Details of Information Flow](https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt-info-flow-details.html): The ScheduleAppointment bot blueprint primarily showcases the use of dynamically generated response cards.

### [Book Trip](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip.html)

Getting started exercise that uses Amazon Lex console.

- [Step 1: Blueprint Review](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip-blueprints.html)
- [Step 2: Create an Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip-create-bot.html): In this section, you create an Amazon Lex bot (BookTrip).
- [Step 3: Create a Lambda function](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip-create-lambda-function.html): In this section you create a Lambda function using a blueprint (lex-book-trip-python) provided in the AWS Lambda console.
- [Step 4: Add the Lambda Function as a Code Hook](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip-create-integrate.html): In this section, you update the configurations of both the BookCar and BookHotel intents by adding the Lambda function as a code hook for initialization/validation and fulfillment activities.
- [Details of the Information Flow](https://docs.aws.amazon.com/lex/latest/dg/book-trip-detail-flow.html): In this exercise, you engaged in a conversation with the Amazon Lex BookTrip bot using the test window client provided in the Amazon Lex console.
- [Example: Using a Response Card](https://docs.aws.amazon.com/lex/latest/dg/ex-resp-card.html): Bot exercise that uses response card for a slot.
- [Updating Utterances](https://docs.aws.amazon.com/lex/latest/dg/ex-utterances.html): In this exercise, you add additional utterances to those you created in Getting Started Exercise 1.
- [Integrating with a Web site](https://docs.aws.amazon.com/lex/latest/dg/ex-web.html): In this example you integrate a bot with a Web site using text and voice.

### [Call Center Agent Assistant](https://docs.aws.amazon.com/lex/latest/dg/ex-agent.html)

Learn how to create an Amazon Lex bot that customer support agents can use to answer customer questions by searching for answers with Amazon Kendra.

- [Step 1: Create an Amazon Kendra Index](https://docs.aws.amazon.com/lex/latest/dg/agent-step-1.html): To create an Amazon Lex bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, first create an Amazon Kendra index of documents that contain answers to commonly asked questions.
- [Step 2: Create an Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/agent-step-2.html): To create an Amazon Lex agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, create a bot that you later configure with an intent that queries the Amazon Kendra index and displays the suggested answers .
- [Step 3: Add a Custom and Built-in Intent](https://docs.aws.amazon.com/lex/latest/dg/agent-step-3.html): To create an Amazon Lex bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, add a custom and built-in intent to the agent assistant bot.
- [Step 4: Set up Amazon Cognito](https://docs.aws.amazon.com/lex/latest/dg/agent-step-4.html): To create an Amazon Lex agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, also set up Amazon Cognito to manage access permissions.
- [Step 5: Deploy Your Bot as a Web Application](https://docs.aws.amazon.com/lex/latest/dg/agent-step-5.html): Deploy an Amazon Lex agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions as a web application.
- [Step 6: Use the Bot](https://docs.aws.amazon.com/lex/latest/dg/agent-step-6.html): The web application is hosted in the browser using the AWS SDK for JavaScript.


## [Migrating a bot](https://docs.aws.amazon.com/lex/latest/dg/migrate.html)

### [Migration messages](https://docs.aws.amazon.com/lex/latest/dg/migrate-messages.html)

During migration, Amazon Lex may find resources, such as built-in slot types, that it can't migrate to the equivalent Amazon Lex V2 resource.

- [Built-in intent](https://docs.aws.amazon.com/lex/latest/dg/message-built-in-intent.html): When you use a built-in intent that is not supported in Amazon Lex V2, the intent is mapped to a custom intent in your Amazon Lex V2 bot.
- [Built-in slot type](https://docs.aws.amazon.com/lex/latest/dg/message-built-in-slot-type.html): Any migrated slot that uses a slot type that is not supported in Amazon Lex V2 won't be given a slot type value.
- [Conversation logs](https://docs.aws.amazon.com/lex/latest/dg/message-logs.html): Migration doesn't update the conversation log settings of the Amazon Lex V2 bot.
- [Message groups](https://docs.aws.amazon.com/lex/latest/dg/migrate-message-groups.html): Amazon Lex V2 supports only one message and two alternative messages per message group.
- [Prompts and phrases](https://docs.aws.amazon.com/lex/latest/dg/message-prompts-phrases.html): Amazon Lex V2 uses a different mechanism for follow up, clarification, and hang up prompts.
- [Other Amazon Lex V1 features](https://docs.aws.amazon.com/lex/latest/dg/message-features.html): The migration tool supports only migration of Amazon Lex V1 bots and their underlying intents, slot types, and slots.
- [Migrating a Lambda function](https://docs.aws.amazon.com/lex/latest/dg/message-lambda.html): Amazon Lex V2 allows only one Lambda function for each language in a bot.


## [Security](https://docs.aws.amazon.com/lex/latest/dg/security.html)

### [Data Protection](https://docs.aws.amazon.com/lex/latest/dg/data-protection.html)

Amazon Lex collects customer content for troubleshooting and to help improve the service.

- [Encryption at Rest](https://docs.aws.amazon.com/lex/latest/dg/at-rest.html): Amazon Lex encrypts the user utterances that it stores.
- [Encryption in Transit](https://docs.aws.amazon.com/lex/latest/dg/in-transit.html): Amazon Lex uses the HTTPS protocol to communicate with your client application.
- [Key Management](https://docs.aws.amazon.com/lex/latest/dg/key-management.html): Amazon Lex protects your content from unauthorized use with internal keys.

### [Identity and Access Management](https://docs.aws.amazon.com/lex/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Amazon Lex resources.

- [How Amazon Lex works with IAM](https://docs.aws.amazon.com/lex/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Lex, learn what IAM features are available to use with Amazon Lex.
- [Identity-based policy examples](https://docs.aws.amazon.com/lex/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Lex resources.
- [AWS managed policies for Amazon Lex](https://docs.aws.amazon.com/lex/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Lex and recent changes to those policies.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/lex/latest/dg/using-service-linked-roles.html): How to use service-linked roles to give Amazon Lex access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/lex/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Lex and IAM.

### [Monitoring](https://docs.aws.amazon.com/lex/latest/dg/monitoring-aws-lex.html)

Monitor Amazon Lex to maintain reliability, availability, and performance.

- [Monitoring Amazon Lex with CloudWatch](https://docs.aws.amazon.com/lex/latest/dg/monitoring-aws-lex-cloudwatch.html): To track the health of your Amazon Lex bots, use Amazon CloudWatch.
- [Logging Amazon Lex API Calls with AWS CloudTrail](https://docs.aws.amazon.com/lex/latest/dg/monitoring-aws-lex-cloudtrail.html): Amazon Lex is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Lex.
- [Compliance Validation](https://docs.aws.amazon.com/lex/latest/dg/compliance.html): Learn which AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/lex/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and discover specific Amazon Lex features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/lex/latest/dg/infrastructure-security.html): Learn how Amazon Lex isolates service traffic.


## [Guidelines and Quotas](https://docs.aws.amazon.com/lex/latest/dg/guidelines-and-limits.html)

- [Supported Regions](https://docs.aws.amazon.com/lex/latest/dg/supported-regions.html): For a list of AWS Regions where Amazon Lex is available, see AWS Regions and Endpoints in the Amazon Web Services General Reference.
- [General Guidelines](https://docs.aws.amazon.com/lex/latest/dg/gl-guidelines.html): This section describes general guidelines when using Amazon Lex.
- [Quotas](https://docs.aws.amazon.com/lex/latest/dg/gl-limits.html): This section describes current quotas in Amazon Lex.


## [API Reference](https://docs.aws.amazon.com/lex/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html)

The following actions are supported by Amazon Lex Model Building Service:

### [Amazon Lex Model Building Service](https://docs.aws.amazon.com/lex/latest/dg/API_Operations_Amazon_Lex_Model_Building_Service.html)

The following actions are supported by Amazon Lex Model Building Service:

- [CreateBotVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateBotVersion.html): Creates a new version of the bot based on the $LATEST version.
- [CreateIntentVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateIntentVersion.html): Creates a new version of an intent based on the $LATEST version of the intent.
- [CreateSlotTypeVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateSlotTypeVersion.html): Creates a new version of a slot type based on the $LATEST version of the specified slot type.
- [DeleteBot](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBot.html): Deletes all versions of the bot, including the $LATEST version.
- [DeleteBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotAlias.html): Deletes an alias for the specified bot.
- [DeleteBotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotChannelAssociation.html): Deletes the association between an Amazon Lex bot and a messaging platform.
- [DeleteBotVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotVersion.html): Deletes a specific version of a bot.
- [DeleteIntent](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteIntent.html): Deletes all versions of the intent, including the $LATEST version.
- [DeleteIntentVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteIntentVersion.html): Deletes a specific version of an intent.
- [DeleteSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteSlotType.html): Deletes all versions of the slot type, including the $LATEST version.
- [DeleteSlotTypeVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteSlotTypeVersion.html): Deletes a specific version of a slot type.
- [DeleteUtterances](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteUtterances.html): Deletes stored utterances.
- [GetBot](https://docs.aws.amazon.com/lex/latest/dg/API_GetBot.html): Returns metadata information for a specific bot.
- [GetBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAlias.html): Returns information about an Amazon Lex bot alias.
- [GetBotAliases](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAliases.html): Returns a list of aliases for a specified Amazon Lex bot.
- [GetBotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociation.html): Returns information about the association between an Amazon Lex bot and a messaging platform.
- [GetBotChannelAssociations](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociations.html): Returns a list of all of the channels associated with the specified bot.
- [GetBots](https://docs.aws.amazon.com/lex/latest/dg/API_GetBots.html): Returns bot information as follows:
- [GetBotVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotVersions.html): Gets information about all of the versions of a bot.
- [GetBuiltinIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntent.html): Returns information about a built-in intent.
- [GetBuiltinIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntents.html): Gets a list of built-in intents that meet the specified criteria.
- [GetBuiltinSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinSlotTypes.html): Gets a list of built-in slot types that meet the specified criteria.
- [GetExport](https://docs.aws.amazon.com/lex/latest/dg/API_GetExport.html): Exports the contents of a Amazon Lex resource in a specified format.
- [GetImport](https://docs.aws.amazon.com/lex/latest/dg/API_GetImport.html): Gets information about an import job started with the StartImport operation.
- [GetIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntent.html): Returns information about an intent.
- [GetIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntents.html): Returns intent information as follows:
- [GetIntentVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntentVersions.html): Gets information about all of the versions of an intent.
- [GetMigration](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigration.html): Provides details about an ongoing or complete migration from an Amazon Lex V1 bot to an Amazon Lex V2 bot.
- [GetMigrations](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigrations.html): Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.
- [GetSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotType.html): Returns information about a specific version of a slot type.
- [GetSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypes.html): Returns slot type information as follows:
- [GetSlotTypeVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypeVersions.html): Gets information about all versions of a slot type.
- [GetUtterancesView](https://docs.aws.amazon.com/lex/latest/dg/API_GetUtterancesView.html): Use the GetUtterancesView operation to get information about the utterances that your users have made to your bot.
- [ListTagsForResource](https://docs.aws.amazon.com/lex/latest/dg/API_ListTagsForResource.html): Gets a list of tags associated with the specified resource.
- [PutBot](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html): Creates an Amazon Lex conversational bot or replaces an existing bot.
- [PutBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_PutBotAlias.html): Creates an alias for the specified version of the bot or replaces an alias for the specified bot.
- [PutIntent](https://docs.aws.amazon.com/lex/latest/dg/API_PutIntent.html): Creates an intent or replaces an existing intent.
- [PutSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_PutSlotType.html): Creates a custom slot type or replaces an existing custom slot type.
- [StartImport](https://docs.aws.amazon.com/lex/latest/dg/API_StartImport.html): Starts a job to import a resource to Amazon Lex.
- [StartMigration](https://docs.aws.amazon.com/lex/latest/dg/API_StartMigration.html): Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2.
- [TagResource](https://docs.aws.amazon.com/lex/latest/dg/API_TagResource.html): Adds the specified tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/lex/latest/dg/API_UntagResource.html): Removes tags from a bot, bot alias or bot channel.

### [Amazon Lex Runtime Service](https://docs.aws.amazon.com/lex/latest/dg/API_Operations_Amazon_Lex_Runtime_Service.html)

The following actions are supported by Amazon Lex Runtime Service:

- [DeleteSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_DeleteSession.html): Removes session information for a specified bot, alias, and user ID.
- [GetSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GetSession.html): Returns session information for a specified bot, alias, and user ID.
- [PostContent](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html): Sends user input (text or speech) to Amazon Lex.
- [PostText](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html): Sends user input to Amazon Lex.
- [PutSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PutSession.html): Creates a new session or modifies an existing session with an Amazon Lex bot.

### [Data Types](https://docs.aws.amazon.com/lex/latest/dg/API_Types.html)

The following data types are supported by Amazon Lex Model Building Service:

### [Amazon Lex Model Building Service](https://docs.aws.amazon.com/lex/latest/dg/API_Types_Amazon_Lex_Model_Building_Service.html)

The following data types are supported by Amazon Lex Model Building Service:

- [BotAliasMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_BotAliasMetadata.html): Provides information about a bot alias.
- [BotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_BotChannelAssociation.html): Represents an association between an Amazon Lex bot and an external messaging platform.
- [BotMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html): Provides information about a bot. .
- [BuiltinIntentMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_BuiltinIntentMetadata.html): Provides metadata for a built-in intent.
- [BuiltinIntentSlot](https://docs.aws.amazon.com/lex/latest/dg/API_BuiltinIntentSlot.html): Provides information about a slot used in a built-in intent.
- [BuiltinSlotTypeMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_BuiltinSlotTypeMetadata.html): Provides information about a built in slot type.
- [CodeHook](https://docs.aws.amazon.com/lex/latest/dg/API_CodeHook.html): Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot..
- [ConversationLogsRequest](https://docs.aws.amazon.com/lex/latest/dg/API_ConversationLogsRequest.html): Provides the settings needed for conversation logs.
- [ConversationLogsResponse](https://docs.aws.amazon.com/lex/latest/dg/API_ConversationLogsResponse.html): Contains information about conversation log settings.
- [EnumerationValue](https://docs.aws.amazon.com/lex/latest/dg/API_EnumerationValue.html): Each slot type can have a set of values.
- [FollowUpPrompt](https://docs.aws.amazon.com/lex/latest/dg/API_FollowUpPrompt.html): A prompt for additional activity after an intent is fulfilled.
- [FulfillmentActivity](https://docs.aws.amazon.com/lex/latest/dg/API_FulfillmentActivity.html): Describes how the intent is fulfilled after the user provides all of the information required for the intent.
- [InputContext](https://docs.aws.amazon.com/lex/latest/dg/API_InputContext.html): The name of a context that must be active for an intent to be selected by Amazon Lex.
- [Intent](https://docs.aws.amazon.com/lex/latest/dg/API_Intent.html): Identifies the specific version of an intent.
- [IntentMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_IntentMetadata.html): Provides information about an intent.
- [KendraConfiguration](https://docs.aws.amazon.com/lex/latest/dg/API_KendraConfiguration.html): Provides configuration information for the AMAZON.KendraSearchIntent intent.
- [LogSettingsRequest](https://docs.aws.amazon.com/lex/latest/dg/API_LogSettingsRequest.html): Settings used to configure delivery mode and destination for conversation logs.
- [LogSettingsResponse](https://docs.aws.amazon.com/lex/latest/dg/API_LogSettingsResponse.html): The settings for conversation logs.
- [Message](https://docs.aws.amazon.com/lex/latest/dg/API_Message.html): The message object that provides the message text and its type.
- [MigrationAlert](https://docs.aws.amazon.com/lex/latest/dg/API_MigrationAlert.html): Provides information about alerts and warnings that Amazon Lex sends during a migration.
- [MigrationSummary](https://docs.aws.amazon.com/lex/latest/dg/API_MigrationSummary.html): Provides information about migrating a bot from Amazon Lex V1 to Amazon Lex V2.
- [OutputContext](https://docs.aws.amazon.com/lex/latest/dg/API_OutputContext.html): The specification of an output context that is set when an intent is fulfilled.
- [Prompt](https://docs.aws.amazon.com/lex/latest/dg/API_Prompt.html): Obtains information from the user.
- [ResourceReference](https://docs.aws.amazon.com/lex/latest/dg/API_ResourceReference.html): Describes the resource that refers to the resource that you are attempting to delete.
- [Slot](https://docs.aws.amazon.com/lex/latest/dg/API_Slot.html): Identifies the version of a specific slot.
- [SlotDefaultValue](https://docs.aws.amazon.com/lex/latest/dg/API_SlotDefaultValue.html): A default value for a slot.
- [SlotDefaultValueSpec](https://docs.aws.amazon.com/lex/latest/dg/API_SlotDefaultValueSpec.html): Contains the default values for a slot.
- [SlotTypeConfiguration](https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeConfiguration.html): Provides configuration information for a slot type.
- [SlotTypeMetadata](https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeMetadata.html): Provides information about a slot type..
- [SlotTypeRegexConfiguration](https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeRegexConfiguration.html): Provides a regular expression used to validate the value of a slot.
- [Statement](https://docs.aws.amazon.com/lex/latest/dg/API_Statement.html): A collection of messages that convey information to the user.
- [Tag](https://docs.aws.amazon.com/lex/latest/dg/API_Tag.html): A list of key/value pairs that identify a bot, bot alias, or bot channel.
- [UtteranceData](https://docs.aws.amazon.com/lex/latest/dg/API_UtteranceData.html): Provides information about a single utterance that was made to your bot.
- [UtteranceList](https://docs.aws.amazon.com/lex/latest/dg/API_UtteranceList.html): Provides a list of utterances that have been made to a specific version of your bot.

### [Amazon Lex Runtime Service](https://docs.aws.amazon.com/lex/latest/dg/API_Types_Amazon_Lex_Runtime_Service.html)

The following data types are supported by Amazon Lex Runtime Service:

- [ActiveContext](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_ActiveContext.html): A context is a variable that contains information about the current state of the conversation between a user and Amazon Lex.
- [ActiveContextTimeToLive](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_ActiveContextTimeToLive.html): The length of time or number of turns that a context remains active.
- [Button](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_Button.html): Represents an option to be shown on the client platform (Facebook, Slack, etc.)
- [DialogAction](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_DialogAction.html): Describes the next action that the bot should take in its interaction with the user and provides information about the context in which the action takes place.
- [GenericAttachment](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GenericAttachment.html): Represents an option rendered to the user when a prompt is shown.
- [IntentConfidence](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_IntentConfidence.html): Provides a score that indicates the confidence that Amazon Lex has that an intent is the one that satisfies the user's intent.
- [IntentSummary](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_IntentSummary.html): Provides information about the state of an intent.
- [PredictedIntent](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PredictedIntent.html): An intent that Amazon Lex suggests satisfies the user's intent.
- [ResponseCard](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_ResponseCard.html): If you configure a response card when creating your bots, Amazon Lex substitutes the session attributes and slot values that are available, and then returns it.
- [SentimentResponse](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_SentimentResponse.html): The sentiment expressed in an utterance.
