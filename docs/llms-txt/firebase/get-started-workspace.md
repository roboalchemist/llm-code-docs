# Source: https://firebase.google.com/docs/studio/get-started-workspace.md.txt

Firebase Studioprovides a collaborative, cloud-based development environment that simplifies the process of building applications with an extensive combination of[frameworks and libraries](https://studio.firebase.google.com/templates).

After you set up aFirebase Studioworkspace, you can access and share a fully-functional, flexible development environment:Firebase Studioworkspaces are accessible from any device and provide integrated tools to streamline you and your team's development process.

## Create a workspace

A workspace inFirebase Studiois a development environment that contains everything you need to develop your application. It contains your code, a code editor (with plugins relevant to your project), and toolchains that support app development. It's just like creating a new project in your local desktop development environment, except you have an entire computer and operating system pre-configured and dedicated*exclusively*to building your application, running on your browser in the cloud, accessible wherever you are.

Firebase Studioworkspaces are optimized to contain a single codebase, so you can keep the environments and system-level dependencies of different applications isolated from each other. You can create multiple workspaces to use with different applications and frameworks.
| **Key Point:** There's a limit to the number of workspaces you can create. If you have a[Google Developer Profile](https://developers.google.com/profile/help/overview), you can create more workspaces. Learn more at[Firebase Studiopricing, quotas and limits](https://firebase.google.com/docs/studio/pricing).

To create a new workspace:

- [Opening a template or sample app](https://firebase.google.com/docs/studio/get-started-template).
- [Importing a project](https://firebase.google.com/docs/studio/get-started-import).
- [Prototype with AI](https://firebase.google.com/docs/studio/get-started-ai), then switch toCodeview (**`</>`**).

## Duplicate a workspace

Duplicating aFirebase Studioworkspace creates a copy of your project that contains everything within the`home/user`directory. This is useful when you want to experiment with a project without affecting the original, or when you want to use an existing project as a starting point for a new one.

To duplicate a workspace:

1. From the[Firebase Studiohomepage](https://studio.firebase.google.com/), click themore_horizmenu next to the workspace you want to copy \>**Duplicate**.
2. Enter the name of your new workspace and click**Duplicate**. The new workspace is created and added to your list of workspaces. Ã Note: Duplicating larger workspaces can take several minutes. If your new workspace doesn't load, wait 5 minutes, then refresh the page.

3. *(Optional)*If the original workspace has a linked Firebase project, consider creating a separate Firebase project for your new workspace. This prevents your new workspace from making changes to the Firebase project linked to your original workspace. To create a Firebase project:

   1. Open the new workspace and askGeminito create a Firebase project for you.
   2. Update any files that reference the Firebase project, such as`.env`or`.firebaserc`.

## Configure your workspace

Firebase Studiouses[Nix](https://nixos.org/manual/nix/stable/introduction)to define the environment configuration for each workspace. Nix is a purely functional package manager and assigns unique identifiers to each dependency, which ultimately means your environment can contain multiple versions of the same dependency, seamlessly. It is also reproducible and declarative. In the context ofFirebase Studio, this means you can share your Nix configuration file across workspaces to load the same environment configuration. Learn more about[Nix +Firebase Studio](https://firebase.google.com/docs/studio/customize-workspace#nix+fs).

### Create or edit the`.idx/dev.nix`file

Environment configuration is defined in the`.idx/dev.nix`file in your code repository. This file specifies all of the components to be added to your workspace including:

- [System tools](https://firebase.google.com/docs/studio/customize-workspace#system-tools)available from the[Nix package registry](https://search.nixos.org/packages), including compilers, packages (like`go`or`angular`), and command line utilities, like extra[gcloud CLIcomponents](https://firebase.google.com/docs/studio/customize-workspace#gcloud).

- [IDE extensions](https://firebase.google.com/docs/studio/customize-workspace#extensions)from the[OpenVSX registry](https://open-vsx.org/), like language-specific debuggers, code formatters, official extensions for cloud services, and more.

- [Common services](https://firebase.google.com/docs/studio/customize-workspace#common-services), like docker, Pub/Sub messaging, databases like Postgres and Redis, and[more](https://firebase.google.com/docs/studio/devnix-reference).

See the following example`.idx/dev.nix`file for a basic workspace environment configuration that enables app previews inFirebase Studio:  

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

### Apply new configuration

Any time you add or update the`dev.nix`configuration file,Firebase Studioshows a prompt in the bottom-right corner to**Rebuild the environment**. The time it takes to rebuild the environment depends on the number of packages your configuration needs.

### Debug environment build failures

Because configuration files are machine-readable code, they can have errors. If this happens, the environment may fail to build and not start.Firebase Studiodisplays an option to start a*Recovery* environment. This workspace doesn't include any of the configuration you've defined and just runs basicCode OSS. This gives you the chance to fix errors in your`dev.nix`configuration file and rebuild the environment.

## Next steps

- [Customize yourFirebase Studioworkspace](https://firebase.google.com/docs/studio/customize-workspace).

- [Create custom templates to use and share](https://firebase.google.com/docs/studio/custom-templates).

- [Share your workspace](https://firebase.google.com/docs/studio/share-your-workspace).

- [Use an "Open inFirebase Studio" button to share your workspace configuration or custom template](https://firebase.google.com/docs/studio/open-in-firebase-studio).