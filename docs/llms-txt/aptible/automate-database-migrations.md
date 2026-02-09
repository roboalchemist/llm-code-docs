# Source: https://www.aptible.com/docs/how-to-guides/database-guides/automate-database-migrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automate Database migrations

Many app frameworks provide libraries for managing database migrations between different revisions of an app.

For example, Rails' ActiveRecord library allows users to define migration files and then run `bundle exec rake db:migrate` to execute them.

To automatically run migrations on each deploy to Aptible, you can use a [`before_release`](/core-concepts/apps/deploying-apps/releases/aptible-yml#before-release) command.

To do so, add the following to your [`.aptible.yml`](/core-concepts/apps/deploying-apps/releases/aptible-yml) file (adjust the command as needed depending on your framework):

```bash  theme={null}
before_release:
  - bundle exec rake db:migrate
```

> ❗️ Don't break your App when running Database migrations! It's easy to forget that your App will be running when automated Database migrations execute, but it's important not to. For example, if your migration locks a table for 10 minutes (e.g., to create a new index synchronously), then that table is going to read-only for 10 minutes. If your App needs to write to this table to function, **it will be down**. Also, if your App is a web App, review the docs over here: [Concurrent Releases](/core-concepts/apps/deploying-apps/releases/overview#concurrent-releases).

## Migration Scripts

If you need to run more complex migration scripts (e.g., with `if` branches, etc.), we recommend encapsulating this logic in a separate script:

```python  theme={null}
#!/bin/sh
# This file lives at script/before_release.sh

if [ "$RAILS_ENV" == "staging" ]; then
  bundle exec rake db:[TASK]
else
  bundle exec rake db:[OTHER_TASK]
fi
```

> ❗️The script needs to be made executable. To do so, run `chmod script/before_release.sh`.

Your new `.aptible.yml` would read:

```bash  theme={null}
before_release:
  - script/before_release.sh
```
