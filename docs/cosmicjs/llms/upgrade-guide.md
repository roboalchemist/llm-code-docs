# Source: https://www.cosmicjs.com/docs/upgrade-guide.md



# Upgrade Guide

Use the following guide to upgrade from the v1 dashboard to the new dashboard. If you are a new user of Cosmic, you can ignore this guide.

> **IMPORTANT NOTE:**
> 
  **IMPORTANT**
  
> 
  The dashboard v1 service and API resources are now sunset. If you haven't
  already, you will need to migrate to the new dashboard as soon as you can.
  Learn more in the
  [announcement](https://www.cosmicjs.com/blog/cosmic-dashboard-v1-and-api-service-deprecation).
  Reach out to [Cosmic support](https://www.cosmicjs.com/contact) if you have
  any questions.

## Dashboard v1

1. Location: https://app-v1.cosmicjs.com
2. REST API versions: `v1`, `v2`
3. GraphQL API versions: `v1`,`v2`,`v3`

## New dashboard

1. Location: https://app.cosmicjs.com
2. REST API version: `v3`
3. GraphQL API version: `none`

## Important notes

1. Even if you have an account on the v1 dashboard, to use the new dashboard, you will need to create a new account with the new dashboard. Create one [here](https://app.cosmicjs.com/signup).
2. The new dashboard and API v3 are **completely isolated** from the v1 dashboard and prior REST API and GraphQL API versions. This means that anything you do in the new dashboard WILL NOT affect anything currently in production or connected to the v1 dashboard or prior API versions. This is to ensure a smooth upgrade process with no possibility of breaking anything currently in production connected to the v1 dashboard and APIs.
3. We encourage you and your team to start preparing to upgrade to the new dashboard as soon as you can.
4. Read [the changelog](https://www.cosmicjs.com/changelog) for details on new features, improvements, and any possible breaking changes from the v1 dashboard and API.

## Upgrade steps

To upgrade to the new dashboard follow the steps below:

### Export Bucket from the v1 dashboard

1.  [Log in to the v1 dashboard](https://app-v1.cosmicjs.com/login) and go to _Bucket Settings > Import / Export_.
2.  Find the area on this page titled “Dashboard v2 compatibility” and run the report. Note any compatibility issues that may occur with the migration. You should see detailed notices of any issues found. These issues can be fixed in the v1 dashboard, or in the new dashboard. If you encounter a general error with the compatibility checker, you may go ahead and try the migration anyway which may prove successful.
3.  Find the area titled "Export Bucket Data". Download your Bucket data file and have it ready to import into the new dashboard.

### Sign up and log in to the new dashboard

1.  [Sign up for the new dashboard](https://app.cosmicjs.com/signup) (it will require a new sign up and takes seconds to complete).
2.  Create a new project and Bucket from scratch and go to _Bucket Settings > Import / Export._
3.  Upload your Bucket export file from the v1 dashboard into your new Bucket. Note: It may take some time depending on the size of your export file.
4.  After the import is complete, you should see all of your Bucket content populated in the new dashboard.

### Connect your application

Connect your application to the new API v3 using your new API access keys (found in the dashboard _Project > API Access_) to make sure everything is working properly in your application. If you were using a client library, see the client library updates below.

- **Cosmic NPM module** - If you were using the [old Cosmic NPM module](https://www.npmjs.com/package/cosmicjs), we have a new [Cosmic JavaScript SDK](https://www.npmjs.com/package/@cosmicjs/sdk) connected to the v3 API.
- **Gatsby source plugin** - If you were using the [old Gatsby source plugin for Cosmic](https://www.npmjs.com/package/gatsby-source-cosmicjs), we have a new [Cosmic source plugin for Gatsby](https://www.npmjs.com/package/@cosmicjs/gatsby-source-cosmic) connected to the v3 API.

Review the [changelog](https://www.cosmicjs.com/changelog) for any updates that may require your attention.

### Testing

Test your content by adding and editing Objects, doing your content editing workflows, making sure everything is working properly in the new dashboard.

### Invite team members, upgrade your plan, and deploy to production

1.  When you have thoroughly tested the new dashboard and API with your application, and confirmed production readiness, the next step is to invite your team members for further testing. This may require a plan upgrade.
2.  If you have a lot of team members to invite, you can export your team members via CSV file from dashboard v1 in _Bucket Settings > Team_ and import them into the new dashboard located in _Project > Team_.
3.  Deploy your application to production connected to the v3 API.

### Remove projects from the v1 dashboard

1.  After you have completely moved your projects over to the new dashboard and API, deployed your app to production, you can safely delete your projects from the v1 dashboard.

## Contact us

Reach out to [Cosmic support](https://www.cosmicjs.com/contact) if you run into any issues or have any questions. We are also available for a call to provide dedicated support for your upgrade if needed.

## Video guide

Watch the following video guide to learn how to upgrade to the new dashboard.

**Video content is available in the web documentation.**

We hope you enjoy using the new dashboard and we can’t wait to see what you build! 🛠️🚀
