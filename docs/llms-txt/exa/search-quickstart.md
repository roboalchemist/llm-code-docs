# Source: https://exa.ai/docs/reference/search-quickstart.md

> ## Documentation Index

> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt

> Use this file to discover all available pages before exploring further.

# Get started with Exa

> Make your first request to Exa's search API

<Tabs>
  <Tab title="Python">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Install the SDK</div>

        <div className="step-content">
          <p>Install the Python SDK with pip.</p>

          ```bash  theme={null}
          pip install exa-py
          ```text

      <li>
        <div className="step-number">2</div>

        <div className="step-line" />

        <div className="step-title">Create your code</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/api-keys" target="_blank">Exa Dashboard</a>, create a file called `exa.py`, and add the code below.</p>

          ```python python theme={null}
          from exa_py import Exa

          exa = Exa(api_key="your-api-key")

          result = exa.search(
            "blog post about artificial intelligence",
            type="auto",
            contents={
              "text": True
            }
          )
          ```text
    </ol>
  </Tab>

  <Tab title="JavaScript">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Install the SDK</div>

        <div className="step-content">
          <p>Install the JavaScript SDK with npm.</p>

          ```bash  theme={null}
          npm install exa-js
          ```text

      <li>
        <div className="step-number">2</div>

        <div className="step-line" />

        <div className="step-title">Create your code</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/api-keys" target="_blank">Exa Dashboard</a>, create a file called `exa.ts`, and add the code below.</p>

          ```javascript javascript theme={null}
          import Exa from "exa-js";

          const exa = new Exa("your-api-key");

          const result = await exa.search(
            "blog post about artificial intelligence",
            {
              type: "auto",
              contents: {
                text: true
              }
            }
          );
          ```text
    </ol>
  </Tab>

  <Tab title="cURL">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Make your first API call</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/api-keys" target="_blank">Exa Dashboard</a> and pass the following command to your terminal.</p>

          ```bash bash theme={null}
          curl --request POST \
            --url https://api.exa.ai/search \
            --header "accept: application/json" \
            --header "content-type: application/json" \
            --header "x-api-key: your-api-key" \
            --data '
          {
            "query": "blog post about artificial intelligence",
            "type": "auto",
            "contents": {
              "text": true
            }
          }'
          ```text
    </ol>
  </Tab>
</Tabs>
