# Source: https://docs.aws.amazon.com/amplify/latest/userguide/llms.txt

# AWS Amplify Hosting User Guide

> AWS Amplify provides a continuous delivery and hosting service for cloud-powered mobile and web applications.

- [What is AWS Amplify Hosting?](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)
- [Deploying without Git](https://docs.aws.amazon.com/amplify/latest/userguide/manual-deploys.html)
- [Unified webhooks for Git repositories](https://docs.aws.amazon.com/amplify/latest/userguide/unified-webhooks.html)
- [Quotas](https://docs.aws.amazon.com/amplify/latest/userguide/quotas-chapter.html)
- [Document history](https://docs.aws.amazon.com/amplify/latest/userguide/document-history.html)

## [Getting started tutorials](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html)

- [Deploy a Next.js app](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started-next.html): Use Amplify Hosting to deploy a Next.js application from existing code in a Git repository.
- [Deploy a Nuxt.js app](https://docs.aws.amazon.com/amplify/latest/userguide/get-started-nuxt.html): Deploy a Nuxt.js app to Amplify using the preset adapter with no additional configuration.You can use this tutorial to learn how to build and deploy an application created using the Nuxt.js framework.
- [Deploy an Astro.js app](https://docs.aws.amazon.com/amplify/latest/userguide/get-started-astro.html): Deploy an Astro.js app to Amplify using a community adapter.
- [Deploy a SvelteKit app](https://docs.aws.amazon.com/amplify/latest/userguide/get-started-sveltekit.html): Deploy a SvelteKit app to Amplify using a community adapter.


## [Deploying SSR applications](https://docs.aws.amazon.com/amplify/latest/userguide/server-side-rendering-amplify.html)

### [Next.js](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-amplify-support.html)

Describes AWS Amplify deployment and hosting support for Next.js applications.

- [Deploying a Next.js SSR application to Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-app.html): Deploy a Next.js 12 or later application to Amplify Hosting.
- [Migrating a Next.js 11 SSR app to Amplify Hosting compute](https://docs.aws.amazon.com/amplify/latest/userguide/update-app-nextjs-version.html): Migrate an existing Next.js 11 application to Next.js 13 or later and deploy it to the Amplify Hosting compute SSR provider.
- [Adding SSR functionality to a static Next.js app](https://docs.aws.amazon.com/amplify/latest/userguide/redeploy-ssg-to-ssr.html): Add SSR functionality to an existing SSG Next.js app deployed to Amplify Hosting.
- [Making environment variables accessible to server-side runtimes](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-environment-variables.html): Modify your app's build specification to make environment variables accessible to Next.js.
- [Deploying a Next.js app in a monorepo](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-monorepo.html): Learn how to deploy a Next.js app to Amplify in a generic monorepo or in a specific monorepo framework such as Yarn workspace, Nx, or Turborepo.
- [Nuxt.js](https://docs.aws.amazon.com/amplify/latest/userguide/nuxt-support.html): Describes AWS Amplify deployment and hosting support for Nuxt.js applications.
- [Astro.js](https://docs.aws.amazon.com/amplify/latest/userguide/astro-support.html): Describes AWS Amplify deployment and hosting support for Astro.js applications using a community adapter.
- [SvelteKit](https://docs.aws.amazon.com/amplify/latest/userguide/sveltekit-support.html): Describes AWS Amplify deployment and hosting support for SvelteKit applications using a community adapter.
- [SSR supported features](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-supported-features.html): Learn about Amplify's support for specific SSR features, including image optimization, Node.js., CloudWatch logs, custom image loaders, and Next.js 11.
- [Troubleshooting SSR deployments](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-ssr-deployment.html): Get help troubleshooting issues with deploying an SSR app to Amplify Hosting.

### [Advanced: Open source adapters](https://docs.aws.amazon.com/amplify/latest/userguide/advanced-open-source-adapters.html)

Learn how to use the deployment specification to author a framework adapter or configure a post-build script.

- [Deployment specification](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-deployment-specification.html): Learn about the Amplify Hosting deployment specification's folder structure.
- [Deploying an Express server](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-express-server.html): Deploy a Simple Express server using the deployment manifest.
- [Image optimization for framework authors](https://docs.aws.amazon.com/amplify/latest/userguide/integrate-image-optimization-framework.html): Integrate the Amplify Image optimization feature when authoring a framework
- [Using open source adapters for any SSR framework](https://docs.aws.amazon.com/amplify/latest/userguide/using-framework-adapter.html): Learn how to deploy an SSR app to Amplify for any Javascript-based SSR framework with an open sourcecs adapter.


## [Deploying a static website from S3](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-website-from-s3.html)

- [Deploying from the Amplify console](https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html): Use the Amplify console to deploy a static website from an Amazon S3 bucket using the simplified integration with Amazon S3
- [Creating a bucket policy to deploy using the SDKs](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-with-sdks.html): Learn how to create a bucket policy when deploying a static website from S3 to Amplify Hosting using the AWS SDKs.
- [Updating a static website deployed from an S3 bucket](https://docs.aws.amazon.com/amplify/latest/userguide/update-website-deployed-from-s3.html): Use the AWS CLI to update a static website deployed from Amazon S3 to Amplify Hosting.
- [Updating an S3 deployment to use a bucket and prefix instead of a .zip file](https://docs.aws.amazon.com/amplify/latest/userguide/update-s3-zip-to-bucket.html): Learn how to change a current Amazon S3 deployment to Amplify Hosting from using a .zip file to using the bucket name and prefix.


## [Build settings and configuration](https://docs.aws.amazon.com/amplify/latest/userguide/build-settings-configuration.html)

### [Configuring build settings](https://docs.aws.amazon.com/amplify/latest/userguide/build-settings.html)

Learn how to configure and edit the build settings for an app deployed with Amplify Hosting.

- [Build specification reference](https://docs.aws.amazon.com/amplify/latest/userguide/yml-specification-syntax.html): The build specification (buildspec) for an Amplify application is a collection of YAML settings and build commands that Amplify uses to run your build.
- [Editing the build specification](https://docs.aws.amazon.com/amplify/latest/userguide/edit-build-settings.html): Learn how to customize the build settings for an application by editing the build specification in the Amplify console.
- [Monorepo build settings](https://docs.aws.amazon.com/amplify/latest/userguide/monorepo-configuration.html): Configure the build settings for an Amplify application where multiple projects or microservices are stored in a single repository.
- [Customizing the build image](https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-image.html): Learn how to use live package updates or create a custom build environment hosted with Amazon ECR for an Amplify app.
- [Configuring the build instance](https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-instance.html): Learn how to configure your Amplify application's build container to provide your build instance with the CPU, memory, and disk space resources that your application requires.
- [Incoming webhooks](https://docs.aws.amazon.com/amplify/latest/userguide/create-incoming-webhook.html): Create a webhook for an Amplify app to start a build without a commit to your Git repository.
- [Build notifications](https://docs.aws.amazon.com/amplify/latest/userguide/notifications.html): Use notifications to alert stakeholders by email when an Amplify app build succeeds or fails.


## [Connecting a custom domain](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

- [Understanding DNS terminology and concepts](https://docs.aws.amazon.com/amplify/latest/userguide/understanding-dns-terminology-and-concepts.html): Describes basic domains and DNS terminology.
- [Using SSL/TLS certificates](https://docs.aws.amazon.com/amplify/latest/userguide/using-certificates.html): Describes how to use the default provisioned certificate or a custom certificate with a custom domain.
- [Adding a custom domain managed by Amazon RouteÂ 53](https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-amazon-route-53.html): Describes how to connect an app deployed in Amplify to a RouteÂ 53 custom domain.
- [Adding a custom domain managed by a third-party DNS provider](https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-a-third-party-dns-provider.html): Describes how to connect an app deployed in Amplify to a custom domain managed by a third-party DNS provider.
- [Updating DNS records for a domain managed by GoDaddy](https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-godaddy.html): Describes how to connect an app deployed in Amplify to a custom domain managed by GoDaddy.
- [Updating the SSL/TLS certificate for a domain](https://docs.aws.amazon.com/amplify/latest/userguide/to-update-certificate.html): Learn how to switch between using a managed or custom certificate, or change the custom certificate in use for a domain.
- [Managing subdomains](https://docs.aws.amazon.com/amplify/latest/userguide/to-manage-subdomains.html): Describes how to manage the subdomains for an app deployed in Amplify that is connected to a custom domain.
- [Setting up wildcard subdomains](https://docs.aws.amazon.com/amplify/latest/userguide/wildcard-subdomain-support.html): Use a wildcard subdomain to route all subdomains to a branch of your Amplify app.
- [Setting up automatic subdomains for an Amazon RouteÂ 53 custom domain](https://docs.aws.amazon.com/amplify/latest/userguide/to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.html): Set up automatic subdomain creation for the newly connected branches of an Amplify app.
- [Troubleshooting custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domain-troubleshoot-guide.html): Get help troubleshooting the custom domain connection process for an Amplify app.


## [Firewall support for hosted sites](https://docs.aws.amazon.com/amplify/latest/userguide/WAF-integration.html)

- [Enable AWS WAF using the console](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started-using-waf.html): Learn how to add a firewall to an Amplify app using the Amplify or AWS WAF consoles.
- [Remove AWS WAF from an app](https://docs.aws.amazon.com/amplify/latest/userguide/disassociate-web-acl.html): Learn how to remove a firewall from an Amplify app
- [Enable AWS WAF using the CDK](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-waf-CDK.html): View a code example that demonstrates how to use the AWS Cloud Development Kit (AWS CDK) to add a firewall to an Amplify application.
- [How Amplify integrates with AWS WAF](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-waf-configuration.html): Learn about the rules and constraints when associating an AWS WAF with an Amplify application.
- [Firewall pricing](https://docs.aws.amazon.com/amplify/latest/userguide/waf-pricing.html): Learn how costs are calculated when you add a Firewall to an Amplify application.


## [Feature branch deployments](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html)

- [Team workflows with fullstack Amplify Gen 2 apps](https://docs.aws.amazon.com/amplify/latest/userguide/team-workflows-gen2.html): Set up deployment workflows for Gen 2 Amplify apps.
- [Team workflows with fullstack Amplify Gen 1 apps](https://docs.aws.amazon.com/amplify/latest/userguide/team-workflows-with-amplify-cli-backend-environments.html): Set up deployment workflows for Gen 1 Amplify apps.
- [Pattern-based feature branch deployments](https://docs.aws.amazon.com/amplify/latest/userguide/pattern-based-feature-branch-deployments.html): Set up pattern-based feature branch deployments.
- [Automatic build-time generation of Amplify config (Gen 1 apps only)](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-config-autogeneration.html): Automatically create the aws-exports.js file for a Gen 1 Amplify app.
- [Conditional backend builds (Gen 1 apps only)](https://docs.aws.amazon.com/amplify/latest/userguide/conditional-backends.html): Skip the backend build step to speed up your build time when changes have only been made to the frontend.
- [Use Amplify backends across apps (Gen 1 apps only)](https://docs.aws.amazon.com/amplify/latest/userguide/reuse-backends.html): Reuse a Gen 1 backend environment that already exists in your Amplify account when creating or updating a frontend.


## [Building a backend](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-backend.html)

- [Create a backend for a Gen 2 app](https://docs.aws.amazon.com/amplify/latest/userguide/build-backend-Gen2.html): Learn how to create a typescript-based backend for an AmplifyGen 2 application.
- [Create a backend for a Gen 1 app](https://docs.aws.amazon.com/amplify/latest/userguide/build-backend-Gen1.html): Learn how to create a backend for an AmplifyGen 1 application using Amplify Studio.


## [Advanced deployment features](https://docs.aws.amazon.com/amplify/latest/userguide/advanced-deploy-features-chapter.html)

- [Password protect branches](https://docs.aws.amazon.com/amplify/latest/userguide/access-control.html): Learn how to configure the access control settings for an Amplify app and restrict access at the global or branch level.
- [Pull request previews](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html): Learn how to set up set up PR previews to deploy every pull request made to your repository to a unique preview URL.
- [End-to-end testing](https://docs.aws.amazon.com/amplify/latest/userguide/running-tests.html): Learn how to configure your build settings to run end-to-end tests for an Amplify application using the Cypress testing framework.
- [One-click deploy button](https://docs.aws.amazon.com/amplify/latest/userguide/one-click.html): Learn how to add the Amplify deployment button to any page that renders HTML to easily share a GitHub project.


## [Redirects and rewrites](https://docs.aws.amazon.com/amplify/latest/userguide/redirects.html)

- [Creating and editing redirects](https://docs.aws.amazon.com/amplify/latest/userguide/creating-editing-redirects.html): Use the Amplify console to create and edit redirects for an Amplify application.
- [Example redirects and rewrites](https://docs.aws.amazon.com/amplify/latest/userguide/redirect-rewrite-examples.html): Use examples of different types of redirects and rewrites to understand the syntax for creating your own redirects for an Amplify application.


## [Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/environment-variables.html)

- [Setting environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/setting-env-vars.html): Learn how to set environment variables for an Amplify application in the console.
- [Managing environment secrets](https://docs.aws.amazon.com/amplify/latest/userguide/environment-secrets.html): Learn how to set and access secrets for Gen 1 and Gen 2 Amplify applications.


## [Custom headers](https://docs.aws.amazon.com/amplify/latest/userguide/custom-headers.html)

- [YAML reference](https://docs.aws.amazon.com/amplify/latest/userguide/custom-header-YAML-format.html): Understand the syntax to use to specify custom headers for an Amplify application.
- [Setting custom headers](https://docs.aws.amazon.com/amplify/latest/userguide/setting-custom-headers.html): Learn how to set custom HTTP headers for an Amplify app using the Amplify console or by editing the customHttp.yml file.
- [Migrating custom headers](https://docs.aws.amazon.com/amplify/latest/userguide/migrate-custom-headers.html): Learn how to migrate the custom headers for an Amplify app that were previously saved in the build specification or in the amplify.yml file.
- [Monorepo custom headers](https://docs.aws.amazon.com/amplify/latest/userguide/monorepo-custom-headers.html): Learn about the specific requirements for custom headers for applications in a monorepo.


## [Managing cache configuration](https://docs.aws.amazon.com/amplify/latest/userguide/caching.html)

- [How Amplify applies cache configuration](https://docs.aws.amazon.com/amplify/latest/userguide/cache-configuration-type.html): Learn how Amplify determines the type of content being served to efficiently manage caching for an app.
- [Managing cache key cookies](https://docs.aws.amazon.com/amplify/latest/userguide/cache-key-cookies.html): Learn how to include or exclude cookies in the cache key for a application hosted with Amplify.
- [Using the Cache-Control header to increase app performance](https://docs.aws.amazon.com/amplify/latest/userguide/Using-headers-to-control-cache-duration.html): Amplify's default hosting architecture optimizes the balance between hosting performance and deployment availability.


## [Skew protection](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html)

- [Configuring skew protection](https://docs.aws.amazon.com/amplify/latest/userguide/configure-skew-protection.html): Learn how to add or remove skew protection from an Amplify application using the Amplify console.
- [How skew protection works](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection-headers.html): Understand how Amplify applies skew protection when serving content.


## [Monitoring applications](https://docs.aws.amazon.com/amplify/latest/userguide/access-logs.html)

- [CloudWatch metrics and alarms](https://docs.aws.amazon.com/amplify/latest/userguide/monitoring-with-cloudwatch.html): Learn how to use CloudWatch Logs to retrieve supported metrics and set alarms for an Amplify app.
- [Access logs](https://docs.aws.amazon.com/amplify/latest/userguide/using-access-logs.html): Learn how to retrieve and analyze access logs to monitor requests made to your Amplify app.
- [Logging Amplify API calls using AWS CloudTrail](https://docs.aws.amazon.com/amplify/latest/userguide/logging-using-cloudtrail.html): Learn how to use to AWS CloudTrail with AWS Amplify to capture calls from the Amplify console and code calls to the Amplify API operations .


## [Using IAM roles with applications](https://docs.aws.amazon.com/amplify/latest/userguide/add-IAM-roles.html)

- [Adding a service role to deploy backend resources](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-service-role.html): Create an IAM service role with the permissions that Amplify requires to deploy backend resources on your behalf.
- [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html): Create an IAM role with the permissions that an Amplify SSR app requires to securely access specific AWS resources.
- [Adding a service role to access CloudWatch Logs](https://docs.aws.amazon.com/amplify/latest/userguide/cloudwatch-logs-role.html): Configure your app with an IAM service roll to allow Amplify to access Amazon CloudWatch Logs.


## [Security](https://docs.aws.amazon.com/amplify/latest/userguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/amplify/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access to your Amplify resources.

- [How Amplify works with IAM](https://docs.aws.amazon.com/amplify/latest/userguide/security_iam_service-with-iam.html): Learn which IAM features you can use with Amplify.
- [Identity-based policy examples](https://docs.aws.amazon.com/amplify/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amplify resources.
- [AWS managed policies](https://docs.aws.amazon.com/amplify/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amplify and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/amplify/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amplify and IAM.

### [Data Protection](https://docs.aws.amazon.com/amplify/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amplify.

- [Encryption at rest](https://docs.aws.amazon.com/amplify/latest/userguide/encryption-at-rest.html): Encryption at rest refers to protecting your data from unauthorized access by encrypting data while stored.
- [Encryption in transit](https://docs.aws.amazon.com/amplify/latest/userguide/encryption-in-transit.html): Encryption in transit refers to protecting your data from being intercepted while it moves between communication endpoints.
- [Encryption key management](https://docs.aws.amazon.com/amplify/latest/userguide/encryption-key-management.html): AWS Key Management Service (KMS) is a managed service for creating and controlling AWS KMS keys, the encryption keys used to encrypt customer data.
- [Compliance Validation](https://docs.aws.amazon.com/amplify/latest/userguide/Amplify-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure Security](https://docs.aws.amazon.com/amplify/latest/userguide/infrastructure-security.html): Learn how AWS Amplify isolates service traffic.
- [Logging and monitoring](https://docs.aws.amazon.com/amplify/latest/userguide/monitoring-overview.html): Monitor Amplify to maintain reliability, availability, and performance.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/amplify/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how to prevent the confused deputy problem and protect your data for all services with service principals that have been given access to resources in your account.
- [Security best practices](https://docs.aws.amazon.com/amplify/latest/userguide/security-best-practices.html): Learn about best practices for deploying and configuring Amplify applications.


## [Troubleshooting](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting.html)

- [General issues](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-general.html): Learn how to fix general issues that you encounter with applications deployed to Amplify Hosting.
- [AL2023 build image](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-AL2023.html): Describes how to fix AL2023 build image issues that you encounter with applications deployed to Amplify Hosting.
- [Build issues](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-build-issues.html): Learn how to fix issues that you encounter when you build an Amplify application.
- [Custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-custom-domains.html): Learn how to fix issues that you encounter when connecting an Amplify application to a custom domain.
- [Server-side rendering (SSR)](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-SSR.html): Learn how to fix issues that you encounter with deploying SSR applications to Amplify Hosting.
- [Redirects and rewrites](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-redirects.html): Describes how to fix redirect and rewrite issues that you encounter with applications deployed to Amplify Hosting.
- [Caching](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-caching.html): Describes how to fix caching issues that you encounter with applications deployed to Amplify Hosting.
- [Setting up GitHub access](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html): Describes how to install and authorize the Amplify GitHub App to allow read-only access to the repository to use to deploy an app.


## [AWS Amplify Hosting reference](https://docs.aws.amazon.com/amplify/latest/userguide/aws-amplify-reference-chapter.html)

- [AWS CloudFormation support](https://docs.aws.amazon.com/amplify/latest/userguide/cloudformation-support-chapter.html): Use AWS CloudFormation templates to provision Amplify resources, enabling repeatable and reliable web app deployments.
- [AWS Command Line Interface support](https://docs.aws.amazon.com/amplify/latest/userguide/aws-cli-support-chapter.html): Use the AWS Command Line Interface to create Amplify apps programmatically from the command line.
- [Resource tagging support](https://docs.aws.amazon.com/amplify/latest/userguide/resource-tagging-support-chapter.html): You can use the AWS Command Line Interface to tag Amplify resources.
- [Amplify Hosting API](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-api-reference.html): This reference provides descriptions of the actions and data types for the Amplify Hosting API.
