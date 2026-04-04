# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/pdso-hcp-configuration-troubleshooting.md

# Hitachi Content Platform (HCP) configuration troubleshooting

To troubleshoot Hitachi Content Platform (HCP) configuration issues, verify the following:

1. HCP is reachable over the network at ports 80/443 from the DataNode.
2. HCP is properly configured according to the instructions in this guide and the HCP documentation.
   * Your user credentials are correct, and your user has **Namespace Management** permission selected.
3. HCP **Hard Quotas** and **Namespace Quotas** have not been exceeded.
