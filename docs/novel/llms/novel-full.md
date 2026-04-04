# Novel Documentation

Source: https://www.novel.sh/docs/llms-full.txt

---

# Editor Bubble

Wrapper over Tiptap Bubble menu

For all the available props, see [Bubble Menu](https://tiptap.dev/docs/editor/api/extensions/bubble-menu).

```tsx
<EditorBubble>
  <EditorBubbleItem />
  <EditorBubbleItem />
  <EditorBubbleItem />
</EditorBubble>
```

## Props

<ParamField required path="children" type="ReactNode" />

<ParamField path="className" type="string" />

<ParamField path="tippyOptions" type="Props" />


# Editor Bubble Item

Bubble Item

```tsx
<EditorBubbleItem
  key={index}
  onSelect={(editor) => {
    item.command(editor);
  }}>
  ...
</EditorBubbleItem>
```

## Props

<ParamField required path="children" type="ReactNode" />

<ParamField path="className" type="string" />

<ParamField path="onSelect" type="(editor: Editor) => void" />


# Editor Command

Wrapper for Command Items using cmdk

For all the available props, see [cmdk](https://github.com/pacocoursey/cmdk).

```tsx
<EditorCommand>
  <EditorCommandItem />
  <EditorCommandItem />
  <EditorCommandItem />
</EditorCommand>
```

## Props

<ParamField required path="children" type="ReactNode" />

<ParamField path="className" type="string" />


# Editor Command Item

Command Item

For all the available props, see [cmdk](https://github.com/pacocoursey/cmdk).

```tsx
  ...
  <EditorCommandItem
    value={item.title}
    onCommand={(val) => item.command(val)}>
    Do something
  </EditorCommand>
```

## Props

<ParamField required path="children" type="ReactNode" />

<ParamField required path="value" type="string">
  This value would be used for filtering
</ParamField>

<ParamField required path="onCommand" type="({ editor, range }: { editor: Editor; range: Range }) => void;">
  Callback function onSelect exposing editor and range
</ParamField>

<ParamField path="className" type="string" />


# Editor Content

Wrapper for Tiptap Provider 

For all the available props, see [Tiptap Settings](https://tiptap.dev/docs/editor/api/editor#settings).

```tsx
<EditorRoot>
  <EditorContent>{children}</EditorContent>
</EditorRoot>
```

## Props

<ParamField required path="children" type="ReactNode">
  A ReactNode that represents the content of the editor.
</ParamField>

<ParamField path="extensions" type="Extension[]" required>
  An array of Tiptap extensions to be used in the editor.
</ParamField>

<ParamField path="initialContent" type="JSONContent">
  Initial editor content in JSON format. [Tiptap
  Output](https://tiptap.dev/docs/editor/guide/output)
</ParamField>

<ParamField
  path="onUpdate"
  type="(props: {
  editor: Editor;
  transaction: Transaction;
  }) => void"
>
  Function that is called when the editor content is updated.
</ParamField>

<ParamField
  path="onCreate"
  type="onCreate?: (props: {
  editor: Editor;
  }) => void"
>
  Function that is called when the editor is created.
</ParamField>

<ParamField path="className" type="string">
  Classname for the parent container.
</ParamField>


# Editor Root

A wrapper component for the editor. It provides a consistent layout and styling for the editor.

<Info>
  This example demonstrates the use of Shadcn-ui for ui, but alternative libraries and components
  can also be employed.
</Info>

```tsx
<EditorRoot>{...}</EditorRoot>
```

## Props

<ParamField required path="children" type="ReactNode">
  A ReactNode that represents the content of the editor.
</ParamField>


# useEditor

Imperative API for interacting with the editor.

Your component must be a child of `EditorRoot` to use this hook.

```tsx
const CustomComponent = ({ open, onOpenChange }: LinkSelectorProps) => {
  const { editor } = useEditor();
...
}

<EditorRoot>
  <CustomComponent/>
</EditorRoot>
```

## Props

<ParamField path="editor" type="Editor">
  All methods are available here [Editor](https://tiptap.dev/docs/editor/api/editor)
</ParamField>


# Development

Learn how to contribute to Novel

<Info>**Prerequisite** You should have installed Node.js (version 18.10.0 or higher).</Info>

## Introduction

Novel's codebase is set up in a monorepo (via [Turborepo](https://turbo.build/repo)) and is fully [open-source on GitHub](https://github.com/steven-tey/novel).

Here's the monorepo structure:

```
apps
├── docs
├── web
packages
├── headless
├── tailwind-config
```

### Step 1: Local setup

First, clone the [Novel repo](https://novel.sh/github)

```bash
git clone https://github.com/steven-tey/novel
```

Run the following command to install the dependencies:

```bash
pnpm i
```

Install Mintlify CLI (for docs server):

```bash
pnpm i -g mintlify
```

### Step 2: Start the development server

Finally, you can start the development server. This will build the packages + start the app servers.

```bash
pnpm dev
```

### Step 3: Use Generative AI Local (Optional)

You can use Ollama to run your local AI server.\
[https://ollama.com/blog/openai-compatibility](https://ollama.com/blog/openai-compatibility)

```bash
# You cand find the config in the web app
/api/generate/route.ts
```


# AI Command (Soon)

Run AI commands in your editor

Comming soon


# Global Drag Handle (New)

Drag and drop blocks across the editor

<Steps>
  <Step title="Install the extension">
    Install the extension with a package manager of your choice.

    ```NPM
    $ npm i tiptap-extension-global-drag-handle
    ```

    ```Yarn
    $ yarn add tiptap-extension-global-drag-handle
    ```

    In order to enjoy all the advantages of a drag handle, it is recommended to install the auto joiner extension as well, which allows you to automatically join various nodes such as 2 lists that are next to each other.

    ```NPM
    $ npm i tiptap-extension-auto-joiner
    ```

    ```Yarn
    $ yarn add tiptap-extension-auto-joiner
    ```
  </Step>

  <Step title="Add drag extension">
    ```tsx
    // extensions.ts
    import GlobalDragHandle from 'tiptap-extension-global-drag-handle'
    import AutoJoiner from 'tiptap-extension-auto-joiner' // optional

    export const defaultExtensions = [
        GlobalDragHandle,
        AutoJoiner, // optional
        // other extensions
    ];

    // editor.tsx
    const Editor = () => {
        return <EditorContent extensions={defaultExtensions} />
    }
    ```
  </Step>

  <Step title="Configure the extension">
    ```tsx
    //extensions.ts
    import GlobalDragHandle from 'tiptap-extension-global-drag-handle'
    import AutoJoiner from 'tiptap-extension-auto-joiner' // optional

    export const defaultExtensions = [
        GlobalDragHandle.configure({
            dragHandleWidth: 20,    // default

            // The scrollTreshold specifies how close the user must drag an element to the edge of the lower/upper screen for automatic 
            // scrolling to take place. For example, scrollTreshold = 100 means that scrolling starts automatically when the user drags an 
            // element to a position that is max. 99px away from the edge of the screen
            // You can set this to 0 to prevent auto scrolling caused by this extension
            scrollTreshold: 100     // default
        }),
        AutoJoiner.configure({
            elementsToJoin: ["bulletList", "orderedList"] // default
        }),
        // other extensions
    ];

    // editor.tsx
    const Editor = () => {
        return <EditorContent extensions={defaultExtensions} />
    }
    ```
  </Step>

  <Step title="Add styling">
    By default the drag handle is headless, which means it doesn't contain any css. If you want to apply styling to the drag handle, use the class "drag-handle" in your css file.

    Take a look at [this](https://github.com/steven-tey/novel/blob/main/apps/web/styles/prosemirror.css#L131) to see an example of drag handle styling.
  </Step>
</Steps>


# Image Upload (New)

Uploading images in the editor

<Steps>
  <Step title="Add image extension">
    Configure image extension with your styling. The `imageClass` is used for styling the placeholder image.

    ```tsx
    //extensions.ts
    import { UploadImagesPlugin } from "novel/plugins";

    const tiptapImage = TiptapImage.extend({
        addProseMirrorPlugins() {
            return [
                UploadImagesPlugin({
                    imageClass: cx("opacity-40 rounded-lg border border-stone-200"),
                }),
            ];
        },
        }).configure({
        allowBase64: true,
        HTMLAttributes: {
            class: cx("rounded-lg border border-muted"),
        },
    });

    export const defaultExtensions = [
        tiptapImage,
        //other extensions
    ];

    //editor.tsx
    const Editor = () => {
        return <EditorContent extensions={defaultExtensions} />
    }

    ```
  </Step>

  <Step title="Create upload function">
    `onUpload` should return a `Promise<string>`
    `validateFn` is triggered before an image is uploaded. It should return a `boolean` value.

    ```tsx image-upload.ts
    import { createImageUpload } from "novel/plugins";
    import { toast } from "sonner";

    const onUpload = async (file: File) => {
        const promise = fetch("/api/upload", {
            method: "POST",
            headers: {
            "content-type": file?.type || "application/octet-stream",
            "x-vercel-filename": file?.name || "image.png",
            },
            body: file,
        });

        //This should return a src of the uploaded image
        return promise;
    };

    export const uploadFn = createImageUpload({
        onUpload,
        validateFn: (file) => {
            if (!file.type.includes("image/")) {
                toast.error("File type not supported.");
                return false;
            } else if (file.size / 1024 / 1024 > 20) {
                toast.error("File size too big (max 20MB).");
                return false;
            }
            return true;
        },
    });

    ```
  </Step>

  <Step title="Configure events callbacks">
    This is required to handle image paste and drop events in the editor.

    ```tsx editor.tsx
    import { handleImageDrop, handleImagePaste } from "novel/plugins";
    import { uploadFn } from "./image-upload";

    ...
    <EditorContent
            editorProps={{
                handlePaste: (view, event) => handleImagePaste(view, event, uploadFn),
                handleDrop: (view, event, _slice, moved) =>  handleImageDrop(view, event, moved, uploadFn),
                ...
            }}
    />
    ...
    ```
  </Step>

  <Step title="Update slash-command suggestionsItems">
    ```tsx
    import { ImageIcon } from "lucide-react";
    import { createSuggestionItems } from "novel/extensions";
    import { uploadFn } from "./image-upload";

    export const suggestionItems = createSuggestionItems([
        ...,
        {
            title: "Image",
            description: "Upload an image from your computer.",
            searchTerms: ["photo", "picture", "media"],
            icon: <ImageIcon size={18} />,
            command: ({ editor, range }) => {
                editor.chain().focus().deleteRange(range).run();
                // upload image
                const input = document.createElement("input");
                input.type = "file";
                input.accept = "image/*";
                input.onchange = async () => {
                    if (input.files?.length) {
                    const file = input.files[0];
                    const pos = editor.view.state.selection.from;
                    uploadFn(file, editor.view, pos);
                    }
                };
                input.click();
            },
        }
     ])
    ```
  </Step>
</Steps>


# Overview

Use Novel with your favorite styling or components

## Active integrations

<Card
  title="Tailwind"
  icon={
     <svg className='h-8 w-8' xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 54 33">
         <g clipPath="url(#prefix__clip0)">
             <path fill="#38bdf8" fillRule="evenodd" d="M27 0c-7.2 0-11.7 3.6-13.5 10.8 2.7-3.6 5.85-4.95 9.45-4.05 2.054.513 3.522 2.004 5.147 3.653C30.744 13.09 33.808 16.2 40.5 16.2c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C36.756 3.11 33.692 0 27 0zM13.5 16.2C6.3 16.2 1.8 19.8 0 27c2.7-3.6 5.85-4.95 9.45-4.05 2.054.514 3.522 2.004 5.147 3.653C17.244 29.29 20.308 32.4 27 32.4c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C23.256 19.31 20.192 16.2 13.5 16.2z" />
         </g>
         <defs>
             <clipPath id="prefix__clip0">
                 <path fill="#fff" d="M0 0h54v32.4H0z"/>
             </clipPath>
         </defs>
     </svg>
  }
  href="/guides/tailwind"
>
  Usage with Tailwind
</Card>

## Upcoming integrations

We are working on having more guides in the futures:

<Card>
  <b>CSS</b>
</Card>

<Card href="https://panda-css.com/">
  <b>Panda CSS</b>
</Card>


# Bubble Menu

Showcase of the Bubble Menu component in various configurations.

<img className="block dark:hidden" src="https://mintlify.s3-us-west-1.amazonaws.com/novel/images/bubble-light.png" alt="Hero Dark" />

<img className="hidden dark:block" src="https://mintlify.s3-us-west-1.amazonaws.com/novel/images/bubble-dark.png" alt="Hero Dark" />

We first have to create the selectors for the different types of nodes and links. We can then use these selectors to create the bubble menu.

<AccordionGroup>
  <Accordion title="Node Selector" icon="share-nodes">
    ```tsx node-selector.tsx
    import {
      Check,
      ChevronDown,
      Heading1,
      Heading2,
      Heading3,
      TextQuote,
      ListOrdered,
      TextIcon,
      Code,
      CheckSquare,
      type LucideIcon,
    } from "lucide-react";
    import { EditorBubbleItem, useEditor } from "novel";

    import { Popover } from "@radix-ui/react-popover";
    import { PopoverContent, PopoverTrigger } from "@/components/ui/popover";
    import { Button } from "@/components/ui/button";

    export type SelectorItem = {
      name: string;
      icon: LucideIcon;
      command: (editor: ReturnType<typeof useEditor>["editor"]) => void;
      isActive: (editor: ReturnType<typeof useEditor>["editor"]) => boolean;
    };

    const items: SelectorItem[] = [
      {
        name: "Text",
        icon: TextIcon,
        command: (editor) => editor.chain().focus().toggleNode("paragraph", "paragraph").run(),
        // I feel like there has to be a more efficient way to do this – feel free to PR if you know how!
        isActive: (editor) =>
          editor.isActive("paragraph") &&
          !editor.isActive("bulletList") &&
          !editor.isActive("orderedList"),
      },
      {
        name: "Heading 1",
        icon: Heading1,
        command: (editor) => editor.chain().focus().toggleHeading({ level: 1 }).run(),
        isActive: (editor) => editor.isActive("heading", { level: 1 }),
      },
      {
        name: "Heading 2",
        icon: Heading2,
        command: (editor) => editor.chain().focus().toggleHeading({ level: 2 }).run(),
        isActive: (editor) => editor.isActive("heading", { level: 2 }),
      },
      {
        name: "Heading 3",
        icon: Heading3,
        command: (editor) => editor.chain().focus().toggleHeading({ level: 3 }).run(),
        isActive: (editor) => editor.isActive("heading", { level: 3 }),
      },
      {
        name: "To-do List",
        icon: CheckSquare,
        command: (editor) => editor.chain().focus().toggleTaskList().run(),
        isActive: (editor) => editor.isActive("taskItem"),
      },
      {
        name: "Bullet List",
        icon: ListOrdered,
        command: (editor) => editor.chain().focus().toggleBulletList().run(),
        isActive: (editor) => editor.isActive("bulletList"),
      },
      {
        name: "Numbered List",
        icon: ListOrdered,
        command: (editor) => editor.chain().focus().toggleOrderedList().run(),
        isActive: (editor) => editor.isActive("orderedList"),
      },
      {
        name: "Quote",
        icon: TextQuote,
        command: (editor) =>
          editor.chain().focus().toggleNode("paragraph", "paragraph").toggleBlockquote().run(),
        isActive: (editor) => editor.isActive("blockquote"),
      },
      {
        name: "Code",
        icon: Code,
        command: (editor) => editor.chain().focus().toggleCodeBlock().run(),
        isActive: (editor) => editor.isActive("codeBlock"),
      },
    ];
    interface NodeSelectorProps {
      open: boolean;
      onOpenChange: (open: boolean) => void;
    }

    export const NodeSelector = ({ open, onOpenChange }: NodeSelectorProps) => {
      const { editor } = useEditor();
      if (!editor) return null;
      const activeItem = items.filter((item) => item.isActive(editor)).pop() ?? {
        name: "Multiple",
      };

      return (
        <Popover modal={true} open={open} onOpenChange={onOpenChange}>
          <PopoverTrigger
            asChild
            className='gap-2 rounded-none border-none hover:bg-accent focus:ring-0'>
            <Button variant='ghost' className='gap-2'>
              <span className='whitespace-nowrap text-sm'>{activeItem.name}</span>
              <ChevronDown className='h-4 w-4' />
            </Button>
          </PopoverTrigger>
          <PopoverContent sideOffset={5} align='start' className='w-48 p-1'>
            {items.map((item, index) => (
              <EditorBubbleItem
                key={index}
                onSelect={(editor) => {
                  item.command(editor);
                  onOpenChange(false);
                }}
                className='flex cursor-pointer items-center justify-between rounded-sm px-2 py-1 text-sm hover:bg-accent'>
                <div className='flex items-center space-x-2'>
                  <div className='rounded-sm border p-1'>
                    <item.icon className='h-3 w-3' />
                  </div>
                  <span>{item.name}</span>
                </div>
                {activeItem.name === item.name && <Check className='h-4 w-4' />}
              </EditorBubbleItem>
            ))}
          </PopoverContent>
        </Popover>
      );
    };
    ```
  </Accordion>

  <Accordion title="Link Selector" icon="link">
    ```tsx link-selector.tsx
    import { cn } from "@/lib/utils";
    import { useEditor } from "novel";
    import { Check, Trash } from "lucide-react";
    import { type Dispatch, type FC, type SetStateAction, useEffect, useRef } from "react";
    import { Popover, PopoverTrigger } from "@radix-ui/react-popover";
    import { Button } from "@/components/tailwind/ui/button";
    import { PopoverContent } from "@/components/tailwind/ui/popover";

    export function isValidUrl(url: string) {
      try {
        new URL(url);
        return true;
      } catch (e) {
        return false;
      }
    }
    export function getUrlFromString(str: string) {
      if (isValidUrl(str)) return str;
      try {
        if (str.includes(".") && !str.includes(" ")) {
          return new URL(`https://${str}`).toString();
        }
      } catch (e) {
        return null;
      }
    }
    interface LinkSelectorProps {
      open: boolean;
      onOpenChange: (open: boolean) => void;
    }

    export const LinkSelector = ({ open, onOpenChange }: LinkSelectorProps) => {
      const inputRef = useRef<HTMLInputElement>(null);
      const { editor } = useEditor();

      // Autofocus on input by default
      useEffect(() => {
        inputRef.current && inputRef.current?.focus();
      });
      if (!editor) return null;

      return (
        <Popover modal={true} open={open} onOpenChange={onOpenChange}>
          <PopoverTrigger asChild>
            <Button variant='ghost' className='gap-2 rounded-none border-none'>
              <p className='text-base'>↗</p>
              <p
                className={cn("underline decoration-stone-400 underline-offset-4", {
                  "text-blue-500": editor.isActive("link"),
                })}>
                Link
              </p>
            </Button>
          </PopoverTrigger>
          <PopoverContent align='start' className='w-60 p-0' sideOffset={10}>
            <form
              onSubmit={(e) => {
                const target = e.currentTarget as HTMLFormElement;
                e.preventDefault();
                const input = target[0] as HTMLInputElement;
                const url = getUrlFromString(input.value);
                url && editor.chain().focus().setLink({ href: url }).run();
              }}
              className='flex  p-1 '>
              <input
                ref={inputRef}
                type='text'
                placeholder='Paste a link'
                className='flex-1 bg-background p-1 text-sm outline-none'
                defaultValue={editor.getAttributes("link").href || ""}
              />
              {editor.getAttributes("link").href ? (
                <Button
                  size='icon'
                  variant='outline'
                  type='button'
                  className='flex h-8 items-center rounded-sm p-1 text-red-600 transition-all hover:bg-red-100 dark:hover:bg-red-800'
                  onClick={() => {
                    editor.chain().focus().unsetLink().run();
                  }}>
                  <Trash className='h-4 w-4' />
                </Button>
              ) : (
                <Button size='icon' className='h-8'>
                  <Check className='h-4 w-4' />
                </Button>
              )}
            </form>
          </PopoverContent>
        </Popover>
      );
    };
    ```
  </Accordion>

  <Accordion title="Text Buttons" icon="bold">
    ```tsx text-buttons.tsx
    import { cn } from "@/lib/utils";
    import { EditorBubbleItem, useEditor } from "novel";
    import { BoldIcon, ItalicIcon, UnderlineIcon, StrikethroughIcon, CodeIcon } from "lucide-react";
    import type { SelectorItem } from "./node-selector";
    import { Button } from "@/components/tailwind/ui/button";

    export const TextButtons = () => {
      const { editor } = useEditor();
      if (!editor) return null;
      const items: SelectorItem[] = [
        {
          name: "bold",
          isActive: (editor) => editor.isActive("bold"),
          command: (editor) => editor.chain().focus().toggleBold().run(),
          icon: BoldIcon,
        },
        {
          name: "italic",
          isActive: (editor) => editor.isActive("italic"),
          command: (editor) => editor.chain().focus().toggleItalic().run(),
          icon: ItalicIcon,
        },
        {
          name: "underline",
          isActive: (editor) => editor.isActive("underline"),
          command: (editor) => editor.chain().focus().toggleUnderline().run(),
          icon: UnderlineIcon,
        },
        {
          name: "strike",
          isActive: (editor) => editor.isActive("strike"),
          command: (editor) => editor.chain().focus().toggleStrike().run(),
          icon: StrikethroughIcon,
        },
        {
          name: "code",
          isActive: (editor) => editor.isActive("code"),
          command: (editor) => editor.chain().focus().toggleCode().run(),
          icon: CodeIcon,
        },
      ];
      return (
        <div className='flex'>
          {items.map((item, index) => (
            <EditorBubbleItem
              key={index}
              onSelect={(editor) => {
                item.command(editor);
              }}>
              <Button size='icon' className='rounded-none' variant='ghost'>
                <item.icon
                  className={cn("h-4 w-4", {
                    "text-blue-500": item.isActive(editor),
                  })}
                />
              </Button>
            </EditorBubbleItem>
          ))}
        </div>
      );
    };
    ```
  </Accordion>

  <Accordion title="Color Selector" icon="palette">
    ```tsx color-selector.tsx
    import { Check, ChevronDown } from "lucide-react";
    import type { Dispatch, SetStateAction } from "react";
    import { EditorBubbleItem, useEditor } from "novel";

    import { PopoverTrigger, Popover, PopoverContent } from "@/components/tailwind/ui/popover";
    import { Button } from "@/components/tailwind/ui/button";
    export interface BubbleColorMenuItem {
      name: string;
      color: string;
    }

    interface ColorSelectorProps {
      isOpen: boolean;
      setIsOpen: Dispatch<SetStateAction<boolean>>;
    }

    const TEXT_COLORS: BubbleColorMenuItem[] = [
      {
        name: "Default",
        color: "var(--novel-black)",
      },
      {
        name: "Purple",
        color: "#9333EA",
      },
      {
        name: "Red",
        color: "#E00000",
      },
      {
        name: "Yellow",
        color: "#EAB308",
      },
      {
        name: "Blue",
        color: "#2563EB",
      },
      {
        name: "Green",
        color: "#008A00",
      },
      {
        name: "Orange",
        color: "#FFA500",
      },
      {
        name: "Pink",
        color: "#BA4081",
      },
      {
        name: "Gray",
        color: "#A8A29E",
      },
    ];

    const HIGHLIGHT_COLORS: BubbleColorMenuItem[] = [
      {
        name: "Default",
        color: "var(--novel-highlight-default)",
      },
      {
        name: "Purple",
        color: "var(--novel-highlight-purple)",
      },
      {
        name: "Red",
        color: "var(--novel-highlight-red)",
      },
      {
        name: "Yellow",
        color: "var(--novel-highlight-yellow)",
      },
      {
        name: "Blue",
        color: "var(--novel-highlight-blue)",
      },
      {
        name: "Green",
        color: "var(--novel-highlight-green)",
      },
      {
        name: "Orange",
        color: "var(--novel-highlight-orange)",
      },
      {
        name: "Pink",
        color: "var(--novel-highlight-pink)",
      },
      {
        name: "Gray",
        color: "var(--novel-highlight-gray)",
      },
    ];

    interface ColorSelectorProps {
      open: boolean;
      onOpenChange: (open: boolean) => void;
    }

    export const ColorSelector = ({ open, onOpenChange }) => {
      const { editor } = useEditor();

      if (!editor) return null;
      const activeColorItem = TEXT_COLORS.find(({ color }) => editor.isActive("textStyle", { color }));

      const activeHighlightItem = HIGHLIGHT_COLORS.find(({ color }) =>
        editor.isActive("highlight", { color })
      );

      return (
        <Popover modal={true} open={open} onOpenChange={onOpenChange}>
          <PopoverTrigger asChild>
            <Button className='gap-2 rounded-none' variant='ghost'>
              <span
                className='rounded-sm px-1'
                style={{
                  color: activeColorItem?.color,
                  backgroundColor: activeHighlightItem?.color,
                }}>
                A
              </span>
              <ChevronDown className='h-4 w-4' />
            </Button>
          </PopoverTrigger>

          <PopoverContent
            sideOffset={5}
            className='my-1 flex max-h-80 w-48 flex-col overflow-hidden overflow-y-auto rounded border p-1 shadow-xl '
            align='start'>
            <div className='flex flex-col'>
              <div className='my-1 px-2 text-sm font-semibold text-muted-foreground'>Color</div>
              {TEXT_COLORS.map(({ name, color }, index) => (
                <EditorBubbleItem
                  key={index}
                  onSelect={() => {
                    editor.commands.unsetColor();
                    name !== "Default" &&
                      editor
                        .chain()
                        .focus()
                        .setColor(color || "")
                        .run();
                  }}
                  className='flex cursor-pointer items-center justify-between px-2 py-1 text-sm hover:bg-accent'>
                  <div className='flex items-center gap-2'>
                    <div className='rounded-sm border px-2 py-px font-medium' style={{ color }}>
                      A
                    </div>
                    <span>{name}</span>
                  </div>
                </EditorBubbleItem>
              ))}
            </div>
            <div>
              <div className='my-1 px-2 text-sm font-semibold text-muted-foreground'>Background</div>
              {HIGHLIGHT_COLORS.map(({ name, color }, index) => (
                <EditorBubbleItem
                  key={index}
                  onSelect={() => {
                    editor.commands.unsetHighlight();
                    name !== "Default" && editor.commands.setHighlight({ color });
                  }}
                  className='flex cursor-pointer items-center justify-between px-2 py-1 text-sm hover:bg-accent'>
                  <div className='flex items-center gap-2'>
                    <div
                      className='rounded-sm border px-2 py-px font-medium'
                      style={{ backgroundColor: color }}>
                      A
                    </div>
                    <span>{name}</span>
                  </div>
                  {editor.isActive("highlight", { color }) && <Check className='h-4 w-4' />}
                </EditorBubbleItem>
              ))}
            </div>
          </PopoverContent>
        </Popover>
      );
    };
    ```
  </Accordion>
</AccordionGroup>

```tsx editor.tsx
import { NodeSelector } from "./selectors/node-selector";
import { LinkSelector } from "./selectors/link-selector";
import { ColorSelector } from "./selectors/color-selector";
import { TextButtons } from "./selectors/text-buttons";


...
<EditorContent>
  <EditorBubble
    tippyOptions={{
      placement: openAI ? "bottom-start" : "top",
    }}
    className='flex w-fit max-w-[90vw] overflow-hidden rounded border border-muted bg-background shadow-xl'>
      <NodeSelector open={openNode} onOpenChange={setOpenNode} />
      <LinkSelector open={openLink} onOpenChange={setOpenLink} />
      <TextButtons />
      <ColorSelector open={openColor} onOpenChange={setOpenColor} />
  </EditorBubble>
</EditorContent>;
...
```


# Extensions

Styled and configured Tiptap extensions for your editor

<Info>You can use any Tiptap extensions or create your own.</Info>

## Default Extensions

```tsx extensions.ts
import {
  TiptapImage,
  TiptapLink,
  UpdatedImage,
  TaskList,
  TaskItem,
  HorizontalRule,
  StarterKit,
  Placeholder,
} from "novel/extensions";

import { cx } from "class-variance-authority";

// TODO I am using cx here to get tailwind autocomplete working, idk if someone else can write a regex to just capture the class key in objects

// You can overwrite the placeholder with your own configuration
const placeholder = Placeholder;
const tiptapLink = TiptapLink.configure({
  HTMLAttributes: {
    class: cx(
      "text-muted-foreground underline underline-offset-[3px] hover:text-primary transition-colors cursor-pointer",
    ),
  },
});

const taskList = TaskList.configure({
  HTMLAttributes: {
    class: cx("not-prose pl-2"),
  },
});
const taskItem = TaskItem.configure({
  HTMLAttributes: {
    class: cx("flex items-start my-4"),
  },
  nested: true,
});

const horizontalRule = HorizontalRule.configure({
  HTMLAttributes: {
    class: cx("mt-4 mb-6 border-t border-muted-foreground"),
  },
});

const starterKit = StarterKit.configure({
  bulletList: {
    HTMLAttributes: {
      class: cx("list-disc list-outside leading-3 -mt-2"),
    },
  },
  orderedList: {
    HTMLAttributes: {
      class: cx("list-decimal list-outside leading-3 -mt-2"),
    },
  },
  listItem: {
    HTMLAttributes: {
      class: cx("leading-normal -mb-2"),
    },
  },
  blockquote: {
    HTMLAttributes: {
      class: cx("border-l-4 border-primary"),
    },
  },
  codeBlock: {
    HTMLAttributes: {
      class: cx("rounded-sm bg-muted border p-5 font-mono font-medium"),
    },
  },
  code: {
    HTMLAttributes: {
      class: cx("rounded-md bg-muted  px-1.5 py-1 font-mono font-medium"),
      spellcheck: "false",
    },
  },
  horizontalRule: false,
  dropcursor: {
    color: "#DBEAFE",
    width: 4,
  },
  gapcursor: false,
});

export const defaultExtensions = [
  starterKit,
  placeholder,
  TiptapLink,
  TiptapImage,
  UpdatedImage,
  taskList,
  taskItem,
  horizontalRule,
];
```

<Note>
  For intellisense in your VS Code editor you can also add this regex to the `settings.json`

  ```json
    "tailwindCSS.experimental.classRegex":[["cx\\(([^)]*)\\)", "(?:'|\"|`)([^']*)(?:'|\"|`)"]],
  ```
</Note>

## Custom Extension

Coming soon


# Setup

Follow this guide to set up Novel with Tailwindcss

<Info>
  This example demonstrates the use of Shadcn-ui for ui, but alternative
  libraries and components can also be employed.
</Info>

<Card title="Shadcn-ui" icon="link" href="https://ui.shadcn.com/docs/installation">
  You can find more info about installing shadcn-ui here. You will need to add
  the following components: <b>Button, Separator, Popover, Command, Dialog</b>
</Card>

This example will use the same stucture from here: [Anatomy](/quickstart#anatomy)\
You can find the full example here: [Tailwind Example](https://github.com/steven-tey/novel/blob/main/apps/web/components/tailwind/advanced-editor.tsx)

## Configure Wrapper

```tsx
"use client";

import { EditorContent, EditorRoot } from "novel";
import { useState } from "react";

const TailwindEditor = () => {
  const [content, setContent] = useState(null);
  return (
    <EditorRoot>
      <EditorContent
        initialContent={content}
        onUpdate={({ editor }) => {
          const json = editor.getJSON();
          setContent(json);
        }}
      />
    </EditorRoot>
  );
};
export default TailwindEditor;
```

<Tip>
  `onUpdate` runs on every change. In most cases, you will want to debounce the updates to prevent too many state changes.

  ```tsx
  import { EditorInstance } from "novel"

  ...
  const debouncedUpdates = useDebouncedCallback(async (editor: EditorInstance) => {
    const json = editor.getJSON();
    setContent(json);
    setSaveStatus("Saved");
  }, 500);

  onUpdate={debouncedUpdates};
  ```
</Tip>

## Configure Extensions

<Card title="Extensions" icon="link" href="/guides/tailwind/extensions">
  You can find here example of extensions
</Card>

```tsx
import { defaultExtensions } from "./extensions";

const extensions = [...defaultExtensions];

<EditorContent
  extensions={extensions}
  ...
/>;
```

## Create Menus

<CardGroup cols={2}>
  <Card title="Slash Command" href="/guides/tailwind/slash-command" icon="terminal">
    Slash commands are a way to quickly insert content into the editor.
  </Card>

  <Card title="Bubble Menu" href="/guides/tailwind/bubble-menu" icon="square-caret-down">
    The bubble menu is a context menu that appears when you select text.
  </Card>
</CardGroup>

## Add Editor Props

`handleCommandNavigation` is required for fixing the arrow navigation in the / command;

```tsx
import { handleCommandNavigation } from "novel/extensions";
import { defaultEditorProps, EditorContent } from "novel";

<EditorContent
  ...
  editorProps={{
      handleDOMEvents: {
        keydown: (_view, event) => handleCommandNavigation(event),
      },
      attributes: {
        class: `prose prose-lg dark:prose-invert prose-headings:font-title font-default focus:outline-none max-w-full`,
      }
  }}
/>
```

## Add Styles

<AccordionGroup>
  <Accordion title="Prosemirror Styles" icon="css3">
    ```css prosemirror.css
    .ProseMirror {
      @apply p-12 px-8 sm:px-12;
    }

    .ProseMirror .is-editor-empty:first-child::before {
      content: attr(data-placeholder);
      float: left;
      color: hsl(var(--muted-foreground));
      pointer-events: none;
      height: 0;
    }
    .ProseMirror .is-empty::before {
      content: attr(data-placeholder);
      float: left;
      color: hsl(var(--muted-foreground));
      pointer-events: none;
      height: 0;
    }

    /* Custom image styles */
    .ProseMirror img {
      transition: filter 0.1s ease-in-out;

      &:hover {
        cursor: pointer;
        filter: brightness(90%);
      }

      &.ProseMirror-selectednode {
        outline: 3px solid #5abbf7;
        filter: brightness(90%);
      }
    }

    .img-placeholder {
      position: relative;

      &:before {
        content: "";
        box-sizing: border-box;
        position: absolute;
        top: 50%;
        left: 50%;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: 3px solid var(--novel-stone-200);
        border-top-color: var(--novel-stone-800);
        animation: spinning 0.6s linear infinite;
      }
    }

    @keyframes spinning {
      to {
        transform: rotate(360deg);
      }
    }

    /* Custom TODO list checkboxes – shoutout to this awesome tutorial: https://moderncss.dev/pure-css-custom-checkbox-style/ */
    ul[data-type="taskList"] li > label {
      margin-right: 0.2rem;
      user-select: none;
    }

    @media screen and (max-width: 768px) {
      ul[data-type="taskList"] li > label {
        margin-right: 0.5rem;
      }
    }

    ul[data-type="taskList"] li > label input[type="checkbox"] {
      -webkit-appearance: none;
      appearance: none;
      background-color: hsl(var(--background));
      margin: 0;
      cursor: pointer;
      width: 1.2em;
      height: 1.2em;
      position: relative;
      top: 5px;
      border: 2px solid hsl(var(--border));
      margin-right: 0.3rem;
      display: grid;
      place-content: center;

      &:hover {
        background-color: hsl(var(--accent));
      }

      &:active {
        background-color: hsl(var(--accent));
      }

      &::before {
        content: "";
        width: 0.65em;
        height: 0.65em;
        transform: scale(0);
        transition: 120ms transform ease-in-out;
        box-shadow: inset 1em 1em;
        transform-origin: center;
        clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
      }

      &:checked::before {
        transform: scale(1);
      }
    }

    ul[data-type="taskList"] li[data-checked="true"] > div > p {
      color: var(--muted-foreground);
      text-decoration: line-through;
      text-decoration-thickness: 2px;
    }

    /* Overwrite tippy-box original max-width */
    .tippy-box {
      max-width: 400px !important;
    }

    .ProseMirror:not(.dragging) .ProseMirror-selectednode {
      outline: none !important;
      background-color: var(--novel-highlight-blue);
      transition: background-color 0.2s;
      box-shadow: none;
    }

    .drag-handle {
      position: fixed;
      opacity: 1;
      transition: opacity ease-in 0.2s;
      border-radius: 0.25rem;

      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 10 10' style='fill: rgba(0, 0, 0, 0.5)'%3E%3Cpath d='M3,2 C2.44771525,2 2,1.55228475 2,1 C2,0.44771525 2.44771525,0 3,0 C3.55228475,0 4,0.44771525 4,1 C4,1.55228475 3.55228475,2 3,2 Z M3,6 C2.44771525,6 2,5.55228475 2,5 C2,4.44771525 2.44771525,4 3,4 C3.55228475,4 4,4.44771525 4,5 C4,5.55228475 3.55228475,6 3,6 Z M3,10 C2.44771525,10 2,9.55228475 2,9 C2,8.44771525 2.44771525,8 3,8 C3.55228475,8 4,8.44771525 4,9 C4,9.55228475 3.55228475,10 3,10 Z M7,2 C6.44771525,2 6,1.55228475 6,1 C6,0.44771525 6.44771525,0 7,0 C7.55228475,0 8,0.44771525 8,1 C8,1.55228475 7.55228475,2 7,2 Z M7,6 C6.44771525,6 6,5.55228475 6,5 C6,4.44771525 6.44771525,4 7,4 C7.55228475,4 8,4.44771525 8,5 C8,5.55228475 7.55228475,6 7,6 Z M7,10 C6.44771525,10 6,9.55228475 6,9 C6,8.44771525 6.44771525,8 7,8 C7.55228475,8 8,8.44771525 8,9 C8,9.55228475 7.55228475,10 7,10 Z'%3E%3C/path%3E%3C/svg%3E");
      background-size: calc(0.5em + 0.375rem) calc(0.5em + 0.375rem);
      background-repeat: no-repeat;
      background-position: center;
      width: 1.2rem;
      height: 1.5rem;
      z-index: 50;
      cursor: grab;

      &:hover {
        background-color: var(--novel-stone-100);
        transition: background-color 0.2s;
      }

      &:active {
        background-color: var(--novel-stone-200);
        transition: background-color 0.2s;
        cursor: grabbing;
      }

      &.hide {
        opacity: 0;
        pointer-events: none;
      }

      @media screen and (max-width: 600px) {
        display: none;
        pointer-events: none;
      }
    }

    .dark .drag-handle {
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 10 10' style='fill: rgba(255, 255, 255, 0.5)'%3E%3Cpath d='M3,2 C2.44771525,2 2,1.55228475 2,1 C2,0.44771525 2.44771525,0 3,0 C3.55228475,0 4,0.44771525 4,1 C4,1.55228475 3.55228475,2 3,2 Z M3,6 C2.44771525,6 2,5.55228475 2,5 C2,4.44771525 2.44771525,4 3,4 C3.55228475,4 4,4.44771525 4,5 C4,5.55228475 3.55228475,6 3,6 Z M3,10 C2.44771525,10 2,9.55228475 2,9 C2,8.44771525 2.44771525,8 3,8 C3.55228475,8 4,8.44771525 4,9 C4,9.55228475 3.55228475,10 3,10 Z M7,2 C6.44771525,2 6,1.55228475 6,1 C6,0.44771525 6.44771525,0 7,0 C7.55228475,0 8,0.44771525 8,1 C8,1.55228475 7.55228475,2 7,2 Z M7,6 C6.44771525,6 6,5.55228475 6,5 C6,4.44771525 6.44771525,4 7,4 C7.55228475,4 8,4.44771525 8,5 C8,5.55228475 7.55228475,6 7,6 Z M7,10 C6.44771525,10 6,9.55228475 6,9 C6,8.44771525 6.44771525,8 7,8 C7.55228475,8 8,8.44771525 8,9 C8,9.55228475 7.55228475,10 7,10 Z'%3E%3C/path%3E%3C/svg%3E");
    }

    /* Custom Youtube Video CSS */
    iframe {
      border: 8px solid #ffd00027;
      border-radius: 4px;
      min-width: 200px;
      min-height: 200px;
      display: block;
      outline: 0px solid transparent;
    }

    div[data-youtube-video] > iframe {
      cursor: move;
      aspect-ratio: 16 / 9;
      width: 100%;
    }

    .ProseMirror-selectednode iframe {
      transition: outline 0.15s;
      outline: 6px solid #fbbf24;
    }

    @media only screen and (max-width: 480px) {
      div[data-youtube-video] > iframe {
        max-height: 50px;
      }
    }

    @media only screen and (max-width: 720px) {
      div[data-youtube-video] > iframe {
        max-height: 100px;
      }
    }

    /* CSS for bold coloring and highlighting issue*/
    span[style] > strong {
      color: inherit;
    }

    mark[style] > strong {
      color: inherit;
    }

    ```
  </Accordion>

  <Accordion title="Globals CSS" icon="globe">
    Update your globals.css with Novel css vars

    ```css globals.css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    @layer base {
      :root {
        ...
        --novel-highlight-default: #ffffff;
        --novel-highlight-purple: #f6f3f8;
        --novel-highlight-red: #fdebeb;
        --novel-highlight-yellow: #fbf4a2;
        --novel-highlight-blue: #c1ecf9;
        --novel-highlight-green: #acf79f;
        --novel-highlight-orange: #faebdd;
        --novel-highlight-pink: #faf1f5;
        --novel-highlight-gray: #f1f1ef;

      }

      .dark {
        ....

        --novel-highlight-default: #000000;
        --novel-highlight-purple: #3f2c4b;
        --novel-highlight-red: #5c1a1a;
        --novel-highlight-yellow: #5c4b1a;
        --novel-highlight-blue: #1a3d5c;
        --novel-highlight-green: #1a5c20;
        --novel-highlight-orange: #5c3a1a;
        --novel-highlight-pink: #5c1a3a;
        --novel-highlight-gray: #3a3a3a;

      }
    }

    ```
  </Accordion>
</AccordionGroup>

<Note>You need `require("@tailwindcss/typography")` for the prose styling</Note>

## Usage within Dialogs

Novel has been designed to work automatically within Radix Dialogs, namely by looking for the closest parent attribute `[role="dialog"]`. If you're using a different implementation for popups and dialogs, ensure you add this attribute above the editor so the drag handle calculates the correct position.


# Slash Command

Create a slash command to insert content into the editor.

## Define suggestions

We export a helper to define the suggestions that will be shown in the command palette. `createSuggestionItems`

```tsx
import {
  CheckSquare,
  Code,
  Heading1,
  Heading2,
  Heading3,
  List,
  ListOrdered,
  MessageSquarePlus,
  Text,
  TextQuote,
} from "lucide-react";
import { createSuggestionItems } from "novel/extensions";
import { startImageUpload } from "novel/plugins";
import { Command, renderItems } from "novel/extensions";

export const suggestionItems = createSuggestionItems([
  {
    title: "Send Feedback",
    description: "Let us know how we can improve.",
    icon: <MessageSquarePlus size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).run();
      window.open("/feedback", "_blank");
    },
  },
  {
    title: "Text",
    description: "Just start typing with plain text.",
    searchTerms: ["p", "paragraph"],
    icon: <Text size={18} />,
    command: ({ editor, range }) => {
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .toggleNode("paragraph", "paragraph")
        .run();
    },
  },
  {
    title: "To-do List",
    description: "Track tasks with a to-do list.",
    searchTerms: ["todo", "task", "list", "check", "checkbox"],
    icon: <CheckSquare size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleTaskList().run();
    },
  },
  {
    title: "Heading 1",
    description: "Big section heading.",
    searchTerms: ["title", "big", "large"],
    icon: <Heading1 size={18} />,
    command: ({ editor, range }) => {
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .setNode("heading", { level: 1 })
        .run();
    },
  },
  {
    title: "Heading 2",
    description: "Medium section heading.",
    searchTerms: ["subtitle", "medium"],
    icon: <Heading2 size={18} />,
    command: ({ editor, range }) => {
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .setNode("heading", { level: 2 })
        .run();
    },
  },
  {
    title: "Heading 3",
    description: "Small section heading.",
    searchTerms: ["subtitle", "small"],
    icon: <Heading3 size={18} />,
    command: ({ editor, range }) => {
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .setNode("heading", { level: 3 })
        .run();
    },
  },
  {
    title: "Bullet List",
    description: "Create a simple bullet list.",
    searchTerms: ["unordered", "point"],
    icon: <List size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleBulletList().run();
    },
  },
  {
    title: "Numbered List",
    description: "Create a list with numbering.",
    searchTerms: ["ordered"],
    icon: <ListOrdered size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleOrderedList().run();
    },
  },
  {
    title: "Quote",
    description: "Capture a quote.",
    searchTerms: ["blockquote"],
    icon: <TextQuote size={18} />,
    command: ({ editor, range }) =>
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .toggleNode("paragraph", "paragraph")
        .toggleBlockquote()
        .run(),
  },
  {
    title: "Code",
    description: "Capture a code snippet.",
    searchTerms: ["codeblock"],
    icon: <Code size={18} />,
    command: ({ editor, range }) =>
      editor.chain().focus().deleteRange(range).toggleCodeBlock().run(),
  },
]);

export const slashCommand = Command.configure({
  suggestion: {
    items: () => suggestionItems,
    render: renderItems,
  },
});
```

## Register the command

We need to add the command to the extensions array

```tsx
const extensions = [...defaultExtensions, slashCommand];

<EditorContent
  extensions={extensions}
  ...
/>;
```

## Create UI for the command

We map the suggestionItems and use the `EditorCommand` and `EditorCommandItem` components to create the UI for the command palette.
Components are wrapper over cmdk

```tsx
...
<EditorContent>
  <EditorCommand className='z-50 h-auto max-h-[330px]  w-72 overflow-y-auto rounded-md border border-muted bg-background px-1 py-2 shadow-md transition-all'>
    <EditorCommandEmpty className='px-2 text-muted-foreground'>No results</EditorCommandEmpty>
<EditorCommandList>
    {suggestionItems.map((item) => (
      <EditorCommandItem
        value={item.title}
        onCommand={(val) => item.command(val)}
        className={`flex w-full items-center space-x-2 rounded-md px-2 py-1 text-left text-sm hover:bg-accent aria-selected:bg-accent `}
        key={item.title}>
        <div className='flex h-10 w-10 items-center justify-center rounded-md border border-muted bg-background'>
          {item.icon}
        </div>
        <div>
          <p className='font-medium'>{item.title}</p>
          <p className='text-xs text-muted-foreground'>{item.description}</p>
        </div>
      </EditorCommandItem>
    ))}
</EditorCommandList>
  </EditorCommand>
</EditorContent>
...
```


# Introduction

Novel is a headless Notion-style WYSIWYG editor

<img className="block dark:hidden" src="https://mintlify.s3-us-west-1.amazonaws.com/novel/images/hero-light.png" alt="Hero Light" />

<img className="hidden dark:block" src="https://mintlify.s3-us-west-1.amazonaws.com/novel/images/hero-dark.png" alt="Hero Dark" />

## Features

TODO: Add features

## Tech Stack

Novel's codebase is [fully open-source](https://github.com/steven-tey/novel) and is built on top of the following technologies:

*   [Tiptap](https://tiptap.dev/) – framework
*   [TypeScript](https://www.typescriptlang.org/) – language
*   [RadixUI](https://www.radix-ui.com/primitives) – components
*   [Cmdk](https://cmdk.paco.me/) – command


# Quickstart

Start using the editor in 5 minutes

## Installation

Novel package doeesn't have any styles included. It's just a collection of custom configs and components for Tiptap.

<CodeGroup>
  ```bash npm
  npm i novel
  ```

  ```bash yarn
  yarn add novel
  ```

  ```bash pnpm
  pnpm add novel
  ```
</CodeGroup>

## Usage

<CardGroup>
  <Card
    title="Tailwind"
    icon={
       <svg className='h-8 w-8' xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 54 33">
           <g clipPath="url(#prefix__clip0)">
               <path fill="#38bdf8" fillRule="evenodd" d="M27 0c-7.2 0-11.7 3.6-13.5 10.8 2.7-3.6 5.85-4.95 9.45-4.05 2.054.513 3.522 2.004 5.147 3.653C30.744 13.09 33.808 16.2 40.5 16.2c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C36.756 3.11 33.692 0 27 0zM13.5 16.2C6.3 16.2 1.8 19.8 0 27c2.7-3.6 5.85-4.95 9.45-4.05 2.054.514 3.522 2.004 5.147 3.653C17.244 29.29 20.308 32.4 27 32.4c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C23.256 19.31 20.192 16.2 13.5 16.2z" />
           </g>
           <defs>
               <clipPath id="prefix__clip0">
                   <path fill="#fff" d="M0 0h54v32.4H0z"/>
               </clipPath>
           </defs>
       </svg>
    }
    href="/guides/tailwind"
  >
    Usage with Tailwind and Shadcn-UI
  </Card>

  <Card icon="react" href="/components" title="Custom">
    Write your own styles using the Novel components
  </Card>
</CardGroup>

## Anatomy

This is mostly how you would use the editor in your application. Similar to Radix Primitives, Novel exports a set of components that you can use to build your own editor.

```tsx
import {
  EditorBubble,
  EditorBubbleItem,
  EditorCommand,
  EditorCommandItem,
  EditorContent,
  EditorRoot,
} from "novel";

export default () => (
  <EditorRoot>
    <EditorContent>
      <EditorCommand>
        <EditorCommandItem />
        <EditorCommandItem />
        <EditorCommandItem />
      </EditorCommand>
      <EditorBubble>
        <EditorBubbleItem />
        <EditorBubbleItem />
        <EditorBubbleItem />
      </EditorBubble>
    </EditorContent>
  </EditorRoot>
);
```


