# Source: https://docs.augmentcode.com/using-augment/instructions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Instructions

> Use Instructions to write or modify blocks of code using natural language. Refactor a function, write unit tests, or craft any prompt to transform your code.

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

<Availability tags={["vscode",]} />

## About Instructions

Augment's Instructions let you use natural language prompts to insert new code or modify your existing code. Instructions can be initiated by hitting <Keyboard shortcut="Cmd/Ctrl I" /> and entering an instruction inside the input box that appears in the diff view. The change will be applied as a diff to be reviewed before accepting.

## Using Instructions

To start a new Instruction, there are two options. You can select & highlight the code you want to change or place your cursor where you want new code to be added, then press <Keyboard shortcut="Cmd/Ctrl I" />. You'll be taken to a diff view where you can enter your prompt and see the results.

For example, you can generate new functions based on existing code:

```
> Add a getUser function that takes userId as a parameter
```

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bb67b9d0048e2a7c1ed23b9c3cccc8eb" className="rounded-xl" alt="Augment Instructions Diff" data-og-width="1310" width="1310" data-og-height="695" height="695" data-path="images/instructions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=238e917a8ba8599ec9b42f937b57096b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=27e6a8088a09230d96fb467c41b9b12c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bc05e6b31dad514fa287b2701a2356ec 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6e73c226d5591861cd9280a042bbfc16 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f7829b5be828f8e8da1442653986f84f 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30ae9550ad8b82d4b84ee39aeeee2e76 2500w" />

Your change will be made as a diff, so you can review the suggested updates before modifying your code. Use the following shortcuts or click the options in the UI to accept or reject the changes.

<Tabs>
  <Tab title="MacOS">
    | Action            | Shortcut                       |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Cmd I" />  |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Shortcut                       |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Ctrl I" /> |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |
  </Tab>
</Tabs>
