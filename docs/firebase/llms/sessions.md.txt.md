# Source: https://firebase.google.com/docs/ai-logic/live-api/sessions.md.txt

<br />

The Gemini Live API processes continuous streams of audio or text called
***sessions***. You can manage the session lifecycle, from the initial handshake
to graceful termination.

## Limits for sessions

For the Live API, a *session* refers to a persistent connection where input
and output are streamed continuously over the same connection.

If the session exceeds ***any*** of the following limits, the connection is
terminated.

- **Connection length** is limited to around 10 minutes.

- **Session length** depends on the input modalities:

  - Audio-only input sessions are limited to 15 minutes.
  - Video + audio input are limited to 2 minutes.
- **Session context window** is limited to 128k tokens.

You'll receive a
[*going away* notification](https://firebase.google.com/docs/ai-logic/live-api/sessions#going-away-notification)
before the connection ends, allowing you to take further actions.

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support the following configurations for session management: resuming a session across multiple connections, extending the session length, or compressing the context window.

## Start a session

Visit the
[getting started guide for the Live API](https://firebase.google.com/docs/ai-logic/live-api#audio-in-audio-out)
for a full snippet showing how to start a session.

## Update mid-session

The Live API models support the following advanced capabilities for
***mid-session updates***:

- [Add incremental content updates](https://firebase.google.com/docs/ai-logic/live-api/sessions#add-incremental-content-updates)

- [Update system instructions](https://firebase.google.com/docs/ai-logic/live-api/sessions#update-system-instructions-mid-session)
  *(for Vertex AI Gemini API only)*

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support affective dialogue or proactive audio when using the Live API. Check back soon!

### Add incremental content updates

You can add incremental updates during an active session. Use this to
send text input, establish session context, or restore session context.

- For longer contexts, we recommend providing a single message summary to free
  up the context window for subsequent interactions.

- For short contexts, you can send turn-by-turn interactions to represent the
  exact sequence of events, like the snippet below.

### Swift

    // Define initial turns (history/context).
    let turns: [ModelContent] = [
      ModelContent(role: "user", parts: [TextPart("What is the capital of France?")]),
      ModelContent(role: "model", parts: [TextPart("Paris")]),
    ]

    // Send history, keeping the conversational turn OPEN (false).
    await session.sendContent(turns, turnComplete: false)

    // Define the new user query.
    let newTurn: [ModelContent] = [
      ModelContent(role: "user", parts: [TextPart("What is the capital of Germany?")]),
    ]

    // Send the final query, CLOSING the turn (true) to trigger the model response.
    await session.sendContent(newTurn, turnComplete: true)

### Kotlin

    Not yet supported for Android apps - check back soon!

### Java

    Not yet supported for Android apps - check back soon!

### Web

    const turns = [{ text: "Hello from the user!" }];

    await session.send(
      turns,
      false // turnComplete: false
    );

    console.log("Sent history. Waiting for next input...");

    // Define the new user query.
    const newTurn [{ text: "And what is the capital of Germany?" }];

    // Send the final query, CLOSING the turn (true) to trigger the model response.
    await session.send(
        newTurn,
        true // turnComplete: true
    );
    console.log("Sent final query. Model response expected now.");

### Dart

    // Define initial turns (history/context).
    final List turns = [
      Content(
        "user",
        [Part.text("What is the capital of France?")],
      ),
      Content(
        "model",
        [Part.text("Paris")],
      ),
    ];

    // Send history, keeping the conversational turn OPEN (false).
    await session.send(
      input: turns,
      turnComplete: false,
    );

    // Define the new user query.
    final List newTurn = [
      Content(
        "user",
        [Part.text("What is the capital of Germany?")],
      ),
    ];

    // Send the final query, CLOSING the turn (true) to trigger the model response.
    await session.send(
      input: newTurn,
      turnComplete: true,
    );

### Unity

    // Define initial turns (history/context).
    List turns = new List {
        new ModelContent("user", new ModelContent.TextPart("What is the capital of France?") ),
        new ModelContent("model", new ModelContent.TextPart("Paris") ),
    };

    // Send history, keeping the conversational turn OPEN (false).
    foreach (ModelContent turn in turns)
    {
        await session.SendAsync(
            content: turn,
            turnComplete: false
        );
    }

    // Define the new user query.
    ModelContent newTurn = ModelContent.Text("What is the capital of Germany?");

    // Send the final query, CLOSING the turn (true) to trigger the model response.
    await session.SendAsync(
        content: newTurn,
        turnComplete: true
    );

### Update system instructions mid-session


|---|
| *Only available when using the Vertex AI Gemini API as your API provider.* |

<br />

You can update the system instructions during an active session. Use this to
adapt the model's responses, for example to change the response language or
modify the tone.

To update the system instructions mid-session, you can send text content with
the `system` role. The updated system instructions will remain in effect for the
remainder of the session.

### Swift

    await session.sendContent(
      [ModelContent(
        role: "system",
        parts: [TextPart("new system instruction")]
      )],
      turnComplete: false
    )

### Kotlin

    Not yet supported for Android apps - check back soon!

### Java

    Not yet supported for Android apps - check back soon!

### Web

    Not yet supported for Web apps - check back soon!

### Dart

    try {
      await _session.send(
        input: Content(
          'system',
          [Part.text('new system instruction')],
        ),
        turnComplete: false,
      );
    } catch (e) {
      print('Failed to update system instructions: $e');
    }

### Unity

    try
    {
        await session.SendAsync(
            content: new ModelContent(
                "system",
                new ModelContent.TextPart("new system instruction")
            ),
            turnComplete: false
        );
    }
    catch (Exception e)
    {
        Debug.LogError($"Failed to update system instructions: {e.Message}");
    }

## Detect when a session is going to end

A *going away* notification is sent to the client 60 seconds before
the session ends, allowing you to take further actions.

The following example shows how to detect an impending session termination by
listening for a *going away* notification:

### Swift

    for try await response in session.responses {
      switch response.payload {

      case .goingAwayNotice(let goingAwayNotice):
        // Prepare for the session to close soon
        if let timeLeft = goingAwayNotice.timeLeft {
            print("Server going away in \(timeLeft) seconds")
        }
      }
    }

### Kotlin

    for (response in session.responses) {
        when (val message = response.payload) {
            is LiveServerGoAway -> {
                // Prepare for the session to close soon
                val remaining = message.timeLeft
                logger.info("Server going away in $remaining")
            }
        }
    }

### Java

    session.getResponses().forEach(response -> {
        if (response.getPayload() instanceof LiveServerResponse.GoingAwayNotice) {
            LiveServerResponse.GoingAwayNotice notice = (LiveServerResponse.GoingAwayNotice) response.getPayload();
            // Prepare for the session to close soon
            Duration timeLeft = notice.getTimeLeft();
        }
    });

### Web

    for await (const message of session.receive()) {
      switch (message.type) {

      ...
      case "goingAwayNotice":
        console.log("Server going away. Time left:", message.timeLeft);
        break;
      }
    }

### Dart

    Future _handleLiveServerMessage(LiveServerResponse response) async {
      final message = response.message;
      if (message is GoingAwayNotice) {
         // Prepare for the session to close soon
         developer.log('Server going away. Time left: ${message.timeLeft}');
      }
    }

### Unity

    foreach (var response in session.Responses) {
        if (response.Payload is LiveSessionGoingAway notice) {
            // Prepare for the session to close soon
            TimeSpan timeLeft = notice.TimeLeft;
            Debug.Log($"Server going away notice received. Remaining: {timeLeft}");
        }
    }

> [!NOTE]
> **Note:** Firebase AI Logic does *not* yet support extending or resuming sessions.