# Source: https://docs.replit.com/getting-started/quickstarts/import-from-zip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import from ZIP

> Learn how to import ZIP files into Replit by uploading your compressed project and letting Agent handle the setup.

export const platform_0 = "ZIP"

export const projectType_0 = "project"

export const setupDescription_0 = "Agent automatically sets up your app's environment and dependencies and configures run commands for the Replit environment"

## Import your ZIP project

⏰ *Estimated time: three minutes*

You can import your projects into Replit by uploading a ZIP file containing your codebase. Agent scans your code and handles the setup automatically.

This quickstart covers the step-by-step process to import your ZIP-compressed projects to Replit with a clean workflow, live preview, and logs.

For comprehensive import options including other platforms like GitHub, Figma, Bolt, Lovable, and Vercel, see the [Import feature documentation](/replit-app/import-to-replit).

<Frame>
  <img src="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=9eb1f09cdab8be319791a4a48899cab8" alt="Preview of ZIP project import in Replit" data-og-width="2718" width="2718" data-og-height="1394" height="1394" data-path="images/workspace/import/zip.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=280&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=9f09c5379d74ae9d707a6fc9eefb995f 280w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=560&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=1ffde19ff35abc3045f335508f687e97 560w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=840&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=34a1d53fba8b8dcbaf3735ed2f4d822d 840w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=1100&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=2af24ed9b95d414d16889b7f3f1c1450 1100w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=1650&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=18c2f2e006c470bc40c4224ca7b97872 1650w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/zip.png?w=2500&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=fad236b7cf95685f82887dacedf28f39 2500w" />
</Frame>

## Import process

1. Navigate to <a href="https://replit.com/import" target="_blank">[https://replit.com/import](https://replit.com/import)</a>.

<Frame>
  <img src="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=da889239a53ed37e7d3434a2a8a34557" alt="Replit import interface showing available sources" data-og-width="2314" width="2314" data-og-height="1026" height="1026" data-path="images/workspace/import/importer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=280&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=78fd4da44bc74153eac8aa8b8580576b 280w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=560&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3650524ad81098c312509c0be726d613 560w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=840&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=80c475f748da291593f20aa586855cbb 840w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1100&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3564782931bb3ddf96cc85f55be6b471 1100w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1650&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=d4a3d1aa5c113359124c9e7c0467b48d 1650w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=2500&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=215bae2f594267c3365bd1c4e8d3659c 2500w" />
</Frame>

2. Select **ZIP** from the available import sources.

3. **Upload your ZIP file** containing your project files.

4. **Provide environment variables** when prompted by Agent. Only non-standard secrets and environment variables will be requested.

5. Select **Import** to start the migration process.

## What gets imported

During the import process, Replit extracts and converts your ZIP file into a functional Replit App:

* **Project structure**: Complete codebase and file organization
* **Dependencies**: Package files and dependency management
* **Build configuration**: Optimized for Replit's environment
* **Environment setup**: Runtime and framework configuration

## What's not included

The following items from your ZIP file are not automatically imported:

* **Environment variables**: You'll be prompted to provide these during import
* **Custom domains**: Set up separately in Replit Deployments
* **Platform-specific configurations**: Some configurations may need adjustment
* **Analytics and monitoring**: Use Replit's built-in monitoring tools
* **Databases**: The database from your original project is not included
* **Connectors**: Any connectors will need to be reconnected after import

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
* [Collaborate](/replit-app/collaborate): Work with others on your imported projects
