# Source: https://docs.metasfresh.org/howto_collection/EN/metasfresh_architecture.html

Title: metasfresh Architecture

URL Source: https://docs.metasfresh.org/howto_collection/EN/metasfresh_architecture.html

Markdown Content:
[![Image 1: metasfresh logo and link to website](https://docs.metasfresh.org/images/metasfreshNEG_400px.png)](https://metasfresh.com/en/ "Visit metasfresh.com")

Wonach suchst Du?

What are you looking for?

Overview
--------

![Image 2: architecture](https://docs.metasfresh.org/images/metasfresh_architecture.png)

Service Details
---------------

| Service | Dev Language | Running on | Technologies |
| --- | --- | --- | --- |
| WebUI | Javascript | Apache / Nginx | React Redux, HTML5, PostCSS |
| WebAPI | Java 8 | Spring Boot | REST, JSON, Swagger, Spring, hazelcast, websocket |
| App | Java 8, SQL | Spring Boot | Jasper Reports, Application Dictionary |
| DB | SQL, PgSQL | Postgres (9.5+) | Application Dictionary |
| Reporting | JRXML | Spring Boot | [JasperReports® Library 6.5.1](https://community.jaspersoft.com/project/jasperreports-library/releases "Open Source Java Reporting Library") |
| elastic Search |  |  | Standard Elastic Search |
| RabbitMQ |  |  | Standard RabbitMQ |
| Java Client | Java 8 | Java JRE 8+ | Swing |
|  |  |  |  |
| **_Optional:_*** |  |  |  |
| Material Schedule | Java 8 | Spring Boot | Real-time calculation of material |
| Jasper Reports | Java 8 | Spring Boot | Render Jasper reports |

_* Can be run as a separate service._

* * *

[View source file on GitHub.com](https://github.com/metasfresh/metasfresh-documentation/blob/gh-pages/_howto_collection/EN/metasfresh_architecture.md "View this page's source file")
