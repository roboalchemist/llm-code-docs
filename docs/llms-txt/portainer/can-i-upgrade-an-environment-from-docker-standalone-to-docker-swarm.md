# Source: https://docs.portainer.io/2.33-lts/faqs/upgrading/can-i-upgrade-an-environment-from-docker-standalone-to-docker-swarm.md

# Source: https://docs.portainer.io/sts/faqs/upgrading/can-i-upgrade-an-environment-from-docker-standalone-to-docker-swarm.md

# Source: https://docs.portainer.io/faqs/upgrading/can-i-upgrade-an-environment-from-docker-standalone-to-docker-swarm.md

# Can I upgrade an environment from Docker Standalone to Docker Swarm?

We do not recommend upgrading existing Docker Standalone environments to Docker Swarm because you will lose your stacks. We do support migrating a stack from one environment to another.

Our recommended approach is to:

1. Add the Docker Swarm environment to your Portainer installation.
2. Migrate your stacks over to the new environment.
