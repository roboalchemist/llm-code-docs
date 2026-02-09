# Source: https://www.aptible.com/docs/reference/aptible-metadata-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Aptible Metadata Variables

Aptible injects the following metadata keys as environment variables:

* `APTIBLE_PROCESS_TYPE`

  * Represents the name of the [Service](/core-concepts/apps/deploying-apps/services) this container belongs to. For example, if the [Procfile](/how-to-guides/app-guides/define-services) defines services like `web` and `worker`.

  * Then, the containers for the web Service will run with `APTIBLE_PROCESS_TYPE=web`, and the containers for the worker Service will run with `APTIBLE_PROCESS_TYPE=worker`.

  * If there is no Procfile and users choose to use an [Implicit Service](/how-to-guides/app-guides/define-services#implicit-service-cmd) instead, the variable is set to `APTIBLE_PROCESS_TYPE=cmd`.

* `APTIBLE_PROCESS_INDEX`

  * All containers for a given [Release](/core-concepts/apps/deploying-apps/releases/overview) of a Service are assigned a unique 0-based process index.

  * For example, if your web service is [scaled](/core-concepts/scaling/overview) to 2 containers, one will have `APTIBLE_PROCESS_INDEX=0`, and the other will have `APTIBLE_PROCESS_INDEX=1`.

* `APTIBLE_PROCESS_CONTAINER_COUNT`

  * This variable is a companion to `APTIBLE_PROCESS_INDEX`, and represents the total count of containers on the service. Note that this will only be present in app service containers (not in pre\_release, ephemeral/ssh, or database containers).

* `APTIBLE_CONTAINER_CPU_SHARE`

  * Provides the vCPU share for the container, matching the ratios in our documentation for [­container profiles](/core-concepts/scaling/container-profiles). Format will be provided in the following format: 0.125, 0.5, 1.0, etc.

* `APTIBLE_CONTAINER_PROFILE`

* `APTIBLE_CONTAINER_SIZE`

  * This variable represents the memory limit in MB of the Container. See [Memory Limits](/core-concepts/scaling/memory-limits) for more information.

* `APTIBLE_LAYER`

  * This variable represents whether the container is an [App](/core-concepts/apps/overview) or [Database](/core-concepts/managed-databases/managing-databases/overview) container using App or Database values.

* `APTIBLE_GIT_REF`

* `APTIBLE_ORGANIZATION_HREF`

  * Aptible API URL representing the [Organization](/core-concepts/security-compliance/access-permissions) this container belongs to.

* `APTIBLE_APP_HREF`

  * Aptible API URL representing the [App](/core-concepts/apps/overview) this container belongs to, if any.

* `APTIBLE_DATABASE_HREF`

  * Aptible API URL representing the [Database](/core-concepts/managed-databases/managing-databases/overview) this container belongs to, if any.

* `APTIBLE_SERVICE_HREF`

  * Aptible API URL representing the Service this container belongs to, if any.

* `APTIBLE_RELEASE_HREF`

  * Aptible API URL representing the Release this container belongs to, if any.

* `APTIBLE_EPHEMERAL_SESSION_HREF`

  * Aptible API URL representing the current [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) this container belongs to, if any.

* `APTIBLE_USER_DOCUMENT`

  * Aptible injects an expired JWT object with user information.
    * The information available is id, email, name, etc.
    * Only available in [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions).

  ```
  decode_base64_url() {
      local len=$((${#1} % 4))
      local result="$1"
      if [ $len -eq 2 ]; then result="$1"'=='
      elif [ $len -eq 3 ]; then result="$1"'=' 
      fi
      echo "$result" | tr '_-' '/+' | openssl enc -d -base64
  }

  decode_jwt(){
      decode_base64_url $(echo -n $2 | cut -d "." -f $1) | sed 's/{/\n&\n/g;s/}/\n&\n/g;s/,/\n&\n/g' | sed 's/^  */  /'
  }

  # Decode JWT header
  alias jwth="decode_jwt 1"

  # Decode JWT Payload
  alias jwtp="decode_jwt 2"
  ```

  You can use the above script to decode the expired JWT object using `jwtp $APTIBLE_USER_DOCUMENT`

* `APTIBLE_RESOURCE_HREF`

  * Aptible uses this variable internally. Do not depend on this value.

* `APTIBLE_ALLOCATION`

  * Aptible uses this variable internally. Do not depend on this value.
