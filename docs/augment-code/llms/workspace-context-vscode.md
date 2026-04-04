# Source: https://docs.augmentcode.com/setup-augment/workspace-context-vscode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add context to your workspace

> You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

export const Availability = ({tags = []}) => {
  const tagColor = {
    invite: "purple",
    beta: "gray",
    "private-preview": "purple",
    vscode: "blue",
    jetbrains: "orange",
    vim: "gray",
    neovim: "gray",
    cli: "green"
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => <Badge key={tag} size="sm" color={tagColor[tag] || "gray"}>
          {tag}
        </Badge>)}
    </div>;
};

export const Command = ({text}) => <span className="font-bold">{text}</span>;

<Availability tags={["vscode",]} />

## About Workspace Context

Augment is powered by its deep understanding of your code. Sometimes important parts of your system exist outside of the current workspace you have open in your IDE. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional context to your workspace will improve the code suggestions and chat responses from Augment.

## View Workspace Context

To view your Workspace Context, click the folder icon <Icon icon="folder-open" iconType="light" /> in the top right corner of the Augment sidebar panel.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=50de98aea1e300bb9386bf282cbe4581" alt="Workspace Context" className="rounded-xl" data-og-width="1156" width="1156" data-og-height="1009" height="1009" data-path="images/workspace-context.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3c66cf05f83956fad54a4d810fafb6b1 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=addf63bc42ae43d1747e74fd2d5c9fae 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=bc898ce5c72a8b07eb4ad378e312143b 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3566538a797b7b20fe288ea712ce3d48 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=01ef280a41d8cec96c771921b56dce17 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=16e11c1644cf33c6c255cac488c0eebe 2500w" />

## Add context to your workspace

To add context to your workspace, click <Command text="+ Add more..." /> at the bottom of the Source Folders section of the context manager. From the file browser select the folders you want to add to your workspace context and click <Command text="Add Source Folder" />.

## View sync status

When viewing Workspace Context, each file and folder will have an icon that indicates whether its sync status. The following icons indicate the sync status of each file in your workspace:

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Indicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Status                                  |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------- |
|                                         <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=83948590ef25800a8cf40c747c28b133" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-included.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9978e5ee6258d59409574de8a746c855 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b245408a2887e5bf6844291c823ca78f 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8076411a27ab25d56766bcce44ecda61 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a37b507ac4b71643cf77243b614a617e 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8f9084eacaa10f33d5661907bcbcbf53 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d1dd1a289906e0bc0552624154dfede1 2500w" />                                         | Synced, or sync in progress             |
|                                         <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e5a93c810f94d3d3db90b8984239699b" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-excluded.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=77728337572736aa0ac1c435428fcbb2 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f875fd61db9c659377ac1b9ee9619e58 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cd429e91f5b30345ca00d86b08b3b567 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=decd20244fdee2f81f1a7b6312081593 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1b09eebbc378320277e85fe780526f98 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a811d1132ea0a90e117a9b85823ef9f6 2500w" />                                         | Not synced                              |
| <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=892115c2ab50b9d2f8261f78abf89283" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-partially-included.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad70bb3c5d05b9098387e29e1e45080f 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=911e14ce3e65aa57b175edff60b29a5b 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6d5fa527bbaa111002ac3e8b864793c3 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d3c65bea8eb987dfced8d8d06ea6aa7a 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9f8e5409a71df31ee126394fbed5ddd7 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b311b9ab4b2c686f5ed292c9423c2744 2500w" /> | Some files within the folder are synced |
