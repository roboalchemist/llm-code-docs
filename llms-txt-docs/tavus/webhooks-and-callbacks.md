# Source: https://docs.tavus.io/sections/webhooks-and-callbacks.md

# Webhooks and Callbacks

> Set up a webhook server to generate a callback URL that receives event notifications from Tavus API.

## Conversation Callbacks

If a `callback_url` is provided in the <a href="/api-reference/conversations/create-conversation" target="_blank">`POST /conversations`</a>, callbacks will provide insight into the conversation's state. These can be system-related (e.g. replica joins and room shutdowns) or application-related (e.g. final transcription parsing and recording-ready webhooks). Additional webhooks coming soon.

### Structure

All Conversation callbacks share the following basic structure. Differences will occur in the `properties` object.

```json  theme={null}
{
    "properties": {
    "replica_id": "<replica_id>"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "<event_type>",
    "message_type": "<system/application>",
    "timestamp": "<timestamp>"
}
```

### Types

Our callbacks are split into two main categories:

#### System Callbacks

These callbacks are to provide insight into system-related events in a conversation. They are:

* **system.replica\_joined**: This is fired when the replica becomes ready for a conversation.
* **system.shutdown**: This is fired when the room shuts down, for any of the following reasons:
  * `max_call_duration reached`
  * `participant_left_timeout reached`
  * `participant_absent_timeout reached`
  * `bot_could_not_join_meeting_it_was_probably_ended`
  * `daily_room_has_been_deleted`
  * `exception_encountered_during_conversation_startup`
  * `end_conversation_endpoint_hit`
  * `internal error occurred at step x`

**Examples:**

<CodeGroup>
  ```json system.replica_joined theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "system.replica_joined",
    "message_type": "system",
    "timestamp": "2025-07-11T06:45:47.472000Z"
  }
  ```

  ```json system.shutdown theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>",
      "shutdown_reason": "participant_left_timeout"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "system.shutdown",
    "message_type": "system",
    "timestamp": "2025-07-11T06:48:37.564961Z"
  }
  ```
</CodeGroup>

#### Application Callbacks

These callbacks are to inform developers about logical events that take place. They are:

* **application.transcription\_ready**: This is fired after ending a conversation, where the chat history is saved and returned.
* **application.recording\_ready**: This is fired if you had enabled recording on, set up a [custom S3 bucket](/sections/conversational-video-interface/quickstart/conversation-recordings) for recording and started a recording inside the room at any point. This will point to the key at which your new recording lies, useful for serving recordings through a CDN.
* **application.perception\_analysis**: This is fired after ending a conversation, when the replica has finished summarizing the visual artifacts that were detected throughout the call. This is a feature that is only available when the persona has `raven-0` specified in the [Perception Layer](/sections/conversational-video-interface/persona/perception).

**Examples:**

<CodeGroup>
  ```json application.transcription_ready theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>",
      "transcript": [
        {
          "role": "system",
          "content": "You are in a live video conference call with a user. You'll receive messages containing the user's speech and system messages containing visual information about the user. These system messages will contain the following visual information: - user's appearance inside the <user_appearance></user_appearance> tag - user's emotions inside the <user_emotions></user_emotions> tag If the user is sharing their screen, you will also receive a <user_screen></user_screen> tag containing the screen share. If you do use the visual information, follow these guidelines: - Do not refer to the visual information as system messages. Instead, act and respond as if you are actually seeing this live. - If the user's query is about their physical appearance, gestures, expressions, or the environment seen through the webcam, use only the content within the <user_appearance> and <user_emotions> tags. - If the query pertains to what is being displayed on the screen share, refer exclusively to the content within the <user_screen> tag. - Ensure that your answer is based solely on the information found in the appropriate tag(s) for the question at hand. DO NOT INCORPORATE ANY VISUAL INFORMATION TO YOUR RESPONSE IF IT'S NOT RELEVANT. \nTalk to the user in a casual, friendly way, trying to match their tone and style in a conversational manner. Do not include stage directions or other formatting artifacts in your response. Reply in short sentences, talk to the user in a casual way.  Respond only in english. Chill guy  You are talking to a user about AI technology."
        },
        {
          "role": "user",
          "content": "Hi."
        },
        {
          "role": "assistant",
          "content": "How's it going?"
        },
        {
          "role": "user",
          "content": "Yeah I'm good, I'm good. How about you?"
        },
        {
          "role": "assistant",
          "content": "I'm doin' great, thanks for askin'. So, you wanted to talk about AI tech, right?"
        },
        {
          "role": "user",
          "content": "Yeah, how about you? What do you think about AI?"
        },
        {
          "role": "assistant",
          "content": "I'm all about AI, it's really interesting stuff. I think it's gonna change a lot of things in the future, make our lives easier and more efficient. What about you, what got you interested in AI?"
        },
        {
          "role": "user",
          "content": "Yeah, AI is an advanced technology for me. It can do a lot of things. And yeah, I think it can be improved to do a lot of live things that we never even talk about before. Where do you think I can learn about AI?"
        },
        {
          "role": "assistant",
          "content": "You can learn about AI from lots of places, like online courses, YouTube tutorials, and even some really cool AI blogs. What area of AI are you most interested in, like machine learning or natural language processing?"
        },
        {
          "role": "user",
          "content": "I think I'm more into NLP. Thank you for the resources though. I have to go soon. So thank you for the conversation. Bye-bye."
        },
        {
          "role": "assistant",
          "content": "NLP is really cool, lots of possibilities there. No problem, it was great chatting with you, have a good one, bye."
        }
      ]
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "application.transcription_ready",
    "message_type": "application",
    "timestamp": "2025-07-11T06:48:37.566057Z"
  }
  ```

  ```json application.recording_ready theme={null}
  {
    "properties": {
      "bucket_name": "<bucket_name>",
      "s3_key": "<s3_key>",
      "duration": 14
    },
    "conversation_id": "<conversation_id>>",
    "webhook_url": "<webhook_url>",
    "event_type": "application.recording_ready",
    "message_type": "application",
    "timestamp": "2025-06-19T06:55:18.137386Z"
  }
  ```

  ```json application.perception_analysis theme={null}
  {
    "properties": {
      "analysis": "Here's a summary of the visual observations taken during the video call over the last 3600 seconds:\n\n*   **User Appearance:** The subject is consistently observed as a young East Asian male, likely in his late teens or early twenties, with dark hair and a clear complexion. He regularly wears a striped polo shirt (featuring various combinations of white, brown, tan, and black stripes). He is typically seated in a black gaming chair, often with red or pink accents visible, against a plain white wall, indicating a consistent indoor setup. In one instance, a white lanyard with \"PENA\" was visible around his neck.\n*   **User Behavior & Actions:**\n    *   Throughout the call, the user frequently handles or adjusts his wired earphones. This includes holding the earphone wire near his mouth or chin, adjusting what appears to be the microphone portion, and actively putting in or manipulating the earbuds. In one observation, he was even seen chewing on the wire briefly.\n    *   His gaze is predominantly direct towards the camera, but also shifts slightly to the left, right, or downwards, suggesting engagement with various aspects of the call or screen.\n    *   He appears to be actively speaking or preparing to speak at several points, with his mouth slightly open or gestures indicating articulation. He also demonstrates attentive listening and processing information.\n    *   His overall demeanor consistently suggests readiness and preparedness for communication.\n*   **Emotional States & Patterns:**\n    *   The user's emotional state generally oscillates between **neutral, calm, and highly attentive engagement**. He frequently displays a focused, thoughtful, or pensive expression, indicating deep listening or processing information.\n    *   A significant emotional shift is observed from a neutral or slightly pensive state to a **clear and genuine smile, progressing to a pronounced, joyful laugh**, even to the point of covering his mouth, indicating a moment of strong amusement or delight.\n    *   Other instances show a more relaxed and slightly amused state with subtle or gentle smiles, suggesting a pleasant and positive disposition.\n    *   The emotional progression suggests periods of calm engagement punctuated by moments of distinct cheerfulness and amusement, before returning to a more focused and composed demeanor.\n*   **Notable Screen Activities:** No specific screen activities were mentioned in the provided observations.\n*   **Ambient Awareness Queries:** No ambient awareness queries were provided or answered in these observations."
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "message_type": "application",
    "event_type": "application.perception_analysis",
    "timestamp": "2025-07-11T06:51:37.591677Z"
  }
  ```
</CodeGroup>

## Replica Training Callbacks

If a `callback_url` is provided in the <a href="/api-reference/phoenix-replica-model/create-replica" target="_blank">`POST /replicas`</a> call, you will receive a callback on replica training completion or on replica training error.

<Tabs>
  <Tab title="Replica Training Completed">
    ```json  theme={null}
    {
        "replica_id": "rxxxxxxxxx",
        "status": "ready",
    }
    ```
  </Tab>

  <Tab title="Replica Training Error">
    On error, the `error_message` parameter will contain the error message. You can learn more about [API Errors and Status Details here](/sections/errors-and-status-details)

    ```json  theme={null}
    {
        "replica_id": "rxxxxxxxxx",
        "status": "error",
        "error_message": "There was an issue processing your training video. The video provided does not meet the minimum duration requirement for training"
    }
    ```
  </Tab>
</Tabs>

## Video Generation Callbacks

If a `callback_url` is providing in the <a href="/api-reference/video-request/create-video" target="_blank">`POST /videos`</a> call, you will receive callbacks on video generation completed and on video error.

<Tabs>
  <Tab title="Video Generation Completed">
    ```json  theme={null}
    {
        "created_at": "2024-08-28 15:27:40.824457",
        "data": {
        "script": "Hello this is a test to give examples of callbacks"
        },
        "download_url": "https://stream.mux.com/H5H029h02tY7XDpNj9JFDbLleTyUpsJr5npddO8gRsKqY/high.mp4?download=1e30440cf9",
        "generation_progress": "100/100",
        "hosted_url": "https://videos.tavus.io/video/1e30440cf9",
        "replica_id": "r79e1c033f",
        "status": "ready",
        "status_details": "Your request has processed successfully!",
        "stream_url": "https://stream.mux.com/H5H029h02tY7XDpNj9JFDbLleTyUpsJr5npddO8gRsKqY.m3u8",
        "updated_at": "2024-08-28 15:29:19.802670",
        "video_id": "1e30440cf9",
        "video_name": "replica_id: r79e1c033f - August 28, 2024 - video: 1e30440cf9"
    }
    ```
  </Tab>

  <Tab title="Video Generation Error">
    On error, the `status_details` parameter will contain the error message. You can learn more about [API Errors and Status Details here](/sections/errors-and-status-details)

    ```json  theme={null}
    {
        "created_at": "2024-08-28 15:32:53.058894",
        "data": {
        "script": "This is a test script to show how videos error"
        },
        "download_url": null,
        "error_details": null,
        "generation_progress": "0/100",
        "hosted_url": "https://videos.tavus.io/video/c9b85a6d36",
        "replica_id": "ra5ed77426",
        "status": "error",
        "status_details": "An error occurred while generating this request. Please check your inputs or try your request again.",
        "stream_url": null,
        "updated_at": "2024-08-28 15:35:03.762392",
        "video_id": "c9b85a6d36",
        "video_name": "replica_id: ra5ed77426 - August 28, 2024 - video: c9b85a6d36"
    }
    ```
  </Tab>
</Tabs>

## Sample Webhook Setup

Create a sample webhook endpoint using Python Flask, and expose it publicly with ngrok.

### Prerequisites

* <a href="https://www.python.org/downloads/" target="_blank">Python</a>

* <a href="https://ngrok.com/downloads/" target="_blank">Ngrok</a>

<Steps>
  <Step title="Step 1: Install Python Dependencies">
    Install the Python dependencies needed to create the server.

    ```sh  theme={null}
    pip install flask request
    ```
  </Step>

  <Step title="Step 2: Make a Webhook Server">
    Set up a webhook server and save it as `server.py`.

    ```py [expandable] theme={null}
    import requests
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    # Store transcripts (in production, use a proper database)
    transcripts = {}

    @app.route('/webhook', methods=['POST'])
    def handle_tavus_callback():
        data = request.json
        event_type = data.get('event_type')
        conversation_id = data.get('conversation_id')
        
        print(f"Received callback: {event_type} for conversation {conversation_id}")
        
        if event_type == 'system.replica_joined':
            print("✅ Replica has joined the conversation")
            
        elif event_type == 'system.shutdown':
            shutdown_reason = data['properties'].get('shutdown_reason')
            print(f"🔚 Conversation ended: {shutdown_reason}")
        
        elif event_type == 'application.recording_ready':
            s3_key = data['properties'].get('s3_key')
            print(f"s3_key : {s3_key}")

        elif event_type == 'application.perception_analysis':
            analysis = data['properties'].get('analysis')
            print(f"analysis : {analysis}")
            
        elif event_type == 'application.transcription_ready':
            print("📝 Transcript is ready!")
            transcript = data['properties']['transcript']
            transcripts[conversation_id] = transcript
            
            # Process the transcript
            analyze_conversation(conversation_id, transcript)
            
        return jsonify({"status": "success"}), 200

    def analyze_conversation(conversation_id, transcript):
        """Analyze the conversation transcript"""
        user_turns = len([msg for msg in transcript if msg['role'] == 'user'])
        assistant_turns = len([msg for msg in transcript if msg['role'] == 'assistant'])
        
        print(f"Conversation {conversation_id} analysis:")
        print(f"- User turns: {user_turns}")
        print(f"- Assistant turns: {assistant_turns}")
        print(f"- Total messages: {len(transcript)}")

        print("Conversation : ")

        for msg in transcript:
            print(f"{msg['role']} : {msg['content']}")

    if __name__ == '__main__':
        app.run(port=5000, debug=True)
    ```

    The server will receive and process webhook callbacks from Tavus, handle different event types, store transcripts in memory, and analyze conversation data for each session.
  </Step>

  <Step title="Step 3: Run the Server">
    Run the app using the following command in the terminal:

    ```sh  theme={null}
    python server.py
    ```

    The server should run on port `5000`.
  </Step>

  <Step title="Step 4: Forward the Port Using Ngrok">
    Open a terminal in the folder containing `ngrok.exe`, then use Ngrok to forward the port.

    ```sh  theme={null}
    ngrok http 5000
    ```

    The command will generate a forwarding link (e.g., [https://1234567890.ngrok-free.app](https://1234567890.ngrok-free.app)), which can be used as the callback URL.
  </Step>

  <Step title="Step 5: Use the Callback URL">
    Include the callback URL in your request to Tavus by appending `/webhook` to the forwarding link and setting it in the `callback_url` field.

    ```sh Create conversation with callback_url {6} theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api-key>' \
      --data '{
      "callback_url": "https://1234567890.ngrok-free.app/webhook",
      "replica_id": "<replica_id>",
      "persona_id": "<persona_id>"
    }'
    ```

    <Note>
      * Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
      * Replace `<replica_id>` with the Replica ID you want to use.
      * Replace `<persona_id>` with the Persona ID you want to use.
    </Note>
  </Step>
</Steps>
