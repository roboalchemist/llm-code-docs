# Source: https://docs.portainer.io/2.33-lts/faqs/troubleshooting/logs-errors-and-debugging/why-cant-my-users-see-anything-in-the-environment-they-have-access-to.md

# Source: https://docs.portainer.io/sts/faqs/troubleshooting/logs-errors-and-debugging/why-cant-my-users-see-anything-in-the-environment-they-have-access-to.md

# Source: https://docs.portainer.io/faqs/troubleshooting/logs-errors-and-debugging/why-cant-my-users-see-anything-in-the-environment-they-have-access-to.md

# Why can't my users see anything in the environment they have access to?

For security reasons, all resources inside an environment are assigned only to the administrator by default. To give non-admin users access, you can either:

* Use the [access control tool](https://docs.portainer.io/advanced/access-control) within each resource to assign ownership to users.
* Make the resource public, so all users get access to it.
