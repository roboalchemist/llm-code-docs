# Source: https://www.speakeasy.com/md/docs/speakeasy-reference/generation/terraform-config.md

# Terraform configuration options

This section details the available configuration options for Terraform Provider generation. All configuration is managed in the `gen.yaml` file under the `terraform` section.

## Version and general configuration

```yml
terraform:
  version: 1.2.3
  author: "examplecorp"
  packageName: "examplecloud"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| version | true | 0.0.1 | Current version of the Terraform Provider. |
| packageName | true | terraform | Terraform Provider name. Prefixes all resource names. For providers published in the public Terraform Registry, this typically matches the suffix after terraform-provider- in the GitHub Repository name. |
| author | true | speakeasy | Terraform Provider namespace. For providers published in the public Terraform Registry, this typically matches the GitHub Organization name. |

## Additions

```yml
terraform:
  additionalDependencies: {}
  additionalResources: []
  additionalDataSources: []
  additionalEphemeralResources: []
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| additionalDependencies | false | {} | Add additional dependencies to include in the generated `go.mod`. |
| additionalResources | false | [] | A list of `{ importLocation?: string, importAlias?: string, resource: string }` objects to insert into the provider resource list. |
| additionalDataSources | false | [] | A list of `{ importLocation?: string, importAlias?: string, datasource: string }` objects to insert into the provider data source list. |
| additionalEphemeralResources | false | [] | A list of `{ importLocation?: string, importAlias?: string, datasource: string }` objects to insert into the provider ephemeral resource list. |

## Environment variables

```yml
terraform:
  environmentVariables:
    - env: EXAMPLECLOUD_TOKEN
      providerAttribute: token
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| environmentVariables | false | [] | A list of objects with `[env: string, providerAttribute: string]` keys/values to associate environment variables with a provider attribute. |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
