# Source: https://docs.mage.ai/orchestration/backfills/guides.md

# Source: https://docs.mage.ai/extensibility/global-hooks/guides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Global Hooks Guide

> Follow this step by step guide on creating a global hook in Mage.

export const urls = {
  chat: 'https://www.mage.ai/chat',
  oss: 'https://www.mage.ai/oss',
  pro: 'https://cloud.mage.ai/sign-up'
};

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="global-hooks" />

<img alt="Penguin Fishing" src="https://mage-ai.github.io/assets/penguin_fishing.gif" />

### <b>Step 1: Navigate to the Global Hooks UI</b>

1. Log in to your Mage account.

<Note>
  If you are new to Mage, follow these steps to enable Global Hooks:

  1. From the Dashboard UI, click Pipelines from the left navigation pane
  2. Once in the Pipelines UI, click click Settings from the left navigation pane
  3. Scroll down to view the features settings and toggle on Global Hooks
</Note>

2. Click on Global Hooks in the left navigation pane
3. Once on the Global Hooks view, click on the "+ Add new global hook" button.

### <b>Step 2: Configure the Hook</b>

1. **Hook UUID**: Enter a unique name for your hook.
2. **Resource Type**: Select the type of resource (API call type) from the resource drop down.
3. **Operation Type**: Select the type of operation needed for your hook.

<Note>
  Once the "Create new global Hook" button is clicked the rest of the configuration settings will populate.
</Note>

4. **Targeting Conditions**: Enter conditions if you want it to apply the hook to only certain pipelines. Leave this field blank to apply the hook to all pipelines.
5. **Before Operation Starts Toggle**: Toggle to on if you want the hook to run before an operation starts.
6. **After Operation Completes Toggle**: Toggle to on if you want the hook to run after an operation ends.
7. **Run if Operation Succeeds Toggle**: Toggle to on if you want to hook to run only if the operation succeeds.
8. **Run if Operation Fails Toggle**: Toggle to on if you want the hook to run if the operation fails.
9. **Pipeline to Execute**: Select the pipeline you want to execute the hook from.
10. **Valid Code Snapshot**: Click the "Create Snapshot of code" button to validate the pipeline code.

<Note>
  When making a code change to the pipeline, you have to re-validate the global hook by clicking the "Create snapshot" button
</Note>

11. **Stop Operation if Hook Fails Toggle**: Toggle on if you want to stop the operation from running if the hook fails.
12. **Execute Hook with History and Logging Toggle**: Toggle to on if you want to log the hook's execution, but be aware of potential performance impacts.

<Note>
  Toggling on the history and logging feature will significantly degrade performance of the of the operations resolution time.
</Note>

13. **Run Hook Asynchronously:** Enable this setting to run hooks asynchronously and not block the current resource operation from resolving
14. **Block Outputs**: To select block output features, Click the "+ Add block outputs" button
15. **Block to Extract Data From**: If needed, select the block data will be merge from into the hook operation’s data.
16. **Object to Merge Block into data**: If needed, select the type of data that will be merged into the hook operation’s data.
17. **Additional Dictionary Keys**: Enter information into this field if you have nested objects in your block.

### **Step 3: Save and Test the Hook**

1. Click the "Save changes" button to update the global hook with the new configuration changes.
2. To execute a global hook, perform the action or operation that matches the hook's configured conditions, and the hook will run the designated code or pipeline based on its defined settings.


Built with [Mintlify](https://mintlify.com).