# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/pdso-maintain-data-optimizer-metadata-cp.md

# Maintain Data Optimizer metadata

Each Pentaho Data Optimizer volume maintains an authoritative local data store that contains the metadata of all files and directories stored by the instance. The term “authoritative” means that the metadata in the store is complete, current, and trusted. The authoritative local metadata store gives significant performance benefits, allowing the Data Optimizer volume to handle metadata inquiries internally without making external API calls to the S3 storage device.

If the local metadata store for a Data Optimizer volume becomes lost or corrupted, you need to recover the metadata store. For example, corruption might occur if the metadata is stored on a failed disk drive. Recovering the store involves relocating the store, putting the Data Optimizer volume in recovery mode, and running the recovery procedure.
