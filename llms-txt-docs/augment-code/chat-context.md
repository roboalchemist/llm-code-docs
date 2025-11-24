# Source: https://docs.augmentcode.com/using-augment/chat-context.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-context.md

# Focusing Context in Chat

> You can specify context from files, folders, and external documentation in your conversation to focus your chat responses.

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat Context

Augment intelligently includes context from your entire workspace based on the ongoing conversation–even if you don't have the relevant files open in your editor–but sometimes you want Augment to prioritize specific details for more relevant responses.

<video src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-context.mp4?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cbdd137e0c8b3c0048cfab708bbb56eb" loop muted controls className="rounded-xl" data-path="images/chat-context.mp4" />

### Focusing context for your conversation

You can specify context by clicking the <AtIcon /> icon at the top-left of the Chat panel or by <Command text="@-mentioning" /> in the input field. You can use fuzzy search to filter the list of context options quickly. There are a number of different types of additional context you can add to your conversation:

1. Highlighted code blocks
2. Specific files or folders within your workspace
3. 3rd party documentation, like Next.js documentation

#### Mentioning files and folders

Include specific files or folders in your context by typing `@` followed by the file or folder name. For example, `@routes.tsx` will include the `routes.tsx` file in your context. You can include multiple files or folders.

#### Mentioning 3rd party documentation

You can also mention 3rd party documentation in your context by typing `@` followed by the name of the documentation. For example, `@Next.js` will include Next.js documentation in your context. Augment provides nearly 300 documentation sets spanning across a wide range of domains such as programming languages, packages, software tools, and frameworks.
