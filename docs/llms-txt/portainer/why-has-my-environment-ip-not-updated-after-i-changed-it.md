# Source: https://docs.portainer.io/2.33-lts/faqs/troubleshooting/agents-and-environment-management/why-has-my-environment-ip-not-updated-after-i-changed-it.md

# Source: https://docs.portainer.io/sts/faqs/troubleshooting/agents-and-environment-management/why-has-my-environment-ip-not-updated-after-i-changed-it.md

# Source: https://docs.portainer.io/faqs/troubleshooting/agents-and-environment-management/why-has-my-environment-ip-not-updated-after-i-changed-it.md

# Why has my Environment IP not updated after I changed it?

If you have updated your Portainer Agent environment's IP address, you may not see the update apply correctly in your Portainer Server instance. To resolve this, restart your Portainer Server container.

Assuming you have followed our [install instructions](https://docs.portainer.io/start/install/server), you can do this from the command line:

On Docker Standalone:

```
docker restart portainer
```

On Docker Swarm:

```
docker service update --force portainer_portainer
```

On Kubernetes:

```
kubectl -n portainer rollout restart deployment.apps/portainer
```
