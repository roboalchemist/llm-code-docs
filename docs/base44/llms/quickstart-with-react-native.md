# Source: https://docs.base44.com/developers/backend/quickstart/frameworks/quickstart-with-react-native.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# React Native (Expo) Quickstart

> Add a Base44 backend to your React Native Expo project

Follow this quickstart to add Base44 to your React Native (Expo) project. You'll create a Base44 backend, define entities, and integrate the SDK into your mobile app.

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
    Navigate to your React Native project directory, then run:

    ```bash  theme={null}
    base44 create
    ```

    If you're not already logged in, the command will prompt you to authenticate.

    Select **Create a basic project** when prompted. This creates the backend files within your React Native project directory. Then follow the prompts to configure your project.

    When you create a project, [Base44 skills](/developers/backend/overview/base44-skills) are included automatically, providing your AI agent with instructions and context for Base44 tasks.
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

    For example, create `api/base44Client.js`:

    ```javascript  theme={null}
    import { createClient } from '@base44/sdk';

    export const base44 = createClient({
      appId: 'your-app-id-from-app.jsonc'
    });
    ```
  </Step>

  <Step title="Create a task list screen">
    Create a simple screen component to list and add tasks. For example, create `screens/TaskListScreen.js`:

    ```javascript  theme={null}
    import { useState, useEffect } from 'react';
    import { View, Text, FlatList, Button, TextInput, StyleSheet, ActivityIndicator } from 'react-native';
    import { base44 } from '../api/base44Client';

    export default function TaskListScreen() {
      const [tasks, setTasks] = useState([]);
      const [newTitle, setNewTitle] = useState('');
      const [isLoading, setIsLoading] = useState(false);

      useEffect(() => {
        loadTasks();
      }, []);

      const loadTasks = async () => {
        setIsLoading(true);
        try {
          // Get records
          const taskList = await base44.entities.Task.list();
          setTasks(taskList);
        } catch (error) {
          console.error('Error loading tasks:', error);
        }
        setIsLoading(false);
      };

      const addTask = async () => {
        if (!newTitle.trim()) return;

        setIsLoading(true);
        try {
          // Create a record
          const newTask = await base44.entities.Task.create({
            title: newTitle,
            completed: false
          });
          setTasks([...tasks, newTask]);
          setNewTitle('');
        } catch (error) {
          console.error('Error creating task:', error);
        }
        setIsLoading(false);
      };

      return (
        <View style={styles.container}>
          <Text style={styles.title}>Tasks</Text>

      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <Text style={styles.task}>{item.title}</Text>}
        ListEmptyComponent={
          isLoading ? <ActivityIndicator /> : <Text style={styles.empty}>No tasks yet</Text>
        }
      />

          <View style={styles.inputRow}>
            <TextInput
              style={styles.input}
              value={newTitle}
              onChangeText={setNewTitle}
              placeholder="New task"
              editable={!isLoading}
            />
            <Button title="Add" onPress={addTask} disabled={isLoading || !newTitle.trim()} />
          </View>
        </View>
      );
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        padding: 20,
      },
      title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
      },
      task: {
        fontSize: 16,
        padding: 12,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
      },
      empty: {
        textAlign: 'center',
        color: '#999',
        marginTop: 20,
      },
      inputRow: {
        flexDirection: 'row',
        gap: 10,
        marginTop: 20,
      },
      input: {
        flex: 1,
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        borderRadius: 5,
      },
    });
    ```

    <Note>
      Use the exact entity name from your schema when calling the SDK, including capitalization. By convention, entity names begin with a capital letter. For example, if your schema has `"name": "Task"`, you access it as `base44.entities.Task.list()`.
    </Note>
  </Step>

  <Step title="Use the screen in your app">
    Update your `App.js` to import and render the `TaskListScreen` component:

    ```javascript  theme={null}
    import { StatusBar } from 'expo-status-bar';
    import { StyleSheet, SafeAreaView } from 'react-native';
    import TaskListScreen from './screens/TaskListScreen';

    export default function App() {
      return (
        <SafeAreaView style={styles.container}>
          <TaskListScreen />
          <StatusBar style="auto" />
        </SafeAreaView>
      );
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#fff',
      },
    });
    ```
  </Step>

  <Step title="Run your app locally">
    Start your Expo development server to test your integration. From your project root, run:

    ```bash  theme={null}
    npx expo start
    ```

    Follow the [Expo CLI instructions](https://docs.expo.dev/more/expo-cli/#develop) to open your app on a simulator, physical device, or web browser.

    Your React Native app will connect to your Base44 backend through the SDK client, allowing you to work with your deployed entities in real-time.
  </Step>
</Steps>

## Next steps

Now that your Base44 backend is integrated with your project, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your mobile app.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/functions), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Test locally by running [`base44 dev`](/developers/references/cli/commands/dev) for the backend alongside your app's dev server. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for setup instructions.

## See also

* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [JavaScript SDK Documentation](/developers/references/sdk/getting-started/overview): Connect your app to the backend
* [Base44 Skills](/developers/backend/overview/base44-skills): Teach AI assistants to work with Base44


Built with [Mintlify](https://mintlify.com).