# Source: https://docs.firehydrant.com/docs/backstage-integration.md

# Backstage

Backstage is Spotify's open-source developer portal platform that centralizes all software components—services, websites, libraries, and more—in a unified catalog. While similar to FireHydrant's [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) in providing standardized organization, FireHydrant's catalog is specifically designed for incident management and integrates with tools like Backstage rather than competing with them.

FireHydrant's integration with Backstage comes with two parts:

* FH Service Catalog ingestion of Backstage-defined services
* FireHydrant plugin within Backstage

## Service Ingestion via GitHub YAML

<Image alt="Creating a Catalog Setting on FireHydrant" align="center" width="650px" border={true} src="https://files.readme.io/6d4e26b31eb9ca9e57d16cc84643c208a9c95a62e2846e584464191e7f9ce64d-CleanShot_2025-06-11_at_13.32.212x.jpg">
  Creating a Catalog Setting on FireHydrant
</Image>

> 📘 Note:
>
> Requires [GitHub](https://docs.firehydrant.com/docs/github-integration) integration configured.

### Create Catalog Setting

1. Navigate to **Catalog**, and then in the left navigation drawer, click **Catalog settings**.
2. Near the top right, click "+ Create catalog setting."
3. Enter parameters:
   1. **Name** - A name for the catalog setting
   2. **Description** - A description for the catalog setting
   3. **Provider** - Select `GitHub`.
      1. **Format** - Select `backstage.io/v1alpha1`
   4. **Targets** - This is where you specify the path(s) of the YAML file(s).
      1. **Type** - Selection `Github`.
      2. **Repository** - Repository name in the format of `org/repo`
      3. **Reference** - The branch name to pull configs from (usually `main`)
      4. **Path** - Path to the YAML file. This will be the path to a single component spec or a `Location` spec that points to multiple YAML files.
      5. Repeat this substep to add more targets/files as needed across any number of repositories.
4. Click **Create setting** button to finalize the catalog setting creation.

### File Formats

> 📘 Note:
>
> Currently, FireHydrant only supports `Component` specs and `Location` specs that point to other `Component` specs.

For a single component, you can specify the `kind` as `Component` and the service's parameters in the `spec` section, like so:

```yaml Single Service Spec YAML
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: Sample-component3
  description: sample backstage component
  tags:
    - microservice
spec:
  type: service
  lifecycle: experimental
  owner: Dalmatians
```

If you have multiple components, as mentioned above, you can configure multiple **Targets** that point at each of the files. Alternatively, to clean things up, you can define a single `Location` type spec that points at multiple other component specs:

```yaml Multi-Service Spec YAML
apiVersion: backstage.io/v1alpha1
kind: Location
metadata:
  name: example-components
  description: A collection of all services that the FireHydrant catalog should point to an ingest
spec:
  targets:
    - ./service_1.yaml
    - ./service_2.yaml
```

## Service Ingestion via API

### Create Catalog Setting

1. Navigate to **Catalog**, and then in the left navigation drawer, click **Catalog settings**.
2. Near the top right, click "+ Create catalog setting."
3. Enter parameters:
   1. **Name** - A name for the catalog setting.
   2. **Description** - A description for the catalog setting.
   3. **Provider** - Select `API Only`.
   4. **Format** - Select `backstage.io/v1alpha1`.
4. Click **Create setting** button to finalize the catalog setting creation. Once created, the setting will output a unique API path, similar to: `/v1/catalogs/72845d2d-77ca-4bc8-8d8e-a8ea16f15a42/ingest`.

From here, you can append to the FireHydrant base API URL `https://api.firehydrant.com//v1/catalogs/72845d2d-77ca-4bc8-8d8e-a8ea16f15a42/ingest` and use this endpoint for sending your Service Catalog configurations.

### Data Format

Ingestion via API supports the same general parameters (see \[next section]\(#parameter-mappings)), but the data will need to be converted to JSON. Once converted to JSON, the information is then inserted into the `data` parameter of the request. Note in the example below, the content in the `data` object matches the YAML spec but in JSON form:

```json JSON Request Body
{
  "encoding": "application/json",
  "data": {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "Component",
    "metadata": {
      "name": "API-Component1",
      "description": "sample backstage component",
      "tags": [
        "microservice",
        "svc1",
        "prod"
      ]
    },
    "spec": {
      "type": "service",
      "lifecycle": "experimental",
      "owner": "SRE (FireHydrant)"
    }
  }
}
```

## Parameter Mappings

The following parameters in the Backstage specs are supported when ingesting and mapping to FireHydrant:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Backstage Field
      </th>

      <th>
        FireHydrant Ingested Field
      </th>

      <th>
        Additional Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `metadata.name`
      </td>

      <td>
        `name`
      </td>

      <td>
        The ingested service's name will be `Component:{namespace}/{name}`.
      </td>
    </tr>

    <tr>
      <td>
        `metadata.description`
      </td>

      <td>
        `description`
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `metadata.namespace`
      </td>

      <td>
        `name`
      </td>

      <td>
        The namespace is incorporated into the service's name when ingested: `Component:{namespace}/{name}`.

        If no namespace is provided, then the default value is `default`.
      </td>
    </tr>

    <tr>
      <td>
        `metadata.tags`
      </td>

      <td>
        `labels['tags']`
      </td>

      <td>
        The tags in the metadata are imported as semi-colon delimited values under the `keys` tag. For example, multiple tags (`microservice`, `prod`, `svc1`) will be imported as:\
        `tags`: `microservice;prod;svc1`
      </td>
    </tr>

    <tr>
      <td>
        `metadata.links`
      </td>

      <td>
        `links`
      </td>

      <td>
        Links in the metadata are included as links in the service
      </td>
    </tr>

    <tr>
      <td>
        `spec.lifecycle`
      </td>

      <td>
        `labels:lifecycle`
      </td>

      <td>
        Added as a value to the `lifecycle` label.
      </td>
    </tr>

    <tr>
      <td>
        `spec.type`
      </td>

      <td>
        `labels:type`
      </td>

      <td>
        Added as a value to the `type` label.
      </td>
    </tr>

    <tr>
      <td>
        `spec.system`
      </td>

      <td>
        `labels:system`
      </td>

      <td>
        Added as a value to the `system` label.
      </td>
    </tr>

    <tr>
      <td>
        `spec.owner`
      </td>

      <td>
        `Owning Team`
      </td>

      <td>
        The `owner` will be set as the owning team on FireHydrant. **The name must match the team name in FireHydrant exactly.**
      </td>
    </tr>
  </tbody>
</Table>

### Parameters Not Currently Supported

* Any `metadata` fields not mentioned above
  * E.g., `metadata.annotations`
* Any `relations` field
* Any `spec` fields not mentioned above
  * E.g., `spec.consumesApis`, `spec.dependsOn`, etc.