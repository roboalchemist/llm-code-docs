# Source: https://docs.replit.com/replit-app/import-to-replit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import

> Importing projects and designs from external tools into Replit Agent Apps.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

export const platform_1 = "Lovable"

export const platform_0 = "Bolt"

export const TeamsCredits = '$40';

export const CoreCredits = '$25';

Replit's import feature allows you to transform existing projects and designs from external development and design tools into Replit Agent Apps. This reference covers supported platforms, technical specifications, limitations, and compatibility requirements.

<Frame>
  <img src="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=da889239a53ed37e7d3434a2a8a34557" alt="Preview of Figma design import in Replit" data-og-width="2314" width="2314" data-og-height="1026" height="1026" data-path="images/workspace/import/importer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=280&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=78fd4da44bc74153eac8aa8b8580576b 280w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=560&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3650524ad81098c312509c0be726d613 560w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=840&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=80c475f748da291593f20aa586855cbb 840w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1100&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3564782931bb3ddf96cc85f55be6b471 1100w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1650&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=d4a3d1aa5c113359124c9e7c0467b48d 1650w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=2500&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=215bae2f594267c3365bd1c4e8d3659c 2500w" />
</Frame>

## Supported import sources

Replit's import feature supports the following external platforms:

* **Figma**: Convert design frames into React applications using AI-powered code generation
* **Bolt**: Import existing Bolt projects and migrate them to Replit Agent Apps
* **Lovable**: Transfer Lovable projects to Replit with Agent assistance
* **Vercel**: Import Vercel projects by linking your GitHub repository with Agent assistance
* **Replit Agent**: Import previously exported Agent Apps from GitHub repositories
* **GitHub**: Import compatible repositories as Agent Apps
* **ZIP**: Import ZIP files containing your project files

<Note>
  All imported projects are validated for Agent compatibility before conversion
  begins.
</Note>

## Quickstart guides

For step-by-step instructions to import from each platform, see the quickstart guides:

<CardGroup cols={2}>
  <Card title="Import from GitHub" icon="github" href="/getting-started/quickstarts/import-from-github">
    ⏱️ *2 minutes*

    Import an existing GitHub repository into Replit.
  </Card>

  <Card title="Import from Figma" icon="figma" href="/getting-started/quickstarts/import-from-figma">
    ⏱️ *3 minutes*

    Convert your Figma designs into functional React applications.
  </Card>

  <Card title="Import from Vercel" icon="triangle" href="/getting-started/quickstarts/import-from-vercel">
    ⏱️ *3 minutes*

    Import your Vercel projects by linking your GitHub repository.
  </Card>

  <Card title="Import from Bolt" icon="bolt" href="/getting-started/quickstarts/import-from-bolt">
    ⏱️ *4 minutes*

    Migrate your Bolt projects to Replit with Agent assistance.
  </Card>

  <Card title="Import from Lovable" icon="heart" href="/getting-started/quickstarts/import-from-lovable">
    ⏱️ *4 minutes*

    Transfer your Lovable projects to Replit and continue building.
  </Card>

  <Card title="Import from ZIP" icon="file-zip" href="/getting-started/quickstarts/import-from-zip">
    ⏱️ *3 minutes*

    Import your ZIP projects by uploading your existing .zip file.
  </Card>
</CardGroup>

## Features

* **Automatic compatibility validation**: Ensures imported projects work with Replit Agent
* **AI-powered migration**: Agent assists with project setup and feature completion
* **Design-to-code conversion**: Transform Figma designs into functional React applications
* **Enterprise-ready templates**: Import customized Agent Apps with internal configurations
* **Real-time progress tracking**: Monitor import status with detailed progress updates

## Usage

### Accessing the import feature

1. Navigate to [replit.com/import](https://replit.com/import)
2. Select your desired import source from the available options
3. Follow the platform-specific import workflow

### Import workflow

The import process follows these general steps:

<AccordionGroup>
  <Accordion title="1. Source selection and validation">
    Choose your import source and provide the necessary project information. The system validates compatibility with Agent before proceeding.

    If your project is incompatible, you'll see an error message with suggestions for resolving compatibility issues.
  </Accordion>

  <Accordion title="2. Import processing">
    During the import process, you'll see an interstitial screen showing progress updates. Processing time varies based on project complexity and source platform.

    <Frame>
      <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d27e3e9f76e7381f431826ee8d90bdb4" alt="Import progress interstitial screen" data-og-width="712" width="712" data-og-height="708" height="708" data-path="images/workspace/import/figma-progress.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0b085b04ed7fd033f443ed9a394b32d6 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=379f2c481bccebb3fdb982d2c1790c54 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=acddb443b71f5459b5844e89c35679ff 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=37b802bbd51bdab8d4b5cf947a09a994 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=11ccebc33e5e592f5bd08ca9a59ec94b 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d04aa6d5d23bb713f3882bb57ace148c 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="3. Agent integration">
    Once import completes, Agent engages to finalize the setup and ensure your project is ready for development. This is similar to the end state of Agent Rapid Build.
  </Accordion>
</AccordionGroup>

## Platform-specific workflows

<AccordionGroup>
  <Accordion title="Figma imports" icon="figma">
    Import your Figma designs directly into Replit Agent Apps and turn them into functional web applications.

    <YouTubeEmbed videoId="NBiFBZaBnaE" />

    ### Getting started

    1. **Connect your Figma account** to authorize access to your designs
    2. **In Figma, select the frame** you want to build in Replit
    3. **Copy the frame URL and paste it** into the Replit import interface

    For a full guide on how to import a Figma design, see our [quickstart guide](/getting-started/quickstarts/import-from-figma).

    ### What we'll import

    * **Theme & components**: Design system elements, colors, typography, and reusable components
    * **Assets & icons**: Images, icons, and other visual assets from your design
    * **App scaffolding**: Basic application structure and layout framework

    ### Import process

    1. Provide your Figma frame URL or file details
    2. The system converts your design into React code
    3. Agent wires the generated code to a JavaScript stack
    4. Your design becomes a functional web application

    <Tip>
      Ensure your Figma designs are well-structured with clear component hierarchies
      complete with auto layout constraints for optimal conversion results.
    </Tip>
  </Accordion>

  <Accordion title="Vercel imports" icon="triangle">
    Import your Vercel projects by linking the GitHub repository that backs your Vercel project with Agent assistance.

    ### Getting started

    1. **Navigate to the import page** and select Vercel from available sources
    2. **Connect your GitHub account** to authorize access to your repositories
    3. **Select the repository** that backs your Vercel project from the available repositories

    For a full guide on how to import a Vercel project, see our [quickstart guide](/getting-started/quickstarts/import-from-vercel).

    ### What we'll import

    * **Project structure**: Complete codebase and file organization
    * **Dependencies**: Package.json and dependency management
    * **Build configuration**: Optimized for Replit's environment
    * **Environment setup**: Runtime and framework configuration

    ### What's not included

    * **Environment variables**: You'll be prompted to provide these during import
    * **Custom domains**: Set up separately in Replit Deployments
    * **Vercel-specific configurations**: Edge functions and middleware may need adjustment
    * **Analytics and monitoring**: Use Replit's built-in monitoring tools

    ### Import process

    1. Agent scans your code and asks for any required secrets/env vars
    2. You provide environment variables one by one—only what isn't already standard
    3. Your app boots on Replit with a clean workflow, live preview, and logs
    4. No manual rewiring of build commands or port configuration needed
  </Accordion>

  <Accordion title="Bolt imports" icon="bolt">
    Import your Bolt projects by exporting them to GitHub first, then importing into Replit Agent Apps.

    ### Getting started

    1. **Export your Bolt project to GitHub** from your Bolt workspace
    2. **Connect your GitHub account to Replit** to authorize repository access
    3. **Select your new Bolt project repo** for import from the available repositories

    For a full guide on how to import a Bolt project, see our [quickstart guide](/getting-started/quickstarts/import-from-bolt).

    ## What gets imported

    During the import process, Replit migrates your {platform_0} project with Agent assistance:

    * **Code**: All application code and logic from your {platform_0} project
    * **Design and styles**: UI components, styling, and visual design elements
    * **Assets**: Images, icons, and other static resources
    * **Backend functionality**: If your {platform_0} project includes backend functionality, it is imported into the Replit environment.
    * **Database schema**: Database structure and table definitions are imported into a Neon Postgres database, which is integrated directly into the Replit environment.

    ### What's not included

    * **Supabase database**: Database content and data are not migrated
    * **Secrets**: Environment variables and API keys must be added separately

    You can ask Agent to help build out functionality, add secrets, and recreate databases in your new app.

    ### Import process

    1. The system validates project structure and dependencies
    2. Agent assists with migration and feature completion
    3. Your project is optimized for the Replit environment

    <ImportDatabaseWarning tool="Bolt" />
  </Accordion>

  <Accordion title="Lovable imports" icon="heart">
    Import your Lovable projects by exporting them to GitHub first, then importing into Replit Agent Apps.

    ### Getting started

    1. **Export your Lovable project to GitHub** from your Lovable workspace
    2. **Connect your GitHub account to Replit** to authorize repository access
    3. **Select your new Lovable project repo** for import from the available repositories

    For a full guide on how to import a Lovable project, see our [quickstart guide](/getting-started/quickstarts/import-from-lovable).

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

    <ImportDatabaseWarning tool="Lovable" />
  </Accordion>

  <Accordion title="Agent App imports" icon="robot">
    Import previously exported Agent Apps from GitHub repositories with preserved configurations.

    ### Getting started

    1. **Provide the GitHub repository URL** containing your exported Agent App
    2. **Verify repository access** ensuring the repository is accessible to your account
    3. **Confirm Agent App structure** in the repository

    For a full guide on how to import a GitHub repository, see our [quickstart guide](/getting-started/quickstarts/import-from-github).

    ### What we'll import

    * **Complete codebase**: All application code, dependencies, and configurations
    * **Agent configurations**: Preserved Agent-specific settings and optimizations
    * **Enterprise customizations**: Internal hardening and custom configurations
    * **Project structure**: Full project hierarchy and organization

    ### Import process

    1. The system validates the repository contains Agent App configurations
    2. Internal customizations and enterprise hardening are preserved
    3. The imported app is ready for immediate use or further development
  </Accordion>

  <Accordion title="GitHub repository imports" icon="github">
    Import compatible GitHub repositories and convert them into Replit Agent Apps.

    ### Getting started

    1. **Provide the repository URL** of the GitHub project you want to import
    2. **Ensure repository access** with proper permissions or public visibility
    3. **Verify compatibility** with supported frameworks and technologies

    For a full guide on how to import a GitHub repository, see our [quickstart guide](/getting-started/quickstarts/import-from-github).

    ### What we'll import

    * **Source code**: Complete repository codebase and file structure
    * **Dependencies**: Package configurations and dependency definitions
    * **Documentation**: README files, documentation, and project notes
    * **Configuration files**: Build configs, environment setups, and project settings

    ### Import process

    1. The system analyzes the codebase for Agent compatibility
    2. If compatible, the repository is converted to an Agent App
    3. Agent assists with any necessary setup or configuration
    4. Project is optimized for the Replit environment
  </Accordion>

  <Accordion title="ZIP imports" icon="file-zip">
    Import ZIP files containing your project files and convert them into Replit Agent Apps.

    ### Getting started

    1. **Create a Zip file** of your project files
    2. **Upload the Zip file** to the Replit import interface
    3. **Prompt the agent** to get your app up and running

    For a full guide on how to import a ZIP file, see our [quickstart guide](/getting-started/quickstarts/import-from-zip).

    ### What we'll import

    * **Source code**: Complete repository codebase and file structure
    * **Dependencies**: Package configurations and dependency definitions
    * **Documentation**: README files, documentation, and project notes
    * **Configuration files**: Build configs, environment setups, and project settings
  </Accordion>
</AccordionGroup>

## Limitations and considerations

### Current limitations

* **Database data**: Database contents are not imported; the system includes only schemas and edge functions
* **Complex dependencies**: Some complex or proprietary dependencies may require manual configuration
* **Large projects**: Very large projects may take longer to process or require optimization

### Future enhancements

* **Database content migration**: Full database content import capabilities
* **Enhanced validation**: Improved compatibility checking for complex projects

## Error handling

If an import fails, you'll receive specific error messages indicating the issue:

* **Compatibility errors**: The project structure may have issues that need to be resolved
* **Access errors**: Unable to access the source project or repository
* **Processing errors**: Technical issues during conversion

<Info>
  If you encounter persistent import issues, check that your source project is
  publicly accessible or that you have proper permissions.
</Info>

## Best practices

### Preparing for import

* **Clean project structure**: Ensure your source project has a clear, organized structure
* **Remove sensitive data**: Remove API keys, credentials, and sensitive information before import
* **Document dependencies**: Include clear documentation of external dependencies
* **Test functionality**: Verify your source project works correctly before importing

### After import

* **Review generated code**: Check the imported code for accuracy and completeness
* **Test functionality**: Thoroughly test all features in the Replit environment
* **Check secrets**: Agent will help you add secrets, but be sure to double check them and add any missing ones using [Replit's Secret](/replit-workspace/workspace-features/secrets) management.
* **Recreate databases**: If your project uses databases, recreate them using the [Database tool](/cloud-services/storage-and-databases/sql-database) or by asking Agent to help you.

## Billing

<Note>
  Import processing may consume Agent credits depending on the complexity of the
  migration and Agent involvement.
</Note>

Imports that require Agent assistance for migration or setup will consume credits based on the amount of processing required. Simple imports may complete without more charges beyond your standard Replit usage.

## Troubleshooting

### Common issues

**Import validation fails**

* Verify your source project uses supported frameworks and technologies
* Check that all required files are present and accessible
* Ensure your project follows standard conventions for your platform

**Import takes too long**

* Large or complex projects may require extended processing time
* Monitor the progress screen for status updates
* Contact support if processing exceeds expected time frames

**Generated code doesn't work as expected**

* Review the imported code for missing dependencies or configurations
* Use Agent to help debug and resolve any issues
* Check that all external services and APIs are properly configured

For more support, visit the [Replit Help Center](https://docs.replit.com) or contact the support team.
