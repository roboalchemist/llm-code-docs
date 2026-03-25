# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/services/manage-images.md

# Working with image registries and repositories

Snowpark Container Services provides an [OCIv2](https://github.com/opencontainers/distribution-spec/blob/main/spec.md)-compliant image registry service and a storage unit call repository to store images. You can use the following Snowflake CLI commands to manage Snowpark Container Services image registries and repositories:

* Manage image registries
* Manage image repositories

For more information about Snowpark Container Services image registries and repositories, see [Snowpark Container Services: Working with an image registry and repository](../../snowpark-container-services/working-with-registry-repository.md).

## Manage image registries

Snowflake CLI lets you perform the following tasks with Snowpark Container Services image repositories:

* Get environment tokens for registry authentication
* Log in to an image registry
* Retrieve the URL for an image registry

For common operations, such as listing or dropping, Snowflake CLI uses `snow object` commands as described in [Managing Snowflake objects](../objects/manage-objects.md).

### Get environment tokens for registry authentication

You can use the [snow spcs image-registry token](../command-reference/spcs-commands/image-registry-commands/token.md) command to return the token associated with the specified
connection that you can use to authenticate with the registry.

```snowcli
snow spcs image-registry token --connection mytest
```

```output
+----------------------------------------------------------------------------------------------------------------------+
| key        | value                                                                                                   |
|------------+---------------------------------------------------------------------------------------------------------|
| token      | ****************************************************************************************************    |
|            | ****************************************************************************************************    |
| expires_in | 3600                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+
```

You can then use that token to log in to a Docker container by piping it to the `docker login` command, similar to the following:

```snowcli
snow spcs image-registry token --format=JSON | docker login <org>-<account>.registry.snowflakecomputing.com -u 0sessiontoken --password-stdin
```

### Log in to an image registry

The [snow spcs image-registry login](../command-reference/spcs-commands/image-registry-commands/login.md) logs you into an image repository with the credentials specified for your connection. Before logging in, you must meet the following prerequisites:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed because the command uses docker to log in to Snowflake.
* The current role must have READ privileges for the image repository in the account to get the registry URL.

To log in to an image registry with your account credentials, use the following:

```snowcli
snow spcs image-registry login
```

```output
Login Succeeded
```

### Retrieve the URL for an image registry

The [snow spcs image-registry url](../command-reference/spcs-commands/image-registry-commands/url.md) command returns a URL for an image repository. The current role must have READ privileges for the image repository in the account to get the registry URL.

To get the URL for a repository, do the following:

```snowcli
snow spcs image-registry url
```

```output
<orgname-acctname>.registry.snowflakecomputing.com
```

## Manage image repositories

Snowflake CLI lets you perform the following tasks with Snowpark Container Services image repositories:

* Create an image repository
* Create and deploy an image repository from a project definition
* Retrieve the URL for an image repository
* List tags and images in an image repository

For common operations, such as listing or dropping, Snowflake CLI uses `snow object` commands as described in [Managing Snowflake objects](../objects/manage-objects.md).

### Create an image repository

The [snow spcs image-repository create](../command-reference/spcs-commands/image-repository-commands/create.md) command creates a new image repository in the current schema.

To create an image repository, enter a command similar to the following:

```snowcli
snow spcs image-repository create tutorial_repository
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

### Create and deploy an image repository from a project definition

You can deploy an image repository to a stage by creating a `snowflake.yml` project definition file and executing the `snow spcs image-repository deploy` command.

The following shows a sample `snowflake.yml` project definition file:

```yaml
definition_version: 2
entities:
  my_image_repository:
    type: image-repository
    identifier: my_image_repository
```

The following table describes the properties of a compute pool project definition.

Image repository project definition properties

| Property | Definition |
| --- | --- |
| **type**  *required*, *string* | Must be `image-repository`. |
| **identifier**  *optional*, *string* | Snowflake identifier for the entity. The value can have the following forms:   *String identifier text  ```yaml   identifier: my-image-repository```  Both unquoted and quoted identifiers are supported. To use quoted identifiers, include the surrounding quotes in the YAML value (for example, `"My Image Repository"`).* Object  ```yaml   identifier:     name: my-image-repository     schema: my-schema # optional     database: my-db # optional```  **Note:** An error occurs if you specify a `schema` or `database` and use a fully qualified name in the `name` property (such as `mydb.schema1.my-app`). |

To create and deploy the image repository, do the following:

1. Change your current directory to the directory containing the project definition file.
2. Run a `snow spcs image-repository deploy` command similar to the following:

   ```snowcli
   snow spcs image-repository deploy
   ```

   ```output
   +---------------------------------------------------------------------+
   | key    | value                                                      |
   |--------+------------------------------------------------------------|
   | status | Image Repository MY_IMAGE_REPOSITORY successfully created. |
   +---------------------------------------------------------------------+
   ```

### Retrieve the URL for an image repository

The [snow spcs image-repository url](../command-reference/spcs-commands/image-repository-commands/url.md) command gets the URL for an image repository.

To get the URL, enter a command similar to the following:

```snowcli
snow spcs image-repository url tutorial_repository
```

```output
<orgname-acctname>.registry.snowflakecomputing.com/tutorial_db/data_schema/tutorial_repository
```

### List tags and images in an image repository

The [snow spcs image-repository list-images](../command-reference/spcs-commands/image-repository-commands/list-images.md) command lets you get the images and tags for an image repository.

To list the images and tags in a repository, enter a command similar to the following, which lists the images in a repository named `images` in the `my_db` database:

```snowcli
snow spcs image-repository list-images images --database my_db
```

```output
+----------------------------+---------------+---------+-------------------------------------------------+-----------------------------------------+
| created_on                 | image_name    | tags    | digest                                          | image_path                              |
|----------------------------+---------------+---------+-------------------------------------------------+-----------------------------------------|
| 2024-10-11 14:23:49-07:00  | echo_service  | latest  | sha256:a8a001fef406fdb3125ce8e8bf9970c35af7084  | my_db/test_schema/images/echo_service:  |
|                            |               |         | fc33b0886d7a8915d3082c781                       | latest                                  |
| 2024-10-14 22:21:14-07:00  | test_counter  | latest  | sha256:8cae96dac29a4a05f54bb5520003f964baf67fc  | my_db/test_schema/images/test_counter:  |
|                            |               |         | 38dcad3d2c85d6c5aa7381174                       | latest                                  |
+----------------------------+---------------+---------+-------------------------------------------------+-----------------------------------------+
```
