Source: https://docs.slack.dev/legacy/legacy-bot-users

# Legacy bot users

Slack apps act independently of a user token. Build a bot user powered by only the specific permissions it needs. [Check out Slack apps now](/app-management/quickstart-app-settings).

## What are bots? {#bots-overview}

A bot is a type of app designed to interact with users via conversation. You can enable conversations between users and apps in Slack by building these bots.

Beginning **March 31, 2025**, we will discontinue support for legacy custom bots.

For your integrations to continue working, you must create brand new Slack apps. Refer to [this changelog article](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation) for more details.

![A conversation between @celeste and @officebot](data:image/png;base64,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)

A bot is the same as a regular app: it can access the same range of APIs and do all of the magical things that a Slack App can do. But when you build a bot for your app, you're giving that app a face, a name, and a personality, and encouraging users to _talk_ to it.

Your bot can send DMs, be mentioned by users, post messages or upload files, and be invited to channels - or kicked out.

* * *

## Creating a bot user {#creating}

Since your bot is capable of doing everything that an app can do, we're going to limit our focus to a common use case for bots. The following steps will get you to the point where you have a bot waiting for messages and sending responses. From there, you can begin adding any kind of app logic you can imagine.

Before you start, you'll need an app. If you don't already have one, click the following button to create it:

[Create an app](https://api.slack.com/apps?new_app=1)

To use your app as a bot, first you'll need to create a [bot user](/legacy/legacy-custom-integrations/legacy-custom-integrations-bot-users) for it.

Head to your [app's settings page](https://api.slack.com/apps) and click the _Bot Users_ feature in the navigation menu. You'll be presented with a button marked _Add a Bot User_, and when you click on it, you'll see a screen where you can configure your app's bot user with the following information:

* **Display name**: the name displayed to other users when the bot posts messages, the bot's profile is viewed, etc.
* **Default username**: the string used when the bot is mentioned in a message. This username may be modified slightly from the default when it is installed to a workspace where that username is already reserved. This modification is an incrementing number appended to the username — so @username might become @username2.
* **Always Show My Bot as Online**: we recommend you enable this feature so that your bot always appears to be ready to receive input (which it probably will be). When disabled, you'll have to programmatically [set its online presence](/apis/web-api/user-presence-and-status#bot_presence).

Once you've completed these fields, click _Add Bot User_ and then _Save Changes_.

Great, you've just created a bouncing baby bot! Don't leave the app settings yet though, there's still a bit of configuration left to do.

### Configuring the Events API {#setup-events-api}

The [Events API](#app-mentions-response) is a bot's eyes and ears. It gives the bot a way to react to posted messages, changes to channels, and other activities that happen in Slack. When these events happen, a data payload will be sent to your bot, and it can use that data to form a useful response.

Give your bot access to the Events API as follows:

1. From your app's settings, click the _Event Subscriptions_ feature in the navigation menu.
2. Switch the _Enable Events_ toggle to on and you'll be presented with a new screen of options.
3. You'll need to [configure the _Request URL_](/apis/events-api/#events_api_request_urls) that the data payloads will be pushed to. This URL needs to be verified first, [as outlined in the Events API docs](/apis/events-api/#request_url_configuration__amp__verification).
4. Then you'll add some individual event subscriptions. For our bot, we're interested in the Bot Events, so click on the _Add Bot User Event_ button.
5. There are lots of different [event types](/reference/events) you could add, but for the purposes of our tutorial let's add two event subscriptions - [`app_mention`](/reference/events/app_mention) which sends events when someone [mentions your bot](https://slack.com/help/articles/205240127-Mention-a-member), and [`message.channels`](/reference/events/message.channels) which sends events when a new message is posted in a public channel.
6. Click _Save Changes_.

Good news! Your bot is looking more and more life-like, and now it's ready to find a home.

### Installing the bot to a workspace {#installing-bot}

A bot user is added to a workspace by installing the app the bot is associated with. Once done, you'll get a [bot token](/authentication/tokens#bot) that is imbued with the [`bot`](/reference/scopes/bot) scope. This token can be used with a [subset of Web API methods](#methods) that we'll discuss later.

If you had already installed your app in the past, you'll need to reinstall to grant the additional [`bot`](/reference/scopes/bot) scope. The process is the same either way:

1. On your [app's settings page](https://api.slack.com/apps), click the _Install App_ settings item in the navigation menu.
2. Click _Install App to your Workspace_. If you had already installed your app, the button to click will instead be called _Reinstall App_.
3. On the permissions authorization page, click _Authorize_.

Your app is now installed to that workspace, but you still need to invite it into individual channels. You should also [invite the bot](https://slack.com/help/articles/201980108-Invite-members-to-a-channel) to a public channel somewhere in your workspace.

Once installed, you'll have generated a [bot token](/authentication/tokens#bot) that you should store for use later on — you can find it in your app's settings under _Install App_ > _Bot User OAuth Access Token_.

Bot tokens can also be generated using the [OAuth install flow](/legacy/legacy-authentication/#bots) if you are distributing your app beyond your own workspace.

Your bot should now be happily residing in the channel picked during the install process. It will be listening for users posting in that channel, and for posted messages that mention it. Now you need to tell it what to do when it hears something.

### Handling events {#handling-events}

Previously, we configured the event subscriptions for your app — but now we have to actually do something with the data that will be sent with each event.

Let's imagine a conversational bot that responds to being mentioned by sending a couple of follow-up messages:

![Example conversation between a user and a bot with the user asking the bot to tell a joke](/assets/images/bot_flow-9edb38f9d46ff1057c9472ec067deb0f.png)

There are four events triggered in this conversation: the first is an `app_mention` event from the first message that mentions the bot; the next three are `message` events for each of the messages posted by Johnny. Our bot will need to be able to interpret each event and respond accordingly.

We've avoided showing you any specific code up until now, but in the following steps we're going to explain the process and then show simplified Express/Node.js examples of what your app logic should look like. These examples translate readily into most modern programming languages.

#### Receiving events {#receiving_events}

The first thing we need to do is create some app code that will correctly receive the events.

Each event will trigger a request containing a JSON payload sent to your configured _Request URL_. The [Events API docs](/apis/events-api/#receiving_events) contain a full description of the shape of this JSON, and the reference for [`app_mention`](/reference/events/app_mention) and the [`message.channels`](/reference/events/message.channels) contain any details specific to each event type.

Your app has to be able to receive and parse this JSON, then send an [immediate confirmation response](/apis/events-api/#responding_to_events) to each event request as described [in the Events API docs](/apis/events-api/#responding_to_events).

Here's how we might build our code for receiving events:

```text
// Receive event payload to Request URL via HTTP POSTrouter.post("/", function(req, res, next) {    // Get event payload    let payload = req.body;    // Respond to this event with HTTP 200 status    res.sendStatus(200);}
```text

Now that you've written code to handle an event, you can think about how to respond in a "bot-like" way.

#### Responding to mentions using the Web API {#responding-to-mentions}

For a bot, [being mentioned](https://slack.com/help/articles/205240127-Mention-a-member) is usually the triggering event for a conversation, just as a human will respond when they hear their name. Your app code should use the [`type` field inside the event payload](/apis/events-api/#receiving_events) to spot these [`app_mention`](/reference/events/app_mention) events, and to differentiate them from any other events it might receive.

In addition, you don't want to respond to every mention, only the ones that are actually intended to trigger the "tell a joke" flow. To do that, use the `text` field from the event payload, which contains the text of the message that the mention was contained in. When `text` mentions the bot _and_ includes the words "tell me a joke", the bot will respond; otherwise it'll just stay quiet.

Here's what the example code might look like with this kind of logic:

```text
router.post("/", function(req, res, next) {    let payload = req.body;    res.sendStatus(200);    if (payload.event.type === "app_mention") {        if (payload.event.text.includes("tell me a joke")) {            // Make call to chat.postMessage using bot's token        }    }}
```text

With the call to `chat.postMessage`, the first line of the joke is sent:

```text
Knock, knock.
```text

To send this, your app should use the [`chat.postMessage`](/reference/methods/chat.postMessage) method with the [token you stored earlier](#installing-bot). Here's an example request:

```text
POST https://slack.com/api/chat.postMessageContent-type: application/jsonAuthorization: Bearer YOUR_BOTS_TOKEN{    "text": "Hello <@UA8RXUPSP>! Knock, knock.",    "channel": "C123ABC456"}
```text

You can read the [API method reference](/reference/methods/chat.postMessage) for more info on building this request. You can also use the [special formatting](/messaging/formatting-message-text), [attachments](/messaging/formatting-message-text#attachments), and [interactive components](/messaging/creating-interactive-messages) available for messages.

So, your bot has uttered those first magical words, and you can assume that the user will reply with the standard "Who's there?" response. Let's find out how to keep the joke going.

#### Responding to other messages {#responding-to-events}

As [we said before](#handling-events), the flow we're describing contains an `app_mention` event followed by three `message` events. In order to identify the differences between those three messages, the app logic becomes a bit more complex.

The first thing you need to do is use the [`type` field inside the event payload](/apis/events-api/#receiving_events) to look for these [`message`](/reference/events/message.channels) events.

Next, use the `text` of the message in the event payload to decide which kind of response your bot should make. Again, let's assume the pattern of "knock, knock" jokes — the first user response is always "Who's there?", and the second user response is always "\_\_\_\_ who?". So, you can check for messages that include these words, and use the right response for each. If you see any messages that don't include either of these phrases, ignore them.

Adding to the code from previous steps, you'll have something like this:

```text
router.post("/", function(req, res, next) {    let payload = req.body;    res.sendStatus(200);    if (payload.event.type === "app_mention") {        if (payload.event.text.includes("tell me a joke")) {            // Make call to chat.postMessage using bot's token        }    }    if (payload.event.type === "message") {        let response_text;        if (payload.event.text.includes("Who's there?")) {            response_text = "A bot user";        }        if (payload.event.text.includes("Bot user who?")) {            response_text = "No, I'm a bot user. I don't understand jokes.";        }        if (response_text !== undefined) {            // Make call to chat.postMessage sending response_text using bot's token        }    }}
```text

Congratulations, your first bot is now chatting! You should now be able to go to the channel you installed the bot into and strike up this conversation with it. Remember to laugh politely when it tells you the punchline.

Your next steps should involve [adding more complexity](#more-complex-bots) to your bot to make it useful.

* * *

## Making more complex bots {#more-complex-bots}

In the steps above, we made a lot of assumptions for simplicity. For example, we expected that users would respond with a very specific spelling, we assumed a test environment where there were no other conversations happening, and so on.

For a real bot in production, some of these assumptions would break the behavior of the bot. So, let's cover some situations that you should address for your own bots — think of these as best practices rather than specific instructions to follow.

### Tracking conversations {#tracking-conversations}

In our example, we've used a mention as the triggering point for a specific conversation, but you'll notice that your bot will still respond if you skip some of the steps. For example, if you type `Who's there?`, your bot will respond to this message with `A bot user`, even if you didn't mention the bot or start at the beginning of the conversation.

A solution to this might involve tracking the beginning of a conversation, the participants involved, and the progress through the flow. For example, when the user first mentions the bot, a database entry is created that identifies that user and the open workflow with them.

As the user progresses through the flow, the database records this, and the user is unable to repeat earlier steps in the conversation (unless that is a desired behavior). Once the workflow is completed, the database entry is also marked as complete, and the bot waits for another mention before starting anew.

### Threaded messages {#threaded-messages}

Be aware that a user might choose to reply to your bot's [messages in a thread](/messaging#threading) rather than at the channel-level. Your bot will still receive `message` events for these threaded replies, but you will have to add some extra logic to ensure that your bot responds to the user in the relevant location.

Check out [threading messages](/messaging#threading) for more information on how to spot the difference between messages and threaded messages.

### Variations in phrasing {#variations-in-phrasing}

Because your bot will be interacting with humans, it's unlikely that you can expect consistent spelling and phrasing across messages from different people that might be trying to invoke the same thing. For example, our example bot used the phrase `tell me a joke` to trigger the start of the workflow, but at a very basic level, a user might also try typing `what's a good joke?` or `make me laugh`.

Your bot can get more complex by broadening the bot's understanding of natural language queries to capture a wider range of potential trigger phrases. Alternatively, you can be more prescriptive about the exact phrasing to use, and provide user education to train correct usage.

### Integrating with other services {#bot-integration}

The real magic of a bot comes when it is connected with external services, providing a seamless conversational interface for them from within Slack. There's a huge range of possibilities for what your bot could do!

* * *

## Limitations {#limitations}

Like other APIs and integrations, bot users are free. Unlike regular users, the actions they can perform are somewhat limited. For workspaces on the Free plan, each bot user counts as a separate integration.

### API methods for legacy bots {#legacy-methods}

Legacy bot users, and legacy bot tokens, can be used with a restricted set of Web API methods. These methods are shown below.

Web API method

Description

[`api.test`](/reference/methods/api.test)

Checks API calling code.

[`auth.test`](/reference/methods/auth.test)

Checks authentication & identity.

[`bots.info`](/reference/methods/bots.info)

Gets information about a bot user.

[`calls.add`](/reference/methods/calls.add)

Registers a new Call.

[`calls.end`](/reference/methods/calls.end)

Ends a Call.

[`calls.info`](/reference/methods/calls.info)

Returns information about a Call.

[`calls.participants.add`](/reference/methods/calls.participants.add)

Registers new participants added to a Call.

[`calls.participants.remove`](/reference/methods/calls.participants.remove)

Registers participants removed from a Call.

[`calls.update`](/reference/methods/calls.update)

Updates information about a Call.
