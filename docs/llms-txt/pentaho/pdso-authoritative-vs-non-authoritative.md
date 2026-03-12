# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/pdso-maintain-data-optimizer-metadata-cp/pdso-recovery-mode-explained/pdso-authoritative-vs-non-authoritative.md

# Authoritative vs non-authoritative

When authoritative (`RECOVERY_MODE=false`), the store is considered complete, that means if a file or folder is not in the store, it does not exist. In authoritative mode, all metadata requests are serviced from the local metadata store.

When non-authoritative (`RECOVERY_MODE=true`), the store is considered incomplete. The absence of a file or folder in the store can indicate that the entity does not exist, or it mean that the file or directory has not been accessed since recovery began. In non-authoritative mode, directory listings and metadata requests for records not previously cached in the local metadata store must be serviced by querying the S3 bucket.
