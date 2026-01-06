# Tilt Documentation
# Source: https://docs.tilt.dev/upgrade.html
# Path: upgrade.html

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

#  Upgrade

You can find a list of Tilt releases on [Tiltâs GitHub Releases
page](https://github.com/tilt-dev/tilt/releases).

Usually it is sufficient to rerun the install script. However, if you
installed Tilt using one of the [alternative installation
methods](install.html) you may need to use one of the [other upgrade
methods](upgrade.html#other-upgrade-methods) listed below.

## macOS or Linux

Rerun the install script:

    
    
    curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
    

## Windows

    
    
    iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.ps1'))
    

## Other Upgrade Methods

## Homebrew (macOS or Linux)

    
    
    brew update && brew upgrade tilt-dev/tap/tilt
    

## Scoop

    
    
    scoop update tilt
    

## Conda

    
    
    conda update -c conda-forge tilt
    

## asdf

    
    
    asdf plugin add tilt
    asdf install tilt 0.36.0
    asdf global tilt 0.36.0
    

## Manual Install

If you installed Tilt manually by downloading a release binary and moving in
to your PATH you may need to do the same to upgrade.

On macOS:

    
    
    curl -fsSL https://github.com/tilt-dev/tilt/releases/download/v0.36.0/tilt.0.36.0.mac.x86_64.tar.gz | tar -xzv tilt && \
      sudo mv tilt /usr/local/bin/tilt
    

On Linux:

    
    
    curl -fsSL https://github.com/tilt-dev/tilt/releases/download/v0.36.0/tilt.0.36.0.linux.x86_64.tar.gz | tar -xzv tilt && \
      sudo mv tilt /usr/local/bin/tilt
    

On Windows:

    
    
    Invoke-WebRequest "https://github.com/tilt-dev/tilt/releases/download/v0.36.0/tilt.0.36.0.windows.x86_64.zip" -OutFile "tilt.zip"
    Expand-Archive "tilt.zip" -DestinationPath "tilt"
    Move-Item -Force -Path "tilt\tilt.exe" -Destination "$home\bin\tilt.exe"
    

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/upgrade.md)







### Was this doc helpful?

Yes No

