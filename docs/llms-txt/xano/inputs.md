# Source: https://docs.xano.com/building/logic/core-components/inputs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inputs

> Data that is supplied to the logic before execution

Inputs are the data that is supplied to the primitive *outside of Xano* that it needs to run. For example, an API used to log in would probably need an email and a password.

There are several different types of inputs you can use to handle any data type. You can also make inputs optional, required, lists, or apply filters to transform them or require them to meet certain criteria.

### Adding an Input

<Tabs>
  <Tab title="Visually: Canvas View" icon="share-nodes">
    <Steps>
      <Step title="Click Add an Input">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-103714.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=9be1c801b5c70e2272265b342f158b59" alt="apis-20251013-103714" width="1147" height="684" data-path="images/apis-20251013-103714.png" /></Frame>
      </Step>

      <Step title="Select the type of input you want to add.">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-103749.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=2d3ae035fa65417a2f1218be9d3035a2" alt="apis-20251013-103749" width="1155" height="682" data-path="images/apis-20251013-103749.png" /></Frame>
      </Step>
    </Steps>
  </Tab>

  <Tab title="Visually: Function Stack" icon="stack">
    <Steps>
      <Step title="Click Add an Input">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/inputs-20251013-105146.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=4a81cfc50ad2023829f3b5b6252e00a2" alt="inputs-20251013-105146" width="995" height="558" data-path="images/inputs-20251013-105146.png" /></Frame>
      </Step>

      <Step title="Select the type of input you want to add.">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/inputs-20251013-105219.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=af6c33c0de68fbd642adf1d8c86e4d09" alt="inputs-20251013-105219" width="1166" height="634" data-path="images/inputs-20251013-105219.png" /></Frame>
      </Step>
    </Steps>
  </Tab>

  <Tab title="XanoScript" icon="code">
    Inputs are defined in the `input` block, placed immediately after the declaration and accompanying parameters, such as the description.

    ```javascript lines icon="code" Example of the input block and positioning theme={null}
    query user_list verb=GET {
        description = "Query all user records"
        input {
            text name? filters=trim
            }
      ...
    }   
    ```
  </Tab>
</Tabs>

Each input will have a different set of options depending on the input type chosen. Keep reading to see more information about all of the available input types and available options.

### Input Options

| Option                   | Explanation                                   | Example                                                    |
| ------------------------ | --------------------------------------------- | ---------------------------------------------------------- |
| Description              | A short, human-readable summary of the input. | For an `email` field: “The user’s email address.”          |
| Data structure           | Single value or list of values.               | Set to `list` to allow multiple values.                    |
| Allow nullable values    | Whether the input can be `null`.              | Set to `true` to allow `null`.                             |
| Default value            | Value used if input isn’t provided.           | Useful for optional fields that still need a stored value. |
| Required                 | Whether the input must be provided.           | Set to `true` to make the field mandatory.                 |
| Sensitive data           | Whether the field contains sensitive info.    | Set to `true` to hide it from request history.             |
| Custom rules and filters | Filters and validation applied to the input.  | e.g. `trim` to remove whitespace.                          |

## Filters and Rules

<Tabs>
  <Tab title="Visually" icon="eye">
    With your input selected, scroll down to the Custom Rules and Filters section, and choose **+ Add an Input Rule**.

    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/inputs-20251013-124949.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=d3cbfbe25703a52724c5e4f930bc8be4" alt="inputs-20251013-124949" width="424" height="812" data-path="images/inputs-20251013-124949.png" /></Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    Filters and rules are defined in the input block, placed immediately after the input type.

    ```javascript lines icon="code" Example of filters and rules in XanoScript theme={null}
    text name? filters=trim|lower
    text name? min:8|minAlpha:1|minDigit:1
    ```
  </Tab>
</Tabs>

### Input Filters

Transform the data sent to the input on the fly.

| Filter  | Explanation                      | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trim`  | Trims whitespace from the input. | `‎ ‎ hello‎ ‎ ` becomes `hello` <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-120859.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=08c4393e46442410c4ad6535e3a6aa1e" alt="core-components-20251010-120859" width="543" height="187" data-path="images/core-components-20251010-120859.png" /></Frame> |
| `lower` | Converts the input to lowercase. | `HELLO` becomes `hello`<br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-120935.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=a9b74b7fd41cd6101ebefedbbfb033ce" alt="core-components-20251010-120935" width="543" height="156" data-path="images/core-components-20251010-120935.png" /></Frame>          |
| `upper` | Converts the input to uppercase. | `hello` becomes `HELLO`<br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-120954.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=d17227b28bf20020b59a04ba2931f16f" alt="core-components-20251010-120954" width="550" height="162" data-path="images/core-components-20251010-120954.png" /></Frame>          |

### Input Rules

Validate the data sent to the input. If the data doesn't meet the criteria, the logic will fail to execute.

| Rule         | Explanation                        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `min`        | Requires a minimum length.         | `Hello` is not valid, but `Hello World` is. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121029.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=78a2ab21299bc69028dee352437b155e" alt="core-components-20251010-121029" width="546" height="302" data-path="images/core-components-20251010-121029.png" /></Frame>                                                  |
| `max`        | Requires a maximum length.         | `Hello World` is not valid, but `Hello` is. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121049.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=80677d9e9c208a168b4c6a570abf40b4" alt="core-components-20251010-121049" width="547" height="304" data-path="images/core-components-20251010-121049.png" /></Frame>                                                  |
| `startsWith` | Requires a prefix.                 | If set to `invoice-`, `invoice-abc123` is valid, but `abc123` is not. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121215.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=40a7ac43b9a077c13067fbf1ce01c737" alt="core-components-20251010-121215" width="548" height="301" data-path="images/core-components-20251010-121215.png" /></Frame>                        |
| `prevent`    | Prevents a phrase.                 | If set to `hello`, `hello world` is not valid, but `goodbye world` is. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121300.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=dc86585de64984d2c254495af1a0272e" alt="core-components-20251010-121300" width="545" height="300" data-path="images/core-components-20251010-121300.png" /></Frame>                       |
| `alphaOk`    | Allows alphabetic characters only. | `hello` is valid, but `hello123` is not. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121318.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=716cd05c172a687824317620acff37b1" alt="core-components-20251010-121318" width="545" height="160" data-path="images/core-components-20251010-121318.png" /></Frame>                                                     |
| `digitOk`    | Allows numerical characters only.  | `hello` is not valid, but `123` is. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121334.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=aa26156d29d632eae381bff437a3e781" alt="core-components-20251010-121334" width="543" height="165" data-path="images/core-components-20251010-121334.png" /></Frame>                                                          |
| `ok`         | Allows only specific characters.   | If set to `abc123`, `hello` is not valid, but `abc123` is. `abc` is valid, but `cde` is not. <br /><br /><Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/core-components-20251010-121357.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=f7e6f86edd25e859f50d920a47d496a5" alt="core-components-20251010-121357" width="540" height="302" data-path="images/core-components-20251010-121357.png" /></Frame> |

## Input Reference

Review all available input types below by selecting the section you're interested in.

<Card title="Text" icon="text">
  A plain string of text, code, or any other characters.
</Card>

<Card title="Integer" icon="arrow-up-1-9">
  A whole number, such as a count, year, or ID.
</Card>

<Card title="UUID" icon="fingerprint">
  A <em>Universally Unique Identifier</em> — a random string used to ensure record uniqueness.
</Card>

<Card title="Object" icon="brackets-curly">
  A JSON object with a defined schema (e.g., user settings or product details).\\

  ```json lines icon="code" Example of an object input theme={null}
  {
      "name": "John Doe",
      "age": 30,
      "email": "john.doe@example.com"
  }
  ```
</Card>

<Card title="Table Reference" icon="link">
  An integer or UUID referencing a record in another table.
</Card>

<Card title="Vector" icon="diagram-project">
  A fixed-length array of numbers (embedding) for similarity search in AI/ML.
</Card>

<Card title="Enum" icon="list-radio">
  A predefined list of values to enforce consistency (e.g., "To Do", "In Progress", "Done", "Pending").
</Card>

<Card title="Timestamp" icon="clock">
  A point in time in milliseconds since the Unix Epoch (Jan 1, 1970).
</Card>

<Card title="Date" icon="calendar">
  A calendar date in <code>YYYY-MM-DD</code> format.
</Card>

<Card title="Boolean" icon="check-circle">
  A true or false value.
</Card>

<Card title="Decimal" icon="calculator">
  A number with a decimal point (e.g., 1.5, 100.00, 0.001).
</Card>

<Card title="Email" icon="envelope">
  An email address.
</Card>

<Card title="Password" icon="lock">
  A hashed and salted password. Plain text is never stored or retrievable.
</Card>

<Card title="JSON" icon="brackets-curly">
  A flexible JSON object or array without a defined schema — ideal for variable data (e.g., from external APIs).

  ```json lines icon="code" Example of a JSON input theme={null}
  {
      "name": "John Doe",
      "age": 30,
      "email": "john.doe@example.com"
  }
  ```
</Card>

<Card title="Storage" icon="floppy-disk">
  File metadata for images, videos, audio, or other files (e.g., URL, name, size, type). Actual files are not stored in the database.
</Card>

<Card title="Geography" icon="map-pin">
  Stores geographic data such as a point, path, or polygon.
</Card>


Built with [Mintlify](https://mintlify.com).