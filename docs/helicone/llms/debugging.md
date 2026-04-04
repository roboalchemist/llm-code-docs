# Source: https://docs.helicone.ai/guides/cookbooks/debugging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Debugging LLM Applications

> Helicone provides an efficient platform for identifying and rectifying errors in your LLM applications, offering insights into their occurrence.

# Identifying Errors

Helicone's request page allows you to filter results by status code, a unique identifier that corresponds to various states of web requests. This feature enables you to pinpoint errors, providing essential information about their timing and location.

<Frame>
    <img
      src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=37fdd1cb114471330b82b291b614dcb9"
      alt="Filter web request results by status code on Helicone's request
  page."
      data-og-width="2198"
      width="2198"
      data-og-height="1534"
      height="1534"
      data-path="images/use-cases/status-filter.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=746f5d6c96de8d34bcc7c9119a77cd81 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=d2efd5ce2ecd4d710953b396f2483118 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=68c6a5f6536e362c719285aab0e13d31 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=17b9f37c48ddebe9408508f41b9afd29 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=37ee9368de5946d4e602e63cc4769af9 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/status-filter.png?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=afa1ace49185765a8c9543ff360762e3 2500w"
    />
</Frame>

We are currently developing dedicated error filters to further enhance your debugging experience. If you are interested in this feature, please support us by upvoting the feature request [here](https://www.helicone.ai/roadmap).

# Debugging Prompts with Playground

<Info>Currently, only ChatGPT is supported</Info>

Helicone's 'Playground' feature offers a platform for debugging your 'prompt'. This tool enables you to test your prompt and swiftly observe the model's output for minor adjustments within the Helicone environment. Here's a step-by-step guide on how to use it:

1. Open a request.

<Frame>
    <img
      src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=ecdeff8d84beb2aa027d1b14d595f487"
      alt="View detailed logging details on Helicone's Requests
  page."
      data-og-width="2730"
      width="2730"
      data-og-height="1842"
      height="1842"
      data-path="images/use-cases/view-request.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=b6ed846e0447d3541767553bbcd8d916 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=80b7931825fe1dd84d77dcd4dfb29f8b 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=881efcc122201d5bd8512278d218d9fb 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=509a4dcf8cdd20d4421740d960fe114f 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=44548b5fff758aa5ced779d18bf35454 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/view-request.png?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=7d7811e68e03881c50c1dee3b73efb77 2500w"
    />
</Frame>

2. Click on the 'Playground' button.

<Frame>
    <img
      src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=8b0f258110af171b838498c94fffd648"
      alt="Access the Playground feature for prompt debugging in
  Helicone"
      data-og-width="798"
      width="798"
      data-og-height="520"
      height="520"
      data-path="images/use-cases/playground-button.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=37a550be5210b6fe4cae84b5a117ea0d 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=7575f7cef1f914422166d3a12be2daef 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=72bac582cdee9cd92e98ba8e733313be 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=03e33c2374b4f15ce6754946ab365e21 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=468d6a25420dbc7b3094b3ed1df4a63b 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground-button.png?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=088e9ff8c08b38fcc198ad4f8994fbfa 2500w"
    />
</Frame>

3. Input and execute your prompt to view the results.

<Frame>
    <img
      src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=63d5f6d87ee25cbe7382e95381a3bf05"
      alt="Use Helicone's Playground to test prompts in a sandbox
  environment"
      data-og-width="2718"
      width="2718"
      data-og-height="1840"
      height="1840"
      data-path="images/use-cases/playground.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=5cf2603f7c10f14d1b4e14fe0fe551a2 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=cfd44fb34eda15e0de8bd4f0898ee563 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=8cffa37338963724d3608d5445147e96 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=88cd517c4132908c52890317ec9aa85a 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=ac9282146a6a090c65ef202dcdff7d83 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/playground.png?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=fcb0ce4a6c4e5d34775452a280d68ae5 2500w"
    />
</Frame>

Please note, the Playground tool is a sandbox environment, so feel free to experiment with different prompts and settings to optimize results for your project.
