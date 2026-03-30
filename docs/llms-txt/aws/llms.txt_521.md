# Source: https://docs.aws.amazon.com/lexv2/latest/dg/llms.txt

# Amazon Lex V2 Developer Guide

> Provides a conceptual overview of Amazon Lex V2. Includes detailed instructions for using various features, such as streaming conversations, and provides a complete reference for the V2 APIs.

- [Latest features](https://docs.aws.amazon.com/lexv2/latest/dg/latest-features.html)
- [Creating a network of bots for your Lex V2 bots](https://docs.aws.amazon.com/lexv2/latest/dg/network-of-bots.html)
- [Guidelines and best practices](https://docs.aws.amazon.com/lexv2/latest/dg/guidelines.html)
- [Quotas](https://docs.aws.amazon.com/lexv2/latest/dg/quotas.html)
- [Migration guide](https://docs.aws.amazon.com/lexv2/latest/dg/migration.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/lexv2/latest/dg/creating-resources-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/lexv2/latest/dg/doc-history.html)
- [API reference](https://docs.aws.amazon.com/lexv2/latest/dg/api_ref.html)
- [AWS Glossary](https://docs.aws.amazon.com/lexv2/latest/dg/glossary.html)

## [What is Amazon Lex V2?](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/lexv2/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Amazon Lex V2 core concepts](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html)

- [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html): Learn the languages and locales that you can use for your Amazon Lex V2 bots.


## [Getting started](https://docs.aws.amazon.com/lexv2/latest/dg/getting-started.html)

- [Step 1: Set up an account](https://docs.aws.amazon.com/lexv2/latest/dg/gs-account.html): Set up an AWS account for testing Amazon Lex V2.

### [Step 2: Getting started (console)](https://docs.aws.amazon.com/lexv2/latest/dg/gs-console.html)

Use the Amazon Lex V2 console to create your first bot.

- [Quick Start: Create a chatbot in 5 minutes](https://docs.aws.amazon.com/lexv2/latest/dg/quick-start.html): Get started quickly with Amazon Lex V2 using pre-built chatbot templates.
- [Exercise 1: Create a chatbot from a template](https://docs.aws.amazon.com/lexv2/latest/dg/exercise-1.html): Create and test your first Amazon Lex V2 chatbot.
- [Exercise 2: Review the conversation flow](https://docs.aws.amazon.com/lexv2/latest/dg/exercise-2.html): See the JSON structures sent by Amazon Lex V2 during a conversation with your client application.
- [Exercise 3: Build an advanced customer service chatbot](https://docs.aws.amazon.com/lexv2/latest/dg/exercise-3.html): Create a comprehensive customer service chatbot that handles order verification, upselling, lead generation, and multi-turn conversations using AI-powered features.
- [Best Practices for Getting Started](https://docs.aws.amazon.com/lexv2/latest/dg/getting-started-best-practices.html): Essential guidelines for building effective Amazon Lex V2 chatbots from the beginning.


## [Bot examples](https://docs.aws.amazon.com/lexv2/latest/dg/examples.html)

### [Call center agent assistant](https://docs.aws.amazon.com/lexv2/latest/dg/example-call-center.html)

Learn how to create an Amazon Lex V2 bot that customer support agents can use to answer customer questions by searching for answers with Amazon Kendra.

- [Step 1: Create an Amazon Kendra Index](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-1.html): To create an Amazon Lex V2 bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, first create an Amazon Kendra index of documents that contain answers to commonly asked questions.
- [Step 2: Create an Amazon Lex V2 Bot](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-2.html): To create an Amazon Lex V2 agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, create a bot that you later configure with an intent that queries the Amazon Kendra index and displays the suggested answers .
- [Step 3: Add a Custom and Built-in Intent](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-3.html): To create an Amazon Lex V2 bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, add a custom and built-in intent to the agent assistant bot.
- [Step 4: Set up Amazon Cognito](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-4.html): To create an Amazon Lex V2 agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions, also set up Amazon Cognito to manage access permissions.
- [Step 5: Deploy Your Bot as a Web Application](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-5.html): Deploy an Amazon Lex V2 agent assistant bot that uses Amazon Kendra to provide a customer service agent with answers to common questions as a web application.
- [Step 6: Use the Bot](https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-6.html): The web application is hosted in the browser using the AWS SDK for JavaScript.


## [Working with Amazon Lex V2 bots](https://docs.aws.amazon.com/lexv2/latest/dg/building-bots.html)

- [Changes to conversation flows in Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/understanding-new-flows.html): Learn about the changes to the way Amazon Lex V2 manages conversations with your users.

### [Different ways to create a bot with Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/create-bot.html)

Learn the different ways of creating a bot with Amazon Lex V2.

- [Using the console](https://docs.aws.amazon.com/lexv2/latest/dg/create-bot-console.html): Learn how to create a bot using the Amazon Lex V2 console.
- [Using bot templates](https://docs.aws.amazon.com/lexv2/latest/dg/bot-templates.html): Amazon Lex V2 offers pre-built solutions to create experiences at scale and drive digital engagement.

### [Creating Amazon Lex V2 bots using the Automated Chatbot Designer](https://docs.aws.amazon.com/lexv2/latest/dg/designing.html)

Use automation tools to start the design of your Amazon Lex V2 bot.

- [Importing conversation transcripts](https://docs.aws.amazon.com/lexv2/latest/dg/designing-import.html): Learn how to import conversation transcripts into an Amazon Lex V2 bot.
- [Creating intents and slot types](https://docs.aws.amazon.com/lexv2/latest/dg/designing-create.html): Create intents and slots for your Amazon Lex bot from imported transcripts.
- [Input transcript format](https://docs.aws.amazon.com/lexv2/latest/dg/designing-input-format.html): See the JSON format for importing transcripts with the Automatic Chatbot designer.
- [Output transcript format](https://docs.aws.amazon.com/lexv2/latest/dg/designing-output-format.html): See the output JSON format from the Automated Chatbot Designer
- [Adding a new language to an Amazon Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/add-language.html): You add one or more languages and locales to your bot to enable it to communicate with users in their languages.

### [Adding intents](https://docs.aws.amazon.com/lexv2/latest/dg/add-intents.html)

Intents are the goals that your users want to accomplish, such as ordering flowers or booking a hotel.

- [Sample utterances](https://docs.aws.amazon.com/lexv2/latest/dg/sample-utterances.html): Learn about creating and generating sample utterances for intent recognition in Amazon Lex V2.

### [Intent structure](https://docs.aws.amazon.com/lexv2/latest/dg/intent-structure.html)

Intents are the goals that your users want to accomplish, such as ordering flowers or booking a hotel.

- [Initial response](https://docs.aws.amazon.com/lexv2/latest/dg/intent-initial.html): The initial response is sent to the user after Amazon Lex V2 determines the intent and before it starts to elicit slot values.

### [Slots](https://docs.aws.amazon.com/lexv2/latest/dg/intent-slots.html)

Slots are values provided by the user to fulfill the intent.

- [Re-eliciting slots](https://docs.aws.amazon.com/lexv2/latest/dg/reelicit-slots.html): You can configure your bot to re-elicit a slot that has already been filled by setting that slot value to null and setting the next step in the conversation to loop back to eliciting that slot.
- [Using multiple values in a slot](https://docs.aws.amazon.com/lexv2/latest/dg/multi-valued-slots.html): Learn how to create intents that accept multiple values in a single slot.
- [Confirmation](https://docs.aws.amazon.com/lexv2/latest/dg/intent-confirm.html): After the conversation with the user is complete and the slot values for the intent are filled, you can configure a confirmation prompt to ask the user if the slot values are correct.
- [Fulfillment](https://docs.aws.amazon.com/lexv2/latest/dg/intent-fulfillment.html): After all the slot values are provided by the user for the intent, Amazon Lex V2 fulfills the userâs request.
- [Closing response](https://docs.aws.amazon.com/lexv2/latest/dg/intent-closing.html): The closing response is sent to your user after their intent is fulfilled.

### [Creating conversation paths](https://docs.aws.amazon.com/lexv2/latest/dg/building-paths.html)

Learn how to use conditional statements to build complex conversations with Amazon Lex V2

- [Configure next steps in the conversation](https://docs.aws.amazon.com/lexv2/latest/dg/paths-nextstep.html): Learn how to configure the next steps in the conversation during a conversation with Amazon Lex V2
- [Set values during the conversation](https://docs.aws.amazon.com/lexv2/latest/dg/paths-setting-values.html): Learn how to set slot and session attribute values during a conversation with Amazon Lex V2
- [Add conditions to branch conversations](https://docs.aws.amazon.com/lexv2/latest/dg/paths-branching.html): Learn how to use conditional branching to create complex conversation paths.
- [Invoke dialog code hook](https://docs.aws.amazon.com/lexv2/latest/dg/paths-code-hook.html): Learn how to use Lambda functions as a code hook to control conversations with your Amazon Lex V2 bot.
- [Using Visual conversation builder](https://docs.aws.amazon.com/lexv2/latest/dg/visual-conversation-builder.html): Visual conversation builder is a drag and drop conversation builder to easily design and visualize conversation paths by using intents within a rich visual environment.

### [Built-in intents](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intents.html)

For common actions, you can use the standard built-in intents library.

- [AMAZON.BedrockAgentIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-bedrockagent.html)
- [AMAZON.CancelIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-cancel.html): Responds to words and phrases that indicate the user wants to cancel the current interaction.
- [AMAZON.FallbackIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-fallback.html): When a user's input to an intent isn't what a bot expects, you can configure Amazon Lex V2 to invoke a fallback intent.
- [AMAZON.HelpIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-help.html): Responds to words or phrases that indicate the user needs help while interacting with your bot.

### [AMAZON.KendraSearchIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-kendra-search.html)

To search documents that you have indexed with Amazon Kendra, use the AMAZON.KendraSearchIntent intent.

- [Example: Creating a FAQ Bot for an Amazon Kendra Index](https://docs.aws.amazon.com/lexv2/latest/dg/faq-bot-kendra-search.html): This example creates an Amazon Lex V2 bot that uses an Amazon Kendra index to provide answers to users' questions.
- [AMAZON.PauseIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-pause.html): Responds to words and phrases that enable the user to pause an interaction with a bot so that they can return to it later.
- [AMAZON.QnAIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qna.html)
- [AMAZON.QnAIntent (multiple use support)](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qna-multi.html): You can choose to have multiple AMAZON.QnAIntents within a locale.
- [AMAZON.QinConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html)
- [AMAZON.RepeatIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-repeat.html): Responds to words and phrases that enable the user to repeat the previous message.
- [AMAZON.ResumeIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-resume.html): Responds to words and phrases the enable the user to resume a previously paused intent.
- [AMAZON.StartOverIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-start-over.html): Responds to words and phrases that enable the user to stop processing the current intent and start over from the beginning.
- [AMAZON.StopIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-stop.html): Responds to words and phrases that indicate that the user wants to stop processing the current intent and end the interaction with a bot.

### [Adding slot types](https://docs.aws.amazon.com/lexv2/latest/dg/add-slot-types.html)

Slot types define the values that users can supply for your intent variables.

### [Built-in slot types](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slots.html)

Amazon Lex supports built-in slot types that define how data in the slot is recognized and handled.

- [AMAZON.AlphaNumeric](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumeric.html): Recognizes strings made up of letters and numbers, such as APQ123.
- [AMAZON.City](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-city.html): Provides a list of local and world cities.
- [AMAZON.Confirmation](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-confirmation.html): This slot type recognizes input phrases that corresponds to 'Yes', 'No', 'Maybe', and 'Don't know' phrases and words for Amazon Lex V2 and converts it one of the four values.
- [AMAZON.Country](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-country.html): The names of countries around the world.
- [AMAZON.Currency](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-currency.html): Converts words that represent a currency into a standard ISO 4217 alphabetic currency code and a number.
- [AMAZON.Date](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-date.html): Converts words that represent dates into a date format.
- [AMAZON.Duration](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-duration.html): Converts words that indicate durations into a numeric duration.
- [AMAZON.EmailAddress](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-email.html): Recognizes words that represent an email address provided as username@domain.
- [AMAZON.FirstName](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-first-name.html): Commonly used first names.
- [AMAZON.LastName](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-last-name.html): Commonly used last names.
- [AMAZON.Number](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-number.html): Converts words or numbers that express a number into digits, including decimal numbers.
- [AMAZON.Percentage](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-percent.html): Converts words and symbols that represent a percentage into a numeric value with a percent sign (%).
- [AMAZON.PhoneNumber](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-phone.html): Converts the numbers or words that represent a phone number into a string format without punctuation as follows.
- [AMAZON.State](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-state.html): The names of geographical and political regions within countries.
- [AMAZON.StreetName](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-street-name.html): The names of streets within a typical street address.
- [AMAZON.Time](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-time.html): Converts words that represent times into time values.
- [AMAZON.UKPostalCode](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-uk-postal-code.html): Converts words that represent a UK postal code to a standard format for postal codes in the United Kingdom.
- [AMAZON.FreeFormInput](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-free-form.html): AMAZON.FreeFormInput can be used to capture free form input from the end user.
- [Custom slot type](https://docs.aws.amazon.com/lexv2/latest/dg/custom-slot-types.html): Learn how to create your own custom slot types for your Amazon Lex V2 intents.

### [Grammar slot type](https://docs.aws.amazon.com/lexv2/latest/dg/building-srgs.html)

Learn how to use the Amazon Lex V2 console or API to create slot types with a custom grammar.

### [Grammar definition](https://docs.aws.amazon.com/lexv2/latest/dg/grammar-srgs-spec.html)

See the entities from the SRGS specification that Amazon Lex V2 implements for the grammar slot type.

- [Header declarations](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-header.html): See the SRGS header declarations that work with the Amazon Lex V2 grammar slot type.
- [Supported XML elements](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-supported-xml.html): See the XML elements supported by the Amazon Lex V2 grammar slot type.
- [Tokens](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-tokens.html): See the token specifications supported by the Amazon Lex V2 grammar slot type.
- [Rule reference](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-rule-reference.html): See the forms of rule references supported by the Amazon Lex V2 grammar slot type.
- [Sequences and encapsulation](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-sequence.html): See the SRGS sequences supported by the Amazon Lex V2 grammar slot type.
- [Repeats](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-repeats.html): See the repeat expansions for SRGS expressions in Amazon Lex V2.
- [Language](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-language.html): See how to use language identifiers in Amazon Lex V2 SRGS grammars.
- [Tags](https://docs.aws.amazon.com/lexv2/latest/dg/srgs-tags.html): See information about using tag for Amazon Lex V2 SRGS grammar slot types.
- [Weights](https://docs.aws.amazon.com/lexv2/latest/dg/grammar-weights.html): You can add the weight attribute to an element.

### [Script format](https://docs.aws.amazon.com/lexv2/latest/dg/grammar-ecmascript-spec.html)

See the ECMAScript features supported by the Amazon Lex V2 grammar slot type.

- [Variable statement](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-variable.html): See the variable statements supported by the grammar slot type in Amazon Lex V2.
- [Expressions](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-expression.html): You can add expressions strings to perform functions in Amazon Lex V2.
- [If statement](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-if.html): Learn how to use ECMAScript if statements in Amazon Lex V2 SRGS slot types.
- [Switch statement](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-switch.html): You can add switch statements to perform functions in Amazon Lex V2.
- [Function declarations](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-function.html): Learn how to use function declarations in an Amazon Lex V2 grammar slot type.
- [Iteration statement](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-iteration.html): Iteration statements can be any one of the following:
- [Block statement](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-block.html): See how to add statement blocks in an Amazon Lex V2 grammar slot type.
- [Comments](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-comments.html): See how to add comments to ECMAScript SRGS slots in Amazon Lex V2
- [Unsupported statements](https://docs.aws.amazon.com/lexv2/latest/dg/ecma-unsupported.html): See the unsupported ECMAScript statements for Amazon Lex V2 grammar slot types.
- [Industry grammars](https://docs.aws.amazon.com/lexv2/latest/dg/grammar-industry.html): Industry grammars are a set of XML files to use with the grammar slot type.
- [Composite slot type](https://docs.aws.amazon.com/lexv2/latest/dg/composite-slots.html): Learn how to create composite slot types for your Amazon Lex V2 intents.
- [Testing a bot](https://docs.aws.amazon.com/lexv2/latest/dg/test-bot.html): Learn how to use the Amazon Lex V2 console to test your bot.


## [Optimize Lex V2 bots with generative AI](https://docs.aws.amazon.com/lexv2/latest/dg/generative-features.html)

### [Descriptive bot builder from your description](https://docs.aws.amazon.com/lexv2/latest/dg/nld-bots.html)

Learn how to create a bot, intents, and slot values using generative AI with the descriptive bot builder.

- [Examples for descriptive bot builder](https://docs.aws.amazon.com/lexv2/latest/dg/nld-examples.html): Here are some helpful example bot descriptions you can use with descriptive bot builder in Amazon Lex V2.
- [Permissions needed for NLD](https://docs.aws.amazon.com/lexv2/latest/dg/nld-permissions.html)
- [Use utterance generation to generate sample utterances for intent recognition](https://docs.aws.amazon.com/lexv2/latest/dg/utterance-generation.html): Learn about generating sample utterances for intent recognition in Amazon Lex V2.

### [Using assisted slot resolution for slot values](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot.html)

Learn how to improve slot accuracy and resolution of customer slot values with assisted slot resolution in Amazon Lex V2.

- [Examples of assisted slot resolution](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot-examples.html): Below are some examples where assisted slot resolution is able to intelligently resolve user utterances into a value.
- [Enable in generative AI configurations](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot-genai.html): You can enable assisted slot resolution for supported built-in slots by navigating to the Generative AI screen.
- [Enable assisted slot resolution for your slot](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot-level.html): You can enable assisted slot resolution for supported built-in slots by navigating to the slot level for each intent that has slots.
- [Permissions for assisted slot resolution](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot-permissions.html)

### [Using BedrockAgentIntent to use a Bedrock Agent in Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent.html)

Learn how to use BedrockAgentIntent to use a Bedrock Agent with your bot in Amazon Lex V2.

- [Enable in generative AI configurations](https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent-genai.html): You can enable Bedrock Agent Intent by navigating to the Generative AI screen.
- [Enable Bedrock Agent Intent for your bot](https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent-level.html): You can enable Bedrock Agent Intent by adding a built-in intent to your Amazon Lex V2 bot.
- [Permissions for Bedrock Agent Intent](https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent-permissions.html)
- [Sample request](https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent-sample.html): The following example shows how to invoke the AMAZON.BedrockAgentIntent and demonstrates the session and request attributes that are populated in the response.
- [Improve intent classification and slot resolution](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-nlu.html): Learn how to improve intent classification and slot resolution using generative AI with assisted NLU.
- [Resolve ambiguous user inputs with Intent Disambiguation](https://docs.aws.amazon.com/lexv2/latest/dg/generative-intent-disambiguation.html): Learn how to use Intent Disambiguation to help resolve ambiguous user inputs when multiple intents could match.

### [AMAZON.QnAIntent](https://docs.aws.amazon.com/lexv2/latest/dg/generative-qna.html)

- [Permissions](https://docs.aws.amazon.com/lexv2/latest/dg/qna-permissions.html): To access this feature on Amazon Lex V2 console, ensure your console role has bedrock:ListFoundationModels permissions.


## [Deploying bots from Lex V2 for your production environment](https://docs.aws.amazon.com/lexv2/latest/dg/deploying.html)

- [Versioning and aliases with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/versions-aliases.html): Learn how to use versions and aliases to manage your Amazon Lex V2 bots.
- [Integrating with a Java application](https://docs.aws.amazon.com/lexv2/latest/dg/deploy-java.html): See an example application that uses the AWS SDK for Java to interact with an Amazon Lex V2 bot.

### [Use Global Resiliency to deploy bots to other Regions](https://docs.aws.amazon.com/lexv2/latest/dg/global-resiliency.html)

Deploy a replication of your bot to a secondary region.

- [Permissions](https://docs.aws.amazon.com/lexv2/latest/dg/gr-permissions.html): If an IAM role has the AmazonLexFullAccess policy attached, it can create and manage bot replicas.
- [Deploying Global Resiliency with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/navigation-gr.html): Learn how to navigate Global Resiliency in Amazon Lex V2.

### [Integrating with messaging platforms](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)

Get directions for deploying an Amazon Lex V2 bot on the messaging platform of your choice.

### [Integrating with Facebook](https://docs.aws.amazon.com/lexv2/latest/dg/deploy-facebook-messenger.html)

Get directions for deploying an Amazon Lex V2 bot on Facebook Messenger.

- [Step 1: Create a Facebook application](https://docs.aws.amazon.com/lexv2/latest/dg/facebook-step-1.html): Create a Facebook Application to integrate with an Amazon Lex V2 bot.
- [Step 2: Integrate Facebook Messenger with the Amazon Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/facebook-step-2.html): Link a Facebook Messenger application with an Amazon Lex V2 bot.
- [Step 3: Complete Facebook integration with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/facebook-step-3.html): Use the Facebook developer console to complete integration with an Amazon Lex V2 bot.
- [Step 4: Test the integration with Facebook Messenger](https://docs.aws.amazon.com/lexv2/latest/dg/facebook-step-4.html): Use Facebook Messenger to test the integration with an Amazon Lex V2 bot.

### [Integrating with Slack](https://docs.aws.amazon.com/lexv2/latest/dg/deploy-slack.html)

Get directions for deploying an Amazon Lex V2 bot on Slack.

- [Step 1: Sign up for Slack and create a Slack team](https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-1.html): Follow these instructions to create a Slack account and Slack team so that you can integrate an Amazon Lex V2 bot with the Slack messaging application.
- [Step 2: Create a Slack application](https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-2.html): Follow these instructions to create a Slack application to integrate an Amazon Lex V2 bot.
- [Step 3: Integrate the Slack application with the Amazon Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-3.html): Follow these instructions to integrate a Slack application with your Amazon Lex V2 bot using the Amazon Lex V2 console.
- [Step 4: Complete Slack integration with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-4.html): Finish integrating your Amazon Lex V2 bot with Slack using the Slack console.
- [Step 5: Test the integration between your Lex V2 bot and Slack](https://docs.aws.amazon.com/lexv2/latest/dg/slack-step-5.html): Use a browser to test the integration between Slack and your Amazon Lex V2 bot.

### [Integrating with Twilio SMS](https://docs.aws.amazon.com/lexv2/latest/dg/deploy-twilio-sms.html)

Get directions for deploying an Amazon Lex V2 bot on Twilio SMS.

- [Step 1: Create a Twilio SMS account](https://docs.aws.amazon.com/lexv2/latest/dg/twilio-step-1.html): Sign up for a Twilio SMS account to integrate your Amazon Lex V2 bot.
- [Step 2: Integrate the Twilio message service endpoint with the Amazon Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/twilio-step-2.html): Associate an Amazon Lex V2 bot with Twilio SMS.
- [Step 3: Complete Twilio integration between your Lex V2 bot and Twilio](https://docs.aws.amazon.com/lexv2/latest/dg/twilio-step-3.html): Use the Twilio console to complete integrating an Amazon Lex V2 bot with Twilio SMS.
- [Step 4: Test the integration between your Lex V2 bot and Twilio](https://docs.aws.amazon.com/lexv2/latest/dg/twilio-step-4.html): Get instructions for testing your Amazon Lex V2 bot with Twilio SMS.

### [Integrating with contact centers](https://docs.aws.amazon.com/lexv2/latest/dg/contact-center.html)

You can integrate Amazon Lex V2 bots with your contact centers to enable self-service use-cases using the Amazon Lex V2 streaming API.

- [Amazon Chime SDK](https://docs.aws.amazon.com/lexv2/latest/dg/contact-center-chime.html): Get directions for integrating an Amazon Lex V2 bot with Amazon Chime.
- [Amazon Connect](https://docs.aws.amazon.com/lexv2/latest/dg/contact-center-connect.html): Amazon Connect is an omnichannel cloud contact center.
- [Genesys Cloud](https://docs.aws.amazon.com/lexv2/latest/dg/contact-center-genesys.html): Genesys Cloud is a suite of cloud services for enterprise communication, collaboration, and contact center management.


## [Understanding Amazon Lex V2 bot conversations](https://docs.aws.amazon.com/lexv2/latest/dg/managing-conversations.html)

### [Conversation context with your Lex V2 bots](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-contexts.html)

Learn about using context to control a conversation with a bot.

- [Setting intent context for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-active-context.html): You can have Amazon Lex V2 trigger intents based on context.
- [Using default slot values in intents for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-default.html): When you use a default value, you specify a source for a slot value to be filled for new intents when no slot is provided by the userâs input.
- [Setting session attributes for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-session-attribs.html): Session attributes contain application-specific information that is passed between a bot and a client application during a session.
- [Setting request attributes for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-request-attribs.html): Request attributes contain request-specific information and apply only to the current request.
- [Setting the session timeout](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-session-timeout.html): Amazon Lex retains context informationâslot data and session attributesâuntil a conversation session ends.
- [Sharing information between intents with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-cross-intent.html): Amazon Lex V2 supports sharing information between intents.
- [Setting complex attributes in your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-complex-attributes.html): Session and request attributes are string-to-string maps of attributes and values.
- [Understanding bot sessions](https://docs.aws.amazon.com/lexv2/latest/dg/managing-sessions.html): Learn how to use the Amazon Lex V2 API to start, change, and close sessions with your bot.


## [Integrating AWS Lambda functions](https://docs.aws.amazon.com/lexv2/latest/dg/lambda.html)

- [AWS Lambda input event format for Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-input-format.html): The first step in integrating a Lambda function into your Amazon Lex V2 bot is to understand the fields in the Amazon Lex V2 event and to determine the information from these fields that you want to use when writing your script.
- [AWS Lambda response format for Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-response-format.html): The second step in integrating a Lambda function into your Amazon Lex V2 bot is to understand the fields in the Lambda function response and to determine which parameters you want to manipulate.
- [Common structures](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-common-structures.html): Within the Lambda response, there are a number of structures that recur.

### [Creating and attaching a Lambda function to a bot alias](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach.html)

To create a Lambda function for your Amazon Lex V2 bot, access AWS Lambda from your AWS Management Console and create a new function.

- [Attach an AWS Lambda function to a Amazon Lex V2 bot using the console](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-console.html): You must first attach a Lambda function to your Amazon Lex V2 bot alias before you can invoke it.
- [Attach an AWS Lambda function to a Amazon Lex V2 bot using API operations](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-api.html): You must first attach a Lambda function to your Amazon Lex V2 bot alias before you can invoke it.
- [Debugging a Lambda function](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-debug.html): Amazon CloudWatch Logs is a tool for tracking API calls and metrics that you can use to help debug your Lambda functions.


## [Customizing bot interactions with users in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/customizing-bot-interactions.html)

- [Analyzing the sentiment of users in the conversation](https://docs.aws.amazon.com/lexv2/latest/dg/sentiment.html): Learn how to use Amazon Comprehend sentiment analysis to understand your user's utterances.

### [Using confidence scores to improve conversation accuracy](https://docs.aws.amazon.com/lexv2/latest/dg/confidence-scores.html)

Learn what automatic speech recognition and natural language understanding confidence scores are and how to use them with your Amazon Lex V2 bot.

- [Using intent confidence scores to improve intent selection with Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html): Learn what natural language understanding confidence scores are and how to use them with your Amazon Lex V2 bot.
- [Using voice transcription confidence scores to improve conversations with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/using-transcript-confidence-scores.html): Learn what automatic speech recognition confidence scores are and how to use them with your Amazon Lex V2 bot.

### [Customizing speech transcriptions for use with your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/customizing-speech-transcriptions.html)

Learn about features to customize your Amazon Lex V2 bot's speech transcription efforts.

### [Configuring speech recognition model preferences](https://docs.aws.amazon.com/lexv2/latest/dg/customizing-speech-model-preferences.html)

Configure speech recognition model preferences to optimize accuracy and performance for your Amazon Lex V2 bot.

- [Setting up Deepgram speech model preference](https://docs.aws.amazon.com/lexv2/latest/dg/customizing-speech-deepgram-setup.html): Learn how to configure Deepgram as your speech recognition model for Amazon Lex V2 bots.
- [Improving speech recognition with a custom vocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html): Learn how to create a custom vocabulary to improve the speech recognition accuracy of slot transcriptions by your bot.
- [Configuring voice activity detection sensitivity](https://docs.aws.amazon.com/lexv2/latest/dg/customizing-speech-vad-sensitivity.html): Learn how to configure voice activity detection (VAD) sensitivity to optimize speech recognition in noisy environments.
- [Improving recognition of slot values with runtime hints in the conversation](https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html): Learn how to use runtime hints to help your bot recognize user utterances.
- [Capturing slot values with spelling styles during the conversation](https://docs.aws.amazon.com/lexv2/latest/dg/spelling-styles.html): Learn how to use spelling styles to enter slot values for Amazon Lex V2.


## [Monitoring bot performance in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-bot-performance.html)

### [Measuring business performance with Analytics](https://docs.aws.amazon.com/lexv2/latest/dg/analytics.html)

Evaluate your bot's performance through analyzing conversations, utterances, intents, and slots in your bot and identify problem areas where you can improve your bot.

- [Key definitions](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-key-definitions.html): Learn the terminology used for analytics in Amazon Lex V2.
- [Filtering results](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-filter.html): Learn how to filter analytics results in Amazon Lex V2.
- [Overview](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-overview.html): Learn about the overview page for analytics.
- [Conversation dashboard](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-dashboard.html): The conversation dashboard visualizes metrics for customersâ conversations (see for the definition of a conversation) with your bot.
- [Performance dashboard](https://docs.aws.amazon.com/lexv2/latest/dg/performance-dashboard.html): In the performance dashboard, you can view details about the performance of your bot's intent fulfillment and utterance recognition.
- [Using APIs for analytics](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-api.html): This section describes the API operations that you use to retrieve analytics for a bot.
- [Managing access permissions for analytics](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-permissions.html): Learn how to manage permissions for analytics in Amazon Lex V2.

### [Enabling conversation logs for your Lex V2 bots](https://docs.aws.amazon.com/lexv2/latest/dg/enabling-logs.html)

Learn how to enable logging of conversations between users and your Amazon Lex V2 bot and how to protect users' privacy.

### [Logging conversations with conversation logs in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs.html)

Learn how to log user conversations with your Amazon Lex V2 bot.

- [IAM Policies for Conversation Logs](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-policies.html): Depending on the type of logging that you select, Amazon Lex V2 requires permission to use Amazon CloudWatch Logs and Amazon Simple Storage Service (S3) buckets to store your logs.
- [Configuring conversation logs for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-configure.html): Learn how to configure Amazon Lex V2 to log audio and text conversations.
- [Viewing text logs in Amazon CloudWatch Logs from Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-cw.html): Learn how to view text conversation logs using the Amazon Lex V2 console.
- [Accessing audio logs in Amazon S3](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-s3.html): Learn how to find the audio logs of an Amazon Lex V2 conversation.
- [Monitoring conversation log status with CloudWatch metrics](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-monitoring.html): Use Amazon CloudWatch metrics to monitor the health of your audio and text logs.
- [Obscuring slot values in conversation logs from Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-obfuscate.html): Learn how to obscure slot values in logs.

### [Selective conversation log capture in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-selective-logging.html)

Learn how to use selective conversation log capture to capture audio and/or text in conversation logs when using an Amazon Lex V2 bot.

- [Manage selective conversation log capture](https://docs.aws.amazon.com/lexv2/latest/dg/manage-selective-logging.html): Learn how to manage selective conversation log capture to capture audio and/or text in conversation logs.
- [Example of selective conversation log capture](https://docs.aws.amazon.com/lexv2/latest/dg/example-selective-logging.html): Review an example of selective conversation log capture to capture audio and/or text in conversation logs.
- [Logging errors with error logs in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/error-logs.html): Learn how to error logs with your Amazon Lex V2 bot.

### [Monitoring operational metrics in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-operational-metrics.html)

Monitor operational metrics with Amazon CloudWatch and AWS CloudTrail.

- [Measuring operational metrics with CloudWatch for Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-cloudwatch.html): You can monitor Amazon Lex V2 using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Viewing events with CloudTrail](https://docs.aws.amazon.com/lexv2/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon Lex V2 with AWS CloudTrail.

### [Evaluating Lex V2 bot performance with the Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/test-workbench.html)

Optimize your bot performance with the Test Workbench.

### [Generate a test set for Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/test-sets.html)

Learn how to create a test set in Amazon Lex V2 when using test workbench.

- [Tips for creating a successful test set](https://docs.aws.amazon.com/lexv2/latest/dg/tips-create-test-set.html): How create a successful test set in Amazon Lex V2
- [Creating a test case within a test set using Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/create-test-case.html): How create a test case within a test set using test workbench in Amazon Lex V2
- [Creating a test set from a CSV file for Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/create-test-set-from-CSV.html): How create a successful test set from a CSV file using test workbench in Amazon Lex V2
- [Create an IAM role for the Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/create-iam-test-set.html): How create an IAM role for the Test Workbench in Amazon Lex V2
- [Create an IAM role for the Test Workbench - Advanced Features](https://docs.aws.amazon.com/lexv2/latest/dg/create-iam-test-set-features.html): How create an IAM role for the Test Workbench in Amazon Lex V2 for audio and Lex Runtime

### [Manage test sets](https://docs.aws.amazon.com/lexv2/latest/dg/manage-test-sets.html)

Learn how to manage a test set in Amazon Lex V2.

- [Test set columns supported by Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/file-input-test-sets.html): Learn how to view test set columns supported by Test Workbench in Amazon Lex V2.
- [View test validation errors in test workbench](https://docs.aws.amazon.com/lexv2/latest/dg/view-errors-test-sets.html): Learn how to view validation errors in a test set in Amazon Lex V2.
- [Delete a test set in Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/delete-test-sets.html): Learn how to delete a test set from test workbench in Amazon Lex V2.
- [Edit test set details](https://docs.aws.amazon.com/lexv2/latest/dg/edit-details-test-sets.html): Learn how to edit the details for a test set in Amazon Lex V2.
- [Update test set](https://docs.aws.amazon.com/lexv2/latest/dg/update-test-sets.html): Learn how to update your test set in Amazon Lex V2.
- [Execute a test](https://docs.aws.amazon.com/lexv2/latest/dg/execute-test-set.html): Learn how to execute a test in Amazon Lex V2.
- [Test set coverage in Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/validation-test-set.html): Learn how to review test validation results in Amazon Lex V2.
- [View test results](https://docs.aws.amazon.com/lexv2/latest/dg/test-results-test-set.html): Learn how to interpret test results from the Test Workbench in Amazon Lex V2.
- [Test results details in Test Workbench](https://docs.aws.amazon.com/lexv2/latest/dg/test-results-details-test-set.html): Learn how to interpret test results details from the Test Workbench in Amazon Lex V2.


## [Streaming conversations to your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/streaming.html)

### [Starting a conversation stream to an Amazon Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/start-stream-conversation.html)

Learn how to stream between your bot and your application and how to automatically handle user responses.

- [Starting a streaming conversation](https://docs.aws.amazon.com/lexv2/latest/dg/using-streaming-api.html): Use the following code examples to help you start a stream between an Amazon Lex V2 bot and your application.
- [Event stream encoding](https://docs.aws.amazon.com/lexv2/latest/dg/event-stream-encoding.html): Event stream encoding provides bidirectional communication using messages between a client and a server.
- [Enabling your bot to be interrupted](https://docs.aws.amazon.com/lexv2/latest/dg/interrupt-bot.html): Enable the Amazon Lex V2 bot to handle users who interrupt the bot before it can finish sending a prompt in an audio stream.
- [Waiting for the user to provide additional information](https://docs.aws.amazon.com/lexv2/latest/dg/wait-and-continue.html): Enable the Amazon Lex V2 bot to wait for the user to provide additional information in a bidirectional stream.
- [Configuring fulfillment progress updates for your Lex V2 bot](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html): When the fulfillment Lambda function for an intent is called, the bot doesn't send a response until the function completes.
- [Timeouts for user input](https://docs.aws.amazon.com/lexv2/latest/dg/session-attribs-speech.html): The Amazon Lex V2 streaming API enables a bot to automatically detect utterances in user input.


## [Importing and exporting bots in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html)

### [Exporting bots from Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/export.html)

You export a bot, bot locale, or custom vocabulary using the console or the CreatExport operation.

- [Exporting a Lex V2 bot (console)](https://docs.aws.amazon.com/lexv2/latest/dg/export-console.html): Learn how to use the Amazon Lex V2 console to export an Amazon Lex V2 bot or bot locale.

### [Importing bots in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/import.html)

To use the console to import a previously exported bot, bot locale or custom vocabulary, you provide the file location on your local computer and the optional password to unlock the file.

- [Importing a Lex V2 bot (console)](https://docs.aws.amazon.com/lexv2/latest/dg/import-console.html): Learn how to use the Amazon Lex V2 console to import an Amazon Lex V2 bot or bot locale.
- [Using a password when importing or exporting](https://docs.aws.amazon.com/lexv2/latest/dg/import-export-password.html): Amazon Lex V2 can password protect your export archives or read your protected import archives using standard .zip file compression.
- [JSON format for importing and exporting bots in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/import-export-format.html): See the JSON file format and directory structure that Amazon Lex V2 uses to import and export bots and bot locales.


## [Tagging resources in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/tagging.html)

- [Tagging resources (console)](https://docs.aws.amazon.com/lexv2/latest/dg/tags-console.html): You can use the console to manage tags on a bot or bot alias.


## [Security](https://docs.aws.amazon.com/lexv2/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/lexv2/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Lex V2.

- [Encryption at rest](https://docs.aws.amazon.com/lexv2/latest/dg/encryption-at-rest.html): Amazon Lex V2 encrypts user utterances and other information that it stores.
- [Encryption in transit](https://docs.aws.amazon.com/lexv2/latest/dg/encryption-in-transit.html): Amazon Lex V2 uses the HTTPS protocol to communicate with your client application.

### [Identity and access management](https://docs.aws.amazon.com/lexv2/latest/dg/security-iam.html)

How to authenticate requests and manage access your Amazon Lex V2 resources.

- [How Amazon Lex V2 works with IAM](https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Lex V2, learn what IAM features are available to use with Amazon Lex V2.
- [Identity-based policy examples](https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Lex V2 resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_resource-based-policy-examples.html): A resource-based policy is attached to a resource, such as a bot or a bot alias.
- [AWS managed policies](https://docs.aws.amazon.com/lexv2/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Lex V2 and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/lexv2/latest/dg/using-service-linked-roles.html): How to use service-linked roles to give Amazon Lex V2 access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Lex V2 and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/lexv2/latest/dg/security-logging-and-monitoring.html): Learn how to use logging and monitoring with Amazon Lex V2 to monitor activity by the service.
- [Compliance validation](https://docs.aws.amazon.com/lexv2/latest/dg/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/lexv2/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Lex V2 features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/lexv2/latest/dg/infrastructure-security.html): Learn how Amazon Lex V2 isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/lexv2/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Lex V2 without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [Code examples](https://docs.aws.amazon.com/lexv2/latest/dg/service_code_examples.html)

### [Scenarios](https://docs.aws.amazon.com/lexv2/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Lex with AWS SDKs.

- [Building an Amazon Lex chatbot](https://docs.aws.amazon.com/lexv2/latest/dg/example_cross_LexChatbotLanguages_section.html): Create an Amazon Lex chatbot to engage your website visitors
