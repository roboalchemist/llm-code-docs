# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/pdso-maintain-data-optimizer-metadata-cp/pdso-recovery-mode-explained.md

# Data Optimizer recovery mode

In recovery mode, the Pentaho Data Optimizer volume operates with its metadata store in non-authoritative mode while recovering file system metadata. The term “non-authoritative” means that the contents of the local metadata store might be incomplete. As a result, certain metadata inquiries can only be serviced by making external API calls to the S3 storage device. The metadata retrieved from the S3 storage device is cached to the local metadata store, reducing the need for future external API calls. Data Optimizer volumes are fully functional while in recovery mode, though performance might be affected.
