# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/cluster-architecture.md

# Architecture

Getint.io platform is designed to work as a clustered system with multiple tenants under each cluster. So its possible to create multiple clusters and point forward incoming requests to specific cluster basing on their e.g. subdomains (like <https://cluster1.getint.io.company.com>).

**With such approach, its possible to**

* run multiple clusters integrating different apps / software of organisation
* separate and perform integrations of particular partners on dedicated clusters
* within a cluster, setup integrations on separate tenants (e.g. put more resource intensive or business critical integrations on separate tenants)
* have getint.io platform running **Fully Behind Firewall**

{% hint style="info" %}
On-Premise version of getint.io allows you to be the **owner and administrator** of the processed data during the integration / synchronization.

With that deployment mode, you can have getint.io working **Fully Behind Firewall**. No requests, except to the apps you are integrating will be performed.&#x20;
{% endhint %}

Below you can find cluster high level architecture diagram

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MSvBbkykpjkiLXBC9CU%2F-MSvE5wFtOei_jda7rtW%2FOnPremise_Cluster%20\(2\).png?alt=media\&token=da22bd9b-7c35-4b76-805d-6bd75eb7a4e5)

Overview

* **Incoming HTTP Requests** is containing information about a cluster and tenant to which it wants to reach. That info can be attached to requests under different technics but for not only subdomain approach is supported. So each tenant within each cluster is having different subdomain e.g. tenant1.getint.mycompany.com
* **Load balancer** is directing the request to the proper cluster
* **Spring Web Application** is the main heart of the cluster. It is receiving incoming requests, authenticates them, extract info about tenant and performs business logics to return a data
* **React UI** is a chosen framework for building modern UI. Its packaged and included within Spring Web Application and server when user visits administration panel
* **Tenant N Thread** as said before, clusters supports *multi-tenancy*. For every tenant separate integration thread is created which is responsible for performing data synchronization according to configured integrations by tenant users
* **PostgreSQL** is a RDBMS of our default choice. Years of experience with that db system make us sure its the best choice we could as a heart of a platform data storage. One of the biggest advantages we found was different supported ways of data replication and most importantly, possibility to store non-relations data
* **Tenant Schema** is created for each tenant within a database to which that cluster is connected. Each tenant has the access **only** to its schema.&#x20;
