# Source: https://www.activepieces.com/docs/developers/development-setup/local.md

# Local Dev Environment

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

  For more details, check out the [Piece Development](/developers/development-setup/getting-started) section.
</Note>

3. Go to ***localhost:4200*** on your web browser and sign in with these details:

Email: `dev@ap.com`
Password: `12345678`
