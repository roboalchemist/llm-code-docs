# Source: https://docs.anyscale.com/get-started/org-overview.md

# Anyscale organization overview

[View Markdown](/get-started/org-overview.md)

# Anyscale organization overview

This page provides an overview of the core constructs and concepts of an Anyscale organization. Understanding these concepts is important for navigating, configuring, and using Anyscale.

## What is an Anyscale organization?[​](#what-is "Direct link to What is an Anyscale organization?")

An Anyscale organization is an isolated tenant that encompasses all of the assets, resources, permissions, and artifacts.

You create an organization when you sign up for Anyscale as a new user. Most customers have a single organization, meaning that if you're not the first user of Anyscale in your company, an admin likely invited you to an existing Anyscale organization.

Many configuration and admin actions require that you're an organization owner. See [User and access management](/administration/organization.md).

## Anyscale organization levels[​](#levels "Direct link to Anyscale organization levels")

The following diagram shows the hierarchy of levels in an Anyscale organization:

![Diagram showing an organization, clouds, projects, and Ray clusters](/assets/images/org-hierarchy-a2b36cbf1f92458558d80f010bd80016.png)

| Concept      | Description                                                                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Organization | An isolated Anyscale tenant tied to a billing account. All customer assets tracked and managed by Anyscale are part of an organization.                                                                                                                                      |
| Cloud        | An Anyscale cloud is an isolated deployment of Anyscale on top of cloud resources or Kubernetes. See [Introduction to Anyscale clouds](/admin/cloud.md).                                                                                                                     |
| Project      | A project is an isolated collection of resources and assets within an Anyscale cloud. Use projects to isolate developer teams, separate environments, and organize resources in the same Anyscale cloud. See [What is a project?](/administration/organization/projects.md). |
| Ray clusters | Workspace, jobs, and services are types of Ray clusters you configure and launch on Anyscale. See [Define a Ray cluster](/configuration.md).                                                                                                                                 |
