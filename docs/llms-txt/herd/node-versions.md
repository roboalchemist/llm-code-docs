# Source: https://herd.laravel.com/docs/macos/technology/node-versions.md

# Manage Node.js

# Managing Node.js versions

Herd ships with [nvm](https://github.com/nvm-sh/nvm), the Node version manager which allows the management of multiple [Node.js](https://nodejs.org/) versions on your machine. By default, Herd automatically installs the latest available version of Node.js for you.

Herd requires a specific nvm version and can't use existing nvm installations. If you are migrating from a previous nvm setup, please consult the [Troubleshooting](#troubleshooting) section if it doesn't work as expected.

## Via the GUI

You may install and update the Node.js versions on your machine via the Herd GUI. Simply click on the button and Herd will take care of the rest.

<Frame>
  <img src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d71e7bda428edc2fb8d13b5456bdee95" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=934de439892b01a69a57d742a070583c 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5ff3dfb77e4b5cea71801bbc9f88370e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2468322860df5c986b1b20b3f4a79413 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4afd8042624ba43249a9e3517fe847fa 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b32675e6048a50ea5892455f7c93b15f 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6931a37540ffa876d14a5947e482090b 2500w" />
</Frame>

## Via the CLI

You can use `nvm` on your command line to install, update and switch between Node.js versions any time. To switch to a different version, simply enter `nvm use VERSION` and nvm runs all required commands to change the version and make it accessible in your terminal.
For more information about nvm, take a look at the [official nvm documentation](https://github.com/nvm-sh/nvm?tab=readme-ov-file#usage).

### Commands that you might use regularly

```bash  theme={null}
# Install node 20
nvm install 20

# Uninstall node 20
nvm uninstall 20

# Switch to node 20
nvm use 20

## Display all commands
nvm help
```

# Per-site Node versions

By default, the Node version available via CLI will be the most recent one.

However, if you need to support different Node.js versions for different sites, you may use the isolated Node functionality.
This configures Herd to use the specified Node version for the site, regardless of the global Node version.

If you use oh-my-zsh, Herd automatically detects the Node.js version to use when changing directories via your terminal.

## Via the CLI

You may use the `herd isolate-node` command to specify which Node.js version a particular folder should use. The `isolate-node` command configures
Herd/nvm to use the specified Node.js version for the site located in your current working directory:

```bash  theme={null}
cd ~/Herd/example-site
 
herd isolate-node 21
```

If your site name does not match the name of the directory that contains it, you may specify the site name using the `--site` option:

```bash  theme={null}
herd isolate-node 21 --site="site-name"
```

You can be as specific as you want, when isolating Node.js versions:

```bash  theme={null}
herd isolate-node 16.13.2
```

You may execute the `isolated-node` command to display a list of all of your isolated sites and their Node.js versions:

```bash  theme={null}
herd isolated-node
```

To revert a site back to the globally installed Node.js version, you may invoke the `unisolate-node` command from the site's root directory:

```bash  theme={null}
herd unisolate-node
```

## Updating Node.js

If you open the Node settings, Herd checks if there are new versions available and displays an update button next to every version that you can update.

<Frame>
  <img alt="Update Node.js in the Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8a0556b87455cdfa4cdfb144a6626629" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_node_update.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5373cd10b35562bb98ef85fb29cac63b 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=76f7dfc022a33eddb76d3038a0cbdca0 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8ad859b62d8bdf39262585ec18051883 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6e42efd9b53dd1518457e7f041737244 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a6683618126b60df2fdac9ff9e971466 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9f1f9414f5dbf74018f1a52ad9c82344 2500w" />
</Frame>

Herd uses nvm under the hood and this means that existing versions are kept when pressing the update button. The update downloads and installs the latest version and makes this one the preferred version for the related major version.

## Uninstalling Node

If you want to uninstall a specific version, either consult the [official nvm documentation](https://github.com/nvm-sh/nvm) or run the uninstall command from your terminal.

```
nvm uninstall VERSION
```

You can verify which versions you have with the command `nvm list`. So if you want to uninstall node 18.20.4, run `nvm uninstall 18.20.4`.

## Troubleshooting

Herd parses command output to determine your current Node.js version. If it can't parse the output because there is output that it doesn't understand, or you are using an unsupported shell, it displays `Unknown` for your node version in the sites list. Herd is an opinionated development environment that relies on bash or zsh, so other shells can lead to errors.

There are situations where Herd can not install nvm and keeps displaying the install button for nvm in the settings. This can happen if there are traces of a previous install on your system – this could be a broken node symlink or nvm paths in your `.zshrc` file.
