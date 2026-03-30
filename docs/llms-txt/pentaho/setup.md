# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/setup.md

# Setup

Modify `…\system\karaf\etc\pentaho.metaverse.cfg` (Client & Pentaho Server when needed):

* You need to enable lineage explicitly by setting **lineage.execution.runtime** = `on`
* Modify the default folder for lineage GraphML files accordingly: `lineage.execution.output.folder=./pentaho-lineage-output`
* Set **lineage.execution.generation.strategy** = `latest` (by default)

After the execution of a job or transformation, the GraphML files are generated in the defined folder.
