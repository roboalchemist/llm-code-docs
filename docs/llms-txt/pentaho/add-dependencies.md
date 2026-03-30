# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/add-dependencies.md

# Add dependencies

Add Maven dependencies to pentaho-metaverse-api and kettle jars in your `pom.xml` file.

```xml
<dependency>
  <groupId>pentaho</groupId>
  <artifactId>pentaho-metaverse-api</artifactId>
  <version>7.1.0.0-12</version>
  <type>bundle</type>
</dependency>

<dependency>
  <groupId>pentaho-kettle</groupId>
  <artifactId>kettle-core</artifactId>
  <version>7.1.0.0-12</version>
</dependency>

<dependency>
  <groupId>pentaho-kettle</groupId>
  <artifactId>kettle-engine</artifactId>
  <version>7.1.0.0-12</version>
</dependency>
```
