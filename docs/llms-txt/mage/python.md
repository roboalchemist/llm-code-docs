# Source: https://docs.mage.ai/production/executors/python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Local python executor

> Local python executors are ran within the same container as the scheduler service.

You can customize the compute resource with the same way mentioned in this
[document](/production/configuring-production-settings/compute-resource).
section.

### Force local Python executor

If you want to use `local_python` executor when `DEFAULT_EXECUTOR_TYPE` is set to another executor type,
you can set the `executor_type` to `local_python_force`.


Built with [Mintlify](https://mintlify.com).