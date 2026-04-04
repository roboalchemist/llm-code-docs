# Source: https://www.activepieces.com/docs/install/guides/separate-workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Separate Workers

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
       <img src="https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=7d8f5c27a14fea432cd609425a90b88d" alt="Workers Token" data-og-width="1596" width="1596" data-og-height="186" height="186" data-path="resources/worker-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=280&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=872b51a7b56302bb16d618d01d4bb658 280w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=560&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=0c65ce418261a61c157063976012a131 560w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=840&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=9693d26d7bead5ab7c6f64abcf025542 840w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=1100&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=d4412f91e5557b27146e275718629acc 1100w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=1650&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=64cb37507fb9f1516760088096701271 1650w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/worker-token.png?w=2500&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=79dcd1811ff4f113e88f53a0fae16267 2500w" />
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
    <img src="https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=cd152896f3be11a1d7f8e6b118102172" alt="Workers Infrastructure" data-og-width="1846" width="1846" data-og-height="1002" height="1002" data-path="resources/workers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=280&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=70c252702c00d85996a76d431911ca1e 280w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=560&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=2253c77b1d6c98ce8f86cb2781cd00b0 560w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=840&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=a461e77fc3c8b90a70a7385d6b4a8af2 840w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=1100&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=ad39850d39bfc56fa94be86e346d3deb 1100w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=1650&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=e5b08443784b7ae964d2f7702adf62d7 1650w, https://mintcdn.com/activepieces/htEDiTsZNK_UML_C/resources/workers.png?w=2500&fit=max&auto=format&n=htEDiTsZNK_UML_C&q=85&s=e983a049af328d7844ad43deb23a269c 2500w" />
  </Step>

  <Step title="Configure App Container Type">
    On the APP machine, set `AP_CONTAINER_TYPE` to `APP`.
  </Step>
</Steps>
