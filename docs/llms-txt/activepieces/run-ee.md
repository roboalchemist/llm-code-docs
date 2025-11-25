# Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/run-ee.md

# Run Enterprise Edition

The enterprise edition requires a postgres and redis instance to run, and a license key to activate.

<Steps>
  <Step title="Run the dev container">
    Follow the instructions [here](/developers/development-setup/dev-container) to run the dev container.
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
    <img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=abc2db5befaabf039899a23fd75d9470" alt="Activation License Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/activation-license-key-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4a9e7f5cce1de95854a23131197452df 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f3aee8442dde13d03ae2ae978b1dd2f4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f6638ba4fa57d7256ec79d9e82ff55aa 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2bce94354609c5ee9d77656dd0490648 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e956a826e5d82a0e77a885ec6dfee2b0 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a9c2344b6be067b18b8367440d4cbf3c 2500w" />
  </Step>
</Steps>
