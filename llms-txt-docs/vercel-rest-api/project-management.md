# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/project-management.md

# Project Management

> Learn how to use the Vercel SDK through real-life examples.

## Create a new project

In this example, you will create a new project and retrieve its details. You will use the following method:

* Create project

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createAndGetProject() {
  try {
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'my-new-project',
        framework: 'nextjs',
      },
    });

    console.log(`Project created: ${createResponse.id}`);
    console.log('Project Details:', JSON.stringify(createResponse, null, 2));
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createAndGetProject();
```

## Create a new project with additional setup

In this example, you will create a new project, add environment variables, and set up automatic GitHub deployments.

* Create project
* Create env

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setupProjectWithGitHub() {
  try {
    // Create a new project with GH integration
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'advanced-project',
        framework: 'nextjs',
        gitRepository: {
          repo: 'your-username-or-orgname/your-repo-name', //The repository should have been created before and the GH account is connected to your Vercel account
          type: 'github',
        },
      },
    });

    console.log(`Project created: ${createResponse.id}`);

    const envResponse = await vercel.projects.createProjectEnv({
      idOrName: createResponse.id,
      upsert: 'true',
      requestBody: [
        {
          key: 'DATABASE_URL',
          value: 'postgresql://user:pass@host:5432/db',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production', 'preview'],
        },
        {
          key: 'API_KEY',
          value: 'your-api-key',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production'],
        },
        {
          key: 'API_URL',
          value: 'your-api-url',
          type: 'plain',
          target: ['production', 'preview'],
        },
      ],
    });

    console.log('Environment variables added:', envResponse.created);
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

setupProjectWithGitHub();
```
