# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/pre-requisites-for-installing-master-data-management/network-configuration.md

# Network configuration

To install Pentaho Data Mastering, you must open the following ports in the firewall settings and respective security rules. The CIDRs are for each port to accept the traffic:

| Type       | Protocol | Port range | Source (Customer defined CIDR) |
| ---------- | -------- | ---------- | ------------------------------ |
| Custom TCP | TCP      | 4317       | 0.0.0.0/0                      |
| Custom TCP | TCP      | 13133      | 0.0.0.0/0                      |
| SSH        | TCP      | 22         | 0.0.0.0/0                      |
| PostgreSQL | TCP      | 5432       | 0.0.0.0/0                      |
| Custom TCP | TCP      | 8888       | 0.0.0.0/0                      |
| Custom TCP | TCP      | 5080       | 0.0.0.0/0                      |
| Custom TCP | TCP      | 24224      | 0.0.0.0/0                      |
| HTTP       | TCP      | 80         | 0.0.0.0/0                      |
| Custom TCP | TCP      | 8080       | 0.0.0.0/0                      |
| Custom TCP | TCP      | 4318       | 0.0.0.0/0                      |
