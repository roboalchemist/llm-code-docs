# Source: https://docs.base44.com/developers/backend/quickstart/frameworks/quickstart-vue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vue Quickstart

> Add a Base44 backend to your Vue project

Follow this quickstart to add Base44 to your Vue project. You'll create a Base44 backend, define entities, and integrate the SDK into your frontend.

<Note>The CLI requires Node.js 20.19.0 or higher.</Note>

## Setup

<Steps>
  <Step title="Install the Base44 CLI">
    Install the Base44 CLI globally:

    ```bash  theme={null}
    npm install -g base44@latest
    ```
  </Step>

  <Step title="Create a Base44 backend">
    Navigate to your Vue project directory, then run:

    ```bash  theme={null}
    base44 create
    ```

    If you're not already logged in, the command will prompt you to authenticate.

    Select **Create a basic project** when prompted. This creates the backend files within your Vue project directory. Then follow the prompts to configure your project.

    When you create a project, [Base44 skills](/developers/backend/overview/base44-skills) are included automatically, providing your AI agent with instructions and context for Base44 tasks.
  </Step>

  <Step title="Configure the output directory">
    Update your [config.jsonc](/developers/backend/overview/project-structure#config-jsonc) to point to your Vue build output. Add or modify the `site.outputDirectory` field:

    ```json  theme={null}
    {
      "site": {
        "outputDirectory": "dist"
      }
    }
    ```
  </Step>

  <Step title="Define entities">
    Create [entity schemas](/developers/references/entities/introduction) to define your data structures. Entity files must be placed in the `base44/entities/` directory.

    For example, create `base44/entities/task.jsonc`:

    ```json  theme={null}
    {
      "name": "Task",
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "completed": {
          "type": "boolean",
          "default": false
        }
      },
      "required": ["title"]
    }
    ```
  </Step>

  <Step title="Push entities to Base44">
    Push your entity schemas to Base44:

    ```bash  theme={null}
    base44 entities push
    ```

    This command synchronizes your local entity definitions with your Base44 backend, making them available for use in your application. See [`entities push`](/developers/references/cli/commands/entities-push) for more information.
  </Step>

  <Step title="Install the Base44 SDK">
    Install the Base44 JavaScript SDK:

    ```bash  theme={null}
    npm install @base44/sdk
    ```
  </Step>

  <Step title="Create a Base44 client">
    Create a Base44 SDK [client](/developers/references/sdk/getting-started/client) in your project. The `appId` can be found in your `base44/.app.jsonc` file.

    For example, create `src/api/base44Client.js`:

    ```javascript  theme={null}
    import { createClient } from '@base44/sdk';

    export const base44 = createClient({
      appId: 'your-app-id-from-app.jsonc'
    });
    ```
  </Step>

  <Step title="Use the SDK in your frontend">
    Create a simple component to list and add tasks. For example, create `src/components/TaskList.vue`:

    ```vue  theme={null}
    <script setup>
    import { ref, onMounted } from 'vue';
    import { base44 } from '@/api/base44Client';

    const tasks = ref([]);
    const newTaskTitle = ref('');
    const isLoading = ref(false);

    onMounted(async () => {
      await loadTasks();
    });

    const loadTasks = async () => {
      isLoading.value = true;
      try {
        // Get records
        tasks.value = await base44.entities.Task.list();
      } catch (error) {
        console.error('Error loading tasks:', error);
      }
      isLoading.value = false;
    };

    const addTask = async (e) => {
      e.preventDefault();
      if (!newTaskTitle.value.trim()) return;

      isLoading.value = true;
      try {
        // Create a record
        const newTask = await base44.entities.Task.create({
          title: newTaskTitle.value,
          completed: false
        });
        tasks.value.push(newTask);
        newTaskTitle.value = '';
      } catch (error) {
        console.error('Error creating task:', error);
      }
      isLoading.value = false;
    };
    </script>

    <template>
      <div>
        <h1>Tasks</h1>

        <p v-if="isLoading">Loading...</p>

        <ul>
          <li v-for="task in tasks" :key="task.id">
            {{ task.title }}
          </li>
        </ul>

        <form @submit="addTask">
          <input
            type="text"
            v-model="newTaskTitle"
            placeholder="New task"
            :disabled="isLoading"
          />
          <button type="submit" :disabled="isLoading || !newTaskTitle.trim()">
            Add Task
          </button>
        </form>
      </div>
    </template>
    ```

    <Note>
      Use the exact entity name from your schema when calling the SDK, including capitalization. By convention, entity names begin with a capital letter. For example, if your schema has `"name": "Task"`, you access it as `base44.entities.Task.list()`.
    </Note>
  </Step>

  <Step title="Run your app locally">
    Start your Vue development server to test your integration. From your project root, run:

    ```bash  theme={null}
    npm run dev
    ```

    Your Vue app will connect to your Base44 backend through the SDK client, allowing you to work with your deployed entities in real-time.
  </Step>

  <Step title="Build your frontend">
    When you're happy with how everything looks locally, build your Vue project for production:

    ```bash  theme={null}
    npm run build
    ```

    This creates optimized production files in your output directory (typically `dist`).
  </Step>

  <Step title="Deploy your frontend">
    Deploy your built frontend to Base44:

    ```bash  theme={null}
    base44 deploy
    ```

    The `deploy` command deploys your built frontend to Base44 hosting. It will also push any updates to your entity schemas if you've made changes since the last push. When complete, you'll see your project name, a link to your Base44 dashboard, and your live application URL.
  </Step>
</Steps>

## Next steps

Now that your Base44 backend is integrated with your project, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your frontend.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/functions), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Test locally by running [`base44 dev`](/developers/references/cli/commands/dev) for the backend and `npm run dev` for the frontend. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for setup instructions.
* Continue building your frontend and deploy updates with [`base44 deploy`](/developers/references/cli/commands/deploy).
* Open your deployed site with [`base44 site open`](/developers/references/cli/commands/site-open).

## See also

* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [JavaScript SDK Documentation](/developers/references/sdk/getting-started/overview): Connect your app to the backend
* [Base44 Skills](/developers/backend/overview/base44-skills): Teach AI assistants to work with Base44


Built with [Mintlify](https://mintlify.com).