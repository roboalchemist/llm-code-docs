# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/using-a-custom-image-in-an-agent/change-user-id.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing User Id

> Change the default user ID and group ID in the env zero self-hosted agent Docker image

Our default image use `node` user with `uid` and `gid` 1000.

If you want to change them, create a custom image with following commands:

```dockerfile Dockerfile theme={null}
FROM <IMAGE>:<TAG> # choose your base image

ARG USER_ID=1001210001
ARG GROUP_ID=2001210001
ENV USER_UID=${USER_ID}
ENV USER_GID=${GROUP_ID}

RUN apk add -U shadow \
    && usermod -u ${USER_ID} node \
    && groupmod -g ${GROUP_ID} node \
    && apk del -U shadow
```

When installing the agent add `runAsUser` and `runAsGroup` to helm `values.customer.yml`, not that `strictSecurityContext` must also be enabled to modify the `uid` and `gid`.

```yaml values.customer.yaml theme={null}
...
strictSecurityContext: true
runAsUser: "1002810011"
runAsGroup: "1002810011"
```

Built with [Mintlify](https://mintlify.com).
