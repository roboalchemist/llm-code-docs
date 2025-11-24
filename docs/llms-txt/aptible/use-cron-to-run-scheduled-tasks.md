# Source: https://www.aptible.com/docs/how-to-guides/app-guides/use-cron-to-run-scheduled-tasks.md

# How to use cron to run scheduled tasks

> Learn how to use cron to run and automate scheduled tasks on Aptible

## Overview

Cron jobs can be used to run, and automate scheduled tasks. On Aptible, users can run cron jobs with the use of an individual app or with a service associated with an app, defined in the app's [procfile](/how-to-guides/app-guides/define-services).

[Supercronic](https://github.com/aptible/supercronic) is an open-source tool created by Aptible that avoids common issues with cron job implementation in containerized platforms.

This guide is designed to walk you through getting started with cron jobs on Aptible with the use of Supercronic.

## Getting Started

**Step 1:** Install [Supercronic](https://github.com/aptible/supercronic#installation) in your Docker image.

**Step 2:** Add a `crontab` to your repository. Here is an example `crontab` you might want to adapt or reuse:

```bash  theme={null}
# Run every minute
*/1 * * * * bundle exec rake some:task

# Run once every hour
@hourly curl -sf example.com >/dev/null && echo 'got example.com!'
```

> 📘 For a complete crontab reference, review the documentation from the library Supercronic uses to parse crontabs, [cronexpr](https://github.com/gorhill/cronexpr#implementation).

> 📘 Unless you've specified otherwise with the `TZ` [environment variable](/core-concepts/architecture/containers/overview), the schedule for your crontab will be interpreted in UTC.

**Step 3:** Copy the `crontab` to your Docker image with a directive such as this one:

```bash  theme={null}
ADD crontab /app/crontab
```

> 📘 The example above grabs a file named `crontab` found at the root of your repository and copies it under `/app` in your image. Adjust as needed.

**Step 4:** Add a new service (if your app already has a Procfile), or deploy a new app altogether to start Supercronic and run your cron jobs. If you are adding a service, use this `Procfile` declaration:

```bash  theme={null}
cron: exec /usr/local/bin/supercronic /app/crontab
```

If you are adding a new app, you can use the same `Procfile` declaration or add a `CMD` declaration to your [Dockerfile](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview):

```bash  theme={null}
CMD ["supercronic", "/app/crontab"]
```
