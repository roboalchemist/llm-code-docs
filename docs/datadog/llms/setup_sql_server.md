# Source: https://docs.datadoghq.com/database_monitoring/setup_sql_server.md

---
title: Setting up SQL Server
description: Setting up Database Monitoring on a SQL Server database
breadcrumbs: Docs > Database Monitoring > Setting up SQL Server
---

# Setting up SQL Server

### SQL Server versions supported{% #sql-server-versions-supported %}

| Self-hosted     | Azure | Amazon RDS                                                                                                                                                                                                                                       | Google Cloud SQL | Note |
| --------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ---- |
| SQL Server 2012 | yes   | SQL Server 2012 reached its end of life on July 12, 2022. Database Monitoring continues to support SQL Server 2012 with [known limitations](https://docs.datadoghq.com/database_monitoring/setup_sql_server/troubleshooting/#known-limitations). |
| SQL Server 2014 | yes   | yes                                                                                                                                                                                                                                              | yes              |
| SQL Server 2016 | yes   | yes                                                                                                                                                                                                                                              | yes              |
| SQL Server 2017 | yes   | yes                                                                                                                                                                                                                                              | yes              | yes  |
| SQL Server 2019 | yes   | yes                                                                                                                                                                                                                                              | yes              | yes  |
| SQL Server 2022 | yes   | yes                                                                                                                                                                                                                                              | yes              | yes  |

For setup instructions, select your hosting type:

- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_sql_server/selfhosted)
- [RDS](https://docs.datadoghq.com/database_monitoring/setup_sql_server/rds)
- [Aurora](https://docs.datadoghq.com/database_monitoring/setup_sql_server/azure)
- [Google Cloud SQL](https://docs.datadoghq.com/database_monitoring/setup_sql_server/gcsql)
