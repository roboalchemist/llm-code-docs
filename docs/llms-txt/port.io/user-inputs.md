# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs.md

# User Inputs

Each action has a `userInputs` section in its definition. In this section, you can define all of the user inputs you want your developers and users to fill when invoking the action.

## Structure[â](#structure "Direct link to Structure")

```
{
  "properties": {
    "myInput": {
      "title": "My input",
      "icon": "My icon",
      "description": "My input",
      "type": "input_type"
    }
  },
  "required": ["myInput"]
}
```

The different components that make up a basic user input definition are listed in the following table:

| Field         | Description                                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | The input's title.                                                                                                                                                               |
| `type`        | **Mandatory field.** The input's data type.                                                                                                                                      |
| `icon`        | The input's icon. See the [full icon list](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md#full-icon-list) for the available icons. |
| `description` | A description that can be used to provide detailed information about a specific input or the way it should be used.                                                              |
| `default`     | A default value for this input in case the action is executed without explicitly providing a value.                                                                              |

property structure

The name of the input is the key of the input object. For example, in the code block above, the name of the input is `myInput`.

Note that all of the [properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties) available for Port blueprints can also be used as user inputs, which is why they follow the same structure.

## Supported input types[â](#supported-input-types "Direct link to Supported input types")

## [ðï¸<!-- --> <!-- -->Array](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/array.md)

[Array is an input for lists of data](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/array.md)

## [ðï¸<!-- --> <!-- -->Datetime](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/datetime.md)

[Datetime is an input used to reference a date and time](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/datetime.md)

## [ðï¸<!-- --> <!-- -->Email](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/email.md)

[Email is an input used to save Email addresses](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/email.md)

## [ðï¸<!-- --> <!-- -->Entity](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/entity.md)

[Entity is an input used to reference existing entities from the software catalog when triggering actions](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/entity.md)

## [ðï¸<!-- --> <!-- -->Number](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/number.md)

[Number is a basic input for numeric data](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/number.md)

## [ðï¸<!-- --> <!-- -->Object](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/object.md)

[Object is a basic input for JSON data](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/object.md)

## [ðï¸<!-- --> <!-- -->Secret](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/secret.md)

[A secret input encrypts its value before sending it to your backend and never stores or logs it. Choose Port-managed encryption or your own public key.](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/secret.md)

## [ðï¸<!-- --> <!-- -->Team](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/team.md)

[Team is an input used to reference teams that exist in Port](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/team.md)

## [ðï¸<!-- --> <!-- -->Text](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/text.md)

[Text is a basic input for textual information](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/text.md)

## [ðï¸<!-- --> <!-- -->Toggle (Boolean)](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/toggle.md)

[Toggle is a basic input that has one of two possible values - true and false](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/toggle.md)

## [ðï¸<!-- --> <!-- -->URL](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/url.md)

[URL is an input used to save links to websites](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/url.md)

## [ðï¸<!-- --> <!-- -->User](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/user.md)

[User is an input used to reference users that exist in Port](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/user.md)

## [ðï¸<!-- --> <!-- -->Yaml](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/yaml.md)

[Yaml is an input used to save object definitions in YAML](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/yaml.md)

## Special `string` formats[â](#special-string-formats "Direct link to special-string-formats")

In addition to the `string` formats available in the [Blueprint properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties) section, Port's actions also support the following special formats:

| `type`   | Description                                     | Example values                                  |
| -------- | ----------------------------------------------- | ----------------------------------------------- |
| `entity` | An entity of a specified blueprint              | `"notifications-service"`                       |
| `array`  | An array of entities from a specified blueprint | `["notifications-service", "frontend-service"]` |

### Entity[â](#entity "Direct link to Entity")

```
"entity_prop": {
    "title": "My string prop",
    "type": "string",
    "format": "entity",
    "blueprint": "microservice",
    "description": "This is an entity property"
}
```

When `"format": "entity"` is used, a `blueprint` field is available.

The `blueprint` field takes an identifier of an existing blueprint. Then, when executing the configured action from Port's UI, the specified field will include a list of existing entities of the selected blueprint from your software catalog to choose from.

### Entity array[â](#entity-array "Direct link to Entity array")

```
"entity_prop": {
    "title": "My string prop",
    "description": "This property is an array of Entities",
    "type": "array",
    "items": {
      "type": "string",
      "blueprint": "service",
      "format": "entity"
    }
}
```

When `"type": "array"` is used, you can create an `items` property. Under this `items` property you can use `"format": "entity"` and write the identifier of the selected `blueprint` which you want to include entities from. You can then pass an entity array to your action.

## Ordering user inputs[â](#ordering-user-inputs "Direct link to Ordering user inputs")

You can define the order in which the user inputs will be displayed in the UI by using the `order` field. This field is an array of the input names:

```
{
  "properties": {
    "myInput1": {
      "title": "My input 1",
      "icon": "My icon 1",
      "description": "My input 1",
      "type": "input_type"
    },
    "myInput2": {
      "title": "My input 2",
      "icon": "My icon 2",
      "description": "My input 2",
      "type": "input_type"
    }
  },
  "required": [],
  "order": ["myInput2", "myInput1"]
}
```
