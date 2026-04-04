# Source: https://docs.zapier.com/platform/build-cli/typescript-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TypeScript integrations

> TypeScript is a first-class language for building integrations with the CLI.

TypeScript is the recommended way to build integrations with the Zapier CLI.
Support for TypeScript was significantly expanded in early 2025 when v17 of the
Zapier platform and CLI was released. This document covers how to create, use,
and test TypeScript integrations.

## Getting Started

The TypeScript+ESM templates generated with `zapier-platform init` (or the deprecated `zapier init`) provide the
configuration needed to get started with TypeScript integrations. If you
are adding TypeScript support to an existing app, you can check the
[Structure of a TS Integration](#structure-of-a-ts-integration) section
below for more details information about compiler settings, using the
`zapier-platform-core` library, and how to compose Triggers, Creates,
and Searches together with TypeScript.

As of the 17.4.0 Platform release, all authentication templates support the `--language`
flag on the `zapier-platform init` command (or deprecated `zapier init`), which can be set to `typescript` or `javascript`.
Note that all TypeScript templates now default to ESM.

For example, for Basic Auth:

```shell  theme={null}
# (deprecated) $ zapier init my-app --template basic-auth --language typescript
$ zapier-platform init my-app --template basic-auth --language typescript
$ cd my-app
$ npm install
```

This will create a new app in `./my-app` with the following structure,
and install the dependencies.

```
my-app/
├── src/
│   ├── authentication.ts
│   ├── index.ts
├── package.json
└── tsconfig.json
```

To add triggers, creates, and searches, you can then run `zapier-platform scaffold` (or deprecated `zapier scaffold`) as needed.
The scaffold command will automatically detect you're using TypeScript, and create the
correct code accordingly:

```shell  theme={null}
# (deprecated) $ zapier scaffold trigger contact
# (deprecated) $ zapier scaffold create contact
$ zapier-platform scaffold trigger contact
$ zapier-platform scaffold create contact
```

## Differences from JS Integrations

There are a few important differences between how TypeScript and
JavaScript integrations are implemented that are worth noting.

* The `define` helper functions are important to wrap your App,
  Triggers, Creates, Searches, and Input Field definitions.
* Code is kept in the `src/` directory and compiled to `dist/`. The
  root of the integration now becomes `./src/index.ts`.
* Modern `import`/`export` syntax is used instead of Node's
  `require`/`module.exports` assignments.
* We recommend testing with [Vitest](https://vitest.dev/), a drop-in
  replacement for Jest that is faster and has better ESM+TypeScript
  support.

## Input Fields

The `defineInputFields` helper function should be used to define the
inputs for all of Triggers, Creates, and Searches. This helper will
automatically infer the types of all of the input fields specified.

This looks like:

```ts  theme={null}
import {
  defineInputFields,
  defineXyz, // i.e. defineTrigger, defineCreate, defineSearch.
  type XyzPerform, // Different per action+perform type.
} from "zapier-platform-core";

const inputFields = defineInputFields([
  // Input fields definition here.
]);

const perform = (async (z, bundle) => {
  // Bundle.inputData typed from inputFields.
  // perform requests & app logic here.
}) satisfies XyzPerform<typeof inputFields>;

export default defineXyz({
  // ... Other details: key, display, noun, etc.
  operations: { inputFields, perform }, // Composed here.
});
```

This is a departure from the previous approach of typically defining the
inputs and sometimes perform functions inside of the top-level exported
action.

### Reusing Input Fields

Input Fields are frequently reused across triggers, creates, and
searches. To make this easier, there is also a singular
`defineInputField` helper that can be used to define an input field.
These can be put somewhere in the `src/` directory, and then imported by
the actions that need them.

```ts  theme={null}
// ./src/inputFields.ts
import { defineInputField } from "zapier-platform-core";

export const SOME_COMMON_FIELD = defineInputField({
  key: "someKey",
  type: "boolean",
  required: true,
});

// ./src/triggers/someTrigger.ts
import { defineInputFields } from "zapier-platform-core";
import { SOME_COMMON_FIELD } from "../inputFields";

const inputFields = defineInputFields([
  SOME_COMMON_FIELD,
  { key: "someOtherKey", type: "string", required: true },
]);

// bundle.inputData: { someKey: boolean; someOtherKey: string }
```

### Dynamic Input Fields

Inputs fields can be dynamic, meaning they are functions that get
executed and can return zero, one, or more input fields determined at
runtime. This is useful when the input fields are dependent on the
values of other input fields, or input field definitions are fetched and
prepared from your API, like is the case for CRM and Database APIs.

The example below shows a dynamic input field that is used to optionally
include a custom subject field when a prior boolean input field is set
to `true`.

```ts  theme={null}
import { defineInputField, defineInputFields } from "zapier-platform-core";

const customSubjectField = defineInputField((z, bundle) => {
  if (bundle.inputData.useCustomSubject as boolean) {
    return defineInputFields([
      { key: "customSubject", type: "string", required: true },
    ]);
  }
  return defineInputFields([]); // IMPORTANT: All returns must be typed.
});

const inputFields = defineInputFields([
  { key: "useCustomSubject", type: "boolean", required: true },
  customSubjectField,
]);

// bundle.inputData: { useCustomSubject: boolean; customSubject?: string }
```

<Warning>
  Inside of dynamic input field functions, `bundle.inputData` will not have type
  information for its sibling input fields. We recommend casting referenced
  fields to their known types. For example above, note
  `inputData.useCustomSubject as boolean`.
</Warning>

#### Known vs Unknown Fields

The example above shows a *known* dynamic input field, where the key and
type are known ahead of time, and the function's logic is used to
include it or not, based on other fields. These sorts of input fields
can be captured by the type system and included in the
`bundle.inputData` property. Input fields returned from input functions
are *always* considered optional, even if they have `required: true` in
their definition, as they cannot be guaranteed to be present.

When fields cannot be known ahead of time, the input function can return
completely *unknown* input fields. This is useful when the input fields
are derived from data returned from an API. In this case, known inputs
are preserved, but the `bundle.inputData` property will consider any
other properties as `unknown`.

```ts  theme={null}
// Unknown dynamic input fields example

import { defineInputField, defineInputFields } from "zapier-platform-core";

/** Example API field type, differs from Zapier Fields */
type ApiField = {
  id: string;
  label: string;
  type: "Text" | "Number" | "Boolean";
};

/** Fetch and prepare multiple input fields from an API. */
const getItemFields = defineInputField(async (z, { inputData }) => {
  const response = await z.request<ApiField[]>(
    `${API_URL}/item/${inputData.itemId}/fields`,
  );
  return response.data.map(({ id, label, type }) =>
    defineInputField({
      key: id,
      label,
      type: type.toLowerCase() as "text" | "number" | "boolean",
    }),
  );
});

const inputFields = defineInputFields([
  { key: "itemId", type: "string", required: true, dynamic: "item.id.label" },
  getItemFields,
]);

// bundle.inputData: { itemId: string; [x: string]: unknown; }
```

## Perform Function Types

There are now dedicated types for all of the different types of Perform
Action. These should be imported with `type` qualified imports. The
relevant `operation` sections inside the `define` helpers will inform
and enforce the correct type for the different perform functions. They
are:

* Polling Triggers:
  * `PollingTriggerPerform`
* Webhook Triggers:
  * `WebhookTriggerPerform`
  * `WebhookTriggerPerformList`
  * `WebhookTriggerPerformSubscribe`
  * `WebhookTriggerPerformUnsubscribe`
* Creates:
  * `CreatePerform`
  * `CreatePerformResume`
* Searches:
  * `SearchPerform`
  * `SearchPerformResume`

They all take at least one type parameter, which is the shape of the the
bundle's `inputData` property. These Perform types should use
`satisfies XyzPerform<typeof inputFields>` to enforce the correct types but
preserve the return type information.

```ts  theme={null}
import type { PollingTriggerPerform } from "zapier-platform-core";

const perform = (async (z, bundle) => {
  // bundle.inputData: { a: number; b?: string }
}) satisfies PollingTriggerPerform<{ a: number; b?: string }>;
```

In most cases though, input data is derived from the array of input fields,
which can be passed directly to the perform functions to be automatically
inferred:

```ts  theme={null}
import type { PollingTriggerPerform } from "zapier-platform-core";

const inputFields = defineInputFields([
  { key: "a", type: "number", required: true },
  { key: "b", type: "string", required: false },
]);

const perform = (async (z, bundle) => {
  // bundle.inputData: { a: number; b?: string }
}) satisfies PollingTriggerPerform<typeof inputFields>;
```

The `bundle.inputData` property is now typed as the inferred input data
from the `inputFields` array.

## Structure of a TS Integration

TypeScript integrations follow the same structure and [underlying
schema](/platform/build-cli/overview#zapier-platform-schema) as any
JavaScript integration. The important difference is that TypeScript apps
require important components of integrations to be wrapped with the
relevant `define` helper functions to provide deep type inference about
the application. These are:

* `defineApp()` – Main function for the top-level app.
* `defineTrigger()`/`defineCreate()`/`defineSearch()` – For the
  relevant actions in an integration.
* `defineInputFields()` – Wraps an array of input field definitions to
  simplify handling full typing information about the input fields.

### `src/index.ts`

The main entry point of the app becomes `src/index.ts`. It should import
its dependencies, and the default export remains as the Application
object. Wrapping it with `defineApp` will help to check its structure.

Otherwise it's a normal integration, and you register Auth, middleware,
hydrators, Triggers, Creates, and Searches all the same way!

```ts  theme={null}
import { defineApp, version as platformVersion } from "zapier-platform-core";
import packageJson from "../package.json" with { type: "json" };

import authentication from "./authentication";
import someCreate from "./creates/some-create";
import someSearch from "./searches/some-search";
import someTrigger from "./triggers/some-trigger";

export default defineApp({
  // IMPORTANT: Note the use of `defineApp`
  version: packageJson.version,
  platformVersion,

  authentication,

  creates: {
    [someCreate.key]: someCreate,
  },
  searches: {
    [someSearch.key]: someSearch,
  },
  triggers: {
    [someTrigger.key]: someTrigger,
  },
});
```

### `src/authentication.ts`

Authentication is defined as a normal object and exported from a file
named `src/authentication.ts`. It uses a `satisfies Authentication`
constraint to check its structure, and does **not** use a `define`
helper.

```ts  theme={null}
// ./src/authentication.ts

import type { Authentication } from "zapier-platform-core";

import { SCOPES } from "./constants";

export default {
  type: "oauth2",
  test: { url: "https://api.webflow.com/v2/token/authorized_by" },
  connectionLabel: "{{email}}",
  oauth2Config: {
    authorizeUrl: {
      url: "https://webflow.com/oauth/authorize",
      params: {
        client_id: "{{process.env.CLIENT_ID}}",
        response_type: "code",
        scope: SCOPES.join(" "),
        redirect_uri: "{{bundle.inputData.redirect_uri}}",
        state: "{{bundle.inputData.state}}",
      },
    },
    getAccessToken: {
      url: "https://api.webflow.com/oauth/access_token",
      method: "POST",
      params: {
        client_id: "{{process.env.CLIENT_ID}}",
        client_secret: "{{process.env.CLIENT_SECRET}}",
        code: "{{bundle.inputData.code}}",
        grant_type: "authorization_code",
        redirect_uri: "{{bundle.inputData.redirect_uri}}",
      },
    },
  },
} satisfies Authentication; // IMPORTANT: Note the use of `satisfies`
```

### `src/middleware.ts`

Middleware functions are functions exported from `src/middleware.ts`,
that are typed as `BeforeRequestMiddleware` or
`AfterResponseMiddleware` types. They are registered in the same way as
in JavaScript integrations in `/src/index.ts`.

```ts  theme={null}
// ./src/middleware.ts

import type { BeforeRequestMiddleware } from "zapier-platform-core";

export const addBearerHeader: BeforeRequestMiddleware = (
  request,
  z,
  bundle,
) => {
  if (bundle.authData.access_token && !request.headers?.Authorization) {
    request.headers = {
      ...request.headers,
      Authorization: `Bearer ${bundle.authData.access_token}`,
    };
  }
  return request;
};
```

### `src/triggers/pollingTrigger.ts`

Triggers, Creates, and Searches are now recommended to define their
inputs and perform functions as separate objects, and composed together
in the `define` helper that is default export from the file.

```ts  theme={null}
// ./src/triggers/pollingTrigger.ts

import {
  defineInputFields,
  defineTrigger,
  type PollingTriggerPerform,
} from "zapier-platform-core";
import { API_URL } from "../constants.js";

const inputFields = defineInputFields([
  // IMPORTANT: Note `defineInputFields`
  {
    key: "country",
    type: "string",
    required: false,
  },
]);

const perform = (async (z, bundle) => {
  // `bundle.inputData` typed as `{ country?: string }`
  const response = await z.request(`${API_URL}/movies`);
  return response.data;
}) satisfies PollingTriggerPerform<typeof inputFields>; // IMPORTANT: Note `satisfies`

export default defineTrigger({
  key: "movie",
  noun: "Movie",

  display: {
    label: "New Movie",
    description: "Triggers when a new movie is created.",
  },

  operation: {
    type: "polling",
    inputFields,
    perform,
    sample: {
      id: "1",
      title: "example",
    },
  },
});
```

### `src/tsconfig.json`

The `tsconfig.json` file configures the TypeScript compiler. Below are
settings that are recommended for developing TypeScript integrations.

```ts  theme={null}
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "noUncheckedIndexedAccess": true,
    "isolatedModules": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true
  },
  "include": ["./src/**/*.ts"],
}
```
