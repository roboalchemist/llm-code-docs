# Source: https://docs.knock.app/cli/message-type/file-structure.md

# Source: https://docs.knock.app/cli/guide/file-structure.md

# Source: https://docs.knock.app/cli/partial/file-structure.md

# Source: https://docs.knock.app/cli/translation/file-structure.md

# Source: https://docs.knock.app/cli/email-layout/file-structure.md

# Source: https://docs.knock.app/cli/workflow/file-structure.md

# File structure

When workflows are pulled from Knock, they are stored in directories named by their workflow key. In addition to a `workflow.json` file that describes all of a given workflow's steps, each workflow directory also contains individual folders for each of the [channel steps](/designing-workflows/channel-step) in the workflow that hold additional content and formatting data.

{`workflows/
└── my-workflow/
    ├── email_1/
    │   ├── visual_blocks/
    │   │   └── 1.content.md
    │   └── visual_blocks.json
    ├── in_app_feed_1/
    │   └── markdown_body.md
    └── workflow.json`}

If you're migrating your local workflow files into Knock, you can arrange them using the example file structure above and then push them into Knock with a single command using [`knock workflow push --all`](/cli/workflow/push). Each `workflow.json` file should follow the structure defined [here](/mapi-reference/workflows/schemas/workflow).
