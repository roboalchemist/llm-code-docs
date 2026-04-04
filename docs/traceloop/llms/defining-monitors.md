# Source: https://www.traceloop.com/docs/monitoring/defining-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining Monitors

> Learn how to create and configure monitors to evaluate your LLM outputs

Monitors in Traceloop allow you to continuously evaluate your LLM outputs in real time. This guide walks you through the process of creating and configuring monitors for your specific use cases.

## Creating a Monitor

To create a monitor, you need to complete these steps:

<Steps>
  <Step title="Send Traces">
    Connect the SDK to your system and add decorators to your flow. See [OpenLLMetry](/openllmetry/introduction) for setup instructions.
  </Step>

  <Step title="Choose an Evaluator">
    Select the evaluation logic that will run on matching spans. You can define your own custom evaluators or use the pre-built ones by Traceloop. See [Evaluators](/evaluators/intro) for more details.
  </Step>

  <Step title="Define Span Filter">
    Set criteria that determine which spans the monitor will evaluate.
  </Step>

  <Step title="Configure Settings">
    Set up how the monitor operates, including sampling rates and other advanced options.
  </Step>
</Steps>

### Basic Monitor Setup

Navigate to the Monitors page and click the **New** button to open the Evaluator Library. Choose the evaluator you want to run in your monitor.
Next, you will be able to configure which spans will be monitored.

## Span Filtering

The span filtering modal shows the actual spans from your system, letting you see how your chosen filters apply to real data.
Add filters by clicking on the  <kbd>+</kbd>  button.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=e882a9b6eb5ca662b5770f2c26fbebc5" data-og-width="2392" width="2392" data-og-height="1406" height="1406" data-path="img/monitor/monitor-filter-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=2848dcefb764e044c7a1c745ca71e83b 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=49dfc8127ce02a358cf70525fb43b059 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=4eda52e0f2aee84a8a8a4ab6b81c7ca6 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=98f51f9869ec06710e28da149a82d383 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=66f0299d567a2fb3bef6115bc153fb67 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-light.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=96843d8f1570a38ba3407d9f09125dc8 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=5d7f6d15f3cc60cc9d4ded8660b4b3e5" data-og-width="2402" width="2402" data-og-height="1408" height="1408" data-path="img/monitor/monitor-filter-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=b9c4ad0ee461305a7d61ae4703b35db9 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=292c5a8fd5102e712316ad03a9879650 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=7ba8780a2238974cfa6f26d06990d241 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=2b4cb399e02dfce20731945f8f9b4f0c 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=50b318edc53500231e625818248001f2 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-dark.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=7f97340ef0526d895874e5c6f21659f0 2500w" />
</Frame>

### Filter Options

* **Environment**: Filter by a specific environment
* **Workflow Name**: Filter by the workflow name defined in your system
* **Service Name**: Target spans from specific services or applications
* **AI Data**: Filter based on LLM-specific attributes like model name, token usage, streaming status, and other AI-related metadata
* **Attributes**: Filter based on span attributes

<img className="block dark:hidden" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=7b9f0c7fa861ee4237a5b930079de105" style={{maxWidth: '500px'}} data-og-width="970" width="970" data-og-height="916" height="916" data-path="img/monitor/monitor-filter-options-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=d7a89fd389a99c2038450b6d0edae6a1 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=3aed584189a6a688be20109e57767015 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=516b0b1f09ab7d53f5371332dab91ec5 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=ddbaa61d04b37d2ba8db639dbb93870b 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=ebef7bb934b61ce38c5764ab8e869d36 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-light.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=bacb7bd4bb4e17a4039ba355dea9acc2 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=f43bbc0f8be5a83e76011f1c2acdbe4d" style={{maxWidth: '500px'}} data-og-width="964" width="964" data-og-height="922" height="922" data-path="img/monitor/monitor-filter-options-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=9de9008a443e674408a93d0d8840fbc9 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=486a7951e08615d2815a8ffe8e17eb92 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=e164d493a8b5ff3400046ed06800a8c4 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=517aaf80ee25e693797a48f93e8cd87a 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=6c0ca452991595c225fa48c009731d43 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-filter-options-dark.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=569669fba78e9c462a1bd54fc8e866ab 2500w" />

## Monitor Settings

### Map Input

You need to map the appropriate span fields to the evaluator’s input schema.
This can be done easily by browsing through the available span field options—once you select a field, the real data is immediately displayed so you can see how it maps to the input.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=32a441ef62772a8f23528fa2a8762153" data-og-width="2388" width="2388" data-og-height="1390" height="1390" data-path="img/monitor/monitor-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=51bd00bf41e8c66bf026bbc019094e0c 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=f089455d4bc03db6a3957cdd88fe4f0a 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ac0d13ccedc0edb338ae9eb5bf84b5e4 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=b23bee03e01518be81e99cfc076bc517 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=bbe258a562140214eb7be4ad1faa923f 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=656e8b40b4c87f62d3eec011fe9e5fe0 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ced02fcf7efcb0d7e00fdf5d0ffb2f7e" data-og-width="2402" width="2402" data-og-height="1406" height="1406" data-path="img/monitor/monitor-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=d5ba7f4015832b1504a5af4c4d4ad2fd 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=841121a746dee5d79cd8678624f3fdc0 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=9496c1d1b2322d6c49f42fb345799501 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=bf429e6954bb8b38e54b4466095e85ba 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ae502a50bf2b9b6d2bd694552e016556 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-settings-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=d7dbd37b256bcddde7e3d22ad7f77342 2500w" />
</Frame>

When the field data is not plain text, you can use JSON key mapping or Regex to extract the specific content you need.

For example, if your content is an array and you want to extract the "text" field from the object:

```json  theme={null}
[{"type":"text","text":"explain who are you and what can you do in one sentence"}]
```

You can use JSON key mapping like `0.text` to extract just the text content. The JSON key mapping will be applied to the Preview table, allowing you to see the extracted result in real-time.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=41f7fd4b8d5e4a353d0c9e6e13857aee" data-og-width="2380" width="2380" data-og-height="1404" height="1404" data-path="img/monitor/monitor-json-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=02ac2a705485d1dd0469d12500a21d55 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=d865289b0586412d5cb3334152c407cf 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=5a7b2c67b1c4992736eb25c84a7a328b 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=ab610b1dee58e1851926a298632f276a 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=dace78e7f152568e41ad731da6edaba2 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-light.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=9eaa7b1c415cca0c70a231568601a1ee 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=d744d896c0d932044a6e298c0138db3c" data-og-width="2390" width="2390" data-og-height="1398" height="1398" data-path="img/monitor/monitor-json-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=856aaaf7843898b626e41ce3925cb38e 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=2fe6c380b59cdb29d781822dd5230f89 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=1f5c2ef66f88fec9e93dac472ba0d154 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=3d93fae5454210aa6a6d93b3f3d983c3 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=cc69ef9a5546bbb1beb4049b30e23d35 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-json-dark.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=06e9791655885d14d6db53643783117e 2500w" />
</Frame>

You can use Regex like `text":"(.+?)"` to extract just the text content. The regex will be applied to the Preview table, allowing you to see the extracted result in real-time.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=28cab1fcf3466cd3507b42757e8d4051" data-og-width="2386" width="2386" data-og-height="1390" height="1390" data-path="img/monitor/monitor-regex-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=269ab08522ee1404e8b3a4a1fb8aaff2 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=f5da3959a3eb63ae5fe198228f800055 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=41794847ddf3dada13d8d9e4ade5a151 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=e71845de50ff6283d1b9862f0e17dece 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=7259d42b9385cd10e70d0b711a96f53f 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=04d21b6d4f60ec812209e9e8ba9a3615 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=cf8eb05558708aaa81d9a8eac34b16ff" data-og-width="2392" width="2392" data-og-height="1396" height="1396" data-path="img/monitor/monitor-regex-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=7c7d95d7341374a90e9ff5e9a83f298e 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=50da1e5b2945caf2194275917829a4ef 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=6e934cd134b2ca8a93ef6b1e3723275c 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=de91a3e8577bb7e5968d8a1dacd06c00 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=52d468c6381c2f5c68ec9b9551e4bcfc 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-regex-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=8008182b47688ed7c8117c55900e8969 2500w" />
</Frame>

### Advanced

You can set a **Rate sample** to control the percentage of spans within the selected filter group that the monitor will run on.
