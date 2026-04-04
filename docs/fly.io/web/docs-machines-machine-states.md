# Source: https://fly.io/docs/machines/machine-states/

Title: Machine states and lifecycle

URL Source: https://fly.io/docs/machines/machine-states/

Published Time: Thu, 26 Feb 2026 22:12:43 GMT

Markdown Content:
Machine states and lifecycle · Fly Docs
===============

[Skip to content](https://fly.io/docs/machines/machine-states/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Docs Index](https://fly.io/docs/)[Fly Machines](https://fly.io/docs/machines/)
*   [Introduction to Fly Machines](https://fly.io/docs/machines/overview/)

[Machines API](https://fly.io/docs/machines/api/)Toggle Machines API section
*   [Working with the Machines API](https://fly.io/docs/machines/api/working-with-machines-api/)
*   [Apps](https://fly.io/docs/machines/api/apps-resource/)
*   [Certificates](https://fly.io/docs/machines/api/certificates-resource/)
*   [Machines](https://fly.io/docs/machines/api/machines-resource/)
*   [Tokens](https://fly.io/docs/machines/api/tokens-resource/)
*   [Volumes](https://fly.io/docs/machines/api/volumes-resource/)
*   [OpenAPI Specification](https://docs.machines.dev/#description/introduction)

Machines and flyctl Toggle Machines and flyctl section
*   [Run a new Machine](https://fly.io/docs/machines/flyctl/fly-machine-run/)
*   [Update a Machine](https://fly.io/docs/machines/flyctl/fly-machine-update/)

Guides and Examples Toggle Guides and Examples section
*   [Machine placement and regional capacity](https://fly.io/docs/machines/guides-examples/machine-placement/)
*   [Machine restart policy](https://fly.io/docs/machines/guides-examples/machine-restart-policy/)
*   [Machine sizing](https://fly.io/docs/machines/guides-examples/machine-sizing/)
*   [Multi-container Machines](https://fly.io/docs/machines/guides-examples/multi-container-machines/)
*   [Network policies](https://fly.io/docs/machines/guides-examples/network-policies/)
*   [Run user code on Fly Machines](https://fly.io/docs/machines/guides-examples/functions-with-machines/)
*   [One app per customer - why?](https://fly.io/docs/machines/guides-examples/one-app-per-user-why/)

Reference Toggle Reference section
*   [Machine states](https://fly.io/docs/machines/machine-states/)
*   [The Machine runtime environment](https://fly.io/docs/machines/runtime-environment/)
*   [CPU Performance](https://fly.io/docs/machines/cpu-performance/)
*   [flyctl Machine commands](https://fly.io/docs/flyctl/machine/)

--- title: Machine states and lifecycle layout: docs nav: machines toc: true --- Fly Machines go through a series of lifecycle states during creation, updates, shutdown, and deletion. If you're automating deployments, coordinating Machine pools, or writing tools against the Machines API, understanding these states can help you make better decisions. ## Machine state vs. machine version state Each Machine has a single Machine ID, but every change (like updating the image or resources) creates a new Machine version. It's important to distinguish between: - Overall Machine state – represents the active version of the Machine. - Machine version state – represents the state of a specific version of a Machine. If you query a Machine without specifying a version, the API returns the current active version's state. If you query an older version, the API may return a terminal state like `replaced`. ## Machine state types ### Persistent states These states remain until you take action (or something fails). | State | Description | |-------|-------------| | `created` | Initial status. Machine has been created but not yet started | | `started` | Running and network-accessible | | `stopped` | Exited, either on its own or explicitly stopped | | `suspended` | Suspended to disk; will attempt to resume on next start | | `failed` | Machine encountered an error and could not start successfully | ### Transient states These are short-lived. The Machine will move to a new state automatically. | State | Description | |-------|-------------| | `creating` | Machine is being initialized | | `starting` | Transitioning from stopped or suspended to started | | `stopping` | Transitioning from started to stopped | | `restarting` | Machine is restarting | | `suspending` | Transitioning from started to suspended | | `destroying` | User asked for the Machine to be completely removed | | `launch_failed` | Machine failed to launch; will transition to destroyed | | `updating` | Machine is being updated to a new version | | `replacing` | User-initiated configuration change (image, VM size, etc.) in progress | ### Terminal states These are final states that a Machine or its version won't exit from. | State | Description | |-------|-------------| | `destroyed` | No longer exists | | `replaced` | Machine version was replaced by a newer one (applies to version-specific queries only). If you query an older version by ID, the API will always return replaced for that version, even if the Machine is currently running. | | `migrated` | Machine has been moved to a new host; previous version is no longer active | ## Machine state lifecycle diagrams ### Overall Machine state lifecycle ![Machine state lifecycle diagram](/docs/images/mermaid-diagram-1.png) ### Machine version state transitions ![Machine version state transitions diagram](/docs/images/mermaid-diagram-2.png) ## Update and versioning behavior When you update a Machine: 1. A new Machine version is created with the updated configuration. 2. The previous version is marked as `replaced`. 3. The new version becomes the active version and: - May stay in `created` if `skip_launch` is set to true. - May transition to `started` by default. - May transition to `stopped`, depending on how the update was triggered and the config used. Machines are launched automatically upon creation or after an update unless `skip_launch` is explicitly set. This flag allows you to create or update a Machine without starting it immediately. If you query an old version by version ID, you may see `replaced`. To always get the current state, query the Machine without specifying a version. ## Diagnosing stuck Machines If a Machine stays in a transient state for an extended time, it might be stuck ("wedged"). The following thresholds can help you decide: - `starting`, `stopping`, `restarting`, or `destroying` > 5 minutes (this can depend on the configured `kill_timeout`) - `updating` > 10 minutes To troubleshoot: 1. Check machine events via the Machines API. 2. Try stopping and starting the Machine. 3. If needed, contact Fly.io support with the Machine ID. ## Important Machine state considerations - `replaced` applies only to old versions and is terminal for that version. If you query an older version by ID, the API will always return `replaced` for that version, even if the Machine is currently running. - `migrated` indicates the Machine was moved to a new host and is no longer active. - Machines in `suspended` preserve memory and disk state, and resume faster than `stopped`. - The `launch_failed` state is usually unrecoverable and transitions to `destroyed`. - Machines in `failed` may be recoverable. You can try restarting, stopping, or destroying them. ## Related docs - [Machines API reference](/docs/machines/api/) - [Working with Machines](/docs/machines/) - [Fly machine update command](/docs/machines/flyctl/fly-machine-update/) 

[Docs](https://fly.io/docs/)[Fly Machines](https://fly.io/docs/machines)Machine states and lifecycle
Machine states and lifecycle
============================

Fly Machines go through a series of lifecycle states during creation, updates, shutdown, and deletion. If you’re automating deployments, coordinating Machine pools, or writing tools against the Machines API, understanding these states can help you make better decisions.

[](https://fly.io/docs/machines/machine-states/#machine-state-vs-machine-version-state)Machine state vs. machine version state
------------------------------------------------------------------------------------------------------------------------------

Each Machine has a single Machine ID, but every change (like updating the image or resources) creates a new Machine version. It’s important to distinguish between:

*   Overall Machine state – represents the active version of the Machine. 
*   Machine version state – represents the state of a specific version of a Machine. 

If you query a Machine without specifying a version, the API returns the current active version’s state. If you query an older version, the API may return a terminal state like `replaced`.

[](https://fly.io/docs/machines/machine-states/#machine-state-types)Machine state types
---------------------------------------------------------------------------------------

### [](https://fly.io/docs/machines/machine-states/#persistent-states)Persistent states

These states remain until you take action (or something fails).

Wrap text

| State | Description |
| --- | --- |
| `created` | Initial status. Machine has been created but not yet started |
| `started` | Running and network-accessible |
| `stopped` | Exited, either on its own or explicitly stopped |
| `suspended` | Suspended to disk; will attempt to resume on next start |
| `failed` | Machine encountered an error and could not start successfully |

### [](https://fly.io/docs/machines/machine-states/#transient-states)Transient states

These are short-lived. The Machine will move to a new state automatically.

Wrap text

| State | Description |
| --- | --- |
| `creating` | Machine is being initialized |
| `starting` | Transitioning from stopped or suspended to started |
| `stopping` | Transitioning from started to stopped |
| `restarting` | Machine is restarting |
| `suspending` | Transitioning from started to suspended |
| `destroying` | User asked for the Machine to be completely removed |
| `launch_failed` | Machine failed to launch; will transition to destroyed |
| `updating` | Machine is being updated to a new version |
| `replacing` | User-initiated configuration change (image, VM size, etc.) in progress |

### [](https://fly.io/docs/machines/machine-states/#terminal-states)Terminal states

These are final states that a Machine or its version won’t exit from.

Wrap text

| State | Description |
| --- | --- |
| `destroyed` | No longer exists |
| `replaced` | Machine version was replaced by a newer one (applies to version-specific queries only). If you query an older version by ID, the API will always return replaced for that version, even if the Machine is currently running. |
| `migrated` | Machine has been moved to a new host; previous version is no longer active |

[](https://fly.io/docs/machines/machine-states/#machine-state-lifecycle-diagrams)Machine state lifecycle diagrams
-----------------------------------------------------------------------------------------------------------------

### [](https://fly.io/docs/machines/machine-states/#overall-machine-state-lifecycle)Overall Machine state lifecycle

![Image 1: Machine state lifecycle diagram](https://fly.io/docs/images/mermaid-diagram-1.png)

### [](https://fly.io/docs/machines/machine-states/#machine-version-state-transitions)Machine version state transitions

![Image 2: Machine version state transitions diagram](https://fly.io/docs/images/mermaid-diagram-2.png)

[](https://fly.io/docs/machines/machine-states/#update-and-versioning-behavior)Update and versioning behavior
-------------------------------------------------------------------------------------------------------------

When you update a Machine:

1.   A new Machine version is created with the updated configuration. 
2.   The previous version is marked as `replaced`. 
3.   The new version becomes the active version and: 
    *   May stay in `created` if `skip_launch` is set to true. 
    *   May transition to `started` by default. 
    *   May transition to `stopped`, depending on how the update was triggered and the config used. 

Machines are launched automatically upon creation or after an update unless `skip_launch` is explicitly set. This flag allows you to create or update a Machine without starting it immediately.

If you query an old version by version ID, you may see `replaced`. To always get the current state, query the Machine without specifying a version.

[](https://fly.io/docs/machines/machine-states/#diagnosing-stuck-machines)Diagnosing stuck Machines
---------------------------------------------------------------------------------------------------

If a Machine stays in a transient state for an extended time, it might be stuck (“wedged”). The following thresholds can help you decide:

*   `starting`, `stopping`, `restarting`, or `destroying`> 5 minutes (this can depend on the configured `kill_timeout`) 
*   `updating`> 10 minutes 

To troubleshoot:

1.   Check machine events via the Machines API. 
2.   Try stopping and starting the Machine. 
3.   If needed, contact Fly.io support with the Machine ID. 

[](https://fly.io/docs/machines/machine-states/#important-machine-state-considerations)Important Machine state considerations
-----------------------------------------------------------------------------------------------------------------------------

*   `replaced` applies only to old versions and is terminal for that version. If you query an older version by ID, the API will always return `replaced` for that version, even if the Machine is currently running. 
*   `migrated` indicates the Machine was moved to a new host and is no longer active. 
*   Machines in `suspended` preserve memory and disk state, and resume faster than `stopped`. 
*   The `launch_failed` state is usually unrecoverable and transitions to `destroyed`. 
*   Machines in `failed` may be recoverable. You can try restarting, stopping, or destroying them. 

[](https://fly.io/docs/machines/machine-states/#related-docs)Related docs
-------------------------------------------------------------------------

*   [Machines API reference](https://fly.io/docs/machines/api/)
*   [Working with Machines](https://fly.io/docs/machines/)
*   [Fly machine update command](https://fly.io/docs/machines/flyctl/fly-machine-update/)

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmachines%2Fmachine-states.html.markerb)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Machine+states+and+lifecycle%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmachines%2Fmachine-states%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmachines%2Fmachine-states.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Machine+states+and+lifecycle%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/machines/machine-states.html.markerb)

[On this page](https://fly.io/docs/machines/machine-states/#)
*   [Machine state vs. machine version state](https://fly.io/docs/machines/machine-states/#machine-state-vs-machine-version-state)
*   [Machine state types](https://fly.io/docs/machines/machine-states/#machine-state-types)
    *   [Persistent states](https://fly.io/docs/machines/machine-states/#persistent-states)
    *   [Transient states](https://fly.io/docs/machines/machine-states/#transient-states)
    *   [Terminal states](https://fly.io/docs/machines/machine-states/#terminal-states)

*   [Machine state lifecycle diagrams](https://fly.io/docs/machines/machine-states/#machine-state-lifecycle-diagrams)
    *   [Overall Machine state lifecycle](https://fly.io/docs/machines/machine-states/#overall-machine-state-lifecycle)
    *   [Machine version state transitions](https://fly.io/docs/machines/machine-states/#machine-version-state-transitions)

*   [Update and versioning behavior](https://fly.io/docs/machines/machine-states/#update-and-versioning-behavior)
*   [Diagnosing stuck Machines](https://fly.io/docs/machines/machine-states/#diagnosing-stuck-machines)
*   [Important Machine state considerations](https://fly.io/docs/machines/machine-states/#important-machine-state-considerations)
*   [Related docs](https://fly.io/docs/machines/machine-states/#related-docs)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmachines%2Fmachine-states.html.markerb)
