# Source: https://docs.baseten.co/development/chain/deploy.md

# Deploy

> Deploy your Chain on Baseten

Deploying a Chain is an atomic action that deploys every Chainlet
within the Chain. Each Chainlet specifies its own remote
environment — hardware resources, Python and system dependencies, autoscaling
settings.

### Development

The default behavior for pushing a chain is to create a development deployment:

```sh  theme={"system"}
truss chains push ./my_chain.py
```

Where `my_chain.py` contains the entrypoint Chainlet for your Chain.

Development deployments are intended for testing and can't scale past one
replica. Each time you make a development deployment, it overwrites the existing
development deployment.

Development deployments support rapid iteration with `watch` - see [above
guide](/development/chain/watch).

### 🆕 Environments

To deploy a Chain to an environment, run:

```sh  theme={"system"}
truss chains push ./my_chain.py --environment {env_name}
```

Environments are intended for live traffic and have access to full
autoscaling settings. Each time you deploy to an environment, a new deployment is
created. Once the new deployment is live, it replaces the previous deployment,
which is relegated to the published deployments list.
[Learn more](/deployment/environments) about environments.
