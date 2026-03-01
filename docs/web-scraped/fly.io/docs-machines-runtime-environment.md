# Source: https://fly.io/docs/machines/runtime-environment/

Title: The Machine Runtime Environment

URL Source: https://fly.io/docs/machines/runtime-environment/

Markdown Content:
[Docs](https://fly.io/docs/)[Fly Machines](https://fly.io/docs/machines)The Machine Runtime Environment
Environment variables make several kinds of information available within a Machine’s runtime environment. The values come from three sources:

*   [Secrets](https://fly.io/docs/reference/secrets)
*   [Environment variable settings](https://fly.io/docs/reference/configuration/#the-env-variables-section) from the Machine config 
*   Fly.io infrastructure, as detailed below 

[](https://fly.io/docs/machines/runtime-environment/#environment-variables)Environment variables
------------------------------------------------------------------------------------------------

* * *

### [](https://fly.io/docs/machines/runtime-environment/#fly_app_name)`FLY_APP_NAME`

**App name**: Each app running on Fly.io has a unique app name. This identifies the app for the user, and can also identify its Machines on their IPv6 private network, using internal DNS. For example, `syd.$FLY_APP_NAME.internal` can refer to the app’s Machines running in the `syd` region. Read more about [6PN Naming](https://fly.io/docs/networking/private-networking/#fly-io-internal-addresses) in the [Private Networking](https://fly.io/docs/networking/private-networking/) docs.

### [](https://fly.io/docs/machines/runtime-environment/#fly_machine_id)`FLY_MACHINE_ID`

**Machine ID**: The Machine’s unique ID on the Fly.io platform. This is the ID you use to target the Machine using flyctl and the Machines API. You can also see it in the [log](https://fly.io/docs/flyctl/logs/) messages emitted by the Machine.

### [](https://fly.io/docs/machines/runtime-environment/#fly_alloc_id)`FLY_ALLOC_ID`

**Allocation ID**: Same as the `FLY_MACHINE_ID`.

### [](https://fly.io/docs/machines/runtime-environment/#fly_region)`FLY_REGION`

**Region name**: The three-letter name of the region the Machine is running in. Details of current regions are listed in the [Regions](https://fly.io/docs/regions/) page. As an example, “ams” is the region name for Amsterdam.

Not to be confused with the [HTTP header](https://fly.io/docs/networking/request-headers/#fly-region)`Fly-Region`, which is where the connection was accepted from.

### [](https://fly.io/docs/machines/runtime-environment/#fly_public_ip)`FLY_PUBLIC_IP`

**IPV6 public IP**: The full public outbound IPV6 address for this Machine. Read more in the [Network Services](https://fly.io/docs/networking/services/#outbound-ip-addresses) section.

### [](https://fly.io/docs/machines/runtime-environment/#fly_image_ref)`FLY_IMAGE_REF`

**Docker image reference**: The name of the Docker image used to create the Machine. `registry.fly.io/my-app-name:deployment-01H9RK9EYO9PGNBYAKGXSHV0PH` is an example of the Docker Image Reference’s format.

Useful if your app needs to launch Machine instances of itself to scale background workers to zero and back, as in [Rails Background Jobs with Fly Machines](https://fly.io/ruby-dispatch/rails-background-jobs-with-fly-machines/).

### [](https://fly.io/docs/machines/runtime-environment/#fly_machine_version)`FLY_MACHINE_VERSION`

**Machine configuration version**: A version identifier associated with a specific Machine configuration. When you update a Machine’s configuration (including when you update its Docker image), it gets a new `FLY_MACHINE_VERSION`. Changing the Machine’s metadata using the metadata endpoint of the Machines API doesn’t trigger a new version. You can also find this value under the name `Instance ID` in the output of `fly machine status`.

### [](https://fly.io/docs/machines/runtime-environment/#fly_private_ip)`FLY_PRIVATE_IP`

**Private IPv6 address**: The IPv6 address of the Machine on its [6PN private network](https://fly.io/docs/networking/private-networking/).

### [](https://fly.io/docs/machines/runtime-environment/#fly_process_group)`FLY_PROCESS_GROUP`

**Process group**: The Fly Launch [process group](https://fly.io/docs/apps/processes) associated with the Machine, if any.

### [](https://fly.io/docs/machines/runtime-environment/#fly_vm_memory_mb)`FLY_VM_MEMORY_MB`

**Machine memory**: The memory allocated to the Machine, in MB. It’s the same value you’ll find under [https://fly.io/dashboard/personal/machines](https://fly.io/dashboard/personal/machines) and VM Memory in the output of `fly machine status`. Learn more about [Machine sizing](https://fly.io/docs/machines/guides-examples/machine-sizing/).

### [](https://fly.io/docs/machines/runtime-environment/#primary_region)`PRIMARY_REGION`

**Primary region**: This is set in your `fly.toml` or with the `--region` flag during deploys. Learn more about [configuring the primary region](https://fly.io/docs/reference/configuration/#primary-region).
