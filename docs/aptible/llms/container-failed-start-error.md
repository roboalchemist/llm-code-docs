# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/container-failed-start-error.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Container Failed to Start Error

## Cause and Resolution

If you receive an error such as `Failed to start containers for ...`, this is usually indicative of one of the following issues:

* The [Container Command](/core-concepts/architecture/containers/overview#container-command) does not exist in your container. In this case, you should fix your `CMD` directive or [Procfile](/how-to-guides/app-guides/define-services) to reference a command that does exist.

* Your [Image](/core-concepts/apps/deploying-apps/image/overview) includes an `ENTRYPOINT`, but that `ENTRYPOINT` does not exist. In this case, you should fix your Image to use a valid `ENTRYPOINT`.

If neither is applicable to you, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for assistance.
