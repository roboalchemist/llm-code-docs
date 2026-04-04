# Concepts

Source: https://developer.hashicorp.com/nomad/docs/concepts

v1.11.x (latest)
Nomad
v1.10.x
v1.9.x
v1.8.x
No versions of this document exist before v1.8.x. Click below to redirect to the version homepage.
v1.7.x
v1.6.x
v1.5.x
v1.4.x
v1.3.x
v1.2.x
v1.1.x
v1.0.x
v0.12.x
v0.11.x
Nomad Documentation
Nomad is a highly available, distributed, data-center aware cluster and application scheduler designed to support the modern datacenter with support for long-running services, batch jobs, and much more.
API
CLI
Tools
Plugins
Getting Started
Learn how to use Nomad to schedule and orchestrate workloads.
CLI Quick Start
Use Cases
Fundamentals
Become familiar with the core concepts of Nomad.
Installing Nomad
Nomad is available as a pre-compiled binary, a package for several OSs, or as source code for you to build from.
Writing Job Specs
The Nomad job specification or 'jobspec' is written in HCL and defines the schema for Nomad jobs.
Agent Configuration
The Nomad agent specification is written in HCL and defines configs like networking, plugins, and integrations.
Manage Nomad Jobs
Learn how to deploy and manage jobs.
Nomad Pack
Use Nomad Pack to deploy popular applications to Nomad.
Introduction to Nomad Pack
Learn about Nomad Pack and how to use it to easily create, share, deploy, and re-use Nomad job specs.
Write a custom Nomad Pack
Learn how to create your own custom Nomad Pack.
Community Repository
The registry of community-maintained packs for Nomad Pack.
Autoscaling
Automatically maintain your cluster and workload instance count to respond to demand while minimizing over-provisioning cost.
Introduction to Autoscaling
The Nomad Autoscaler is a horizontal application and cluster autoscaler for Nomad.
Horizontal Cluster Autoscaling
Learn how to use the autoscaler to dynamically scale infrastructure up and down and handle application load spikes.
Create On-demand Batch Jobs
Learn how to use the autoscaler to automatically provision and decommission clients for running batch jobs.
Manage Job Placement and Affinities
Learn how to use the affinity stanza to express job placement preferences.
Cluster Management
Learn the features operators will need to build and maintain Nomad clusters.
Upgrade a Cluster
Learn about the process of upgrading a cluster including upgrading in place.
Enable Multi-Region Federation
Learn how to use federation to allow users to submit jobs or interact with the API from any region attached to the cluster.
Connect Nodes into a Cluster
Learn how to connect nodes to a cluster manually, with Cloud Auto-Join, or with Consul.
Enable Autopilot
Learn about the Autopilot features and how to use them to cleanup servers, monitor Raft state, and introduce servers stably.
Developers
Provision Nomad with Terraform
API Reference
Nomad Ecosystem Tools
Community Task Drivers