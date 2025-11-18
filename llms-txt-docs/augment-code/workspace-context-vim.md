# Source: https://docs.augmentcode.com/vim/setup-augment/workspace-context-vim.md

# Add context to your workspace

> You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Availability = ({tags}) => {
  const tagTypes = {
    invite: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    beta: {
      styles: "border border-zinc-500/20 bg-zinc-50/50 dark:border-zinc-500/30 dark:bg-zinc-500/10 text-zinc-900 dark:text-zinc-200"
    },
    vscode: {
      styles: "border border-sky-500/20 bg-sky-50/50 dark:border-sky-500/30 dark:bg-sky-500/10 text-sky-900 dark:text-sky-200"
    },
    jetbrains: {
      styles: "border border-amber-500/20 bg-amber-50/50 dark:border-amber-500/30 dark:bg-amber-500/10 text-amber-900 dark:text-amber-200"
    },
    vim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    neovim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    default: {
      styles: "bg-gray-200"
    }
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => {
    const tagType = tagTypes[tag] || tagTypes.default;
    return <div key={tag} className={`px-2 py-0.5 rounded-md text-xs font-medium ${tagType.styles}`}>
            {tag}
          </div>;
  })}
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
