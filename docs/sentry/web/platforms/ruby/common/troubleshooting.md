---
---
title: Troubleshooting
description: "Learn how to troubleshoot your SDK setup."
---

## General

  Currently, every tag has a maximum character limit of 200 characters. Tags over the 200 character limit will become truncated, losing potentially important information. To retain this data, you can split data over several tags instead.

  For example, a 200+ character tagged request:

  `https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=161803398874989484820458683436563811772030917980576`

  The 200+ character request above will become truncated to:

  `https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=1618033988749894848`

## Profiling

  If you don't see any profiling data in [sentry.io](https://sentry.io), you can try the following:

  - Ensure that Tracing is enabled.
  - Ensure that the automatic instrumentation is sending performance data to Sentry by going to the **Performance** page
  in [sentry.io](https://sentry.io).
  - If the automatic instrumentation is not sending performance data, try using custom instrumentation.
  - Enable debug mode in the SDK and check the logs.

  ### Limitations

  Profiles for multi-threaded servers like `puma` might not capture frames correctly when async I/O is happening. This
  is a limitation of `stackprof`.

## Crons

You may not have linked errors to your monitor.

You may not have set up alerts for your monitor.

Our current data retention policy is 90 days.

Currently, we only support crontab expressions with five fields.

