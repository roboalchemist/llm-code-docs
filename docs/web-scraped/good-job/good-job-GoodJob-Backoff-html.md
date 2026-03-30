# Source: https://hexdocs.pm/good_job/GoodJob.Backoff.html

Title: GoodJob.Backoff — good_job v0.2.0

URL Source: https://hexdocs.pm/good_job/GoodJob.Backoff.html

Markdown Content:
GoodJob.Backoff — good_job v0.2.0
===============

[good_job](https://hexdocs.pm/good_job/readme.html)

▼Project version 

*   Pages
*   Modules
*   Mix Tasks

*   [API Reference](https://hexdocs.pm/good_job/api-reference.html)
    *   [Modules](https://hexdocs.pm/good_job/api-reference.html#modules)
    *   [Mix Tasks](https://hexdocs.pm/good_job/api-reference.html#tasks)

*   [README](https://hexdocs.pm/good_job/readme.html)
    *   [Features](https://hexdocs.pm/good_job/readme.html#features)
    *   [Installation](https://hexdocs.pm/good_job/readme.html#installation)
    *   [Quick Start](https://hexdocs.pm/good_job/readme.html#quick-start)
    *   [Usage](https://hexdocs.pm/good_job/readme.html#usage)
    *   [Queue Configuration](https://hexdocs.pm/good_job/readme.html#queue-configuration)
    *   [Execution Modes](https://hexdocs.pm/good_job/readme.html#execution-modes)
    *   [Configuration](https://hexdocs.pm/good_job/readme.html#configuration)
    *   [Web Dashboard](https://hexdocs.pm/good_job/readme.html#web-dashboard)
    *   [Testing](https://hexdocs.pm/good_job/readme.html#testing)
    *   [Requirements](https://hexdocs.pm/good_job/readme.html#requirements)
    *   [Examples](https://hexdocs.pm/good_job/readme.html#examples)
    *   [Contributing](https://hexdocs.pm/good_job/readme.html#contributing)
    *   [Credits](https://hexdocs.pm/good_job/readme.html#credits)
    *   [License](https://hexdocs.pm/good_job/readme.html#license)

*   [CHANGELOG](https://hexdocs.pm/good_job/changelog.html)
    *   [0.2.0](https://hexdocs.pm/good_job/changelog.html#0-2-0)
    *   [0.1.1](https://hexdocs.pm/good_job/changelog.html#0-1-1)
    *   [0.1.0](https://hexdocs.pm/good_job/changelog.html#0-1-0)

*   [Ruby GoodJob Compatibility](https://hexdocs.pm/good_job/compatibility.html)
    *   [Database Schema Compatibility ✅](https://hexdocs.pm/good_job/compatibility.html#database-schema-compatibility)
    *   [Retry & Error Logic Compatibility ✅](https://hexdocs.pm/good_job/compatibility.html#retry-error-logic-compatibility)
    *   [Usage Patterns](https://hexdocs.pm/good_job/compatibility.html#usage-patterns)
    *   [Differences (By Design)](https://hexdocs.pm/good_job/compatibility.html#differences-by-design)
    *   [Best Practices](https://hexdocs.pm/good_job/compatibility.html#best-practices)
    *   [Migration Notes](https://hexdocs.pm/good_job/compatibility.html#migration-notes)

*   [Contributing Guidelines](https://hexdocs.pm/good_job/contributing.html)
    *   [The Golden Rule of Automation](https://hexdocs.pm/good_job/contributing.html#the-golden-rule-of-automation)
    *   [How to Contribute](https://hexdocs.pm/good_job/contributing.html#how-to-contribute)
    *   [Development Setup](https://hexdocs.pm/good_job/contributing.html#development-setup)
    *   [Quality Checks](https://hexdocs.pm/good_job/contributing.html#quality-checks)
    *   [Testing](https://hexdocs.pm/good_job/contributing.html#testing)

*   [Project Governance](https://hexdocs.pm/good_job/governance.html)
    *   [Overview](https://hexdocs.pm/good_job/governance.html#overview)
    *   [Roles](https://hexdocs.pm/good_job/governance.html#roles)
    *   [Decision Making process](https://hexdocs.pm/good_job/governance.html#decision-making-process)

*   [LICENSE](https://hexdocs.pm/good_job/license.html)
*   [Examples](https://hexdocs.pm/good_job/examples.html)
    *   [Examples](https://hexdocs.pm/good_job/examples.html#examples)
    *   [Running Examples](https://hexdocs.pm/good_job/examples.html#running-examples)

*   [Migration Guide: good_job (Ruby) to good_job.ex (Elixir)](https://hexdocs.pm/good_job/migration_from_ruby.html)
    *   [Overview](https://hexdocs.pm/good_job/migration_from_ruby.html#overview)
    *   [API Mapping](https://hexdocs.pm/good_job/migration_from_ruby.html#api-mapping)
    *   [Key Differences](https://hexdocs.pm/good_job/migration_from_ruby.html#key-differences)
    *   [Migration Steps](https://hexdocs.pm/good_job/migration_from_ruby.html#migration-steps)
    *   [Compatibility Notes](https://hexdocs.pm/good_job/migration_from_ruby.html#compatibility-notes)
    *   [Getting Help](https://hexdocs.pm/good_job/migration_from_ruby.html#getting-help)

*   [SECURITY](https://hexdocs.pm/good_job/security.html)
    *   [Reporting a Vulnerability](https://hexdocs.pm/good_job/security.html#reporting-a-vulnerability)
    *   [Automation Security](https://hexdocs.pm/good_job/security.html#automation-security)

*   [Publishing Guide](https://hexdocs.pm/good_job/publishing.html)
    *   [Prerequisites](https://hexdocs.pm/good_job/publishing.html#prerequisites)
    *   [Pre-Release Checklist](https://hexdocs.pm/good_job/publishing.html#pre-release-checklist)
    *   [Publishing Steps](https://hexdocs.pm/good_job/publishing.html#publishing-steps)
    *   [Version Numbering](https://hexdocs.pm/good_job/publishing.html#version-numbering)
    *   [Post-Release](https://hexdocs.pm/good_job/publishing.html#post-release)
    *   [Troubleshooting](https://hexdocs.pm/good_job/publishing.html#troubleshooting)

*   [GoodJob Standalone Usage (Without Phoenix)](https://hexdocs.pm/good_job/standalone.html)
    *   [What Works Without Phoenix](https://hexdocs.pm/good_job/standalone.html#what-works-without-phoenix)
    *   [Usage Without Phoenix](https://hexdocs.pm/good_job/standalone.html#usage-without-phoenix)
    *   [PubSub Behavior Without Phoenix](https://hexdocs.pm/good_job/standalone.html#pubsub-behavior-without-phoenix)
    *   [Monitoring Without Web Dashboard](https://hexdocs.pm/good_job/standalone.html#monitoring-without-web-dashboard)
    *   [Migration Path](https://hexdocs.pm/good_job/standalone.html#migration-path)
    *   [Example: Standalone Elixir Application](https://hexdocs.pm/good_job/standalone.html#example-standalone-elixir-application)

*   [GoodJob.Application](https://hexdocs.pm/good_job/GoodJob.Application.html)
*   [GoodJob.Behaviour](https://hexdocs.pm/good_job/GoodJob.Behaviour.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Behaviour.html#summary)
    *   [Callbacks](https://hexdocs.pm/good_job/GoodJob.Behaviour.html#callbacks)
        *   [backoff/1](https://hexdocs.pm/good_job/GoodJob.Behaviour.html#c:backoff/1 "backoff(attempt)")
        *   [max_attempts/0](https://hexdocs.pm/good_job/GoodJob.Behaviour.html#c:max_attempts/0 "max_attempts()")
        *   [perform/1](https://hexdocs.pm/good_job/GoodJob.Behaviour.html#c:perform/1 "perform(args)")

*   [GoodJob.CleanupTracker](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#functions)
        *   [cleanup?/1](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#cleanup?/1 "cleanup?(tracker)")
        *   [increment/1](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#increment/1 "increment(tracker)")
        *   [new/1](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#new/1 "new(opts \\ [])")
        *   [reset/1](https://hexdocs.pm/good_job/GoodJob.CleanupTracker.html#reset/1 "reset(tracker)")

*   [GoodJob.Config.Defaults](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html#functions)
        *   [defaults/0](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html#defaults/0 "defaults()")
        *   [get/1](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html#get/1 "get(key)")
        *   [merge/1](https://hexdocs.pm/good_job/GoodJob.Config.Defaults.html#merge/1 "merge(config)")

*   [GoodJob.Config.Env](https://hexdocs.pm/good_job/GoodJob.Config.Env.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Config.Env.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Config.Env.html#functions)
        *   [merge_env_vars/1](https://hexdocs.pm/good_job/GoodJob.Config.Env.html#merge_env_vars/1 "merge_env_vars(config)")

*   [GoodJob.Config.Validation](https://hexdocs.pm/good_job/GoodJob.Config.Validation.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Config.Validation.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Config.Validation.html#functions)
        *   [validate!/1](https://hexdocs.pm/good_job/GoodJob.Config.Validation.html#validate!/1 "validate!(config)")

*   [GoodJob.ConfiguredJob](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html#functions)
        *   [new/2](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html#new/2 "new(job_module, options \\ [])")
        *   [perform_later/2](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html#perform_later/2 "perform_later(configured_job, args \\ %{})")
        *   [perform_now/2](https://hexdocs.pm/good_job/GoodJob.ConfiguredJob.html#perform_now/2 "perform_now(configured_job, args \\ %{})")

*   [GoodJob.DatabaseURL](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#content)
        *   [Database URL Format](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#module-database-url-format)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#module-usage)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#functions)
        *   [configure_repo/2](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#configure_repo/2 "configure_repo(repo_module, url)")
        *   [configure_repo_from_env/1](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#configure_repo_from_env/1 "configure_repo_from_env(repo_module)")
        *   [from_env/0](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#from_env/0 "from_env()")
        *   [parse/1](https://hexdocs.pm/good_job/GoodJob.DatabaseURL.html#parse/1 "parse(url)")

*   [GoodJob.Engines.Basic](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#functions)
        *   [complete_job/2](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#complete_job/2 "complete_job(config, job)")
        *   [discard_job/2](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#discard_job/2 "discard_job(config, job)")
        *   [error_job/3](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#error_job/3 "error_job(config, job, seconds)")
        *   [fetch_jobs/2](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#fetch_jobs/2 "fetch_jobs(config, opts \\ [])")
        *   [insert_job/3](https://hexdocs.pm/good_job/GoodJob.Engines.Basic.html#insert_job/3 "insert_job(config, changeset, opts)")

*   [GoodJob.Engines.Inline](https://hexdocs.pm/good_job/GoodJob.Engines.Inline.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Engines.Inline.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Engines.Inline.html#functions)
        *   [insert_job/3](https://hexdocs.pm/good_job/GoodJob.Engines.Inline.html#insert_job/3 "insert_job(config, changeset, opts)")

*   [GoodJob.Errors](https://hexdocs.pm/good_job/GoodJob.Errors.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Errors.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Errors.html#functions)
        *   [classify_error/1](https://hexdocs.pm/good_job/GoodJob.Errors.html#classify_error/1 "classify_error(arg1)")
        *   [connection_error?/1](https://hexdocs.pm/good_job/GoodJob.Errors.html#connection_error?/1 "connection_error?(arg1)")
        *   [format_error/1](https://hexdocs.pm/good_job/GoodJob.Errors.html#format_error/1 "format_error(error)")
        *   [permanent_error?/1](https://hexdocs.pm/good_job/GoodJob.Errors.html#permanent_error?/1 "permanent_error?(arg1)")
        *   [timeout_error?/1](https://hexdocs.pm/good_job/GoodJob.Errors.html#timeout_error?/1 "timeout_error?(error)")

*   [GoodJob.Execution](https://hexdocs.pm/good_job/GoodJob.Execution.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Execution.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Execution.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Execution.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Execution.html#functions)
        *   [changeset/2](https://hexdocs.pm/good_job/GoodJob.Execution.html#changeset/2 "changeset(execution, attrs)")

*   [GoodJob.ExecutionMode](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html#functions)
        *   [execute/3](https://hexdocs.pm/good_job/GoodJob.ExecutionMode.html#execute/3 "execute(job, mode, opts \\ [])")

*   [GoodJob.ExternalJob](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#content)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#module-usage)
        *   [Monorepo Setup](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#module-monorepo-setup)
        *   [External Jobs Configuration](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#module-external-jobs-configuration)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#functions)
        *   [__using__/1](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#__using__/1 "__using__(opts \\ [])")
        *   [find_external_class/1](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#find_external_class/1 "find_external_class(elixir_module)")
        *   [module_to_external_class/1](https://hexdocs.pm/good_job/GoodJob.ExternalJob.html#module_to_external_class/1 "module_to_external_class(module)")

*   [GoodJob.Job.Instance](https://hexdocs.pm/good_job/GoodJob.Job.Instance.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Job.Instance.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Job.Instance.html#functions)
        *   [new/3](https://hexdocs.pm/good_job/GoodJob.Job.Instance.html#new/3 "new(job_module, args \\ %{}, options \\ [])")
        *   [perform/1](https://hexdocs.pm/good_job/GoodJob.Job.Instance.html#perform/1 "perform(instance)")

*   [GoodJob.Job.Query](https://hexdocs.pm/good_job/GoodJob.Job.Query.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#functions)
        *   [advisory_locked/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#advisory_locked/1 "advisory_locked(query \\ Job)")
        *   [advisory_unlocked/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#advisory_unlocked/1 "advisory_unlocked(query \\ Job)")
        *   [created_after/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#created_after/2 "created_after(query \\ Job, datetime)")
        *   [created_before/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#created_before/2 "created_before(query \\ Job, datetime)")
        *   [dequeueing_ordered/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#dequeueing_ordered/1 "dequeueing_ordered(query \\ Job)")
        *   [discarded/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#discarded/1 "discarded(query \\ Job)")
        *   [exclude_paused/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#exclude_paused/1 "exclude_paused(query \\ Job)")
        *   [finished/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#finished/1 "finished(query \\ Job)")
        *   [finished_before/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#finished_before/2 "finished_before(query \\ Job, datetime)")
        *   [in_batch/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#in_batch/2 "in_batch(query \\ Job, batch_id)")
        *   [in_queue/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#in_queue/2 "in_queue(query \\ Job, queue_name)")
        *   [joins_advisory_locks/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#joins_advisory_locks/1 "joins_advisory_locks(query \\ Job)")
        *   [locked/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#locked/1 "locked(query \\ Job)")
        *   [only_scheduled/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#only_scheduled/1 "only_scheduled(query \\ Job)")
        *   [order_by_created_asc/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#order_by_created_asc/1 "order_by_created_asc(query \\ Job)")
        *   [order_by_created_desc/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#order_by_created_desc/1 "order_by_created_desc(query \\ Job)")
        *   [order_by_finished_desc/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#order_by_finished_desc/1 "order_by_finished_desc(query \\ Job)")
        *   [order_by_scheduled_asc/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#order_by_scheduled_asc/1 "order_by_scheduled_asc(query \\ Job)")
        *   [order_for_candidate_lookup/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#order_for_candidate_lookup/2 "order_for_candidate_lookup(query \\ Job, parsed_queues \\ %{})")
        *   [queue_ordered/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#queue_ordered/2 "queue_ordered(query \\ Job, queues)")
        *   [queued/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#queued/1 "queued(query \\ Job)")
        *   [running/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#running/1 "running(query \\ Job)")
        *   [scheduled/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#scheduled/1 "scheduled(query \\ Job)")
        *   [scheduled_before/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#scheduled_before/2 "scheduled_before(query \\ Job, datetime)")
        *   [succeeded/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#succeeded/1 "succeeded(query \\ Job)")
        *   [unfinished/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#unfinished/1 "unfinished(query \\ Job)")
        *   [unlocked/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#unlocked/1 "unlocked(query \\ Job)")
        *   [with_all_labels/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_all_labels/2 "with_all_labels(query \\ Job, labels)")
        *   [with_any_label/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_any_label/2 "with_any_label(query \\ Job, labels)")
        *   [with_batch_id/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_batch_id/2 "with_batch_id(query \\ Job, batch_id)")
        *   [with_concurrency_key/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_concurrency_key/2 "with_concurrency_key(query \\ Job, key)")
        *   [with_cron_key/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_cron_key/2 "with_cron_key(query \\ Job, cron_key)")
        *   [with_errors/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_errors/1 "with_errors(query \\ Job)")
        *   [with_job_class/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_job_class/2 "with_job_class(query \\ Job, job_class)")
        *   [with_label/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_label/2 "with_label(query \\ Job, label)")
        *   [with_labels/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_labels/2 "with_labels(query \\ Job, labels)")
        *   [with_max_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_max_priority/2 "with_max_priority(query \\ Job, max_priority)")
        *   [with_min_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_min_priority/2 "with_min_priority(query \\ Job, min_priority)")
        *   [with_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#with_priority/2 "with_priority(query \\ Job, priority)")
        *   [without_errors/1](https://hexdocs.pm/good_job/GoodJob.Job.Query.html#without_errors/1 "without_errors(query \\ Job)")

*   [GoodJob.Job.State](https://hexdocs.pm/good_job/GoodJob.Job.State.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Job.State.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Job.State.html#functions)
        *   [calculate/2](https://hexdocs.pm/good_job/GoodJob.Job.State.html#calculate/2 "calculate(job, current_time \\ nil)")

*   [GoodJob.JobCallbacks](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#functions)
        *   [after_enqueue/3](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#after_enqueue/3 "after_enqueue(job_module, job, opts)")
        *   [after_perform/4](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#after_perform/4 "after_perform(job_module, args, job, result)")
        *   [before_enqueue/3](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#before_enqueue/3 "before_enqueue(job_module, args, opts)")
        *   [before_perform/3](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#before_perform/3 "before_perform(job_module, args, job)")
        *   [on_error/4](https://hexdocs.pm/good_job/GoodJob.JobCallbacks.html#on_error/4 "on_error(job_module, args, job, error)")

*   [GoodJob.JobExecutor.ErrorHandler](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ErrorHandler.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ErrorHandler.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ErrorHandler.html#functions)
        *   [check_discard_on/2](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ErrorHandler.html#check_discard_on/2 "check_discard_on(job_module, error)")

*   [GoodJob.JobExecutor.ResultHandler](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#functions)
        *   [finish_execution/9](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#finish_execution/9 "finish_execution(job, execution, value, handled_error, unhandled_error, error_event, start_time, process_id, stacktrace \\ [])")
        *   [handle_cancel/4](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#handle_cancel/4 "handle_cancel(job, reason, start_time, process_id)")
        *   [handle_discard/4](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#handle_discard/4 "handle_discard(job, reason, start_time, process_id)")
        *   [handle_error/5](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#handle_error/5 "handle_error(job, reason, start_time, process_id, stacktrace \\ [])")
        *   [handle_snooze/4](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#handle_snooze/4 "handle_snooze(job, seconds, start_time, process_id)")
        *   [handle_success/4](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#handle_success/4 "handle_success(job, result, start_time, process_id)")
        *   [normalize_result/1](https://hexdocs.pm/good_job/GoodJob.JobExecutor.ResultHandler.html#normalize_result/1 "normalize_result(result)")

*   [GoodJob.JobExecutor.Timeout](https://hexdocs.pm/good_job/GoodJob.JobExecutor.Timeout.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobExecutor.Timeout.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobExecutor.Timeout.html#functions)
        *   [get_job_timeout/2](https://hexdocs.pm/good_job/GoodJob.JobExecutor.Timeout.html#get_job_timeout/2 "get_job_timeout(job_module, job)")
        *   [perform_with_timeout/3](https://hexdocs.pm/good_job/GoodJob.JobExecutor.Timeout.html#perform_with_timeout/3 "perform_with_timeout(perform_fun, job, timeout_ms)")

*   [GoodJob.JobStats](https://hexdocs.pm/good_job/GoodJob.JobStats.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobStats.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobStats.html#functions)
        *   [activity_over_time/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#activity_over_time/1 "activity_over_time(hours)")
        *   [average_execution_time/0](https://hexdocs.pm/good_job/GoodJob.JobStats.html#average_execution_time/0 "average_execution_time()")
        *   [average_execution_time/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#average_execution_time/1 "average_execution_time(queue_name)")
        *   [count_all/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_all/1 "count_all(query)")
        *   [count_discarded/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_discarded/1 "count_discarded(query)")
        *   [count_queued/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_queued/1 "count_queued(query)")
        *   [count_running/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_running/1 "count_running(query)")
        *   [count_succeeded/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_succeeded/1 "count_succeeded(query)")
        *   [count_with_errors/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#count_with_errors/1 "count_with_errors(query)")
        *   [job_class_stats/0](https://hexdocs.pm/good_job/GoodJob.JobStats.html#job_class_stats/0 "job_class_stats()")
        *   [newest_job/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#newest_job/1 "newest_job(query)")
        *   [oldest_job/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#oldest_job/1 "oldest_job(query)")
        *   [queue_stats/0](https://hexdocs.pm/good_job/GoodJob.JobStats.html#queue_stats/0 "queue_stats()")
        *   [stats/0](https://hexdocs.pm/good_job/GoodJob.JobStats.html#stats/0 "stats()")
        *   [stats/1](https://hexdocs.pm/good_job/GoodJob.JobStats.html#stats/1 "stats(queue_name)")

*   [GoodJob.JobStats.Aggregation](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html#functions)
        *   [average_execution_time/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html#average_execution_time/1 "average_execution_time(query)")
        *   [job_class_stats/0](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html#job_class_stats/0 "job_class_stats()")
        *   [queue_stats/0](https://hexdocs.pm/good_job/GoodJob.JobStats.Aggregation.html#queue_stats/0 "queue_stats()")

*   [GoodJob.JobStats.Counters](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#functions)
        *   [count_all/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_all/1 "count_all(query)")
        *   [count_discarded/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_discarded/1 "count_discarded(query)")
        *   [count_queued/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_queued/1 "count_queued(query)")
        *   [count_running/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_running/1 "count_running(query)")
        *   [count_succeeded/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_succeeded/1 "count_succeeded(query)")
        *   [count_with_errors/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#count_with_errors/1 "count_with_errors(query)")
        *   [newest_job/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#newest_job/1 "newest_job(query)")
        *   [oldest_job/1](https://hexdocs.pm/good_job/GoodJob.JobStats.Counters.html#oldest_job/1 "oldest_job(query)")

*   [GoodJob.JobStats.DatetimeHelpers](https://hexdocs.pm/good_job/GoodJob.JobStats.DatetimeHelpers.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobStats.DatetimeHelpers.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobStats.DatetimeHelpers.html#functions)
        *   [convert_to_datetime/1](https://hexdocs.pm/good_job/GoodJob.JobStats.DatetimeHelpers.html#convert_to_datetime/1 "convert_to_datetime(dt)")
        *   [format_hour/1](https://hexdocs.pm/good_job/GoodJob.JobStats.DatetimeHelpers.html#format_hour/1 "format_hour(datetime)")

*   [GoodJob.JobStats.TimeSeries](https://hexdocs.pm/good_job/GoodJob.JobStats.TimeSeries.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobStats.TimeSeries.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobStats.TimeSeries.html#functions)
        *   [activity_over_time/1](https://hexdocs.pm/good_job/GoodJob.JobStats.TimeSeries.html#activity_over_time/1 "activity_over_time(hours \\ 24)")

*   [GoodJob.Poller](https://hexdocs.pm/good_job/GoodJob.Poller.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Poller.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Poller.html#functions)
        *   [add_recipient/1](https://hexdocs.pm/good_job/GoodJob.Poller.html#add_recipient/1 "add_recipient(recipient)")
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Poller.html#child_spec/1 "child_spec(init_arg)")
        *   [remove_recipient/1](https://hexdocs.pm/good_job/GoodJob.Poller.html#remove_recipient/1 "remove_recipient(recipient)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Poller.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.Process](https://hexdocs.pm/good_job/GoodJob.Process.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Process.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Process.html#functions)
        *   [active/0](https://hexdocs.pm/good_job/GoodJob.Process.html#active/0 "active()")
        *   [changeset/2](https://hexdocs.pm/good_job/GoodJob.Process.html#changeset/2 "changeset(process, attrs)")
        *   [find_or_create_record/1](https://hexdocs.pm/good_job/GoodJob.Process.html#find_or_create_record/1 "find_or_create_record(list)")
        *   [inactive/0](https://hexdocs.pm/good_job/GoodJob.Process.html#inactive/0 "inactive()")

*   [GoodJob.Protocol](https://hexdocs.pm/good_job/GoodJob.Protocol.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Protocol.html#content)
        *   [When to use](https://hexdocs.pm/good_job/GoodJob.Protocol.html#module-when-to-use)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Protocol.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Protocol.html#functions)
        *   [enqueue_for_elixir/3](https://hexdocs.pm/good_job/GoodJob.Protocol.html#enqueue_for_elixir/3 "enqueue_for_elixir(job_identifier, args, opts \\ [])")
        *   [enqueue_for_external/3](https://hexdocs.pm/good_job/GoodJob.Protocol.html#enqueue_for_external/3 "enqueue_for_external(job_identifier, args, opts \\ [])")

*   [GoodJob.Protocol.Deserializer](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html#functions)
        *   [deserialize_args/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html#deserialize_args/1 "deserialize_args(serialized_params)")
        *   [deserialize_job_module/2](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html#deserialize_job_module/2 "deserialize_job_module(job_class, serialized_params)")
        *   [normalize_args_for_elixir/3](https://hexdocs.pm/good_job/GoodJob.Protocol.Deserializer.html#normalize_args_for_elixir/3 "normalize_args_for_elixir(module, args, job)")

*   [GoodJob.Protocol.Notification](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#content)
        *   [Notification Format](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#module-notification-format)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#module-usage)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#functions)
        *   [create/2](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#create/2 "create(queue_name, scheduled_at \\ nil)")
        *   [for_job/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Notification.html#for_job/1 "for_job(map)")

*   [GoodJob.Protocol.Serialization](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#content)
        *   [ActiveJob Serialization Format](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#module-activejob-serialization-format)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#module-usage)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#functions)
        *   [external_class_to_module/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#external_class_to_module/1 "external_class_to_module(external_class)")
        *   [from_active_job/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#from_active_job/1 "from_active_job(serialized_params)")
        *   [module_to_external_class/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#module_to_external_class/1 "module_to_external_class(module)")
        *   [to_active_job/1](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#to_active_job/1 "to_active_job(opts)")
        *   [update_executions/2](https://hexdocs.pm/good_job/GoodJob.Protocol.Serialization.html#update_executions/2 "update_executions(serialized_params, executions)")

*   [GoodJob.PubSub](https://hexdocs.pm/good_job/GoodJob.PubSub.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.PubSub.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.PubSub.html#functions)
        *   [broadcast/2](https://hexdocs.pm/good_job/GoodJob.PubSub.html#broadcast/2 "broadcast(event, job_id)")
        *   [subscribe/1](https://hexdocs.pm/good_job/GoodJob.PubSub.html#subscribe/1 "subscribe(pubsub_server \\ nil)")

*   [GoodJob.Registry](https://hexdocs.pm/good_job/GoodJob.Registry.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Registry.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Registry.html#functions)
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Registry.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.RepoPool](https://hexdocs.pm/good_job/GoodJob.RepoPool.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#content)
        *   [Connection Pool Sizing](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#module-connection-pool-sizing)
        *   [Statement and Lock Timeouts](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#module-statement-and-lock-timeouts)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#types)
        *   [postgrex_conn/0](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#t:postgrex_conn/0 "postgrex_conn()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#functions)
        *   [configure_repo/1](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#configure_repo/1 "configure_repo(repo)")
        *   [recommended_pool_size/0](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#recommended_pool_size/0 "recommended_pool_size()")
        *   [set_timeouts/1](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#set_timeouts/1 "set_timeouts(conn)")
        *   [total_connections_needed/0](https://hexdocs.pm/good_job/GoodJob.RepoPool.html#total_connections_needed/0 "total_connections_needed()")

*   [GoodJob.Scheduler.Supervisor](https://hexdocs.pm/good_job/GoodJob.Scheduler.Supervisor.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Scheduler.Supervisor.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Scheduler.Supervisor.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Scheduler.Supervisor.html#child_spec/1 "child_spec(init_arg)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Scheduler.Supervisor.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.SettingManager](https://hexdocs.pm/good_job/GoodJob.SettingManager.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#functions)
        *   [cron_key_enabled?/2](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#cron_key_enabled?/2 "cron_key_enabled?(cron_key, default \\ true)")
        *   [disable_cron/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#disable_cron/1 "disable_cron(cron_key)")
        *   [enable_cron/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#enable_cron/1 "enable_cron(cron_key)")
        *   [pause/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#pause/1 "pause(opts \\ [])")
        *   [paused?/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#paused?/1 "paused?(opts \\ [])")
        *   [unpause/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#unpause/1 "unpause(opts \\ [])")
        *   [unpause_by_key/1](https://hexdocs.pm/good_job/GoodJob.SettingManager.html#unpause_by_key/1 "unpause_by_key(pause_key)")

*   [GoodJob.SettingSchema](https://hexdocs.pm/good_job/GoodJob.SettingSchema.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.SettingSchema.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.SettingSchema.html#functions)
        *   [changeset/2](https://hexdocs.pm/good_job/GoodJob.SettingSchema.html#changeset/2 "changeset(setting, attrs)")

*   [GoodJob.Telemetry.Formatters](https://hexdocs.pm/good_job/GoodJob.Telemetry.Formatters.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Telemetry.Formatters.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Telemetry.Formatters.html#functions)
        *   [build_generic_log_message/4](https://hexdocs.pm/good_job/GoodJob.Telemetry.Formatters.html#build_generic_log_message/4 "build_generic_log_message(category, event, measure, meta)")
        *   [build_job_log_message/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.Formatters.html#build_job_log_message/3 "build_job_log_message(atom, measure, meta)")

*   [GoodJob.Telemetry.Logger](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html#functions)
        *   [attach/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html#attach/1 "attach(opts \\ [])")
        *   [default_handler_id/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html#default_handler_id/0 "default_handler_id()")
        *   [detach/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.Logger.html#detach/0 "detach()")

*   [GoodJob.TestRepo](https://hexdocs.pm/good_job/GoodJob.TestRepo.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#functions)
        *   [aggregate/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#aggregate/3 "aggregate(queryable, aggregate, opts \\ [])")
        *   [aggregate/4](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#aggregate/4 "aggregate(queryable, aggregate, field, opts)")
        *   [all/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#all/2 "all(queryable, opts \\ [])")
        *   [all_by/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#all_by/3 "all_by(queryable, clauses, opts \\ [])")
        *   [checked_out?/0](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#checked_out?/0 "checked_out?()")
        *   [checkout/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#checkout/2 "checkout(fun, opts \\ [])")
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#child_spec/1 "child_spec(opts)")
        *   [config/0](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#config/0 "config()")
        *   [default_options/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#default_options/1 "default_options(operation)")
        *   [delete/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#delete/2 "delete(struct, opts \\ [])")
        *   [delete!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#delete!/2 "delete!(struct, opts \\ [])")
        *   [delete_all/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#delete_all/2 "delete_all(queryable, opts \\ [])")
        *   [disconnect_all/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#disconnect_all/2 "disconnect_all(interval, opts \\ [])")
        *   [exists?/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#exists?/2 "exists?(queryable, opts \\ [])")
        *   [explain/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#explain/3 "explain(operation, queryable, opts \\ [])")
        *   [get/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#get/3 "get(queryable, id, opts \\ [])")
        *   [get!/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#get!/3 "get!(queryable, id, opts \\ [])")
        *   [get_by/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#get_by/3 "get_by(queryable, clauses, opts \\ [])")
        *   [get_by!/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#get_by!/3 "get_by!(queryable, clauses, opts \\ [])")
        *   [get_dynamic_repo/0](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#get_dynamic_repo/0 "get_dynamic_repo()")
        *   [in_transaction?/0](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#in_transaction?/0 "in_transaction?()")
        *   [insert/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#insert/2 "insert(struct, opts \\ [])")
        *   [insert!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#insert!/2 "insert!(struct, opts \\ [])")
        *   [insert_all/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#insert_all/3 "insert_all(schema_or_source, entries, opts \\ [])")
        *   [insert_or_update/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#insert_or_update/2 "insert_or_update(changeset, opts \\ [])")
        *   [insert_or_update!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#insert_or_update!/2 "insert_or_update!(changeset, opts \\ [])")
        *   [load/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#load/2 "load(schema_or_types, data)")
        *   [one/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#one/2 "one(queryable, opts \\ [])")
        *   [one!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#one!/2 "one!(queryable, opts \\ [])")
        *   [preload/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#preload/3 "preload(struct_or_structs_or_nil, preloads, opts \\ [])")
        *   [prepare_query/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#prepare_query/3 "prepare_query(operation, query, opts)")
        *   [prepare_transaction/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#prepare_transaction/2 "prepare_transaction(fun_or_multi, opts)")
        *   [put_dynamic_repo/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#put_dynamic_repo/1 "put_dynamic_repo(dynamic)")
        *   [query/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#query/3 "query(sql, params \\ [], opts \\ [])")
        *   [query!/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#query!/3 "query!(sql, params \\ [], opts \\ [])")
        *   [query_many/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#query_many/3 "query_many(sql, params \\ [], opts \\ [])")
        *   [query_many!/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#query_many!/3 "query_many!(sql, params \\ [], opts \\ [])")
        *   [reload/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#reload/2 "reload(queryable, opts \\ [])")
        *   [reload!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#reload!/2 "reload!(queryable, opts \\ [])")
        *   [rollback/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#rollback/1 "rollback(value)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#start_link/1 "start_link(opts \\ [])")
        *   [stop/1](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#stop/1 "stop(timeout \\ 5000)")
        *   [stream/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#stream/2 "stream(queryable, opts \\ [])")
        *   [to_sql/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#to_sql/2 "to_sql(operation, queryable)")
        *   [transact/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#transact/2 "transact(fun_or_multi, opts \\ [])")
        *   [transaction/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#transaction/2 "transaction(fun_or_multi, opts \\ [])")
        *   [update/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#update/2 "update(struct, opts \\ [])")
        *   [update!/2](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#update!/2 "update!(struct, opts \\ [])")
        *   [update_all/3](https://hexdocs.pm/good_job/GoodJob.TestRepo.html#update_all/3 "update_all(queryable, updates, opts \\ [])")

*   [GoodJob.Types.Interval](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#functions)
        *   [cast/1](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#cast/1 "cast(interval)")
        *   [dump/1](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#dump/1 "dump(interval)")
        *   [embed_as/1](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#embed_as/1 "embed_as(_)")
        *   [equal?/2](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#equal?/2 "equal?(a, b)")
        *   [load/1](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#load/1 "load(interval)")
        *   [type/0](https://hexdocs.pm/good_job/GoodJob.Types.Interval.html#type/0 "type()")

*   [GoodJob.Utils](https://hexdocs.pm/good_job/GoodJob.Utils.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Utils.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Utils.html#functions)
        *   [format_backtrace/1](https://hexdocs.pm/good_job/GoodJob.Utils.html#format_backtrace/1 "format_backtrace(stacktrace)")
        *   [format_datetime_log/1](https://hexdocs.pm/good_job/GoodJob.Utils.html#format_datetime_log/1 "format_datetime_log(datetime)")
        *   [format_duration_microseconds/1](https://hexdocs.pm/good_job/GoodJob.Utils.html#format_duration_microseconds/1 "format_duration_microseconds(duration)")
        *   [format_error/1](https://hexdocs.pm/good_job/GoodJob.Utils.html#format_error/1 "format_error(error)")

*   [GoodJob.Web.ChartFormatter](https://hexdocs.pm/good_job/GoodJob.Web.ChartFormatter.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.ChartFormatter.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.ChartFormatter.html#functions)
        *   [format_activity_chart/1](https://hexdocs.pm/good_job/GoodJob.Web.ChartFormatter.html#format_activity_chart/1 "format_activity_chart(map)")

*   [GoodJob.Web.Components.Batches](https://hexdocs.pm/good_job/GoodJob.Web.Components.Batches.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Batches.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Batches.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Batches.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.Cron](https://hexdocs.pm/good_job/GoodJob.Web.Components.Cron.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Cron.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Cron.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Cron.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.JobDetail](https://hexdocs.pm/good_job/GoodJob.Web.Components.JobDetail.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.JobDetail.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.JobDetail.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.JobDetail.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.Jobs](https://hexdocs.pm/good_job/GoodJob.Web.Components.Jobs.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Jobs.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Jobs.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Jobs.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.Navigation](https://hexdocs.pm/good_job/GoodJob.Web.Components.Navigation.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Navigation.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Navigation.html#functions)
        *   [breadcrumbs/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Navigation.html#breadcrumbs/1 "breadcrumbs(assigns)")
        *   [navbar/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Navigation.html#navbar/1 "navbar(assigns)")

*   [GoodJob.Web.Components.Overview](https://hexdocs.pm/good_job/GoodJob.Web.Components.Overview.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Overview.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Overview.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Overview.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.Pauses](https://hexdocs.pm/good_job/GoodJob.Web.Components.Pauses.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Pauses.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Pauses.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Pauses.html#render/1 "render(assigns)")

*   [GoodJob.Web.Components.Processes](https://hexdocs.pm/good_job/GoodJob.Web.Components.Processes.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Components.Processes.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Components.Processes.html#functions)
        *   [render/1](https://hexdocs.pm/good_job/GoodJob.Web.Components.Processes.html#render/1 "render(assigns)")

*   [GoodJob.Web.DataLoader](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#functions)
        *   [get_cron_entry/1](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#get_cron_entry/1 "get_cron_entry(cron_key)")
        *   [load_batches/1](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_batches/1 "load_batches(opts)")
        *   [load_chart_data/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_chart_data/0 "load_chart_data()")
        *   [load_cron_entries/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_cron_entries/0 "load_cron_entries()")
        *   [load_executions/1](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_executions/1 "load_executions(active_job_id)")
        *   [load_jobs/1](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_jobs/1 "load_jobs(opts)")
        *   [load_nav_counts/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_nav_counts/0 "load_nav_counts()")
        *   [load_pauses/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_pauses/0 "load_pauses()")
        *   [load_processes/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_processes/0 "load_processes()")
        *   [load_queue_stats/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_queue_stats/0 "load_queue_stats()")
        *   [load_stats/0](https://hexdocs.pm/good_job/GoodJob.Web.DataLoader.html#load_stats/0 "load_stats()")

*   [GoodJob.Web.Formatters](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#functions)
        *   [format_count/1](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#format_count/1 "format_count(count)")
        *   [format_datetime/1](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#format_datetime/1 "format_datetime(datetime)")
        *   [format_duration/1](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#format_duration/1 "format_duration(interval)")
        *   [format_job_class/1](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#format_job_class/1 "format_job_class(class)")
        *   [state_badge_class/1](https://hexdocs.pm/good_job/GoodJob.Web.Formatters.html#state_badge_class/1 "state_badge_class(arg1)")

*   [GoodJob.Web.LiveDashboardPage.DataLoader](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.DataLoader.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.DataLoader.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.DataLoader.html#functions)
        *   [load_data_for_view/4](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.DataLoader.html#load_data_for_view/4 "load_data_for_view(socket, atom, job_id, params)")

*   [GoodJob.Web.LiveDashboardPage.Handlers](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#functions)
        *   [handle_bulk_delete/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_bulk_delete/2 "handle_bulk_delete(job_ids, socket)")
        *   [handle_bulk_retry/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_bulk_retry/2 "handle_bulk_retry(job_ids, socket)")
        *   [handle_create_pause_job_class/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_create_pause_job_class/2 "handle_create_pause_job_class(job_class, socket)")
        *   [handle_create_pause_queue/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_create_pause_queue/2 "handle_create_pause_queue(queue, socket)")
        *   [handle_delete_job/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_delete_job/2 "handle_delete_job(job_id, socket)")
        *   [handle_delete_pause/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_delete_pause/2 "handle_delete_pause(pause_key, socket)")
        *   [handle_deselect_all/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_deselect_all/1 "handle_deselect_all(socket)")
        *   [handle_disable_cron/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_disable_cron/2 "handle_disable_cron(cron_key, socket)")
        *   [handle_discard_job/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_discard_job/2 "handle_discard_job(job_id, socket)")
        *   [handle_enable_cron/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_enable_cron/2 "handle_enable_cron(cron_key, socket)")
        *   [handle_enqueue_cron/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_enqueue_cron/2 "handle_enqueue_cron(cron_key, socket)")
        *   [handle_filter/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_filter/2 "handle_filter(params, socket)")
        *   [handle_retry_batch/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_retry_batch/2 "handle_retry_batch(batch_id, socket)")
        *   [handle_retry_job/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_retry_job/2 "handle_retry_job(job_id, socket)")
        *   [handle_select_all/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_select_all/1 "handle_select_all(socket)")
        *   [handle_set_poll_interval/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_set_poll_interval/2 "handle_set_poll_interval(interval_str, socket)")
        *   [handle_toggle_job_selection/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_toggle_job_selection/2 "handle_toggle_job_selection(job_id, socket)")
        *   [handle_toggle_polling/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Handlers.html#handle_toggle_polling/1 "handle_toggle_polling(socket)")

*   [GoodJob.Web.LiveDashboardPage.Helpers](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#functions)
        *   [build_uri/3](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#build_uri/3 "build_uri(view, job_id, assigns)")
        *   [parse_page/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#parse_page/1 "parse_page(arg1)")
        *   [parse_poll_interval/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#parse_poll_interval/1 "parse_poll_interval(arg1)")
        *   [parse_view/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#parse_view/1 "parse_view(arg1)")
        *   [schedule_refresh/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.Helpers.html#schedule_refresh/1 "schedule_refresh(socket)")

*   Core
*   [GoodJob](https://hexdocs.pm/good_job/GoodJob.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.html#content)
        *   [Configuration](https://hexdocs.pm/good_job/GoodJob.html#module-configuration)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.html#module-usage)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.html#functions)
        *   [cleanup_preserved_jobs/1](https://hexdocs.pm/good_job/GoodJob.html#cleanup_preserved_jobs/1 "cleanup_preserved_jobs(opts \\ [])")
        *   [config/0](https://hexdocs.pm/good_job/GoodJob.html#config/0 "config()")
        *   [enqueue/3](https://hexdocs.pm/good_job/GoodJob.html#enqueue/3 "enqueue(job_module, args, opts \\ [])")
        *   [new_batch/1](https://hexdocs.pm/good_job/GoodJob.html#new_batch/1 "new_batch(opts \\ [])")
        *   [pause/1](https://hexdocs.pm/good_job/GoodJob.html#pause/1 "pause(opts \\ [])")
        *   [paused?/1](https://hexdocs.pm/good_job/GoodJob.html#paused?/1 "paused?(opts \\ [])")
        *   [shutdown/1](https://hexdocs.pm/good_job/GoodJob.html#shutdown/1 "shutdown(opts \\ [])")
        *   [shutdown?/0](https://hexdocs.pm/good_job/GoodJob.html#shutdown?/0 "shutdown?()")
        *   [stats/0](https://hexdocs.pm/good_job/GoodJob.html#stats/0 "stats()")
        *   [stats/1](https://hexdocs.pm/good_job/GoodJob.html#stats/1 "stats(queue_name)")
        *   [unpause/1](https://hexdocs.pm/good_job/GoodJob.html#unpause/1 "unpause(opts \\ [])")

*   [GoodJob.Config](https://hexdocs.pm/good_job/GoodJob.Config.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Config.html#content)
        *   [Configuration Options](https://hexdocs.pm/good_job/GoodJob.Config.html#module-configuration-options)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Config.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Config.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Config.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Config.html#functions)
        *   [advisory_lock_heartbeat?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#advisory_lock_heartbeat?/0 "advisory_lock_heartbeat?()")
        *   [cleanup_discarded_jobs?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cleanup_discarded_jobs?/0 "cleanup_discarded_jobs?()")
        *   [cleanup_interval_jobs/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cleanup_interval_jobs/0 "cleanup_interval_jobs()")
        *   [cleanup_interval_seconds/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cleanup_interval_seconds/0 "cleanup_interval_seconds()")
        *   [cleanup_preserved_jobs_before_seconds_ago/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cleanup_preserved_jobs_before_seconds_ago/0 "cleanup_preserved_jobs_before_seconds_ago()")
        *   [config/0](https://hexdocs.pm/good_job/GoodJob.Config.html#config/0 "config()")
        *   [cron/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cron/0 "cron()")
        *   [cron_entries/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cron_entries/0 "cron_entries()")
        *   [cron_graceful_restart_period/0](https://hexdocs.pm/good_job/GoodJob.Config.html#cron_graceful_restart_period/0 "cron_graceful_restart_period()")
        *   [database_lock_timeout/0](https://hexdocs.pm/good_job/GoodJob.Config.html#database_lock_timeout/0 "database_lock_timeout()")
        *   [database_pool_size/0](https://hexdocs.pm/good_job/GoodJob.Config.html#database_pool_size/0 "database_pool_size()")
        *   [database_statement_timeout/0](https://hexdocs.pm/good_job/GoodJob.Config.html#database_statement_timeout/0 "database_statement_timeout()")
        *   [enable_cron?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#enable_cron?/0 "enable_cron?()")
        *   [enable_listen_notify?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#enable_listen_notify?/0 "enable_listen_notify?()")
        *   [enable_pauses?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#enable_pauses?/0 "enable_pauses?()")
        *   [enqueue_after_transaction_commit?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#enqueue_after_transaction_commit?/0 "enqueue_after_transaction_commit?()")
        *   [execution_mode/0](https://hexdocs.pm/good_job/GoodJob.Config.html#execution_mode/0 "execution_mode()")
        *   [external_jobs/0](https://hexdocs.pm/good_job/GoodJob.Config.html#external_jobs/0 "external_jobs()")
        *   [get/2](https://hexdocs.pm/good_job/GoodJob.Config.html#get/2 "get(key, default \\ nil)")
        *   [in_webserver?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#in_webserver?/0 "in_webserver?()")
        *   [max_cache/0](https://hexdocs.pm/good_job/GoodJob.Config.html#max_cache/0 "max_cache()")
        *   [max_processes/0](https://hexdocs.pm/good_job/GoodJob.Config.html#max_processes/0 "max_processes()")
        *   [notifier_channel/0](https://hexdocs.pm/good_job/GoodJob.Config.html#notifier_channel/0 "notifier_channel()")
        *   [notifier_keepalive_interval/0](https://hexdocs.pm/good_job/GoodJob.Config.html#notifier_keepalive_interval/0 "notifier_keepalive_interval()")
        *   [notifier_pool_size/0](https://hexdocs.pm/good_job/GoodJob.Config.html#notifier_pool_size/0 "notifier_pool_size()")
        *   [notifier_wait_interval/0](https://hexdocs.pm/good_job/GoodJob.Config.html#notifier_wait_interval/0 "notifier_wait_interval()")
        *   [plugins/0](https://hexdocs.pm/good_job/GoodJob.Config.html#plugins/0 "plugins()")
        *   [poll_interval/0](https://hexdocs.pm/good_job/GoodJob.Config.html#poll_interval/0 "poll_interval()")
        *   [preserve_job_records?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#preserve_job_records?/0 "preserve_job_records?()")
        *   [queue_select_limit/0](https://hexdocs.pm/good_job/GoodJob.Config.html#queue_select_limit/0 "queue_select_limit()")
        *   [queues/0](https://hexdocs.pm/good_job/GoodJob.Config.html#queues/0 "queues()")
        *   [repo/0](https://hexdocs.pm/good_job/GoodJob.Config.html#repo/0 "repo()")
        *   [retry_on_unhandled_error?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#retry_on_unhandled_error?/0 "retry_on_unhandled_error?()")
        *   [shutdown_timeout/0](https://hexdocs.pm/good_job/GoodJob.Config.html#shutdown_timeout/0 "shutdown_timeout()")
        *   [start_in_application?/0](https://hexdocs.pm/good_job/GoodJob.Config.html#start_in_application?/0 "start_in_application?()")
        *   [validate_cron/0](https://hexdocs.pm/good_job/GoodJob.Config.html#validate_cron/0 "validate_cron()")

*   [GoodJob.Executor](https://hexdocs.pm/good_job/GoodJob.Executor.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Executor.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Executor.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Executor.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Executor.html#functions)
        *   [call/1](https://hexdocs.pm/good_job/GoodJob.Executor.html#call/1 "call(exec)")
        *   [new/2](https://hexdocs.pm/good_job/GoodJob.Executor.html#new/2 "new(job, opts \\ [])")

*   [GoodJob.Job](https://hexdocs.pm/good_job/GoodJob.Job.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Job.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Job.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Job.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Job.html#functions)
        *   [advisory_locked/1](https://hexdocs.pm/good_job/GoodJob.Job.html#advisory_locked/1 "advisory_locked(query \\ __MODULE__)")
        *   [advisory_unlocked/1](https://hexdocs.pm/good_job/GoodJob.Job.html#advisory_unlocked/1 "advisory_unlocked(query \\ __MODULE__)")
        *   [build_for_enqueue/1](https://hexdocs.pm/good_job/GoodJob.Job.html#build_for_enqueue/1 "build_for_enqueue(attrs)")
        *   [calculate_state/1](https://hexdocs.pm/good_job/GoodJob.Job.html#calculate_state/1 "calculate_state(job)")
        *   [changeset/2](https://hexdocs.pm/good_job/GoodJob.Job.html#changeset/2 "changeset(job, attrs)")
        *   [created_after/2](https://hexdocs.pm/good_job/GoodJob.Job.html#created_after/2 "created_after(query \\ __MODULE__, datetime)")
        *   [created_before/2](https://hexdocs.pm/good_job/GoodJob.Job.html#created_before/2 "created_before(query \\ __MODULE__, datetime)")
        *   [delete/1](https://hexdocs.pm/good_job/GoodJob.Job.html#delete/1 "delete(job)")
        *   [dequeueing_ordered/1](https://hexdocs.pm/good_job/GoodJob.Job.html#dequeueing_ordered/1 "dequeueing_ordered(query \\ __MODULE__)")
        *   [discarded/1](https://hexdocs.pm/good_job/GoodJob.Job.html#discarded/1 "discarded(query \\ __MODULE__)")
        *   [enqueue/1](https://hexdocs.pm/good_job/GoodJob.Job.html#enqueue/1 "enqueue(attrs)")
        *   [exclude_paused/1](https://hexdocs.pm/good_job/GoodJob.Job.html#exclude_paused/1 "exclude_paused(query \\ __MODULE__)")
        *   [find_by_active_job_id/1](https://hexdocs.pm/good_job/GoodJob.Job.html#find_by_active_job_id/1 "find_by_active_job_id(active_job_id)")
        *   [find_by_id/1](https://hexdocs.pm/good_job/GoodJob.Job.html#find_by_id/1 "find_by_id(id)")
        *   [finished/1](https://hexdocs.pm/good_job/GoodJob.Job.html#finished/1 "finished(query \\ __MODULE__)")
        *   [finished_before/2](https://hexdocs.pm/good_job/GoodJob.Job.html#finished_before/2 "finished_before(query \\ __MODULE__, datetime)")
        *   [in_batch/2](https://hexdocs.pm/good_job/GoodJob.Job.html#in_batch/2 "in_batch(query \\ __MODULE__, batch_id)")
        *   [in_queue/2](https://hexdocs.pm/good_job/GoodJob.Job.html#in_queue/2 "in_queue(query \\ __MODULE__, queue_name)")
        *   [joins_advisory_locks/1](https://hexdocs.pm/good_job/GoodJob.Job.html#joins_advisory_locks/1 "joins_advisory_locks(query \\ __MODULE__)")
        *   [locked/1](https://hexdocs.pm/good_job/GoodJob.Job.html#locked/1 "locked(query \\ __MODULE__)")
        *   [only_scheduled/1](https://hexdocs.pm/good_job/GoodJob.Job.html#only_scheduled/1 "only_scheduled(query \\ __MODULE__)")
        *   [order_by_created_asc/1](https://hexdocs.pm/good_job/GoodJob.Job.html#order_by_created_asc/1 "order_by_created_asc(query \\ __MODULE__)")
        *   [order_by_created_desc/1](https://hexdocs.pm/good_job/GoodJob.Job.html#order_by_created_desc/1 "order_by_created_desc(query \\ __MODULE__)")
        *   [order_by_finished_desc/1](https://hexdocs.pm/good_job/GoodJob.Job.html#order_by_finished_desc/1 "order_by_finished_desc(query \\ __MODULE__)")
        *   [order_by_scheduled_asc/1](https://hexdocs.pm/good_job/GoodJob.Job.html#order_by_scheduled_asc/1 "order_by_scheduled_asc(query \\ __MODULE__)")
        *   [order_for_candidate_lookup/2](https://hexdocs.pm/good_job/GoodJob.Job.html#order_for_candidate_lookup/2 "order_for_candidate_lookup(query \\ __MODULE__, parsed_queues \\ %{})")
        *   [queued/1](https://hexdocs.pm/good_job/GoodJob.Job.html#queued/1 "queued(query \\ __MODULE__)")
        *   [retry/1](https://hexdocs.pm/good_job/GoodJob.Job.html#retry/1 "retry(job)")
        *   [running/1](https://hexdocs.pm/good_job/GoodJob.Job.html#running/1 "running(query \\ __MODULE__)")
        *   [scheduled/1](https://hexdocs.pm/good_job/GoodJob.Job.html#scheduled/1 "scheduled(query \\ __MODULE__)")
        *   [scheduled_before/2](https://hexdocs.pm/good_job/GoodJob.Job.html#scheduled_before/2 "scheduled_before(query \\ __MODULE__, datetime)")
        *   [succeeded/1](https://hexdocs.pm/good_job/GoodJob.Job.html#succeeded/1 "succeeded(query \\ __MODULE__)")
        *   [unfinished/1](https://hexdocs.pm/good_job/GoodJob.Job.html#unfinished/1 "unfinished(query \\ __MODULE__)")
        *   [unlocked/1](https://hexdocs.pm/good_job/GoodJob.Job.html#unlocked/1 "unlocked(query \\ __MODULE__)")
        *   [with_all_labels/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_all_labels/2 "with_all_labels(query \\ __MODULE__, labels)")
        *   [with_any_label/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_any_label/2 "with_any_label(query \\ __MODULE__, labels)")
        *   [with_batch_id/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_batch_id/2 "with_batch_id(query \\ __MODULE__, batch_id)")
        *   [with_concurrency_key/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_concurrency_key/2 "with_concurrency_key(query \\ __MODULE__, key)")
        *   [with_cron_key/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_cron_key/2 "with_cron_key(query \\ __MODULE__, cron_key)")
        *   [with_errors/1](https://hexdocs.pm/good_job/GoodJob.Job.html#with_errors/1 "with_errors(query \\ __MODULE__)")
        *   [with_job_class/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_job_class/2 "with_job_class(query \\ __MODULE__, job_class)")
        *   [with_label/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_label/2 "with_label(query \\ __MODULE__, label)")
        *   [with_labels/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_labels/2 "with_labels(query \\ __MODULE__, labels)")
        *   [with_max_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_max_priority/2 "with_max_priority(query \\ __MODULE__, max_priority)")
        *   [with_min_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_min_priority/2 "with_min_priority(query \\ __MODULE__, min_priority)")
        *   [with_priority/2](https://hexdocs.pm/good_job/GoodJob.Job.html#with_priority/2 "with_priority(query \\ __MODULE__, priority)")
        *   [without_errors/1](https://hexdocs.pm/good_job/GoodJob.Job.html#without_errors/1 "without_errors(query \\ __MODULE__)")

*   [GoodJob.JobExecutor](https://hexdocs.pm/good_job/GoodJob.JobExecutor.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobExecutor.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobExecutor.html#functions)
        *   [execute/3](https://hexdocs.pm/good_job/GoodJob.JobExecutor.html#execute/3 "execute(job, lock_id, opts \\ [])")
        *   [execute_inline/2](https://hexdocs.pm/good_job/GoodJob.JobExecutor.html#execute_inline/2 "execute_inline(job, opts \\ [])")

*   [GoodJob.JobState](https://hexdocs.pm/good_job/GoodJob.JobState.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobState.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.JobState.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.JobState.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobState.html#functions)
        *   [all/0](https://hexdocs.pm/good_job/GoodJob.JobState.html#all/0 "all()")
        *   [can_transition?/2](https://hexdocs.pm/good_job/GoodJob.JobState.html#can_transition?/2 "can_transition?(arg1, arg2)")
        *   [final?/1](https://hexdocs.pm/good_job/GoodJob.JobState.html#final?/1 "final?(arg1)")
        *   [from_string/1](https://hexdocs.pm/good_job/GoodJob.JobState.html#from_string/1 "from_string(string)")
        *   [to_string/1](https://hexdocs.pm/good_job/GoodJob.JobState.html#to_string/1 "to_string(state)")
        *   [transition/2](https://hexdocs.pm/good_job/GoodJob.JobState.html#transition/2 "transition(current, arg2)")
        *   [valid?/1](https://hexdocs.pm/good_job/GoodJob.JobState.html#valid?/1 "valid?(state)")

*   Scheduling
*   [GoodJob.Cron.Entry](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#functions)
        *   [enqueue/2](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#enqueue/2 "enqueue(entry, cron_at)")
        *   [new/1](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#new/1 "new(opts)")
        *   [next_at/2](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#next_at/2 "next_at(entry, previously_at \\ nil)")
        *   [within/3](https://hexdocs.pm/good_job/GoodJob.Cron.Entry.html#within/3 "within(entry, start_time, end_time)")

*   [GoodJob.Cron.Expression](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#functions)
        *   [next_at/2](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#next_at/2 "next_at(expr, time \\ DateTime.utc_now())")
        *   [now?/2](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#now?/2 "now?(cron, datetime)")
        *   [parse/1](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#parse/1 "parse(input)")
        *   [parse!/1](https://hexdocs.pm/good_job/GoodJob.Cron.Expression.html#parse!/1 "parse!(input)")

*   [GoodJob.CronManager](https://hexdocs.pm/good_job/GoodJob.CronManager.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.CronManager.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.CronManager.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.CronManager.html#child_spec/1 "child_spec(init_arg)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.CronManager.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.JobPerformer](https://hexdocs.pm/good_job/GoodJob.JobPerformer.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.JobPerformer.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.JobPerformer.html#functions)
        *   [parse_queues/1](https://hexdocs.pm/good_job/GoodJob.JobPerformer.html#parse_queues/1 "parse_queues(queue_string)")
        *   [perform_next/3](https://hexdocs.pm/good_job/GoodJob.JobPerformer.html#perform_next/3 "perform_next(queue_string, lock_id, opts \\ [])")

*   [GoodJob.Scheduler](https://hexdocs.pm/good_job/GoodJob.Scheduler.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Scheduler.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Scheduler.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Scheduler.html#child_spec/1 "child_spec(init_arg)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Scheduler.html#start_link/1 "start_link(opts)")

*   Infrastructure
*   [GoodJob.AdvisoryLock](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#functions)
        *   [hash_key/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#hash_key/1 "hash_key(key)")
        *   [job_id_to_lock_key/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#job_id_to_lock_key/1 "job_id_to_lock_key(job_id)")
        *   [key_to_lock_key/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#key_to_lock_key/1 "key_to_lock_key(key)")
        *   [lock/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#lock/1 "lock(key)")
        *   [lock_concurrency_key/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#lock_concurrency_key/1 "lock_concurrency_key(key)")
        *   [lock_job/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#lock_job/1 "lock_job(job_id)")
        *   [lock_session/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#lock_session/1 "lock_session(key)")
        *   [unlock_session/1](https://hexdocs.pm/good_job/GoodJob.AdvisoryLock.html#unlock_session/1 "unlock_session(key)")

*   [GoodJob.Notifier](https://hexdocs.pm/good_job/GoodJob.Notifier.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Notifier.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Notifier.html#functions)
        *   [add_recipient/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#add_recipient/1 "add_recipient(recipient)")
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#child_spec/1 "child_spec(opts)")
        *   [handle_call/3](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_call/3 "handle_call(arg1, from, state)")
        *   [handle_cast/2](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_cast/2 "handle_cast(arg, state)")
        *   [handle_connect/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_connect/1 "handle_connect(state)")
        *   [handle_disconnect/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_disconnect/1 "handle_disconnect(state)")
        *   [handle_info/2](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_info/2 "handle_info(arg1, state)")
        *   [handle_result/2](https://hexdocs.pm/good_job/GoodJob.Notifier.html#handle_result/2 "handle_result(result, state)")
        *   [init/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#init/1 "init(state)")
        *   [notify/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#notify/1 "notify(message)")
        *   [notify/3](https://hexdocs.pm/good_job/GoodJob.Notifier.html#notify/3 "notify(channel, payload, state)")
        *   [remove_recipient/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#remove_recipient/1 "remove_recipient(recipient)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Notifier.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.ProcessTracker](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html#child_spec/1 "child_spec(init_arg)")
        *   [id_for_lock/0](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html#id_for_lock/0 "id_for_lock()")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.ProcessTracker.html#start_link/1 "start_link(opts \\ [])")

*   [GoodJob.Repo](https://hexdocs.pm/good_job/GoodJob.Repo.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Repo.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Repo.html#functions)
        *   [query/2](https://hexdocs.pm/good_job/GoodJob.Repo.html#query/2 "query(sql, params \\ [])")
        *   [query_one/2](https://hexdocs.pm/good_job/GoodJob.Repo.html#query_one/2 "query_one(sql, params \\ [])")
        *   [repo/0](https://hexdocs.pm/good_job/GoodJob.Repo.html#repo/0 "repo()")

*   [GoodJob.Supervisor](https://hexdocs.pm/good_job/GoodJob.Supervisor.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#child_spec/1 "child_spec(init_arg)")
        *   [shutdown/1](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#shutdown/1 "shutdown(opts \\ [])")
        *   [shutdown?/0](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#shutdown?/0 "shutdown?()")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Supervisor.html#start_link/1 "start_link(opts \\ [])")

*   Features
*   [GoodJob.Backoff](https://hexdocs.pm/good_job/GoodJob.Backoff.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Backoff.html#content)
        *   [How It Works](https://hexdocs.pm/good_job/GoodJob.Backoff.html#module-how-it-works)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Backoff.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Backoff.html#functions)
        *   [add_jitter/2](https://hexdocs.pm/good_job/GoodJob.Backoff.html#add_jitter/2 "add_jitter(delay, jitter)")
        *   [constant/2](https://hexdocs.pm/good_job/GoodJob.Backoff.html#constant/2 "constant(attempt, opts \\ [])")
        *   [exponential/2](https://hexdocs.pm/good_job/GoodJob.Backoff.html#exponential/2 "exponential(attempt, opts \\ [])")
        *   [linear/2](https://hexdocs.pm/good_job/GoodJob.Backoff.html#linear/2 "linear(attempt, opts \\ [])")
        *   [polynomial/2](https://hexdocs.pm/good_job/GoodJob.Backoff.html#polynomial/2 "polynomial(executions, opts \\ [])")

*   [GoodJob.Batch](https://hexdocs.pm/good_job/GoodJob.Batch.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Batch.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Batch.html#functions)
        *   [%GoodJob.Batch{}](https://hexdocs.pm/good_job/GoodJob.Batch.html#__struct__/0 "%GoodJob.Batch{}")
        *   [add_job/4](https://hexdocs.pm/good_job/GoodJob.Batch.html#add_job/4 "add_job(batch, job_module, args, opts \\ [])")
        *   [check_completion/2](https://hexdocs.pm/good_job/GoodJob.Batch.html#check_completion/2 "check_completion(batch_id, job \\ nil)")
        *   [enqueue/1](https://hexdocs.pm/good_job/GoodJob.Batch.html#enqueue/1 "enqueue(batch)")
        *   [new/1](https://hexdocs.pm/good_job/GoodJob.Batch.html#new/1 "new(opts \\ [])")
        *   [retry_batch/1](https://hexdocs.pm/good_job/GoodJob.Batch.html#retry_batch/1 "retry_batch(batch)")

*   [GoodJob.BatchRecord](https://hexdocs.pm/good_job/GoodJob.BatchRecord.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.BatchRecord.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.BatchRecord.html#functions)
        *   [changeset/2](https://hexdocs.pm/good_job/GoodJob.BatchRecord.html#changeset/2 "changeset(batch, attrs)")
        *   [finished_before/2](https://hexdocs.pm/good_job/GoodJob.BatchRecord.html#finished_before/2 "finished_before(query \\ __MODULE__, cutoff)")

*   [GoodJob.Cleanup](https://hexdocs.pm/good_job/GoodJob.Cleanup.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Cleanup.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Cleanup.html#functions)
        *   [cleanup_preserved_jobs/1](https://hexdocs.pm/good_job/GoodJob.Cleanup.html#cleanup_preserved_jobs/1 "cleanup_preserved_jobs(opts \\ [])")

*   [GoodJob.Concurrency](https://hexdocs.pm/good_job/GoodJob.Concurrency.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Concurrency.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Concurrency.html#functions)
        *   [check_enqueue_limit/2](https://hexdocs.pm/good_job/GoodJob.Concurrency.html#check_enqueue_limit/2 "check_enqueue_limit(concurrency_key, config)")
        *   [check_perform_limit/3](https://hexdocs.pm/good_job/GoodJob.Concurrency.html#check_perform_limit/3 "check_perform_limit(concurrency_key, job_id, config)")

*   [GoodJob.HealthCheck](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#functions)
        *   [check/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#check/0 "check()")
        *   [check_database/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#check_database/0 "check_database()")
        *   [check_notifier/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#check_notifier/0 "check_notifier()")
        *   [check_schedulers/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#check_schedulers/0 "check_schedulers()")
        *   [check_supervisor/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#check_supervisor/0 "check_supervisor()")
        *   [status/0](https://hexdocs.pm/good_job/GoodJob.HealthCheck.html#status/0 "status()")

*   Testing
*   [GoodJob.Testing](https://hexdocs.pm/good_job/GoodJob.Testing.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Testing.html#content)
        *   [Usage](https://hexdocs.pm/good_job/GoodJob.Testing.html#module-usage)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Testing.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Testing.html#functions)
        *   [assert_enqueued/3](https://hexdocs.pm/good_job/GoodJob.Testing.html#assert_enqueued/3 "assert_enqueued(job_module, args, opts \\ [])")
        *   [assert_performed/1](https://hexdocs.pm/good_job/GoodJob.Testing.html#assert_performed/1 "assert_performed(job)")
        *   [perform_jobs/1](https://hexdocs.pm/good_job/GoodJob.Testing.html#perform_jobs/1 "perform_jobs(job_module \\ nil)")
        *   [refute_enqueued/3](https://hexdocs.pm/good_job/GoodJob.Testing.html#refute_enqueued/3 "refute_enqueued(job_module, args \\ %{}, opts \\ [])")

*   [GoodJob.Testing.Assertions](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html#functions)
        *   [assert_enqueued/3](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html#assert_enqueued/3 "assert_enqueued(job_module, args, opts \\ [])")
        *   [assert_performed/1](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html#assert_performed/1 "assert_performed(job)")
        *   [refute_enqueued/3](https://hexdocs.pm/good_job/GoodJob.Testing.Assertions.html#refute_enqueued/3 "refute_enqueued(job_module, args \\ %{}, opts \\ [])")

*   [GoodJob.Testing.Helpers](https://hexdocs.pm/good_job/GoodJob.Testing.Helpers.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Testing.Helpers.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Testing.Helpers.html#functions)
        *   [perform_jobs/1](https://hexdocs.pm/good_job/GoodJob.Testing.Helpers.html#perform_jobs/1 "perform_jobs(job_module \\ nil)")

*   [GoodJob.Testing.JobCase](https://hexdocs.pm/good_job/GoodJob.Testing.JobCase.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Testing.JobCase.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Testing.JobCase.html#functions)
        *   [create_job/1](https://hexdocs.pm/good_job/GoodJob.Testing.JobCase.html#create_job/1 "create_job(attrs \\ %{})")

*   [GoodJob.Testing.RepoCase](https://hexdocs.pm/good_job/GoodJob.Testing.RepoCase.html)
*   Web
*   [GoodJob.Web.LiveDashboard](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboard.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboard.html#content)
        *   [Installation](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboard.html#module-installation)
        *   [Features](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboard.html#module-features)

*   [GoodJob.Web.LiveDashboardPage](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#functions)
        *   [__page_live__/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#__page_live__/1 "__page_live__(opts)")
        *   [echarts_js_path/0](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#echarts_js_path/0 "echarts_js_path()")
        *   [init/1](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#init/1 "init(opts)")
        *   [menu_link/2](https://hexdocs.pm/good_job/GoodJob.Web.LiveDashboardPage.html#menu_link/2 "menu_link(session, capabilities)")

*   Plugins
*   [GoodJob.Plugin](https://hexdocs.pm/good_job/GoodJob.Plugin.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Plugin.html#content)
        *   [Example](https://hexdocs.pm/good_job/GoodJob.Plugin.html#module-example)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Plugin.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.Plugin.html#types)
        *   [option/0](https://hexdocs.pm/good_job/GoodJob.Plugin.html#t:option/0 "option()")

    *   [Callbacks](https://hexdocs.pm/good_job/GoodJob.Plugin.html#callbacks)
        *   [format_logger_output/2](https://hexdocs.pm/good_job/GoodJob.Plugin.html#c:format_logger_output/2 "format_logger_output(t, map)")
        *   [start_link/1](https://hexdocs.pm/good_job/GoodJob.Plugin.html#c:start_link/1 "start_link(list)")
        *   [validate/1](https://hexdocs.pm/good_job/GoodJob.Plugin.html#c:validate/1 "validate(list)")

*   [GoodJob.Plugins.Lifeline](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#content)
        *   [Configuration](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#module-configuration)
        *   [Options](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#module-options)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Plugins.Lifeline.html#child_spec/1 "child_spec(init_arg)")

*   [GoodJob.Plugins.Pruner](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#content)
        *   [Configuration](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#module-configuration)
        *   [Options](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#module-options)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#functions)
        *   [child_spec/1](https://hexdocs.pm/good_job/GoodJob.Plugins.Pruner.html#child_spec/1 "child_spec(init_arg)")

*   Telemetry
*   [GoodJob.Telemetry](https://hexdocs.pm/good_job/GoodJob.Telemetry.html)
    *   [Sections](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#content)
        *   [Default Logger](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#module-default-logger)
        *   [Custom Handlers](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#module-custom-handlers)

    *   [Summary](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#summary)
    *   [Functions](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#functions)
        *   [attach_default_logger/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#attach_default_logger/1 "attach_default_logger(opts \\ [])")
        *   [batch_callback/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#batch_callback/3 "batch_callback(batch_record, event, callback_string)")
        *   [batch_complete/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#batch_complete/2 "batch_complete(batch_record, discarded_count)")
        *   [batch_enqueue/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#batch_enqueue/2 "batch_enqueue(batch_record, job_count)")
        *   [batch_retry/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#batch_retry/1 "batch_retry(batch_record)")
        *   [cleanup_preserved_jobs/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#cleanup_preserved_jobs/2 "cleanup_preserved_jobs(deleted_count, opts)")
        *   [cleanup_triggered/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#cleanup_triggered/1 "cleanup_triggered(reason)")
        *   [concurrency_limit_exceeded/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#concurrency_limit_exceeded/3 "concurrency_limit_exceeded(concurrency_key, limit, type)")
        *   [concurrency_throttle_exceeded/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#concurrency_throttle_exceeded/3 "concurrency_throttle_exceeded(concurrency_key, throttle, type)")
        *   [cron_job_enqueued/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#cron_job_enqueued/2 "cron_job_enqueued(entry, cron_at)")
        *   [cron_manager_start/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#cron_manager_start/1 "cron_manager_start(cron_entries)")
        *   [default_handler_id/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#default_handler_id/0 "default_handler_id()")
        *   [detach_default_logger/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#detach_default_logger/0 "detach_default_logger()")
        *   [enqueue/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#enqueue/1 "enqueue(job)")
        *   [execute_error/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#execute_error/3 "execute_error(job, error, start_time)")
        *   [execute_exception/5](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#execute_exception/5 "execute_exception(job, error, kind, stacktrace, start_time)")
        *   [execute_start/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#execute_start/1 "execute_start(job)")
        *   [execute_success/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#execute_success/3 "execute_success(job, result, start_time)")
        *   [execute_timeout/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#execute_timeout/3 "execute_timeout(job, timeout_ms, start_time)")
        *   [job_cancel/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_cancel/3 "job_cancel(job, reason, start_time)")
        *   [job_delete/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_delete/1 "job_delete(job)")
        *   [job_discard/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_discard/3 "job_discard(job, reason, start_time)")
        *   [job_locked/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_locked/2 "job_locked(job, lock_id)")
        *   [job_retry_manual/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_retry_manual/1 "job_retry_manual(job)")
        *   [job_snooze/3](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_snooze/3 "job_snooze(job, seconds, start_time)")
        *   [job_unlocked/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#job_unlocked/2 "job_unlocked(job, lock_id)")
        *   [lock_acquired/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#lock_acquired/2 "lock_acquired(lock_key, lock_type)")
        *   [lock_failed/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#lock_failed/2 "lock_failed(lock_key, lock_type)")
        *   [notifier_connection_error/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#notifier_connection_error/2 "notifier_connection_error(error_count, error)")
        *   [notifier_listen/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#notifier_listen/0 "notifier_listen()")
        *   [notifier_notified/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#notifier_notified/1 "notifier_notified(payload)")
        *   [process_heartbeat/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#process_heartbeat/1 "process_heartbeat(process_id)")
        *   [retry/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#retry/2 "retry(job, scheduled_at)")
        *   [scheduler_job_fetched/2](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#scheduler_job_fetched/2 "scheduler_job_fetched(job, queue_string)")
        *   [scheduler_job_not_found/1](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#scheduler_job_not_found/1 "scheduler_job_not_found(queue_string)")
        *   [scheduler_poll/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#scheduler_poll/0 "scheduler_poll()")
        *   [scheduler_process_created/0](https://hexdocs.pm/good_job/GoodJob.Telemetry.html#scheduler_process_created/0 "scheduler_process_created()")

*   Exceptions
*   [GoodJob.Concurrency.ConcurrencyExceededError](https://hexdocs.pm/good_job/GoodJob.Concurrency.ConcurrencyExceededError.html)
*   [GoodJob.Concurrency.ThrottleExceededError](https://hexdocs.pm/good_job/GoodJob.Concurrency.ThrottleExceededError.html)
*   [GoodJob.CrashError](https://hexdocs.pm/good_job/GoodJob.CrashError.html)
*   [GoodJob.Errors.ConcurrencyExceededError](https://hexdocs.pm/good_job/GoodJob.Errors.ConcurrencyExceededError.html)
*   [GoodJob.Errors.ConfigurationError](https://hexdocs.pm/good_job/GoodJob.Errors.ConfigurationError.html)
*   [GoodJob.Errors.InterruptError](https://hexdocs.pm/good_job/GoodJob.Errors.InterruptError.html)
*   [GoodJob.Errors.JobTimeoutError](https://hexdocs.pm/good_job/GoodJob.Errors.JobTimeoutError.html)
*   [GoodJob.Errors.PreviouslyPerformedError](https://hexdocs.pm/good_job/GoodJob.Errors.PreviouslyPerformedError.html)
*   [GoodJob.Errors.ThrottleExceededError](https://hexdocs.pm/good_job/GoodJob.Errors.ThrottleExceededError.html)
*   [GoodJob.ExternalJob.LocalExecutionError](https://hexdocs.pm/good_job/GoodJob.ExternalJob.LocalExecutionError.html)
*   [GoodJob.InterruptError](https://hexdocs.pm/good_job/GoodJob.InterruptError.html)
    *   [Summary](https://hexdocs.pm/good_job/GoodJob.InterruptError.html#summary)
    *   [Types](https://hexdocs.pm/good_job/GoodJob.InterruptError.html#types)
        *   [t/0](https://hexdocs.pm/good_job/GoodJob.InterruptError.html#t:t/0 "t()")

*   [mix good_job.install](https://hexdocs.pm/good_job/Mix.Tasks.GoodJob.Install.html)

Search documentation of good_job 

Default

Default In-browser search

Settings

GoodJob.Backoff(good_job v0.2.0)
================================

[View Source](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L1 "View Source")

Provides backoff calculation strategies for job retries.

This module calculates the delay (in seconds) before retrying a failed job. It does NOT handle retry logic itself - that's handled by the job retry/discard system.

Aligned with Ruby GoodJob's ActiveJob retry behavior:

*   Default: Constant 3 seconds (matches Ruby GoodJob's `retry_on` default)
*   Supports exponential, linear, constant, and polynomial backoff
*   Default jitter: 15% (0.15) to match Ruby GoodJob's ActiveJob default

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#module-how-it-works)How It Works
------------------------------------------------------------------------------------

When a job fails and the retry system decides to retry it:

1.   The job's `backoff/1` callback (or default) is called to calculate the delay
2.   The job is rescheduled with `scheduled_at = now + backoff_seconds`
3.   The scheduler picks up the job when `scheduled_at` is reached

This is separate from the retry/discard decision logic, which determines whether a job should be retried at all.

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#summary)Summary
===================================================================

[Functions](https://hexdocs.pm/good_job/GoodJob.Backoff.html#functions)
-----------------------------------------------------------------------

[add_jitter(delay, jitter)](https://hexdocs.pm/good_job/GoodJob.Backoff.html#add_jitter/2)

Adds jitter to a delay value.

[constant(attempt, opts \\ [])](https://hexdocs.pm/good_job/GoodJob.Backoff.html#constant/2)

Calculates constant backoff.

[exponential(attempt, opts \\ [])](https://hexdocs.pm/good_job/GoodJob.Backoff.html#exponential/2)

Calculates exponential backoff with jitter.

[linear(attempt, opts \\ [])](https://hexdocs.pm/good_job/GoodJob.Backoff.html#linear/2)

Calculates linear backoff.

[polynomial(executions, opts \\ [])](https://hexdocs.pm/good_job/GoodJob.Backoff.html#polynomial/2)

Calculates polynomial backoff (matches Ruby ActiveJob's `:polynomially_longer`).

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#functions)Functions
=======================================================================

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#add_jitter/2)

add_jitter(delay, jitter)
=========================

[](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L154)

@spec add_jitter([integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)(), [float](https://hexdocs.pm/elixir/typespecs.html#basic-types)()) :: [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Adds jitter to a delay value.

Uses additive-only jitter calculation (rand _delay_ jitter), matching Ruby GoodJob's behavior. Default jitter is 15% (0.15) to match Ruby ActiveJob's default.

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#add_jitter/2-examples)Examples
----------------------------------------------------------------------------------

```
iex> jittered = GoodJob.Backoff.add_jitter(100, 0.15)
...> jittered >= 100 and jittered <= 115
true
```

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#constant/2)

constant(attempt, opts \\ [])
=============================

[](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L78)

@spec constant(
  [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)(),
  [keyword](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()
) :: [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Calculates constant backoff.

This is the default strategy for Ruby GoodJob (ActiveJob's `retry_on` default wait: 3 seconds).

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#constant/2-examples)Examples
--------------------------------------------------------------------------------

```
iex> GoodJob.Backoff.constant(1)
3

iex> GoodJob.Backoff.constant(3)
3

iex> GoodJob.Backoff.constant(1, base: 5)
5
```

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#exponential/2)

exponential(attempt, opts \\ [])
================================

[](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L43)

@spec exponential(
  [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)(),
  [keyword](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()
) :: [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Calculates exponential backoff with jitter.

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#exponential/2-examples)Examples
-----------------------------------------------------------------------------------

```
iex> GoodJob.Backoff.exponential(1)
2

iex> GoodJob.Backoff.exponential(3)
8
```

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#linear/2)

linear(attempt, opts \\ [])
===========================

[](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L101)

@spec linear(
  [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)(),
  [keyword](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()
) :: [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Calculates linear backoff.

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#linear/2-examples)Examples
------------------------------------------------------------------------------

```
iex> GoodJob.Backoff.linear(1, base: 5)
5

iex> GoodJob.Backoff.linear(3, base: 5)
15
```

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#polynomial/2)

polynomial(executions, opts \\ [])
==================================

[](https://github.com/amkisko/good_job.ex/blob/v0.2.0/lib/good_job/backoff.ex#L124)

@spec polynomial(
  [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)(),
  [keyword](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()
) :: [integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Calculates polynomial backoff (matches Ruby ActiveJob's `:polynomially_longer`).

Formula: `((executions^4) + (rand * executions^4 * jitter)) + 2`

This matches Ruby ActiveJob's polynomial backoff strategy.

[](https://hexdocs.pm/good_job/GoodJob.Backoff.html#polynomial/2-examples)Examples
----------------------------------------------------------------------------------

```
iex> delay = GoodJob.Backoff.polynomial(1)
...> delay >= 2 and delay <= 3
true

iex> delay = GoodJob.Backoff.polynomial(2)
...> delay >= 18 and delay <= 19
true
```

[Hex Package](https://hex.pm/packages/good_job/0.2.0)[Hex Preview](https://preview.hex.pm/preview/good_job/0.2.0) Go to package docs [Download ePub version](https://hexdocs.pm/good_job/good_job.epub "ePub version")

Built using [ExDoc](https://github.com/elixir-lang/ex_doc "ExDoc") (v0.39.3) for the [Elixir programming language](https://elixir-lang.org/ "Elixir")
