# Source: https://render.com/docs/migrate-mongodb-static-hosting-to-render.md

# Migrate MongoDB Static Hosting to Render

*MongoDB Atlas Static Hosting is deprecated, with service [ending in March 2025](https://www.mongodb.com/docs/atlas/app-services/migrate-hosting-graphql/).* Render provides a flexible, scalable secure alternative for hosting your static sites.

## About Render

Render is a cloud application platform that helps developers flexibly deploy and scale their apps and services. You can host your static sites on Render alongside the entire rest of your stack (frontend and backend). All static sites deployed on Render are served over a global CDN with automatic management of TLS certificates.

You can easily auto-deploy from a Git repo, preview changes before you merge a pull request, roll back changes when you need to, and more. Render hosts static sites for free, charging only for additional amounts of [outbound bandwidth](outbound-bandwidth).

## Before you begin

1. As a precaution, ensure that you have a backup of your application and data before making any significant changes.
2. [Sign up for Render.](https://dashboard.render.com/register)
3. Make sure your application source is either hosted in a repostitory on [GitHub](github)/[GitLab](gitlab)/[Bitbucket](bitbucket) or available as a [prebuilt Docker image](/deploying-an-image).

## Migrate to Render

You can deploy your static site from the [Render Dashboard](https://dashboard.render.com) in just a few steps:

1. *Push your code to your Git repository.*

   Render enables you to deploy code directly from [GitHub](github), [GitLab](gitlab), and [Bitbucket](bitbucket).

2. *Deploy your code as a static site on Render.*

   See [our docs on Static Sites](static-sites#get-started) for full instructions and links to example code.

3. *[Optional] Add a custom domain.*

   Each static site on Render automatically gets a public `onrender.com` URL. You can also set up a custom domain. See our [docs on custom domains](custom-domains) for full instructions.

4. *Shut down Atlas App Services hosting.*

   After you verify that your application deploys successfully to Render, delete your hosted files from your Atlas App Services app. As a reminder, static sites hosted on Atlas App Services are scheduled to shut down on March 12, 2025.

## Next steps

Check out the Render docs to learn about other [service types](service-types) you can use alongside your new static site.