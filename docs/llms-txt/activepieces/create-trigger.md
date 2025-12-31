# Source: https://www.activepieces.com/docs/build-pieces/building-pieces/create-trigger.md

# Source: https://www.activepieces.com/docs/developers/building-pieces/create-trigger.md

# Create Trigger

This tutorial will guide you through the process of creating trigger for a Gelato piece that fetches new icecream flavor.

## Trigger Definition

To create trigger run the following command,

```bash  theme={null}
npm run cli triggers create
```

1. `Piece Folder Name`: This is the name associated with the folder where the trigger resides. It helps organize and categorize triggers within the piece.
2. `Trigger Display Name`: The name users see in the interface, conveying the trigger's purpose clearly.
3. `Trigger Description`: A brief, informative text in the UI, guiding users about the trigger's function and purpose.
4. `Trigger Technique`: Specifies the trigger type - either [polling](../piece-reference/triggers/polling-trigger) or [webhook](../piece-reference/triggers/webhook-trigger).

**Example:**

```bash  theme={null}
npm run cli triggers create

? Enter the piece folder name : gelato
? Enter the trigger display name : new flavor created
? Enter the trigger description : triggers when a new icecream flavor is created.
? Select the trigger technique: polling
```

This will create a new TypeScript file at `packages/pieces/community/gelato/src/lib/triggers` named `new-flavor-created.ts`.

Inside this file, paste the following code:

```ts  theme={null}
import { gelatoAuth } from '../../';
import {
  DedupeStrategy,
  HttpMethod,
  HttpRequest,
  Polling,
  httpClient,
  pollingHelper,
} from '@activepieces/pieces-common';
import {
  PiecePropValueSchema,
  TriggerStrategy,
  createTrigger,
} from '@activepieces/pieces-framework';
import dayjs from 'dayjs';

const polling: Polling<
  PiecePropValueSchema<typeof gelatoAuth>,
  Record<string, never>
> = {
  strategy: DedupeStrategy.TIMEBASED,
  items: async ({ auth, propsValue, lastFetchEpochMS }) => {
    const request: HttpRequest = {
      method: HttpMethod.GET,
      url: 'https://cloud.activepieces.com/api/v1/webhooks/aHlEaNLc6vcF1nY2XJ2ed/sync',
      headers: {
        authorization: auth,
      },
    };
    const res = await httpClient.sendRequest(request);
    return res.body['flavors'].map((flavor: string) => ({
      epochMilliSeconds: dayjs().valueOf(),
      data: flavor,
    }));
  },
};

export const newFlavorCreated = createTrigger({
  auth: gelatoAuth,
  name: 'newFlavorCreated',
  displayName: 'new flavor created',
  description: 'triggers when a new icecream flavor is created.',
  props: {},
  sampleData: {},
  type: TriggerStrategy.POLLING,
  async test(context) {
    return await pollingHelper.test(polling, context);
  },
  async onEnable(context) {
    const { store, auth, propsValue } = context;
    await pollingHelper.onEnable(polling, { store, auth, propsValue });
  },

  async onDisable(context) {
    const { store, auth, propsValue } = context;
    await pollingHelper.onDisable(polling, { store, auth, propsValue });
  },

  async run(context) {
    return await pollingHelper.poll(polling, context);
  },
});
```

The way polling triggers usually work is as follows:

`Run`:The run method executes every 5 minutes, fetching data from the endpoint within a specified timestamp range or continuing until it identifies the last item ID. It then returns the new items as an array. In this example, the httpClient.sendRequest method is utilized to retrieve new flavors, which are subsequently stored in the store along with a timestamp.

## Expose The Definition

To make the trigger readable by Activepieces, add it to the array of triggers in the piece definition.

```typescript  theme={null}
import { createPiece } from '@activepieces/pieces-framework';
import { getIcecreamFlavor } from './lib/actions/get-icecream-flavor';
// Don't forget to add the following import.
import { newFlavorCreated } from './lib/triggers/new-flavor-created';

export const gelato = createPiece({
  displayName: 'Gelato Tutorial',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  authors: [],
  auth: gelatoAuth,
  actions: [getIcecreamFlavor],
  // Add the trigger here.
  triggers: [newFlavorCreated], // <--------
});
```

# Testing

By default, the development setup only builds specific components. Open the file `packages/server/api/.env` and include "gelato" in the `AP_DEV_PIECES`.

For more details, check out the [Piece Development](../development-setup/getting-started) section.

Once you edit the environment variable, restart the backend. The piece will be rebuilt. After this process, you'll need to **refresh** the frontend to see the changes.

To test the trigger, use the load sample data from flow builder in Activepieces. It should function as shown in the screenshot.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0ac29f0025296b3ecc2111709a2b9a33" alt="Gelato Action" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/screenshots/gelato-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=eca339aa40eb13c77c0523a69a53e98a 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=904295025aa163dec6da607b7c8a2b50 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=797d6f9dd13b1c2c4bf48f9e7b074c89 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9faad30e7502ed152a76af3085047433 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=21ae16d188441fee36496bf699763488 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=462aa47d42e057d2f34b3872a83cc35b 2500w" />
