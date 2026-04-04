# Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/run-ee.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Enterprise Edition

The enterprise edition requires a postgres and redis instance to run, and a license key to activate.

<Steps>
  <Step title="Run the dev container">
    Follow the instructions [here](/build-pieces/misc/dev-container) to run the dev container.
  </Step>

  <Step title="Add the following env variables in `server/api/.env`">
    Pase the following env variables in `server/api/.env`

    ```bash  theme={null}
    ## these variables are set to align with the .devcontainer/docker-compose.yml file
    AP_DB_TYPE=POSTGRES
    AP_DEV_PIECES="your_piece_name"
    AP_ENVIRONMENT="dev"
    AP_EDITION=ee
    AP_EXECUTION_MODE=UNSANDBOXED
    AP_FRONTEND_URL="http://localhost:4200"
    AP_WEBHOOK_URL="http://localhost:3000"
    AP_PIECES_SOURCE='FILE'
    AP_PIECES_SYNC_MODE='NONE'
    AP_LOG_LEVEL=debug
    AP_LOG_PRETTY=true
    AP_REDIS_HOST="redis"
    AP_REDIS_PORT="6379"
    AP_TRIGGER_DEFAULT_POLL_INTERVAL=1
    AP_CACHE_PATH=/workspace/cache
    AP_POSTGRES_DATABASE=activepieces
    AP_POSTGRES_HOST=db
    AP_POSTGRES_PORT=5432
    AP_POSTGRES_USERNAME=postgres
    AP_POSTGRES_PASSWORD=A79Vm5D4p2VQHOp2gd5
    AP_ENCRYPTION_KEY=427a130d9ffab21dc07bcd549fcf0966
    AP_JWT_SECRET=secret
    ```
  </Step>

  <Step title="Activate Your License Key">
    After signing in, activate the license key by going to **Platform Admin -> Setup -> License Keys**
    <img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=55f06c585c932ff6b532e38740b9d141" alt="Activation License Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/activation-license-key-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=0cb0fb8b1d31b975b82ea3e1434e9b74 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=cb31fd68ee358724626ffc349c9cf45e 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=f4f64622121073403d2bebdb05d3daad 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=afbbe4d28a784b792b4a55ddf2f0001d 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=44249715eec7fecd4c9b45c19517df08 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/activation-license-key-settings.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=300627457e14ab17abfed9ca7eb8e8f7 2500w" />
  </Step>
</Steps>
