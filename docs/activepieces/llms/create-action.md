# Source: https://www.activepieces.com/docs/build-pieces/building-pieces/create-action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Action

## Action Definition

Now let's create first action which fetch random ice-cream flavor.

```bash  theme={null}
npm run cli actions create
```

You will be asked three questions to define your new piece:

1. `Piece Folder Name`: This is the name associated with the folder where the action resides. It helps organize and categorize actions within the piece.
2. `Action Display Name`: The name users see in the interface, conveying the action's purpose clearly.
3. `Action Description`: A brief, informative text in the UI, guiding users about the action's function and purpose.
   Next, Let's create the action file:

**Example:**

```bash  theme={null}
npm run cli actions create

? Enter the piece folder name : gelato
? Enter the action display name : get icecream flavor
? Enter the action description : fetches random icecream flavor.
```

This will create a new TypeScript file named `get-icecream-flavor.ts` in the `packages/pieces/community/gelato/src/lib/actions` directory.

Inside this file, paste the following code:

```typescript  theme={null}
import {
  createAction,
  Property,
  PieceAuth,
} from '@activepieces/pieces-framework';
import { httpClient, HttpMethod } from '@activepieces/pieces-common';
import { gelatoAuth } from '../..';

export const getIcecreamFlavor = createAction({
  name: 'get_icecream_flavor', // Must be a unique across the piece, this shouldn't be changed.
  auth: gelatoAuth,
  displayName: 'Get Icecream Flavor',
  description: 'Fetches random icecream flavor',
  props: {},
  async run(context) {
    const res = await httpClient.sendRequest<string[]>({
      method: HttpMethod.GET,
      url: 'https://cloud.activepieces.com/api/v1/webhooks/RGjv57ex3RAHOgs0YK6Ja/sync',
      headers: {
        Authorization: context.auth, // Pass API key in headers
      },
    });
    return res.body;
  },
});
```

The createAction function takes an object with several properties, including the `name`, `displayName`, `description`, `props`, and `run` function of the action.

The `name` property is a unique identifier for the action. The `displayName` and `description` properties are used to provide a human-readable name and description for the action.

The `props` property is an object that defines the properties that the action requires from the user. In this case, the action doesn't require any properties.

The `run` function is the function that is called when the action is executed. It takes a single argument, context, which contains the values of the action's properties.

The `run` function utilizes the httpClient.sendRequest function to make a GET request, fetching a random ice cream flavor. It incorporates API key authentication in the request headers. Finally, it returns the response body.

## Expose The Definition

To make the action readable by Activepieces, add it to the array of actions in the piece definition.

```typescript  theme={null}
import { createPiece } from '@activepieces/pieces-framework';
// Don't forget to add the following import.
import { getIcecreamFlavor } from './lib/actions/get-icecream-flavor';

export const gelato = createPiece({
  displayName: 'Gelato',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  authors: [],
  auth: gelatoAuth,
  // Add the action here.
  actions: [getIcecreamFlavor], // <--------
  triggers: [],
});
```

# Testing

By default, the development setup only builds specific components. Open the file `packages/server/api/.env` and include "gelato" in the `AP_DEV_PIECES`.

For more details, check out the [Piece Development](./development-setup) section.

Once you edit the environment variable, restart the backend. The piece will be rebuilt. After this process, you'll need to **refresh** the frontend to see the changes.

<Tip>
  If the build fails, try debugging by running `npx nx run-many -t build --projects=gelato`.
  It will display any errors in your code.
</Tip>

To test the action, use the flow builder in Activepieces. It should function as shown in the screenshot.

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=fbe58632202341db74909ce0d5428767" alt="Gelato Action" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/screenshots/gelato-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=b665dbb041ff604d0ad7644b2ba1daeb 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=35c487dea20f54e739d8f4a5ef43df17 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=002ea216af3c68a37bb05bffdbf6dc8b 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=412e312b2d70f4717132afd994ecde04 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=7bf7cdbae9e5d6c7376a8b3ecb33069d 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/gelato-action.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=799c7211ce7bdc240960f0e15c1ac76c 2500w" />
