# Source: https://flatfile.com/docs/core-concepts/apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Apps

> The anatomy of an App

## Apps

Apps are an organizational unit in Flatfile, designed to manage and coordinate data import workflows across different environments. They serve as containers for organizing related Spaces and provide a consistent configuration that can be deployed across your development pipeline.

Apps can be given [namespaces](/guides/namespaces-and-filters#app-namespaces) to isolate different parts of your application and control which [listeners](/core-concepts/listeners) receive events from which spaces.

<Frame caption="App settings modal">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c1d2cb160c8805bf59bdd3d227e76691" width="400" data-og-width="1134" data-og-height="1184" data-path="core-concepts/assets/app-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f9da65cc68a4a0c3a3b9b8fc5e5a7527 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=0d49bd55b7128cdcbd960b6859a0ca24 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=b2c8d3655c15b03b6fa3c49bc0b9da23 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=87b0a59a9a75131d6fe1c2f426adebd2 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=427ce1de51e04f3f71388b13ca6d64e1 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/app-settings.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e659471afc4a7382d067776173080d44 2500w" />
</Frame>

Apps are available across Development-level environments by default, and optionally available across Production environments with a configuration option:

<Frame caption="Production Environment checkbox">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=1995b5b97c406f8c8d4a55753bb67341" width="275" data-og-width="574" data-og-height="70" data-path="getting-started/quickstart/assets/apps_show_in_production_environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=3b034c736ace8b26f1e445ff69539123 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=6cd73732666badc2ff9b775a05df2a79 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=23de9e2d1359b985945e1d8b01c2c152 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e7974ad32288abb1fc06155f0e5a15c8 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e3d3bd4eaf161828dee69a38155f5240 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/apps_show_in_production_environments.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=51fa6b4baa682c1f59b6b81f0be2e384 2500w" />
</Frame>
