# Source: https://mintlify.com/docs/editor.md

# Visual editor

> Create, maintain, and publish documentation in your browser.

<img className="block dark:hidden my-0 pointer-events-none" src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0579093c2743bb8f55c4f81bece9e902" alt="Mintlify visual editor interface in light mode" data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/editor/editor-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f3b25fa346d59d9dcc2dd3063a1d10c6 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5045f2f0b031a0cb002730fdfb8f61a7 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4dbbc38d9e1bafad2c4f97eebb88bfe3 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=da0aa51386d8b8bf165971da4ed9858a 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f3c0dbdc22a3e9db5b945070ab6f2ff0 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=689f4a120db989fa4b50fa3ae21ef504 2500w" />

<img className="hidden dark:block my-0 pointer-events-none" src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=09938d1ca65739f048de43183a5bbaab" alt="Mintlify visual editor interface in dark mode" data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/editor/editor-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0b80b411a438896b0f5665fa0444c43b 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8bf16a72a4dcf78341da9040e0bcf459 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e073207886bff80ae09c2746cd860839 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=32bb289ccc5b5e6c78dd556b362db9fd 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=32899abbcd447d8f596dc52304218b0d 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/editor-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=83bab23334958d0a7cec5ffc42924403 2500w" />

Access the visual editor from your [dashboard](https://dashboard.mintlify.com/editor) to manage your documentation directly in your browser.

* **WYSIWYG editing**: Make changes to your documentation using a what-you-see-is-what-you-get (WYSIWYG) editor that shows how your content will look when published.
* **Git synchronization**: All changes automatically sync with your Git repository to maintain version control.
* **Team collaboration**: Multiple people can work on documentation simultaneously.
* **Component integration**: Add callouts, code blocks, and other components with slash commands.
* **No setup required**: Start writing immediately from your dashboard.

## Overview

Here is how you'll typically work in the visual editor:

<Steps>
  <Step title="Choose your branch">
    Create a branch or make changes directly to your deployment branch. We recommend creating a branch so that you can preview your changes before they go live.
  </Step>

  <Step title="Open your file">
    Navigate to an existing file in the sidebar or create a new one using the file explorer.
  </Step>

  <Step title="Edit your content">
    Make changes in the visual editor. Press <kbd>/</kbd>

    to open the component menu.
  </Step>

  <Step title="Preview your changes">
    Visual mode shows you how your changes will appear on your live site. Use this to verify everything looks correct.
  </Step>

  <Step title="Publish your changes">
    If you're working on your deployment branch, publish your changes directly from the visual editor. On other branches, you'll create a pull request for review before publishing.
  </Step>
</Steps>

## Editor modes

The visual editor has two modes to accommodate different editing preferences and needs: visual mode and Markdown mode.

Use the mode toggle in the editor toolbar to switch modes.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0b2baae4cb19ddb0030bbe3173b25753" alt="Mode toggle icons highlighted in the visual editor." className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1216" height="1216" data-path="images/editor/mode-toggle-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c3776cfb0957215158305eeda14abced 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=88af63fec3ce59972ae09d9a57aeea77 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=075689fbb8dfc4aaf2f093224a7f9f44 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=07485ad854ca781356d6f31913ad3f44 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d5b9183c165c97720d590ea42e418927 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2fb3d17a8b9752c0d7d007acc771d344 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7d86e8e068c61b35f14dcc7db72a1bca" alt="Mode toggle icons highlighted in the visual editor." className="hidden dark:block" data-og-width="3016" width="3016" data-og-height="1212" height="1212" data-path="images/editor/mode-toggle-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5906136f79c3ece33a65ee0e5e2ca79d 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f83bfefb96b5d5c94ce0fa08124fe07b 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0f0dcf44cffff9ae039993ac585ee11b 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4a4d71afb167ff754c160357eb02c7e2 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=937f4cca413c6a398f9d1ca9ee2d6ddc 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/mode-toggle-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e2344f77493cfb53d53b35ef5dfe2adf 2500w" />
</Frame>

### Visual mode

Visual mode provides a WYSIWYG experience where changes that you make in the editor reflect how your published documentation will look. This mode is ideal for when you want to see how your changes will look in real-time.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=118fddb77421ce262613c9c61506af7a" alt="Visual editing mode in the Mintlify visual editor" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1232" height="1232" data-path="images/editor/visual-mode-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=89c3a7bc7b250c18748ba74c94ff6476 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0368ea7d223d4518218c235265e27cbe 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9d0369ad3731ade39d88e4ac0fbc1e23 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f14aaac5f6abe5dd21959c7c70f56196 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=33295ee805b96384cfa71ec87a17d4d9 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cf0f208baf77599a1d104404d053897c 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b7709d87928dd232317efd531011e03e" alt="Visual editing mode in the Mintlify visual editor" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1226" height="1226" data-path="images/editor/visual-mode-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=33d48d9b36523ead4822914e743e88d7 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e37cf0785534e4c78e1ce2be413bb682 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=45a844fcf31b9dce990aa4c81aafc8cd 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=82223c17e2d40019d1dde8ed55e0e96b 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ead211848b9e8c74c5a48ed1fb111141 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/visual-mode-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2b5fe5bca66ed906a6328c0c6889eb0c 2500w" />
</Frame>

### Markdown mode

Markdown mode provides direct access to the underlying `MDX` code of your documentation. This mode is ideal for when you need precise control over component properties or when you prefer to write in Markdown syntax.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2319a3a212b7e8a52eaab74becd2db63" alt="Markdown mode in the Mintlify visual editor" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1248" height="1248" data-path="images/editor/markdown-mode-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=081733ec46a3ede1e7486935ec75e313 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=fca6d74ee8f76f25e5f4a8558b2cd0a8 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2e5b24125582d12cb508a519c735d28d 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=43000b6581621009fa5339a3d03abd2d 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=454e4503b3d2f6af5206fa6389969e5a 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d87a3bad391cb9aecaec9c27fd5ef6ed 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=db078fb4d23ec8a63c04ea12cc3cd3ad" alt="Markdown mode in the Mintlify visual editor" className="hidden dark:block" data-og-width="3016" width="3016" data-og-height="1246" height="1246" data-path="images/editor/markdown-mode-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7ae49009300bd72a77f13c6bd82f6ed3 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=994ec0278ad64215e95b149a46adeaf1 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9297dd33c57d2ca3f6f3c1f328cbacd2 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5ac2c199beb6b7b107a7acd603e00221 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a59e338ac9639aab399f70f9a8e2c37c 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/markdown-mode-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=df608050360a857b9aca2a7552f4e19c 2500w" />
</Frame>

## Manage content

### Navigate your files

Use the sidebar file explorer to browse your documentation files. Click on any file to open it in the editor.

Press <kbd>Command</kbd>

* <kbd>P</kbd>

on macOS or <kbd>Ctrl</kbd>

* <kbd>P</kbd>

on Windows to search for files by name.

### Create new pages

Select the **Create a new file** icon in the file explorer sidebar.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6cfacb198f66f3fedee52a0c36143499" className="block dark:hidden rounded-2xl border border-gray-100 shadow-lg" style={{ width:"400px",height:"auto" }} alt="Files menu in the visual editor" data-og-width="688" width="688" data-og-height="130" height="130" data-path="images/editor/files-menu-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=049392718e14681cf19548aa2883d679 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=42487b7bcfb8cef9b5e3215a34ddb688 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a879772eac1013b1d63fe058b3386747 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7731feaf064ba24dacf33c5209e7d83e 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=23f51c70cde1740d8ae106bea9e6f3de 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c010f204f31c665569ca48908dd23da8 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=21a91ff1652683b82ce99734e7fa417a" className="hidden dark:block rounded-2xl border border-white/10 shadow-lg" style={{ width:"400px",height:"auto" }} alt="Files menu in the visual editor in dark mode" data-og-width="690" width="690" data-og-height="132" height="132" data-path="images/editor/files-menu-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=323a509c3bf4b7e769348de07b103a06 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=340e72ed1df893f31892d7cbd90314c6 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f852d5e911ee4a6866e492204af9f235 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=759f1aa46c113f0b4eb620755af59c24 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=162ebe89c018f383f707f5ab2e149084 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/files-menu-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=fd76814779ae3255987d08c949ff5788 2500w" />
</Frame>

Filenames are automatically appended with a `.mdx` extension. To change the file type, click the file extension. Select the file type you want from the dropdown menu.

<Frame>
  <img src="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=6041d78c79d2d9ca3026c8f8a9d98942" className="block dark:hidden" style={{ width:"auto",height:"400px" }} alt="File extension menu in the visual editor." data-og-width="590" width="590" data-og-height="562" height="562" data-path="images/editor/file-type-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=280&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=14f627afc4bb51d187005f57b66deacf 280w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=560&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=194d455b1ce2346a2055ecad6037de02 560w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=840&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=da53a330a5cde65378533cbd72264c60 840w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=1100&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=13d74e9b07aa8cd20922f15dbef2009e 1100w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=1650&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=1b6c26affe14c1701ee09e074156f815 1650w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-light.png?w=2500&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=a6e8f09db76261111dd8a6fab476fdcc 2500w" />

  <img src="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=812eb275251e3e21402fd8a8a2520f26" className="hidden dark:block" style={{ width:"auto",height:"400px" }} alt="File extension menu in the visual editor in dark mode." data-og-width="590" width="590" data-og-height="554" height="554" data-path="images/editor/file-type-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=280&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=0e64a05f1b182b3790ef8c01c2919eec 280w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=560&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=5a57a43f515b4ef88de4bf9d52dff37a 560w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=840&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=f78f4fcaf98dc34bb8c817b4c87b9a5d 840w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=1100&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=ae515e56d37fed2defead57fabebb137 1100w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=1650&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=660d5968c1e452c90927fe52aa9a1540 1650w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/file-type-dark.png?w=2500&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=02b0b14b47a287661722d8f8e4807ac0 2500w" />
</Frame>

### Rename pages

To rename a page, click the kebab menu icon for the file you want to rename. Select **Rename** from the dropdown menu.

<Frame>
  <img src="https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=cfd270cde9f3aae7ca76ca106a26f123" className="block dark:hidden" alt="Rename page in the visual editor." data-og-width="968" width="968" data-og-height="366" height="366" data-path="images/editor/rename-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=280&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=cb0ab107d8a7ac434f158944b4d47d02 280w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=560&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=a237097ee0ef78101eb4630f723213ac 560w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=840&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=500144b634f4ba83c7c1cf3e3ccd0e80 840w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=1100&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=95ceeb2944476e85d0b12f6c0aa037eb 1100w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=1650&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=e61713d718e691d75cf83c264d210fd8 1650w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-light.png?w=2500&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=b60d17ebcea714b26b92297ee1359fa5 2500w" />

  <img src="https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=9536d5fa8b21899aff346b038a0a3afd" className="hidden dark:block" alt="Rename page in the visual editor in dark mode." data-og-width="968" width="968" data-og-height="366" height="366" data-path="images/editor/rename-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=280&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=75db9f8a470839908f7c27eed31c1761 280w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=560&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=188a772b3f15c6c25794ffd70b54c81b 560w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=840&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=b11ac0e0ddf85d52fb7080681463b93b 840w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=1100&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=723b18578fb201abda82a5523e8ce0a5 1100w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=1650&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=f974377b815d1040a3fe4b0556c24a7f 1650w, https://mintcdn.com/mintlify/KhZk9ZNhcQruz0r5/images/editor/rename-dark.png?w=2500&fit=max&auto=format&n=KhZk9ZNhcQruz0r5&q=85&s=d56144b843f37acb24858d8e5e94a662 2500w" />
</Frame>

### Delete pages

To delete a page, click the kebab menu icon for the file you want to delete. Select **Delete** from the dropdown menu.

<Frame>
  <img src="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=4f8f74b6c1cebae0801debbb9000a347" className="block dark:hidden" alt="Delete page in the visual editor." data-og-width="968" width="968" data-og-height="366" height="366" data-path="images/editor/delete-page-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=280&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=f815bf5626dc627eb4beff5cf6c94f21 280w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=560&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=c3b50abe40ed089af1c39db46b630009 560w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=840&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=b4eaa3c4d950aa3c8e8580336b443ab9 840w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=1100&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=1bc91872ea9e7b00eb373be72d2a760a 1100w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=1650&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=19c2a42a9bc7f7280cf3b0d82bd4c802 1650w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-light.png?w=2500&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=65940d011f2f589c4fcf81105dc07ebc 2500w" />

  <img src="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=f9cac83057727574fa05bd51656d8f22" className="hidden dark:block" alt="Delete page in the visual editor in dark mode." data-og-width="968" width="968" data-og-height="366" height="366" data-path="images/editor/delete-page-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=280&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=62dd7cca509575211525be28fa06b389 280w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=560&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=84d7d4c1fb2256bb8d4f56d569c41f1a 560w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=840&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=95eb9a55afc3a41299870f482046f692 840w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=1100&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=133e8b60b7390f0270ce8e2c5000b9af 1100w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=1650&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=b66961d37934580b315bae11892d13eb 1650w, https://mintcdn.com/mintlify/cqGxx4WboVGarcmi/images/editor/delete-page-dark.png?w=2500&fit=max&auto=format&n=cqGxx4WboVGarcmi&q=85&s=d97c3ed2ef190527592dbb5e6a969b6b 2500w" />
</Frame>

### Organize your navigation

Edit your `docs.json` file to add new pages and remove deleted pages from your site navigation. See [Navigation](/organize/navigation) for more information on how to organize pages.

**Example: Add a Themes page to the Profile group**

In this example, you created a new page titled Themes and you want to add it to the Profile group in your documentation. Add the path to the new page to the `pages` array of the `Profile` group in your `docs.json` file for it to appear in your site navigation.

```json Adding a Themes page to the Profile group {18} theme={null}
{
    "navigation": {
        "groups": [
            {
                "group": "Getting started",
                "pages": [
                    "index",
                    "quickstart",
                    "installation"
                ]
            },
            {
                "group": "Profile",
                "pages": [
                    "settings",
                    "account-types",
                    "dashboard",
                    "themes"
                ]
            }
        ]
    }
}
```

### Edit content

Make changes to your pages using visual mode or Markdown mode in the editor.

In visual mode, press <kbd>/</kbd>

to open the component menu. Add content blocks, callouts, code blocks, and other components to customize your documentation.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=09e298fca75a938c7b265a909265df74" alt="The unfurled component menu emphasized in the Mintlify visual editor" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1592" height="1592" data-path="images/editor/component-menu-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=eaa187e0cf104c9e05d4a3c901298d48 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=eb4c28ebe1e5fa61bfae03f83069762d 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b23b038a2b3ee6be7eb46decfe602686 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8bec996b9a0ebdb0736a410d2c33040d 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=13aae7f7611b51c2691e30660727b75e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ad3ea6cea1cbd115387515351489fd6a 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cb9940f2020875674ad5c0ed1596fb5a" alt="The unfurled component menu emphasized in the Mintlify visual editor" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1592" height="1592" data-path="images/editor/component-menu-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=75049d30a9d07b01d0abeffe99a8f81a 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=34b541e6d7905f184b05de245c4a14cf 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=06015806c6153137ccb0811a0ec7be24 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5deec9ddf80bacd5239d54cce6b173ee 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=13374677e235922030beaca045ec6079 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/component-menu-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e4dbb1f9f7d98b76aafbb8097db39f0b 2500w" />
</Frame>

In Markdown mode, you directly edit the `MDX` of your pages. This can be helpful when you need to:

* Set specific component properties
* Work with complex nested components
* Copy and paste `MDX` content from other sources

See [Format text](/create/text) and [Format code](/create/code) for more information on how to write using Markdown syntax.

## Publish your changes

The branch that you work on determines how the editor publishes your changes:

* **Deployment branch**: Publishing updates your live site immediately.
* **Other branches**: Publishing creates a pull request so you can review changes before deploying them to production.

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4e114c9f1a37819bd39e034b61348a56" alt="The publish button emphasized in the Mintlify visual editor" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1046" height="1046" data-path="images/editor/publish-flow-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4b28eec8285f0f8f8dda0e65e243b7d3 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4d1d8ba7100c6d7ecdc4de581bf8c684 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2be6f94b393683dc372c091dafc538e6 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3cec1bedf78ddc1fa42692c925a68cf8 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=71cd177427b341feefdd867db7ed1124 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0ca838ed471726b177c58eb3c6e58fc8 2500w" />

  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=59cb87df534527a16948eec1a8de73af" alt="The publish button emphasized in the Mintlify visual editor" className="hidden dark:block" data-og-width="3020" width="3020" data-og-height="1044" height="1044" data-path="images/editor/publish-flow-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c5663388541ff8416c6b287bd6946dde 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=950f79827014cbd4f4b2d5169c5d8042 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cc179700430fbb2322edcbdca52e54c2 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ef1ebf512640b8963e93dcf04bea4988 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=62fa4d37792cb4abc97d585b82fd9c2f 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/publish-flow-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3e2c44c901d48203f425e66427110a4f 2500w" />
</Frame>

If you authorize Mintlify to your GitHub user, your commits will be signed as if you had made them yourself. If not, they will be signed by the Mintlify GitHub app.

### Pull requests and reviewing changes

Pull requests let you propose changes from your branch so that other people can review them before merging into your live documentation. This helps ensure that your changes are correct and gives your team a chance to collaborate on content.

<Tip>
  Even if you're working solo, pull requests are valuable for previewing changes and maintaining a clear history of updates.
</Tip>

#### Create a pull request

<Steps>
  <Step title="Save your work">
    Select **Save Changes** to save all changes on your branch.
  </Step>

  <Step title="Create the pull request">
    Select **Publish Pull Request** from the editor toolbar.
  </Step>

  <Step title="Add a title and description">
    Write a clear title and description explaining:

    * What changes you made
    * Why you made them
    * Any specific areas that need review
  </Step>

  <Step title="Create and share">
    Select **Publish Pull Request**. The editor will provide a link to view your pull request.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=40827b354fc1f1d9015b9dde545816f4" alt="Publish pull request button emphasized in the Mintlify visual editor" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1146" height="1146" data-path="images/editor/pull-request-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cb6db61b0dba2f34f3bcaa8c04321058 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7a5877b932fee30fa0fff232d3da9cc2 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1da2bcb092f27d5042a8f87d403cfdc8 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9e0d2a412066142e2d04135d0c1de596 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=820615a76df3fe20af849836c385c8d4 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1a45b1fc0fca7f19dbf08519166feab9 2500w" />

      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=92c87e2d5cc485ae5f8fc9b4da25cdd8" alt="Publish pull request button emphasized in the Mintlify visual editor" className="hidden dark:block" data-og-width="3020" width="3020" data-og-height="1144" height="1144" data-path="images/editor/pull-request-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3164d6ef21df46052956c5024470c659 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c68609579fdfb391631936f19ac1848b 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ad533a8f04c9cd073b82ed54ad0af718 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f3b3191c4a20a04e15693584297d359a 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=073c3cecdf3d5f81444c7aff78908239 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/editor/pull-request-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=97cb6badb29df6517e890c7d3f96e3d7 2500w" />
    </Frame>
  </Step>
</Steps>

#### Review pull requests

Once your pull request is created:

1. **Review changes**: You and your team members can review your pull request in your Git provider like GitHub or GitLab.
2. **Leave feedback**: Add comments or request changes.
3. **Make additional changes**: Make additional changes in the visual editor. When you save changes, the editor pushes them to your pull request.
4. **Approve**: Approve the pull request when you're satisfied with the changes.
5. **Merge**: Merge the pull request when you're ready to deploy your changes to production.

## Keyboard shortcuts

The visual editor supports all common keyboard shortcuts such as copy, paste, undo, and select all, and the following shortcuts:

| Command                          | macOS                                                | Windows                                                  |
| :------------------------------- | :--------------------------------------------------- | :------------------------------------------------------- |
| **Search files**                 | <kbd>Cmd</kbd>   + <kbd>P</kbd>                      | <kbd>Control</kbd>   + <kbd>P</kbd>                      |
| **Add link to highlighted text** | <kbd>Cmd</kbd>   + <kbd>K</kbd>                      | <kbd>Control</kbd>   + <kbd>K</kbd>                      |
| **Add line break**               | <kbd>Cmd</kbd>   + <kbd>Enter</kbd>                  | <kbd>Control</kbd>   + <kbd>Enter</kbd>                  |
| **Bold**                         | <kbd>Cmd</kbd>   + <kbd>B</kbd>                      | <kbd>Control</kbd>   + <kbd>B</kbd>                      |
| **Italic**                       | <kbd>Cmd</kbd>   + <kbd>I</kbd>                      | <kbd>Control</kbd>   + <kbd>I</kbd>                      |
| **Underline**                    | <kbd>Cmd</kbd>   + <kbd>U</kbd>                      | <kbd>Control</kbd>   + <kbd>U</kbd>                      |
| **Strikethrough**                | <kbd>Cmd</kbd>   + <kbd>Shift</kbd>   + <kbd>S</kbd> | <kbd>Control</kbd>   + <kbd>Shift</kbd>   + <kbd>S</kbd> |
| **Code**                         | <kbd>Cmd</kbd>   + <kbd>E</kbd>                      | <kbd>Control</kbd>   + <kbd>E</kbd>                      |
| **Normal text**                  | <kbd>Cmd</kbd>   + <kbd>Alt</kbd>   + <kbd>0</kbd>   | <kbd>Control</kbd>   + <kbd>Alt</kbd>   + <kbd>0</kbd>   |
| **Heading 1**                    | <kbd>Cmd</kbd>   + <kbd>Alt</kbd>   + <kbd>1</kbd>   | <kbd>Control</kbd>   + <kbd>Alt</kbd>   + <kbd>1</kbd>   |
| **Heading 2**                    | <kbd>Cmd</kbd>   + <kbd>Alt</kbd>   + <kbd>2</kbd>   | <kbd>Control</kbd>   + <kbd>Alt</kbd>   + <kbd>2</kbd>   |
| **Heading 3**                    | <kbd>Cmd</kbd>   + <kbd>Alt</kbd>   + <kbd>3</kbd>   | <kbd>Control</kbd>   + <kbd>Alt</kbd>   + <kbd>3</kbd>   |
| **Heading 4**                    | <kbd>Cmd</kbd>   + <kbd>Alt</kbd>   + <kbd>4</kbd>   | <kbd>Control</kbd>   + <kbd>Alt</kbd>   + <kbd>4</kbd>   |
| **Ordered list**                 | <kbd>Cmd</kbd>   + <kbd>Shift</kbd>   + <kbd>7</kbd> | <kbd>Control</kbd>   + <kbd>Shift</kbd>   + <kbd>7</kbd> |
| **Unordered list**               | <kbd>Cmd</kbd>   + <kbd>Shift</kbd>   + <kbd>8</kbd> | <kbd>Control</kbd>   + <kbd>Shift</kbd>   + <kbd>8</kbd> |
| **Blockquote**                   | <kbd>Cmd</kbd>   + <kbd>Shift</kbd>   + <kbd>B</kbd> | <kbd>Control</kbd>   + <kbd>Shift</kbd>   + <kbd>B</kbd> |
| **Subscript**                    | <kbd>Cmd</kbd>   + <kbd>,</kbd>                      | <kbd>Control</kbd>   + <kbd>,</kbd>                      |
| **Superscript**                  | <kbd>Cmd</kbd>   + <kbd>.</kbd>                      | <kbd>Control</kbd>   + <kbd>.</kbd>                      |

## Troubleshooting

Find solutions to common issues you might encounter while using the visual editor.

<AccordionGroup>
  <Accordion title="Changes not appearing after publishing">
    **Possible causes:**

    * Deployment is still in progress
    * Browser caching issues
    * Build or deployment errors

    **Solutions:**

    1. Check deployment status in your dashboard.
    2. Hard refresh your browser (<kbd>Ctrl</kbd>

       * <kbd>F5</kbd>

       or <kbd>Cmd</kbd>

       * <kbd>Shift</kbd>

       * <kbd>R</kbd>

       )
    3. Clear your browser cache.
  </Accordion>

  <Accordion title="Permission errors when publishing">
    **Possible causes:**

    * Insufficient permissions to the Git repository
    * Authentication issues with your Git provider

    **Solutions:**

    1. Verify you have correct access to the repository.
    2. Check if your Git integration is properly configured.
    3. Review the [Editor Permissions](/dashboard/permissions) documentation.
  </Accordion>

  <Accordion title="Editor loading issues">
    **Possible causes:**

    * Network connectivity problems
    * Large documentation repositories

    **Solutions:**

    1. Check your internet connection.
    2. Refresh the page.
    3. Contact support if the issue persists.
  </Accordion>

  <Accordion title="Files not loading or showing errors">
    **Possible causes:**

    * Invalid MDX syntax in files
    * Missing or corrupted files
    * Large file sizes causing timeouts

    **Solutions:**

    1. Check the file syntax for MDX formatting errors
    2. Verify the file exists in your repository.
  </Accordion>
</AccordionGroup>

## Next steps

* Learn fundamental [Git concepts](/guides/git-concepts)
* Learn best practices for collaborating with [branches](/guides/branches)
