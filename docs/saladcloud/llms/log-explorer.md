# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/log-explorer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Explorer

*Last Updated: January 6, 2026*

The Log Explorer provides access to container and system logs across all container groups, allowing you to run detailed
queries. Once you have selected an organization, the Log Explorer is accessible from the left menu. You can also access
it from the Container Logs or System Events tab of a Container Group, where the query will be pre-populated for the
group you were viewing

There are two interfaces for creating queries in the Log Explorer: the Query Builder and the Code Builder. The Query
Builder offers a simple graphical interface to build log queries without needing to know the
[Salad Log Query Language](https://docs.salad.com/container-engine/reference/log-queries). Use the dropdowns and input
fields to specify filters for your logs. The Code Builder allows you to write queries directly in the Salad Log Query
Language for more advanced capabilities.

After you run a query, the results are displayed in the table below the query interface.

<img src="https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=02b5a4bb1cac01bd8a96bd255507d2cc" alt="Log Explorer Portal Screenshot" data-og-width="1864" width="1864" data-og-height="588" height="588" data-path="container-engine/images/portal-log-explorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=280&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=c41ffa684450f46fd1e529181fcb26bd 280w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=560&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=5c3022da8030ea48eab5331bcb0f9bf0 560w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=840&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=19bd172a2a340ff5d2abea2520f985e3 840w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=1100&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=b62d92acda7aeb17a1d2eb5e7587c961 1100w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=1650&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=d9ead1853bad6be47466af7fd6607ab5 1650w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-log-explorer.png?w=2500&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=04255b4a9067889253ecad6f3aa03b39 2500w" />
