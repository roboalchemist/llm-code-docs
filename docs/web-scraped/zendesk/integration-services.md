# Source: https://developer.zendesk.com/documentation/integration-services/

# Zendesk Integration Services | Zendesk Developer Docs zendev_horizontal zendev_horizontal Documentation API Reference Search / Integration Services Home

-
-

## Integration Services

- Introduction

-
-

### Getting Started

- Understanding Zendesk Integration Services

- Anatomy of a ZIS bundle

- Understanding ZIS capabilities for building an integration

- ZIS Frequently Asked Questions (FAQs)

-
-

### Developer Guide

- Developing private ZIS integrations

- ZIS flow states
- Understanding flow states

- Action state

- ZIS built-in actions

- ZIS custom actions

- Choice state

- Fail state

- Map state

- Pass state

- Succeed state

- Wait state

- Flow states retry and error handling

- Encoding URL Parameters

- jq cheat sheet

- ZIS configs

- Connections
- Understanding connections

- Creating and managing OAuth connections

- ZIS links

- Security best practices for ZIS integrations

- Fixing common ZIS errors

- Glossary

-
-

### Integration design guidelines

- Introduction

- Understanding the admin user journey

- Designing your installation and OAuth flow for a private integration

- Designing configuration pages

- Designing an uninstall flow

-
-

### Zendesk Integration Services examples

- ZIS action: Converting a number to a string

- ZIS action: Getting the current date

- ZIS bundle: Adding a Choice state

- ZIS bundle: Creating an HTTP request body using jq

- ZIS bundle: Parsing and sending an event to an external API

- ZIS bundle: Posting a message in Slack when the ticket status changes

-
-

### Zendesk Integration Services tutorials

- Getting started
- Building your first ZIS integration

- Using a ZIS action to make authenticated API requests

- Using conditional branching in a ZIS flow

- Transforming data in a ZIS flow

- Iterating over a collection in a ZIS flow

- Using ZIS Links

- Using ZIS inbound webhooks

- Kicking off a ZIS flow with user activity events

- Using JWTs to verify requests from ZIS

- Zendesk app as an admin interface
- Part 1: Build a Zendesk app with OAuth

- Part 2: Connect to Slack

- Part 3: Add a configuration UI

- Part 4: Install the integration

## On this page

- What is Zendesk Integration Services (ZIS)?

- Getting started

- Reference information

# Zendesk Integration Services

Build and run an integration

## What is Zendesk Integration Services (ZIS)?

ZIS is a set of Zendesk-hosted web services that let you integrate Zendesk with other systems and applications. ZIS powers Conversational Data Orchestration, a feature set for automating workflows based on events.

ZIS reduces or eliminates the need to build and host middleware for integration features such as:

- Ingesting webhooks from an external system

- Executing business logic in response to events

- Making API calls into Zendesk and the external system

- Obtaining and managing authentication tokens

- Storing configuration settings

- Storing metadata about related objects in Zendesk and the external system

ZIS simplifies the process to build and run private integrations.

## Getting started

Understanding Zendesk Integration Services
Learn about ZIS services and the resources used to build an integration.

Anatomy of a ZIS bundle
Learn how a ZIS bundle is a declaration of your resources in an integration.

Building your first ZIS integration
Get hands-on. This tutorial shows you how to build your first ZIS integration from scratch and run it.

Designing an integration
Learn about designing your installation and OAuth flow for your integration.

ZIS Frequently Asked Questions
Find answers to common questions about ZIS.

Introduction to ZIS
Learn the key features of ZIS in this free, on-demand training course.

## Reference information

Refer to the ZIS APIs to build your integration and the Trigger events schema when designing an integration to respond to Zendesk events.

ZIS APIs
Trigger events reference
Join our developer community Forum Blog Slack Zendesk 181 Fremont Street, 17th Floor, San Francisco, California 94105 Privacy Notice Zendesk Developer Terms System Status
