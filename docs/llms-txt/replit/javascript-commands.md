# Source: https://docs.replit.com/extensions/examples/javascript-commands.md

# JavaScript Commands

> Learn how to build an extension that adds JavaScript-related commands to Replit for managing npm packages and running scripts.

This tutorial assumes that you have basic web development knowledge, some familiarity with Replit, and familiarity with the Command system.

In a gist, we will fork an extension template, add a background script, and in that background script, write code that adds Commands to to the Replit workspace. Our command can be thought of as a simple tree. There's a root command called "JavaScript tools". It returns three subcommands:

* "Install": This command lets you search the npm registry for packages to install, based on what you've typed. Selecting a package opens a new shell and invokes `npm install <package name>`

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b15182c8c4797798d583e3de19f94a62" alt="" data-og-width="1640" width="1640" data-og-height="1842" height="1842" data-path="images/extensions/examples/js-commands/js-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4f5e96deb5fb29986b4dc1b5e60a53a0 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ba6fa63fc4072bed3595437b3adee2fc 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9055f25cc97aab7dcdf5da46c549809b 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8d7f635a1c6504d746ae2005d326cd3b 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d480bb2f6d3348e8d63f74424454ba8e 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-install.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9f506f7a600fafedc5fae74fda99122b 2500w" />
</Frame>

* "Scripts": This command displays scripts in your package.json file. Selecting the script opens a new shell and invokes that command.

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6ebe5dc32d2519018b986f1191e7f26f" alt="" data-og-width="1686" width="1686" data-og-height="1700" height="1700" data-path="images/extensions/examples/js-commands/js-scripts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ddb7058246d7a75a9ed23a290499de63 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c0d1d4842b467d6810c4305dac0ea010 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6ac306b6c2eb14575a52931d267e4f3d 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6f4a6b34c3180dc57d8134e3ba4ed87e 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c5a059a7d49582c642cb4e1039a626f7 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-scripts.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=05e469e43e7af8ed6f6a11b93ce7f93e 2500w" />
</Frame>

* "Uninstall": This returns all your installed packages. Selecting a package uninstalls it

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=1fc96e338e4da5be3b7332e5d97ef979" alt="" data-og-width="1634" width="1634" data-og-height="1046" height="1046" data-path="images/extensions/examples/js-commands/js-uninstall.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=b5e1c0bb03891ee0335e0899b54e458d 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a06f23a491926fcefee4673dd7fde6f0 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=dcf28c19017293a7043ad35e83241211 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=72c15e289ea486c033ea6ba1df6fa0b8 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=1228245ad4084699db5b3733525c545d 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/js-uninstall.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f20fd6e54355085980fd8a13a017557a 2500w" />
</Frame>

## Setting up your extension replit app

The first thing you want to do is fork an extension template. We recommend using the [React Extension Template](https://replit.com/@replit/React-Extension?v=1). although we are not going to write any react code in this tutorial.

Add a background script to your extension. You can scaffold a background script by typing in `replkit add background` in the shell. This creates a new folder `src/background`. The `src/background/main.tsx` file here is where we'll be writing our code.

## Adding a root command

Let's add a simple root command to the command bar to contain our subcommands.

```typescript  theme={null}
async function main() {
  await replit.commands.add({
    id: "js-commands",
    contributions: [replit.ContributionType.CommandBar],
    command: {
      label: "JS",
      description: "JavaScript Commands",
      icon: "js.png",
      commands: async () => {
        // This is where subcomands go:
        return [];
      },
    },
  });
}

main();
```

This adds an empty 'context' command, AKA a command that contains other sub-commands. This is what it looks like:

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=aa63f0a470a531cf85d0bfc0b2d2d3c3" alt="" data-og-width="1202" width="1202" data-og-height="270" height="270" data-path="images/extensions/examples/js-commands/empty-cmd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6903377ef7d01d306aca27c9c8770106 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=af1bb9820104eda95f0218410a2401e9 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=79b71a1288bff86d37f6106ede721de9 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=469bc297ba753b7bb92a56f249934a43 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ceb785eab2669fe34ff01a618e177f85 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/empty-cmd.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=1dfd910b24f3309047b8ea3f553a349e 2500w" />
</Frame>

## Building "Uninstall"

Let's start with Uninstall. This command first figures out what packages you have installed, and then runs `npm uninstall ${package}`

The simplest way to figure out what you have installed is by parsing `package.json`, and looking at the dependencies object. Since this tutorial is focused on commands, here's the code that reads `package.json` and returns an array of installed packages:

```typescript  theme={null}
async function getPackageJson() {
  // This uses replit's filesystem API to read the package.json file. The command returns an object containing `content` as a string, or an `error` field if something went wrong
  const res = await replit.fs.readFile("package.json");

  if (res.error) return { error: res.error, result: null };

  try {
    let packageJsonObject = JSON.parse(res.content);
    return { error: null, result: packageJsonObject };
  } catch (e) {
    return {
      error: new Error("Failed to parse package.json: " + e.message),
      result: null,
    };
  }
}

async function getInstalledPackages() {
  const packageJsonRes = await getPackageJson();

  if (packageJsonRes.error) return packageJsonRes;

  // This returns an array of { name, version } objects
  const packages = Object.entries(packageJsonRes.result.dependencies).map(([name, version]) => ({
    name,
    version,
  }));

  return {
    error: null,
    result: packages,
  }
}
```

Armed with these functions, we can build the uninstall subcommand. The subcommand returns a list of action commands, one per package.

```typescript  theme={null}
const uninstallCommand = {
  label: "Uninstall",
  description: "Uninstall npm packages",
  commands: async () => {
    const packagesRes = await getInstalledPackages();

    if (packagesRes.error) {
      return null;
    }

    return packagesRes.result.map(({ name, version }) => {
      return {
        label: name,
        description: version,
        run: async () => {
          await replit.exec.exec(`npm uninstall ${name}`);
        },
      };
    });
  },
};
```

To add this command to our root command, simply include `uninstallCommand` as one of the commands returned by the root command:

```typescript  theme={null}
    {
      commands: async () => {
        // This is where subcomands go:
        return [
            uninstallCommand,
        ];
      },
    }
```

This is what it looks like in our JavaScript command now:

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ac2ca3544c0d52de098877595d070d4d" alt="" data-og-width="1096" width="1096" data-og-height="248" height="248" data-path="images/extensions/examples/js-commands/uninstall-root.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=cc7862960d376555ef3fe0cae76675d0 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c85ac03566efcbb4fa78339553168393 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d97d1872716907f7852944ceb3bafd42 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ecb3a17f93d46cdd034dd441683e89ee 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7e803d6f35f2c680457cb521b3cc913b 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-root.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9f2466ae5d793ea0c83488e30619712e 2500w" />
</Frame>

As you can see, the uninstall command lists installed npm packages that you can uninstall

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=979eaf198cc7362b687b69a161a5cba9" alt="" data-og-width="1124" width="1124" data-og-height="306" height="306" data-path="images/extensions/examples/js-commands/uninstall-pkgs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4ed7657238e6cd0235b039e51de87e38 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c169c5f1ee54e4fe580e6046c84aee90 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2b014e1d0dfacf12bfcbb816d75b225b 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d6c6cbce6095308db97962b78ff7c39b 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=718385e6ba69f2415bebd567ec1935f1 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/uninstall-pkgs.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=800ad0b00bb069aa2d50c2fc9eba6112 2500w" />
</Frame>

## Building "Scripts"

"Scripts" is very similar to uninstall, except that we need to surface the output from the script. For this, we use an experimental API called execInShell.

Other than that, we can reuse most of the code from "Uninstall"

```typescript  theme={null}
async function getScripts() {
  const packageJsonRes = await getPackageJson();

  if (packageJsonRes.error) return packageJsonRes;

  // This returns an array of { name, version } objects
  const scripts = Object.entries(packageJsonRes.result.scripts).map(
    ([name, cmd]) => ({
      name,
      cmd,
    }),
  );

  return {
    error: null,
    result: scripts,
  };
}

const scriptsCommand = {
  label: "Scripts",
  description: "Run scripts in your package.json",
  commands: async () => {
    const scriptsRes = await getScripts();

    if (scriptsRes.error) {
      return null;
    }

    return scriptsRes.result.map(({ name, cmd }) => {
      return {
        label: name,
        description: cmd,
        run: async () => {
          await replit.experimental.execInShell(`npm run ${name}`);
        },
      };
    });
  },
};
```

Let's add the scripts command to our root command!

```typescript  theme={null}
    {
      commands: async () => {
        // This is where subcomands go:
        return [
            scriptsCommand,
            uninstallCommand,
        ];
      },
    }
```

Here's our command!

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8346a4131cb307bb80225f807beb7c5e" alt="" data-og-width="1068" width="1068" data-og-height="502" height="502" data-path="images/extensions/examples/js-commands/scripts-root.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6a0c2556403287417760fbe5af921fde 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6c25c2a52ab1672c154c0d918da47cdd 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3fb62536d6db17006969f0738223b67f 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c840f519f4c7a282ed9b0a2483a623b9 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=4782df6993ec415d5450d4e52f26da58 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-root.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d1881b2c2d05622604d09565728664d2 2500w" />
</Frame>

## Building "Install"

"Install" is somewhat different: we are pulling external data from the npm registry in response to the user typing in a search query. And we only want to explicitly trigger this search when the user has indicated that they want to search for npm packages to install

```typescript  theme={null}
async function getNpmPackages(search) {
  try {
    const res = await fetch(
      `https://registry.npmjs.org/-/v1/search?text=${search}`,
    );
    const json = await res.json();

    return { error: null, result: json.objects };
  } catch (e) {
    return { error: e, result: null };
  }
}

const installCommand = {
  label: "Install",
  description: "Install a package from npm",
  commands: async ({ search, active }) => {
    // This makes sure we do not perform a search unless someone selects "Install"
    if (!active) {
      return;
    }

    const packagesRes = await getNpmPackages();

    if (packagesRes.error) {
      return null;
    }

    return packagesRes.result.map((pkg) => {
      return {
        label: pkg.package.name,
        description: pkg.package.description,
        run: async () => {
          await replit.experimental.execInShell(`npm i ${pkg.package.name}`);
        },
      };
    });
  },
};
```

Notice the `search` and `active` parameters?

* `active` is `true` when users have selected the "Install" command (as opposed to the command system merely querying for subcommands in advance). We can check for it to make sure that we only query npm when we know that a user is interested in installing an extension.
* `search` returns what the user has typed into the command bar, which we use for searching the npm registry

This means that extensions can decide which scripts are directly accessible from the root CommandBar. For example, the scripts extension can let users search and trigger scripts immediately after opening the CommandBar:

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7fcbe911395e5a07fab8ee8a519e099a" alt="" data-og-width="1068" width="1068" data-og-height="642" height="642" data-path="images/extensions/examples/js-commands/scripts-directly-accessible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9c99db492b2a01d260e4b81cca0e3e68 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=586a14865899c144acc6c1e975703f55 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c4a9f88dd5a9efbf1223dedaae71dbf9 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c0d902d13b15dbaa6823b357157b0aaf 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2f226168d13706735b73c7a0fbe003aa 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/scripts-directly-accessible.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=e423af9d93ad4c71a08f226cb4cf9b2f 2500w" />
</Frame>

We are ready to add "Install" to the root command! This is what our root command object looks like now:

```typescript  theme={null}
  await replit.commands.add({
    id: "js-commands",
    contributions: [replit.ContributionType.CommandBar],
    command: {
      label: "JS",
      description: "JavaScript Commands",
      commands: async () => {
        // This is where subcomands go:
        return [
            installCommand,
            scriptsCommand,
            uninstallCommand,
        ];
      },
    },
  });
```

Open the command bar, type in "Install", select your new command, and give it a try!

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=505bd969acb7a47572e9bcc53794cb64" alt="" data-og-width="1114" width="1114" data-og-height="1162" height="1162" data-path="images/extensions/examples/js-commands/install-react.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7785ab6a7181c2497e5d064af41c336e 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=02e059b48108f1251a3379fd9d3721a4 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f5619069676fd5e521d5a04385f4da7e 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=68190b22aaeb522d7faaa866b9c3770e 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=381b90b8ffcdc6250c9ee51c464b255d 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/js-commands/install-react.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6248326650c18c6e03bf12871aeb921b 2500w" />
</Frame>

## Exercises left to the reader

We built a basic version of the JavaScript commands extension. This could be improved quite a bit:

* Did you notice that we only use `npm` in all the examples? JavaScript ecosystem has a plethora of package managers, including yarn, pnpm, and bun. How can we support all of them? And can we do it "magically" where someone using this extension doesn't have to manually select their package manager in our command? (Hint: it involves the lockfiles)

* We can probably cache the npm registry fetch call, so when you backspace through any letters, the results for that search query appear instantly.

* We can debounce npm search requests to prevent hitting npmjs.com excessively while you're typing out the package you're looking for.

* What happens if someone uses this command in a replit app that isn't a JavaScript project? We can probably check for the presence of `package.json` before showing the command. And maybe, if someone doesn't have a `package.json` yet, we can instead show a command to `npm init` their project!

If you just want to look at the solution, see the JavaScript commands extension on the store:

* Here's the link to the [extension](https://replit.com/extension/@ArnavBansal/adccbcd2-c9d6-4778-b0cb-20e1bf289634)
* Here's a link to the extension's [source replit app](https://replit.com/@ArnavBansal/js-commands-extension?v=1)
