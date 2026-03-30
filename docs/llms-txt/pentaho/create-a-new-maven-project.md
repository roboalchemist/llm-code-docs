# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/create-a-new-maven-project.md

# Create a new Maven project

The easiest way to get started is to use the `karaf-bundle-archetype` to create a new Maven project, which generates a bundle artifact that works in a Karaf container.

```xml
mvn archetype:generate \
  -DarchetypeGroupId=org.apache.karaf.archetypes \
  -DarchetypeArtifactId=karaf-bundle-archetype \
  -DarchetypeVersion=2.2.11 \
  -DgroupId=your.company \
  -DartifactId=your-artifact-id \
  -Dversion=1.0-SNAPSHOT \
  -Dpackage=your.company.package \
```
