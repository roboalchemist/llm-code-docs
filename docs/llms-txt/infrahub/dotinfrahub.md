# Source: https://docs.infrahub.app/reference/dotinfrahub.md

# Repository configuration file

The repository configuration file allows you to define multiple resources that need to be imported into Infrahub.

The file should be formatted as a Yaml file, have the filename `.infrahub.yml` and should be stored at the root of the [repository](/topics/repository.md).

info

See [this topic](/topics/infrahub-yml.md) for more details on the available repository configuration options

note

To help with the development process of a repository configuration file, you can leverage the schemas we publish for validation within your [editor](/development/editor.md)

## Check Definitions[​](#check-definitions "Direct link to Check Definitions")

**Description**: User defined checks<br />**Key**: check\_definitions<br />**Type**: array<br />**Item type**: InfrahubCheckDefinitionConfig<br />

| Property    | Type   | Description                                                                | Mandatory |
| ----------- | ------ | -------------------------------------------------------------------------- | --------- |
| name        | string | The name of the Check Definition                                           | True      |
| file\_path  | string | The file within the repository with the check code.                        | True      |
| parameters  | object | The input parameters required to run this check                            | False     |
| targets     | string | The group to target when running this check, leave blank for global checks | False     |
| class\_name | string | The name of the check class to run.                                        | False     |

## Schemas[​](#schemas "Direct link to Schemas")

**Description**: Schema files<br />**Key**: schemas<br />**Type**: array<br />**Item type**: string<br />**Item format**: path<br />

## Jinja2 Transforms[​](#jinja2-transforms "Direct link to Jinja2 Transforms")

**Description**: Jinja2 data transformations<br />**Key**: jinja2\_transforms<br />**Type**: array<br />**Item type**: InfrahubJinja2TransformConfig<br />

| Property       | Type   | Description                                         | Mandatory |
| -------------- | ------ | --------------------------------------------------- | --------- |
| name           | string | The name of the transform                           | True      |
| query          | string | The name of the GraphQL Query                       | True      |
| template\_path | string | The path within the repository of the template file | True      |
| description    | string | Description for this transform                      | False     |

## Artifact Definitions[​](#artifact-definitions "Direct link to Artifact Definitions")

**Description**: Artifact definitions<br />**Key**: artifact\_definitions<br />**Type**: array<br />**Item type**: InfrahubRepositoryArtifactDefinitionConfig<br />

| Property       | Type   | Description                                           | Mandatory |
| -------------- | ------ | ----------------------------------------------------- | --------- |
| name           | string | The name of the artifact definition                   | True      |
| artifact\_name | string | Name of the artifact created from this definition     | False     |
| parameters     | object | The input parameters required to render this artifact | True      |
| content\_type  | string | The content type of the rendered artifact             | True      |
| targets        | string | The group to target when creating artifacts           | True      |
| transformation | string | The transformation to use.                            | True      |

## Python Transforms[​](#python-transforms "Direct link to Python Transforms")

**Description**: Python data transformations<br />**Key**: python\_transforms<br />**Type**: array<br />**Item type**: InfrahubPythonTransformConfig<br />

| Property                 | Type    | Description                                                                                         | Mandatory |
| ------------------------ | ------- | --------------------------------------------------------------------------------------------------- | --------- |
| name                     | string  | The name of the Transform                                                                           | True      |
| file\_path               | string  | The file within the repository with the transform code.                                             | True      |
| class\_name              | string  | The name of the transform class to run.                                                             | False     |
| convert\_query\_response | boolean | Decide if the transform should convert the result of the GraphQL query to SDK InfrahubNode objects. | False     |

## Generator Definitions[​](#generator-definitions "Direct link to Generator Definitions")

**Description**: Generator definitions<br />**Key**: generator\_definitions<br />**Type**: array<br />**Item type**: InfrahubGeneratorDefinitionConfig<br />

| Property                      | Type    | Description                                                                                         | Mandatory |
| ----------------------------- | ------- | --------------------------------------------------------------------------------------------------- | --------- |
| name                          | string  | The name of the Generator Definition                                                                | True      |
| file\_path                    | string  | The file within the repository with the generator code.                                             | True      |
| query                         | string  | The GraphQL query to use as input.                                                                  | True      |
| parameters                    | object  | The input parameters required to run this check                                                     | False     |
| targets                       | string  | The group to target when running this generator                                                     | True      |
| class\_name                   | string  | The name of the generator class to run.                                                             | False     |
| convert\_query\_response      | boolean | Decide if the generator should convert the result of the GraphQL query to SDK InfrahubNode objects. | False     |
| execute\_in\_proposed\_change | boolean | Decide if the generator should execute in a proposed change.                                        | False     |
| execute\_after\_merge         | boolean | Decide if the generator should execute after a merge.                                               | False     |

## Queries[​](#queries "Direct link to Queries")

**Description**: GraphQL Queries<br />**Key**: queries<br />**Type**: array<br />**Item type**: InfrahubRepositoryGraphQLConfig<br />

| Property   | Type   | Description                                         | Mandatory |
| ---------- | ------ | --------------------------------------------------- | --------- |
| name       | string | The name of the GraphQL Query                       | True      |
| file\_path | string | The file within the repository with the query code. | True      |

## Objects[​](#objects "Direct link to Objects")

**Description**: Objects<br />**Key**: objects<br />**Type**: array<br />**Item type**: string<br />**Item format**: path<br />

## Menus[​](#menus "Direct link to Menus")

**Description**: Menus<br />**Key**: menus<br />**Type**: array<br />**Item type**: string<br />**Item format**: path<br />
