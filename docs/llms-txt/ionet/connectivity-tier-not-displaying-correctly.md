# Source: https://io.net/docs/guides/workers/connectivity-tier-not-displaying-correctly.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity Displays Incorrectly

> To troubleshoot connectivity tier issues, users can test network speeds via a sample Docker container. Here's how:

1. Pull the Python 3.9 Slim container:

   ```
   docker pull python:3.9-slim
   ```
2. Run the container:

   ```
   docker run -it --name speedtest-container python:3.9-slim /bin/bash
   ```
3. Install the speedtest tool:

   ```
   pip install speedtest-cli
   ```
4. Test the network speed:

   ```
   speedtest-cli
   ```

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cc6b9502f7455b3153e181bb556671e7" alt="" className="mx-auto" style={{ width:"81%" }} data-og-width="1314" width="1314" data-og-height="1382" height="1382" data-path="images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=50b28c7daf9f17027dce990aaccd5813 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=378ea1852365318e70d6090a68283635 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=5948d3e45bd3a45780ad96e5a2e7f92c 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=8299b043050b88b990f4abca200dc2b3 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=aaeb5033c71065aa9b347573b5196971 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c253d1c75dd3b1539b73ff5dff611670c7b322ba8a1c05ffb80c46f44221db55-DockerIssue6.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cd9b22b62c874b91fc97ef916fa6f437 2500w" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.
