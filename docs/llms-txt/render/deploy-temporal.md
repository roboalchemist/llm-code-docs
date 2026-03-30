# Source: https://render.com/docs/deploy-temporal.md

# Deploy Temporal

[Temporal](https://temporal.io/) is a great way to manage asynchronous workflows. [Blueprints](blueprint-spec) make it effortless to deploy a production-ready Temporal cluster to Render!

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to deploy Temporal to Render.

<deploy-to-render repo="https://github.com/render-examples/temporal">
</deploy-to-render>

## Manual Deploy

1. Create a new repository using the `render-examples/temporal` [GitHub template](https://github.com/render-examples/temporal). The `render.yaml` blueprint defines the following components:

   - Temporal cluster:
     - A PostgreSQL database.
     - An Elasticsearch instance, for [advanced visibility](https://docs.temporal.io/docs/concepts/what-is-advanced-visibility/).
     - One [private service](private-services) for each Temporal service: frontend, matching, history, and worker.
     - The Temporal web UI.
   - Example app from [render-examples/sample-temporal-app](https://github.com/render-examples/sample-temporal-app):
     - `app-workflow-trigger` runs a simple HTTP server with two routes:
       - `/` for health checking.
       - `/trigger-workflow` for kicking off the `TransferMoney` workflow.
     - `app-worker` executes any triggered workflows.
       To plug in your own application code, replace the configuration for these two services.

1. Click the "Deploy to Render" button, and wait for your services to deploy.

1. To verify that your Temporal cluster is healthy, access the any of the four Temporal services (`temporal-frontend`, `temporal-history`, `temporal-matching`, or `temporal-worker`) using either the web shell or [SSH](ssh), and try these commands:

   ```shell{outputLines:2,4-100}
   tctl cluster health
   temporal.api.workflowservice.v1.WorkflowService: SERVING
   tctl admin membership list_gossip # lists all Temporal services. Below is expected, non-exact output:
   [
     {
       "role": "frontend",
       "member_count": 1,
       "members": [
         {
           "identity": "10.129.8.40:10000"
         }
       ]
     },
     {
       "role": "history",
       "member_count": 1,
       "members": [
         {
           "identity": "10.129.8.40:7234"
         }
       ]
     },
     {
       "role": "matching",
       "member_count": 1,
       "members": [
         {
           "identity": "10.129.8.40:7235"
         }
       ]
     },
     {
       "role": "worker",
       "member_count": 1,
       "members": [
         {
           "identity": "10.129.8.40:7239"
         }
       ]
     }
   ]
   ```

1. We will use the `app-workflow-trigger` service to trigger a Temporal workflow. Navigate to the `app-workflow-trigger` service page, and click on its public URL. Expect a plain text response that says "OK!".

1. To trigger a new workflow, append `/trigger-workflow` to the URL. Expected sample output:

   ```
   Transfer of $54.990002 from account 001-001 to account 002-002 is processing. ReferenceID: 2aef8b93-72ba-430f-9278-94281453ce59

   WorkflowID: transfer-money-workflow RunID: 4f700f58-98ba-4cbe-9488-bf0be65bf06d
   ```

1. To check that your `app-worker` service executed the workflow, you can navigate to its "Logs" page and see:

   [image: worker-logs]

## UI Access

Temporal ships with a [web UI](https://docs.temporal.io/docs/devtools/web-ui/) for viewing workflow executions. Rather than [configuring authentication](https://docs.temporal.io/docs/devtools/web-ui/#configuring-authentication), our Blueprint runs the UI as a private service called `temporal-ui`. You can use SSH port forwarding to securely access the service:

1. Configure [SSH](ssh) for your account, if you haven't already.
1. Navigate to the `temporal-ui` private service page, and copy the service address.
1. Navigate to the shell for the `app-worker` service, and copy the SSH address.
1. Start an SSH port forward from your local machine to the `temporal-ui` service via the `app-worker` service. If the `temporal-ui` service address is `temporal-ui-hpb3:8088` and the `app-worker` SSH address is `srv-c8vpm5g39ip9bkcn73tg@ssh.oregon.render.com`, then you would run this command to port forward the Temporal UI to `localhost:8088`:

   ```shell
   ssh -L 8088:temporal-ui-hpb3:8088 -NT srv-c8vpm5g39ip9bkcn73tg@ssh.oregon.render.com
   ```

1. Visit `http://localhost:8088` in a browser to see the executed workflows:

   [image: temporal-ui]

## External Access to Your Temporal Cluster

Our Temporal Blueprint assumes you have the flexibility to host both your
[Temporal
workers](https://docs.temporal.io/docs/temporal-explained/task-queues-and-workers/#workers)
and the application code where you trigger Temporal workflows on Render. With
this setup, all your components can communicate securely, using any protocol,
within a private network Render automatically configures for you. If you need
direct access to one of your private services, you can use the web shell or SSH,
as described above.

If you would prefer to host your workers or application code elsewhere,
consider using one of the following workarounds. A workaround is necessary
because Temporal uses [gRPC](https://grpc.io) and
[mTLS](https://docs.temporal.io/docs/server/security/#encryption-in-transit-with-mtls),
but Render doesn't yet have native support for gRPC and mTLS over external
connections.

### Extend Your Private Network with Tailscale

Deploy a [Tailscale subnet router](https://github.com/render-examples/tailscale)
to run in the same private network as your Temporal cluster. This allows you to
securely access your Render private services, using any protocol, from other
machines where you have Tailscale running. With this approach, you can run both
your workers and your application code somewhere other than Render, and still
connect to your Temporal cluster on Render using gRPC and mTLS.

### Deploy a REST to gRPC Proxy Server

For some use cases it may be impractical to install Tailscale alongside your
application code. This may apply, for example, if you'd like to trigger Temporal
workflows from serverless functions running outside of Render.

For these cases, consider deploying a [REST to gRPC proxy
server](https://github.com/render-examples/temporal-rest-proxy) alongside your
Temporal cluster on Render. This server exposes the Temporal workflow service as
a [collection of REST API
endpoints](https://temporal-rest-api-docs.onrender.com/), and is secured using
Bearer token authentication. With this approach, you still need to run your
workers on Render, but the application code that starts and interacts with
Temporal workflows can run anywhere.

Uncomment the `rest-to-grpc-proxy` [web service definition in the render.yaml
file](https://github.com/render-examples/temporal/blob/26b0dbcfc2c62b77b4b5f8bd8ebba888b534e38a/render.yaml#L264-L282), and
sync your corresponding Render Blueprint. Attach an `AUTH_TOKEN` environment
variable to the service. API requests must include this token in the
`Authorization` header. The repository includes a [sample javascript
client](https://github.com/render-examples/temporal-rest-proxy/blob/main/examples/client-js/index.js)
that demonstrates how to trigger workflow executions. It also includes an
[OpenAPI
schema](https://github.com/render-examples/temporal-rest-proxy/blob/main/server/generated/openapi/service.swagger.json)
that can be used to generate client bindings in your language of choice.

> This approach has not been tested at scale. Please perform
> your own tests before choosing it for production workloads.

## Alternatives

If you prefer to get started with a smaller Temporal deployment, check out [temporalio/temporal-render-simple](https://github.com/temporalio/temporal-render-simple). In this repository, Temporal is configured to run all four core services as a single Render service. While it could suffice for experimentation or low-load use cases, this configuration is not recommended for production: the Temporal components cannot be scaled independently, and the entire cluster can be taken down by failures on the `temporal` service.

If your Temporal cluster is deployed elsewhere, you can opt to run just your workers on Render, as [background workers](background-workers), and have them connect to the remote Temporal frontend service.

## Custom Autoscaling

The default autoscaling parameters offered in the `render-examples/temporal` example are based on CPU and memory. However, you might want to scale up or down your `app-worker` services (note that this is not referring to the `temporal-worker` service) programmatically, using the [Render API](https://api-docs.render.com/reference/scale-service). One way to do this would be to use the client-side `Schedule to Start` task latency metric to inform scaling decisions; you can find more information in this [Temporal community thread](https://community.temporal.io/t/strategies-for-scaling-aws-services/1577/7).