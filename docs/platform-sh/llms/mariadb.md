# Source: https://docs.upsun.com/development/sanitize-db/mariadb.md

# Sanitizing databases: MariaDB and Drupal


Databases of live websites often contain personally identifiable information (PII)
such as full names, mailing addresses, and phone numbers.
To ensure people reviewing code changes can't access information they shouldn't,
sanitize your databases of any PII that they may contain.

This example goes through the process for a MySQL database using Drupal.

## Before you begin

You need:

- A project with a [MySQL database](https://docs.upsun.com../../add-services/mysql.md).
- A command interface installed:
  - If doing it manually, the [Upsun CLI](https://docs.upsun.com../../administration/cli.md).
  - Otherwise, make sure [Drush](https://www.drush.org/latest/install/) is installed in your environment.

This guide is about sanitizing MySQL databases.

This guide doesn't address:

- Sanitizing NoSQL Databases (such as [MongoDB](https://docs.upsun.com../../add-services/mongodb.md))
- Input validation and input sanitization, which both help prevent security vulnerabilities

## Sanitize the database

Make sure that you only sanitize preview environments and **never** the production environment.
Otherwise you may lose most or even all of the relevant data stored in your database.

First, take a [database dump](https://docs.upsun.com../../add-services/mysql.md#exporting-data) of your preview environment.
This is just a safety precaution.
Production data isn't altered.
To get a database dump, run the following command:
``upsun
 db:dump -e <DEVELOPMENT_ENVIRONMENT_NAME>
``.

You see output like the following:

```sql {}
+----+------------+---------------+---------------------------+---------------+
| ID | first_name | last_name     | user_email                | display_name  |
+----+------------+---------------+---------------------------+---------------+
|  1 | admin      | admin         | admin@yourcompany.com     | admin         |
|  2 | john       | doe           | john.doe@gmail.com        | john          |
|  3 | jane       | doe           | janedoe@ymail.com         | jane          |
+----+------------+---------------+---------------------------+---------------+
```

 - Change the fields where PII is contained with the [UPDATE](https://mariadb.com/kb/en/update/).
For example, to change the display name of users with an email address not in your company’s domain
to a random value, run the following query:

```sql {}
UPDATE users
SET display_name==substring(md5(display_name||'$PLATFORM_PROJECT_ENTROPY') for 8);
WHERE email NOT LIKE '%@yourcompany%'
```

Adapt and run that query for all fields that you need to sanitize.
If you modify fields that you shouldn’t alter,
[you can restore them](https://docs.upsun.com/environments/restore.md) from the dump you took in step 1.
You can create a script to automate the sanitization process to be run automatically on each new deployment.
Once you have a working script, add your script to sanitize the database to [a ](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#deploy-hook):

    .upsun/config.yaml

```yaml {}
applications:
    myapp:

        # ...

        hooks:
            deploy: |

                # ...

                cd /app/public
                if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
                    # Do whatever you want on the production site.
                else
                    # The sanitization of the database should happen here (since it's non-production)
                    sanitize_the_database.sh
                fi
```

To sanitize your database and get rid of sensitive, live information, use the ``drush sql:sanitize`` command.
Add your script to sanitize the database to [a ](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#deploy-hook)
for preview environments:

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    hooks:
      deploy: |

        # ...

        cd /app/public
        if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
          # Do whatever you want on the production site.
        else
          drush -y sql:sanitize
        fi
        drush -y updatedb
```

More options are available.
These are described in the [Drush documentation](https://www.drush.org/latest/commands/sql_sanitize/).
To sanitize only on the initial deploy and not all future deploys,
use [Drush state](https://www.drush.org/latest/commands/state_set/) as in the following example:

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    hooks:
      deploy: |

        # ...

        cd /app/public
        if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ] || [ "$(drush state:get --format=string mymodule.sanitized)" != yes ]; then
          # Do whatever you want on the production site.
        else
          drush -y sql:sanitize
          drush state:set --input-format=string mymodule.sanitized yes
        fi
```

## What's next

You learned how to remove sensitive data from a database.

To replace sensitive data that with other meaningful data, you can add a `faker` to the process.
A `faker` is a program that generates fake data that looks real.
Having meaningful PII-free data allows you to keep your current Q&A, external reviews, and other processes.
To add a faker, adapt your sanitizing queries to replace each value that contains PII with a new value generated by the faker.

You might also want to make sure that you [implement input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.md#goals-of-input-validation).

If your database contains a lot of data, consider using the [`OPTIMIZE TABLE` statement](https://mariadb.com/kb/en/optimize-table/)
to reduce its size and help improve performance.

