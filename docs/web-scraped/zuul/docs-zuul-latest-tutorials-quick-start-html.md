# Source: https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html

Title: Quick-Start Installation and Tutorial — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html

Published Time: Wed, 11 Mar 2026 16:34:38 GMT

Markdown Content:
Quick-Start Installation and Tutorial — Zuul documentation
===============

[![Image 20: Logo](https://zuul-ci.org/docs/zuul/latest/_static/logo.svg)](https://zuul-ci.org/docs/zuul/latest/index.html)

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

*   [Quick-Start Installation and Tutorial](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#)
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
    *   [Configuration](https://zuul-ci.org/docs/zuul/latest/configuration.html)
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
*   Quick-Start Installation and Tutorial
*   [View page source](https://zuul-ci.org/docs/zuul/latest/_sources/tutorials/quick-start.rst.txt)

* * *

Quick-Start Installation and Tutorial[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#quick-start-installation-and-tutorial "Link to this heading")
======================================================================================================================================================================

Zuul is not like other CI or CD systems. It is a project gating system designed to assist developers in taking a change from proposal through deployment. Zuul can support any number of workflow processes and systems, but to help you get started with Zuul, this tutorial will walk through setting up a basic gating configuration which protects projects from merging broken code.

This tutorial is entirely self-contained and may safely be run on a workstation. The only requirements are a network connection, the ability to run containers, and at least 2GiB of RAM.

This tutorial supplies a working Gerrit for code review, though the concepts you will learn apply equally to GitHub.

Note

Even if you don’t ultimately intend to use Gerrit, you are encouraged to follow this tutorial to learn how to set up and use Zuul.

At the end of the tutorial, you will find further information about how to configure your Zuul to interact with GitHub.

Start Zuul Containers[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#start-zuul-containers "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

Before you start, ensure that some needed packages are installed.

# Fedora:

sudo dnf install git git-review docker-compose

# OpenSuse:

sudo zypper install git git-review docker-compose

# Ubuntu (Noble or later) / Debian:

sudo apt update
sudo apt install git git-review docker-compose-v2

Clone the Zuul repository:

git clone https://opendev.org/zuul/zuul

Then cd into the directory containing this document, and run docker compose in order to start Zuul and Gerrit.

cd zuul/doc/source/examples
docker compose -p zuul-tutorial up

For reference, the files in that directory are also [browsable on the web](https://opendev.org/zuul/zuul/src/branch/master/doc/source/examples).

All of the services will be started with debug-level logging sent to the standard output of the terminal where docker compose is running. You will see a considerable amount of information scroll by, including some errors. Zuul will immediately attempt to connect to Gerrit and begin processing, even before Gerrit has fully initialized. The docker composition includes scripts to configure Gerrit and create an account for Zuul. Once this has all completed, the system should automatically connect, stabilize and become idle. When this is complete, you will have the following services running:

*   Zookeeper

*   Gerrit

*   Zuul Scheduler

*   Zuul Web Server

*   Zuul Executor

*   Zuul Launcher

*   Apache HTTPD

And a long-running static test node used by Zuul upon which to run tests.

The Zuul scheduler is configured to connect to Gerrit via a connection named `gerrit`. Zuul can interact with as many systems as necessary, each such connection is assigned a name for use in the Zuul configuration.

Zuul is a multi-tenant application, so that differing needs of independent work-groups can be supported from one system. This example configures a single tenant named `example-tenant`. Assigned to this tenant are three projects: `zuul-config`, `test1` and `test2`. These have already been created in Gerrit and are ready for us to begin using.

Add Your Gerrit Account[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#add-your-gerrit-account "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Before you can interact with Gerrit, you will need to create an account. The initialization script has already created an account for Zuul, but has left the task of creating your own account to you so that you can provide your own SSH key. You may safely use any existing SSH key on your workstation, or you may create a new one by running `ssh-keygen`.

Gerrit is configured in a development mode where passwords are not required in the web interface and you may become any user in the system at any time.

To create your Gerrit account, visit [http://localhost:8080](http://localhost:8080/) in your browser and click Sign in in the top right corner.

![Image 21: ../_images/sign-in.png](https://zuul-ci.org/docs/zuul/latest/_images/sign-in.png)
Then click New Account under Register.

![Image 22: ../_images/register.png](https://zuul-ci.org/docs/zuul/latest/_images/register.png)
Don’t bother to enter anything into the confirmation dialog that pops up, instead, click the settings link at the bottom.

![Image 23: ../_images/confirm.png](https://zuul-ci.org/docs/zuul/latest/_images/confirm.png)
In the Profile section at the top, enter the username you use to log into your workstation in the Username field and your full name in the Full name field, then click Save Changes.

![Image 24: ../_images/profile.png](https://zuul-ci.org/docs/zuul/latest/_images/profile.png)
Scroll down to the Email Addresses section and enter your email address into the New email address field, then click Send Verification. Since Gerrit is in developer mode, it will not actually send any email, and the address will be automatically confirmed. This step is useful since several parts of the Gerrit user interface expect to be able to display email addresses.

![Image 25: ../_images/email.png](https://zuul-ci.org/docs/zuul/latest/_images/email.png)
Scroll down to the SSH keys section and copy and paste the contents of `~/.ssh/id_rsa.pub` into the New SSH key field and click Add New SSH Key.

![Image 26: ../_images/sshkey.png](https://zuul-ci.org/docs/zuul/latest/_images/sshkey.png)
Click the Reload button in your browser to reload the page with the new settings in effect. At this point you have created and logged into your personal account in Gerrit and are ready to begin configuring Zuul.

Configure Zuul Pipelines[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#configure-zuul-pipelines "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Zuul recognizes two types of projects: [config projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project) and [untrusted projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-untrusted-project). An _untrusted project_ is a normal project from Zuul’s point of view. In a gating system, it contains the software under development and/or most of the job content that Zuul will run. A _config project_ is a special project that contains the Zuul’s configuration. Because it has access to normally restricted features in Zuul, changes to this repository are not dynamically evaluated by Zuul. The security and functionality of the rest of the system depends on this repository, so it is best to limit what is contained within it to the minimum, and ensure thorough code review practices when changes are made.

Zuul has no built-in workflow definitions, so in order for it to do anything, you will need to begin by making changes to a _config project_. The initialization script has already created a project named `zuul-config` which you should now clone onto your workstation:

git clone http://localhost:8080/zuul-config

You will find that this repository is empty. Zuul reads its configuration from either a single file or a directory. In a _Config Project_ with substantial Zuul configuration, you may find it easiest to use the `zuul.d` directory for Zuul configuration. Later, in _Untrusted Projects_ you will use a single file for in-repo configuration. Make the directory:

cd zuul-config
mkdir zuul.d

The first type of configuration items we need to add are the Pipelines we intend to use. In Zuul, a Pipeline represents a workflow action. It is triggered by some action on a connection. Projects are able to attach jobs to run in that pipeline, and when they complete, the results are reported along with actions which may trigger further Pipelines. In a gating system two pipelines are required: [check](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-check) and [gate](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-gate). In our system, `check` will be triggered when a patch is uploaded to Gerrit, so that we are able to immediately run tests and report whether the change works and is therefore able to merge. The `gate` pipeline is triggered when a code reviewer approves the change in Gerrit. It will run test jobs again (in case other changes have merged since the change in question was uploaded) and if these final tests pass, will automatically merge the change. To configure these pipelines, copy the following file into `zuul.d/pipelines.yaml`:

- pipeline:
 name: check
 description: |
 Newly uploaded patchsets enter this pipeline to receive an
 initial +/-1 Verified vote.
 manager: independent
 require:
 gerrit:
 open: True
 current-patchset: True
 trigger:
 gerrit:
 - event: patchset-created
 - event: change-restored
 - event: comment-added
 comment: (?i)^(Patch Set [0-9]+:)?( [\w\\+-]*)*(\n\n)?\s*recheck
 success:
 gerrit:
 Verified: 1
 failure:
 gerrit:
 Verified: -1

- pipeline:
 name: gate
 description: |
 Changes that have been approved are enqueued in order in this
 pipeline, and if they pass tests, will be merged.
 manager: dependent
 post-review: True
 require:
 gerrit:
 open: True
 current-patchset: True
 approval:
 - Workflow: 1
 trigger:
 gerrit:
 - event: comment-added
 approval:
 - Workflow: 1
 start:
 gerrit:
 Verified: 0
 success:
 gerrit:
 Verified: 2
 submit: true
 failure:
 gerrit:
 Verified: -2

Once we have bootstrapped our initial Zuul configuration, we will want to use the gating process on this repository too, so we need to attach the `zuul-config` repository to the `check` and `gate` pipelines we are about to create. There are no jobs defined yet, so we must use the internally defined `noop` job, which always returns success.

Later on we will be configuring some other projects, and while we will be able to dynamically add jobs to their pipelines, those projects must first be attached to the pipelines in order for that to work, and that attachment can not be made dynamically; we need to merge a change where the projects are at least configured to use the pipelines, even if we later dynamically configure the actual jobs they run.

In our system, we want all of the projects in Gerrit to participate in the check and gate pipelines, so we can use a regular expression to apply this to all projects. To configure the `check` and `gate` pipelines for `zuul-config` to run the `noop` job, and add all projects to those pipelines (with no jobs), copy the following file into `zuul.d/projects.yaml`:

- project:
 name: ^.*$
 check:
 jobs: []
 gate:
 jobs: []

- project:
 name: zuul-config
 check:
 jobs:
 - noop
 gate:
 jobs:
 - noop

Every real job (i.e., all jobs other than `noop`) must inherit from a [base job](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-base-job), and base jobs may only be defined in a [config-project](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project). Let’s go ahead and add a simple base job that we can build on later. Copy the following into `zuul.d/jobs.yaml`:

- job:
 name: base
 parent: null
 nodeset:
 nodes:
 - name: ubuntu-jammy
 label: ubuntu-jammy

Commit the changes and push them up for review:

git add zuul.d
git commit -m "Add initial Zuul configuration"
git review

Because Zuul is currently running with no configuration whatsoever, it will ignore this change. For this initial change which bootstraps the entire system, we will need to bypass code review (hopefully for the last time). To do this, you need to switch to the Administrator account in Gerrit. Visit [http://localhost:8080](http://localhost:8080/) in your browser and then:

Click the avatar image in the top right corner then click Sign out.

![Image 27: ../_images/sign-out-user.png](https://zuul-ci.org/docs/zuul/latest/_images/sign-out-user.png)
Then click the Sign in link again.

![Image 28: ../_images/sign-in.png](https://zuul-ci.org/docs/zuul/latest/_images/sign-in.png)
Click admin to log in as the admin user.

![Image 29: ../_images/become-select.png](https://zuul-ci.org/docs/zuul/latest/_images/become-select.png)
You will then see a list of open changes; click on the change you uploaded.

![Image 30: ../_images/open-changes.png](https://zuul-ci.org/docs/zuul/latest/_images/open-changes.png)
Click Reply… at the top center of the change screen. This will open a dialog where you can leave a review message and vote on the change. As the administrator, you have access to vote in all of the review categories, even Verified which is normally reserved for Zuul. Vote Code-Review: +2, Verified: +2, Workflow: +1, and then click Send to leave your approval votes.

![Image 31: ../_images/review-1001.png](https://zuul-ci.org/docs/zuul/latest/_images/review-1001.png)
Once the required votes have been set, the Submit button will appear in the top right; click it. This will cause the change to be merged immediately. This is normally handled by Zuul, but as the administrator you can bypass Zuul to forcibly merge a change.

![Image 32: ../_images/submit-1001.png](https://zuul-ci.org/docs/zuul/latest/_images/submit-1001.png)
Now that the initial configuration has been bootstrapped, you should not need to bypass testing and code review again, so switch back to the account you created for yourself. Click on the avatar image in the top right corner then click Sign out.

![Image 33: ../_images/sign-out-admin.png](https://zuul-ci.org/docs/zuul/latest/_images/sign-out-admin.png)
Then click the Sign in link again.

![Image 34: ../_images/sign-in.png](https://zuul-ci.org/docs/zuul/latest/_images/sign-in.png)
And click your username to log into your account.

![Image 35: ../_images/become-select.png](https://zuul-ci.org/docs/zuul/latest/_images/become-select.png)
Test Zuul Pipelines[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#test-zuul-pipelines "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Zuul is now running with a basic [check](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-check) and [gate](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-gate) configuration. Now is a good time to take a look at Zuul’s web interface. Visit [http://localhost:9000/t/example-tenant/status](http://localhost:9000/t/example-tenant/status) to see the current status of the system. It should be idle, but if you leave this page open during the following steps, you will see it update automatically.

We can now begin adding Zuul configuration to one of our [untrusted projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-untrusted-project). Start by cloning the test1 project which was created by the setup script.

cd ..
git clone http://localhost:8080/test1

Every Zuul job that runs needs a playbook, so let’s create a sub-directory in the project to hold playbooks:

cd test1
mkdir playbooks

Start with a simple playbook which just outputs a debug message. Copy the following to `playbooks/testjob.yaml`:

- hosts: all
 tasks:
 - debug:
 msg: Hello world!

Now define a Zuul job which runs that playbook. Zuul will read its configuration from any of `zuul.d/` or `.zuul.d/` directories, or the files `zuul.yaml` or `.zuul.yaml`. Generally in an _untrusted project_ which isn’t dedicated entirely to Zuul, it’s best to put Zuul’s configuration in a hidden file. Copy the following to `.zuul.yaml` in the root of the project:

- job:
 name: testjob
 run: playbooks/testjob.yaml

- project:
 check:
 jobs:
 - testjob
 gate:
 jobs:
 - testjob

Commit the changes and push them up to Gerrit for review:

git add .zuul.yaml playbooks
git commit -m "Add test Zuul job"
git review

Zuul will dynamically evaluate proposed changes to its configuration in _untrusted projects_ immediately, so shortly after your change is uploaded, Zuul will run the new job and report back on the change.

Visit [http://localhost:8080/dashboard/self](http://localhost:8080/dashboard/self) and open the change you just uploaded. If the build is complete, Zuul should have left a Verified: +1 vote on the change, along with a comment at the bottom. Expand the comments and you should see that the job succeeded, and a link to the build result in Zuul is provided. You can follow that link to see some information about the build, but you won’t find any logs since Zuul hasn’t been told where to save them yet.

![Image 36: ../_images/check1-1002.png](https://zuul-ci.org/docs/zuul/latest/_images/check1-1002.png)
This means everything is working so far, but we need to configure a bit more before we have a useful job.

Configure a Base Job[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#configure-a-base-job "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Every Zuul tenant needs at least one base job. Zuul administrators can use a base job to customize Zuul to the local environment. This may include tasks which run both before jobs, such as setting up package mirrors or networking configuration, or after jobs, such as artifact and log storage.

Zuul doesn’t take anything for granted, and even tasks such as copying the git repos for the project being tested onto the remote node must be explicitly added to a base job (and can therefore be customized as needed). The Zuul in this tutorial is pre-configured to use the [zuul jobs](https://zuul-ci.org/docs/zuul-jobs/) repository which is the “standard library” of Zuul jobs and roles. We will make use of it to quickly create a base job which performs the necessary set up actions and stores build logs.

Return to the `zuul-config` repo that you were working in earlier. We’re going to add some playbooks to the empty base job we created earlier. Start by creating a directory to store those playbooks:

cd ..
cd zuul-config
mkdir -p playbooks/base

Zuul supports running any number of playbooks before a job (called _pre-run_ playbooks) or after a job (called _post-run_ playbooks). We’re going to add a single _pre-run_ playbook now. Copy the following to `playbooks/base/pre.yaml`:

- hosts: all
 roles:
 - add-build-sshkey
 - prepare-workspace-git

This playbook does two things; first it creates a new SSH key and adds it to all of the hosts in the inventory, and removes the private key that Zuul normally uses to log into nodes from the running SSH agent. This is just an extra bit of protection which ensures that if Zuul’s SSH key has access to any important systems, normal Zuul jobs can’t use it. The second thing the playbook does is copy the git repositories that Zuul has prepared (which may have one or more changes being tested) to all of the nodes used in the job.

Next, add a _post-run_ playbook to remove the per-build SSH key. Copy the following to `playbooks/base/cleanup.yaml`:

- hosts: all
 roles:
 - remove-build-sshkey

This is the complement of the add-build-sshkey role in the pre-run playbook – it simply removes the per-build ssh key from any remote systems. Zuul always tries to run all of the post-run playbooks regardless of whether any previous playbooks have failed. Marking this _post-run_ playbook as a cleanup playbook also ensures it will run if the job is aborted for some reason.

Because we always want log collection to run and we want it to run last, we create a second post-run playbook for it. Copy the following to `playbooks/base/post-logs.yaml`:

- hosts: localhost
 gather_facts: False
 roles:
 - generate-zuul-manifest
 - role: upload-logs
 zuul_log_url: "http://localhost:8000"

The first role in this playbook generates some metadata about the logs which are about to be uploaded. Zuul uses this metadata in its web interface to nicely render the logs and other information about the build.

This tutorial is running an Apache webserver in a container which will serve build logs from a volume that is shared with the Zuul executor. That volume is mounted at /srv/static/logs, which is the default location in the [upload-logs](https://zuul-ci.org/docs/zuul-jobs/roles.html#role-upload-logs) role. The role also supports copying files to a remote server via SCP; see the role documentation for how to configure it. For this simple case, the only option we need to provide is the URL where the logs can ultimately be found.

Note

Zuul-jobs also contains [roles](https://zuul-ci.org/docs/zuul-jobs/log-roles.html) to upload logs to a OpenStack Object Storage (swift) or Google Cloud Storage containers. If you create a role to upload logs to another system, please feel free to contribute it to the zuul-jobs repository for others to use.

Now that the new playbooks are in place, update the `base` job definition to include them. Overwrite `zuul.d/jobs.yaml` with the following:

- job:
 name: base
 parent: null
 description: |
 The recommended base job.

 All jobs ultimately inherit from this. It runs a pre-playbook
 which copies all of the job's prepared git repos on to all of
 the nodes in the nodeset.

 It also sets a default timeout value (which may be overidden).
 pre-run: playbooks/base/pre.yaml
 post-run:
 - name: playbooks/base/cleanup.yaml
 cleanup: true
 - playbooks/base/post-logs.yaml
 roles:
 - zuul: zuul/zuul-jobs
 timeout: 1800
 nodeset:
 nodes:
 - name: ubuntu-jammy
 label: ubuntu-jammy

Then commit the change and upload it to Gerrit for review:

git add playbooks zuul.d/jobs.yaml
git commit -m "Update Zuul base job"
git review

Visit [http://localhost:8080/dashboard/self](http://localhost:8080/dashboard/self) and open the `zuul-config` change you just uploaded.

You should see a Verified +1 vote from Zuul. Click Reply then vote Code-Review: +2 and Workflow: +1 then click Send.

![Image 37: ../_images/review-1003.png](https://zuul-ci.org/docs/zuul/latest/_images/review-1003.png)
Wait a few moments for Zuul to process the event, and then reload the page. The change should have been merged.

Visit [http://localhost:8080/dashboard/self](http://localhost:8080/dashboard/self) and return to the `test1` change you uploaded earlier. Click Reply then type recheck into the text field and click Send.

![Image 38: ../_images/recheck-1002.png](https://zuul-ci.org/docs/zuul/latest/_images/recheck-1002.png)
This will cause Zuul to re-run the test job we created earlier. This time it will run with the updated base job configuration, and when complete, it will report the published log location as a comment on the change:

![Image 39: ../_images/check2-1002.png](https://zuul-ci.org/docs/zuul/latest/_images/check2-1002.png)
Follow the link and you will be directed to the build result page. If you click on the Logs tab, you’ll be able to browse the console log for the job. In the middle of the log, you should see the “Hello, world!” output from the job’s playbook.

Also try the Console tab for a more structured view of the log. Click on the OK button in the middle of the page to see the output of just the task we’re interested in.

Further Steps[](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html#further-steps "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

You now have a Zuul system up and running, congratulations!

The Zuul community would love to hear about how you plan to use Zuul. Please take a few moments to fill out the [Zuul User Survey](https://www.surveymonkey.com/r/K2B2MWL) to provide feedback and information around your deployment. All information is confidential to the OpenStack Foundation unless you designate that it can be public.

If you would like to make further changes to Zuul, its configuration files are located in the `zuul/doc/source/examples` directory and are bind-mounted into the running containers. You may edit them and restart the Zuul containers to make changes.

If you would like to connect your Zuul to GitHub, see [GitHub](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-driver).

[Previous](https://zuul-ci.org/docs/zuul/latest/gating.html "Project Gating")[Next](https://zuul-ci.org/docs/zuul/latest/project-config.html "Project Configuration")

* * *

© Copyright 2012-2026, Zuul project contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

Versions v: latest 

[latest](https://zuul-ci.org/docs/zuul/latest/)[14.0.0](https://zuul-ci.org/docs/zuul/14.0.0/)[13.1.1](https://zuul-ci.org/docs/zuul/13.1.1/)[13.1.0](https://zuul-ci.org/docs/zuul/13.1.0/)[13.0.1](https://zuul-ci.org/docs/zuul/13.0.1/)[13.0.0](https://zuul-ci.org/docs/zuul/13.0.0/)[12.1.0](https://zuul-ci.org/docs/zuul/12.1.0/)[12.0.0](https://zuul-ci.org/docs/zuul/12.0.0/)[11.3.0](https://zuul-ci.org/docs/zuul/11.3.0/)[11.2.0](https://zuul-ci.org/docs/zuul/11.2.0/)[11.1.0](https://zuul-ci.org/docs/zuul/11.1.0/)[11.0.1](https://zuul-ci.org/docs/zuul/11.0.1/)[11.0.0](https://zuul-ci.org/docs/zuul/11.0.0/)[10.2.0](https://zuul-ci.org/docs/zuul/10.2.0/)[10.1.0](https://zuul-ci.org/docs/zuul/10.1.0/)[10.0.0](https://zuul-ci.org/docs/zuul/10.0.0/)[9.5.0](https://zuul-ci.org/docs/zuul/9.5.0/)[9.4.0](https://zuul-ci.org/docs/zuul/9.4.0/)[9.3.0](https://zuul-ci.org/docs/zuul/9.3.0/)[9.2.0](https://zuul-ci.org/docs/zuul/9.2.0/)[9.1.0](https://zuul-ci.org/docs/zuul/9.1.0/)[9.0.0](https://zuul-ci.org/docs/zuul/9.0.0/)[8.3.1](https://zuul-ci.org/docs/zuul/8.3.1/)[8.3.0](https://zuul-ci.org/docs/zuul/8.3.0/)[8.2.0](https://zuul-ci.org/docs/zuul/8.2.0/)[8.1.0](https://zuul-ci.org/docs/zuul/8.1.0/)[8.0.1](https://zuul-ci.org/docs/zuul/8.0.1/)[8.0.0](https://zuul-ci.org/docs/zuul/8.0.0/)[7.1.0](https://zuul-ci.org/docs/zuul/7.1.0/)[7.0.0](https://zuul-ci.org/docs/zuul/7.0.0/)[6.4.0](https://zuul-ci.org/docs/zuul/6.4.0/)[6.3.0](https://zuul-ci.org/docs/zuul/6.3.0/)[6.2.0](https://zuul-ci.org/docs/zuul/6.2.0/)[6.1.0](https://zuul-ci.org/docs/zuul/6.1.0/)[6.0.0](https://zuul-ci.org/docs/zuul/6.0.0/)[5.2.5](https://zuul-ci.org/docs/zuul/5.2.5/)[5.2.4](https://zuul-ci.org/docs/zuul/5.2.4/)[5.2.3](https://zuul-ci.org/docs/zuul/5.2.3/)[5.2.2](https://zuul-ci.org/docs/zuul/5.2.2/)[5.2.1](https://zuul-ci.org/docs/zuul/5.2.1/)[5.2.0](https://zuul-ci.org/docs/zuul/5.2.0/)[5.1.0](https://zuul-ci.org/docs/zuul/5.1.0/)[5.0.0](https://zuul-ci.org/docs/zuul/5.0.0/)[4.12.0](https://zuul-ci.org/docs/zuul/4.12.0/)[4.11.0](https://zuul-ci.org/docs/zuul/4.11.0/)[4.10.4](https://zuul-ci.org/docs/zuul/4.10.4/)[4.10.3](https://zuul-ci.org/docs/zuul/4.10.3/)[4.10.2](https://zuul-ci.org/docs/zuul/4.10.2/)[4.10.1](https://zuul-ci.org/docs/zuul/4.10.1/)[4.10.0](https://zuul-ci.org/docs/zuul/4.10.0/)[4.9.0](https://zuul-ci.org/docs/zuul/4.9.0/)[4.8.1](https://zuul-ci.org/docs/zuul/4.8.1/)[4.8.0](https://zuul-ci.org/docs/zuul/4.8.0/)[4.7.0](https://zuul-ci.org/docs/zuul/4.7.0/)[4.6.0](https://zuul-ci.org/docs/zuul/4.6.0/)[4.5.1](https://zuul-ci.org/docs/zuul/4.5.1/)[4.5.0](https://zuul-ci.org/docs/zuul/4.5.0/)[4.4.0](https://zuul-ci.org/docs/zuul/4.4.0/)[4.3.0](https://zuul-ci.org/docs/zuul/4.3.0/)[4.2.0](https://zuul-ci.org/docs/zuul/4.2.0/)[4.1.0](https://zuul-ci.org/docs/zuul/4.1.0/)[4.0.0](https://zuul-ci.org/docs/zuul/4.0.0/)[3.19.1](https://zuul-ci.org/docs/zuul/3.19.1/)[3.19.0](https://zuul-ci.org/docs/zuul/3.19.0/)[3.18.0](https://zuul-ci.org/docs/zuul/3.18.0/)[3.17.0](https://zuul-ci.org/docs/zuul/3.17.0/)[3.16.1](https://zuul-ci.org/docs/zuul/3.16.1/)[3.16.0](https://zuul-ci.org/docs/zuul/3.16.0/)[3.15.0](https://zuul-ci.org/docs/zuul/3.15.0/)[3.14.0](https://zuul-ci.org/docs/zuul/3.14.0/)[3.13.0](https://zuul-ci.org/docs/zuul/3.13.0/)[3.12.0](https://zuul-ci.org/docs/zuul/3.12.0/)[3.11.1](https://zuul-ci.org/docs/zuul/3.11.1/)[3.11.0](https://zuul-ci.org/docs/zuul/3.11.0/)[3.10.2](https://zuul-ci.org/docs/zuul/3.10.2/)[3.10.1](https://zuul-ci.org/docs/zuul/3.10.1/)[3.10.0](https://zuul-ci.org/docs/zuul/3.10.0/)[3.9.0](https://zuul-ci.org/docs/zuul/3.9.0/)[3.8.1](https://zuul-ci.org/docs/zuul/3.8.1/)[3.8.0](https://zuul-ci.org/docs/zuul/3.8.0/)[3.7.1](https://zuul-ci.org/docs/zuul/3.7.1/)[3.7.0](https://zuul-ci.org/docs/zuul/3.7.0/)[3.6.1](https://zuul-ci.org/docs/zuul/3.6.1/)[3.6.0](https://zuul-ci.org/docs/zuul/3.6.0/)[3.5.0](https://zuul-ci.org/docs/zuul/3.5.0/)[3.4.0](https://zuul-ci.org/docs/zuul/3.4.0/)[3.3.1](https://zuul-ci.org/docs/zuul/3.3.1/)[3.3.0](https://zuul-ci.org/docs/zuul/3.3.0/)
