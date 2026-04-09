# Source: https://zuul-ci.org/docs/zuul/latest/gating.html

Title: Project Gating — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/gating.html

Markdown Content:
Project Gating — Zuul documentation
===============

[![Image 14: Logo](https://zuul-ci.org/docs/zuul/latest/_static/logo.svg)](https://zuul-ci.org/docs/zuul/latest/index.html)

*   [About Zuul](https://zuul-ci.org/docs/zuul/latest/about.html)
    *   [Zuul Concepts](https://zuul-ci.org/docs/zuul/latest/concepts.html)
    *   [Project Gating](https://zuul-ci.org/docs/zuul/latest/gating.html#)
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
*   [About Zuul](https://zuul-ci.org/docs/zuul/latest/about.html)
*   Project Gating
*   [View page source](https://zuul-ci.org/docs/zuul/latest/_sources/gating.rst.txt)

* * *

Project Gating[](https://zuul-ci.org/docs/zuul/latest/gating.html#project-gating "Link to this heading")
=========================================================================================================

Traditionally, many software development projects merge changes from developers into the repository, and then identify regressions resulting from those changes (perhaps by running a test suite with a continuous integration system), followed by more patches to fix those bugs. When the mainline of development is broken, it can be very frustrating for developers and can cause lost productivity, particularly so when the number of contributors or contributions is large.

The process of gating attempts to prevent changes that introduce regressions from being merged. This keeps the mainline of development open and working for all developers, and only when a change is confirmed to work without disruption is it merged.

Many projects practice an informal method of gating where developers with mainline commit access ensure that a test suite runs before merging a change. With more developers, more changes, and more comprehensive test suites, that process does not scale very well, and is not the best use of a developer’s time. Zuul can help automate this process, with a particular emphasis on ensuring large numbers of changes are tested correctly.

Testing in parallel[](https://zuul-ci.org/docs/zuul/latest/gating.html#testing-in-parallel "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

A particular focus of Zuul is ensuring correctly ordered testing of changes in parallel. A gating system should always test each change applied to the tip of the branch exactly as it is going to be merged. A simple way to do that would be to test one change at a time, and merge it only if it passes tests. That works very well, but if changes take a long time to test, developers may have to wait a long time for their changes to make it into the repository. With some projects, it may take hours to test changes, and it is easy for developers to create changes at a rate faster than they can be tested and merged.

Zuul’s [dependent pipeline manager](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.dependent "value-pipeline.manager.dependent") allows for parallel execution of test jobs for gating while ensuring changes are tested correctly, exactly as if they had been tested one at a time. It does this by performing speculative execution of test jobs; it assumes that all jobs will succeed and tests them in parallel accordingly. If they do succeed, they can all be merged. However, if one fails, then changes that were expecting it to succeed are re-tested without the failed change. In the best case, as many changes as execution contexts are available may be tested in parallel and merged at once. In the worst case, changes are tested one at a time (as each subsequent change fails, changes behind it start again).

For example, if a reviewer approves five changes in rapid succession:

A, B, C, D, E

Zuul queues those changes in the order they were approved, and notes that each subsequent change depends on the one ahead of it merging:

![Image 15: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];
  A -> B -> C -> D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-91e135798482b06f8e2f1d205b7c97337fa15fa5.png)

Zuul then starts immediately testing all of the changes in parallel. But in the case of changes that depend on others, it instructs the test system to include the changes ahead of it, with the assumption they pass. That means jobs testing change _B_ include change _A_ as well:

Jobs for A: merge change A, then test
Jobs for B: merge changes A and B, then test
Jobs for C: merge changes A, B and C, then test
Jobs for D: merge changes A, B, C and D, then test
Jobs for E: merge changes A, B, C, D and E, then test

Hence jobs triggered to tests A will only test A and ignore B, C, D:

![Image 16: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  subgraph cluster_merged {
    label="Merged Changes for A";
    style=filled;
    color=orange;
    node [style=filled,color=black,fillcolor=white];
    master -> A;
  }

  subgraph cluster_ignored {
    label="Ignored Changes";
    style=filled;
    color=lightgrey;
    node [style=filled,color=black,fillcolor=white];
    B -> C -> D -> E;
  }

  A -> B;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-d9d029af9b579276eaf0a79ac4adb560f77fd3c5.png)

The jobs for E would include the whole dependency chain: A, B, C, D, and E. E will be tested assuming A, B, C, and D passed:

![Image 17: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  subgraph cluster_merged {
    label="Merged Changes for E";
    style=filled;
    color=orange;
    node [style=filled,color=black,fillcolor=white];
    master -> A -> B -> C -> D -> E;
  }
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-979fec1a100b4540a7136fd5785b68023ba0eb4f.png)

If changes _A_ and _B_ pass tests (green), and _C_, _D_, and _E_ fail (red):

![Image 18: digraph foo{
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  A [style=filled,color=black,fillcolor=lightgreen];
  B [style=filled,color=black,fillcolor=lightgreen];
  C [style=filled,color=black,fillcolor=lightpink];
  D [style=filled,color=black,fillcolor=lightpink];
  E [style=filled,color=black,fillcolor=lightpink];
  master -> A -> B -> C -> D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-1272a5a2f1cb9e88d8328b4ff85d9359fe1ba193.png)

Zuul will merge change _A_ followed by change _B_, leaving this queue:

![Image 19: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  C [style=filled,color=black,fillcolor=lightpink];
  D [style=filled,color=black,fillcolor=lightpink];
  E [style=filled,color=black,fillcolor=lightpink];
  C -> D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-5bd9e10b79c8bca20c34e81e7e27bb948a1db7a4.png)

Since _D_ was dependent on _C_, it is not clear whether _D_’s failure is the result of a defect in _D_ or _C_:

![Image 20: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  C [style=filled,color=black,fillcolor=lightpink];
  D [label="D\n?"];
  E [label="E\n?"];
  C -> D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-a66bb3059f266554fdca4801ab5a6c6574758c79.png)

Since _C_ failed, Zuul will report its failure and drop _C_ from the queue, keeping D and E:

![Image 21: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  D [label="D\n?"];
  E [label="E\n?"];
  D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-f2c2826db062f6a48041dc08785ffe6162e0710c.png)

This queue is the same as if two new changes had just arrived, so Zuul starts the process again testing _D_ against the tip of the branch, and _E_ against _D_:

![Image 22: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  subgraph cluster_merged {
    label="Merged Changes for D";
    style=filled;
    color=orange;
    node [style=filled,color=black,fillcolor=white];
    master -> D;
  }

  subgraph cluster_skip {
    label="Skip";
    style=filled;
    color=lightgrey;
    node [style=filled,color=black,fillcolor=white];
    E;
  }

  D -> E;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-59f4b3fcdfdd6f624a868717c9a6e6dc4a2e2463.png)

![Image 23: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  subgraph cluster_merged {
    label="Merged Changes for E";
    style=filled;
    color=orange;
    node [style=filled,color=black,fillcolor=white];
    master -> D -> E;
  }
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-60cb3ccc0d8c802bc1ac549bfe2f13eb2b284e1c.png)

### Pipeline Window[](https://zuul-ci.org/docs/zuul/latest/gating.html#pipeline-window "Link to this heading")

Zuul allows for some control over this process. Pipelines have a [window](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-window) which is portion of the pipeline where jobs are permitted to run. The window is the number of changes at the head of the queue where Zuul will start jobs. Any changes beyond this number are held in the queue without running jobs. As changes exit the head of the queue, the changes outside the window will move up and eventually start their jobs.

![Image 24: digraph foo {
  bgcolor="transparent";
  rankdir="LR";
  node [shape=box];
  edge [dir=back];

  subgraph cluster_active {
    label="Pipeline Active Window";
    style=filled;
    color=lightblue1;
    node [style=filled,color=black,fillcolor=white];
    A -> B -> C;
  }

  subgraph cluster_inactive {
    label="Waiting to run jobs";
    style=filled;
    color=lightgrey;
    node [style=filled,color=black,fillcolor=white];
    D -> E;
  }

  master -> A;
  C -> D;
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-367498b1677d93bd65d6989eb38a093bc1106619.png)

The window is designed to control the amount of resources used for parallel testing. As described above, if changes fail testing in a dependent pipeline, build results are discarded and new builds are started without the failing changes. If this happens frequently, then Zuul can end up using increasingly large amounts of test resources for little gain. Ideally if builds frequently succeed, the window should be large in order to maximize throughput, and if they frequently fail, it should be small in order to minimize waste.

By default, Zuul uses an algorithm inspired by the Transmission Control Protocol’s flow control to determine the window size. It starts with the window set to a certain value (twenty changes by default). Each time a change successfully merges, the window is increased by one. Each time a change fails, the window is halved. This allows the window to shrink rapidly when changes start to fail, and recover slowly if they succeed. A floor is set to ensure that (by default) there is always at least some amount of parallel testing, and a ceiling may be set to prevent a wildly successful pipeline from starving others of resources.

All of the parameters above can be customized to match local needs, but the defaults are a good starting point. See [pipeline.window](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.window "attr-pipeline.window") for details.

The window parameters are set on the pipeline, but each [project queue](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-project-queue) within that pipeline maintains its own window so that unreliable tests in one project queue don’t affect the window of other project queues.

While every pipeline has a window, only pipelines using the [dependent](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.dependent "value-pipeline.manager.dependent") pipeline manager allow configuration of the window. Other pipeline managers use fixed values to implement their particular behaviors. For example, [independent](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.independent "value-pipeline.manager.independent") pipelines always have unlimited windows, and [serial](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.serial "value-pipeline.manager.serial") pipelines have a fixed window size of 1.

The window can be visualized in the web interface by inspecting the icon to the left of a change. If a change is outside the window, it will have an hourglass icon and the mouseover text will indicate that jobs will start when the change moves closer to the head of the queue.

Cross Project Testing[](https://zuul-ci.org/docs/zuul/latest/gating.html#cross-project-testing "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

When your projects are closely coupled together, you want to make sure changes entering the gate are going to be tested with the version of other projects currently enqueued in the gate (since they will eventually be merged and might introduce breaking features).

Such relationships can be defined in Zuul configuration by placing projects in a shared queue within a dependent pipeline. Whenever changes for any project enter a pipeline with such a shared queue, they are tested together, such that the commits for the changes ahead in the queue are automatically present in the jobs for the changes behind them. See [Project](https://zuul-ci.org/docs/zuul/latest/config/project.html#project) for more details.

A given dependent pipeline may have as many shared change queues as necessary, so groups of related projects may share a change queue without interfering with unrelated projects. [Independent pipelines](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.independent "value-pipeline.manager.independent") do not use shared change queues, however, they may still be used to test changes across projects using cross-project dependencies.

Cross-Project Dependencies[](https://zuul-ci.org/docs/zuul/latest/gating.html#cross-project-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

Zuul permits users to specify dependencies across projects. Using a special footer, users may specify that a change depends on another change in any repository known to Zuul. In Gerrit based projects this footer needs to be added to the git commit message. In GitHub based projects this footer must be added to the pull request description.

Zuul’s cross-project dependencies behave like a directed acyclic graph (DAG), like git itself, to indicate a one-way dependency relationship between changes in different git repositories. Change A may depend on B, but B may not depend on A.

To use them, include `Depends-On: <change-url>` in the footer of a commit message or pull request. For example, a change which depends on a GitHub pull request (PR #4) might have the following footer:

Depends-On: https://github.com/example/test/pull/4

Note

For Github the `Depends-On:` footer must be in the _Pull Request_ description, which is separate and often different to the commit message (i.e. the text submitted with `git commit`). This is in contrast to Gerrit where the change description is always the commit message.

A change which depends on a Gerrit change (change number 3):

Depends-On: https://review.example.com/3

Changes may depend on changes in any other project, even projects not on the same system (i.e., a Gerrit change may depend on a GitHub pull request).

Note

An older syntax of specifying dependencies using Gerrit change-ids is still supported, however it is deprecated and will be removed in a future version.

### Dependent Pipeline[](https://zuul-ci.org/docs/zuul/latest/gating.html#dependent-pipeline "Link to this heading")

When Zuul sees changes with cross-project dependencies, it serializes them in the usual manner when enqueuing them into a pipeline. This means that if change A depends on B, then when they are added to a dependent pipeline, B will appear first and A will follow:

![Image 25: digraph crd {
  bgcolor="transparent";
  stat_B [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_A [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_B -> stat_A [arrowhead="none"];

  change_B [shape=box,fixedsize=true,width=1.75,height=0.75,label="Change B\nURL: .../4"];
  change_A [shape=box,fixedsize=true,width=1.75,height=0.75,label="Change A\nDepends-On: .../4"];

  change_B -> change_A [dir=back];
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-fc014da48de771e48dc9baf8a27ae288e715bb7b.png)

If tests for B fail, both B and A will be removed from the pipeline, and it will not be possible for A to merge until B does.

Note

If changes with cross-project dependencies do not share a change queue then Zuul is unable to enqueue them together, and the first will be required to merge before the second can be enqueued. If the second change is approved before the first is merged, Zuul can’t act on the approval and won’t automatically enqueue the second change, requiring a new approval event to enqueue it after the first change merges.

### Independent Pipeline[](https://zuul-ci.org/docs/zuul/latest/gating.html#independent-pipeline "Link to this heading")

When changes are enqueued into an independent pipeline, all of the related dependencies (both normal git-dependencies that come from parent commits as well as cross-project dependencies) appear in a dependency graph, as in a dependent pipeline. This means that even in an independent pipeline, your change will be tested with its dependencies. Changes that were previously unable to be fully tested until a related change landed in a different repository may now be tested together from the start.

All of the changes are still independent (you will note that the whole pipeline does not share a graph as in a dependent pipeline), but for each change tested, all of its dependencies are visually connected to it, and they are used to construct the git repositories that Zuul uses when testing.

When looking at this graph on the status page, you will note that the dependencies show up as grey dots, while the actual change tested shows up as red or green (depending on the jobs results):

![Image 26: digraph crdgrey {
  bgcolor="transparent";
  stat_B [shape=circle,style=filled,color=black,fillcolor=grey,label=""];
  stat_A [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_B -> stat_A [arrowhead="none"];

  change_B [shape=box,fixedsize=true,width=1.75,height=0.75,label="Change B\nURL: .../4"];
  change_A [shape=box,fixedsize=true,width=1.75,height=0.75,label="Change A\nDepends-On: .../4"];

  change_B -> change_A [dir=back];
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-449bd938cfd607f13d13cc1507b55dc64a5b6e5b.png)

This is to indicate that the grey changes are only there to establish dependencies. Even if one of the dependencies is also being tested, it will show up as a grey dot when used as a dependency, but separately and additionally will appear as its own red or green dot for its test.

### Multiple Changes[](https://zuul-ci.org/docs/zuul/latest/gating.html#multiple-changes "Link to this heading")

A change may list more than one dependency by simply adding more `Depends-On:` lines to the commit message footer. It is possible for a change in project A to depend on a change in project B and a change in project C.

![Image 27: digraph crdmultichanges {
  bgcolor="transparent";
  splines=ortho;
  stat_B [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_C [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_A [shape=circle,style=filled,color=black,fillcolor=forestgreen,label=""];
  stat_B -> stat_C -> stat_A [arrowhead="none"];

  subgraph cluster_deps {
    label="Dependencies";
    style=filled;
    color=lightgrey;
    node [style=filled,color=black,fillcolor=white];
    repo_B [shape=box,fixedsize=true,width=1.75,height=0.75,label="Repo B\nURL: .../3",group=redir];
    repo_C [shape=box,fixedsize=true,width=1.75,height=0.75,label="Repo C\nURL: .../4",group=redir];
    {rank=same;repo_B;redir_B}
    // We use the redirect point, group redir, and ortho splines to keep
    // repo A,B,C nodes in a vertical line then draw lines from A around
    // C to B.
    redir_B [label="",shape=point,height=.005];
    // This is an invisible edge because we want them vertically aligned
    // and ordered but there is no git/zuul dependency between the changes
    // so we don't draw the edge.
    repo_B -> repo_C [style=invis];
  }

  repo_A [shape=box,fixedsize=true,width=1.75,height=0.75,label="Repo A\nDepends-On: .../3\nDepends-On: .../4",group=redir];
  repo_B -> redir_B [dir=back];
  redir_B -> repo_A [arrowhead=none];
  repo_C -> repo_A [dir=back];
}](https://zuul-ci.org/docs/zuul/latest/_images/graphviz-45399ed6ba21525cfe99d39ef2a794c5c54b86f2.png)

### Cycles[](https://zuul-ci.org/docs/zuul/latest/gating.html#cycles "Link to this heading")

Zuul supports cycles that are created by use of cross-project dependencies. However this feature is opt-in and can be configured on the queue. See [queue.allow-circular-dependencies](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue.allow-circular-dependencies "attr-queue.allow-circular-dependencies") for information on how to configure this.

### Global Repo State[](https://zuul-ci.org/docs/zuul/latest/gating.html#global-repo-state "Link to this heading")

If a git repository is used by at least one job for a queue item, then Zuul will freeze the repo state (i.e., branch heads and tags) and use that same state for every job run for that queue item. Not every job will get a git repo checkout of every repo, but for any repo that is checked out, it will have the same state. Because of this, authors can be sure that jobs running on the same queue item have a consistent view of all involved git repos, even if one job starts running much later than another.

[Previous](https://zuul-ci.org/docs/zuul/latest/concepts.html "Zuul Concepts")[Next](https://zuul-ci.org/docs/zuul/latest/tutorials/quick-start.html "Quick-Start Installation and Tutorial")

* * *

© Copyright 2012-2026, Zuul project contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

Versions v: latest 

[latest](https://zuul-ci.org/docs/zuul/latest/)[14.0.0](https://zuul-ci.org/docs/zuul/14.0.0/)[13.1.1](https://zuul-ci.org/docs/zuul/13.1.1/)[13.1.0](https://zuul-ci.org/docs/zuul/13.1.0/)[13.0.1](https://zuul-ci.org/docs/zuul/13.0.1/)[13.0.0](https://zuul-ci.org/docs/zuul/13.0.0/)[12.1.0](https://zuul-ci.org/docs/zuul/12.1.0/)[12.0.0](https://zuul-ci.org/docs/zuul/12.0.0/)[11.3.0](https://zuul-ci.org/docs/zuul/11.3.0/)[11.2.0](https://zuul-ci.org/docs/zuul/11.2.0/)[11.1.0](https://zuul-ci.org/docs/zuul/11.1.0/)[11.0.1](https://zuul-ci.org/docs/zuul/11.0.1/)[11.0.0](https://zuul-ci.org/docs/zuul/11.0.0/)[10.2.0](https://zuul-ci.org/docs/zuul/10.2.0/)[10.1.0](https://zuul-ci.org/docs/zuul/10.1.0/)[10.0.0](https://zuul-ci.org/docs/zuul/10.0.0/)[9.5.0](https://zuul-ci.org/docs/zuul/9.5.0/)[9.4.0](https://zuul-ci.org/docs/zuul/9.4.0/)[9.3.0](https://zuul-ci.org/docs/zuul/9.3.0/)[9.2.0](https://zuul-ci.org/docs/zuul/9.2.0/)[9.1.0](https://zuul-ci.org/docs/zuul/9.1.0/)[9.0.0](https://zuul-ci.org/docs/zuul/9.0.0/)[8.3.1](https://zuul-ci.org/docs/zuul/8.3.1/)[8.3.0](https://zuul-ci.org/docs/zuul/8.3.0/)[8.2.0](https://zuul-ci.org/docs/zuul/8.2.0/)[8.1.0](https://zuul-ci.org/docs/zuul/8.1.0/)[8.0.1](https://zuul-ci.org/docs/zuul/8.0.1/)[8.0.0](https://zuul-ci.org/docs/zuul/8.0.0/)[7.1.0](https://zuul-ci.org/docs/zuul/7.1.0/)[7.0.0](https://zuul-ci.org/docs/zuul/7.0.0/)[6.4.0](https://zuul-ci.org/docs/zuul/6.4.0/)[6.3.0](https://zuul-ci.org/docs/zuul/6.3.0/)[6.2.0](https://zuul-ci.org/docs/zuul/6.2.0/)[6.1.0](https://zuul-ci.org/docs/zuul/6.1.0/)[6.0.0](https://zuul-ci.org/docs/zuul/6.0.0/)[5.2.5](https://zuul-ci.org/docs/zuul/5.2.5/)[5.2.4](https://zuul-ci.org/docs/zuul/5.2.4/)[5.2.3](https://zuul-ci.org/docs/zuul/5.2.3/)[5.2.2](https://zuul-ci.org/docs/zuul/5.2.2/)[5.2.1](https://zuul-ci.org/docs/zuul/5.2.1/)[5.2.0](https://zuul-ci.org/docs/zuul/5.2.0/)[5.1.0](https://zuul-ci.org/docs/zuul/5.1.0/)[5.0.0](https://zuul-ci.org/docs/zuul/5.0.0/)[4.12.0](https://zuul-ci.org/docs/zuul/4.12.0/)[4.11.0](https://zuul-ci.org/docs/zuul/4.11.0/)[4.10.4](https://zuul-ci.org/docs/zuul/4.10.4/)[4.10.3](https://zuul-ci.org/docs/zuul/4.10.3/)[4.10.2](https://zuul-ci.org/docs/zuul/4.10.2/)[4.10.1](https://zuul-ci.org/docs/zuul/4.10.1/)[4.10.0](https://zuul-ci.org/docs/zuul/4.10.0/)[4.9.0](https://zuul-ci.org/docs/zuul/4.9.0/)[4.8.1](https://zuul-ci.org/docs/zuul/4.8.1/)[4.8.0](https://zuul-ci.org/docs/zuul/4.8.0/)[4.7.0](https://zuul-ci.org/docs/zuul/4.7.0/)[4.6.0](https://zuul-ci.org/docs/zuul/4.6.0/)[4.5.1](https://zuul-ci.org/docs/zuul/4.5.1/)[4.5.0](https://zuul-ci.org/docs/zuul/4.5.0/)[4.4.0](https://zuul-ci.org/docs/zuul/4.4.0/)[4.3.0](https://zuul-ci.org/docs/zuul/4.3.0/)[4.2.0](https://zuul-ci.org/docs/zuul/4.2.0/)[4.1.0](https://zuul-ci.org/docs/zuul/4.1.0/)[4.0.0](https://zuul-ci.org/docs/zuul/4.0.0/)[3.19.1](https://zuul-ci.org/docs/zuul/3.19.1/)[3.19.0](https://zuul-ci.org/docs/zuul/3.19.0/)[3.18.0](https://zuul-ci.org/docs/zuul/3.18.0/)[3.17.0](https://zuul-ci.org/docs/zuul/3.17.0/)[3.16.1](https://zuul-ci.org/docs/zuul/3.16.1/)[3.16.0](https://zuul-ci.org/docs/zuul/3.16.0/)[3.15.0](https://zuul-ci.org/docs/zuul/3.15.0/)[3.14.0](https://zuul-ci.org/docs/zuul/3.14.0/)[3.13.0](https://zuul-ci.org/docs/zuul/3.13.0/)[3.12.0](https://zuul-ci.org/docs/zuul/3.12.0/)[3.11.1](https://zuul-ci.org/docs/zuul/3.11.1/)[3.11.0](https://zuul-ci.org/docs/zuul/3.11.0/)[3.10.2](https://zuul-ci.org/docs/zuul/3.10.2/)[3.10.1](https://zuul-ci.org/docs/zuul/3.10.1/)[3.10.0](https://zuul-ci.org/docs/zuul/3.10.0/)[3.9.0](https://zuul-ci.org/docs/zuul/3.9.0/)[3.8.1](https://zuul-ci.org/docs/zuul/3.8.1/)[3.8.0](https://zuul-ci.org/docs/zuul/3.8.0/)[3.7.1](https://zuul-ci.org/docs/zuul/3.7.1/)[3.7.0](https://zuul-ci.org/docs/zuul/3.7.0/)[3.6.1](https://zuul-ci.org/docs/zuul/3.6.1/)[3.6.0](https://zuul-ci.org/docs/zuul/3.6.0/)[3.5.0](https://zuul-ci.org/docs/zuul/3.5.0/)[3.4.0](https://zuul-ci.org/docs/zuul/3.4.0/)[3.3.1](https://zuul-ci.org/docs/zuul/3.3.1/)[3.3.0](https://zuul-ci.org/docs/zuul/3.3.0/)
