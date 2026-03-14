# Source: https://docs.startree.ai/thirdeye/how-tos/alert/use-templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Templates

Creating alerts can take time. To help reduce the time needed, you can make an alert detection logic configurable, and reuse it in multiple alerts with alert templates.

## Install StarTree templates

ThirdEye comes packaged with ready-to-use templates. To reinstall these templates, make the following call to the ThirdEye API:

```js  theme={null}
    curl -X POST "<YOUR_THIRDEYE_URL>/api/alert-templates/load-defaults" -H "Content-Type: application/x-www-form-urlencoded" -d "updateExisting=true"
```

Or use the [Swagger UI](/thirdeye/how-tos/use-the-api): Alert Template → load-defaults.

The StarTree templates are actively maintained and updated regularly. To update the templates in your environment, run the same command.

<Info>
  Updates are backward compatible. They will not break your alert configuration nor change the alert behavior, except for bug fixes.
</Info>

If you don't want to update the existing templates and only want to add new templates, use `-d "updateExisting=false"` in the command above.

## Create a new template

1. Click **Create** → **Create Alert Template**.
2. Create your template. The JSON schema is the same as the template field in an alert. See [alert configuration](/thirdeye/alert-configuration#template).
3. Add a `name` and a `description`.
4. Use properties in format `${myProperty}` where you want the detection logic to be configurable. These properties will be set by the alert using the template.

<img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/_create_template.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=aae611270fe7693f121fc37b782d330c" width="90%" data-path="img/thirdeye/_create_template.png" />

<Info>
  Most of the time, the template creation process looks like this:

* Create an alert - experiment, make sure it works fine and validate it can be reused for similar problems.
* Copy the template of the alert inside an alert template.
* Add a `name` and a `description` to the template. Save.
* Reuse the alert
</Info>

## Use the template

See [how to use the alert creation UI](/thirdeye/how-tos/alert/how-to-use-alert-creation-ui).

Built with [Mintlify](https://mintlify.com).
