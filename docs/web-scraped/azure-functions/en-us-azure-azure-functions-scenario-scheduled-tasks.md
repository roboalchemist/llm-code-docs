# Source: https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks

Title: Run scheduled tasks using Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks

Markdown Content:
In this article, you use the Azure Developer CLI (`azd`) to create a Timer trigger function to run a scheduled task in Azure Functions. After verifying the code locally, you deploy it to a new serverless function app you create running in a Flex Consumption plan in Azure Functions.

The project source uses `azd` to create the function app and related resources and to deploy your code to Azure. This deployment follows current best practices for secure and scalable Azure Functions deployments.

By default, the Flex Consumption plan follows a _pay-for-what-you-use_ billing model, which means you can complete this article and only incur a small cost of a few USD cents or less in your Azure account.

Important

While [running scheduled tasks](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer) is supported for all languages, this quickstart scenario currently only has examples for C#, Python, and TypeScript. To complete this quickstart, select one of these supported languages at the top of the article.

*   [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)

*   [Node.js 22](https://nodejs.org/) or above

*   [Python 3.11](https://www.python.org/) or above

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-dotnet-azd-timer -e scheduled-dotnet
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-timer) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the app folder:

```
cd src
```
3.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
        "TIMER_SCHEDULE": "*/30 * * * * *"
    }
}
```

This file is required when running locally.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-typescript-azd-timer -e scheduled-ts
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-timer) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "node",
        "TIMER_SCHEDULE": "*/30 * * * * *"
    }
}
```

This file is required when running locally.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-python-azd-timer -e scheduled-py
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-python-azd-timer) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "TIMER_SCHEDULE": "*/30 * * * * *"
    }
}
```

This file is required when running locally.

In the root folder, run these commands to create and activate a virtual environment named `.venv`:

*   [Linux/macOS](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks#tabpanel_1_linux)
*   [Windows (bash)](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks#tabpanel_1_windows-bash)
*   [Windows (Cmd)](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks#tabpanel_1_windows-cmd)

```
python3 -m venv .venv
source .venv/bin/activate
```

If Python doesn't install the venv package on your Linux distribution, run the following command:

```
sudo apt-get install python3-venv
```

1.   Run this command from your app folder in a terminal or command prompt:

```
func start
```

1.   Run this command from your app folder in a terminal or command prompt:

```
npm install
npm start
```

1.   When the Functions host starts in your local project folder, it writes information about your Timer triggered function to the terminal output. You should see your Timer triggered function execute based on the schedule defined in your code.

The default schedule is `*/30 * * * * *`, which runs every 30 seconds.

2.   When you're done, press Ctrl+C in the terminal window to stop the `func.exe` host process.

1.   Run `deactivate` to shut down the virtual environment.

You can review the code that defines the Timer trigger function:

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Extensions.Timer;
using Microsoft.Extensions.Logging;

namespace Company.Function
{
    public class timerFunction
    {
        private readonly ILogger _logger;

        public timerFunction(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<timerFunction>();
        }

        [Function("timerFunction")]
        public void Run(
            [TimerTrigger("%TIMER_SCHEDULE%", RunOnStartup = true)] TimerInfo myTimer,
            FunctionContext context
        )
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");

            if (myTimer.IsPastDue)
            {
                _logger.LogWarning("The timer is running late!");
            }
        }
    }
}
```

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-timer).

```
import { app, InvocationContext, Timer } from '@azure/functions';

export async function timerFunction(myTimer: Timer, context: InvocationContext): Promise<void> {
    context.log(`TypeScript Timer trigger function executed at: ${new Date().toISOString()}`);

    if (myTimer.isPastDue) {
        context.warn("The timer is running late!");
    }
}

app.timer('timerFunction', {
    schedule: '%TIMER_SCHEDULE%',
    runOnStartup: true,
    handler: timerFunction
});
```

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-timer).

```
import datetime
import logging

import azure.functions as func

# Create the function app instance
app = func.FunctionApp()

@app.timer_trigger(schedule="%TIMER_SCHEDULE%", 
                   arg_name="mytimer", 
                   run_on_startup=True,
                   use_monitor=False) 
def timer_function(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    logging.info(f'Python timer trigger function executed at: {utc_timestamp}')
    
    if mytimer.past_due:
        logging.warning('The timer is running late!')
```

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-python-azd-timer).

After you verify your function locally, it's time to publish it to Azure.

This project is configured to use the `azd up` command to deploy your code to a new function app in a Flex Consumption plan in Azure.

Tip

This project includes a set of Bicep files that `azd` uses to create a secure deployment to a Flex consumption plan that follows best practices.

1.   Run this command to have `azd` create the required Azure resources in Azure and deploy your code project to the new function app:

```
azd up
```

The root folder contains the `azure.yaml` definition file required by `azd`.

If you're not already signed in, you're asked to authenticate with your Azure account.

2.   When prompted, provide these required deployment parameters:

| Parameter | Description |
| --- | --- |
| _Azure subscription_ | Subscription in which your resources are created. |
| _Azure location_ | Azure region in which to create the resource group that contains the new Azure resources. Only regions that currently support the Flex Consumption plan are shown. | 
The `azd up` command uses your response to these prompts with the Bicep configuration files to complete these deployment tasks:

    *   Create and configure these required Azure resources (equivalent to `azd provision`):

        *   Flex Consumption plan and function app
        *   Azure Storage (required) and Application Insights (recommended)
        *   Access policies and roles for your account
        *   Service-to-service connections using managed identities (instead of stored connection strings)
        *   Virtual network to securely run both the function app and the other Azure resources

    *   Package and deploy your code to the deployment container (equivalent to `azd deploy`). The app is then started and runs in the deployed package.

After the command completes successfully, you see links to the resources you created.

After deployment completes, your Timer trigger function automatically starts running in Azure based on its schedule.

1.   In the [Azure portal](https://portal.azure.com/), go to your new function app.

2.   Select **Log stream** from the left menu to monitor your function executions in real-time.

3.   You should see log entries that show your Timer trigger function executing according to its schedule.

Run the `azd up` command as many times as you need to both provision your Azure resources and deploy code updates to your function app.

Note

Deployed code files are always overwritten by the latest deployment package.

Your initial responses to `azd` prompts and any environment variables generated by `azd` are stored locally in your named environment. Use the `azd env get-values` command to review all of the variables in your environment that were used when creating Azure resources.

When you're done working with your function app and related resources, use this command to delete the function app and its related resources from Azure and avoid incurring any further costs:

```
azd down --no-prompt
```

Note

The `--no-prompt` option instructs `azd` to delete your resource group without a confirmation from you.

This command doesn't affect your local code project.

*   [Timer trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer)
*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
*   [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)
*   [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
*   [azd reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference)
*   [Azure Functions Core Tools reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference)
*   [Code and test Azure Functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
