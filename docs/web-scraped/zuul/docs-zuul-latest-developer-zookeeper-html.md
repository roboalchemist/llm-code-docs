# Source: https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html

Title: ZooKeeper — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html

Published Time: Wed, 11 Mar 2026 16:34:20 GMT

Markdown Content:
ZooKeeper — Zuul documentation
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

    *   [ZooKeeper](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#)
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
*   [Developer’s Guide](https://zuul-ci.org/docs/zuul/latest/developer/index.html)
*   ZooKeeper
*   [View page source](https://zuul-ci.org/docs/zuul/latest/_sources/developer/zookeeper.rst.txt)

* * *

ZooKeeper[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#zookeeper "Link to this heading")
============================================================================================================

Overview[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#overview "Link to this heading")
----------------------------------------------------------------------------------------------------------

Zuul has a microservices architecture with the goal of no single point of failure in mind.

Zuul is an event driven system with several event loops that interact with each other:

*   Driver event loop: Drivers like GitHub or Gerrit have their own event loops. They perform preprocessing of the received events and add events into the scheduler event loop.

*   Scheduler event loop: This event loop processes the pipelines and reconfigurations.

Each of these event loops persists data in ZooKeeper so that other components can share or resume processing.

A key aspect of scalability is maintaining an event queue per pipeline. This makes it easy to process several pipelines in parallel. A new driver event is first processed in the driver event queue. This adds a new event into the scheduler event queue. The scheduler event queue then checks which pipeline may be interested in this event according to the tenant configuration and layout. Based on this the event is dispatched to all matching pipeline queues.

In order to make reconfigurations efficient we store the parsed branch config in Zookeeper. This makes it possible to create the current layout without the need to ask the mergers multiple times for the configuration. This is used by zuul-web to keep an up-to-date layout for API requests.

We store the pipeline state in Zookeeper. This contains the complete information about queue items, jobs and builds, as well as a separate abbreviated state for quick access by zuul-web for the status page.

Driver Event Ingestion[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#driver-event-ingestion "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

There are three types of event receiving mechanisms in Zuul:

*   Active event gathering: The connection actively listens to events (Gerrit) or generates them itself (git, timer, zuul)

*   Passive event gathering: The events are sent to Zuul from outside (GitHub webhooks)

*   Internal event generation: The events are generated within Zuul itself and typically get injected directly into the scheduler event loop.

The active event gathering needs to be handled differently from passive event gathering.

### Active Event Gathering[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#active-event-gathering "Link to this heading")

This is mainly done by the Gerrit driver. We actively maintain a connection to the target and receive events. We utilize a leader election to make sure there is exactly one instance receiving the events.

### Passive Event Gathering[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#passive-event-gathering "Link to this heading")

In case of passive event gathering the events are sent to Zuul typically via webhooks. These types of events are received in zuul-web which then stores them in Zookeeper. This type of event gathering is used by GitHub and other drivers. In this case we can have multiple instances but still receive only one event so that we don’t need to take special care of event deduplication or leader election. Multiple instances behind a load balancer are safe to use and recommended for such passive event gathering.

Configuration Storage[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#configuration-storage "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Zookeeper is not designed as a database with a large amount of data, so we should store as little as possible in zookeeper. Thus we only store the per project-branch unparsed config in zookeeper. From this, every part of Zuul, like the scheduler or zuul-web, can quickly recalculate the layout of each tenant and keep it up to date by watching for changes in the unparsed project-branch-config.

We store the actual config sharded in multiple nodes, and those nodes are stored under per project and branch znodes. This is needed because of the 1MB limit per znode in zookeeper. It further makes it less expensive to cache the global config in each component as this cache is updated incrementally.

Executor and Merger Queues[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#executor-and-merger-queues "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

The executors and mergers each have an execution queue (and in the case of executors, optionally per-zone queues). This makes it easy for executors and mergers to simply pick the next job to run without needing to inspect the entire pipeline state. The scheduler is responsible for submitting job requests as the state changes.

Zookeeper Map[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#zookeeper-map "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

This is a reference for object layout in Zookeeper.

/zuul[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul "Link to this definition")

All ephemeral data stored here. Remove the entire tree to “reset” the system.

/zuul/cache/connection/<connection>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E "Link to this definition")

The connection cache root. Each connection has a dedicated space for its caches. Two types of caches are currently implemented: change and branch.

/zuul/cache/connection/<connection>/branches[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E/branches "Link to this definition")

The connection branch cache root. Contains the cache itself and a lock.

/zuul/cache/connection/<connection>/branches/data[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E/branches/data "Link to this definition")

Type:_BranchCacheZKObject(sharded)_

The connection branch cache data. This is a single sharded JSON blob.

/zuul/cache/connection/<connection>/branches/lock[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E/branches/lock "Link to this definition")

Type:_RWLock_

The connection branch cache read/write lock.

/zuul/cache/connection/<connection>/cache[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E/cache "Link to this definition")

The connection change cache. Each node under this node is an entry in the change cache. The node ID is a sha256 of the cache key, the contents are the JSON serialization of the cache entry metadata. One of the included items is the data_uuid which is used to retrieve the actual change data.

When a cache entry is updated, a new data node is created without deleting the old data node. They are eventually garbage collected.

/zuul/cache/connection/<connection>/data[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/connection/%3Cconnection%3E/data "Link to this definition")

Data for the change cache. These nodes are identified by a UUID referenced from the cache entries.

These are sharded JSON blobs of the change data.

/zuul/cache/blob/data[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/blob/data "Link to this definition")

Data for the blob store. These nodes are identified by a sha256sum of the secret content.

These are sharded blobs of data.

/zuul/cache/blob/lock[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cache/blob/lock "Link to this definition")

Side-channel lock directory for the blob store. The store locks by key id under this znode when writing.

/zuul/cleanup[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup "Link to this definition")

This node holds locks for the cleanup routines to make sure that only one scheduler runs them at a time.

/zuul/cleanup/build_requests[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/build_requests "Link to this definition")

/zuul/cleanup/connection[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/connection "Link to this definition")

/zuul/cleanup/general[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/general "Link to this definition")

/zuul/cleanup/merge_requests[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/merge_requests "Link to this definition")

/zuul/cleanup/node_request[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/node_request "Link to this definition")

/zuul/cleanup/semaphores[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/cleanup/semaphores "Link to this definition")

/zuul/components[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components "Link to this definition")

The component registry. Each Zuul process registers itself under the appropriate node in this hierarchy so the system has a holistic view of what’s running. The name of the node is based on the hostname but is a sequence node in order to handle multiple processes. The nodes are ephemeral so an outage is automatically detected.

The contents of each node contain information about the running process and may be updated periodically.

/zuul/components/executor[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components/executor "Link to this definition")

/zuul/components/fingergw[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components/fingergw "Link to this definition")

/zuul/components/merger[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components/merger "Link to this definition")

/zuul/components/scheduler[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components/scheduler "Link to this definition")

/zuul/components/web[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/components/web "Link to this definition")

/zuul/config/cache[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/config/cache "Link to this definition")

The unparsed config cache. This contains the contents of every Zuul config file returned by the mergers for use in configuration. Organized by repo canonical name, branch, and filename. The files themselves are sharded.

/zuul/config/lock[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/config/lock "Link to this definition")

Locks for the unparsed config cache.

/zuul/events/connection/<connection>/events[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/connection/%3Cconnection%3E/events "Link to this definition")

Type:_ConnectionEventQueue_

The connection event queue root. Each connection has an event queue where incoming events are recorded before being moved to the tenant event queue.

/zuul/events/connection/<connection>/events/queue[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/connection/%3Cconnection%3E/events/queue "Link to this definition")

The actual event queue. Entries in the queue reference separate data nodes. These are sequence nodes to maintain the event order.

/zuul/events/connection/<connection>/events/data[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/connection/%3Cconnection%3E/events/data "Link to this definition")

Event data nodes referenced by queue items. These are sharded.

/zuul/events/connection/<connection>/events/election[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/connection/%3Cconnection%3E/events/election "Link to this definition")

An election to determine which scheduler processes the event queue and moves events to the tenant event queues.

Drivers may have additional elections as well. For example, Gerrit has an election for the watcher and poller.

/zuul/events/tenant/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E "Link to this definition")

Tenant-specific event queues. Each queue described below has a data and queue subnode.

/zuul/events/tenant/<tenant>/management[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/management "Link to this definition")

The tenant-specific management event queue.

/zuul/events/tenant/<tenant>/trigger[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/trigger "Link to this definition")

The tenant-specific trigger event queue.

/zuul/events/tenant/<tenant>/pipelines[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/pipelines "Link to this definition")

Holds a set of queues for each pipeline.

/zuul/events/tenant/<tenant>/pipelines/<pipeline>/management[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/pipelines/%3Cpipeline%3E/management "Link to this definition")

The pipeline management event queue.

/zuul/events/tenant/<tenant>/pipelines/<pipeline>/result[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/pipelines/%3Cpipeline%3E/result "Link to this definition")

The pipeline result event queue.

/zuul/events/tenant/<tenant>/pipelines/<pipeline>/trigger[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/pipelines/%3Cpipeline%3E/trigger "Link to this definition")

The pipeline trigger event queue.

/zuul/events/tenant/<tenant>/state[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/events/tenant/%3Ctenant%3E/state "Link to this definition")

A Znode that, if exists, can be used to pause event processing.

/zuul/executor/unzoned[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned "Link to this definition")

Type:_JobRequestQueue_

The unzoned executor build request queue. The generic description of a job request queue follows:

/zuul/executor/unzoned/requests/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/requests/%3Crequest%20uuid%3E "Link to this definition")

Requests are added by UUID. Consumers watch the entire tree and order the requests by znode creation time.

/zuul/executor/unzoned/locks/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/locks/%3Crequest%20uuid%3E "Link to this definition")

Type:_Lock_

A consumer will create a lock under this node before processing a request. The znode containing the lock and the request znode have the same UUID. This is a side-channel lock so that the lock can be held while the request itself is deleted.

/zuul/executor/unzoned/params/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/params/%3Crequest%20uuid%3E "Link to this definition")

Parameters can be quite large, so they are kept in a separate znode and only read when needed, and may be removed during request processing to save space in ZooKeeper. The data may be sharded.

/zuul/executor/unzoned/result-data/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/result-data/%3Crequest%20uuid%3E "Link to this definition")

When a job is complete, the results of the merge are written here. The results may be quite large, so they are sharded.

/zuul/executor/unzoned/results/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/results/%3Crequest%20uuid%3E "Link to this definition")

Since writing sharded data is not atomic, once the results are written to `result-data`, a small znode is written here to indicate the results are ready to read. The submitter can watch this znode to be notified that it is ready.

/zuul/executor/unzoned/waiters/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned/waiters/%3Crequest%20uuid%3E "Link to this definition")

(ephemeral)

A submitter who requires the results of the job creates an ephemeral node here to indicate their interest in the results. This is used by the cleanup routines to ensure that they don’t prematurely delete the result data. Used for merge jobs

/zuul/executor/zones/<zone>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/zones/%3Czone%3E "Link to this definition")

A zone-specific executor build request queue. The contents are the same as above.

/zuul/launcher/stats-election[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/launcher/stats-election "Link to this definition")

Type:_LauncherStatsElection_

An election to decide which launcher will report system-wide launcher stats (such as total nodes).

/zuul/layout/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/layout/%3Ctenant%3E "Link to this definition")

The layout state for the tenant. Contains the cache and time data needed for a component to determine if its in-memory layout is out of date and update it if so.

/zuul/layout-data/<layout uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/layout-data/%3Clayout%20uuid%3E "Link to this definition")

Additional information about the layout. This is sharded data for each layout UUID.

/zuul/locks[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks "Link to this definition")

Holds various types of locks so that multiple components can coordinate.

/zuul/locks/connection[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/connection "Link to this definition")

Locks related to connections.

/zuul/locks/connection/<connection>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/connection/%3Cconnection%3E "Link to this definition")

Locks related to a single connection.

/zuul/locks/connection/database/migration[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/connection/database/migration "Link to this definition")

Type:_Lock_

Only one component should run a database migration; this lock ensures that.

/zuul/locks/events[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/events "Link to this definition")

Locks related to tenant event queues.

/zuul/locks/events/trigger/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/events/trigger/%3Ctenant%3E "Link to this definition")

Type:_Lock_

The scheduler locks the trigger event queue for each tenant before processing it. This lock is only needed when processing and removing items from the queue; no lock is required to add items.

/zuul/locks/events/management/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/events/management/%3Ctenant%3E "Link to this definition")

Type:_Lock_

The scheduler locks the management event queue for each tenant before processing it. This lock is only needed when processing and removing items from the queue; no lock is required to add items.

/zuul/locks/pipeline[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/pipeline "Link to this definition")

Locks related to pipelines.

/zuul/locks/pipeline/<tenant>/<pipeline>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/pipeline/%3Ctenant%3E/%3Cpipeline%3E "Link to this definition")

Type:_Lock_

The scheduler obtains a lock before processing each pipeline.

/zuul/locks/tenant[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/tenant "Link to this definition")

Tenant configuration locks.

/zuul/locks/tenant/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/locks/tenant/%3Ctenant%3E "Link to this definition")

Type:_RWLock_

A write lock is obtained at this location before creating a new tenant layout and storing its metadata in ZooKeeper. Components which later determine that they need to update their tenant configuration to match the state in ZooKeeper will obtain a read lock at this location to ensure the state isn’t mutated again while the components are updating their layout to match.

/zuul/ltime[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/ltime "Link to this definition")

An empty node which serves to coordinate logical timestamps across the cluster. Components may update this znode which will cause the latest ZooKeeper transaction ID to appear in the zstat for this znode. This is known as the ltime and can be used to communicate that any subsequent transactions have occurred after this ltime. This is frequently used for cache validation. Any cache which was updated after a specified ltime may be determined to be sufficiently up-to-date for use without invalidation.

/zuul/merger[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/merger "Link to this definition")

Type:_JobRequestQueue_

A JobRequestQueue for mergers. See [zuul/executor/unzoned](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/executor/unzoned "path-zuul/executor/unzoned").

/zuul/nodepool[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodepool "Link to this definition")

Type:_NodepoolEventElection_

An election to decide which scheduler will monitor nodepool requests and generate node completion events as they are completed.

/zuul/results/management[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/results/management "Link to this definition")

Stores results from management events (such as an enqueue event).

/zuul/scheduler/timer-election[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/scheduler/timer-election "Link to this definition")

Type:_SessionAwareElection_

An election to decide which scheduler will generate events for timer pipeline triggers.

/zuul/scheduler/stats-election[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/scheduler/stats-election "Link to this definition")

Type:_SchedulerStatsElection_

An election to decide which scheduler will report system-wide stats (such as total node requests).

/zuul/global-semaphores/<semaphore>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/global-semaphores/%3Csemaphore%3E "Link to this definition")

Type:_SemaphoreHandler_

Represents a global semaphore (shared by multiple tenants). Information about which builds hold the semaphore is stored in the znode data.

/zuul/semaphores/<tenant>/<semaphore>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/semaphores/%3Ctenant%3E/%3Csemaphore%3E "Link to this definition")

Type:_SemaphoreHandler_

Represents a semaphore. Information about which builds hold the semaphore is stored in the znode data.

/zuul/system[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/system "Link to this definition")

Type:_SystemConfigCache_

System-wide configuration data.

/zuul/system/conf[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/system/conf "Link to this definition")

The serialized version of the unparsed abide configuration as well as system attributes (such as the tenant list).

/zuul/system/conf-lock[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/system/conf-lock "Link to this definition")

Type:_WriteLock_

A lock to be acquired before updating [zuul/system/conf](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/system/conf "path-zuul/system/conf")

/zuul/tenant/<tenant>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E "Link to this definition")

Tenant-specific information here.

/zuul/tenant/<tenant>/pipeline/<pipeline>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E "Link to this definition")

Pipeline state.

/zuul/tenant/<tenant>/pipeline/<pipeline>/dirty[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/dirty "Link to this definition")

A flag indicating that the pipeline state is “dirty”; i.e., it needs to have the pipeline processor run.

/zuul/tenant/<tenant>/pipeline/<pipeline>/queue[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/queue "Link to this definition")

Holds queue objects.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E "Link to this definition")

Items belong to queues, but are held in their own hierarchy since they may shift to different queues during reconfiguration.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>/buildset/<buildset uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E/buildset/%3Cbuildset%20uuid%3E "Link to this definition")

There will only be one buildset under the buildset/ node. If we reset it, we will get a new uuid and delete the old one. Any external references to it will be automatically invalidated.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>/buildset/<buildset uuid>/repo_state[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E/buildset/%3Cbuildset%20uuid%3E/repo_state "Link to this definition")

The global repo state for the buildset is kept in its own node since it can be large, and is also common for all jobs in this buildset.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>/buildset/<buildset uuid>/job/<job name>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E/buildset/%3Cbuildset%20uuid%3E/job/%3Cjob%20name%3E "Link to this definition")

The frozen job.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>/buildset/<buildset uuid>/job/<job name>/build/<build uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E/buildset/%3Cbuildset%20uuid%3E/job/%3Cjob%20name%3E/build/%3Cbuild%20uuid%3E "Link to this definition")

Information about this build of the job. Similar to buildset, there should only be one entry, and using the UUID automatically invalidates any references.

/zuul/tenant/<tenant>/pipeline/<pipeline>/item/<item uuid>/buildset/<buildset uuid>/job/<job name>/build/<build uuid>/parameters[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%3E/pipeline/%3Cpipeline%3E/item/%3Citem%20uuid%3E/buildset/%3Cbuildset%20uuid%3E/job/%3Cjob%20name%3E/build/%3Cbuild%20uuid%3E/parameters "Link to this definition")

Parameters for the build; these can be large so they’re in their own znode and will be read only if needed.

/zuul/nodeset/requests/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodeset/requests/%3Crequest%20uuid%3E "Link to this definition")

Type:_NodesetRequest_

A new-style (nodepool-in-zuul) node request. This will replace nodepool/requests. The two may operate in parallel for a time.

Schedulers create requests and may delete them at any time (regardless of lock state).

/zuul/nodeset/locks/<request uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodeset/locks/%3Crequest%20uuid%3E "Link to this definition")

A lock for the new-style node request. Launchers will acquire a lock when operating on the request.

/zuul/nodes/nodes/<node uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodes/nodes/%3Cnode%20uuid%3E "Link to this definition")

Type:_ProviderNode_

A new-style (nodepool-in-zuul) node record. This holds information about the node (mostly supplied by the provider). It also holds enough information to get the endpoint responsible for the node.

/zuul/nodes/nodes/<node uuid>/snapshot[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodes/nodes/%3Cnode%20uuid%3E/snapshot "Link to this definition")

Type:_ProviderNodeSnapshot_

Information about a provider node snapshot. The launcher locks the companion snapshot-lock znode and updates this znode while the executor continues to hold the lock on the main node’s znode.

/zuul/nodes/nodes/<node uuid>/snapshot-lock[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodes/nodes/%3Cnode%20uuid%3E/snapshot-lock "Link to this definition")

The lock for the snapshot child znode.

/zuul/nodes/locks/<node uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/nodes/locks/%3Cnode%20uuid%3E "Link to this definition")

A lock for the new-style node. Launchers or executors will hold this lock while operating on the node.

/zuul/tenant/<tenant name>/provider/<provider canonical name>/config[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/tenant/%3Ctenant%20name%3E/provider/%3Cprovider%20canonical%20name%3E/config "Link to this definition")

The flattened configuration for a provider. This holds the complete information about the images, labels, and flavors the provider supports. It is the combination of the provider stanza plus any inherited sections.

References to images, labels, and flavors are made using canonical names since the same short names may be different in different tenants. Since the same canonically-named provider may appear in different tenants with different images, labels, and flavors, the provider itself is tenant scoped.

Only updated by schedulers upon reconfiguration. Read-only for launchers.

/zuul/images/artifacts/<uuid>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/images/artifacts/%3Cuuid%3E "Link to this definition")

Stores information about an image build artifact. Each build job may produce any number of artifacts (each corresponding to an image+format). Information about each is stored here under a random uuid.

/zuul/image-uploads/<image canonical name>/<image build uuid>/endpoint/<endpoint id>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/image-uploads/%3Cimage%20canonical%20name%3E/%3Cimage%20build%20uuid%3E/endpoint/%3Cendpoint%20id%3E "Link to this definition")

Stores information about an image upload to a particular cloud endpoint.

/zuul/endpoint/<endpoint name>/quota[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/endpoint/%3Cendpoint%20name%3E/quota "Link to this definition")

Type:_QuotaCache_

A TreeCache that stores quota information for the endpoint.

/zuul/endpoint/<endpoint name>/quota/limits[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/endpoint/%3Cendpoint%20name%3E/quota/limits "Link to this definition")

Stores information about the quota limits of the endpoint.

/zuul/endpoint/<endpoint name>/quota/unmanaged-usage[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/endpoint/%3Cendpoint%20name%3E/quota/unmanaged-usage "Link to this definition")

Stores information about the unmanaged quota usage of the endpoint.

/zuul/endpoint/<endpoint name>/quota/resource/<resource id>[](https://zuul-ci.org/docs/zuul/latest/developer/zookeeper.html#path-zuul/endpoint/%3Cendpoint%20name%3E/quota/resource/%3Cresource%20id%3E "Link to this definition")

Stores information about the quota requirements of driver-defined resources (such as instance or volume types). This allows any launcher to calculate the estimated quota usage of any request, without having an active endpoint.

[Previous](https://zuul-ci.org/docs/zuul/latest/developer/specs/web-rbac.html "Fine-Grained API/Web Access Control")[Next](https://zuul-ci.org/docs/zuul/latest/developer/model-changelog.html "Data Model Changelog")

* * *

© Copyright 2012-2026, Zuul project contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

Versions v: latest 

[latest](https://zuul-ci.org/docs/zuul/latest/)[14.0.0](https://zuul-ci.org/docs/zuul/14.0.0/)[13.1.1](https://zuul-ci.org/docs/zuul/13.1.1/)[13.1.0](https://zuul-ci.org/docs/zuul/13.1.0/)[13.0.1](https://zuul-ci.org/docs/zuul/13.0.1/)[13.0.0](https://zuul-ci.org/docs/zuul/13.0.0/)[12.1.0](https://zuul-ci.org/docs/zuul/12.1.0/)[12.0.0](https://zuul-ci.org/docs/zuul/12.0.0/)[11.3.0](https://zuul-ci.org/docs/zuul/11.3.0/)[11.2.0](https://zuul-ci.org/docs/zuul/11.2.0/)[11.1.0](https://zuul-ci.org/docs/zuul/11.1.0/)[11.0.1](https://zuul-ci.org/docs/zuul/11.0.1/)[11.0.0](https://zuul-ci.org/docs/zuul/11.0.0/)[10.2.0](https://zuul-ci.org/docs/zuul/10.2.0/)[10.1.0](https://zuul-ci.org/docs/zuul/10.1.0/)[10.0.0](https://zuul-ci.org/docs/zuul/10.0.0/)[9.5.0](https://zuul-ci.org/docs/zuul/9.5.0/)[9.4.0](https://zuul-ci.org/docs/zuul/9.4.0/)[9.3.0](https://zuul-ci.org/docs/zuul/9.3.0/)[9.2.0](https://zuul-ci.org/docs/zuul/9.2.0/)[9.1.0](https://zuul-ci.org/docs/zuul/9.1.0/)[9.0.0](https://zuul-ci.org/docs/zuul/9.0.0/)[8.3.1](https://zuul-ci.org/docs/zuul/8.3.1/)[8.3.0](https://zuul-ci.org/docs/zuul/8.3.0/)[8.2.0](https://zuul-ci.org/docs/zuul/8.2.0/)[8.1.0](https://zuul-ci.org/docs/zuul/8.1.0/)[8.0.1](https://zuul-ci.org/docs/zuul/8.0.1/)[8.0.0](https://zuul-ci.org/docs/zuul/8.0.0/)[7.1.0](https://zuul-ci.org/docs/zuul/7.1.0/)[7.0.0](https://zuul-ci.org/docs/zuul/7.0.0/)[6.4.0](https://zuul-ci.org/docs/zuul/6.4.0/)[6.3.0](https://zuul-ci.org/docs/zuul/6.3.0/)[6.2.0](https://zuul-ci.org/docs/zuul/6.2.0/)[6.1.0](https://zuul-ci.org/docs/zuul/6.1.0/)[6.0.0](https://zuul-ci.org/docs/zuul/6.0.0/)[5.2.5](https://zuul-ci.org/docs/zuul/5.2.5/)[5.2.4](https://zuul-ci.org/docs/zuul/5.2.4/)[5.2.3](https://zuul-ci.org/docs/zuul/5.2.3/)[5.2.2](https://zuul-ci.org/docs/zuul/5.2.2/)[5.2.1](https://zuul-ci.org/docs/zuul/5.2.1/)[5.2.0](https://zuul-ci.org/docs/zuul/5.2.0/)[5.1.0](https://zuul-ci.org/docs/zuul/5.1.0/)[5.0.0](https://zuul-ci.org/docs/zuul/5.0.0/)[4.12.0](https://zuul-ci.org/docs/zuul/4.12.0/)[4.11.0](https://zuul-ci.org/docs/zuul/4.11.0/)[4.10.4](https://zuul-ci.org/docs/zuul/4.10.4/)[4.10.3](https://zuul-ci.org/docs/zuul/4.10.3/)[4.10.2](https://zuul-ci.org/docs/zuul/4.10.2/)[4.10.1](https://zuul-ci.org/docs/zuul/4.10.1/)[4.10.0](https://zuul-ci.org/docs/zuul/4.10.0/)[4.9.0](https://zuul-ci.org/docs/zuul/4.9.0/)[4.8.1](https://zuul-ci.org/docs/zuul/4.8.1/)[4.8.0](https://zuul-ci.org/docs/zuul/4.8.0/)[4.7.0](https://zuul-ci.org/docs/zuul/4.7.0/)[4.6.0](https://zuul-ci.org/docs/zuul/4.6.0/)[4.5.1](https://zuul-ci.org/docs/zuul/4.5.1/)[4.5.0](https://zuul-ci.org/docs/zuul/4.5.0/)[4.4.0](https://zuul-ci.org/docs/zuul/4.4.0/)[4.3.0](https://zuul-ci.org/docs/zuul/4.3.0/)[4.2.0](https://zuul-ci.org/docs/zuul/4.2.0/)[4.1.0](https://zuul-ci.org/docs/zuul/4.1.0/)[4.0.0](https://zuul-ci.org/docs/zuul/4.0.0/)[3.19.1](https://zuul-ci.org/docs/zuul/3.19.1/)[3.19.0](https://zuul-ci.org/docs/zuul/3.19.0/)[3.18.0](https://zuul-ci.org/docs/zuul/3.18.0/)[3.17.0](https://zuul-ci.org/docs/zuul/3.17.0/)[3.16.1](https://zuul-ci.org/docs/zuul/3.16.1/)[3.16.0](https://zuul-ci.org/docs/zuul/3.16.0/)[3.15.0](https://zuul-ci.org/docs/zuul/3.15.0/)[3.14.0](https://zuul-ci.org/docs/zuul/3.14.0/)[3.13.0](https://zuul-ci.org/docs/zuul/3.13.0/)[3.12.0](https://zuul-ci.org/docs/zuul/3.12.0/)[3.11.1](https://zuul-ci.org/docs/zuul/3.11.1/)[3.11.0](https://zuul-ci.org/docs/zuul/3.11.0/)[3.10.2](https://zuul-ci.org/docs/zuul/3.10.2/)[3.10.1](https://zuul-ci.org/docs/zuul/3.10.1/)[3.10.0](https://zuul-ci.org/docs/zuul/3.10.0/)[3.9.0](https://zuul-ci.org/docs/zuul/3.9.0/)[3.8.1](https://zuul-ci.org/docs/zuul/3.8.1/)[3.8.0](https://zuul-ci.org/docs/zuul/3.8.0/)[3.7.1](https://zuul-ci.org/docs/zuul/3.7.1/)[3.7.0](https://zuul-ci.org/docs/zuul/3.7.0/)[3.6.1](https://zuul-ci.org/docs/zuul/3.6.1/)[3.6.0](https://zuul-ci.org/docs/zuul/3.6.0/)[3.5.0](https://zuul-ci.org/docs/zuul/3.5.0/)[3.4.0](https://zuul-ci.org/docs/zuul/3.4.0/)[3.3.1](https://zuul-ci.org/docs/zuul/3.3.1/)[3.3.0](https://zuul-ci.org/docs/zuul/3.3.0/)
