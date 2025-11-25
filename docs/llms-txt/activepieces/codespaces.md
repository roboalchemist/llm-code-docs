# Source: https://www.activepieces.com/docs/developers/development-setup/codespaces.md

# GitHub Codespaces

GitHub Codespaces is a cloud development platform that enables developers to write, run, and debug code directly in their browsers, seamlessly integrated with GitHub.

### Steps to setup Codespaces

1. Go to [Activepieces repo](https://github.com/activepieces/activepieces).

2. Click Code `<>`, then under codespaces click create codespace on main.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2228948ff3bf64691d9ff82072da37b2" alt="Create Codespace" data-og-width="1383" width="1383" data-og-height="713" height="713" data-path="resources/screenshots/development-setup_codespaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a4ad0df90c9bae41b9dc1037c74098b8 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e538e737312e98184bdd9d0c1ee76a41 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=189866428f49bd5cf73b93e6355e1d1c 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0e1257933c43de7b1837306618a7f275 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=863628159653952542cf694a26f9cd25 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8e09af5ec8413cc2e059eaa425bedebd 2500w" />

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/developers/development-setup/getting-started) section.
</Note>

3. Open the terminal and run `npm start`

4. Access the frontend URL by opening port 4200 and signing in with these details:

Email: `dev@ap.com`
Password: `12345678`
