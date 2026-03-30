# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.settings`

Prefect settings are defined using `BaseSettings` from `pydantic_settings`. `BaseSettings` can load setting values
from system environment variables and each additionally specified `env_file`.

The recommended user-facing way to access Prefect settings at this time is to import specific setting objects directly,
like `from prefect.settings import PREFECT_API_URL; print(PREFECT_API_URL.value())`.

Importantly, we replace the `callback` mechanism for updating settings with an "after" model\_validator that updates dependent settings.
After [https://github.com/pydantic/pydantic/issues/9789](https://github.com/pydantic/pydantic/issues/9789) is resolved, we will be able to define context-aware defaults
for settings, at which point we will not need to use the "after" model\_validator.


Built with [Mintlify](https://mintlify.com).