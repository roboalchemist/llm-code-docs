# Source: https://docs.infrahub.app/topics/artifact.md

# Source: https://docs.infrahub.app/guides/artifact.md

# How to generate configuration artifacts from Jinja2 templates

Generate configuration files and other artifacts by combining Infrahub data with templates. This guide shows you how to create artifacts that automatically update when your infrastructure data changes.

For conceptual information about artifacts and their architecture, see [artifacts](/topics/artifact.md).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before starting this guide, ensure you have:

* A working Infrahub instance
* An existing Transformation (either [Jinja2](/guides/jinja2-transform.md) or [Python](/guides/python-transform.md))
* Access to create and modify schemas
* A Git repository connected to Infrahub

## Step 1: Enable artifact generation for your nodes[​](#step-1-enable-artifact-generation-for-your-nodes "Direct link to Step 1: Enable artifact generation for your nodes")

To generate artifacts for specific nodes, modify your schema to inherit from `CoreArtifactTarget`.

```
---
version: "1.0"
nodes:
  - name: Device
    namespace: Network
    display_label: "{{ name__value }}"
    inherit_from:
      - CoreArtifactTarget
    attributes:
      - name: name
        kind: Text
        label: Name
        optional: false
        unique: true
      - name: description
        kind: Text
        label: Description
        optional: true
```

Load the modified schema into Infrahub:

```
infrahubctl schema load /tmp/schema.yml
```

## Step 2: Create a target group[​](#step-2-create-a-target-group "Direct link to Step 2: Create a target group")

Create a Standard Group to define which objects will generate artifacts.

1. Navigate to the Groups section in the web interface
2. Create a new Standard Group named `DeviceGroup`
3. Add your target devices (`switch1`, `switch2`, `switch3`) as members

For detailed group creation steps, see [Creating a group](/guides/groups.md).

## Step 3: Define the artifact generation[​](#step-3-define-the-artifact-generation "Direct link to Step 3: Define the artifact generation")

Add an artifact definition to your repository's `.infrahub.yml` file:

```
artifact_definitions:
  - name: "Device configuration file"
    artifact_name: "device_configuration"
    parameters:
      name: "name__value"
    content_type: "text/plain"
    targets: "DeviceGroup"
    transformation: "device_config_transform"
```

This configuration specifies:

* **name**: Machine identifier (no spaces)
* **artifact\_name**: Human-readable label
* **parameters**: Values passed to the Transformation query
* **content\_type**: MIME type of the generated artifact
* **targets**: Group containing target objects
* **transformation**: Name of the Jinja2 or Python Transformation

For complete `.infrahub.yml` syntax, see [.infrahub.yml reference](/topics/infrahub-yml.md).

## Step 4: Deploy the artifact definition[​](#step-4-deploy-the-artifact-definition "Direct link to Step 4: Deploy the artifact definition")

Commit and push your changes to activate the artifact generation:

```
git add .
git commit -m "add device_configuration artifact definition"
git push origin main
```

The task workers will detect the repository change and create the artifact definition in the database.

## Step 5: Verify artifact generation[​](#step-5-verify-artifact-generation "Direct link to Step 5: Verify artifact generation")

Check that your artifacts are being generated correctly.

### Through the web interface[​](#through-the-web-interface "Direct link to Through the web interface")

1. Navigate to **Object Management** → **Artifacts**
2. Locate your generated artifacts in the list

![Artifact view](/assets/images/artifact_view-777fb5878c3215e4ec8c75e7035564e5.png)

3. Click on an artifact to view its content

![Artifact detail](/assets/images/artifact_detail-c200bf9e9f6ab6441f26557b43449922.png)

### Through object details[​](#through-object-details "Direct link to Through object details")

1. Navigate to a specific device (for example, `switch1`)

2) Select the **Artifacts** tab

3. View all artifacts generated for this object

## Step 6: Access generated artifacts[​](#step-6-access-generated-artifacts "Direct link to Step 6: Access generated artifacts")

Download or retrieve your artifacts using these methods:

### Web interface download[​](#web-interface-download "Direct link to Web interface download")

Click the download button on any artifact detail page.

### REST API access[​](#rest-api-access "Direct link to REST API access")

Download artifacts using the storage object endpoint (authentication required):

```
curl -H "X-INFRAHUB-KEY: <your-api-token>" \
  http://<INFRAHUB_HOST:INFRAHUB_PORT>/api/storage/object/<storage_identifier>
```

Copy the artifact ID from the artifact menu:

![Artifact menu](/assets/images/artifact_menu-39d8eebb0ed771074c03a119ddfaf5d1.png)

### Programmatic access[​](#programmatic-access "Direct link to Programmatic access")

Query artifacts through the GraphQL API for automation workflows.

## Validation[​](#validation "Direct link to Validation")

Confirm your artifact generation is working:

* ✓ artifact definitions appear in the web interface
* ✓ artifacts are generated for all group members
* ✓ Generated content matches your template expectations
* ✓ artifacts update when source data changes

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If artifacts aren't generating:

1. Check task worker logs for processing errors
2. Verify the Transformation name matches exactly
3. Ensure group members inherit from `CoreArtifactTarget`
4. Confirm the Git repository sync is working

## Next steps[​](#next-steps "Direct link to Next steps")

* [Create complex Transformations with Python](/guides/python-transform.md)
* [Use GraphQL queries in Transformations](/topics/transformation.md)
* [Automate artifact deployment with CI/CD](/topics/repository.md)
