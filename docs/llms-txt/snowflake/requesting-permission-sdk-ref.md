# Source: https://docs.snowflake.com/en/developer-guide/native-apps/requesting-permission-sdk-ref.md

# Python Permission SDK reference

This topic provides reference information for the functions supported by the `snowflake.permissions`
module of the Python Permission SDK. For information on using the Python Permission SDK to request privileges in the consumer account, see [Create a user interface to request privileges and references](requesting-ui.md).

## get_application_specifications()

Returns all app specifications defined for the app.

Signature:
:   ```python
    get_application_specifications()
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   An array of dictionaries, where each dictionary contains the following key/value pairs:

    ```json
    {
      "name": "<value>",
      "requested_on": "<value>",
      "type": "<value>",
      "sequence_number": "<value>",
      "status": "<value>",
      "status_upgraded_on": "<value>",
      "label": "<value>",
      "description": "<value>",
      "definition": "<value>",
    }
    ```

    Where:

    * `name`: The name of the app specification.
    * `requested_on`: Timestamp when the app specification was requested.
    * `type`: Type of app specification. Supported values are: EXTERNAL ACCESS and SECURITY INTEGRATION.
    * `sequence_number`: ID for a version of an app specification. This value is incremented each time a provider
      changes the [app specification definition](requesting-app-specs.md).
    * `status`: Specifies the current status of the app specification. Possible values are:

      + `APPROVED`: The consumer approved the app specification.
      + `DECLINED`: The app specification is waiting for the consumer to approve or decline.
      + `DECLINED`: The consumer declined the app specification.
      + `PENDING`: The app specification is waiting for the consumer to approve or decline.
    * `status_updated_on`: Timestamp of the last status change.
    * `label`: Name of the app specification that is displayed to the consumer in Snowsight.
    * `description`: Description of the app specification that is displayed to the consumer in Snowsight.
    * `definition`: Values that are part of the
      [app specification definition](requesting-app-specs.md). The values of
      this column depend on the type of app specification.

## get_detailed_reference_associations()

Provides detailed information about a reference to an object in the consumer account.

Signature:
:   ```python
    get_detailed_reference_associations(reference_name: str) -> List[dict]
    ```

Arguments:
:   A string value containing the name of a reference.

Returns:
:   Returns a JSON object representing an array of dictionaries. Each dictionary contains the following
    key/value pairs:

    ```json
    {
      "alias": "<value>",
      "database": "<value>",
      "schema": "<value>",
      "name": "<value>"
    }
    ```

    Where:

    * `alias`: The system-generated alias for the reference.
    * `database`: The parent database name of the consumer object, if the object resides in a database.
      Otherwise, null.
    * `schema`: The parent schema of the consumer object, if the object resides in a schema. Otherwise,
      null.
    * `name`: The name of the consumer object.

## get_held_account_privileges()

Returns the privileges that have been granted to the app.

Signature:
:   ```python
    get_held_account_privileges(privilege_names: [str]) -> [str]
    ```

Arguments:
:   An array of string values containing the names of privileges to check.

Returns:
:   Returns an array containing the privileges that have been granted to the app
    based on the array of privileges passed to the function.

    Returns an array containing the privileges that have been granted to the Snowflake Native App
    based on the array of privileges passed to the function.

## get_missing_account_privileges()

Returns the privileges that have not been granted to the app.

Signature:
:   ```python
    get_missing_account_privileges(privilege_names: [str]) -> [str]
    ```

Arguments:
:   An array of string values containing the names of privileges to check.

Returns:
:   Returns a string array containing the privileges that have **not** been granted to the app
    based on the array of privileges passed to the function.

## get_reference_associations()

Determines the objects in the consumer account that are associated with a reference.

To get more detailed information about references to objects in the consumer account,
use get_detailed_reference_associations().

Signature:
:   ```python
    get_reference_associations(reference_name: str) -> [str]
    ```

Arguments:
:   A string value containing the name of a reference.

Returns:
:   Returns an array containing Snowflake-generated aliases of objects in the consumer account
    that are bound to the reference.

## is_application_all_mandatory_telemetry_event_definitions_enabled()

Checks if all mandatory telemetry event definitions are enabled for the app.

For more information on telemetry event sharing, see
[Verify event definitions by using the Permissions SDK](event-develop.md).

Signature:
:   ```python
    is_application_all_mandatory_telemetry_event_definitions_enabled() -> bool
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   Returns TRUE if all mandatory telemetry event definitions are enabled for the app.
    Returns FALSE, otherwise.

## is_application_authorized_for_telemetry_event_sharing()

Checks if the current application is authorized for telemetry event sharing.

For more information on telemetry event sharing, see [Verify event definitions by using the Permissions SDK](event-develop.md).

Signature:
:   ```python
    is_application_authorized_for_telemetry_event_sharing() -> bool
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   Returns TRUE if the application is authorized for telemetry event sharing.
    Returns FALSE, otherwise.

## is_application_local_to_package()

Checks if the app is installed in the same account as the application package.

Signature:
:   ```python
    is_application_local_to_package() -> bool
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   Returns TRUE if the app is installed in the same account as the application package.
    Returns FALSE, otherwise.

## is_event_sharing_enabled()

Checks if event sharing is enabled for the app.

Signature:
:   ```python
    is_event_sharing_enabled() -> bool
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   Returns TRUE if the SHARE_EVENTS_WITH_PROVIDER property is true and the consumer account has an
    active event table configured. Returns FALSE, otherwise.

## is_external_data_enabled()

Checks if the current application is enabled to use external and iceberg tables.

Signature:
:   ```python
    is_external_data_enabled() -> bool
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   Returns TRUE if the app is enabled to use external and iceberg tables.
    Returns FALSE, otherwise.

## request_application_specification_review()

Opens a dialog in a Streamlit app that allows the consumer to review an app specification then
approve, decline, or take no action. A consumer can only decline an app specification if it is optional.

Signature:
:   ```python
    request_application_specification_review(spec_names: [str] = None)
    ```

Arguments:
:   An optional array of string values containing the names of the app specifications to review. If this parameter is
    not specified, the dialog will show all app specifications defined for the app.

Returns:
:   This method does not return a value.

## request_aws_api_integration()

Requests an API integration from the consumer for the Amazon API Gateway.

You must define the API integration in the manifest file. For more information,
see [CREATE API INTEGRATION](../../sql-reference/sql/create-api-integration.md) for information on other parameters.

Signature:
:   ```python
    request_aws_api_integration(id: str, allowed_prefixes: [str], gateway: AwsGateway, aws_role_arn: str, api_key: str = None, name: str = None, comment: str = None)
    ```

Arguments:
:   *`id`: The name of the API integration defined in the manifest file.
    * `allowed_prefixes`: An array of string values containing the allowed prefixes for the API integration.
    * `gateway`: The type of API Gateway to use. This parameter must be one of the following values:

      + permissions.AwsGateway.API_GATEWAY
      + permissions.AwsGateway.PRIVATE_API_GATEWAY
      + permissions.AwsGateway.GOV_API_GATEWAY
      + permissions.AwsGateway.GOV_PRIVATE_API_GATEWAY
    * `aws_role_arn`: The Amazon Resource Name (ARN) of the IAM role that the API Gateway uses to access the
      consumer account.
    * `api_key`: An optional API key for the API Gateway.
    * `name`: An optional name for the API integration.
    * `comment`: An optional comment for the API integration.

    See [CREATE API INTEGRATION](../../sql-reference/sql/create-api-integration.md) for information on other possible parameters.

Returns:
:   A string value containing the name of a reference.

## request_azure_api_integration()

Requests an API integration from the consumer for Azure API Management.

You must define the API integration in the manifest file. For more information,
see [CREATE API INTEGRATION](../../sql-reference/sql/create-api-integration.md) for information on other parameters.

Signature:
:   ```python
    request_azure_api_integration(id: str, allowed_prefixes: [str], tenant_id: str, application_id: str, api_key: str = None, name: str = None, comment: str = None)
    ```

Arguments:
:   *`id`: The name of the API integration defined in the manifest file.
    * `allowed_prefixes`: An array of string values containing the allowed prefixes for the API integration.
    *`tenant_id`: The tenant ID for the Azure API Management.
    * `application_id`: The application ID for the Azure API Management.
    *`api_key`: An optional API key for the Azure API Management.
    * `name`: An optional name for the API integration.
    * `comment`: An optional comment for the API integration.

Returns:
:   This method does not return a value.

## request_event_sharing()

Opens a dialog in a Streamlit app that allows the consumer to share events with the app.

Signature:
:   ```python
    request_event_sharing()
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   This method does not return a value.

## request_external_data()

Requests consent from the consumer to use external and iceberg tables.

Signature:
:   ```python
    request_external_data()
    ```

Arguments:
:   This function does not take any arguments.

Returns:
:   This method does not return a value.

## request_google_api_integration()

Requests an API integration from the consumer for Google Cloud API Gateway.

You must define the API integration in the manifest file. For more information,
see [CREATE API INTEGRATION](../../sql-reference/sql/create-api-integration.md) for information on other parameters.

Signature:
:   ```python
    request_google_api_integration(id: str, allowed_prefixes: [str], audience: str, name: str = None, comment: str = None, api_key: str = None
    ```

Arguments:
:   *`id`: The name of the API integration defined in the manifest file.
    * `allowed_prefixes`: An array of string values containing the allowed prefixes for the API integration.
    *`audience`: The audience for the Google Cloud API Gateway.
    * `name`: An optional name for the API integration.
    *`comment`: An optional comment for the API integration.
    * `api_key`: An optional API key for the Google Cloud API Gateway.

Returns:
:   This method does not return a value.

## request_account_privileges()

Requests privileges from the consumer specified by a string array passed to the function that
contains the privileges. The specified privileges must be listed in the manifest file.

Signature:
:   ```python
    request_account_privileges(privileges: [str])
    ```

Arguments:
:   An string array containing a list of privileges the app is requesting.

Returns:
:   This method does not return a value.

## request_reference()

Requests a reference from the consumer specified by the string passed to the function. The
reference passed to the function must be defined in the manifest file.

See [Object types and privileges that a reference can contain](requesting-refs.md) for a list of the objects that can be
included in a reference and their supported privileges.

Signature:
:   ```python
    request_reference(reference: str)
    ```

Arguments:
:   A string value containing the name of a reference to request.

Returns:
:   This method does not return a value.
