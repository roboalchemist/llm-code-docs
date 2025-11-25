# Source: https://www.activepieces.com/docs/install/configuration/separate-workers.md

# Separate Workers from App

Benefits of separating workers from the main application (APP):

* **Availability**: The application remains lightweight, allowing workers to be scaled independently.
* **Security**: Workers lack direct access to Redis and the database, minimizing impact in case of a security breach.

<Steps>
  <Step title="Create Worker Token">
    To create a worker token, use the local CLI command to generate the JWT and sign it with your `AP_JWT_SECRET` used for the app server. Follow these steps:

    1. Open your terminal and navigate to the root of the repository.
    2. Run the command: `npm run workers token`.
    3. When prompted, enter the JWT secret (this should be the same as the `AP_JWT_SECRET` used for the app server).
    4. The generated token will be displayed in your terminal, copy it and use it in the next step.
       <img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=385159c04bb0a8add654f66efcf801ca" alt="Workers Token" data-og-width="1596" width="1596" data-og-height="186" height="186" data-path="resources/worker-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=280&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=e9afc1093ed882c2688803ec9963534c 280w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=560&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=579f183a1795dcc0c8f6f8c598b02781 560w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=840&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=7431803b6afe1b8929ad90010f60dc8d 840w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=1100&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=0598c948aa2735fabff5df63d6d2aea1 1100w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=1650&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=1cc59fff58465f5edac646a3f3ced201 1650w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=2500&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=8c72dc84eb5a54a7b53a756ea9e45727 2500w" />
  </Step>

  <Step title="Configure Environment Variables">
    Define the following environment variables in the `.env` file on the worker machine:

    * Set `AP_CONTAINER_TYPE` to `WORKER`
    * Specify `AP_FRONTEND_URL`
    * Provide `AP_WORKER_TOKEN`
  </Step>

  <Step title="Configure Persistent Volume">
    Configure a persistent volume for the worker to cache flows and pieces. This is important as first uncached execution of pieces and flows are very slow. Having a persistent volume significantly improves execution speed.

    Add the following volume mapping to your docker configuration:

    ```yaml  theme={null}
    volumes:
      - <your path>:/usr/src/app/cache
    ```

    Note: This setup works whether you attach one volume per worker, It cannot be shared across multiple workers.
  </Step>

  <Step title="Launch Worker Machine">
    Launch the worker machine and supply it with the generated token.
  </Step>

  <Step title="Verify Worker Operation">
    Verify that the workers are visible in the Platform Admin Console under Infra -> Workers.
    <img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=0156f35f93278e16e9a0f461cf3a2282" alt="Workers Infrastructure" data-og-width="1846" width="1846" data-og-height="1002" height="1002" data-path="resources/workers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=280&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=df0e889fac81ad27560d0eb42dd99c1b 280w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=560&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=686369eaa1c9d299c185dd90e66fe250 560w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=840&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=91dba13ef1a08af7feb9873afe874aab 840w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=1100&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=e826bd5fc83a83484a8bf18791eff058 1100w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=1650&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=60e0e99f7f110057e2b353a3dcc59bec 1650w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=2500&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=04fb7d7d3172c787634fcce9e1fae150 2500w" />
  </Step>

  <Step title="Configure App Container Type">
    On the APP machine, set `AP_CONTAINER_TYPE` to `APP`.
  </Step>
</Steps>
