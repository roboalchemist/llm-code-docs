# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-alert.md

# ALTER ALERT

Modifies the properties of an existing alert and suspends or resumes an existing [alert](../../user-guide/alerts.md).

See also:
:   [CREATE ALERT](create-alert.md) , [DESCRIBE ALERT](desc-alert.md), [DROP ALERT](drop-alert.md) , [SHOW ALERTS](show-alerts.md) , [EXECUTE ALERT](execute-alert.md)

## Syntax

```sqlsyntax
ALTER ALERT [ IF EXISTS ] <name> { RESUME | SUSPEND };

ALTER ALERT [ IF EXISTS ] <name> SET
  [ WAREHOUSE = <string> ]
  [ SCHEDULE = '{ <number> MINUTE | USING CRON <expr> <time_zone> }' ]
  [ COMMENT = '<string_literal>' ]

ALTER ALERT [ IF EXISTS ] <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER ALERT [ IF EXISTS ] <name> UNSET
  [ WAREHOUSE ]
  [ COMMENT ]

ALTER ALERT <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER ALERT [ IF EXISTS ] <name> MODIFY CONDITION EXISTS (<condition>)

ALTER ALERT [ IF EXISTS ] <name> MODIFY ACTION <action>
```

## Parameters

`name`
:   Identifier for the alert to alter. If the identifier contains spaces or special characters, the entire string must be enclosed
    in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`{ RESUME | SUSPEND }`
:   Specifies the action to perform on the alert:

    * `RESUME` makes a suspended alert active.
    * `SUSPEND` puts the alert into a “Suspended” state.

    If the alert schedule is set to an interval (i.e. `num MINUTE`), then to avoid ambiguity, the *base interval time* for
    the schedule is reset to the current time when the alert is resumed.

    The base interval time starts the interval counter from the current clock time. For example, if an alert is created with
    `10 MINUTE` and the alert is resumed at 9:03 AM, then the alert runs at 9:13 AM, 9:23 AM, and so on. Note that we make a best
    effort to ensure absolute precision, but only guarantee that alerts do not execute before their set interval occurs
    (e.g., in the current example, the alert could first run at 9:14 AM, but will definitely not run at 9:12 AM).

`SET ...`
:   Specifies one (or more) properties to set for the alert (separated by blank spaces, commas, or new lines).

    `WAREHOUSE = warehouse_name`
    :   Specifies the [virtual warehouse](../../user-guide/warehouses.md) that provides compute resources for executing this alert.

        > **Note:**
        >
        > For [serverless alerts](../../user-guide/alerts.md), do not set this property.

    `SCHEDULE ...`
    :   Specifies the schedule for periodically evaluating the condition for the alert on a schedule.

        When you create an alert, omitting this parameter or setting it to NULL creates an
        [alert on new data](../../user-guide/alerts.md).

        For alerts on a schedule, you can specify the schedule in one of the following ways:

        * `USING CRON expr time_zone`

          Specifies a cron expression and time zone for periodically evaluating the condition for the alert. Supports a subset of
          standard cron utility syntax.

          The cron expression consists of the following fields:

          ```bash
          # __________ minute (0-59)
          # | ________ hour (0-23)
          # | | ______ day of month (1-31, or L)
          # | | | ____ month (1-12, JAN-DEC)
          # | | | | _ day of week (0-6, SUN-SAT, or L)
          # | | | | |
          # | | | | |
            * * * * *
          ```

          The following special characters are supported:

          | Special Character | Description |
          | --- | --- |
          | `*` | Wildcard. When specified for a given field, the alert runs at every unit of time for that field.  For example, `*` in the month field specifies that the alert runs every month. |
          | `L` | Stands for “last”. When used in the day-of-week field, it allows you to specify constructs such as “the last Friday” (“5L”) of a given month. In the day-of-month field, it specifies the last day of the month. |
          | `/n` | Indicates the `n`th instance of a given unit of time. Each quanta of time is computed independently.  For example, if `4/3` is specified in the month field, then the evaluation of the condition is scheduled for April, July and October (i.e. every 3 months, starting with the 4th month of the year).  The same schedule is maintained in subsequent years. That is, the condition is not scheduled to be evaluated in January (3 months after the October run). |

          > **Note:**
          > + The cron expression currently evaluates against the specified time zone only. Altering the
          >   [TIMEZONE](../parameters.md) parameter value for the account (or setting the value at the user or session level) does not
          >   change the time zone for the alert.
          > + The cron expression defines all valid times for the evaluation of the condition for the alert. Snowflake attempts
          >   to evaluate the condition based on this schedule; however, any valid run time is skipped if a previous run has not
          >   completed before the next valid run time starts.
          > + When both a specific day of month and day of week are included in the cron expression, then the evaluation of the
          >   condition is scheduled on days satisfying either the day of month or day of week. For example,
          >   `SCHEDULE = 'USING CRON 0 0 10-20 * TUE,THU UTC'` schedules an evaluation at 0AM on any 10th to 20th day of the month
          >   and also on any Tuesday or Thursday outside of those dates.
        * `num MINUTE`

          Specifies an interval (in minutes) of wait time inserted between evaluations of the alert. Accepts positive integers only.

          Also supports `num M` syntax.

          To avoid ambiguity, a *base interval time* is set when the alert is resumed (using
          ALTER ALERT … RESUME).

          The base interval time starts the interval counter from the current clock time. For example, if an alert is created with
          `10 MINUTE` and the alert is resumed at 9:03 AM, then the condition for the alert is evaluated at 9:13 AM, 9:23 AM, and so
          on. Note that we make a best effort to ensure absolute precision, but only guarantee that conditions are not evaluated
          before their set interval occurs (e.g. in the current example, the condition could be evaluated first at 9:14 AM but
          definitely not at 9:12 AM).

          > **Note:**
          >
          > The maximum supported value is `11520` (8 days). Alerts that have a greater `num MINUTE` value never have their
          > conditions evaluated.

    `COMMENT = 'string_literal'`
    :   Specifies a comment for the alert.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`UNSET ...`
:   Specifies one or more properties/parameters to unset for the alert, which resets them back to their defaults:

    * `WAREHOUSE`
    * `COMMENT`
    * `TAG tag_key [ , tag_key ... ]`

`MODIFY CONDITION EXISTS (condition)`
:   Specifies the SQL statement that should represent the condition for the alert. You can use the following commands:

    * [SELECT](select.md)
    * [SHOW <objects>](show.md)
    * [CALL](call.md)

    If the statement returns one or more rows, the action for the alert is executed.

`MODIFY ACTION action`
:   Specifies the SQL statement that should be executed if the condition returns one or more rows.

    To send a notification, you can
    [call the SYSTEM$SEND_EMAIL or SYSTEM$SEND_SNOWFLAKE_NOTIFICATION stored procedure](../../user-guide/notifications/about-notifications.md).

## Access control requirements

Executing this SQL command requires [roles](../../user-guide/security-access-control-overview.md) with the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

* To resume an alert:

  * The role executing ALTER ALERT must have either the OPERATE or OWNERSHIP privilege on the alert.
  * The role with the OWNERSHIP privilege on the alert must also have the following privileges:

    * The global EXECUTE ALERT privilege.
    * The global EXECUTE MANAGED ALERT privilege, if the alert is a [serverless alert](../../user-guide/alerts.md).
    * The USAGE privilege on the warehouse, if the [alert uses a specified warehouse](../../user-guide/alerts.md).
* To suspend an alert, the role executing ALTER ALERT must have either the OPERATE or OWNERSHIP privilege on the alert.
* To modify the properties of the alert, the role executing ALTER ALERT must have the OWNERSHIP privilege on the alert.

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* You cannot change an [alert on new data](../../user-guide/alerts.md) to an
  [alert on a schedule](../../user-guide/alerts.md). Similarly, you cannot change an alert on a schedule to an alert
  on new data.
* When an alert is resumed, Snowflake verifies that the role with the OWNERSHIP privilege on the alert also has the USAGE
  privilege on the warehouse assigned to the alert, as well as the global EXECUTE ALERT privilege; if not, an error is produced.
* Only account administrators (users with the ACCOUNTADMIN role) can grant the EXECUTE ALERT privilege to a role. For ease of use,
  we recommend creating a custom role (e.g. alert_admin) and assigning the EXECUTE ALERT privilege to this role. Any role that can
  grant privileges (e.g. SECURITYADMIN or any role with the MANAGE GRANTS privilege) can then grant this custom role to any alert
  owner role to allow altering their own alerts. For instructions for creating custom roles and role hierarchies, see
  [Configuring access control](../../user-guide/security-access-control-configure.md).

* When you execute CREATE ALERT or ALTER ALERT, some validation checks are not performed on the statements in the condition and
  action, including:

  * The resolution of the identifiers for objects.
  * The resolution of the data types of expressions.
  * The verification of the number and types of arguments in a function call.

  The CREATE ALERT and ALTER ALERT commands do not fail if the SQL statement for a condition or action specifies an invalid
  identifier, incorrect data type, incorrect number and types of function arguments, etc. Instead, the failure occurs when the
  alert executes.

  To check for failures in an existing alert, use the [ALERT_HISTORY](../functions/alert_history.md) table function.

  To avoid these types of failures, before you specify the conditions and actions for alerts, verify the SQL expressions and
  statements for those conditions and actions.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

See [Suspending and resuming an alert](../../user-guide/alerts.md).
