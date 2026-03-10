# Source: https://developers.webflow.com/data/reference/rest-introduction.mdx

***

title: Introduction
slug: data/reference/rest-introduction
subtitle: Your reference for building successful integrations with the Webflow Data API.
layout: reference
hidden: false
-------------

The Webflow Data API provides an extensive set of RESTful endpoints to help you create advanced tools and applications for Webflow users. This documentation is your guide to building successful integrations.

## Make your first API call

<div class="my-6">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 items-center">
    <div class="prose dark:prose-invert">
      To get started, click the "Try it" button on the Get Sites endpoint to make your first API call. Clicking it will open an interactive API explorer where you can authenticate and send a live request to see a list of your sites.

      Once you authenticate, you can navigate to other endpoints to see the different resources and actions you can perform.
    </div>

    <ApiEndpoint method="GET" endpoint="/v2/sites" link="/data/reference/sites/list?explorer=true" returnPath="/data/reference/rest-introduction" />
  </div>
</div>

## Core concepts

Get familiar with the core concepts of the Webflow Data API.

<CardGroup>
  <Card
    title="Authentication"
    href="/data/reference/authentication"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/SecurityCertified.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/SecurityCertified.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Learn how to authenticate your requests to the Webflow Data API.
  </Card>

  <Card
    title="Rate Limiting"
    href="/data/reference/rate-limits"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/TimeTurner.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/TimeTurner.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Understand the rate limits for the Webflow Data API.
  </Card>

  <Card
    title="Versioning"
    href="/data/reference/versioning"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/BranchMerge.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/BranchMerge.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Learn how to work with API versions.
  </Card>

  <Card
    title="Error Handling"
    href="/data/reference/error-handling"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Support.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Support.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Understand how to handle errors returned by the API.
  </Card>
</CardGroup>

<br />

## API structure

Webflow's API follows a resource model, providing a clear hierarchy for accessing and manipulating data. The diagram below illustrates the main resources and their relationships. Lear more about the response objects for each resource in the [API structure](/data/reference/structure-1) documentation.

<div>
  <iframe src="https://webflow-api-diagram.netlify.app" width="100%" height="800px" />
</div>

## Next steps

Now that you've made your first API call, you're ready to dive deeper.

<CardGroup cols={2}>
  <Card
    title="Developer Guides"
    href="/data/docs/data-clients"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Docs.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Docs.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Follow our guides to build common integrations and workflows.
  </Card>

  <Card
    title="SDKs"
    href="/data/reference/sdks"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Code.svg"
          alt=""
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Code.svg"
          alt=""
          className="block dark:hidden"
        />
      </>
    }
  >
    Explore our official SDKs to accelerate your development.
  </Card>
</CardGroup>

<br />

<Note title="Need to work directly in the Designer?">
  If you're looking to build apps that create and enhance designs within
  Webflow, the [Designer APIs](/designer/reference/introduction) are the right
  tools for the job. These APIs enable you to add and modify elements, styles,
  assets, and more on your design canvas.

  <br />

  <br />

  <a href="/designer/reference/introduction">
    <button class="cc-primary">
      Explore the Designer APIs
    </button>
  </a>
</Note>

<br />
