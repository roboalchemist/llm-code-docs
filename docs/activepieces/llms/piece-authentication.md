# Source: https://www.activepieces.com/docs/build-pieces/building-pieces/piece-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Piece Authentication

### Piece Authentication

Activepieces supports multiple forms of authentication, you can check those forms [here](../piece-reference/authentication)

Now, let's establish authentication for this piece, which necessitates the inclusion of an API Key in the headers.

Modify `src/index.ts` file to add authentication,

```ts  theme={null}
import { PieceAuth, createPiece } from '@activepieces/pieces-framework';

export const gelatoAuth = PieceAuth.SecretText({
  displayName: 'API Key',
  required: true,
  description: 'Please use **test-key** as value for API Key',
});

export const gelato = createPiece({
  displayName: 'Gelato',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  auth: gelatoAuth,
  authors: [],
  actions: [],
  triggers: [],
});
```

<Note>
  Use the value **test-key** as the API key when testing actions or triggers for
  Gelato.
</Note>
