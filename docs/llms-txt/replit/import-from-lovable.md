# Source: https://docs.replit.com/getting-started/quickstarts/import-from-lovable.md

# Import from Lovable

> Learn how to import Lovable projects into Replit by exporting to GitHub first, then importing with Agent assistance.

export const platform_1 = "Lovable"

export const platform_0 = "Lovable"

export const projectType_0 = "project"

export const setupDescription_0 = "Agent validates your project structure and assists with migration to optimize it for the Replit environment"

## Import your Lovable project

⏰ *Estimated time: four minutes*

You can import your Lovable projects into Replit by exporting them to GitHub first, then importing them as Replit Agent Apps.
This quickstart covers the step-by-step process to migrate your Lovable projects to Replit.

For comprehensive import options including other platforms like GitHub, Figma, and Bolt, see the [Import feature documentation](/replit-app/import-to-replit).

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=259c9b27b6acf2b6dcf3f86c26ffebe6" alt="Preview of Lovable project import in Replit" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/lovable.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=197f9b0ff2685f6a7f38e6a9fedee597 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b431c2a506993f7d354798942eca62a4 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=8a615e3800b9273ee28e9c34c810c7a5 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=78a930968ea332f5c2e76314c5eb8085 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=58ecd62f5ef0051f6e939a6a24012661 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b070fecc78967d63c8c9f39fbe6d92c4 2500w" />
</Frame>

## Export and import process

1. **Export your Lovable project to GitHub** from your Lovable workspace.

2. Navigate to <a href="https://replit.com/import" target="_blank">[https://replit.com/import](https://replit.com/import)</a>.

3. Select **Lovable** from the available import sources.

4. **Connect your GitHub account to Replit** to authorize repository access.

5. **Select your new Lovable project repo** for import from the available repositories.

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

* **[Agent](/replitai/agent)**: Use AI to add new features and refine your imported project
* **[Assistant](/replitai/assistant)**: Get help with code questions and debugging
* **[Secrets](/replit-workspace/workspace-features/secrets)**: Add your API keys and environment variables
* **[Workflows](/replit-workspace/workflows)**: Configure the Run button to your preferred command

## Continue your journey

Now that you've imported your {platform_0} {projectType_0}, learn more about what you can do with your Replit App:

* [Replit Agent](/replitai/agent): Get AI assistance with code review, testing, and feature implementation
* [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your app as a Template for others to remix
* [Replit Deployments](/category/replit-deployments): Publish your app to the cloud with a few clicks
* [Database setup](/cloud-services/storage-and-databases/sql-database): Let Agent help you configure and optimize your database
* [Collaborate](/replit-app/collaborate): Work with others on your imported projects
