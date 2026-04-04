# Source: https://coolify.io/docs/services/mage-ai.md

---
url: /docs/services/mage-ai.md
description: 'Build, run, and manage data pipelines for integrating and transforming data.'
---

## What is Mage AI?

Mage AI (Mage OSS) is a self-hosted development environment designed to help
teams create production-grade data pipelines with confidence.

Ideal for automating ETL tasks, architecting data flow, or orchestrating
transformations — all in a fast, notebook-style interface powered by modular
code.

## Default Credentials

On a fresh deployment, you can log in with the following details:

```
USERNAME: admin@admin.com
PASSWORD: admin
```

## Issue with Older CPUs

Mage AI requires modern CPU features to be available. On older
devices, you may see the error:

```
The following required CPU features were not detected:
  sse4.2, popcnt, avx, avx2, fma, bmi1, bmi2, lzcnt, pclmulqdq
```

For more details, refer to the [following issue](https://github.com/pola-rs/polars/issues/15404).

## Links

* [Official website](https://mage.ai/?utm_source=coolify.io)
* [GitHub](https://github.com/mage-ai/mage-ai?utm_source=coolify.io)
