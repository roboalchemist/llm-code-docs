# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/packages/java.md

# Java

In this example you are going to create a `mavenDependencies` blueprint that ingests Maven packages using a combination of Port's [API](/build-your-software-catalog/custom-integration/api/.md) and [webhook functionality](/build-your-software-catalog/custom-integration/webhook/.md).

To ingest the Maven dependencies to Port, a script that sends information about packages according to the webhook configuration is used.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Create the following blueprint definitions and webhook configuration:

Maven dependency blueprint

Create in Port

```
{
  "identifier": "mavenDependency",
  "description": "This blueprint represents a Maven dependency",
  "title": "Maven Dependency",
  "icon": "java",
  "schema": {
    "properties": {
      "groupId": {
        "icon": "DefaultProperty",
        "title": "Group ID",
        "description": "The group ID of the dependency package",
        "type": "string"
      },
      "artifactId": {
        "type": "string",
        "title": "Artifact ID",
        "description": "The artifact ID of the dependency package"
      },
      "version": {
        "type": "string",
        "title": "Version",
        "description": "The version of the dependency"
      },
      "scope": {
        "type": "string",
        "title": "Scope",
        "description": "The scope of the dependency (e.g., compile, test, etc.)"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Maven webhook configuration

```
{
  "identifier": "mavenDependencyMapper",
  "title": "Maven Dependency Mapper",
  "description": "A webhook configuration to map Maven dependencies to Port",
  "icon": "Java",
  "mappings": [
    {
      "blueprint": "mavenDependency",
      "entity": {
        "identifier": ".body.artifactId",
        "title": ".body.groupId",
        "properties": {
          "groupId": ".body.groupId",
          "artifactId": ".body.artifactId",
          "version": ".body.version",
          "scope": ".body.scope"
        }
      }
    }
  ],
  "enabled": true
}
```

Maven Bash script

```
#!/bin/bash
set -e

# Create or clear the output file
echo "[]" > output.json

# Extract dependencies from pom.xml
mapfile -t dependencies < <(xmlstarlet sel -N x=http://maven.apache.org/POM/4.0.0 -t -m '//x:dependency' -v 'concat(x:groupId, ":", x:artifactId, ":", x:version, ":", x:scope)' -n pom.xml)

# Parse each dependency into a package JSON
for dependency in "${dependencies[@]}"; do
    # Split line into an array
    IFS=':' read -r -a parts <<< "$dependency"

    # Assign array items to variables
    groupId="${parts[0]}"
    artifactId="${parts[1]}"
    version="${parts[2]}"
    scope="${parts[3]}"

    # Create the package JSON
    package_json=$(jq -n \
        --arg gi "$groupId" \
        --arg ai "$artifactId" \
        --arg v "$version" \
        --arg s "$scope" \
        '{
            groupId: $gi,
            artifactId: $ai,
            version: $v,
            scope: $s
        }')

    # Add the package JSON to the output file
    jq --argjson p "$package_json" '. += [$p]' output.json > temp.json && mv temp.json output.json
    # Send the package JSON to the webhook
    curl --location 'https://ingest.getport.io/YOUR_WEBHOOK_URL' \
        --header 'Content-Type: application/json' \
        --data "$package_json"
done
```

note

* The script utilizes the `mapfile` command, which is a built-in command in the Bash shell, to read lines from the `pom.xml` file and store them in an array. Please note that this command may not be available in all shells by default. If you are using a different shell such as Dash or Zsh, you may need to switch to Bash or modify the script to achieve a similar functionality.
* The script relies on the `jq` command for manipulating JSON data. It is used to create JSON objects based on the package details extracted from the `go.mod` file and append these objects to an output JSON file. It is important to note that `jq` is a powerful JSON processor for the command-line, but it is not typically included in many systems by default. You may need to install it separately to use it.

## Parsing `pom.xml` file and sending dependency data to Port[â](#parsing-pomxml-file-and-sending-dependency-data-to-port "Direct link to parsing-pomxml-file-and-sending-dependency-data-to-port")

The following section outlines how to use the mapper script to send data from the `pom.xml` file to Port.

### Script Usage[â](#script-usage "Direct link to Script Usage")

1. Copy the script into a file in the root of your Java project. Make sure your `pom.xml` file is also located in the root of the project;

2. Make the script executable. For instance, if you named the script `parse_and_send.sh`, you would use the following command:

   ```
   chmod +x parse_and_send.sh
   ```

3. Run the script:

   ```
   ./parse_and_send.sh
   ```

Done! After the script has run, it will automatically injest Maven dependencies into Port via HTTP Requests
