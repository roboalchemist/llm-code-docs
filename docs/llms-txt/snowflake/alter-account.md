# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-account.md

# ALTER ACCOUNT

Modifies an account. The ALTER ACCOUNT command has two purposes:

* Allows account administrators (that is, users with the ACCOUNTADMIN role) to modify [parameters](../parameters.md) and
  other settings at the account level. For example, the account administrator can set the resource monitor or enable a security feature for
  an account. For these actions, the account administrator executes ALTER ACCOUNT from the account being modified.
* Allows [organization administrators](../../user-guide/organization-administrators.md) to modify core characteristics of an account. For example, the
  organization administrator can rename an account. For these actions, the organization administrator executes ALTER ACCOUNT from a
  different account than the one being modified.

> **Note:**
>
> While ALTER ACCOUNT is primarily executed by account administrators and organization administrators, users with the SECURITYADMIN
> role can use it to set the network policy for the account.

## Syntax

The syntax for ALTER ACCOUNT varies depending on whether you are modifying the current account or a different account.

### Altering the current account

```sqlsyntax
ALTER ACCOUNT SET { [ accountProperties ] | [ accountParams ] | [ objectParams ] | [ sessionParams ] }

ALTER ACCOUNT UNSET <param_name> [ , ... ]

ALTER ACCOUNT SET RESOURCE_MONITOR = <monitor_name>

ALTER ACCOUNT ADD ORGANIZATION USER GROUP <group_name>
ALTER ACCOUNT REMOVE ORGANIZATION USER GROUP <group_name>

ALTER ACCOUNT SET { AUTHENTICATION | SESSION } POLICY <policy_name> [ { FOR ALL PERSON USERS | FOR ALL SERVICE USERS } ] [ FORCE ]

ALTER ACCOUNT UNSET { AUTHENTICATION | SESSION } POLICY [ { FOR ALL PERSON USERS | FOR ALL SERVICE USERS } ]

ALTER ACCOUNT SET FEATURE POLICY <policy_name> FOR ALL APPLICATIONS [ FORCE ]

ALTER ACCOUNT UNSET FEATURE POLICY FOR ALL APPLICATIONS

ALTER ACCOUNT SET MAINTENANCE POLICY <policy_name> [ FORCE ] FOR ALL APPLICATIONS

ALTER ACCOUNT UNSET MAINTENANCE POLICY FOR ALL APPLICATIONS

ALTER ACCOUNT SET { PACKAGES | PASSWORD } POLICY <policy_name> [ FORCE ]

ALTER ACCOUNT UNSET { PACKAGES | PASSWORD } POLICY

ALTER ACCOUNT SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER ACCOUNT UNSET TAG <tag_name> [ , <tag_name> ... ]
```

Where:

```sqlsyntax
accountProperties ::=
    LOGIN_IDP_REDIRECT = ( <interface> = <security_integration> [ , ... ] )
    OBJECT_VISIBILITY = { <object_visibility_spec> | PRIVILEGED }
```

```sqlsyntax
accountParams ::=
  ALLOW_ID_TOKEN = TRUE | FALSE
  ALLOWED_SPCS_WORKLOAD_TYPES = { '<list_of_workload_types>' | 'ALL' }
  CLIENT_ENCRYPTION_KEY_SIZE = <integer>
  CORTEX_ENABLED_CROSS_REGION = { 'DISABLED' | 'ANY_REGION' | '<list_of_regions>' }
  DISALLOWED_SPCS_WORKLOAD_TYPES = { '<list_of_workload_types>' | 'ALL' }
  DISABLE_USER_PRIVILEGE_GRANTS = TRUE | FALSE
  DEFAULT_DBT_VERSION = { '<version>' }
  ENABLE_EGRESS_COST_OPTIMIZER = TRUE | FALSE
  ENABLE_INTERNAL_STAGES_PRIVATELINK = TRUE | FALSE
  ENFORCE_NETWORK_RULES_FOR_INTERNAL_STAGES = TRUE | FALSE
  ENABLE_NOTEBOOK_CREATION_IN_PERSONAL_DB = TRUE | FALSE
  ENABLE_SPCS_BLOCK_STORAGE_SNOWFLAKE_FULL_ENCRYPTION_ENFORCEMENT = TRUE | FALSE
  EXTERNAL_OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST = TRUE | FALSE
  INITIAL_REPLICATION_SIZE_LIMIT_IN_TB = <num>
  LISTING_AUTO_FULFILLMENT_REPLICATION_REFRESH_SCHEDULE = <schedule>
  LLM_INFERENCE_PARSE_DOCUMENT_PRESIGNED_URL_EXPIRY_SECONDS = <integer>
  NETWORK_POLICY = <string>
  OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST = TRUE | FALSE
  PERIODIC_DATA_REKEYING = TRUE | FALSE
  READ_CONSISTENCY_MODE = 'SESSION' | 'GLOBAL'
  REQUIRE_STORAGE_INTEGRATION_FOR_STAGE_CREATION = TRUE | FALSE
  REQUIRE_STORAGE_INTEGRATION_FOR_STAGE_OPERATION = TRUE | FALSE
  SAML_IDENTITY_PROVIDER = <json_object>
  SQL_TRACE_QUERY_TEXT = ON | OFF
  SSO_LOGIN_PAGE = TRUE | FALSE
  USE_WORKSPACES_FOR_SQL = { 'always' | 'never' }
```

```sqlsyntax
objectParams ::=
  BASE_LOCATION_PREFIX = '<string>'
  CATALOG = <catalog_integration_name>
  CATALOG_SYNC = '<snowflake_open_catalog_integration_name>'
  CORTEX_MODELS_ALLOWLIST = {'<list_of_models>' | 'ALL' | 'NONE'}
  DATA_RETENTION_TIME_IN_DAYS = <integer>
  DEFAULT_DDL_COLLATION = '<collation_specification>'
  DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU = <compute_pool_name>
  DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU = <compute_pool_name>
  DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE = <warehouse_name>
  ENABLE_DATA_COMPACTION = { TRUE | FALSE }
  ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE }
  ENABLE_TAG_PROPAGATION_EVENT_LOGGING = TRUE | FALSE
  ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR = TRUE | FALSE
  ENABLE_UNREDACTED_SECURE_OBJECT_ERROR = TRUE | FALSE
  EVENT_TABLE = <string>
  EXTERNAL_VOLUME = <external_volume_name>
  ICEBERG_VERSION_DEFAULT = <integer>
  LOG_LEVEL = <string>
  MAX_CONCURRENCY_LEVEL = <num>
  MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer>
  METRIC_LEVEL = <string>
  NETWORK_POLICY = <string>
  PIPE_EXECUTION_PAUSED = TRUE | FALSE
  PREVENT_UNLOAD_TO_INLINE_URL = TRUE | FALSE
  PREVENT_UNLOAD_TO_INTERNAL_STAGES = TRUE | FALSE
  REPLACE_INVALID_CHARACTERS = TRUE | FALSE
  STATEMENT_QUEUED_TIMEOUT_IN_SECONDS = <num>
  STATEMENT_TIMEOUT_IN_SECONDS = <num>
  STORAGE_SERIALIZATION_POLICY = COMPATIBLE | OPTIMIZED
  TRACE_LEVEL = <string>
```

```sqlsyntax
sessionParams ::=
  ABORT_DETACHED_QUERY = TRUE | FALSE
  AUTOCOMMIT = TRUE | FALSE
  BINARY_INPUT_FORMAT = <string>
  BINARY_OUTPUT_FORMAT = <string>
  DATE_INPUT_FORMAT = <string>
  DATE_OUTPUT_FORMAT = <string>
  DEFAULT_NULL_ORDERING = <string>
  ENABLE_GET_DDL_USE_DATA_TYPE_ALIAS = TRUE | FALSE
  ERROR_ON_NONDETERMINISTIC_MERGE = TRUE | FALSE
  ERROR_ON_NONDETERMINISTIC_UPDATE = TRUE | FALSE
  JSON_INDENT = <num>
  LOCK_TIMEOUT = <num>
  QUERY_TAG = <string>
  ROWS_PER_RESULTSET = <num>
  S3_STAGE_VPCE_DNS_NAME = <string>
  SEARCH_PATH = <string>
  SIMULATED_DATA_SHARING_CONSUMER = <string>
  STATEMENT_TIMEOUT_IN_SECONDS = <num>
  STRICT_JSON_OUTPUT = TRUE | FALSE
  TIMESTAMP_DAY_IS_ALWAYS_24H = TRUE | FALSE
  TIMESTAMP_INPUT_FORMAT = <string>
  TIMESTAMP_LTZ_OUTPUT_FORMAT = <string>
  TIMESTAMP_NTZ_OUTPUT_FORMAT = <string>
  TIMESTAMP_OUTPUT_FORMAT = <string>
  TIMESTAMP_TYPE_MAPPING = <string>
  TIMESTAMP_TZ_OUTPUT_FORMAT = <string>
  TIMEZONE = <string>
  TIME_INPUT_FORMAT = <string>
  TIME_OUTPUT_FORMAT = <string>
  TRANSACTION_DEFAULT_ISOLATION_LEVEL = <string>
  TWO_DIGIT_CENTURY_START = <num>
  UNSUPPORTED_DDL_ACTION = <string>
  USE_CACHED_RESULT = TRUE | FALSE
  WEEK_OF_YEAR_POLICY = <num>
  WEEK_START = <num>
```

> **Note:**
>
> For readability, the complete list of session parameters that can be set for an account is not included here. For a complete list of all session
> parameters, with their descriptions, as well as account and object parameters, see [Parameters](../parameters.md).

### Altering a different account

```sqlsyntax
ALTER ACCOUNT <name> SET IS_ORG_ADMIN = { TRUE | FALSE }

ALTER ACCOUNT <name> RENAME TO <new_name> [ SAVE_OLD_URL = { TRUE | FALSE } ]

ALTER ACCOUNT <name> DROP OLD URL

ALTER ACCOUNT <name> DROP OLD ORGANIZATION URL
```

## Account properties

You can set the following properties for the current account.

`SET property`
:   Specifies a property to set for your account:

> `LOGIN_IDP_REDIRECT = ( interface = security_integration [ , ... ] )`
> :   Specifies a mapping between Snowflake interfaces and
> [SAML security integrations](../../user-guide/admin-security-fed-auth-security-integration.md). SAML security integrations are used to
> implement single sign-on (SSO) authentication. If an interface is mapped to a SAML security integration, then users who access the
> interface are redirected to the third-party identity provider (IdP) to authenticate; they never see the Snowflake login screen.
>
>     If you don’t want interface users automatically redirected to an IdP, specify `interface = NULL`. Possible interfaces are:
>
>     `DEFAULT = security_integration`
>     :   Specifies the default security integration. Unless overridden by another interface-to-integration mapping, users are automatically
>         directed to the integration’s IdP when they access any Snowflake interface. Use this mapping to define the security integration
>         for Snowsight.
>
>     `SNOWFLAKE_INTELLIGENCE = security_integration`
>     :   Specifies the security integration used to redirect unauthenticated users to an IdP when they access
>         [Snowflake Intelligence](../../user-guide/snowflake-cortex/snowflake-intelligence.md). This overrides the DEFAULT mapping
>         for Snowflake Intelligence. For more information, see [Redirect users to your identity provider](../../user-guide/snowflake-cortex/snowflake-intelligence/deploy-agents.md).
>
>     `STREAMLIT = security_integration`
>     :   Specifies the security integration used to redirect unauthenticated users to an IdP when they access
>         Streamlit in Snowflake app-viewer URLs. This overrides the DEFAULT mapping for Streamlit app-viewer URLs. For more information,
>         see [Redirect app viewers to your identity provider](../../developer-guide/streamlit/object-management/security.md).
>
>     Default: Empty list `( )`
>
> `OBJECT_VISIBILITY = {object_visibility_spec | PRIVILEGED }`
> :   [Preview Feature](../../release-notes/preview-features.md) — Open
>
>     Available to all accounts.
>
>     Specifies the visibility of objects in the account, which controls the [discoverability of the objects](../../user-guide/ui-snowsight/object-visibility-universal-search.md)
>     and enables users without explicit access privileges to find objects and request access.
>
>     * A YAML specification describing the visibility in one of the following formats:
>
>       ```sqlexample-yaml
>       $$
>       organization_targets:
>         - all_accounts_including_external
>       $$
>       ```
>
>       Or
>
>       ```sqlexample-yaml
>       $$
>       organization_targets:
>         - account: <account_name_1>
>         - account: <account_name_2>
>         - ...
>         - organization_user_group: <org_user_group_1>
>         - organization_user_group: <org_user_group_2>
>       $$
>       ```
>
>       In the syntax above:
>
>       + `all_accounts_including_external`: Specifies that all users in all accounts in the organization can see the object. This includes
>         all accounts within the organization, even those to which external parties may have been given access, such as
>         [reader accounts](../../user-guide/data-sharing-reader-create.md).
>       + `account: account_name`: Specifies that all users in the specified account can see the object. You can specify multiple accounts.
>         Note that `account` is the account name, not the account locator. You must specify only the account name, excluding the organization name.09-22
>       + `organization_user_group: org_user_group`: Specifies that the specified [organization user group](../../user-guide/organization-users.md) can
>         see the object in all accounts in the organization where the [organization user group has been imported](../../user-guide/organization-users.md).
>     * `PRIVILEGED`: Specifies that only roles within the current account that are granted an explicit privilege on the object can see the object.
>       This is the default behavior in Snowflake.
>
>     For examples, see [Make database objects discoverable in Universal Search](../../user-guide/ui-snowsight/object-visibility-universal-search.md).
>
>     Default: `'PRIVILEGED'`

`UNSET property`
:   Reverts the specified account property to its default.

## Parameters for altering the current account

Use the following parameters when modifying the current account.

For more information about setting parameters at the account level, see [Parameter management](../../user-guide/admin-account-management.md). For details about a particular parameter, see [Parameters](../parameters.md).

`SET ...`
:   Specifies one (or more) account, session, object parameters, and object properties to set for your account (separated by blank spaces, commas, or new lines):

    * Account parameters cannot be changed by any other users.
    * Session and object parameters set at the account level serve only as defaults and can be changed by other users.

    For descriptions of the parameters you can set for your account, see [Parameters](../parameters.md).

`UNSET ...`
:   Specifies one (or more) account, session, and object parameters to unset for your account, which resets them to the system defaults.

    You can reset multiple properties with a single ALTER statement; however, each property must be separated by a comma. When resetting a
    property, specify only the name; specifying a value for the property will return an error.

`SET RESOURCE_MONITOR resource_monitor_name`
:   Special parameter that specifies the name of the resource monitor used to control all virtual warehouses created in the account.

    > **Important:**
    >
    > Setting a resource monitor at the account level does not impact any of the Snowflake-provided warehouses that Snowflake uses
    > for Snowpipe, automatic reclustering, or materialized views. The credits consumed by these warehouses do not count towards the
    > credit quota for an account-level resource monitor.
    >
    > For more details, see [Working with resource monitors](../../user-guide/resource-monitors.md).

`ADD ORGANIZATION USER GROUP group_name`
:   Imports an [organization user group](../../user-guide/organization-users.md) into the account. Organization users in the group are added to the
    account as user objects.

`REMOVE ORGANIZATION USER GROUP group_name`
:   Removes an [organization user group](../../user-guide/organization-users.md) from the account.

`SET { AUTHENTICATION | SESSION } POLICY policy_name [ { FOR ALL PERSON USERS | FOR ALL SERVICE USERS } ] [ FORCE ]`
:   Specifies the [authentication policy](../../user-guide/authentication-policies.md) or
    [session policy](../../user-guide/session-policies.md) for the account.

    The `FOR ALL PERSON USERS` clause applies the policy to users with their TYPE property set to NULL or PERSON.

    The `FOR ALL SERVICE USERS` clause applies the policy to users with their TYPE property set to SERVICE or
    LEGACY_SERVICE.

    If you don’t specify `FOR ALL SERVICE USERS` or `FOR ALL PERSON USERS`, then the policy applies to all users in the account.

    If you explicitly set a policy on a specific user or a specific user type, then that policy takes precedence over a policy applied to `FOR ALL SERVICE USERS` or `FOR ALL PERSON USERS`.

    If you specify FORCE, then policies you set on specific users or specific user types are overridden. You can use
    this if you don’t want to unset policies.

    If a policy is already set on the current account, you can use FORCE to set the policy without having to unset the
    existing policy first.

`SET FEATURE POLICY policy_name FOR ALL APPLICATIONS [ FORCE ]`
:   Specifies the feature policy to set for the account. If a feature policy
    is already set on the current account, you can use FORCE to set the feature policy
    without having to unset the feature policy first.

`UNSET FEATURE POLICY FOR ALL APPLICATIONS`
:   Unsets the feature policy for the account.

    If you already set a policy on the current account, then you can specify FORCE to set the policy without needing to unset an
    existing policy first.

`SET MAINTENANCE POLICY policy_name [ FORCE ] FOR ALL APPLICATIONS`
:   Specifies the [maintenance policy](../../developer-guide/native-apps/consumer-maintenance-policies.md) to apply to all applications in the account. If a maintenance policy is already set on
    the account, you can use FORCE to set the maintenance policy without having to unset the
    maintenance policy first.

`UNSET MAINTENANCE POLICY FOR ALL APPLICATIONS`
:   Removes the maintenance policy from all applications in the account. When a maintenance policy is removed from all applications in an account,
    the account-level maintenance policy, if it exists, is applied.

`UNSET { AUTHENTICATION | SESSION } POLICY [ FOR ALL PERSON USERS | FOR ALL SERVICE USERS ]`
:   Unsets the [authentication policy](../../user-guide/authentication-policies.md) or
    [session policy](../../user-guide/session-policies.md) for the account.

    Specifying `FOR ALL SERVICE USERS` or `FOR ALL PERSON USERS` narrows the scope of the command; the policy is unset from the
    specified user type only instead of all users in the account.

`SET PACKAGES | PASSWORD POLICY policy_name [ FORCE ]`
:   Specifies the [packages policy](../../developer-guide/udf/python/packages-policy.md) or
    [password policy](../../user-guide/password-authentication.md) for the account.

    If you already set a policy on the current account, then you can specify FORCE to set the policy without needing to unset an
    existing policy first.

`UNSET { PACKAGES | PASSWORD } POLICY`
:   Unsets the [packages policy](../../developer-guide/udf/python/packages-policy.md) or
    [password policy](../../user-guide/password-authentication.md) for the account.

`TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Parameters for altering a different account

Use the following parameters when using the current account to modify a different account. Only [organization administrators](../../user-guide/organization-administrators.md) can use these parameters.

`name`
:   Specifies the name of the account that is being modified.

`SET`
:   Specifies an account property to set for the account.

    `IS_ORG_ADMIN = { TRUE | FALSE }`
    :   Sets an account property that determines whether the ORGADMIN role is enabled in the account.

        > **Note:**
        >
        > Using the ORGADMIN role in a regular account is being phased out. Organization administrators should use the
        > [organization account](../../user-guide/organization-accounts.md) to complete organization-level tasks.

        To enable the ORGADMIN role for an account, specify `SET IS_ORG_ADMIN = TRUE`.

        You cannot set the property to `FALSE` from the current account. As a workaround, enable the role in a different account,
        and then switch to that account before executing the ALTER ACCOUNT command.

        By default, the ORGADMIN role can be enabled in a maximum of 8 accounts. If your organization requires more accounts with the ORGADMIN
        role, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

`RENAME TO new_name`
:   Changes the name of an account to the specified name.

    The new name should conform with all the [requirements for account identifiers](../../user-guide/admin-account-identifier.md).

    Organization administrators cannot rename an account while they are logged in to it, so they must log in to a different account before
    executing the ALTER ACCOUNT command. If your organization consists of a single account that needs to be renamed, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    `SAVE_OLD_URL = { TRUE | FALSE }`
    :   Optional parameter used in conjunction with `RENAME TO` that preserves the [account URL](../../user-guide/organizations-connect.md) used to
        access Snowflake prior to renaming. By default, Snowflake saves the original URL, which means you can access the account with either
        the old URL or the URL that contains the new account name. When set to `FALSE`, you must use the new URL to access the account.

        Default:
        :   TRUE

`DROP OLD URL`
:   Removes the original [account URL](../../user-guide/organizations-connect.md) of an account that was renamed. Once the old URL is dropped, you must
    access the account with the URL that contains the new account name.

    If an account has an old account URL because it was moved to another organization, had its organization renamed, or was part of an
    organization that was merged, use the ALTER ACCOUNT … DROP OLD ORGANIZATION URL instead.

`DROP OLD ORGANIZATION URL`
:   Removes the original [account URL](../../user-guide/organizations-connect.md) of an account after one of the following occurs:

    * Account moved to another organization
    * Account had its organization renamed.
    * Account was part of an organization that was merged with another organization.

    If an account has an old account URL because the account, not the organization, was renamed, use the ALTER ACCOUNT … DROP OLD URL
    command instead.

## Usage notes

* Account parameters can be set only at the account level.
* Session and object parameters that are set using this command serve only as defaults:

  > * User parameters can be overridden at the individual user level.
  > * Session parameters can be overridden at the individual user and session level.
  > * Object parameters can be overridden at the individual object level.
* Setting a resource monitor at the account level controls the credit usage for all virtual warehouses created in the account, but does not impact
  the credit usage for any of the Snowflake-provided warehouses. For more details, see [Working with resource monitors](../../user-guide/resource-monitors.md).

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Associate a network policy named `mypolicy` with your account:

> ```sqlexample
> ALTER ACCOUNT SET NETWORK_POLICY = mypolicy;
> ```

Disable user privilege grants:

> ```sqlexample
> ALTER ACCOUNT SET DISABLE_USER_PRIVILEGE_GRANTS = TRUE;
> ```

Remove the network policy association from your account:

> ```sqlexample
> ALTER ACCOUNT UNSET NETWORK_POLICY;
> ```

Set the packages policy at the account level.

> ```sqlexample
> ALTER ACCOUNT SET PACKAGES POLICY packages_policy_prod_1 FORCE;
> ```
>
> > **Note:**
> >
> > If a packages policy is already set on the current account, you can use FORCE to set the packages policy without
> > having to unset the packages policy first.

Unset the packages policy.

> ```sqlexample
> ALTER ACCOUNT UNSET PACKAGES POLICY;
> ```
