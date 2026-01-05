# Tilt Documentation
# Source: https://docs.tilt.dev/editor.html
# Path: editor.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Learn About Tilt

    

  * [ Getting Started ](/)
  * [ Is Tilt right for me? ](/product_faq.html)

First Look at Tilt

    

  * [ Overview ](/tutorial/index.html)
  * [ 1\. Preparation (optional) ](/tutorial/1-prerequisites.html)
  * [ 2\. Launching & Managing Resources ](/tutorial/2-tilt-up.html)
  * [ 3\. Tilt UI ](/tutorial/3-tilt-ui.html)
  * [ 4\. Code. Update. Repeat. ](/tutorial/4-code-update-repeat.html)
  * [ 5\. Smart Rebuilds with Live Update ](/tutorial/5-live-update.html)

Quick Links

    

  * [ Install ](/install.html)
  * [ Upgrade ](/upgrade.html)
  * [ Tiltfile Snippets ](/snippets.html)
  * [ Editor Support new ](/editor.html)

How Does Tilt Work?

    

  * [ The Control Loop ](/controlloop.html)
  * [ Choosing a Local Dev Cluster ](/choosing_clusters.html)
  * [ Local vs Remote Services ](/local_vs_remote.html)

FAQs

    

  * [ Frequently Asked Questions ](/faq.html)
  * [ Why is Tilt broken? ](/debug_faq.html)
  * [ What does Tilt send? ](/telemetry_faq.html)

#  Editor Support

Whether youâre just starting or are a seasoned Tilter, writing `Tiltfile`s
should not be tedious.  
We want to make it easy to experiment with your Tiltfile, so you can
experience the magic of Tiltâs responsiveness with minimal interruptions to
your development flow, that includes switching context to look up `Tiltfile`
documentation.

Weâre offering Tiltfile support for [VS
Code](https://code.visualstudio.com/) and select IDEs of the [JetBrains
suite](https://www.jetbrains.com/products/#type=ide).  
All code is public and open source. We appreciate contributions of all kinds.

## VS Code

The [official `Tiltfile`
extension](https://marketplace.visualstudio.com/items?itemName=tilt-
dev.Tiltfile) is available at the VS Code marketplace.  
It provides syntax highlighting, autocomplete and signature support for
`Tiltfile` functions.

![](assets/img/vscode-extension.gif)

## TextMate bundles

The [tiltfile.tmbundle](https://github.com/tilt-dev/tiltfile.tmbundle) offers
syntax highlighting for any IDEs supporting TextMate bundles, like IntelliJ
GoLand, PyCharm or WebStorm.

## Emacs

Tilt is compatible with Emacsâ `lsp-mode`.

To enable it, install `lsp-mode` and add the following to your `.emacs`:

    
    
    (require 'python-mode)
    
    (define-derived-mode tiltfile-mode
      python-mode "tiltfile"
      "Major mode for Tilt Dev."
      (setq-local case-fold-search nil))
    
    (add-to-list 'auto-mode-alist '("Tiltfile$" . tiltfile-mode))
    
    (with-eval-after-load 'lsp-mode
      (add-to-list 'lsp-language-id-configuration
        '(tiltfile-mode . "tiltfile"))
    
      (lsp-register-client
        (make-lsp-client :new-connection (lsp-stdio-connection `("tilt" "lsp" "start"))
                         :activation-fn (lsp-activate-on "tiltfile")
                         :server-id 'tilt-lsp)))
    

## Other editors

Tilt embeds its own language server based on Tree Sitter.

https://github.com/tilt-dev/starlark-lsp

To run it locally, run:

    
    
    tilt lsp start
    

Adding Tiltfile support to a new editor usually requires a few lines of config
to start the language server and connect.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/editor.md)







### Was this doc helpful?

Yes No

