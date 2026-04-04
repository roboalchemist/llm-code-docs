# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-context-vim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add context to your workspace

> You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

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

<Availability tags={["vim","neovim"]} />

## About Workspace Context

Augment is powered by its deep understanding of your code. You'll need to configure your project's source in your workspace context to get full codebase understanding in your chats and suggestions.

Sometimes important parts of your system exist outside of the current project. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional codebases to your workspace context will improve the code suggestions and chat responses from Augment.

## Add context to your workspace

<Note>
  Be sure to set `g:augment_workspace_folders` before the Augment plugin is loaded.
</Note>

To add context to your workspace, in your `.vimrc` set `g:augment_workspace_folders` to a list of paths to the folders you want to add to your workspace context. For example:

```vim  theme={null}
let g:augment_workspace_folders = ['/path/to/folder', '~/path/to/another/folder']
```

You may want to ignore specific folders, like `node_modules`, see [Ignoring files with .augmentignore](/setup-augment/workspace-indexing#ignoring-files-with-augmentignore) for more details.

After adding a workspace folder and restarting Vim, the output of the <Keyboard shortcut=":Augment status" /> command will include the syncing progress for the added folder.
