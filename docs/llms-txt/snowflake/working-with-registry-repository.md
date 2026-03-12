# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-registry-repository.md

# Snowpark Container Services: Working with an image registry and repository

Snowpark Container Services provides an
[OCIv2](https://github.com/opencontainers/distribution-spec/blob/main/spec.md)-compliant image registry service and a storage unit call repository to store images.

## Image registry

The image registry service serves the OCIv2 API for storing OCI-compliant container images.

## Image registry hostname

Each image registry in a Snowflake account has a unique hostname, which allows OCI clients
(such as Docker CLI) to access an image registry using REST API calls.
The general syntax for an image registry hostname is:

```output
<orgname>-<acctname>.registry.snowflakecomputing.com
```

In the hostname:

* `<orgname>-<acctname>` identifies a Snowflake account.
* `registry` allows Snowflake to provide hostnames
  per account for registry customers.

  The hostname is always all lowercase.

> **Note:**
>
> A Snowflake account name (`<acctname>`) can have an underscore
> (for example, `my_account`), but underscores are not valid in a URL.
> Therefore, when using a registry hostname, you need to replace an underscore
> with a dash. For example, change `my_account` to `my-account`.

You can find your organization name and account name information for image
repository host names in one of the following ways:

* The Snowsight web interface: Use the account selector. For more information, see [Getting started with Snowsight](../../user-guide/ui-snowsight-gs.md).
* Execute the [SHOW IMAGE REPOSITORIES](../../sql-reference/sql/show-image-repositories.md) command.

## Image registry authentication

To access an image repository in your Snowflake account, users must authenticate to the image registry using their Snowflake credentials. Additionally, appropriate privileges are required to access repositories within the registry. To obtain these privileges, a user must have a role that grants access privileges to the repository.

You have the following options to authenticate your client with an image registry in your account:

* **Use Snowflake CLI:** The Snowflake CLI supports all forms of Snowflake authentication.

  * For the Docker client, use the [snow spcs image-registry login](../snowflake-cli/command-reference/spcs-commands/image-registry-commands/login.md) command to authenticate Docker with a registry.
  * For any client (including Docker), Snowflake CLI also provides the option to first generate an authentication token and use it to authenticate the client. For more information, see [snow spcs image-registry token](../snowflake-cli/command-reference/spcs-commands/image-registry-commands/token.md).
* **Use client-provided commands:** Tools like Docker offer commands to authenticate with a registry by using a username and password.
  There are several ways to use username and password authentication with external tools:

  * Instead of using your own username and password, you can use a [programmatic access token (PAT)](../../user-guide/programmatic-access-tokens.md). First, [generate a token](../../user-guide/programmatic-access-tokens.md), then use it with a tool — such as Docker — by providing “USER” as the username and the token as the password.
  * You can also provide your Snowflake username and password, but this is only allowed if your account administrator enables username/password authentication. By default, username/password login isn’t supported without multi-factor authentication (MFA), which is incompatible with the `docker login` command.

## Image repository

A *registry* is a service that serves the OCIv2 API, and a *repository* is a
storage unit that you create within the service.

A repository is a named location in your account where you store images.
This is similar to the relationship between a DBMS and a table within the DBMS.
That is, a DBMS is equivalent to a registry, and a table is equivalent to a repository.

You can create one or more repositories in your Snowflake account. For example,
DEV, TEST, and PROD repositories can store images during development, testing,
and production. You can also create repositories that have different
permissions; for example, some repositories may be read-only for some roles.

Access control is supported at the repository level;
individual image-level access control is not supported.

For uploading images to an image repository, the registry service offers various authentication options and single sign-on (SSO).

For an example of creating a repository and uploading an image, see [Tutorial 1](tutorials/tutorial-1.md).

## Image repository URL

The following is a general syntax for a Snowflake repository URL:

```output
<registry-hostname>/<db_name>/<schema_name>/<repository_name>
```

For example,

```output
myorg-myacct.registry.snowflake.com/my_db/my_schema/my_repository
```

To look up the repository URL in your account, use the SHOW IMAGE REPOSITORIES
SQL command.

> **Note:**
>
> * Snowflake URL-encodes the $ character, which is the only non-URL
>   character Snowflake supports in identifiers
>   (See [Identifier Requirements](../../sql-reference/identifiers-syntax.md)).
>   Double-quoted names that contain special characters are not supported.
> * When you manually construct a repository URL, replace an underscore in an account
>   name (`my_acct`) with a dash (`my-acct`).

### Repository operations

To create and manage repositories, Snowflake supports the following
[repository operations](../../sql-reference/commands-snowpark-container-services.md):

* [CREATE IMAGE REPOSITORY](../../sql-reference/sql/create-image-repository.md)
* [DROP IMAGE REPOSITORY](../../sql-reference/sql/drop-image-repository.md)
* [SHOW IMAGE REPOSITORIES](../../sql-reference/sql/show-image-repositories.md)

To list images stored within a Snowflake image repository, use the following command:

* [SHOW IMAGES IN IMAGE REPOSITORY](../../sql-reference/sql/show-images-in-image-repository.md)

For an example of creating a repository and uploading an image,
see [Tutorial Common Setup](tutorials/common-setup.md).

### Repository privileges

When you work with a repository, the following privilege model applies:

* To create a repository in a schema, you must have the
  CREATE IMAGE REPOSITORY privilege on the schema.
* For repository management, the following privileges (capabilities)
  are supported:

  | Privilege | Usage |
  | --- | --- |
  | READ | Enables listing and downloading images from a repository. |
  | WRITE | Enables listing and downloading images from a repository. You can also push images in the repository. |
  | OWNERSHIP | Enables listing and downloading images from a repository. You can also push images in the repository. |
  | SERVICE READ | Enables a container service to list and download images from a repository. This is needed for the image building step of [model serving](../snowflake-ml/inference/real-time-inference-rest-api.md). |
  | SERVICE WRITE | Enables a container service to push images in the repository. This is needed for the image building step of [model serving](../snowflake-ml/inference/real-time-inference-rest-api.md). |

## Guidelines and Limitations

* Dropping images from a repository is currently not supported. You can drop a repository, but that removes all images from that repository.
* Contact your account representative if you require inbound private connectivity.
* The maximum layer size permitted for an image registry in compressed format is 160 GiB for Snowflake accounts on AWS, and 195 GiB for Snowflake accounts on Azure.
