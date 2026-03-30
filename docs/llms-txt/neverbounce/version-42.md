# Source: https://developers.neverbounce.com/changelog/version-42.md

# Version 4.2

## Job Callbacks

Job callbacks enable your applications to react to updates to your verification jobs. This means you no longer need a long running process to periodically poll our API for updates, though this is still an option.

For more information on Job Callbacks [click here](https://developers.neverbounce.com/reference/job-callbacks).

## General Improvements

* *\[Breaking]* Fixed typo in `acedemic_host` flag. This flag is now `academic_host`.
* Added the `failure_reason` property to the [/status](https://developers.neverbounce.com/reference/jobs-status) response. If a job enters a `failed` status this property will contain a reason code.
* API jobs are no longer eligible for [manual review](https://developers.neverbounce.com/reference/jobs-create) by default. This feature now requires an opt-in during the job's creation.