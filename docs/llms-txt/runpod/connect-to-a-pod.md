# Source: https://docs.runpod.io/pods/connect-to-a-pod.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Connection options

> Explore our Pod connection options, including the web terminal, SSH, JupyterLab, and VSCode/Cursor.

<Frame alt="Pod connection options">
  <img src="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=f9218705ee6220c239f2f7e6179e0539" data-og-width="2173" width="2173" data-og-height="1014" height="1014" data-path="images/pod-connection-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=280&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=0713163c249e3638f0fb052ca015d05f 280w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=560&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=7c2968885b50b386a4555323061b36eb 560w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=840&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=d2588eeef35ad37e2a13f839b4a41146 840w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=1100&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=a75e7d0e340f21f5136f227a71d3cd4f 1100w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=1650&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=7d572828dbc43975a725db3d1706774f 1650w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/pod-connection-options.png?w=2500&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=58b8806725a31f471deb09cfcc4fe3b2 2500w" />
</Frame>

## Web terminal connection

The web terminal offers a convenient, browser-based method to quickly connect to your Pod and run commands. However, it's not recommended for long-running processes, such as training an LLM, as the connection might not be as stable or persistent as a direct [SSH connection](#ssh-terminal-connection).

The availability of the web terminal depends on the [Pod's template](/pods/templates/overview).

To connect using the web terminal:

1. Navigate to the [Pods page](https://console.runpod.io/pods) in the Runpod console.
2. Expand the desired Pod and select **Connect**.
3. If your web terminal is **Stopped**, click **Start**.
   <Tip>
     If clicking **Start** does nothing, try refreshing the page.
   </Tip>
4. Click **Open Web Terminal** to open a new tab in your browser with a web terminal session.

## JupyterLab connection

JupyterLab provides an interactive, web-based environment for running code, managing files, and performing data analysis. Many Runpod templates, especially those geared towards machine learning and data science, come with JupyterLab pre-configured and accessible via HTTP.

To connect to JupyterLab (if it's available on your Pod):

1. Deploy your Pod, ensuring that the template is configured to run JupyterLab. Official Runpod templates like "Runpod Pytorch" are usually compatible.
2. Once the Pod is running, navigate to the [Pods page](https://console.runpod.io/pods) in the Runpod console.
3. Find the Pod you created and click the **Connect** button. If it's grayed out, your Pod hasn't finished starting up yet.
4. In the window that opens, under **HTTP Services**, look for a link to **Jupyter Lab** (or a similarly named service on the configured HTTP port, often 8888). Click this link to open the JupyterLab workspace in your browser.
   <Tip>
     If the JupyterLab tab displays a blank page for more than a minute or two, try restarting the Pod and opening it again.
   </Tip>
5. Once in JupyterLab, you can create new notebooks (e.g., under **Notebook**, select **Python 3 (ipykernel)**), upload files, and run code interactively.

## SSH terminal connection

Connecting to a Pod via an SSH (Secure Shell) terminal provides a secure and reliable method for interacting with your instance. To establish an SSH connection, you'll need an SSH client installed on your local machine. The exact command will vary slightly depending on whether you're using the basic proxy connection or a direct connection to a public IP.

To learn more, see [Connect to a Pod with SSH](/pods/configuration/use-ssh).

## Connect to VSCode or Cursor

For a more integrated development experience, you can connect directly to your Pod instance through Visual Studio Code (VSCode) or Cursor. This allows you to work within your Pod's volume directory as if the files were stored on your local machine, leveraging VSCode's or Cursor's powerful editing and debugging features.

For a step-by-step guide, see [Connect to a Pod with VSCode or Cursor](/pods/configuration/connect-to-ide).
