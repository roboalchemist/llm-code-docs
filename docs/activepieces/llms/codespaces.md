# Source: https://www.activepieces.com/docs/build-pieces/misc/codespaces.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Codespaces

GitHub Codespaces is a cloud development platform that enables developers to write, run, and debug code directly in their browsers, seamlessly integrated with GitHub.

### Steps to setup Codespaces

1. Go to [Activepieces repo](https://github.com/activepieces/activepieces).

2. Click Code `<>`, then under codespaces click create codespace on main.

<img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=94470febd82b0491474e2481124eb562" alt="Create Codespace" data-og-width="1383" width="1383" data-og-height="713" height="713" data-path="resources/screenshots/development-setup_codespaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=cf33e942541fe257384bffa8377fee1b 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=30bc1ed998e1bab3390af5dc8f54306e 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=da78115808fa2ff1ea5d2131ba47c668 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=99b94406446bb4a1147d765f5777baf5 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=eff55aa6bc1a1d34943e9a2c3723d95b 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/development-setup_codespaces.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=092a5f882369bd1b2ce25b92487d179d 2500w" />

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/build-pieces/building-pieces/development-setup#pieces-development) section.
</Note>

3. Open the terminal and run `npm start`

4. Access the frontend URL by opening port 4200 and signing in with these details:

Email: `dev@ap.com`
Password: `12345678`
