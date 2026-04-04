# Source: https://clickwrap-developer.ironcladapp.com/docs/getting-started.md

# Introduction

Hi there! Welcome to the Ironclad Clickwrap Developer Portal. We have a rich set of developer tools to help you integrate into your own environment.

> 📘 We are in the process of renaming PactSafe to Ironclad Clickwrap in our developer docs
>
> You may notice various places in this documentation refer to "PactSafe". Ironclad acquired PactSafe in March 2021 and has renamed the product to be Ironclad Clickwrap.

# Orientation

## Why do customers use Ironclad Clickwrap?

First designed for billions of terms of service acceptances a year, Ironclad Clickwrap is an API-first system to help you update, embed, track, and accept any type of contract that is native to your digital experience.

## Customers use Ironclad Clickwrap to do things like...

Let legal directly update & manage all of their online legal content, like terms, consents, and disclosures\
Automatically capture and report on the evidence needed to authenticate legal terms in a court case, audit, or regulatory inquiry.

Dynamically draft and present complicated contracts for acceptance or signature.

## Why do development teams love using Ironclad Clickwrap?

Ironclad Clickwrap is the only embedded contracting tool that allows you to fully customize your UX for acceptance, while staying legally compliant & enforceable. Our JS & Activity API components were designed to either allow you to use our UI components or embed quietly using your own.

In addition, when embedded contracts are handled in-house, it creates risk and technical debt for businesses. When legal teams are faced with court cases or audits around embedded contracts, developers can be left on the hook to testify to how systems were built unless an external authentication system is used. Tech teams also become the gatekeepers between online terms and the legal team, meaning fixing that typo someone caught can become unplanned work that distracts from core competencies.

As you begin to work with Ironclad Clickwrap, you’ll find that our system features three core technical services that work together or independently, depending on your use case - **Clickwrap Groups** for *embedding contracts & tracking acceptance*, **Snapshots** for *automated UX capture, and our legal content management service*.

# Core services:

## Clickwrap Groups  *(for embedding and tracking acceptance)*

*Before you get started with our SDKs or APIs, you'll need to take the following actions in your Ironclad Clickwrap account.*

### Uploading a contract/getting started with our editor

Before you can embed a contract into your page, you'll need to upload a contract. [Check out this article to get started](https://support.ironcladapp.com/hc/en-us/articles/13621141941271-Create-and-Manage-Templates).

## Choose between a static or dynamic template

For dynamic templates, you'll need to start with setting tokens in your templates. [Get started with dynamic templates](https://support.ironcladapp.com/hc/en-us/articles/12402908815511-Create-Dynamic-Templates)

### Configure your Clickwrap Group

Templates can be grouped together for display and acceptance. To define which templates should be used and what the experience should look like, [check out this article](https://support.ironcladapp.com/hc/en-us/articles/13622030976663-Clickwrap-Groups-Overview).

## Acceptance Tracking

### Javascript Library

Our JavaScript library allows you to integrate acceptance tracking using Ironclad Clickwrap in your own environment. The JavaScript library utilizes our Activity API, which is a microservice designed for fast and reliable acceptance tracking. Learn more about the JavaScript library on the [JavaScript Library](https://clickwrap-developer.ironcladapp.com/docs/javascript-library-getting-started) page.

### Activity API

Our Activity API is a separate API (from our REST API) designed for **sending acceptance** data to the Ironclad Clickwrap platform, checking the acceptance status of a Signer, or retrieving data for creating a Clickwrap experience. Learn more about using our Activity API [here](/docs/activity-api).

### REST API

Our REST API—which also powers our web app—can be used to create contracts, retrieve data from the Ironclad Clickwrap platform, or to manage the settings and sites even within your own Ironclad Clickwrap account! For acceptance tracking, gain more customizability and freedom with our REST API. With plenty of power, we also have plenty of documentation—which can be located [here](/docs/getting-started-rest-api).

> 🚧 API Key Requirement
>
> Please note that our REST API **does** require an API key to be used on **all** API calls.

### Our SDKs - Acceptance and/or Contract Management

We have several SDKs available to be used. Each SDK will typically only cover acceptance tracking but some newer versions may cover more advanced use cases. Please feel free to peruse our available SDKs on our [GitHub account](https://github.com/pactsafe) to see all of our libraries!

### Re-acceptance and what to do when terms change

When terms change and users need to re-accept the new version of the terms, check out this article on [Checking Acceptance on Login](https://clickwrap-developer.ironcladapp.com/docs/prompting-your-user-on-login).

## Snapshots

Can be configured using command builder via our dashboard or uploaded directly via the [API for native mobile integrations](https://clickwrap-developer.ironcladapp.com/reference/snapshots).

Get started with snapshots by checking out [this article](https://support.ironcladapp.com/hc/en-us/articles/12448605308055-Snapshots-Overview#:~:text=Snapshots%20enable%20you%20to%20keep,with%20manual%20uploads%20if%20necessary.).

## Legal content management

You can either set up an Ironclad-hosted legal center directly through our dashboard or pull the content.

this link explains how to [Integrating Ironclad Clickwrap with your web content management system](https://clickwrap-developer.ironcladapp.com/page/integrating-pactsafe-with-your-web-content-management-system)