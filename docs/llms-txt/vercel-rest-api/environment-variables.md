# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/environment-variables.md

# Environment Variables

> Learn how to use the Vercel SDK through real-life examples.

## Add environment variables to a project

In this example, you will add new environment variables to a project and list the details of the added values.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const projectName = 'my-project'; //The project name used in the deployment URL

async function addAndListEnvVars() {
  try {
    // Add new environment variables
    const addResponse = await vercel.projects.createProjectEnv({
      idOrName: projectName,
      upsert: 'true',
      requestBody: [
        {
          key: 'API_KEY',
          value: 'secret_value',
          target: ['production', 'preview'],
          type: 'encrypted',
        },
        {
          key: 'DEBUG',
          value: 'true',
          target: ['development'],
          type: 'plain',
        },
      ],
    });
    console.log(
      'Added environment variables:',
      JSON.stringify(addResponse, null, 2),
    );
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

addAndListEnvVars();
```

## Manage variables across projects

In this example, you manage environment variables across multiple projects and environments.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import { OneTarget } from '@vercel/sdk/models/operations/createprojectenv';

const PROJECTS = ['project-id-1', 'project-id-2', 'project-id-3'];
const environments = ['development', 'preview', 'production'];
const VERCEL_TOKEN = process.env.VERCEL_TOKEN;

const vercel = new Vercel({
  bearerToken: VERCEL_TOKEN,
});

async function manageEnvironmentVariables() {
  try {
    const variables = [
      { key: 'API_URL', value: 'https://api.example.com' },
      { key: 'DEBUG', value: 'true', environments: ['development', 'preview'] },
      {
        key: 'SECRET_KEY',
        value: 'super-secret-key',
        encrypt: true,
        environments: ['production', 'preview'],
      },
    ];

    for (const projectId of PROJECTS) {
      console.log(`Managing environment variables for project: ${projectId}`);
      for (const variable of variables) {
        const targets =
          (variable.environments as OneTarget[]) ||
          (environments as OneTarget[]);

        const addEnv = await vercel.projects.createProjectEnv({
          idOrName: projectId,
          upsert: 'true',
          requestBody: {
            key: variable.key,
            value: variable.value,
            target: targets,
            type: variable.encrypt ? 'encrypted' : 'plain',
          },
        });
        console.log(addEnv.created);
      }
      const readEnvs = await vercel.projects.filterProjectEnvs({
        idOrName: projectId,
      });
      console.log(
        'Env Details for ',
        projectId,
        ':',
        JSON.stringify(readEnvs, null, 2),
      );
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

manageEnvironmentVariables();
```
