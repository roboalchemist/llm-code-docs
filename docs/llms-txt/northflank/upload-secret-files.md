# Source: https://northflank.com/docs/v1/application/secure/upload-secret-files.md

# Upload secret files

You can upload secret files to mount within your containers. They can be used to:

- make configuration files available within your services, jobs and builds

- create text based configuration files like `.json`, `.html`, `.css`, `.yaml`

- add certificate files or complex secrets that cannot be handled by environment variables

- create manifest files with build or runtime variable configuration

Secret files are equivalent to [Kubernetes' ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) and [Docker file volumes](https://docs.docker.com/storage/volumes/).

Each secret file must have a unique path where it will be mounted, and some file content. You can use [dynamic templating](inject-secrets#dynamic-templating) (in the format `${ENV_KEY}`) to substitute environment variables into your secret files.

Secret files are encrypted at rest and injected at runtime or build time.

> [!note] Secret file permissions
> Secret files will be owned by the user and group `root` in your container. You may need to add a shell script to change the [ownership or permissions](https://northflank.com/docs/v1/application/run/run-as-a-different-user#change-file-ownership-and-permissions).

## Add a secret file

You can add a secret file to a service or job from the environment or build arguments pages, to add a file to be available at runtime or build respectively.

Click add file to manually enter the file content, or upload from your local filesystem. Enter the mount path, where your file will be located in the container filesystem, and either repeat to add more files or save changes.

You can also add secret files in the same way to a [secret group](manage-secret-groups), which will be made available in any services or jobs that inherit from that secret group.

![Uploading a secret file in the Northflank application](https://assets.northflank.com/documentation/v1/application/secure/upload-secret-files/secret-file-editor.png)

### Access secret files in builds

Secret files in builds are injected relative to the repository root, unlike secret files in deployed containers which are injected relative to the build root.

Secret files in builds also cannot overwrite files in the repository, for example a repository with `data/config.json` would fail to build if you added a secret file with the path `/data/config.json`.

If you reference a secret file in your Dockerfile it is relative to the build context, not the container root. This also means that the secret file path needs to take the build context into account when you add the file to Northflank.

If you want to access a secret file while using the build context `/frontend` the file path must be set to `/frontend/data/config.json`. You can make the file available under this path by specifying `COPY ./data/config.json .` in the Dockerfile.

The table below gives examples of how a path would be set and accessed in various contexts:

| Secret file mount path | Build context | Secret file relative to build context | Dockerfile COPY example | File location in build after `WORKDIR app; COPY ${file} .` |
| --- | --- | --- | --- | --- |
| `/secrets/my-secret` | `/` | `./secrets/my-secret` | `COPY ./secrets/my-secret .` | `/app/my-secret` |
| `/secrets/my-secret` | `/frontend` | `secret outside of build context` | `secret outside of build context` | `secret outside of build context` |
| `/frontend/secrets/my-secret` | `/frontend` | `./secrets/my-secret` | `COPY ./secrets/my-secret .` | `/app/my-secret` |

## Edit a secret file

You can  edit or  delete existing secret files by finding them in the relevant service, job, or secret group.

## Next steps

- [Inject secrets: Set build arguments and inject runtime variables into running deployments.](/v1/application/secure/inject-secrets)
- [Manage groups of secrets: Create and manage groups of secrets that can be inherited throughout an entire project or by specific services and jobs.](/v1/application/secure/manage-secret-groups)
- [Execute files in a container: Make files and directories in your containers executable.](/v1/application/run/run-as-a-different-user#change-file-ownership-and-permissions)
