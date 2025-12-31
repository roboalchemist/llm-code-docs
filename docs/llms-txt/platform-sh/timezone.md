# Source: https://docs.upsun.com/create-apps/timezone.md

# Timezones

On Upsun, there are several timezones you might want to keep in mind.
All timezones default to UTC time.
You can customize some of them, but in most cases,
it's best if you leave them in UTC
and store user data with an associated timezone instead.

The different timezones on Upsun are the following:

| Timezone             | Description                                  |Customizable  |
|----------------------|----------------------------------------------|--------------|
| Container timezone   | The timezone for all Upsun containers (UTC). |No            |
| App runtime timezone | [Set an app runtime timezone](#set-an-app-runtime-timezone) if you want your app runtime to use a specific timezone instead of the container timezone.<BR>The app runtime timezone only affects your app itself.                | Yes         |
| Cron timezone        | [Set a cron timezone](#set-a-cron-timezone) if you want your crons to run in a specific timezone instead of the app runtime timezone (or instead of the container timezone if no app runtime timezone is set on your project). <BR>The cron timezone only affects your cron jobs.                          | Yes         |
| Log timezone         | The timezone for all Upsun logs (UTC).      | No           |

**Note**: 

Each Upsun project also has a **project timezone** that only affects [automated backups](https://docs.upsun.com/environments/backup.md#automated-backups).
By default, the project timezone is based on the [region](https://docs.upsun.com/development/regions.md) where your project is hosted.
You can [change it from the Console](https://docs.upsun.com/projects/change-project-timezone.md) at any time.

## Set an app runtime timezone

How you can set an app runtime timezone depends on your actual app runtime:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    variables:
      php:
        "date.timezone": "Europe/Paris"
```

Start the server with ``env TZ=’<TIMEZONE>’ node server.js``.Start the server with ``env TZ=’<TIMEZONE>’ python server.py``.
 - Start the server with ``env TZ=’<TIMEZONE>’ java -jar …`` OR.
 - Set the Java virtual machine argument ``user.timezone``.
This Java virtual machine argument takes precedence over the environment variable TZ.
For example, you can use the flag ``-D`` when running the application:
``java -jar -D user.timezone=GMT`` or ``java -jar -D user.timezone="Asia/Kolkata"``

## Set a cron timezone

You can set a specific timezone for your crons so they don't run in your app runtime timezone (or container timezone if no app runtime timezone is set on your project).
To do so, [set the `timezone` top-level property](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) in your app configuration.

