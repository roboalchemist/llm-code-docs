# Source: https://herd.laravel.com/docs/macos/debugging/tinker.md

# Tinker

# Launching Tinker

Laravel Tinker is a REPL for Laravel, and it allows you to interact with your application via the command line. While you usually start it via the terminal by running `php artisan tinker` or `herd tinker`, Herd provides a convenient button in the actions column in the sites settings as well as a global shortcut that instantly opens the active project automatically.

<Note>
  Herd integrates natively with [Tinkerwell](https://tinkerwell.app) and gives you a fantastic tinker experience with multi-line code editing, autocompletion, and SSH access to your applications.
</Note>

## Open Tinker from the site settings

You can run the Tinker site action from the [Site Manager](/macos/sites/managing-sites) to start a new tinker or Tinkerwell session directly in your site.

<Frame>
  <img alt="Tinker button in the site manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=764428860a4ff3a27c6a190cd356beb7" data-og-width="1872" width="1872" data-og-height="1122" height="1122" data-path="images/docs/sites_actions_tinker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dca4ecdd340e4b8f549fe61933a75d6f 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b289646e381fe6b3b339e2680d38b6a 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b138322002bf217a2361450a49b8d83 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=16bc7f7ed8c20edaea543e4fffaf1a80 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=42c4673523ea794cc48b7f6e0b84b6eb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=461e84b5ccc2975374ca6cd63dff5ff4 2500w" />
</Frame>

## Open Tinker with a global shortcut

Herd allows you to define global system shortcuts and Tinker is part of this configuration. By pressing the global tinker shortcut, Herd starts a tinker session for the last site that you visited via your browser.

<Frame>
  <img alt="Tinker Shortcut Settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ce4b61afb1f57650423bb4896fa47c65" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_shortcuts_tinker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c8ad1723788f6f16a29c84271d4fbeb3 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbc3d1cf4b07885e97efc8b911da1a06 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=770ef9391e2bbd98f9df47719ad480e0 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=541288637502e1c71a954f82c45d3aa4 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ad21ceb8c8a15a2fce19e88ac1f7ee5c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e897365d8de8e64da355b1c46ab88791 2500w" />
</Frame>

# Tinkerwell Integration

[Tinkerwell](https://tinkerwell.app) users benefit from the deep integration between both tools, so if you are running `herd tinker`, click the button in the site settings or press the global shortcut and Herd detects Tinkerwell on your machine, Tinkerwell opens a new tab with the most recent Herd project automatically.

This allows you to quickly iterate on complex Eloquent queries or debug some code. It also provides autocompletion and a familiar multi-line code editor experience that goes beyond a simple REPL.

<Frame>
  <a href="https://tinkerwell.app">
    <img alt="Tinkerwell with a complex Eloquent query" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d5e8cb39e5b93c1eef9b80e6034a02e5" data-og-width="2618" width="2618" data-og-height="1720" height="1720" data-path="images/docs/tinker-tinkerwell.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=94dfc8e446dd8bfdefd8b0eb1533f4ab 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=aa479b6622361e78aaf1c7d7d1e57cb8 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6ce7f9b891f4902f98857a60e7583e8f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3e21c433bce09e0d6d15daec1593a324 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=335ba30872c027ca8bd0e5abbe489a3e 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b2c8d1966135960cdbae323c8b0bb247 2500w" />
  </a>
</Frame>

Tinkerwell ships with support for all of Herds PHP versions and automatically loads the correct configuration files.
