# Source: https://docs.runpod.io/references/troubleshooting/token-authentication-enabled.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# JupyterLab server token authentication

If you see a "Token authentication is enabled" screen when trying to access your Pod's JupyterLab server, follow the steps below to log in.

<Frame caption="Jupyter server token authentication screen">
  <img src="https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=ff2743b0078023768a6a379aa15448ea" alt="Jupyter server token authentication" data-og-width="1414" width="1414" data-og-height="1504" height="1504" data-path="images/jupyter-server-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=280&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=b6f0cf7cc33a89713f32073b72ce167a 280w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=560&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=ae769e60e9c2cb0696b5b238a51aa927 560w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=840&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=4608e7c8ac9dfed118e546567c655e42 840w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=1100&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=614de38f155e164131db5f3df73e4385 1100w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=1650&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=b4541cb282a8dbf26e89c720d653639d 1650w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/jupyter-server-token.png?w=2500&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=d1fce4bd6dfc662cc3a357885ed49329 2500w" />
</Frame>

1. Go to the Pod page in the Runpod console and click the **Connect** button for the Pod you want to access.
2. Look for the **Web Terminal** start button.
3. Click **Start**, then open the web terminal.
4. In the terminal, run the following command to get the JupyterLab server token:

   ```
   jupyter server list
   ```

You should see output similar to this:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
root@2779b5db68b8:/# jupyter server list
Currently running servers:
http://localhost:8888/?token=ua5nw5fwkdzseqpp5apj :: /
root@2779b5db68b8:/#
```

The token you need is the string of characters that appears after the `=` sign, such as `ua5nw5fwkdzseqpp5apj` in the example above.

Copy this token, return to your JupyterLab login page, and paste it into the **Token** field to sign in.
