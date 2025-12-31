# Source: https://www.activepieces.com/docs/build-pieces/building-pieces/development-setup.md

# Development setup

## Prerequisites

* Node.js v18+
* npm v9+

## Instructions

1. Setup the environment

```bash  theme={null}
node tools/setup-dev.js
```

2. Start the environment

This command will start activepieces with sqlite3 and in memory queue.

```bash  theme={null}
npm start
```

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/build-pieces/building-pieces/development-setup#pieces-development) section.
</Note>

3. Go to ***localhost:4200*** on your web browser and sign in with these details:

Email: `dev@ap.com`
Password: `12345678`

## Pieces Development

When [`AP_SYNC_MODE`](https://github.com/activepieces/activepieces/blob/main/packages/server/api/.env#L17) is set to `OFFICIAL_AUTO`, all pieces are automatically loaded from the cloud API and synced to the database on first launch. This process may take a few seconds to several minutes depending on your internet connection.

For local development, pieces are loaded from your local `dist` folder instead of the database. To enable this, set the [`AP_DEV_PIECES`](https://github.com/activepieces/activepieces/blob/main/packages/server/api/.env#L4) environment variable with a comma-separated list of pieces. For example, to develop with `google-sheets` and `cal-com`:

```sh  theme={null}
AP_DEV_PIECES=google-sheets,cal-com npm start
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.activepieces.com/docs/llms.txt