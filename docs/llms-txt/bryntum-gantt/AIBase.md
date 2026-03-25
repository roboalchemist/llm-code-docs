# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/AIBase.md

# [AIBase](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase)

Base class for AI chat feature. Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[promptUrl](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-promptUrl)
The URL to send text prompts to

[textToSpeechUrl](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-textToSpeechUrl)
The URL to send text for speech synthesizing

[transcribeUrl](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-transcribeUrl)
The URL to send audio for transcribing

[feedbackUrl](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-feedbackUrl)
The URL to send feedback (thumbs up/thumbs down) to

[model](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-model)
AI model name (if applicable)

[apiPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-apiPlugin)
AI plugin to use. Provide the class here. Available plugins are:

* `OpenAIPlugin` - use OpenAI API
* `AnthropicPlugin` - use Anthropic API
* `GooglePlugin` - use Google API

You can also provide a custom plugin by extending the `AbstractApiPlugin` class.

[availableApis](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-availableApis)
Shows an AI model selector in the SettingsPanel where the user can select between the available API:s

[temperature](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-temperature)
Temperature setting (if applicable). Overrides the default temperature set by the apiPlugin.

[max_tokens](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-max_tokens)
Max tokens setting (if applicable)

[chatButton](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-chatButton)
Set this to `true` or a config object to add a [ChatButton](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatButton)

[delayStatusTexts](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-delayStatusTexts)
An array of strings which will be circulated as waiting status texts when awaiting long AI responses Defaults to `['Waiting', 'Waiting ...', 'Still waiting', 'Still waiting ...']`

[voiceActivation](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-voiceActivation)
Configuration settings for voice activation

[voiceOnly](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-voiceOnly)
Forces voice only mode, which hides the chat panel and only shows a record chat button.

[manageChatHistory](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-manageChatHistory)
Set to `false` to not manage chat history on the client

[tools](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-tools)
Use this to add custom tools to the AI model's tool list or to remove existing tools. Provide an object with the tool names as keys and configuration objects as values. Please note that modifying existing tools is not supported, only removing them.

Available tools (for AIBase) are:

* `changeTheme` - Switches between dark and light themes
* `undo` - Undoes the last action performed by the AI
* `endVoiceConversation` - Ends the current voice conversation

More tools are available for the specific product AI features

[models](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-models)
Use this to provide more details of data models currently available for the AI agent to work with. Provide an object with model class names as keys and configuration objects as values.

A setup in a Bryntum Grid application which uses the class Project for its rows and also have a related class Member could look like this:

```
{
    Member  : { store : memberStore },
    Project : {
        relations : {
            members : {
                relatedModelName : 'Member'
            },
            owner : {
                relatedModelName : 'Member'
            }
        }
    }
}
```

[fetchOptions](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-fetchOptions)
Additional options to pass to fetch requests

[undo](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-undo)
Enables support for undoing data modifying actions performed by the AI. Shows an undo icon under the last undoable message in the ChatPanel.

[redo](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-redo)
Enables support for redoing data modifying actions performed by the AI. Shows a redo icon under the last redoable message in the ChatPanel. Requires undo to be enabled.

[showNoConnectionIcon](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-showNoConnectionIcon)
Set to `true` to upon creation, send a test prompt to verify the connection to the AI backend. If the test fails, a warning icon will be shown on the chat panel.

[debugMode](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-debugMode)
Set to `true` to automatically console.log things that happen internally. AI responses and audio processing for example.

[requireConfirmationOnUpdates](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-requireConfirmationOnUpdates)
Set to `true` to always prompt the user for confirmation before allowing the AI to update records

[requireConfirmationOnRemovals](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-requireConfirmationOnRemovals)
Set to `true` to always prompt the user for confirmation before allowing the AI to remove records

[requireConfirmationOnAdds](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-requireConfirmationOnAdds)
Set to `true` to always prompt the user for confirmation before allowing the AI to add records

[timeout](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-timeout)
A number of milliseconds a prompt is allowed to take before being aborted. Defaults to `60000` (1 minute).

[userSettings](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-userSettings)
A configuration object containing the user's preferred AI feature settings. If there is a matching AI feature class config, the user setting will take precedence JSON.

[highlightRelatedItems](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-highlightRelatedItems)
By default, data item which are targeted in an AI action will be highlighted in the UI. Set this to `false` to prevent this behavior.

[verbosityLevel](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-verbosityLevel)
Experimental configuration of the AI verbosity. Valid values are `"1"`, `"2"` and `"3"`, where `"1"` is lowest.

[trainingData](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#config-trainingData)
Use this to provide example prompt scenarios to "teach" the AI of more complex tasks. Must be configured as an array containing arrays which contains the AI messages for the complete conversation.

Please be advised that the content here will be provided in each request sent to the AI API and will therefore consume tokens and take up space in the context window.

Adding an example to the "training data" will often solve one particular case, but may "confuse" the AI in ways not expected.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAIBase](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#property-isAIBase)
Identifies an object as an instance of [AIBase](https://bryntum.com/docs/gantt/api/#Core/feature/ai/AIBase) class, or subclass thereof.

[isAIBase](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#property-isAIBase-static)
Identifies an object as an instance of [AIBase](https://bryntum.com/docs/gantt/api/#Core/feature/ai/AIBase) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[addAsyncMessage](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#function-addAsyncMessage)
Creates a Promissory and adds its promise to the chatPanel as an async message. Returns a new promptContext object

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[userSettingsUpdate](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#event-userSettingsUpdate)
Fired when the user changes it's settings via the settings panel

## Typedefs

Typedefs are type definitions for the class

[AIModelConfiguration](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIModelConfiguration)
Configuration object used in the AI feature `models` config

[AIRelatedModelConfiguration](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIRelatedModelConfiguration)
Configuration object used in the AIModelConfiguration

[AIVoiceActivationConfig](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIVoiceActivationConfig)
Configuration object used in the AI feature's `voiceActivation` config

[AIModelSelector](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIModelSelector)
Configuration object for the AI feature's `availableApis` config. All properties are required.

[AIToolProperty](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIToolProperty)
A tool parameters schema object

[AIToolConfig](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIBase#typedef-AIToolConfig)
Tool configuration object
