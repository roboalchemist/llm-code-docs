# Source: https://zuul-ci.org/docs/zuul/latest/configuration.html

Title: Configuration — Zuul  documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/configuration.html

Published Time: Wed, 11 Mar 2026 16:34:13 GMT

Markdown Content:
Configuration — Zuul documentation
===============

[![Image 1: Logo](https://zuul-ci.org/docs/zuul/latest/_static/logo.svg)](https://zuul-ci.org/docs/zuul/latest/index.html)

*   [About Zuul](https://zuul-ci.org/docs/zuul/latest/about.html)
    *   [Zuul Concepts](https://zuul-ci.org/docs/zuul/latest/concepts.html)
    *   [Project Gating](https://zuul-ci.org/docs/zuul/latest/gating.html)
        *   [Testing in parallel](https://zuul-ci.org/docs/zuul/latest/gating.html#testing-in-parallel)
            *   [Pipeline Window](https://zuul-ci.org/docs/zuul/latest/gating.html#pipeline-window)

        *   [Cross Project Testing](https://zuul-ci.org/docs/zuul/latest/gating.html#cross-project-testing)
        *   [Cross-Project Dependencies](https://zuul-ci.org/docs/zuul/latest/gating.html#cross-project-dependencies)
            *   [Dependent Pipeline](https://zuul-ci.org/docs/zuul/latest/gating.html#dependent-pipeline)
            *   [Independent Pipeline](https://zuul-ci.org/docs/zuul/latest/gating.html#independent-pipeline)
            *   [Multiple Changes](https://zuul-ci.org/docs/zuul/latest/gating.html#multiple-changes)
            *   [Cycles](https://zuul-ci.org/docs/zuul/latest/gating.html#cycles)
            *   [Global Repo State](https://zuul-ci.org/docs/zuul/latest/gating.html#global-repo-state)

*   [Quick-Start Installation and Tutorial](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html)
    *   [Start Zuul Containers](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#start-zuul-containers)
    *   [Add Your Gerrit Account](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#add-your-gerrit-account)
    *   [Configure Zuul Pipelines](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#configure-zuul-pipelines)
    *   [Test Zuul Pipelines](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#test-zuul-pipelines)
    *   [Configure a Base Job](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#configure-a-base-job)
    *   [Further Steps](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#further-steps)

*   [Project Configuration](https://zuul-ci.org/docs/zuul/latest/project-config.html)
    *   [Security Contexts](https://zuul-ci.org/docs/zuul/latest/project-config.html#security-contexts)
    *   [Configuration Loading](https://zuul-ci.org/docs/zuul/latest/project-config.html#configuration-loading)
    *   [Regular Expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regular-expressions)
    *   [Encryption](https://zuul-ci.org/docs/zuul/latest/project-config.html#encryption)
    *   [Configuration Items](https://zuul-ci.org/docs/zuul/latest/project-config.html#configuration-items)
        *   [Pipeline](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html)
        *   [Job](https://zuul-ci.org/docs/zuul/latest/config/job.html)
        *   [Project](https://zuul-ci.org/docs/zuul/latest/config/project.html)
        *   [Project Template](https://zuul-ci.org/docs/zuul/latest/config/project.html#project-template)
        *   [Queue](https://zuul-ci.org/docs/zuul/latest/config/queue.html)
        *   [Secret](https://zuul-ci.org/docs/zuul/latest/config/secret.html)
            *   [Data Secrets](https://zuul-ci.org/docs/zuul/latest/config/secret.html#data-secrets)
            *   [Token Secrets](https://zuul-ci.org/docs/zuul/latest/config/secret.html#token-secrets)
            *   [Usage](https://zuul-ci.org/docs/zuul/latest/config/secret.html#usage)

        *   [Nodeset](https://zuul-ci.org/docs/zuul/latest/config/nodeset.html)
        *   [Semaphore](https://zuul-ci.org/docs/zuul/latest/config/semaphore.html)
        *   [Pragma](https://zuul-ci.org/docs/zuul/latest/config/pragma.html)
        *   [Image](https://zuul-ci.org/docs/zuul/latest/config/image.html)
        *   [Flavor](https://zuul-ci.org/docs/zuul/latest/config/flavor.html)
        *   [Label](https://zuul-ci.org/docs/zuul/latest/config/label.html)
        *   [Section](https://zuul-ci.org/docs/zuul/latest/config/section.html)
        *   [Provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html)

*   [Job Content](https://zuul-ci.org/docs/zuul/latest/job-content.html)
    *   [Working Directory](https://zuul-ci.org/docs/zuul/latest/job-content.html#working-directory)
    *   [Git Repositories](https://zuul-ci.org/docs/zuul/latest/job-content.html#git-repositories)
    *   [Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#variables)
        *   [Site-wide Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#site-wide-variables)
        *   [Job Extra Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#job-extra-variables)
        *   [Secrets](https://zuul-ci.org/docs/zuul/latest/job-content.html#secrets)
        *   [Job Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#job-variables)
        *   [Project Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#project-variables)
        *   [File Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#file-variables)
        *   [Parent Job Results](https://zuul-ci.org/docs/zuul/latest/job-content.html#parent-job-results)

    *   [Zuul Variables](https://zuul-ci.org/docs/zuul/latest/job-content.html#zuul-variables)
        *   [Job Ref](https://zuul-ci.org/docs/zuul/latest/job-content.html#job-ref)
        *   [Item](https://zuul-ci.org/docs/zuul/latest/job-content.html#item)
        *   [Job](https://zuul-ci.org/docs/zuul/latest/job-content.html#job)
        *   [Working Directory](https://zuul-ci.org/docs/zuul/latest/job-content.html#id2)

    *   [SSH Keys](https://zuul-ci.org/docs/zuul/latest/job-content.html#ssh-keys)
        *   [Nodepool Key](https://zuul-ci.org/docs/zuul/latest/job-content.html#nodepool-key)
        *   [Tenant Key](https://zuul-ci.org/docs/zuul/latest/job-content.html#tenant-key)
        *   [Project Key](https://zuul-ci.org/docs/zuul/latest/job-content.html#project-key)

    *   [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values)
        *   [Returning the log url](https://zuul-ci.org/docs/zuul/latest/job-content.html#returning-the-log-url)
        *   [Returning artifact URLs](https://zuul-ci.org/docs/zuul/latest/job-content.html#returning-artifact-urls)
        *   [Skipping dependent jobs](https://zuul-ci.org/docs/zuul/latest/job-content.html#skipping-dependent-jobs)
        *   [Leaving warnings](https://zuul-ci.org/docs/zuul/latest/job-content.html#leaving-warnings)
        *   [Leaving file comments](https://zuul-ci.org/docs/zuul/latest/job-content.html#leaving-file-comments)
        *   [Pausing the job](https://zuul-ci.org/docs/zuul/latest/job-content.html#pausing-the-job)
        *   [Skipping retries](https://zuul-ci.org/docs/zuul/latest/job-content.html#skipping-retries)

    *   [Ansible Groups](https://zuul-ci.org/docs/zuul/latest/job-content.html#ansible-groups)
    *   [Build Status](https://zuul-ci.org/docs/zuul/latest/job-content.html#id5)

*   [Service Administration](https://zuul-ci.org/docs/zuul/latest/admin.html)
    *   [Installation](https://zuul-ci.org/docs/zuul/latest/installation.html)
        *   [External Dependencies](https://zuul-ci.org/docs/zuul/latest/installation.html#external-dependencies)
            *   [Nodepool](https://zuul-ci.org/docs/zuul/latest/installation.html#nodepool)
            *   [ZooKeeper](https://zuul-ci.org/docs/zuul/latest/installation.html#zookeeper)

        *   [Executor Deployment](https://zuul-ci.org/docs/zuul/latest/installation.html#executor-deployment)
        *   [Web Deployment](https://zuul-ci.org/docs/zuul/latest/installation.html#web-deployment)
            *   [Reverse Proxy](https://zuul-ci.org/docs/zuul/latest/installation.html#reverse-proxy)
            *   [Static Offload](https://zuul-ci.org/docs/zuul/latest/installation.html#static-offload)
            *   [Sub directory serving](https://zuul-ci.org/docs/zuul/latest/installation.html#sub-directory-serving)
            *   [White Labeled Tenant](https://zuul-ci.org/docs/zuul/latest/installation.html#white-labeled-tenant)
            *   [Static External](https://zuul-ci.org/docs/zuul/latest/installation.html#static-external)

    *   [Upgrading](https://zuul-ci.org/docs/zuul/latest/upgrading.html)
        *   [Rolling Upgrades](https://zuul-ci.org/docs/zuul/latest/upgrading.html#rolling-upgrades)
        *   [Skipping Versions](https://zuul-ci.org/docs/zuul/latest/upgrading.html#skipping-versions)

    *   [Component Overview](https://zuul-ci.org/docs/zuul/latest/components.html)
    *   [Configuration](https://zuul-ci.org/docs/zuul/latest/configuration.html#)
        *   [Common Options](https://zuul-ci.org/docs/zuul/latest/configuration.html#common-options)
            *   [Statsd](https://zuul-ci.org/docs/zuul/latest/configuration.html#statsd)
            *   [Tracing](https://zuul-ci.org/docs/zuul/latest/configuration.html#tracing)
            *   [ZooKeeper](https://zuul-ci.org/docs/zuul/latest/configuration.html#zookeeper)
            *   [Database](https://zuul-ci.org/docs/zuul/latest/configuration.html#database)
            *   [OIDC](https://zuul-ci.org/docs/zuul/latest/configuration.html#oidc)

        *   [Scheduler](https://zuul-ci.org/docs/zuul/latest/configuration.html#scheduler)
        *   [Merger](https://zuul-ci.org/docs/zuul/latest/configuration.html#merger)
        *   [Executor](https://zuul-ci.org/docs/zuul/latest/configuration.html#executor)
            *   [Trusted and Untrusted Playbooks](https://zuul-ci.org/docs/zuul/latest/configuration.html#trusted-and-untrusted-playbooks)
            *   [Security Considerations](https://zuul-ci.org/docs/zuul/latest/configuration.html#security-considerations)
            *   [Configuration](https://zuul-ci.org/docs/zuul/latest/configuration.html#id5)

        *   [Web Server](https://zuul-ci.org/docs/zuul/latest/configuration.html#web-server)
            *   [Authentication](https://zuul-ci.org/docs/zuul/latest/configuration.html#authentication)
                *   [Driver-specific attributes](https://zuul-ci.org/docs/zuul/latest/configuration.html#driver-specific-attributes)
                    *   [HS256](https://zuul-ci.org/docs/zuul/latest/configuration.html#hs256)
                    *   [RS256](https://zuul-ci.org/docs/zuul/latest/configuration.html#rs256)
                    *   [RS256withJWKS](https://zuul-ci.org/docs/zuul/latest/configuration.html#rs256withjwks)
                    *   [OpenIDConnect](https://zuul-ci.org/docs/zuul/latest/configuration.html#openidconnect)

        *   [Launcher](https://zuul-ci.org/docs/zuul/latest/configuration.html#launcher)
        *   [Client](https://zuul-ci.org/docs/zuul/latest/configuration.html#client)
        *   [Finger Gateway](https://zuul-ci.org/docs/zuul/latest/configuration.html#finger-gateway)

    *   [Connections](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections)
    *   [Drivers](https://zuul-ci.org/docs/zuul/latest/drivers/index.html)
        *   [Gerrit](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#connection-configuration)
                *   [SSH Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#ssh-configuration)
                *   [HTTP Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#http-configuration)
                *   [Kafka Event Support](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#kafka-event-support)
                *   [AWS Kinesis Event Support](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#aws-kinesis-event-support)
                *   [Google Cloud Pub/Sub Event Support](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#google-cloud-pub-sub-event-support)

            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#trigger-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#reporter-configuration)
            *   [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#requirements-configuration)
            *   [Reference Pipelines Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#reference-pipelines-configuration)
            *   [Checks Plugin Support (Deprecated)](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#checks-plugin-support-deprecated)

        *   [Git](https://zuul-ci.org/docs/zuul/latest/drivers/git.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/git.html#connection-configuration)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/git.html#trigger-configuration)

        *   [GitHub](https://zuul-ci.org/docs/zuul/latest/drivers/github.html)
            *   [Configure GitHub](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#configure-github)
                *   [Web-Hook](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#web-hook)
                *   [Application](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#application)

            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#connection-configuration)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#trigger-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reporter-configuration)
            *   [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#requirements-configuration)
            *   [Reference pipelines configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reference-pipelines-configuration)
                *   [Branch protection rules](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#branch-protection-rules)
                *   [Reference pipelines](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reference-pipelines)

            *   [Github Checks API](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-checks-api)
                *   [Design decisions](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#design-decisions)
                *   [Behaviour in Zuul](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#behaviour-in-zuul)
                    *   [Reporting](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reporting)
                    *   [Trigger](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#trigger)
                    *   [Requirements](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#requirements)

                *   [Actions / Events](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#actions-events)
                *   [File comments (annotations)](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#file-comments-annotations)
                    *   [Custom actions](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#custom-actions)

                *   [Restrictions and Recommendations](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#restrictions-and-recommendations)

        *   [GitLab](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html)
            *   [Configure GitLab](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#configure-gitlab)
                *   [web-hooks](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#web-hooks)
                *   [API](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#api)

            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#connection-configuration)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#trigger-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#reporter-configuration)
            *   [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#requirements-configuration)
            *   [Reference pipelines configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#reference-pipelines-configuration)

        *   [Pagure](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html)
            *   [Configure Pagure](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#configure-pagure)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#connection-configuration)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#trigger-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#reporter-configuration)
            *   [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#requirements-configuration)
            *   [Reference pipelines configuration](https://zuul-ci.org/docs/zuul/latest/drivers/pagure.html#reference-pipelines-configuration)

        *   [Elasticsearch](https://zuul-ci.org/docs/zuul/latest/drivers/elasticsearch.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/elasticsearch.html#connection-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/elasticsearch.html#reporter-configuration)

        *   [MQTT](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html)
            *   [Message Schema](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#message-schema)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#connection-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#reporter-configuration)

        *   [SMTP](https://zuul-ci.org/docs/zuul/latest/drivers/smtp.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/smtp.html#connection-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/smtp.html#reporter-configuration)

        *   [Timer](https://zuul-ci.org/docs/zuul/latest/drivers/timer.html)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/timer.html#trigger-configuration)

        *   [Zuul](https://zuul-ci.org/docs/zuul/latest/drivers/zuul.html)
            *   [Trigger Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/zuul.html#trigger-configuration)
            *   [Reporter Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/zuul.html#reporter-configuration)

        *   [AWS](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#connection-configuration)
            *   [Provider Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/aws.html#provider-configuration)

        *   [Azure](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#connection-configuration)
            *   [Provider Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/azure.html#provider-configuration)

        *   [Kubernetes](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#connection-configuration)
            *   [Provider Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/kubernetes.html#provider-configuration)

        *   [OpenStack](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#connection-configuration)
            *   [Provider Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html#provider-configuration)

        *   [Static](https://zuul-ci.org/docs/zuul/latest/drivers/static.html)
            *   [Connection Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#connection-configuration)
            *   [Provider Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#provider-configuration)

    *   [Tenant Configuration](https://zuul-ci.org/docs/zuul/latest/tenants.html)
        *   [Tenant](https://zuul-ci.org/docs/zuul/latest/tenants.html#tenant)
        *   [Global Semaphore](https://zuul-ci.org/docs/zuul/latest/tenants.html#global-semaphore)
        *   [Authorization Rule](https://zuul-ci.org/docs/zuul/latest/tenants.html#authorization-rule)
        *   [Authorization Rule Templating](https://zuul-ci.org/docs/zuul/latest/tenants.html#authorization-rule-templating)
        *   [Role](https://zuul-ci.org/docs/zuul/latest/tenants.html#role)
        *   [API Root](https://zuul-ci.org/docs/zuul/latest/tenants.html#api-root)

    *   [Build Nodes](https://zuul-ci.org/docs/zuul/latest/build-nodes.html)
        *   [Node Reuse](https://zuul-ci.org/docs/zuul/latest/build-nodes.html#node-reuse)
        *   [Image Creation](https://zuul-ci.org/docs/zuul/latest/build-nodes.html#image-creation)
        *   [Image Validation](https://zuul-ci.org/docs/zuul/latest/build-nodes.html#image-validation)
        *   [Nodepool Migration](https://zuul-ci.org/docs/zuul/latest/build-nodes.html#nodepool-migration)

    *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html)
        *   [Scheduler](https://zuul-ci.org/docs/zuul/latest/operation.html#scheduler)
            *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html#id2)
            *   [Reconfiguration](https://zuul-ci.org/docs/zuul/latest/operation.html#reconfiguration)
            *   [Advanced Options](https://zuul-ci.org/docs/zuul/latest/operation.html#advanced-options)
            *   [Managing Event Processing](https://zuul-ci.org/docs/zuul/latest/operation.html#managing-event-processing)
            *   [Backup and Restoration](https://zuul-ci.org/docs/zuul/latest/operation.html#backup-and-restoration)

        *   [Merger](https://zuul-ci.org/docs/zuul/latest/operation.html#merger)
            *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html#id4)

        *   [Executor](https://zuul-ci.org/docs/zuul/latest/operation.html#executor)
            *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html#id5)
            *   [Ansible and Python 3](https://zuul-ci.org/docs/zuul/latest/operation.html#ansible-and-python-3)
            *   [Log Streaming](https://zuul-ci.org/docs/zuul/latest/operation.html#log-streaming)
                *   [Posix Log Streaming](https://zuul-ci.org/docs/zuul/latest/operation.html#posix-log-streaming)
                *   [Windows Log Streaming](https://zuul-ci.org/docs/zuul/latest/operation.html#windows-log-streaming)

        *   [Web Server](https://zuul-ci.org/docs/zuul/latest/operation.html#web-server)
            *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html#id7)

        *   [Finger Gateway](https://zuul-ci.org/docs/zuul/latest/operation.html#finger-gateway)
            *   [Operation](https://zuul-ci.org/docs/zuul/latest/operation.html#id8)

    *   [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html)
        *   [Important Security Considerations](https://zuul-ci.org/docs/zuul/latest/authentication.html#important-security-considerations)
        *   [Configuration](https://zuul-ci.org/docs/zuul/latest/authentication.html#configuration)
        *   [JWT Format](https://zuul-ci.org/docs/zuul/latest/authentication.html#jwt-format)
        *   [Manually Generating a JWT](https://zuul-ci.org/docs/zuul/latest/authentication.html#manually-generating-a-jwt)
        *   [Debugging](https://zuul-ci.org/docs/zuul/latest/authentication.html#debugging)
        *   [Interfacing with Other Systems](https://zuul-ci.org/docs/zuul/latest/authentication.html#interfacing-with-other-systems)
            *   [Configuring Google Authentication](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html)
                *   [Prerequisites](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html#prerequisites)
                *   [Setting up credentials with Google](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html#setting-up-credentials-with-google)
                    *   [Create OAuth client ID](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html#create-oauth-client-id)
                    *   [Configure Zuul](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html#configure-zuul)

                *   [Further Reading](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-google.html#further-reading)

            *   [Configuring Keycloak Authentication](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html)
                *   [Prerequisites](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#prerequisites)
                *   [Setting up Keycloak](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#setting-up-keycloak)
                    *   [Create a client](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#create-a-client)
                    *   [Create a client scope](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#create-a-client-scope)
                    *   [(Optional) Set up a social identity provider](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#optional-set-up-a-social-identity-provider)

                *   [Setting up Zuul](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#setting-up-zuul)
                *   [Further Reading](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-keycloak.html#further-reading)

            *   [Configuring Microsoft Authentication](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-microsoft.html)
                *   [Prerequisites](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-microsoft.html#prerequisites)
                *   [Creating the App Registration](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-microsoft.html#creating-the-app-registration)
                    *   [Optional: Include Groups Claim](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-microsoft.html#optional-include-groups-claim)

                *   [Setting up Zuul](https://zuul-ci.org/docs/zuul/latest/howtos/openid-with-microsoft.html#setting-up-zuul)

            *   [Keycloak Tutorial](https://zuul-ci.org/docs/zuul/latest/tutorials/keycloak.html)
                *   [Update /etc/hosts](https://zuul-ci.org/docs/zuul/latest/tutorials/keycloak.html#update-etc-hosts)
                *   [Restart Zuul Containers](https://zuul-ci.org/docs/zuul/latest/tutorials/keycloak.html#restart-zuul-containers)
                *   [Start Keycloak](https://zuul-ci.org/docs/zuul/latest/tutorials/keycloak.html#start-keycloak)
                *   [Log Into Zuul](https://zuul-ci.org/docs/zuul/latest/tutorials/keycloak.html#log-into-zuul)

    *   [Monitoring](https://zuul-ci.org/docs/zuul/latest/monitoring.html)
        *   [Statsd reporting](https://zuul-ci.org/docs/zuul/latest/monitoring.html#statsd-reporting)
            *   [Configuration](https://zuul-ci.org/docs/zuul/latest/monitoring.html#configuration)
            *   [Metrics](https://zuul-ci.org/docs/zuul/latest/monitoring.html#metrics)

        *   [Prometheus monitoring](https://zuul-ci.org/docs/zuul/latest/monitoring.html#prometheus-monitoring)
            *   [Configuration](https://zuul-ci.org/docs/zuul/latest/monitoring.html#id1)
            *   [Metrics](https://zuul-ci.org/docs/zuul/latest/monitoring.html#id2)
            *   [Liveness Probes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#liveness-probes)

    *   [Tracing](https://zuul-ci.org/docs/zuul/latest/tracing.html)
        *   [Configuration](https://zuul-ci.org/docs/zuul/latest/tracing.html#configuration)
        *   [Tutorial](https://zuul-ci.org/docs/zuul/latest/tracing.html#tutorial)
            *   [Jaeger Tracing Tutorial](https://zuul-ci.org/docs/zuul/latest/tutorials/tracing.html)
                *   [Restart Zuul Containers](https://zuul-ci.org/docs/zuul/latest/tutorials/tracing.html#restart-zuul-containers)
                *   [Start Jaeger](https://zuul-ci.org/docs/zuul/latest/tutorials/tracing.html#start-jaeger)
                *   [Recheck a change](https://zuul-ci.org/docs/zuul/latest/tutorials/tracing.html#recheck-a-change)

    *   [Zuul Admin Client](https://zuul-ci.org/docs/zuul/latest/client.html)
        *   [Configuration](https://zuul-ci.org/docs/zuul/latest/client.html#configuration)
        *   [Usage](https://zuul-ci.org/docs/zuul/latest/client.html#usage)
            *   [tenant-conf-check](https://zuul-ci.org/docs/zuul/latest/client.html#tenant-conf-check)
            *   [create-auth-token](https://zuul-ci.org/docs/zuul/latest/client.html#create-auth-token)
            *   [export-keys](https://zuul-ci.org/docs/zuul/latest/client.html#export-keys)
            *   [import-keys](https://zuul-ci.org/docs/zuul/latest/client.html#import-keys)
            *   [copy-keys](https://zuul-ci.org/docs/zuul/latest/client.html#copy-keys)
            *   [delete-keys](https://zuul-ci.org/docs/zuul/latest/client.html#delete-keys)
            *   [delete-oidc-signing-keys](https://zuul-ci.org/docs/zuul/latest/client.html#delete-oidc-signing-keys)
            *   [delete-state](https://zuul-ci.org/docs/zuul/latest/client.html#delete-state)
            *   [delete-pipeline-state](https://zuul-ci.org/docs/zuul/latest/client.html#delete-pipeline-state)
            *   [prune-database](https://zuul-ci.org/docs/zuul/latest/client.html#prune-database)

        *   [Deprecated commands](https://zuul-ci.org/docs/zuul/latest/client.html#deprecated-commands)
            *   [Autohold](https://zuul-ci.org/docs/zuul/latest/client.html#autohold)
            *   [Autohold Delete](https://zuul-ci.org/docs/zuul/latest/client.html#autohold-delete)
            *   [Autohold Info](https://zuul-ci.org/docs/zuul/latest/client.html#autohold-info)
            *   [Autohold List](https://zuul-ci.org/docs/zuul/latest/client.html#autohold-list)
            *   [Dequeue](https://zuul-ci.org/docs/zuul/latest/client.html#dequeue)
            *   [Enqueue](https://zuul-ci.org/docs/zuul/latest/client.html#enqueue)
            *   [Enqueue-ref](https://zuul-ci.org/docs/zuul/latest/client.html#enqueue-ref)
                *   [Manual enqueue examples](https://zuul-ci.org/docs/zuul/latest/client.html#manual-enqueue-examples)

            *   [Promote](https://zuul-ci.org/docs/zuul/latest/client.html#promote)

    *   [Troubleshooting](https://zuul-ci.org/docs/zuul/latest/troubleshooting.html)
        *   [Thread Dumps and Profiling](https://zuul-ci.org/docs/zuul/latest/troubleshooting.html#thread-dumps-and-profiling)

*   [REST API](https://zuul-ci.org/docs/zuul/latest/rest-api.html)
*   [How-To Guides](https://zuul-ci.org/docs/zuul/latest/howtos/index.html)
    *   [Project Testing Interface](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html)
        *   [Projects layout](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#projects-layout)
            *   [org-config](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#org-config)
            *   [org-jobs](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#org-jobs)

        *   [Projects content](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#projects-content)
        *   [Usage](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#usage)
            *   [Project tests](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#project-tests)
            *   [Updating PTI test](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#updating-pti-test)

        *   [Cross project gating](https://zuul-ci.org/docs/zuul/latest/howtos/pti.html#cross-project-gating)

    *   [Badges](https://zuul-ci.org/docs/zuul/latest/howtos/badges.html)
    *   [Chatting with Matrix](https://zuul-ci.org/docs/zuul/latest/howtos/matrix.html)
        *   [Why Use Matrix?](https://zuul-ci.org/docs/zuul/latest/howtos/matrix.html#why-use-matrix)
        *   [Create An Account](https://zuul-ci.org/docs/zuul/latest/howtos/matrix.html#create-an-account)
        *   [Join the #zuul Room](https://zuul-ci.org/docs/zuul/latest/howtos/matrix.html#join-the-zuul-room)
        *   [Optional Next Steps](https://zuul-ci.org/docs/zuul/latest/howtos/matrix.html#optional-next-steps)
            *   [Optional: Save Encryption Keys](https://zuul-ci.org/docs/zuul/latest/howtos/matrix-encryption.html)
            *   [Optional: Register with an Identity Provider](https://zuul-ci.org/docs/zuul/latest/howtos/matrix-id.html)
            *   [Optional: Join an IRC Room](https://zuul-ci.org/docs/zuul/latest/howtos/matrix-irc.html)

    *   [ZooKeeper Administration](https://zuul-ci.org/docs/zuul/latest/howtos/zookeeper.html)
        *   [Configuration](https://zuul-ci.org/docs/zuul/latest/howtos/zookeeper.html#configuration)
        *   [Encrypted Connections](https://zuul-ci.org/docs/zuul/latest/howtos/zookeeper.html#encrypted-connections)

*   [Developer’s Guide](https://zuul-ci.org/docs/zuul/latest/developer/index.html)
    *   [`Scheduler`](https://zuul-ci.org/docs/zuul/latest/developer/index.html#zuul.scheduler.Scheduler)
    *   [Data Model](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html)
        *   [`Pipeline`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Pipeline)
        *   [`PipelineManager`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.manager.PipelineManager)
        *   [`DependentPipelineManager`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.manager.dependent.DependentPipelineManager)
        *   [`IndependentPipelineManager`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.manager.independent.IndependentPipelineManager)
        *   [`ChangeQueue`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.ChangeQueue)
        *   [`Job`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Job)
        *   [`JobGraph`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.JobGraph)
        *   [`Build`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Build)
        *   [`QueueItem`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.QueueItem)
        *   [`BuildSet`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.BuildSet)
        *   [Changes](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#changes)
            *   [`Change`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Change)
            *   [`Ref`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Ref)

        *   [Filters](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#filters)
            *   [`RefFilter`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.RefFilter)
            *   [`EventFilter`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.EventFilter)

        *   [Tenants](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#tenants)
            *   [`Tenant`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Tenant)
            *   [`UnparsedAbideConfig`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.UnparsedAbideConfig)
            *   [`UnparsedConfig`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.UnparsedConfig)
            *   [`ParsedConfig`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.ParsedConfig)

        *   [Other Global Objects](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#other-global-objects)
            *   [`Project`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Project)
            *   [`Layout`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.Layout)
            *   [`RepoFiles`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.RepoFiles)
            *   [`TriggerEvent`](https://zuul-ci.org/docs/zuul/latest/developer/datamodel.html#zuul.model.TriggerEvent)

    *   [Drivers](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html)
        *   [`Driver`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.Driver)
            *   [`Driver.reconfigure()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.Driver.reconfigure)
            *   [`Driver.registerScheduler()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.Driver.registerScheduler)
            *   [`Driver.stop()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.Driver.stop)

        *   [`ConnectionInterface`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.ConnectionInterface)
            *   [`ConnectionInterface.getConnection()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.ConnectionInterface.getConnection)

        *   [`SourceInterface`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.SourceInterface)
            *   [`SourceInterface.getRejectSchema()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.SourceInterface.getRejectSchema)
            *   [`SourceInterface.getRequireSchema()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.SourceInterface.getRequireSchema)
            *   [`SourceInterface.getSource()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.SourceInterface.getSource)

        *   [`TriggerInterface`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.TriggerInterface)
            *   [`TriggerInterface.getTrigger()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.TriggerInterface.getTrigger)
            *   [`TriggerInterface.getTriggerEventClass()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.TriggerInterface.getTriggerEventClass)
            *   [`TriggerInterface.getTriggerSchema()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.TriggerInterface.getTriggerSchema)

        *   [`ReporterInterface`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.ReporterInterface)
            *   [`ReporterInterface.getReporter()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.ReporterInterface.getReporter)
            *   [`ReporterInterface.getReporterSchema()`](https://zuul-ci.org/docs/zuul/latest/developer/drivers.html#zuul.driver.ReporterInterface.getReporterSchema)

    *   [Triggers](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html)
        *   [`BaseTrigger`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.trigger.BaseTrigger)
            *   [`BaseTrigger.getEventFilters()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.trigger.BaseTrigger.getEventFilters)
            *   [`BaseTrigger.onChangeEnqueued()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.trigger.BaseTrigger.onChangeEnqueued)
            *   [`BaseTrigger.onChangeMerged()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.trigger.BaseTrigger.onChangeMerged)
            *   [`BaseTrigger.postConfig()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.trigger.BaseTrigger.postConfig)

        *   [`GerritTrigger`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.gerrit.gerrittrigger.GerritTrigger)
            *   [`GerritTrigger.getEventFilters()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.gerrit.gerrittrigger.GerritTrigger.getEventFilters)

        *   [`TimerTrigger`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.timer.timertrigger.TimerTrigger)
            *   [`TimerTrigger.getEventFilters()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.timer.timertrigger.TimerTrigger.getEventFilters)

        *   [`ZuulTrigger`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.zuul.zuultrigger.ZuulTrigger)
            *   [`ZuulTrigger.getEventFilters()`](https://zuul-ci.org/docs/zuul/latest/developer/triggers.html#zuul.driver.zuul.zuultrigger.ZuulTrigger.getEventFilters)

    *   [Testing](https://zuul-ci.org/docs/zuul/latest/developer/testing.html)
        *   [`simple_layout()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.simple_layout)
        *   [`ZuulTestCase`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase)
            *   [`ZuulTestCase.addEvent()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.addEvent)
            *   [`ZuulTestCase.assertBuilds()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.assertBuilds)
            *   [`ZuulTestCase.assertHistory()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.assertHistory)
            *   [`ZuulTestCase.assertReportedStat()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.assertReportedStat)
            *   [`ZuulTestCase.commitConfigUpdate()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.commitConfigUpdate)
            *   [`ZuulTestCase.getSortedBuilds()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.getSortedBuilds)
            *   [`ZuulTestCase.getUpstreamRepos()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.getUpstreamRepos)
            *   [`ZuulTestCase.logState()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.logState)
            *   [`ZuulTestCase.newTenantConfig()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.newTenantConfig)
            *   [`ZuulTestCase.printHistory()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.printHistory)
            *   [`ZuulTestCase.setUp()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.setUp)
            *   [`ZuulTestCase.waitUntilNodeCacheSync()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.ZuulTestCase.waitUntilNodeCacheSync)

        *   [`FakeGerritConnection`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection)
            *   [`FakeGerritConnection.addFakeChange()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.addFakeChange)
            *   [`FakeGerritConnection.checkBranchCache()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.checkBranchCache)
            *   [`FakeGerritConnection.cleanupCache()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.cleanupCache)
            *   [`FakeGerritConnection.clearBranchCache()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.clearBranchCache)
            *   [`FakeGerritConnection.clearConnectionCacheOnBranchEvent()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.clearConnectionCacheOnBranchEvent)
            *   [`FakeGerritConnection.getEventQueue()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.getEventQueue)
            *   [`FakeGerritConnection.getProjectBranches()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.getProjectBranches)
            *   [`FakeGerritConnection.getProjectDefaultBranch()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.getProjectDefaultBranch)
            *   [`FakeGerritConnection.getProjectMergeModes()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.getProjectMergeModes)
            *   [`FakeGerritConnection.getWebController()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.getWebController)
            *   [`FakeGerritConnection.isBranchProtected()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.isBranchProtected)
            *   [`FakeGerritConnection.maintainCache()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.maintainCache)
            *   [`FakeGerritConnection.toDict()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.toDict)
            *   [`FakeGerritConnection.updateProjectBranches()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.updateProjectBranches)
            *   [`FakeGerritConnection.validateWebConfig()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.fakegerrit.FakeGerritConnection.validateWebConfig)

        *   [`RecordingExecutorServer`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.RecordingExecutorServer)
            *   [`RecordingExecutorServer.failJob()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.RecordingExecutorServer.failJob)
            *   [`RecordingExecutorServer.release()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.RecordingExecutorServer.release)
            *   [`RecordingExecutorServer.retryJob()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.RecordingExecutorServer.retryJob)
            *   [`RecordingExecutorServer.returnData()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.RecordingExecutorServer.returnData)

        *   [`FakeBuild`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.FakeBuild)
            *   [`FakeBuild.getWorkspaceRepos()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.FakeBuild.getWorkspaceRepos)
            *   [`FakeBuild.hasChanges()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.FakeBuild.hasChanges)
            *   [`FakeBuild.isWaiting()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.FakeBuild.isWaiting)
            *   [`FakeBuild.release()`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.FakeBuild.release)

        *   [`BuildHistory`](https://zuul-ci.org/docs/zuul/latest/developer/testing.html#tests.base.BuildHistory)

    *   [Metrics](https://zuul-ci.org/docs/zuul/latest/developer/metrics.html)
        *   [Event Overview](https://zuul-ci.org/docs/zuul/latest/developer/metrics.html#event-overview)

    *   [Documentation](https://zuul-ci.org/docs/zuul/latest/developer/docs.html)
        *   [ReStructuredText Conventions](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#restructuredtext-conventions)
            *   [Code Blocks](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#code-blocks)
            *   [Literal Values](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#literal-values)
            *   [Terminology](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#terminology)

        *   [Zuul Sphinx Directives](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#zuul-sphinx-directives)
            *   [zuul:attr::](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#zuul-attr)
            *   [zuul:value::](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#zuul-value)
            *   [zuul:var::](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#zuul-var)

        *   [Zuul Sphinx Roles](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#zuul-sphinx-roles)
            *   [:zuul:attr:](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#id1)
            *   [:zuul:value:](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#id2)
            *   [:zuul:var:](https://zuul-ci.org/docs/zuul/latest/developer/docs.html#id3)

    *   [Ansible Integration](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html)
        *   [Streaming job output](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#streaming-job-output)
            *   [`CallbackModule`](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#zuul.ansible.base.callback.zuul_stream.CallbackModule)
            *   [`LogStreamer`](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#zuul.lib.log_streamer.LogStreamer)
            *   [`LogStreamHandler`](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#zuul.web.LogStreamHandler)
            *   [`ZuulWeb`](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#zuul.web.ZuulWeb)
            *   [`CallbackModule`](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#zuul.ansible.base.callback.zuul_json.CallbackModule)

        *   [Capturing live command output](https://zuul-ci.org/docs/zuul/latest/developer/ansible.html#capturing-live-command-output)

    *   [Zuul Dashboard Javascript](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html)
        *   [For the impatient who don’t want deal with javascript toolchains](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#for-the-impatient-who-don-t-want-deal-with-javascript-toolchains)
        *   [yarn dependency management](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#yarn-dependency-management)
        *   [Dealing with yarn.lock merge conflicts](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#dealing-with-yarn-lock-merge-conflicts)
        *   [React Components and Styling](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#react-components-and-styling)
        *   [Development](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#development)
            *   [Authentication](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#authentication)

        *   [Deploying](https://zuul-ci.org/docs/zuul/latest/developer/javascript.html#deploying)

    *   [Specifications](https://zuul-ci.org/docs/zuul/latest/developer/specs/index.html)
        *   [Nodepool in Zuul](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html)
            *   [Introduction](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#introduction)
            *   [Image Management](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#image-management)
                *   [Snapshot Images](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#snapshot-images)

            *   [Node Management](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#node-management)
                *   [Quota Handling & Rate Limiting](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#quota-handling-rate-limiting)

            *   [Configuration](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#configuration)
            *   [Upgrade Process](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#upgrade-process)
            *   [Library Requirements](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#library-requirements)
            *   [Diskimage-Builder Testing](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#diskimage-builder-testing)
            *   [Work Items](https://zuul-ci.org/docs/zuul/latest/developer/specs/nodepool-in-zuul.html#work-items)

        *   [Initializer Jobs](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html)
            *   [Introduction](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#introduction)
            *   [Proposal](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#proposal)
            *   [Implementation](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#implementation)
            *   [User Interface](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#user-interface)
            *   [Other Types of Jobs](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#other-types-of-jobs)
            *   [Alternatives](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#alternatives)
            *   [Work Items](https://zuul-ci.org/docs/zuul/latest/developer/specs/init-jobs.html#work-items)

        *   [Reporter Jobs](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html)
            *   [Introduction](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#introduction)
            *   [Proposal](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#proposal)
            *   [Implementation](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#implementation)
            *   [User Interface](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#user-interface)
            *   [Limitations](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#limitations)
            *   [Alternatives](https://zuul-ci.org/docs/zuul/latest/developer/specs/reporter-jobs.html#alternatives)

        *   [Branch-Assigned Queues](https://zuul-ci.org/docs/zuul/latest/developer/specs/branch-assigned-queues.html)
            *   [Introduction](https://zuul-ci.org/docs/zuul/latest/developer/specs/branch-assigned-queues.html#introduction)
            *   [Proposal](https://zuul-ci.org/docs/zuul/latest/developer/specs/branch-assigned-queues.html#proposal)
            *   [User Interface](https://zuul-ci.org/docs/zuul/latest/developer/specs/branch-assigned-queues.html#user-interface)

        *   [Fine-Grained API/Web Access Control](https://zuul-ci.org/docs/zuul/latest/developer/specs/web-rbac.html)
            *   [Introduction](https://zuul-ci.org/docs/zuul/latest/developer/specs/web-rbac.html#introduction)
            *   [Proposal](https://zuul-ci.org/docs/zuul/latest/developer/specs/web-rbac.html#proposal)
            *   [Alternatives](https://zuul-ci.org/docs/zuul/latest/developer/specs/web-rbac.html#alternatives)

    *   [ZooKeeper](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html)
        *   [Overview](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#overview)
        *   [Driver Event Ingestion](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#driver-event-ingestion)
            *   [Active Event Gathering](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#active-event-gathering)
            *   [Passive Event Gathering](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#passive-event-gathering)

        *   [Configuration Storage](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#configuration-storage)
        *   [Executor and Merger Queues](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#executor-and-merger-queues)
        *   [Zookeeper Map](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#zookeeper-map)

    *   [Data Model Changelog](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html)
        *   [Version 0](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-0)
        *   [Version 1](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-1)
        *   [Version 2](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-2)
        *   [Version 3](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-3)
        *   [Version 4](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-4)
        *   [Version 5](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-5)
        *   [Version 6](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-6)
        *   [Version 7](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-7)
        *   [Version 8](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-8)
        *   [Version 9](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-9)
        *   [Version 10](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-10)
        *   [Version 11](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-11)
        *   [Version 12](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-12)
        *   [Version 13](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-13)
        *   [Version 14](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-14)
        *   [Version 15](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-15)
        *   [Version 16](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-16)
        *   [Version 17](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-17)
        *   [Version 18](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-18)
        *   [Version 19](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-19)
        *   [Version 20](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-20)
        *   [Version 21](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-21)
        *   [Version 22](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-22)
        *   [Version 23](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-23)
        *   [Version 24](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-24)
        *   [Version 25](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-25)
        *   [Version 26](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-26)
        *   [Version 27](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-27)
        *   [Version 28](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-28)
        *   [Version 29](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-29)
        *   [Version 30](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-30)
        *   [Version 31](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-31)
        *   [Version 32](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-32)
        *   [Version 33](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-33)
        *   [Version 34](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-34)
        *   [Version 35](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-35)
        *   [Version 36](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html#version-36)

    *   [Release Notes](https://zuul-ci.org/docs/zuul/latest/developer/releasenotes.html)
        *   [Installing reno](https://zuul-ci.org/docs/zuul/latest/developer/releasenotes.html#installing-reno)
        *   [Adding a new release note](https://zuul-ci.org/docs/zuul/latest/developer/releasenotes.html#adding-a-new-release-note)

*   [Zuul Project Governance](https://zuul-ci.org/docs/zuul/latest/governance.html)
    *   [Zuul Maintainers](https://zuul-ci.org/docs/zuul/latest/governance.html#zuul-maintainers)
    *   [Zuul Project Lead](https://zuul-ci.org/docs/zuul/latest/governance.html#zuul-project-lead)
    *   [Zuul-Jobs Maintainers](https://zuul-ci.org/docs/zuul/latest/governance.html#zuul-jobs-maintainers)

*   [Vulnerability Reporting](https://zuul-ci.org/docs/zuul/latest/vulnerabilities.html)
    *   [Create a Private Story in StoryBoard](https://zuul-ci.org/docs/zuul/latest/vulnerabilities.html#create-a-private-story-in-storyboard)
    *   [Report via Encrypted E-mail](https://zuul-ci.org/docs/zuul/latest/vulnerabilities.html#report-via-encrypted-e-mail)

*   [Release Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html)
    *   [In Development](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#in-development)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#deprecation-notes)

    *   [14.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0-deprecation-notes)

    *   [13.1.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-1)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#security-issues)

    *   [13.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#bug-fixes)

    *   [13.0.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1-bug-fixes)

    *   [13.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0-upgrade-notes)

    *   [12.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-1-0-new-features)

    *   [12.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-bug-fixes)

    *   [11.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0-upgrade-notes)

    *   [11.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0-upgrade-notes)

    *   [11.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-bug-fixes)

    *   [11.0.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-1-bug-fixes)

    *   [11.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-deprecation-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-security-issues)

    *   [10.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-bug-fixes)
        *   [Other Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#other-notes)

    *   [10.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-bug-fixes)

    *   [10.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0)
        *   [Prelude](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#prelude)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-deprecation-notes)

    *   [9.5.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-5-0)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-5-0-upgrade-notes)

    *   [9.4.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0-new-features)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0-bug-fixes)

    *   [9.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-bug-fixes)

    *   [9.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-deprecation-notes)

    *   [9.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-bug-fixes)

    *   [9.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-bug-fixes)

    *   [8.3.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-1)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-1-security-issues)

    *   [8.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-bug-fixes)

    *   [8.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-deprecation-notes)

    *   [8.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-security-issues)

    *   [8.0.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-1-bug-fixes)

    *   [8.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-bug-fixes)

    *   [7.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0-upgrade-notes)

    *   [7.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0-upgrade-notes)

    *   [6.4.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0-upgrade-notes)

    *   [6.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-3-0-new-features)

    *   [6.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0-new-features)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0-bug-fixes)

    *   [6.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-deprecation-notes)

    *   [6.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-bug-fixes)

    *   [5.2.5](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-5)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-5-bug-fixes)

    *   [5.2.4](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-4)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-4-bug-fixes)

    *   [5.2.3](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-3)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-3-bug-fixes)

    *   [5.2.2](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-2)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-2-bug-fixes)

    *   [5.2.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-bug-fixes)

    *   [5.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-security-issues)

    *   [5.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-bug-fixes)

    *   [5.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-0-0)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-0-0-upgrade-notes)

    *   [4.12.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-12-0)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-12-0-upgrade-notes)

    *   [4.11.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0-upgrade-notes)

    *   [4.10.4](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-4)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-4-bug-fixes)

    *   [4.10.3](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-3)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-3-bug-fixes)

    *   [4.10.2](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-2)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-2-bug-fixes)

    *   [4.10.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1-new-features)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1-bug-fixes)

    *   [4.10.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-0)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-0-upgrade-notes)

    *   [4.9.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0-upgrade-notes)

    *   [4.8.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1-bug-fixes)

    *   [4.8.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-0-new-features)

    *   [4.7.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-deprecation-notes)

    *   [4.6.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0-new-features)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0-security-issues)

    *   [4.5.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-1-bug-fixes)

    *   [4.5.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-0)
        *   [Prelude](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-0-prelude)

    *   [4.4.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0-deprecation-notes)

    *   [4.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-bug-fixes)

    *   [4.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-2-0)
        *   [Prelude](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-2-0-prelude)

    *   [4.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-bug-fixes)

    *   [4.0.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0)
        *   [Prelude](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-prelude)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-bug-fixes)

    *   [3.19.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1-bug-fixes)

    *   [3.19.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0)
        *   [Prelude](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-prelude)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-bug-fixes)

    *   [3.18.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-deprecation-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-bug-fixes)

    *   [3.17.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0-new-features)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0-security-issues)

    *   [3.16.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-1-bug-fixes)

    *   [3.16.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-deprecation-notes)

    *   [3.15.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-15-0)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-15-0-bug-fixes)

    *   [3.14.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0-upgrade-notes)

    *   [3.13.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0-upgrade-notes)

    *   [3.12.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-upgrade-notes)
        *   [Other Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-other-notes)

    *   [3.11.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-1-bug-fixes)

    *   [3.11.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0-upgrade-notes)

    *   [3.10.2](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-new-features)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-bug-fixes)

    *   [3.10.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-1-bug-fixes)

    *   [3.10.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0-upgrade-notes)

    *   [3.9.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-9-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-9-0-new-features)

    *   [3.8.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-1-bug-fixes)

    *   [3.8.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-new-features)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-bug-fixes)

    *   [3.7.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-1)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-1-bug-fixes)

    *   [3.7.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0-upgrade-notes)

    *   [3.6.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-1)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-1-security-issues)

    *   [3.6.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0-upgrade-notes)

    *   [3.5.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-bug-fixes)

    *   [3.4.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0-upgrade-notes)

    *   [3.3.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-bug-fixes)

    *   [3.3.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-upgrade-notes)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-deprecation-notes)

    *   [3.2.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0-new-features)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0-bug-fixes)

    *   [3.1.0](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-upgrade-notes)
        *   [Security Issues](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-security-issues)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-bug-fixes)

    *   [3.0.3](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-new-features)
        *   [Deprecation Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-deprecation-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-bug-fixes)

    *   [3.0.2](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-bug-fixes)

    *   [3.0.1](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1)
        *   [New Features](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-new-features)
        *   [Upgrade Notes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-upgrade-notes)
        *   [Bug Fixes](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-bug-fixes)

*   [Glossary](https://zuul-ci.org/docs/zuul/latest/glossary.html)

[Zuul](https://zuul-ci.org/docs/zuul/latest/index.html)

*   [](https://zuul-ci.org/docs/zuul/latest/index.html)
*   [Service Administration](https://zuul-ci.org/docs/zuul/latest/admin.html)
*   Configuration
*   [View page source](https://zuul-ci.org/docs/zuul/latest/_sources/configuration.rst.txt)

* * *

Configuration[](https://zuul-ci.org/docs/zuul/latest/configuration.html#configuration "Link to this heading")
==============================================================================================================

All Zuul processes read the `/etc/zuul/zuul.conf` file (an alternate location may be supplied on the command line) which uses an INI file syntax. Each component may have its own configuration file, though you may find it simpler to use the same file for all components.

Zuul will interpolate environment variables starting with the `ZUUL_` prefix given in the config file escaped as python string expansion. `foo=%(ZUUL_HOME)s` will set the value of `foo` to the same value as the environment variable named `ZUUL_HOME`.

An example `zuul.conf`:

[zookeeper]
hosts=zk1.example.com,zk2.example.com,zk3.example.com

[database]
dburi=<URI>

[keystore]
password=MY_SECRET_PASSWORD

[web]
root=https://zuul.example.com/

[scheduler]
log_config=/etc/zuul/scheduler-logging.yaml

Common Options[](https://zuul-ci.org/docs/zuul/latest/configuration.html#common-options "Link to this heading")
----------------------------------------------------------------------------------------------------------------

The following sections of `zuul.conf` are used by all Zuul components:

### Statsd[](https://zuul-ci.org/docs/zuul/latest/configuration.html#statsd "Link to this heading")

statsd[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-statsd "Link to this definition")

Information about the optional statsd server. If the `statsd` python module is installed and this section is configured, statistics will be reported to statsd. See [Statsd reporting](https://zuul-ci.org/docs/zuul/latest/monitoring.html#statsd) for more information.

statsd.server[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-statsd.server "Link to this definition")

Hostname or IP address of the statsd server.

statsd.port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-statsd.port "Link to this definition")

Default:`8125`

The UDP port on which the statsd server is listening.

statsd.prefix[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-statsd.prefix "Link to this definition")

If present, this will be prefixed to all of the keys before transmitting to the statsd server.

### Tracing[](https://zuul-ci.org/docs/zuul/latest/configuration.html#tracing "Link to this heading")

tracing[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing "Link to this definition")

Information about the optional OpenTelemetry tracing configuration. See [Tracing](https://zuul-ci.org/docs/zuul/latest/tracing.html#tracing) for more information.

tracing.enabled(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.enabled "Link to this definition")

To enable tracing, set this value to `true`. This is the only required parameter in order to export to a collector running locally.

tracing.protocol[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.protocol "Link to this definition")

Default:`grpc`

The OTLP wire protocol to use.

grpc[](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.grpc "Link to this definition")
Use gRPC (the default).

http/protobuf[](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.http/protobuf "Link to this definition")
Use HTTP with protobuf encoding.

tracing.endpoint[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.endpoint "Link to this definition")

The endpoint to use. The default is protocol specific, but defaults to localhost in all cases.

tracing.service_name[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.service_name "Link to this definition")

Default:`zuul`

The service name may be specified here. Multiple Zuul installations should use different values.

tracing.tls_cert[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.tls_cert "Link to this definition")

The path to the PEM encoded certificate file. Used only by [grpc](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.grpc "value-tracing.protocol.grpc").

tracing.tls_key[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.tls_key "Link to this definition")

The path to the PEM encoded key file. Used only by [grpc](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.grpc "value-tracing.protocol.grpc").

tracing.tls_ca[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.tls_ca "Link to this definition")

The path to the PEM encoded CA certificate file. Used only by [grpc](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.grpc "value-tracing.protocol.grpc").

tracing.certificate_file[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.certificate_file "Link to this definition")

The path to the PEM encoded certificate file used to verify the endpoint. Used only by [http/protobuf](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.http/protobuf "value-tracing.protocol.http/protobuf").

tracing.insecure[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.insecure "Link to this definition")

Whether to allow an insecure connection. Used only by [grpc](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-tracing.protocol.grpc "value-tracing.protocol.grpc").

tracing.timeout[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.timeout "Link to this definition")

Default:`10000`

The timeout for outgoing data in milliseconds.

tracing.compression[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-tracing.compression "Link to this definition")

The compression algorithm to use. Available values depend on the protocol and endpoint. The only universally supported value is `gzip`.

### ZooKeeper[](https://zuul-ci.org/docs/zuul/latest/configuration.html#zookeeper "Link to this heading")

zookeeper[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper "Link to this definition")

Client connection information for ZooKeeper. TLS is required.

zookeeper.hosts(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper.hosts "Link to this definition")

A list of zookeeper hosts for Zuul to use.

zookeeper.tls_cert(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper.tls_cert "Link to this definition")

The path to the PEM encoded certificate file.

zookeeper.tls_key(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper.tls_key "Link to this definition")

The path to the PEM encoded key file.

zookeeper.tls_ca(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper.tls_ca "Link to this definition")

The path to the PEM encoded CA certificate file.

zookeeper.session_timeout[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper.session_timeout "Link to this definition")

Default:`10.0`

The ZooKeeper session timeout, in seconds.

### Database[](https://zuul-ci.org/docs/zuul/latest/configuration.html#database "Link to this heading")

database[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-database "Link to this definition")

database.dburi(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-database.dburi "Link to this definition")

Database connection information in the form of a URI understood by SQLAlchemy. See [The SQLAlchemy manual](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls) for more information.

Zuul supports PostgreSQL, MySQL, and MariaDB. Supported SQLAlchemy dialects and drivers are: `postgresql://`, `mysql+pymysql://`, and `mariadb+pymysql`.

If using MariaDB, be sure to use the `mariadb` dialect.

The driver will automatically set up the database creating and managing the necessary tables. Therefore the provided user should have sufficient permissions to manage the database. For example:

GRANT ALL ON my_database TO 'my_user'@'%';

database.pool_recycle[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-database.pool_recycle "Link to this definition")

Default:`1`

Tune the pool_recycle value. See [The SQLAlchemy manual on pooling](http://docs.sqlalchemy.org/en/latest/core/pooling.html#setting-pool-recycle) for more information.

database.table_prefix[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-database.table_prefix "Link to this definition")

Default:`''`

The string to prefix the table names. This makes it possible to run several zuul deployments against the same database. This can be useful if you rely on external databases which are not under your control. The default is to have no prefix.

### OIDC[](https://zuul-ci.org/docs/zuul/latest/configuration.html#oidc "Link to this heading")

oidc[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-oidc "Link to this definition")

This optional section of `zuul.conf`, if present, can be used to customize the configuration of Zuul as an OpenId Connect (OIDC) Identity Provider.

oidc.supported_signing_algorithms[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-oidc.supported_signing_algorithms "Link to this definition")

Default:`RS256`

Algorithms that should be supported for signing the OIDC tokens, a string of algorithm names separated by `,`. Currently `RS256` is supported.

oidc.default_signing_algorithm[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-oidc.default_signing_algorithm "Link to this definition")

Default:`RS256`

The default algorithm used for signing the OIDC tokens if not specified in secret configuration.

oidc.signing_key_rotation_interval[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-oidc.signing_key_rotation_interval "Link to this definition")

Default:`604800`

The rotation interval of the signing key, in seconds.

Scheduler[](https://zuul-ci.org/docs/zuul/latest/configuration.html#scheduler "Link to this heading")
------------------------------------------------------------------------------------------------------

The scheduler is the primary component of Zuul. The scheduler is a scalable component; one or more schedulers must be running at all times for Zuul to be operational. It receives events from any connections to remote systems which have been configured, enqueues items into pipelines, distributes jobs to executors, and reports results.

The scheduler must be able to connect to the ZooKeeper cluster. It must also be able to connect to any services for which connections are configured (Gerrit, GitHub, etc).

The following sections of `zuul.conf` are used by the scheduler:

web[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web "Link to this definition")

web.root(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.root "Link to this definition")

The root URL of the web service (e.g., `https://zuul.example.com/`).

See [tenant.web-root](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.web-root "attr-tenant.web-root") for additional options for whitelabeled tenant configuration.

keystore[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keystore "Link to this definition")

keystore.password(required)[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keystore.password "Link to this definition")

Encryption password for private data stored in Zookeeper.

scheduler[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler "Link to this definition")

scheduler.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.command_socket "Link to this definition")

Default:`/var/lib/zuul/scheduler.socket`

Path to command socket file for the scheduler process.

scheduler.tenant_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config "Link to this definition")

Path to [Tenant Configuration](https://zuul-ci.org/docs/zuul/latest/tenants.html#tenant-config) file. This attribute is exclusive with [scheduler.tenant_config_script](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config_script "attr-scheduler.tenant_config_script").

scheduler.tenant_config_script[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config_script "Link to this definition")

Path to a script to execute and load the tenant config from. This attribute is exclusive with [scheduler.tenant_config](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config "attr-scheduler.tenant_config").

scheduler.default_ansible_version[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.default_ansible_version "Link to this definition")

Default ansible version to use for jobs that doesn’t specify a version. See [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version") for details.

scheduler.log_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.log_config "Link to this definition")

Path to log config file.

scheduler.pidfile[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.pidfile "Link to this definition")

Default:`/var/run/zuul/scheduler.pid`

Path to PID lock file.

scheduler.relative_priority[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.relative_priority "Link to this definition")

Default:`False`

A boolean which indicates whether the scheduler should supply relative priority information for node requests.

In all cases, each pipeline may specify a precedence value which is used to satisfy requests from higher-precedence pipelines first. If `relative_priority` is set to `True`, then Zuul will additionally group items in the same pipeline by pipeline queue and weight each request by its position in that project’s group. A request for the first change in a given queue will have the highest relative priority, and the second change a lower relative priority. The first change of each queue in a pipeline has the same relative priority, regardless of the order of submission or how many other changes are in the pipeline. This can be used to make node allocations complete faster for projects with fewer changes in a system dominated by projects with more changes.

After the first 10 changes, the relative priority becomes more coarse (batching groups of 10 changes at the same priority). Likewise, after 100 changes they are batched in groups of 100. This is to avoid causing additional load with unnecessary priority changes if queues are long.

If this value is `False` (the default), then node requests are sorted by pipeline precedence followed by the order in which they were submitted. If this is `True`, they are sorted by pipeline precedence, followed by relative priority, and finally the order in which they were submitted.

scheduler.default_hold_expiration[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.default_hold_expiration "Link to this definition")

Default:`max_hold_expiration`

The default value for held node expiration if not supplied. This will default to the value of `max_hold_expiration` if not changed, or if it is set to a higher value than the max.

scheduler.max_hold_expiration[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.max_hold_expiration "Link to this definition")

Default:`0`

Maximum number of seconds any nodes held for an autohold request will remain available. A value of 0 disables this, and the nodes will remain held until the autohold request is manually deleted. If a value higher than `max_hold_expiration` is supplied during hold request creation, it will be lowered to this value.

scheduler.prometheus_port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.prometheus_port "Link to this definition")

Set a TCP port to start the prometheus metrics client.

scheduler.prometheus_addr[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.prometheus_addr "Link to this definition")

Default:`0.0.0.0`

The IPv4 addr to listen for prometheus metrics poll. To use IPv6, python>3.8 is required [issue24209](https://bugs.python.org/issue24209).

Merger[](https://zuul-ci.org/docs/zuul/latest/configuration.html#merger "Link to this heading")
------------------------------------------------------------------------------------------------

Mergers are an optional Zuul service; they are not required for Zuul to operate, but some high volume sites may benefit from running them. Zuul performs quite a lot of git operations in the course of its work. Each change that is to be tested must be speculatively merged with the current state of its target branch to ensure that it can merge, and to ensure that the tests that Zuul perform accurately represent the outcome of merging the change. Because Zuul’s configuration is stored in the git repos it interacts with, and is dynamically evaluated, Zuul often needs to perform a speculative merge in order to determine whether it needs to perform any further actions.

All of these git operations add up, and while Zuul executors can also perform them, large numbers may impact their ability to run jobs. Therefore, administrators may wish to run standalone mergers in order to reduce the load on executors.

Mergers need to be able to connect to the ZooKeeper cluster as well as any services for which connections are configured (Gerrit, GitHub, etc).

The following section of `zuul.conf` is used by the merger:

merger[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger "Link to this definition")

merger.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.command_socket "Link to this definition")

Default:`/var/lib/zuul/merger.socket`

Path to command socket file for the merger process.

merger.git_dir[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_dir "Link to this definition")

Default:`/var/lib/zuul/merger-git`

Directory in which Zuul should clone git repositories.

merger.git_http_low_speed_limit[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_http_low_speed_limit "Link to this definition")

Default:`1000`

If the HTTP transfer speed is less then git_http_low_speed_limit for longer then git_http_low_speed_time, the transfer is aborted.

Value in bytes, setting to 0 will disable.

merger.git_http_low_speed_time[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_http_low_speed_time "Link to this definition")

Default:`30`

If the HTTP transfer speed is less then git_http_low_speed_limit for longer then git_http_low_speed_time, the transfer is aborted.

Value in seconds, setting to 0 will disable.

merger.git_timeout[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_timeout "Link to this definition")

Default:`300`

Timeout for git clone and fetch operations. This can be useful when dealing with large repos. Note that large timeouts can increase startup and reconfiguration times if repos are not cached so be cautious when increasing this value.

Value in seconds.

merger.git_user_email[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_user_email "Link to this definition")

Value to pass to [git config user.email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

merger.git_user_name[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.git_user_name "Link to this definition")

Value to pass to [git config user.name](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

merger.log_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.log_config "Link to this definition")

Path to log config file for the merger process.

merger.pidfile[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.pidfile "Link to this definition")

Default:`/var/run/zuul/merger.pid`

Path to PID lock file for the merger process.

merger.prometheus_port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.prometheus_port "Link to this definition")

Set a TCP port to start the prometheus metrics client.

merger.prometheus_addr[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-merger.prometheus_addr "Link to this definition")

Default:`0.0.0.0`

The IPv4 addr to listen for prometheus metrics poll. To use IPv6, python>3.8 is required [issue24209](https://bugs.python.org/issue24209).

Executor[](https://zuul-ci.org/docs/zuul/latest/configuration.html#executor "Link to this heading")
----------------------------------------------------------------------------------------------------

Executors are responsible for running jobs. At the start of each job, an executor prepares an environment in which to run Ansible which contains all of the git repositories specified by the job with all dependent changes merged into their appropriate branches. The branch corresponding to the proposed change will be checked out (in all projects, if it exists). Any roles specified by the job will also be present (also with dependent changes merged, if appropriate) and added to the Ansible role path. The executor also prepares an Ansible inventory file with all of the nodes requested by the job.

The executor also contains a merger. This is used by the executor to prepare the git repositories used by jobs, but is also available to perform any tasks normally performed by standalone mergers. Because the executor performs both roles, small Zuul installations may not need to run standalone mergers.

Executors need to be able to connect to the ZooKeeper cluster, any services for which connections are configured (Gerrit, GitHub, etc), as well as directly to the build nodes.

### Trusted and Untrusted Playbooks[](https://zuul-ci.org/docs/zuul/latest/configuration.html#trusted-and-untrusted-playbooks "Link to this heading")

The executor runs playbooks in one of two execution contexts depending on whether the project containing the playbook is a [config-project](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project) or an [untrusted-project](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-untrusted-project). If the playbook is in a config project, the executor runs the playbook in the _trusted_ execution context, otherwise, it is run in the _untrusted_ execution context.

Both execution contexts use [bubblewrap](https://github.com/projectatomic/bubblewrap) to create a namespace to ensure that playbook executions are isolated and are unable to access files outside of a restricted environment. The administrator may configure additional local directories on the executor to be made available to the restricted environment.

### Security Considerations[](https://zuul-ci.org/docs/zuul/latest/configuration.html#security-considerations "Link to this heading")

Bubblewrap restricts access to files outside of the build environment in both execution contexts. Operators may allow either read-only or read-write access to additional paths in either the trusted context or both contexts with additional options described below. Be careful when adding additional paths, and consider that any trusted or untrusted (as appropriate) playbook will have access to these paths.

If executors are configured to use WinRM certificates, these must be made available to the bubblewrap environment in order for Ansible to use them. This invariably makes them accessible to any playbook in that execution context. Operators may want to consider only supplying WinRM credentials to trusted playbooks and installing per-build certificates in a pre-playbook; or using Ansible’s experimental SSH support instead of WinRM.

Local code execution is permitted on the executor, so if a vulnerability in bubblewrap or the kernel allows for an escape from the restricted environment, users may be able to escalate their privileges and obtain access to any data or secrets available to the executor.

Playbooks which run on the executor will have the same network access as the executor itself. This should be kept in mind when considering IP-based network access control within an organization. Zuul’s internal communication is via ZooKeeper which is authenticated and secured by TLS certificates, so as long as these certificates are not made available to jobs, users should not be able to access or disrupt Zuul’s internal communications. However, statsd is an unauthenticated protocol, so a malicious user could emit false statsd information.

If the Zuul executor is running in a cloud environment with a network metadata service, users may be able to access that service. If it supplies credentials, they may be able to obtain those credentials and access cloud resources. Operators should ensure that in these environments, the executors are configured with appropriately restricted IAM profiles.

### Configuration[](https://zuul-ci.org/docs/zuul/latest/configuration.html#id5 "Link to this heading")

The following sections of `zuul.conf` are used by the executor:

executor[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor "Link to this definition")

executor.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.command_socket "Link to this definition")

Default:`/var/lib/zuul/executor.socket`

Path to command socket file for the executor process.

executor.finger_port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.finger_port "Link to this definition")

Default:`7900`

Port to use for finger log streamer.

executor.state_dir[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.state_dir "Link to this definition")

Default:`/var/lib/zuul`

Path to directory in which Zuul should save its state.

executor.git_dir[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.git_dir "Link to this definition")

Default:`/var/lib/zuul/executor-git`

Directory that Zuul should clone local git repositories to. The executor keeps a local copy of every git repository it works with to speed operations and perform speculative merging.

This should be on the same filesystem as [executor.job_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.job_dir "attr-executor.job_dir") so that when git repos are cloned into the job workspaces, they can be hard-linked to the local git cache.

executor.job_dir[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.job_dir "Link to this definition")

Default:`/var/lib/zuul/builds`

Directory that Zuul should use to hold temporary job directories. When each job is run, a new entry will be created under this directory to hold the configuration and scratch workspace for that job. It will be deleted at the end of the job (unless the –keep-jobdir command line option is specified).

This should be on the same filesystem as [executor.git_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.git_dir "attr-executor.git_dir") so that when git repos are cloned into the job workspaces, they can be hard-linked to the local git cache.

executor.log_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.log_config "Link to this definition")

Path to log config file for the executor process.

executor.pidfile[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.pidfile "Link to this definition")

Default:`/var/run/zuul/executor.pid`

Path to PID lock file for the executor process.

executor.private_key_file[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.private_key_file "Link to this definition")

Default:`~/.ssh/id_rsa`

SSH private key file to be used when logging into build nodes.

Note

If you use an RSA key, ensure it is encoded in the PEM format (use the `-t rsa -m PEM` arguments to ssh-keygen).

executor.default_username[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.default_username "Link to this definition")

Default:`zuul`

Username to use when logging into build nodes, if none is supplied by the image configuration.

executor.winrm_cert_key_file[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.winrm_cert_key_file "Link to this definition")

Default:`~/.winrm/winrm_client_cert.key`

The private key file of the client certificate to use for winrm connections to Windows nodes.

executor.winrm_cert_pem_file[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.winrm_cert_pem_file "Link to this definition")

Default:`~/.winrm/winrm_client_cert.pem`

The certificate file of the client certificate to use for winrm connections to Windows nodes.

Note

Currently certificate verification is disabled when connecting to Windows nodes via winrm.

executor.winrm_operation_timeout_sec[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.winrm_operation_timeout_sec "Link to this definition")

Default:`None. The Ansible default of 20 is used in this case.`

The timeout for WinRM operations.

executor.winrm_read_timeout_sec[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.winrm_read_timeout_sec "Link to this definition")

Default:`None. The Ansible default of 30 is used in this case.`

The timeout for WinRM read. Increase this if there are intermittent network issues and read timeout errors keep occurring.

executor.variables[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.variables "Link to this definition")

Path to an Ansible variables file to supply site-wide variables. This should be a YAML-formatted file consisting of a single dictionary. The contents will be made available to all jobs as Ansible variables. These variables take precedence over all other forms (job variables and secrets). Care should be taken when naming these variables to avoid potential collisions with those used by jobs. Prefixing variable names with a site-specific identifier is recommended. The default is not to add any site-wide variables. See the [User’s Guide](https://zuul-ci.org/docs/zuul/latest/job-content.html#user-jobs-sitewide-variables) for more information.

executor.manage_ansible[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.manage_ansible "Link to this definition")

Default:`True`

Specifies whether the zuul-executor should install the supported ansible versions during startup or not. If this is `True` the zuul-executor will install the ansible versions into [executor.ansible_root](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.ansible_root "attr-executor.ansible_root").

It is recommended to set this to `False` and manually install Ansible after the Zuul installation by running `zuul-manage-ansible`. This has the advantage that possible errors during Ansible installation can be spotted earlier. Further especially containerized deployments of Zuul will have the advantage of predictable versions.

executor.ansible_root[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.ansible_root "Link to this definition")

Default:`<state_dir>/ansible-bin`

Specifies where the zuul-executor should look for its supported ansible installations. By default it looks in the following directories and uses the first which it can find.

*   `<zuul_install_dir>/lib/zuul/ansible`

*   `<ansible_root>`

The `ansible_root` setting allows you to override the second location which is also used for installation if `manage_ansible` is `True`.

executor.ansible_setup_timeout[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.ansible_setup_timeout "Link to this definition")

Default:`60`

Timeout of the ansible setup playbook in seconds that runs before the first playbook of the job.

executor.disk_limit_per_job[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.disk_limit_per_job "Link to this definition")

Default:`250`

This integer is the maximum number of megabytes that any one job is allowed to consume on disk while it is running. If a job’s scratch space has more than this much space consumed, it will be aborted. Set to -1 to disable the limit.

executor.trusted_ro_paths[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.trusted_ro_paths "Link to this definition")

List of paths, separated by `:` to read-only bind mount into trusted bubblewrap contexts.

executor.trusted_rw_paths[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.trusted_rw_paths "Link to this definition")

List of paths, separated by `:` to read-write bind mount into trusted bubblewrap contexts.

executor.untrusted_ro_paths[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.untrusted_ro_paths "Link to this definition")

List of paths, separated by `:` to read-only bind mount into untrusted bubblewrap contexts.

executor.untrusted_rw_paths[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.untrusted_rw_paths "Link to this definition")

List of paths, separated by `:` to read-write bind mount into untrusted bubblewrap contexts.

executor.load_multiplier[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.load_multiplier "Link to this definition")

Default:`2.5`

When an executor host gets too busy, the system may suffer timeouts and other ill effects. The executor will stop accepting more than 1 job at a time until load has lowered below a safe level. This level is determined by multiplying the number of CPU’s by load_multiplier.

So for example, if the system has 2 CPUs, and load_multiplier is 2.5, the safe load for the system is 5.00. Any time the system load average is over 5.00, the executor will quit accepting multiple jobs at one time.

The executor will observe system load and determine whether to accept more jobs every 30 seconds.

executor.max_starting_builds[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.max_starting_builds "Link to this definition")

Default:`None`

An executor is accepting up to as many starting builds as defined by the [executor.load_multiplier](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.load_multiplier "attr-executor.load_multiplier") on systems with more than four CPU cores, and up to twice as many on systems with four or less CPU cores. For example, on a system with two CPUs: 2 * 2.5 * 2 - up to ten starting builds may run on such executor; on systems with eight CPUs: 2.5 * 8 - up to twenty starting builds may run on such executor.

On systems with high CPU/vCPU count an executor may accept too many starting builds. This can be overwritten using this option providing a fixed number of maximum starting builds on an executor.

executor.min_avail_hdd[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.min_avail_hdd "Link to this definition")

Default:`5.0`

This is the minimum percentage of HDD storage available for the [executor.state_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.state_dir "attr-executor.state_dir") directory. The executor will stop accepting more than 1 job at a time until more HDD storage is available. The available HDD percentage is calculated from the total available disk space divided by the total real storage capacity multiplied by 100.

executor.min_avail_inodes[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.min_avail_inodes "Link to this definition")

Default:`5.0`

This is the minimum percentage of HDD inodes available for the [executor.state_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.state_dir "attr-executor.state_dir") directory. The executor will stop accepting more than 1 job at a time until more inodes are available. The available inode percentage is calculated from the total available inodes divided by the total real inode capacity multiplied by 100.

executor.min_avail_mem[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.min_avail_mem "Link to this definition")

Default:`5.0`

This is the minimum percentage of system RAM available. The executor will stop accepting more than 1 job at a time until more memory is available. The available memory percentage is calculated from the total available memory divided by the total real memory multiplied by 100. Buffers and cache are considered available in the calculation.

executor.output_max_bytes[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.output_max_bytes "Link to this definition")

Default:`1073741824`

Warning

This option is deprecated. In the future, the default value of 1GiB is likely to become fixed and unable to be changed. Set this option only if needed and only as long as needed to adjust existing jobs to avoid the limit.

Zuul limits the total number of bytes output via stdout or stderr from a single Ansible command to this value. If the command outputs more than this number of bytes, the command execution will fail. This is to protect the executor from being required to read an excessively large amount of data from an ansible task result.

If a job fails due to this limit, consider adjusting the command task to redirect output to a file and collecting the file separately.

executor.hostname[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.hostname "Link to this definition")

Default:`hostname of the server`

The executor needs to know its hostname under which it is reachable by zuul-web. Otherwise live console log streaming doesn’t work. In most cases This is automatically detected correctly. But when running in environments where it cannot determine its hostname correctly this can be overridden here.

executor.paused_on_start[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.paused_on_start "Link to this definition")

Default:`false`

Whether the executor should start in a paused mode. Such executor will not accept tasks until it is unpaused.

executor.zone[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.zone "Link to this definition")

Default:`None`

Name of the executor-zone to exclusively execute all jobs that have nodes with the specified executor-zone attribute. As an example, it is possible for nodes to exist in a cloud without public accessible IP address. By adding an executor to a zone, nodes may be configured to use private ip addresses.

To enable this in Nodepool, you’ll use the node-attributes setting in a provider pool. For example:

pools:
 - name: main
 node-attributes:
 executor-zone: vpn

To enable this with Zuul’s provider configuration, set the `executor-zone` attribute of the label.

executor.allow_unzoned[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.allow_unzoned "Link to this definition")

Default:`False`

If [executor.zone](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.zone "attr-executor.zone") is set it by default only processes jobs with nodes of that specific zone even if the nodes have no zone at all. Enabling `allow_unzoned` lets the executor also take jobs with nodes without zone.

executor.merge_jobs[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.merge_jobs "Link to this definition")

Default:`True`

To disable global merge job, set it to false. This is useful for zoned executors that are running on slow network where you don’t want them to perform merge operations for any events. The executor will still perform the merge operations required for the build they are executing.

executor.sigterm_method[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.sigterm_method "Link to this definition")

Default:`graceful`

Determines how the executor responds to a `SIGTERM` signal.

graceful[](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-executor.sigterm_method.graceful "Link to this definition")
Stop accepting new jobs and wait for all running jobs to complete before exiting.

stop[](https://zuul-ci.org/docs/zuul/latest/configuration.html#value-executor.sigterm_method.stop "Link to this definition")
Abort all running jobs and exit as soon as possible.

executor.prometheus_port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.prometheus_port "Link to this definition")

Set a TCP port to start the prometheus metrics client.

executor.prometheus_addr[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.prometheus_addr "Link to this definition")

Default:`0.0.0.0`

The IPv4 addr to listen for prometheus metrics poll. To use IPv6, python>3.8 is required [issue24209](https://bugs.python.org/issue24209).

keystore

keystore.password(required)

Encryption password for private data stored in Zookeeper.

merger

merger.git_user_email

Value to pass to [git config user.email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

merger.git_user_name

Value to pass to [git config user.name](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

merger.prometheus_port

Set a TCP port to start the prometheus metrics client.

merger.prometheus_addr

Default:`0.0.0.0`

The IPv4 addr to listen for prometheus metrics poll. To use IPv6, python>3.8 is required [issue24209](https://bugs.python.org/issue24209).

ansible_callback"<name>"["" title="Link to this definition">](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-ansible_callback)

To whitelist ansible callback `<name>`. Any attributes found is this section will be added to the `callback_<name>` section in ansible.cfg.

An example of what configuring the builtin mail callback would look like. The configuration in zuul.conf.

[ansible_callback "mail"]
to = user@example.org
sender = zuul@example.org

Would generate the following in ansible.cfg:

[defaults]
callback_whitelist = mail

[callback_mail]
to = user@example.org
sender = zuul@example.org

Web Server[](https://zuul-ci.org/docs/zuul/latest/configuration.html#web-server "Link to this heading")
--------------------------------------------------------------------------------------------------------

The Zuul web server serves as the single process handling all HTTP interactions with Zuul. This includes the websocket interface for live log streaming, the REST API and the html/javascript dashboard. All three are served as a holistic web application. For information on additional supported deployment schemes, see [Web Deployment](https://zuul-ci.org/docs/zuul/latest/installation.html#web-deployment-options).

Web servers need to be able to connect to the ZooKeeper cluster and the SQL database. If a GitHub, Gitlab, or Pagure connection is configured, they need to be reachable so they may receive notifications.

In addition to the common configuration sections, the following sections of `zuul.conf` are used by the web server:

web

web.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.command_socket "Link to this definition")

Default:`/var/lib/zuul/web.socket`

Path to command socket file for the web process.

web.listen_address[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.listen_address "Link to this definition")

Default:`127.0.0.1`

IP address or domain name on which to listen.

web.log_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.log_config "Link to this definition")

Path to log config file for the web server process.

web.pidfile[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.pidfile "Link to this definition")

Default:`/var/run/zuul/web.pid`

Path to PID lock file for the web server process.

web.port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.port "Link to this definition")

Default:`9000`

Port to use for web server process.

web.websocket_url[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.websocket_url "Link to this definition")

Base URL on which the websocket service is exposed, if different than the base URL of the web app.

web.stats_url[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.stats_url "Link to this definition")

Base URL from which statistics emitted via statsd can be queried.

web.stats_type[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.stats_type "Link to this definition")

Default:`graphite`

Type of server hosting the statistics information. Currently only ‘graphite’ is supported by the dashboard.

web.static_path[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.static_path "Link to this definition")

Default:`zuul/web/static`

Path containing the static web assets.

web.static_cache_expiry[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.static_cache_expiry "Link to this definition")

Default:`3600`

The Cache-Control max-age response header value for static files served by the zuul-web. Set to 0 during development to disable Cache-Control.

web.zone[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.zone "Link to this definition")

The zone in which zuul-web is deployed. This is only needed if there are executors with different zones in the environment and not all executors are directly addressable from zuul-web. The parameter specifies the zone where the executors are directly addressable. Live log streaming will go directly to the executors of the same zone and be routed to a finger gateway of the target zone if the zones are different.

In a mixed system (with zoned and unzoned executors) there may also be zoned and unzoned zuul-web services. Omit the zone parameter for any unzoned zuul-web servers.

If this is used the finger gateways should be configured accordingly.

web.auth_log_file_requests[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.auth_log_file_requests "Link to this definition")

Default:`false`

If set to true, the JavaScript web client will pass an Authorization header with HTTP requests for log files if the origin of a log file is the same as the Zuul API. This is useful when build logs are served through the same authenticated endpoint as the API (e.g. a reverse proxy).

keystore

keystore.password(required)

Encryption password for private data stored in Zookeeper.

### Authentication[](https://zuul-ci.org/docs/zuul/latest/configuration.html#authentication "Link to this heading")

A user can be granted access to protected REST API endpoints by providing a valid JWT (JSON Web Token) as a bearer token when querying the API endpoints.

JWTs are signed and therefore Zuul must be configured so that signatures can be verified. More information about the JWT standard can be found on the [IETF’s RFC page](https://tools.ietf.org/html/rfc7519).

This optional section of `zuul.conf`, if present, will activate the protected endpoints and configure JWT validation:

auth<authenticator name>[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E "Link to this definition")

auth<authenticator name>.driver[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.driver "Link to this definition")

The signing algorithm to use. Accepted values are `HS256`, `RS256`, `RS256withJWKS` or `OpenIDConnect`. See below for driver-specific configuration options.

auth<authenticator name>.allow_authz_override[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.allow_authz_override "Link to this definition")

Default:`false`

Allow a JWT to override predefined access rules. See the section on [JWT contents](https://zuul-ci.org/docs/zuul/latest/authentication.html#jwt-format) for more details on how to grant access to tenants with a JWT.

auth<authenticator name>.realm[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.realm "Link to this definition")

The authentication realm.

auth<authenticator name>.default[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.default "Link to this definition")

Default:`false`

If set to `true`, use this realm as the default authentication realm when handling HTTP authentication errors.

auth<authenticator name>.client_id[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.client_id "Link to this definition")

The expected value of the “aud” claim in the JWT. This is required for validation.

auth<authenticator name>.issuer_id[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.issuer_id "Link to this definition")

The expected value of the “iss” claim in the JWT. This is required for validation.

auth<authenticator name>.uid_claim[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.uid_claim "Link to this definition")

Default:`sub`

The JWT claim that Zuul will use as a unique identifier for the bearer of a token. This is “sub” by default, as it is usually the purpose of this claim in a JWT. This identifier is used in audit logs.

auth<authenticator name>.max_validity_time[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.max_validity_time "Link to this definition")

Optional value to ensure a JWT cannot be valid for more than this amount of time in seconds. This is useful if the Zuul operator has no control over the service issuing JWTs, and the tokens are too long-lived.

auth<authenticator name>.skew[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-auth%20%3Cauthenticator%20name%3E.skew "Link to this definition")

Default:`0`

Optional integer value to compensate for skew between Zuul’s and the JWT emitter’s respective clocks. Use a negative value if Zuul’s clock is running behind.

This section can be repeated as needed with different authenticators, allowing access to privileged API actions from several JWT issuers.

#### Driver-specific attributes[](https://zuul-ci.org/docs/zuul/latest/configuration.html#driver-specific-attributes "Link to this heading")

##### HS256[](https://zuul-ci.org/docs/zuul/latest/configuration.html#hs256 "Link to this heading")

This is a symmetrical encryption algorithm that only requires a shared secret between the JWT issuer and the JWT consumer (ie Zuul). This driver should be used in test deployments, or in deployments where JWTs may be issued manually to users.

Note

At least one HS256 authenticator should be configured in order to use admin commands with the Zuul command line interface.

secret

The shared secret used to sign JWTs and validate signatures.

##### RS256[](https://zuul-ci.org/docs/zuul/latest/configuration.html#rs256 "Link to this heading")

This is an asymmetrical encryption algorithm that requires an RSA key pair. Only the public key is needed by Zuul for signature validation.

public_key[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-public_key "Link to this definition")

The path to the public key of the RSA key pair. It must be readable by Zuul.

private_key[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-private_key "Link to this definition")

Optional. The path to the private key of the RSA key pair. It must be readable by Zuul.

##### RS256withJWKS[](https://zuul-ci.org/docs/zuul/latest/configuration.html#rs256withjwks "Link to this heading")

Warning

This driver is deprecated, use `OpenIDConnect` instead.

Some Identity Providers use key sets (also known as **JWKS**), therefore the key to use when verifying the Authentication Token’s signatures cannot be known in advance; the key’s id is stored in the JWT’s header and the key must then be found in the remote key set. The key set is usually available at a specific URL that can be found in the “well-known” configuration of an OpenID Connect Identity Provider.

keys_url[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keys_url "Link to this definition")

The URL where the Identity Provider’s key set can be found. For example, for Google’s OAuth service: [https://www.googleapis.com/oauth2/v3/certs](https://www.googleapis.com/oauth2/v3/certs)

##### OpenIDConnect[](https://zuul-ci.org/docs/zuul/latest/configuration.html#openidconnect "Link to this heading")

Use a third-party Identity Provider implementing the OpenID Connect protocol. The issuer ID should be an URI, from which the “well-known” configuration URI of the Identity Provider can be inferred. This is intended to be used for authentication on Zuul’s web user interface.

scope[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scope "Link to this definition")

Default:`openid profile`

The scope(s) to use when requesting access to a user’s details. This attribute can be multivalued (values must be separated by a space). Most OpenID Connect Identity Providers support the default scopes “openid profile”. A full list of supported scopes can be found in the well-known configuration of the Identity Provider under the key “scopes_supported”.

keys_url

Optional. The URL where the Identity Provider’s key set can be found. For example, for Google’s OAuth service: [https://www.googleapis.com/oauth2/v3/certs](https://www.googleapis.com/oauth2/v3/certs) The well-known configuration of the Identity Provider should provide this URL under the key “jwks_uri”, therefore this attribute is usually not necessary.

Some providers may not conform to the JWT specification and further configuration may be necessary. In these cases, the following additional values may be used:

authority[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-authority "Link to this definition")

Default:`issuer_id`

If the authority in the token response is not the same as the issuer_id in the request, it may be explicitly set here.

audience[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-audience "Link to this definition")

Default:`client_id`

If the audience in the token response is not the same as the issuer_id in the request, it may be explicitly set here.

load_user_info[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-load_user_info "Link to this definition")

Default:`true`

If the web UI should skip accessing the “UserInfo” endpoint and instead rely only on the information returned in the token, set this to `false`.

Launcher[](https://zuul-ci.org/docs/zuul/latest/configuration.html#launcher "Link to this heading")
----------------------------------------------------------------------------------------------------

The launcher is responsible for the lifecycle of build nodes and other resources. They may be virtual machines (ephemeral or long-lived), real hardware with static addresses, containers, or other resources. There are a number of drivers that implement functionality for static hosts and various cloud providers.

The launcher must communicate with ZooKeeper and also the build nodes that it is responsible for. Multiple launchers may be run, and they will work cooperatively to scale out their handling of requests. Certain launchers may be restricetd by configuration to servicing only certain connections.

In addition to the common configuration sections, the following sections of `zuul.conf` are used by the launcher:

launcher[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-launcher "Link to this definition")

launcher.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-launcher.command_socket "Link to this definition")

Default:`/var/lib/zuul/launcher.socket`

Path to command socket file for the launcher process.

launcher.temp_dir[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-launcher.temp_dir "Link to this definition")

Default:`/tmp`

Temporary directory used for downloading images while uploading them to providers. Depending on the number of images and their sizes that are managed by Zuul, this space may need to be very large.

launcher.connection_filter[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-launcher.connection_filter "Link to this definition")

If this launcher should only be used for certain connections, specify them here as a comma separated string.

Client[](https://zuul-ci.org/docs/zuul/latest/configuration.html#client "Link to this heading")
------------------------------------------------------------------------------------------------

Zuul’s command line client may be configured to make calls to Zuul’s web server. The client will then look for a `zuul.conf` file with a `webclient` section to set up the connection over HTTP.

Note

At least one authenticator must be configured in Zuul for admin commands to be enabled in the client.

webclient[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-webclient "Link to this definition")

webclient.url[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-webclient.url "Link to this definition")

The root URL of Zuul’s web server.

webclient.verify_ssl[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-webclient.verify_ssl "Link to this definition")

Default:`true`

Enforce SSL verification when sending requests over to Zuul’s web server. This should only be disabled when working with test servers.

Finger Gateway[](https://zuul-ci.org/docs/zuul/latest/configuration.html#finger-gateway "Link to this heading")
----------------------------------------------------------------------------------------------------------------

The Zuul finger gateway listens on the standard finger port (79) for finger requests specifying a build UUID for which it should stream log results. The gateway will determine which executor is currently running that build and query that executor for the log stream.

This is intended to be used with the standard finger command line client. For example:

finger UUID@zuul.example.com

The above would stream the logs for the build identified by UUID.

Finger gateway servers need to be able to connect to the ZooKeeper cluster, as well as the console streaming port on the executors (usually 7900).

Finger gateways are optional. They may be run for either or both of the following purposes:

*   Allowing end-users to connect to the finger port to stream logs.

*   Providing an accessible log streaming port for remote zoned executors which are otherwise inaccessible.

In this case, log streaming requests from finger gateways or zuul-web will route to the executors via finger gateways in the same zone.

In addition to the common configuration sections, the following sections of `zuul.conf` are used by the finger gateway:

fingergw[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw "Link to this definition")

> fingergw.command_socket[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.command_socket "Link to this definition")
> 
> Default:`/var/lib/zuul/fingergw.socket`
> 
> 
> Path to command socket file for the executor process.
> 
> fingergw.listen_address[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.listen_address "Link to this definition")
> 
> Default:`all addresses`
> 
> 
> IP address or domain name on which to listen.
> 
> fingergw.log_config[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.log_config "Link to this definition")
> 
> 
> Path to log config file for the finger gateway process.
> 
> fingergw.pidfile[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.pidfile "Link to this definition")
> 
> Default:`/var/run/zuul/fingergw.pid`
> 
> 
> Path to PID lock file for the finger gateway process.
> 
> fingergw.port[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.port "Link to this definition")
> 
> Default:`79`
> 
> 
> Port to use for the finger gateway. Note that since command line finger clients cannot usually specify the port, leaving this set to the default value is highly recommended.
> 
> fingergw.user[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.user "Link to this definition")
> 
> 
> User ID for the zuul-fingergw process. In normal operation as a daemon, the finger gateway should be started as the `root` user, but if this option is set, it will drop privileges to this user during startup. It is recommended to set this option to an unprivileged user.
> 
> fingergw.hostname[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.hostname "Link to this definition")
> 
> Default:`hostname of the server`
> 
> 
> When running finger gateways in a multi-zone configuration, the gateway needs to know its hostname under which it is reachable by zuul-web. Otherwise live console log streaming doesn’t work. In most cases This is automatically detected correctly. But when running in environments where it cannot determine its hostname correctly this can be overridden here.
> 
> fingergw.zone[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.zone "Link to this definition")
> 
> 
> The zone where the finger gateway is located. This is only needed for live log streaming if the zuul deployment is spread over multiple zones without the ability to directly connect to all executors from zuul-web. See [executor.zone](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.zone "attr-executor.zone") for further information.
> 
> 
> In a mixed system (with zoned and unzoned executors) there may also be zoned and unzoned finger gateway services. Omit the zone parameter for any unzoned finger gateway servers.

If the Zuul installation spans an untrusted network (for example, if there are remote executor zones), it may be necessary to use TLS between the components that handle log streaming (zuul-executor, zuul-fingergw, and zuul-web). If so, set the following options.

Note that this section is also read by zuul-web in order to load a client certificate to use when connecting to a finger gateway which requires TLS, and it is also read by zuul-executor to load a server certificate for its console streaming port.

If any of these are present, all three certificate options must be provided.

> fingergw.tls_cert[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_cert "Link to this definition")
> 
> 
> The path to the PEM encoded certificate file.
> 
> fingergw.tls_key[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_key "Link to this definition")
> 
> 
> The path to the PEM encoded key file.
> 
> fingergw.tls_ca[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_ca "Link to this definition")
> 
> 
> The path to the PEM encoded CA certificate file.
> 
> fingergw.tls_verify_hostnames[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_verify_hostnames "Link to this definition")
> 
> Default:`true`
> 
> 
> In the case of a private CA it may be both safe and convenient to disable hostname checks. However, if the certificates are issued by a public CA, hostname verification should be enabled.
> 
> fingergw.tls_client_only[](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_client_only "Link to this definition")
> 
> Default:`false`
> 
> 
> In order to provide a finger gateway which can reach remote finger gateways and executors which use TLS, but does not itself serve end-users via TLS (i.e., it runs within a protected network and users access it directly via the finger port), set this to `true` and the finger gateway will not listen on TLS, but will still use the supplied certificate to make remote TLS connections.

Connections[](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections "Link to this heading")
==========================================================================================================

Most of Zuul’s configuration is contained in the git repositories upon which Zuul operates, however, some configuration outside of git repositories is still required to bootstrap the system. This includes information on connections between Zuul and other systems, as well as identifying the projects Zuul uses.

In order to interact with external systems, Zuul must have a _connection_ to that system configured. Zuul includes a number of [drivers](https://zuul-ci.org/docs/zuul/latest/drivers/index.html#drivers), each of which implements the functionality necessary to connect to a system. Each connection in Zuul is associated with a driver.

Connections are also used for communicating with cloud providers used by the Zuul launcher.

To configure a connection in Zuul, select a unique name for the connection and add a section to `zuul.conf` with the form `[connection NAME]`. For example, a connection to a gerrit server may appear as:

[connection mygerritserver]
driver=gerrit
server=review.example.com

Zuul needs to use a single connection to look up information about changes hosted by a given system. When it looks up changes, it will do so using the first connection it finds that matches the server name it’s looking for. It’s generally best to use only a single connection for a given server, however, if you need more than one (for example, to satisfy unique reporting requirements) be sure to list the primary connection first as that is what Zuul will use to look up all changes for that server.

[Previous](https://zuul-ci.org/docs/zuul/latest/components.html "Component Overview")[Next](https://zuul-ci.org/docs/zuul/latest/drivers/index.html "Drivers")

* * *

© Copyright 2012-2026, Zuul project contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

Versions v: latest 

[latest](https://zuul-ci.org/docs/zuul/latest/)[14.0.0](https://zuul-ci.org/docs/zuul/14.0.0/)[13.1.1](https://zuul-ci.org/docs/zuul/13.1.1/)[13.1.0](https://zuul-ci.org/docs/zuul/13.1.0/)[13.0.1](https://zuul-ci.org/docs/zuul/13.0.1/)[13.0.0](https://zuul-ci.org/docs/zuul/13.0.0/)[12.1.0](https://zuul-ci.org/docs/zuul/12.1.0/)[12.0.0](https://zuul-ci.org/docs/zuul/12.0.0/)[11.3.0](https://zuul-ci.org/docs/zuul/11.3.0/)[11.2.0](https://zuul-ci.org/docs/zuul/11.2.0/)[11.1.0](https://zuul-ci.org/docs/zuul/11.1.0/)[11.0.1](https://zuul-ci.org/docs/zuul/11.0.1/)[11.0.0](https://zuul-ci.org/docs/zuul/11.0.0/)[10.2.0](https://zuul-ci.org/docs/zuul/10.2.0/)[10.1.0](https://zuul-ci.org/docs/zuul/10.1.0/)[10.0.0](https://zuul-ci.org/docs/zuul/10.0.0/)[9.5.0](https://zuul-ci.org/docs/zuul/9.5.0/)[9.4.0](https://zuul-ci.org/docs/zuul/9.4.0/)[9.3.0](https://zuul-ci.org/docs/zuul/9.3.0/)[9.2.0](https://zuul-ci.org/docs/zuul/9.2.0/)[9.1.0](https://zuul-ci.org/docs/zuul/9.1.0/)[9.0.0](https://zuul-ci.org/docs/zuul/9.0.0/)[8.3.1](https://zuul-ci.org/docs/zuul/8.3.1/)[8.3.0](https://zuul-ci.org/docs/zuul/8.3.0/)[8.2.0](https://zuul-ci.org/docs/zuul/8.2.0/)[8.1.0](https://zuul-ci.org/docs/zuul/8.1.0/)[8.0.1](https://zuul-ci.org/docs/zuul/8.0.1/)[8.0.0](https://zuul-ci.org/docs/zuul/8.0.0/)[7.1.0](https://zuul-ci.org/docs/zuul/7.1.0/)[7.0.0](https://zuul-ci.org/docs/zuul/7.0.0/)[6.4.0](https://zuul-ci.org/docs/zuul/6.4.0/)[6.3.0](https://zuul-ci.org/docs/zuul/6.3.0/)[6.2.0](https://zuul-ci.org/docs/zuul/6.2.0/)[6.1.0](https://zuul-ci.org/docs/zuul/6.1.0/)[6.0.0](https://zuul-ci.org/docs/zuul/6.0.0/)[5.2.5](https://zuul-ci.org/docs/zuul/5.2.5/)[5.2.4](https://zuul-ci.org/docs/zuul/5.2.4/)[5.2.3](https://zuul-ci.org/docs/zuul/5.2.3/)[5.2.2](https://zuul-ci.org/docs/zuul/5.2.2/)[5.2.1](https://zuul-ci.org/docs/zuul/5.2.1/)[5.2.0](https://zuul-ci.org/docs/zuul/5.2.0/)[5.1.0](https://zuul-ci.org/docs/zuul/5.1.0/)[5.0.0](https://zuul-ci.org/docs/zuul/5.0.0/)[4.12.0](https://zuul-ci.org/docs/zuul/4.12.0/)[4.11.0](https://zuul-ci.org/docs/zuul/4.11.0/)[4.10.4](https://zuul-ci.org/docs/zuul/4.10.4/)[4.10.3](https://zuul-ci.org/docs/zuul/4.10.3/)[4.10.2](https://zuul-ci.org/docs/zuul/4.10.2/)[4.10.1](https://zuul-ci.org/docs/zuul/4.10.1/)[4.10.0](https://zuul-ci.org/docs/zuul/4.10.0/)[4.9.0](https://zuul-ci.org/docs/zuul/4.9.0/)[4.8.1](https://zuul-ci.org/docs/zuul/4.8.1/)[4.8.0](https://zuul-ci.org/docs/zuul/4.8.0/)[4.7.0](https://zuul-ci.org/docs/zuul/4.7.0/)[4.6.0](https://zuul-ci.org/docs/zuul/4.6.0/)[4.5.1](https://zuul-ci.org/docs/zuul/4.5.1/)[4.5.0](https://zuul-ci.org/docs/zuul/4.5.0/)[4.4.0](https://zuul-ci.org/docs/zuul/4.4.0/)[4.3.0](https://zuul-ci.org/docs/zuul/4.3.0/)[4.2.0](https://zuul-ci.org/docs/zuul/4.2.0/)[4.1.0](https://zuul-ci.org/docs/zuul/4.1.0/)[4.0.0](https://zuul-ci.org/docs/zuul/4.0.0/)[3.19.1](https://zuul-ci.org/docs/zuul/3.19.1/)[3.19.0](https://zuul-ci.org/docs/zuul/3.19.0/)[3.18.0](https://zuul-ci.org/docs/zuul/3.18.0/)[3.17.0](https://zuul-ci.org/docs/zuul/3.17.0/)[3.16.1](https://zuul-ci.org/docs/zuul/3.16.1/)[3.16.0](https://zuul-ci.org/docs/zuul/3.16.0/)[3.15.0](https://zuul-ci.org/docs/zuul/3.15.0/)[3.14.0](https://zuul-ci.org/docs/zuul/3.14.0/)[3.13.0](https://zuul-ci.org/docs/zuul/3.13.0/)[3.12.0](https://zuul-ci.org/docs/zuul/3.12.0/)[3.11.1](https://zuul-ci.org/docs/zuul/3.11.1/)[3.11.0](https://zuul-ci.org/docs/zuul/3.11.0/)[3.10.2](https://zuul-ci.org/docs/zuul/3.10.2/)[3.10.1](https://zuul-ci.org/docs/zuul/3.10.1/)[3.10.0](https://zuul-ci.org/docs/zuul/3.10.0/)[3.9.0](https://zuul-ci.org/docs/zuul/3.9.0/)[3.8.1](https://zuul-ci.org/docs/zuul/3.8.1/)[3.8.0](https://zuul-ci.org/docs/zuul/3.8.0/)[3.7.1](https://zuul-ci.org/docs/zuul/3.7.1/)[3.7.0](https://zuul-ci.org/docs/zuul/3.7.0/)[3.6.1](https://zuul-ci.org/docs/zuul/3.6.1/)[3.6.0](https://zuul-ci.org/docs/zuul/3.6.0/)[3.5.0](https://zuul-ci.org/docs/zuul/3.5.0/)[3.4.0](https://zuul-ci.org/docs/zuul/3.4.0/)[3.3.1](https://zuul-ci.org/docs/zuul/3.3.1/)[3.3.0](https://zuul-ci.org/docs/zuul/3.3.0/)
