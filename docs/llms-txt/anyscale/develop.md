# Source: https://docs.anyscale.com/runtime/serve/develop.md

# Source: https://docs.anyscale.com/get-started/develop.md

# Tutorial: Develop on Anyscale

[View Markdown](/get-started/develop.md)

# Tutorial: Develop on Anyscale

This tutorial provides an introduction to developing Ray code using Visual Studio Code on Anyscale. The Anyscale console provides Visual Studio Code for all running workspaces.

If you don't have access to an Anyscale Workspace, see [Tutorial: Create a workspace](/get-started/create-workspace.md).

## Develop with VS Code[​](#vs-code "Direct link to Develop with VS Code")

You can use VS Code in Anyscale to develop code in a similar fashion to how you might write code on your personal machine. You can author assets including Ray code, Python modules, arbitrary programs, and configuration files.

Complete the following steps to develop and run a simple Ray program:

1. Navigate to a running Anyscale Workspace.

2. In the top menu, click the **VS Code** tab.

3. Create a new file and name it `hello_world.py`.

   ![Create a new file](/assets/images/development-new-file-ae21ea5011bab44b64b03eacd4592863.png)

4. Add the following Ray code to the `hello_world.py` file:

   ```

   import ray

   @ray.remote
   def hello_world():
      return "Hello World!"

   result = ray.get(hello_world.remote())
   print(result)
   ```

5. In the top-right corner, click **►** to submit the Python file to the cluster.

![Submit task to cluster](/assets/images/development-run-df2ac02f1637b8c37243bfc01488bd89.png)

When you run Ray code, the autoscaler adds worker nodes to your cluster if they're needed to run your code. The workload results display in your terminal once the workload completes.

![Hello world](/assets/images/development-result-9f05fbc94b14d39913978c560188a53f.png)

## Add dependencies to a workload[​](#dependencies "Direct link to Add dependencies to a workload")

To demonstrate dependency management, install the `emoji` package to your workspace and add a 👋 emoji to the `hello_world.py` Ray application. Complete the following steps:

1. Update the code in the `hello_world.py` file to the following:

   ```
   import emoji
   import ray

   @ray.remote
   def hello_world():
      return emoji.emojize("Hello World! :waving_hand:")

   result = ray.get(hello_world.remote())
   print(result)
   ```

   VS Code warns that it can't resolve the `emoji` package.

2. Navigate to the **Dependencies** tab in the workspace navigation bar.

3. Click **Edit containerfile** and add the following line to the editor:

   ```
   RUN pip install --no-cache-dir --upgrade emoji
   ```

![Select your IDE](/assets/images/development-dependency-f01484f3431e87786ce3a4b95f5a1dfb.png)

5. Click **Save and build image** and wait for the container image to build.

   The following notification displays in the **Dependencies** tab:

   > All new Ray workers launched will use the updated container image. Restart the workspace to use the new image for the head node.

6. Click **Restart workspace**.

7. Once the workspace restarts, return to VS Code and run your `hello_world.py` script.

![Hello World with a wave](/assets/images/development-emoji-cedfa06205c1e39cc7d35081c3bab632.png)

## Develop with other IDEs[​](#other-ides "Direct link to Develop with other IDEs")

Aside from the built-in VS Code environment, you can also use JupyterLab and a terminal from the web UI. You can also open the workspace locally in your own IDE through SSH. We support VS Code and Cursor directly from the UI, or you can configure your own IDE to connect to the workspace.

Click the **VS Code** tab in the top navigation bar to select your IDE of choice:

![Select your IDE](/assets/images/development-ide-f2fa7f06667f685b27a40b7d0e3a1591.png)
