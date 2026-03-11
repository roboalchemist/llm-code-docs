# Source: https://docs.envzero.com/changelogs/2023/11/easy-oidc-authentication-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔐 Easy OIDC Authentication Integration

Usually to authorize yourself in a deployment in env0 you will need to create a deployment credential and assign that credential to the relevant project. That requires keeping long lived credentials in env0.\
To avoid that you can use OIDC credentials which are being generated per deployment so you can use short lived credentials. Now you can use OIDC credentials directly by creating an OIDC credential (which requires no sensitive data) and assign that credential to a project and all the setup for the deployment will be done.\
You will still need to configure the OIDC provider (AWS, Azure, GCP, Vault etc).\
Read more about it [here](/guides/integrations/oidc-integrations)

Built with [Mintlify](https://mintlify.com).
