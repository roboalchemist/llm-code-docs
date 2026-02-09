# Source: https://docs.replit.com/getting-started/quickstarts/import-from-bolt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import from Bolt

> Learn how to import Bolt projects into Replit by exporting to GitHub first, then importing with Agent assistance.

export const platform_1 = "Bolt"

export const platform_0 = "Bolt"

export const projectType_0 = "project"

export const setupDescription_0 = "Agent validates your project structure and assists with migration to optimize it for the Replit environment"

## Import your Bolt project

⏰ *Estimated time: four minutes*

<Warning>
  Agent currently only supports Vite + React apps imported from Bolt.
</Warning>

You can import your Bolt projects into Replit by exporting them to GitHub first, then importing them as Replit Agent Apps.

This quickstart covers the step-by-step process to migrate your Bolt projects to Replit.

For comprehensive import options including other platforms like GitHub, Figma, and Lovable, see the [Import feature documentation](/replit-app/import-to-replit).

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0caf2e34824e87c9aee57e3922fb8ecd" alt="Preview of Bolt project import in Replit" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/bolt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=5483a79d99f25c36185e10ebc06ddd18 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=f339ca604e9714d64ce4c25754c3d583 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bf37b85cb66b0473bb827a5e7b50821d 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=a3192355bf00cfeebce86edd43010958 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=02d298e6954056345e124e81fb713c4e 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/bolt.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=ee88ce360ab102a2540783ef5d4ef4ec 2500w" />
</Frame>

## Export and import process

1. **Export your Bolt project to GitHub** from your Bolt workspace.

2. Navigate to <a href="https://replit.com/import" target="_blank">[https://replit.com/import](https://replit.com/import)</a>.

3. Select **Bolt** from the available import sources.

4. **Connect your GitHub account to Replit** to authorize repository access.

5. **Select your new Bolt project repo** for import from the available repositories.

6. Select **Import** to start the migration process.

## What gets imported

During the import process, Replit migrates your {platform_1} project with Agent assistance:

* **Code**: All application code and logic from your {platform_1} project
* **Design and styles**: UI components, styling, and visual design elements
* **Assets**: Images, icons, and other static resources
* **Backend functionality**: If your {platform_1} project includes backend functionality, it is imported into the Replit environment.
* **Database schema**: Database structure and table definitions are imported into a Neon Postgres database, which is integrated directly into the Replit environment.

### What's not included

* **Supabase database**: Database content and data are not migrated
* **Secrets**: Environment variables and API keys must be added separately

You can ask Agent to help build out functionality, add secrets, and recreate databases in your new app.

## Configure and run your app

During the import process, {setupDescription_0}.
If your app doesn't run as expected, Replit offers the following workspace tools to help you resolve the issues:

* **[Agent](/replitai/agent)**: Use AI to add new features, refine your imported project, and get help with code questions
* **[Secrets](/replit-workspace/workspace-features/secrets)**: Add your API keys and environment variables
* **[Workflows](/replit-workspace/workflows)**: Configure the Run button to your preferred command

## Continue your journey

Now that you've imported your {platform_0} {projectType_0}, learn more about what you can do with your Replit App:

* [Replit Agent](/replitai/agent): Get AI assistance with code review, testing, and feature implementation
* [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your app as a Template for others to remix
* [Replit Deployments](/category/replit-deployments): Publish your app to the cloud with a few clicks
* [Database setup](/cloud-services/storage-and-databases/sql-database): Let Agent help you configure and optimize your database
* [Collaborate](/replit-app/collaborate): Work with others on your imported projects
