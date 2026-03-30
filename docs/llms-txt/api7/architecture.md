# Source: https://docs.api7.ai/enterprise-whitepaper/architecture.md

# Source: https://docs.api7.ai/enterprise-whitepaper/tags/architecture.md

# Source: https://docs.api7.ai/enterprise/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.8.x/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.7.x/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.6.x/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.5.x/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.4.x/introduction/architecture.md

# Source: https://docs.api7.ai/enterprise/3.3.x/introduction/architecture.md

# Architecture

## How It Works[â](#how-it-works "Direct link to How It Works")

As the high-performance cloud-native API gateway built on NGINX, API7 Enterprise utilizes a scalable, flexible architecture to meet the requirements of enterprise-grade API management. This foundation handles security, traffic control, and resilience at scale.

![how api7 works](https://static.api7.ai/uploads/2024/03/20/AcYkJH1M_%E6%9E%B6%E6%9E%84%E5%9B%BE-%E8%8B%B1%E6%96%87.jpg)

* **Data Plane**: The API7 Gateway component handles all API traffic. After configuring routing rules, administrators can route incoming requests to appropriate upstream services based on predefined criteria. API7 Enterprise provides over 60 built-in plugins to address common requirements like authentication, traffic control, transformations, analytics, etc. If needed, you can also develop custom plugins in Lua, Java, Go, or Python and integrate them with API7 Enterprise to intervene at various stages of the request/response lifecycle.

* **Control Plane**: API7 Enterprise simplifies gateway management through an intuitive web interface (API7 Dashboard). Key capabilities include monitoring APIs, analyzing traffic, auditing logs, and switching between gateway groups. This centralized API Dashboard streamlines gateway administration and enhances visibility into API operations.

tip

For production deployments, API7 Enterprise also supports MySQL and OceanBase in place of PostgreSQL. Deployment is supported only through container-based methods, such as Docker, or through container orchestration platforms like Kubernetes. Installation using deb or rpm packages is not supported.
