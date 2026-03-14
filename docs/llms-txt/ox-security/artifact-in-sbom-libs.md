# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/artifact-in-sbom-libs.md

# artifactInSbomLibs

Represents an artifact included in SBOM libraries, such as a container image.

### Examples

```graphql
type ArtifactInSbomLibs {
  image: String
  imageLink: String
  imageCreatedAt: String
  sha: String
  os: String
  osVersion: String
  baseImage: String
  baseImageVersion: String
  tag: String
  layer: String
  registryName: String
  source: String
}
```

### Fields

| Field                     | Description                                           | Supported fields |
| ------------------------- | ----------------------------------------------------- | ---------------- |
| image `String`            | Name of the container image                           |                  |
| imageLink `String`        | URL link to the container image                       |                  |
| imageCreatedAt `String`   | Creation date/time of the image (ISO 8601 string)     |                  |
| sha `String`              | SHA digest of the artifact/image                      |                  |
| os `String`               | Operating system used in the image                    |                  |
| osVersion `String`        | Version of the operating system                       |                  |
| baseImage `String`        | Base image name from which this image is derived      |                  |
| baseImageVersion `String` | Version of the base image                             |                  |
| tag `String`              | Tag assigned to the image                             |                  |
| layer `String`            | Specific layer identifier within the image            |                  |
| registryName `String`     | Name of the container registry hosting the image      |                  |
| source `String`           | Source of the artifact - public or connected registry |                  |

### References

#### Fields with this object

* [{} SbomLib.artifactInSbomLibs](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
