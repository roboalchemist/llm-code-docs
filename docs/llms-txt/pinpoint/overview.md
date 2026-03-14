# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.2.2/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.0/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.1/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.2/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.3/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.4.0/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.0/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.1/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.2/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.3/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.4/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.0/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.1/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.2/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.3/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.4/want-a-quick-tour/overview.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview.md

# Overview

Services nowadays often consist of many different components, communicating amongst themselves as well as making API calls to external services. How each and every transaction gets executed is often left as a blackbox. Pinpoint traces transaction flows between these components and provides a clear view to identify problem areas and potential bottlenecks.

* **ServerMap** - Understand the topology of any distributed systems by visualizing how their components are interconnected. Clicking on a node reveals details about the component, such as its current status, and transaction count.
* **Realtime Active Thread Chart** - Monitor active threads inside applications in real-time.
* **Request/Response Scatter Chart** - Visualize request count and response patterns over time to identify potential problems. Transactions can be selected for additional detail by **dragging over the chart**.

![Server Map](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media\&token=899f1043-030f-4df7-a52f-4433b6e2ca72)

* **CallStack** - Gain code-level visibility to every transaction in a distributed environment, identifying bottlenecks and points of failure in a single view.

![Call Stack](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-735f042f7dc51378efe3f24d2ce53e1f295409d4%2Fss_call-stack.png?alt=media\&token=4afcecf6-8d1a-48d5-b5b8-8d0e6c8e8647)

* **Inspector** - View additional details on the application such as CPU usage, Memory/Garbage Collection, TPS, and JVM arguments.

![Inspector](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-07c84a62894cf4307ed7dc6ab2f5e44013ca2892%2Fss_inspector.png?alt=media\&token=97d631ef-f05b-47fa-8059-36efa841278b)

## Architecture

![Pinpoint Architecture](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-fc010a909c9559db169703072bd0dccacc283078%2Fpinpoint-architecture.png?alt=media)
