# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/general-configuration-problems/zookeeper-problems.md

# Zookeeper problems

| Symptoms                                                          | Common Causes                                                                                                  | Common Resolutions                                                                                                                                              |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cannot connect to Zookeeper                                       | <ul><li>Firewall is impeding connection with the Zookeeper service.</li><li>Other networking issues.</li></ul> | <ul><li>Verify that a firewall is not impeding the connection.</li></ul>                                                                                        |
| Zookeeper hostname or port not found or does not resolve properly | <ul><li>Hostname/IP Address and Port name is missing or is incorrect.</li></ul>                                | <ul><li>Try to connect to the Zookeeper nodes using ping or another method.</li><li>Verify that the Hostname/IP Address and Port numbers are correct.</li></ul> |
