# Source: https://posthog.com/docs/logs/link-session-replay.md

# Source: https://posthog.com/docs/llm-analytics/link-session-replay.md

# Link session replay - Docs

Connecting your backend LLM events to frontend session replays provides complete visibility into the user journey, helping you understand the full context around AI interactions in your application.

## Why link to session replay?

By including session IDs in your LLM events, you can:

-   **See the full user journey**: Navigate from an LLM trace directly to the session replay to see user actions before, during, and after AI interactions
-   **Debug issues faster**: Quickly find and watch the exact session where problems occurred
-   **Understand user behavior**: See how users interact with AI features and what prompts they use
-   **Correlate performance**: Match slow AI responses with actual user experience impact

## Implementation

There are two ways to pass session IDs from your frontend to your backend:

1.  **Automatic header injection** - posthog-js automatically adds headers to your API requests
2.  **Manual approach** - explicitly pass the session ID in your request body

### Option 1: Automatic header injection (recommended)

Configure posthog-js to automatically inject session headers into requests to your backend:

JavaScript

PostHog AI

```javascript
posthog.init('<ph_project_token>', {
  api_host: 'https://us.i.posthog.com',
  __add_tracing_headers: ['api.your-app.com']  // Your backend hostname(s)
})
```

This automatically adds `X-POSTHOG-SESSION-ID` (and `X-POSTHOG-DISTINCT-ID`) headers to all `fetch` and `XMLHttpRequest` calls to the specified hostnames.

On your backend, read the header and include it in your LLM tracking:

PostHog AI

### JavaScript

```javascript
app.post('/api/chat', async (req, res) => {
  const sessionId = req.headers['x-posthog-session-id']
  const response = await openai.responses.create({
    model: 'gpt-5',
    messages: [{ role: 'user', content: req.body.message }],
    posthogDistinctId: req.userId,
    posthogProperties: {
      $session_id: sessionId  // Links to session replay
    }
  })
  res.json({ response: response.choices[0].message.content })
})
```

### Python

```python
@app.route('/api/chat', methods=['POST'])
def chat():
    session_id = request.headers.get('X-POSTHOG-SESSION-ID')
    response = client.responses.create(
        model="gpt-5",
        messages=[{"role": "user", "content": request.json['message']}],
        posthog_distinct_id=current_user.id,
        posthog_properties={
            "$session_id": session_id  # Links to session replay
        }
    )
    return jsonify({
        "response": response.choices[0].message.content
    })
```

### Option 2: Manual approach

If you prefer explicit control, retrieve the session ID and pass it in your request body:

JavaScript

PostHog AI

```javascript
// Frontend
import posthog from 'posthog-js'
const response = await fetch('/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: userInput,
    sessionId: posthog.getSessionId()
  })
})
```

PostHog AI

### JavaScript

```javascript
// Backend
app.post('/api/chat', async (req, res) => {
  const { message, sessionId } = req.body
  const response = await openai.responses.create({
    model: 'gpt-5',
    messages: [{ role: 'user', content: message }],
    posthogDistinctId: req.userId,
    posthogProperties: {
      $session_id: sessionId  // Links to session replay
    }
  })
  res.json({ response: response.choices[0].message.content })
})
```

### Python

```python
# Backend
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get('sessionId')
    response = client.responses.create(
        model="gpt-5",
        messages=[{"role": "user", "content": data['message']}],
        posthog_distinct_id=current_user.id,
        posthog_properties={
            "$session_id": session_id  # Links to session replay
        }
    )
    return jsonify({
        "response": response.choices[0].message.content
    })
```

## Viewing linked replays

Once you've set up session linking, you can navigate from LLM generations to their corresponding session replays:

1.  In the [LLM analytics dashboard](https://app.posthog.com/llm-analytics), find the generation or trace you're interested in
2.  Click the session replay button to jump directly to the replay
3.  Watch the user's interaction with your AI features in context

This linking helps you understand not just what your AI is doing, but how users are experiencing it in your application.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better