# Source: https://dev.writer.com/blueprints/httprequest.md

# HTTP Request

Sends a HTTP request to an API endpoint. Used to fetch data or send data.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f16580b0da0799d3e2e7b634b0ae5ad3" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/http-request-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2ebc880428b61323734d9252705adb1d 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b59d2c22fa8f19372400a76cecfbb39a 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9a827d81ce58fda7004c533c277b4ffe 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=432b8fe8efbd99c5c439ce49b738ea70 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=205505cd825b9a46c0f2934b4a7e7115 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0b4a5458a3feecf5600c8b752bff346b 2500w" />

## Overview

The **HTTP Request** block sends an HTTP request to an API endpoint. Use it to fetch data from external services, send data to APIs, or integrate with third-party systems.

You can configure the HTTP method, URL, headers, body, and body type (plain text or JSON). The block supports `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` methods.

## Common use cases

* Fetching data from a REST API
* Sending data to a webhook or external service
* Integrating with third-party tools
* Automating workflows that require external communication

## How it works

1. **Method**: Choose the HTTP method, for example, `GET`, `POST`.
2. **URL**: Enter the endpoint URL. Pass path parameters in the URL; for example, `https://api.openweathermap.org/data/2.5/weather?q=@{payload.city}&appid=@{vault.openweather_key}&units=metric`.
3. **Headers**: Optionally specify headers as key-value pairs. You can also use [secrets](/agent-builder/secrets) to access API keys and other sensitive values.
4. **Body type**: Choose whether the body you are sending is `text` or `JSON`.
5. **Body**: Enter the request body for `POST`, `PUT`, and `PATCH` requests.

The block sends the request and returns the response. If the request fails due to a connection error (for example, network timeout, DNS failure), it outputs a connection error. If the request receives an error response from the server (for example, `4xx` or `5xx` status code), it outputs a response error. You can access the error details in the next block using the `@{message}` variable.

## Examples

### External API integration

This example demonstrates making HTTP requests to an external API using a public API endpoint. It uses the [Open-Notify API](https://open-notify.org/), which provides real-time data about the International Space Station (ISS); it's free and requires no authentication, so you can use this example to test your workflow before you use it with another API.

**Blueprint flow:**

1. **UI Trigger** → Receives request to fetch ISS location
2. **HTTP Request** → Calls Open-Notify API to get current ISS position
3. **Text generation** → Creates location description based on the body of the response (`@{result.body}`), which contains the latitude and longitude of the ISS
4. **Set state** → Stores the result of the text generation block in state variable to display in the UI

**HTTP Request block configuration:**

* **Method:** GET
* **URL:** `http://api.open-notify.org/iss-now.json`
* **Headers:** None
* **Body type:** None
* **Body:** None

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7da87767c917835dd9c5dded837a5755" alt="" data-og-width="2393" width="2393" data-og-height="1104" height="1104" data-path="images/agent-builder/blueprints/http-request-block-iss-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=120a0adf11befb6966b745ccb4ccb893 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4ef202e0e73f5506673b54afe448a927 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f89023e17cf48f567d938b6080d71e31 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c74718ccf7e1fba4b59e6cf88d00562f 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=51169b5c936726daa0af185016bd8fdd 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/http-request-block-iss-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7d02fb24d7b61df44dccb542cc31ca60 2500w" />

This workflow enables integration with external APIs to enhance your agent's capabilities.

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Method</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>GET - GET</li>

          <li>POST - POST</li>

          <li>PUT - PUT</li>

          <li>PATCH - PATCH</li>

          <li>DELETE - DELETE</li>
        </ul>
      </td>

      <td>
        Allowed values: GET, POST, PUT, PATCH, DELETE
      </td>
    </tr>

    <tr>
      <td>URL</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Headers</td>
      <td>Key-Value</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Body type</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>text</code>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>text - Plain text</li>

          <li>JSON - JSON</li>
        </ul>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Body</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Response error</td>
      <td>-</td>
      <td>error</td>
      <td>The connection was established successfully but an error response code was received or the response was invalid.</td>
    </tr>

    <tr>
      <td>Connection error</td>
      <td>-</td>
      <td>error</td>
      <td>The connection couldn't be established.</td>
    </tr>
  </tbody>
</table>
