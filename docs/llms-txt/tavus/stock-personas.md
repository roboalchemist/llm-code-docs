# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/stock-personas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Stock Personas

> Tavus offers pre-built personas to help you get started quickly.

These personas are optimized for a variety of real-world scenarios:

<Note>
  To fetch all available stock personas, use the <a href="/api-reference/personas/get-personas" target="_blank" rel="noopener noreferrer">List Personas endpoint</a>.
</Note>

### Education

<CardGroup cols={2}>
  <Card title="Sales Coach" icon="user">
    Teaches sales tips and strategies.

    ```text  theme={null}
    pdced222244b
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "rc2146c13e81",
            "persona_id": "pdced222244b"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Corporate Trainer" icon="briefcase">
    Delivers workplace training.

    ```text  theme={null}
    p7fb0be3
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "ra54d1d861",
            "persona_id": "p7fb0be3"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="History Teacher" icon="book">
    Talks about history topics.

    ```text  theme={null}
    pc55154f229a
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r6ae5b6efc9d",
            "persona_id": "pc55154f229a"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="College Tutor" icon="graduation-cap">
    Helps with academic subjects.

    ```text  theme={null}
    p88964a7
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "rfb51183fe",
            "persona_id": "p88964a7"
        }'
      ```
    </Accordion>
  </Card>
</CardGroup>

### Business

<CardGroup cols={2}>
  <Card title="Sales Agent at Tavus" icon="briefcase">
    Answers questions about Tavus.

    ```text  theme={null}
    pb8bb46b
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "ref226fe7e",
            "persona_id": "pb8bb46b"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Healthcare Intake Assistant" icon="stethoscope">
    Collects patient info

    ```text  theme={null}
    p5d11710002a
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r4317e64d25a",
            "persona_id": "p5d11710002a"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="AI Interviewer" icon="headset">
    Runs mock interviews.

    ```text  theme={null}
    pe13ed370726
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r9d30b0e55ac",
            "persona_id": "pe13ed370726"
        }'
      ```
    </Accordion>
  </Card>
</CardGroup>

### Assistant

<CardGroup cols={2}>
  <Card title="Technical Co Pilot" icon="code">
    Helps with coding.

    ```text  theme={null}
    pd43ffef
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "rbb0f535dd",
            "persona_id": "pd43ffef"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Tavus' Personal AI" icon="robot">
    General Tavus-branded assistant.

    ```text  theme={null}
    p2fbd605
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r4c41453d2",
            "persona_id": "p2fbd605"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Tavus Researcher" icon="flask">
    Shares research insights.

    ```text  theme={null}
    p48fdf065d6b
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "rf4703150052",
            "persona_id": "p48fdf065d6b"
        }'
      ```
    </Accordion>
  </Card>
</CardGroup>

### Others

<CardGroup cols={2}>
  <Card title="Demo Persona" icon="users">
    Tavus demo persona.

    ```text  theme={null}
    p9a95912
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r79e1c033f",
            "persona_id": "p9a95912"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Santa" icon="gift">
    Talks with Santa for festive experience.

    ```text  theme={null}
    p3bb4745d4f9
    ```

    <Accordion title="Create Conversation">
      ```shell  theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r3fbe3834a3e",
            "persona_id": "p3bb4745d4f9"
        }'
      ```
    </Accordion>
  </Card>
</CardGroup>
