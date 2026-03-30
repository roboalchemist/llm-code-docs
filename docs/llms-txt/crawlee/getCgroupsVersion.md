# Source: https://crawlee.dev/js/api/utils/function/getCgroupsVersion.md

# getCgroupsVersion<!-- -->

### Callable

* ****getCgroupsVersion**(forceReset): Promise\<null | V1 | V2>

***

* gets the cgroup version by checking for a file at /sys/fs/cgroup/memory

  ***

  #### Parameters

  * ##### optionalforceReset: boolean

  #### Returns Promise\<null | V1 | V2>

  "V1" or "V2" for the version of cgroup or null if cgroup is not found.
