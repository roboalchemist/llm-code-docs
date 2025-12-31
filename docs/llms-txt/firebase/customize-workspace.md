# Source: https://firebase.google.com/docs/studio/customize-workspace.md.txt

Firebase Studiolets you to tailor your workspace to your project's unique needs by defining a single`.idx/dev.nix`configuration file that describes:

- The**system tools**that you need to be able to run (for example, from the Terminal), such as compilers or other binaries.
- The**extensions**you need installed (for example, programming language support).
- How your**[app previews](https://firebase.google.com/docs/studio/preview-apps)**should show up (for example, the commands to run your web server).
- Global**environment variables**available to local servers running in your workspace.

See the[`dev.nix`reference](https://firebase.google.com/docs/studio/devnix-reference)for a complete description of what's available.

## Nix andFirebase Studio

Firebase Studiouses[Nix](https://nixos.org/manual/nix/stable/introduction)to define the environment configuration for each workspace. Specifically,Firebase Studiouses:

- The[Nix programming language](https://nix.dev/tutorials/nix-language)to describe workspace environments. Nix is a functional programming language. The attributes and package libraries you can define in the`dev.nix`file follow the[Nix attribute set syntax](https://nix.dev/tutorials/first-steps/nix-language#attribute-set).

- The[Nix package manager](https://search.nixos.org/packages)to manage the system tools available to your workspace. This is similar to OS-specific package managers such as APT (`apt`and`apt-get`), Homebrew (`brew`), and`dpkg`.

Because Nix environments are reproducible and declarative, in the context ofFirebase Studio, this means you can share your Nix configuration file as part of your Git repository to ensure everyone who works on your project has the same environment configuration.

## A basic example

The following example shows a basic environment configuration enabling previews:  

    { pkgs, ... }: {

      # Which nixpkgs channel to use.
      channel = "stable-23.11"; # or "unstable"

      # Use https://search.nixos.org/packages to find packages
      packages = [
        pkgs.nodejs_20
      ];

      # Sets environment variables in the workspace
      env = {
        SOME_ENV_VAR = "hello";
      };

      # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
      idx.extensions = [
        "angular.ng-template"
      ];

      # Enable previews and customize configuration
      idx.previews = {
        enable = true;
        previews = {
          web = {
            command = [
              "npm"
              "run"
              "start"
              "--"
              "--port"
              "$PORT"
              "--host"
              "0.0.0.0"
              "--disable-host-check"
            ];
            manager = "web";
            # Optionally, specify a directory that contains your web app
            # cwd = "app/client";
          };
        };
      };
    }

## Add system tools

To add system tools to your workspace, such as compilers or CLI programs for cloud services,[find the unique package ID in the Nix package registry](https://search.nixos.org/packages)and add it to your`dev.nix`file's`packages`object, prefixed with \`pkgs.:  

    { pkgs, ... }: {
      # Which nixpkgs channel to use.
      channel = "stable-23.11"; # or "unstable"

      # Use https://search.nixos.org/packages to find packages
      packages = [
        pkgs.nodejs_20
      ];
      ...
    }

This is different from how you might typically install system packages using OS-specific package managers such as APT (`apt`and`apt-get`), Homebrew (`brew`), and`dpkg`. Declaratively describing exactly which system packages are needed meansFirebase Studioworkspaces are easier to share and reproduce.
| **Note:** The`channel`key specifies which Nix package registry channel to use. You can use the`unstable`channel to use the latest versions of packages, but as the name of the channel implies, doing so can prevent your environment from building, depending on when you start your workspace.

### Use local node binaries

Just like on your local machine, binaries related to locally installed node packages (for example, packages defined in your`package.json`) can be executed in a Terminal panel by invoking them with the[`npx`command](https://docs.npmjs.com/cli/v7/commands/npx).

As an additional convenience, if you're in a directory with a`node_modules`folder (such as the root directory of a web project), locally installed binaries can be invoked directly, without the`npx`prefix.

### Add`gcloud`components

A default configuration of the[`gcloud`CLI forGoogle Cloud](https://cloud.google.com/sdk/gcloud)is available to allFirebase Studioworkspaces.

If you need additional components, you can add them to your`dev.nix`file:  

    { pkgs }: {
      packages = [
        ...
        (pkgs.google-cloud-sdk.withExtraComponents [
          pkgs.google-cloud-sdk.components.cloud-datastore-emulator
        ])
        ...
      ];
    }

## Add IDE extensions

You can install extensions inFirebase Studiousing the[OpenVSX](https://open-vsx.org/)extension registry in two ways:

- **Use the*Extensions* panel inFirebase Studioto discover and install extensions.** This approach is best for**user-specific extensions**, such as:

  - Custom color themes
  - Editor emulation, like VSCodeVim
- **Add extensions to your`dev.nix`file** . These extensions will be automatically installed when you share your workspace configuration. This approach is best for**project-specific extensions**, such as:

  - Programming language extensions, including language-specific debuggers
  - Official extensions for cloud services used in your project
  - Code formatters

For the latter approach, you can include IDE extensions in your`dev.nix`file by finding the fully-qualified extension ID (of the form`<publisher>.<id>`) and adding it to the`idx.extensions`object like so:  

    { pkgs, ... }: {
      ...
      # Search for the extensions you want on https://open-vsx.org/ and use the format
      # "<publisher>.<id>"
      idx.extensions = [
        "angular.ng-template"
      ];
      ...
    }

## Add common services

Firebase Studioalso offers simplified setup and configuration for common services you may need during development, including:

- Containers
  - Docker (`services.docker.*`)
- Messaging
  - Pub/Sub Emulator (`services.pubsub.*`)
- Databases
  - MySQL (`services.mysql.*`)
  - Postgres (`services.postgres.*`)
  - Redis (`services.redis.*`)
  - Spanner (`services.spanner.*`)

For details on enabling these services in your workspace, see the`services.*`portions of the[`dev.nix`reference](https://firebase.google.com/docs/studio/devnix-reference).

## Customize previews

For details on how to customize your app previews, see[Preview your app](https://firebase.google.com/docs/studio/preview-apps).

## Set your workspace icon

You can choose a custom icon for your workspace by placing a PNG file named`icon.png`inside the`.idx`directory at the same level as your`dev.nix`file.Firebase Studiowill then use this icon to represent your workspace in your dashboard.

Because this file can be checked into source control (such as Git), this is a good way to help everyone who works on your project see the same icon for your project when usingFirebase Studio. And because the file can vary across Git branches, you can use this icon to visually distinguish between beta and production app workspaces and for other purposes.

## Turn your customizations into a template

To turn your environment configuration into a "starter environment" that anyone can use to build new projects, see the docs for[Create custom templates](https://firebase.google.com/docs/studio/custom-templates).

## Explore all customization options

Check out the[`dev.nix`reference](https://firebase.google.com/docs/studio/devnix-reference)for a detailed description of the environment configuration schema.

## Download your files

To download your files as a zip file:

- Right-click on any directory in the Explorer pane and select**Zip and Download**.

To download everything in your project directory:

1. Select**File \> Open Folder**.

2. Accept the default`/home/user`directory.

3. After the files load, right-click your working directory and select**Zip and Download** . If using theApp Prototyping agent, your working directory will be`studio`. If using a template or uploaded project, this will be your project name.

4. When prompted to rebuild the environment, click**Cancel**.

5. After your download completes, re-open your working directory from the**File**menu to move back into your workspace.

| **Tip:** You can also[export to GitHub](https://firebase.google.com/docs/studio/github).

## Next steps

- [Integrate with Firebase and Google services](https://firebase.google.com/docs/studio/google-integrations).
- [Create custom templates](https://firebase.google.com/docs/studio/custom-templates).
- [Add an Open inFirebase Studiobutton](https://firebase.google.com/docs/studio/open-in-firebase-studio).
- [Learn more aboutFirebase Studioworkspaces](https://firebase.google.com/docs/studio/get-started-workspace).