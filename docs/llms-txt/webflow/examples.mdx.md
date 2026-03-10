# Source: https://developers.webflow.com/data/examples.mdx

***

title: Examples
slug: examples
description: Examples of how to use the Webflow Cloud API
hidden: false
layout: custom
--------------

{/* <!-- vale off --> */}

<div>
  <ExamplesContainer
    cols={3}
    examples={[
      {
        title: "Designer API Playground",
        description: "Interactive playground demonstrating Designer API capabilities for interacting with the Webflow Designer.",
        liveUrl: "https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62",
        products: ["Designer Extension"],
        image: "https://cdn.prod.website-files.com/64f93520898fc6f3157fe5bb/6762e2d9973fb410af1e44b2_developers_sticky-design-experience.webp",
        imageAlt: "Designer API Icon",
      },
      {
        title: "Careers Page",
        description: "Next.js careers page that can be deployed to Webflow Cloud. This example integrates Webflow DevLink components and uses the Greenhouse API to display job listings.",
        liveUrl: "https://astral-cloud-start.webflow.io/careers",
        repoUrl: "https://github.com/Webflow-Examples/careers-page-webapp",
        products: ["Webflow Cloud"],
        imageAlt: "Webflow Cloud Icon",
        image: "https://cdn.prod.website-files.com/686431ad597a0e8140e9a6b2/6876e137118dad4e1eec6e79_Screenshot%202025-07-15%20at%206.15.58%E2%80%AFPM.png",
        framework: "Next.js"
      },
      {
        title: "OAuth Example",
        description: "Starter template showcasing Webflow OAuth authentication and API integration.",
        repoUrl: "https://github.com/Webflow-Examples/webflow-app-starter-v2",
        products: ["Data Client"],
        imageAlt: "Data Client Icon",
      },
      {
        title: "Hybrid App Example",
        description: "Starter template showcasing Webflow Hybrid App with Data Client and Designer Extension capabilities.",
        repoUrl: "https://github.com/Webflow-Examples/hybrid-app-starter",
        products: ["Data Client", "Designer Extension"],
        imageAlt: "Hybrid App Icon",
      },
      {
        title: "CMS Example",
        description: "Data Client app showing how to use the Webflow CMS API to fetch and update content.",
        repoUrl: "https://github.com/Webflow-Examples/cms-examples",
        products: ["Data Client"],
        image: "https://cdn.prod.website-files.com/64f93520898fc6f3157fe5bb/6762dc375b41c77e82fa1b66_developers_webflow-integrations.webp",
        imageAlt: "CMS Image",
      },
      {
        title: "LLMS.txt Generator",
        description: "Create an LLMS.txt file for your Webflow site.",
        liveUrl: "https://hello-webflow-cloud.webflow.io/llmstxt",
        repoUrl: "https://github.com/Webflow-Examples/llms-txt-generator-webapp",
        products: ["Webflow Cloud"],
        framework: "Astro"
      },
      {
        title: "BetterAuth - Next.js",
        description: "BetterAuth integration using SQLite database with Next.js to persist user sessions",
        liveUrl: "https://clone-auth-test.webflow.io/app/login",
        repoUrl: "https://github.com/Webflow-Examples/auth-cloud-webapp/tree/main/betterauth-nextjs",
        products: ["Webflow Cloud"],
        image: "https://cdn.prod.website-files.com/686431ad597a0e8140e9a6b2/6876dfefc671a20280b09e28_Screenshot%202025-07-15%20at%206.10.24%E2%80%AFPM.png",
        framework: "Next.js"
      },
            {
        title: "BetterAuth - Astro",
        description: "BetterAuth integration using SQLite database with Astro to persist user sessions",
        liveUrl: "https://auth-cloud-test.webflow.io/app/login",
        repoUrl: "https://github.com/Webflow-Examples/auth-cloud-webapp/tree/main/betterauth-astro",
        image: "https://cdn.prod.website-files.com/686431ad597a0e8140e9a6b2/6876dfefd74623f64680a2e4_Screenshot%202025-07-15%20at%206.10.15%E2%80%AFPM.png",
        products: ["Webflow Cloud"],
        framework: "Astro"
      },
      {
        title: "Pricing Calculator",
        description: "A Pricing calculator built in React for Code Components",
        liveUrl: "https://cc-test-66117f.webflow.io/insurance-quote-widget/",
        repoUrl: "https://github.com/Webflow-Examples/code-components-examples/blob/main/pricing-quote-calculator/README.md",
        products: ["Code Components"],
        image: "https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fwebflow.docs.buildwithfern.com%2F2025-09-17T13%3A28%3A21.262Z%2Fproducts%2Fassets%2Fimages%2Fexample-hero%2Fpricing-calculator.png&w=3840&q=75",
        framework: "React"
      },
            {
        title: "Store Locator",
        description: "A Store Locator component built in React for Code Components",
        liveUrl: "https://store-finder-example.webflow.io/",
        repoUrl: "https://github.com/Webflow-Examples/code-components-examples/blob/main/store-locator/README.md",
        products: ["Code Components"],
        image: "https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fwebflow.docs.buildwithfern.com%2F2025-09-17T13%3A28%3A21.262Z%2Fproducts%2Fassets%2Fimages%2Fexample-hero%2Fstore-locator.png&w=3840&q=75",
        framework: "React"
      },
                  {
        title: "Multi-Step Form",
        description: "A dynamic multi-step form built in React for Code Components",
        liveUrl: "https://hello-webflow-cloud.webflow.io/form",
        repoUrl: "https://github.com/Webflow-Examples/code-components-examples/blob/main/multi-step-form/README.md",
        products: ["Code Components"],
        image: "https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fwebflow.docs.buildwithfern.com%2F2025-09-17T13%3A28%3A21.262Z%2Fproducts%2Fassets%2Fimages%2Fexample-hero%2Fdynamic-form.png&w=3840&q=75",
        framework: "React"
      },
      {
        title: "ShadCN/UI Components",
        description: "A collection of direct ShadCN/UI components built in React for Code Components",
        liveUrl: "https://shadcn-ui-code-components.webflow.io/",
        repoUrl: "https://github.com/Webflow-Examples/code-components-examples/tree/main/shadcn-components",
        products: ["Code Components"],
        image: "https://i.imgur.com/evvsuRp.png",
        framework: "React"
      },
      {
        title:"CMS Slider",
        description: "A CMS Slider component built in React for Code Components",
        liveUrl:"https://cms-slider-4d63c4.webflow.io/",
        repoUrl:"https://github.com/Webflow-Examples/code-components-examples/blob/main/cms-slider/README.md",
        products: ["Code Components"],
        framework: "React",
        image:"https://i.imgur.com/hFZGYpe.gif",
        imageAlt:"CMS Slider Image",
      },
      {
        title:"CMS Filter & Search",
        "description": "A CMS Filter and Search component built in React for Code Components",
        liveUrl:"https://cms-filter-code-components.webflow.io/",
        "repoUrl":"https://github.com/julianmemberstack/cms-filters",
        products: ["Code Components"],
        framework: "React",
        image:"https://i.imgur.com/6TIj5zE.gif",
        imageAlt:"CMS Filter & Search Image",
      }
    ]}
  />
</div>

{/* <!-- vale on --> */}
