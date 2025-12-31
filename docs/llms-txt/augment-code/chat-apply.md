# Source: https://docs.augmentcode.com/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/using-augment/chat-apply.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply.md

# Applying code blocks from Chat

> Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

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

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const CheckIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M389-267 195-460l51-52 143 143 325-324 51 51-376 375Z" />
    </svg>
  </div>;

export const FileNewIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h360v80H200v560h560v-360h80v360q0 33-23.5 56.5T760-120H200Zm120-160v-80h320v80H320Zm0-120v-80h320v80H320Zm0-120v-80h320v80H320Zm360-80v-80h-80v-80h80v-80h80v80h80v80h-80v80h-80Z" />
    </svg>
  </div>;

export const FileCopyIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M760-200H320q-33 0-56.5-23.5T240-280v-560q0-33 23.5-56.5T320-920h280l240 240v400q0 33-23.5 
      56.5T760-200ZM560-640v-200H320v560h440v-360H560ZM160-40q-33 0-56.5-23.5T80-120v-560h80v560h440v80H
      160Zm160-800v200-200 560-560Z" />
    </svg>
  </div>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b461dba46612cb6cc46db000bebb7566" alt="Augment Chat Apply" className="rounded-xl" data-og-width="1291" width="1291" data-og-height="375" height="375" data-path="images/chat-apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd3f5cea028042ba31b68a12f009acbc 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a1aca8f5dbff77303d4568677444eafa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b4d3137bba658cecc13434bf193ea9a7 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=011d9dfafca386660985500a6d4c7ab6 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d9cc3f973615bbc1727876d11e0f4c7e 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2e3a50fd918339cb519553c06bc5a242 2500w" />

## Using code blocks from within Chat

Whenever Chat responds with code, you will have the option to add the code to your codebase. The most common option will be shown as a button and you can access the other options by clicking the overflow menu icon<MoreVertIcon />at the top-right of the code block. You can use the following options to apply the code:

* <FileCopyIcon />**Copy**
  the code from the block to your clipboard
* <FileNewIcon />**Create**
  a new file with the code from the block
* <CheckIcon />**Apply**
  the code from the block intelligently to your file
