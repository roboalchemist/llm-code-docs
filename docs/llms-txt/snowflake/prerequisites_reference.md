# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/prerequisites_reference.md

# Prerequisites SQL Reference

## Database objects and procedures

The following database objects are created through the file `prerequisites.sql`.

### STATE.PREREQUISITES

An internal table to persist the data about the prerequisites. This table is not accessible from outside the app. To read the data use the `PUBLIC.PREREQUISITES` view below.
The table contains the following columns:

* `id STRING`
* `title VARCHAR`
* `description VARCHAR`
* `learnmore_url VARCHAR`
* `documentation_url VARCHAR`
* `guide_url VARCHAR`
* `custom_properties VARIANT`
* `is_completed BOOLEAN`
* `position INTEGER`

### PUBLIC.PREREQUISITES

This view is exposed to the `ADMIN` and `VIEWER` roles. It returns the data from the above table. Rows will be sorted ascending by the `position` column.
Inserting prerequisites happens inside `setup.sql`. However, it has to be done in a way that will skip the insert during the update.
For example:

```sqlexample
EXECUTE IMMEDIATE
$$
DECLARE
    prerequisites_exist NUMBER;
BEGIN
    SELECT COUNT (*) INTO :prerequisites_exist FROM state.prerequisites;
    IF (:prerequisites_exist = 0) THEN
        INSERT INTO STATE.PREREQUISITES (ID, TITLE, DESCRIPTION, DOCUMENTATION_URL, POSITION)
            VALUES
                ('1', '<Prerequisite name>', '<Prerequisite description>', 'Prerequisite url', 1)
    END IF;
END;
$$;
```

Another approach is to use a merge statement instead and do nothing (or update) on match.

### PUBLIC.COMPLETE_PREREQUISITES_STEP()

A procedure available to `ADMIN` users. The successful execution of this procedure does not require all prerequisites to be completed.
If the configuration status of the connector is `INSTALLED` it sets the status of the Connector to:

```json
{
    "status": "CONFIGURING",
    "configurationStatus": "PREREQUISITES_DONE"
}
```

Otherwise, there is no effect.

This procedure requires the connector to be in the `CONFIGURING` status and configuration status other than `FINALIZED`. Otherwise an exception is thrown.

Possible errors include:

* `INVALID_CONNECTOR_STATUS` - connector_status is not `[CONFIGURING]`.
* `INVALID_CONNECTOR_CONFIGURATION_STATUS` - configuration_status is `FINALIZED`.
* `UNKNOWN_ERROR` - Something unexpected went wrong - message of thrown exception is forwarded.

### PUBLIC.UPDATE_PREREQUISITE (ID VARCHAR, IS_COMPLETED BOOLEAN)

This procedure sets a status of the given prerequisite to the provided value. It is only available to `ADMIN` users.
The validations are similar to the `COMPLETE_PREREQUISITES_STEP()` procedure.

Possible errors include:

* `INVALID_CONNECTOR_STATUS` - Connector status is not `[CONFIGURING]`.
* `INVALID_CONNECTOR_CONFIGURATION_STATUS` - Connector configuration status is `FINALIZED`.
* `PREREQUISITE_NOT_FOUND` - Prerequisite with given ID not found.

### PUBLIC.MARK_ALL_PREREQUISITES_AS_DONE()

This procedures sets the `is_completed` column for all the prerequisites to `true`. The validations are similar to the `COMPLETE_PREREQUISITES_STEP()` procedure.

Possible errors include:

* `INVALID_CONNECTOR_STATUS` - Connector status is not `[CONFIGURING]`.
* `INVALID_CONNECTOR_CONFIGURATION_STATUS` - Connector configuration status is `FINALIZED`.
