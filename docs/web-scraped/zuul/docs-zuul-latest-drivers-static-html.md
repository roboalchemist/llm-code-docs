# Source: https://zuul-ci.org/docs/zuul/latest/drivers/static.html

Title: Static — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/static.html

Published Time: Wed, 11 Mar 2026 16:34:26 GMT

Markdown Content:
Static — Zuul documentation
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

        *   [Static](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#)
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
*   [Drivers](https://zuul-ci.org/docs/zuul/latest/drivers/index.html)
*   Static
*   [View page source](https://zuul-ci.org/docs/zuul/latest/_sources/drivers/static.rst.txt)

* * *

Static[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#static "Link to this heading")
=================================================================================================

Zuul can use statically defined nodes as a source for build nodes. These can be real hardware or virtual machines that are managed externally to Zuul.

To add static nodes to a provider in Zuul, use the [provider[static].nodes](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes "attr-provider[static].nodes") attribute.

Static nodes in Zuul have persistent node ids that are determined based on their connection information. This means the same node ID is used for every build on a given static node.

Warning

There is no restriction that would prohibit users in multiple tenants from configuring the same static nodes. If static nodes should only be used by users of certain tenants, you may wish to configure the static node to only accept a [Tenant Key](https://zuul-ci.org/docs/zuul/latest/job-content.html#tenant-key) in order to restrict access.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#connection-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The connection configuration for the static driver is not used to provide any settings or information to Zuul, but a connection is nonetheless required in order to enable the functionality.

The only supported option in `zuul.conf` connections is:

<static connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-%3Cstatic%20connection%3E "Link to this definition")

<static connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-%3Cstatic%20connection%3E.driver "Link to this definition")

static[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-%3Cstatic%20connection%3E.driver.static "Link to this definition")
The connection must set `driver=static` for a static connection.

Provider Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#provider-configuration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

The `static` driver adds the following options to the [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider") and [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") configurations:

provider[static][](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static] "Link to this definition")

Type:_dict_

The attributes available for configuring a static provider are below.

provider[static].abstract[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].abstract "Link to this definition")

Default:`False`

Type:_bool_

Whether a section is intended to be inherited by another [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") or a [provider](https://zuul-ci.org/docs/zuul/latest/config/provider.html#attr-provider "attr-provider"). This setting is currently unused (but may be used in the future). If a section is used to provide common values to other sections, set this to true. Otherwise, the default of false indicates that the section should be referenced directly by providers.

provider[static].connection[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].connection "Link to this definition")

Type:_str_

The name of the [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) to use. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects and may not be changed via inheritance.

provider[static].flavor-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavor-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any flavor used with this provider. Many attributes which may be set on an individual flavor may be set once in this section and used for all the flavors in this provider. Values set on individual flavors may still override the values set here.

provider[static].flavor-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavor-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavor-defaults.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavor-defaults.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavor-defaults.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[static].flavors[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavors "Link to this definition")

Type:_dict_

A list of flavors associated with this provider.

provider[static].flavors.description[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavors.description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[static].flavors.final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavors.final "Link to this definition")

Default:`False`

Whether the configuration of the flavor may be updated by values in flavor-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavors.final.true "Link to this definition")
The flavor may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavors.final.false "Link to this definition")
The flavor may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].flavors.final.allow-override "Link to this definition")
The flavor may not be updated by flavor-defaults but may be explicitly overidden by redefining it in a new ‘flavor’ entry.

provider[static].flavors.name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].flavors.name "Link to this definition")

Type:_str_

The name of the flavor. Used to refer to the flavor in Zuul configuration.

provider[static].image-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any image used with this provider. Many attributes which may be set on an individual image may be set once in this section and used for all the images in this provider. Values set on individual images may still override the values set here.

provider[static].image-defaults.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[static].image-defaults.connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.connection-type.ssh "Link to this definition")
An ssh connection.

provider[static].image-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[static].image-defaults.import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[static].image-defaults.python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[static].image-defaults.shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[static].image-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[static].image-defaults.upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].image-defaults.upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[static].image-defaults.username[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].image-defaults.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[static].images[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images "Link to this definition")

Type:_list_

A list of images associated with this provider.

provider[static].images[cloud][](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud] "Link to this definition")

Type:_dict_

These are the attributes available for a cloud image.

provider[static].images[cloud].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[static].images[cloud].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].connection-type.ssh "Link to this definition")
An ssh connection.

provider[static].images[cloud].description[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[static].images[cloud].final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[static].images[cloud].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[static].images[cloud].name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[static].images[cloud].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[static].images[cloud].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[static].images[cloud].type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].type "Link to this definition")

The type of image.

cloud[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[cloud].type.cloud "Link to this definition")
An existing image available in the cloud.

provider[static].images[cloud].username[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[cloud].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[static].images[zuul][](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul] "Link to this definition")

Type:_dict_

These are the attributes available for a Zuul image.

provider[static].images[zuul].connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[static].images[zuul].connection-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].connection-type "Link to this definition")

The connection type that a consumer should use when connecting to the node.

winrm[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].connection-type.winrm "Link to this definition")
A winrm connection.

ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].connection-type.ssh "Link to this definition")
An ssh connection.

provider[static].images[zuul].description[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].description "Link to this definition")

Type:_str_

A textual description of the image for reference purposes.

provider[static].images[zuul].final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[static].images[zuul].import-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].import-timeout "Link to this definition")

Default:`300`

Type:_int_

The limit on the amount of time a successful image import can take.

provider[static].images[zuul].name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].name "Link to this definition")

Type:_str_

The name of the image. Used to refer to the image in Zuul configuration.

provider[static].images[zuul].python-path[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].python-path "Link to this definition")

Type:_str_

The path of the default python interpreter. Used by Zuul to set `ansible_python_interpreter`. The special value `auto` will direct Zuul to use inbuilt Ansible logic to select the interpreter.

provider[static].images[zuul].shell-type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].shell-type "Link to this definition")

Type:_str_

The shell type of the node’s default shell executable. Used by Zuul to set `ansible_shell_type`. This setting should only be used

*   For a windows image with the experimental connection-type`ssh` in which case `cmd` or `powershell` should be set and reflect the node’s `DefaultShell` configuration.

*   If the default shell is not Bourne compatible (sh), but instead e.g. `csh` or `fish`, and the user is aware that there is a long-standing issue with `ansible_shell_type` in combination with `become`.

provider[static].images[zuul].tags[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to uploaded images, and to nodes created from them. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[static].images[zuul].type[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].type "Link to this definition")

The type of image.

zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].type.zuul "Link to this definition")
An image managed by Zuul.

provider[static].images[zuul].upload-methods[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].upload-methods "Link to this definition")

Default:`['copy', 'import', 'upload']`

Type:_list_

An ordered list of methods to use when creating an image in the provider.

copy[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].upload-methods.copy "Link to this definition")
Copy the image from another provider if available.

import[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].upload-methods.import "Link to this definition")
Import the image directly from its storage location.

upload[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].images[zuul].upload-methods.upload "Link to this definition")
Download the image from its storage location and upload it to the provider.

provider[static].images[zuul].username[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].images[zuul].username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[static].label-defaults[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults "Link to this definition")

Type:_dict_

Attributes to be set as default values for any label used with this provider. Many attributes which may be set on an individual label may be set once in this section and used for all the labels in this provider. Values set on individual labels may still override the values set here.

provider[static].label-defaults.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[static].label-defaults.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[static].label-defaults.final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].label-defaults.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].label-defaults.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].label-defaults.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[static].label-defaults.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[static].label-defaults.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[static].label-defaults.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[static].label-defaults.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[static].label-defaults.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[static].label-defaults.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[static].label-defaults.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[static].label-defaults.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[static].label-defaults.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[static].label-defaults.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].label-defaults.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[static].labels[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels "Link to this definition")

Type:_dict_

A list of labels associated with this provider.

provider[static].labels.boot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.boot-timeout "Link to this definition")

Default:`300`

Type:_int_

The time (in seconds) to wait for a node to boot.

provider[static].labels.description[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.description "Link to this definition")

Type:_str_

A textual description of the label for reference purposes.

provider[static].labels.executor-zone[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.executor-zone "Link to this definition")

Type:_str_

Specify that a Zuul executor in the specified zone is used to run jobs with nodes from this label.

provider[static].labels.final[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.final "Link to this definition")

Default:`False`

Whether the configuration of the label may be updated by values in label-defaults or overidden with a new definition by sections or providers lower in the hierarchy than the point at which the final attribute is applied.

True[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].labels.final.true "Link to this definition")
The label may not be updated or overidden.

False[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].labels.final.false "Link to this definition")
The label may be updated or overidden.

allow-override[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#value-provider[static].labels.final.allow-override "Link to this definition")
The label may not be updated by label-defaults but may be explicitly overidden by redefining it in a new ‘label’ entry.

provider[static].labels.flavor[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.flavor "Link to this definition")

Type:_str_

The flavor to use with this label.

provider[static].labels.host-key-checking[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.host-key-checking "Link to this definition")

Default:`True`

Type:_bool_

Whether to validate SSH host keys. When true, this helps ensure that nodes are ready to receive SSH connections before they are used. When set to false, Zuul will not attempt to ssh-keyscan nodes after they are booted. Disable this if the zuul-launcher and the nodes it launches are on different networks, where the launcher is unable to reach the nodes directly.

provider[static].labels.image[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.image "Link to this definition")

Type:_str_

The image to use with this label.

provider[static].labels.key-name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.key-name "Link to this definition")

Type:_str_

The name of a keypair that will be used when booting the node.

provider[static].labels.max-age[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.max-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since creation that a node may be available for use. Ready nodes older than this time will be deleted.

provider[static].labels.max-ready-age[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.max-ready-age "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) an unassigned node should stay in ready state.

provider[static].labels.min-retention-time[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.min-retention-time "Link to this definition")

Default:`0`

Type:_int_

The time (in seconds) since an instance was launched, during which a node will not be deleted. For node resources with minimum billing times, this can be used to ensure that the instance is retained for at least the minimum billing interval.

This setting takes precedence over max-[ready-]age.

provider[static].labels.name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.name "Link to this definition")

Type:_str_

The name of the label. Used to refer to the label in Zuul configuration.

provider[static].labels.reuse[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.reuse "Link to this definition")

Default:`False`

Type:_bool_

Should the node be reused (True) or deleted (False) after use.

provider[static].labels.slots[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.slots "Link to this definition")

Default:`1`

Type:_int_

How many jobs are permitted run on the same node simultaneously.

provider[static].labels.snapshot-expiration[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.snapshot-expiration "Link to this definition")

Default:`604800`

Type:_int_

The time (in seconds) until a snapshot expires.

provider[static].labels.snapshot-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.snapshot-timeout "Link to this definition")

Default:`3600`

Type:_int_

The time (in seconds) to wait for a snapshot to complete.

provider[static].labels.tags[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].labels.tags "Link to this definition")

Type:_dict_

A dictionary of tags to add to nodes. Avoid the use of zuul_ as a key prefix since Zuul uses this for internal values.

provider[static].launch-attempts[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].launch-attempts "Link to this definition")

Default:`3`

Type:_int_

The number of times to attempt launching a node before considering the request failed.

provider[static].launch-timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].launch-timeout "Link to this definition")

Type:_int_

The time to wait from issuing the command to create a new node until the node is reporting as running. If the timeout is exceeded, the node launch is aborted and the node deleted.

provider[static].name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].name "Link to this definition")

Type:_str_

The name of the provider. Used to refer to the provider in Zuul configuration.

provider[static].nodes[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes "Link to this definition")

Type:_dict_

A list of nodes to be used by this provider.

provider[static].nodes.aliases[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.aliases "Link to this definition")

Type:_str_

A list of label aliases to associate with this node. These labels may be used to request this node, but none of their attributes will be used to define characteristics.

provider[static].nodes.connection-port[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.connection-port "Link to this definition")

Type:_int_

The port that Zuul should use when connecting to the node. For most nodes this is not necessary. This defaults to 22 when `connection-type` is ‘ssh’ and 5986 when it is ‘winrm’.

provider[static].nodes.host-key[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.host-key "Link to this definition")

Type:_str_

The ssh host key of the node.

provider[static].nodes.label[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.label "Link to this definition")

Type:_str_

The label to associate with this node. This is the primary label for the node and will be used to supply any necessary information about the node’s characteristics.

provider[static].nodes.name[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.name "Link to this definition")

Type:_str_

The hostname or ip address of the static node.

provider[static].nodes.username[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].nodes.username "Link to this definition")

Type:_str_

The username Zuul should use when connecting to the node.

provider[static].parent[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].parent "Link to this definition")

Type:_str_

The name of the parent section from which to inherit. This attribute is only used by [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") objects. To indicate which section a provider should be attached to, use [provider[static].section](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].section "attr-provider[static].section")

provider[static].resource-limits[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].resource-limits "Link to this definition")

Type:_dict_

Resource limits for this provider.

provider[static].resource-limits.instances[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].resource-limits.instances "Link to this definition")

Type:_int_

The number of instances.

provider[static].section[](https://zuul-ci.org/docs/zuul/latest/drivers/static.html#attr-provider[static].section "Link to this definition")

Type:_str_

The name of the [section](https://zuul-ci.org/docs/zuul/latest/config/section.html#attr-section "attr-section") from which to inherit.

[Previous](https://zuul-ci.org/docs/zuul/latest/drivers/openstack.html "OpenStack")[Next](https://zuul-ci.org/docs/zuul/latest/tenants.html "Tenant Configuration")

* * *

© Copyright 2012-2026, Zuul project contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

Versions v: latest 

[latest](https://zuul-ci.org/docs/zuul/latest/)[14.0.0](https://zuul-ci.org/docs/zuul/14.0.0/)[13.1.1](https://zuul-ci.org/docs/zuul/13.1.1/)[13.1.0](https://zuul-ci.org/docs/zuul/13.1.0/)[13.0.1](https://zuul-ci.org/docs/zuul/13.0.1/)[13.0.0](https://zuul-ci.org/docs/zuul/13.0.0/)[12.1.0](https://zuul-ci.org/docs/zuul/12.1.0/)[12.0.0](https://zuul-ci.org/docs/zuul/12.0.0/)[11.3.0](https://zuul-ci.org/docs/zuul/11.3.0/)[11.2.0](https://zuul-ci.org/docs/zuul/11.2.0/)[11.1.0](https://zuul-ci.org/docs/zuul/11.1.0/)[11.0.1](https://zuul-ci.org/docs/zuul/11.0.1/)[11.0.0](https://zuul-ci.org/docs/zuul/11.0.0/)[10.2.0](https://zuul-ci.org/docs/zuul/10.2.0/)[10.1.0](https://zuul-ci.org/docs/zuul/10.1.0/)[10.0.0](https://zuul-ci.org/docs/zuul/10.0.0/)[9.5.0](https://zuul-ci.org/docs/zuul/9.5.0/)[9.4.0](https://zuul-ci.org/docs/zuul/9.4.0/)[9.3.0](https://zuul-ci.org/docs/zuul/9.3.0/)[9.2.0](https://zuul-ci.org/docs/zuul/9.2.0/)[9.1.0](https://zuul-ci.org/docs/zuul/9.1.0/)[9.0.0](https://zuul-ci.org/docs/zuul/9.0.0/)[8.3.1](https://zuul-ci.org/docs/zuul/8.3.1/)[8.3.0](https://zuul-ci.org/docs/zuul/8.3.0/)[8.2.0](https://zuul-ci.org/docs/zuul/8.2.0/)[8.1.0](https://zuul-ci.org/docs/zuul/8.1.0/)[8.0.1](https://zuul-ci.org/docs/zuul/8.0.1/)[8.0.0](https://zuul-ci.org/docs/zuul/8.0.0/)[7.1.0](https://zuul-ci.org/docs/zuul/7.1.0/)[7.0.0](https://zuul-ci.org/docs/zuul/7.0.0/)[6.4.0](https://zuul-ci.org/docs/zuul/6.4.0/)[6.3.0](https://zuul-ci.org/docs/zuul/6.3.0/)[6.2.0](https://zuul-ci.org/docs/zuul/6.2.0/)[6.1.0](https://zuul-ci.org/docs/zuul/6.1.0/)[6.0.0](https://zuul-ci.org/docs/zuul/6.0.0/)[5.2.5](https://zuul-ci.org/docs/zuul/5.2.5/)[5.2.4](https://zuul-ci.org/docs/zuul/5.2.4/)[5.2.3](https://zuul-ci.org/docs/zuul/5.2.3/)[5.2.2](https://zuul-ci.org/docs/zuul/5.2.2/)[5.2.1](https://zuul-ci.org/docs/zuul/5.2.1/)[5.2.0](https://zuul-ci.org/docs/zuul/5.2.0/)[5.1.0](https://zuul-ci.org/docs/zuul/5.1.0/)[5.0.0](https://zuul-ci.org/docs/zuul/5.0.0/)[4.12.0](https://zuul-ci.org/docs/zuul/4.12.0/)[4.11.0](https://zuul-ci.org/docs/zuul/4.11.0/)[4.10.4](https://zuul-ci.org/docs/zuul/4.10.4/)[4.10.3](https://zuul-ci.org/docs/zuul/4.10.3/)[4.10.2](https://zuul-ci.org/docs/zuul/4.10.2/)[4.10.1](https://zuul-ci.org/docs/zuul/4.10.1/)[4.10.0](https://zuul-ci.org/docs/zuul/4.10.0/)[4.9.0](https://zuul-ci.org/docs/zuul/4.9.0/)[4.8.1](https://zuul-ci.org/docs/zuul/4.8.1/)[4.8.0](https://zuul-ci.org/docs/zuul/4.8.0/)[4.7.0](https://zuul-ci.org/docs/zuul/4.7.0/)[4.6.0](https://zuul-ci.org/docs/zuul/4.6.0/)[4.5.1](https://zuul-ci.org/docs/zuul/4.5.1/)[4.5.0](https://zuul-ci.org/docs/zuul/4.5.0/)[4.4.0](https://zuul-ci.org/docs/zuul/4.4.0/)[4.3.0](https://zuul-ci.org/docs/zuul/4.3.0/)[4.2.0](https://zuul-ci.org/docs/zuul/4.2.0/)[4.1.0](https://zuul-ci.org/docs/zuul/4.1.0/)[4.0.0](https://zuul-ci.org/docs/zuul/4.0.0/)[3.19.1](https://zuul-ci.org/docs/zuul/3.19.1/)[3.19.0](https://zuul-ci.org/docs/zuul/3.19.0/)[3.18.0](https://zuul-ci.org/docs/zuul/3.18.0/)[3.17.0](https://zuul-ci.org/docs/zuul/3.17.0/)[3.16.1](https://zuul-ci.org/docs/zuul/3.16.1/)[3.16.0](https://zuul-ci.org/docs/zuul/3.16.0/)[3.15.0](https://zuul-ci.org/docs/zuul/3.15.0/)[3.14.0](https://zuul-ci.org/docs/zuul/3.14.0/)[3.13.0](https://zuul-ci.org/docs/zuul/3.13.0/)[3.12.0](https://zuul-ci.org/docs/zuul/3.12.0/)[3.11.1](https://zuul-ci.org/docs/zuul/3.11.1/)[3.11.0](https://zuul-ci.org/docs/zuul/3.11.0/)[3.10.2](https://zuul-ci.org/docs/zuul/3.10.2/)[3.10.1](https://zuul-ci.org/docs/zuul/3.10.1/)[3.10.0](https://zuul-ci.org/docs/zuul/3.10.0/)[3.9.0](https://zuul-ci.org/docs/zuul/3.9.0/)[3.8.1](https://zuul-ci.org/docs/zuul/3.8.1/)[3.8.0](https://zuul-ci.org/docs/zuul/3.8.0/)[3.7.1](https://zuul-ci.org/docs/zuul/3.7.1/)[3.7.0](https://zuul-ci.org/docs/zuul/3.7.0/)[3.6.1](https://zuul-ci.org/docs/zuul/3.6.1/)[3.6.0](https://zuul-ci.org/docs/zuul/3.6.0/)[3.5.0](https://zuul-ci.org/docs/zuul/3.5.0/)[3.4.0](https://zuul-ci.org/docs/zuul/3.4.0/)[3.3.1](https://zuul-ci.org/docs/zuul/3.3.1/)[3.3.0](https://zuul-ci.org/docs/zuul/3.3.0/)
