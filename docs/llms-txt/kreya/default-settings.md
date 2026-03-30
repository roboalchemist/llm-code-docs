# Source: https://kreya.app/docs/default-settings.md

# Default / directory settings

Are you using only one endpoint in your project and you are tired of pasting `{{ env.endpoint }}` into every endpoint field? Do you want to use gRPC-Web for a bunch of operations which are all in the same directory? Or do you want to ignore the TLS server certificate validation for all operations when working locally? Then this feature is for you.

Note that this are *default* settings. You can still overwrite them in folders and operations.

## Project default settings[​](#project-default-settings "Direct link to Project default settings")

Project default settings apply to the whole project (unless overwritten of course). In the menu, click Project → Default settings to access the default settings.

**Important: The default settings are separated by gRPC, REST, GraphQL and WebSocket because they use different values.** Make sure that you configure the correct default settings by selecting the correct tab.

Default authentications can be configured in the Auth tab.

![The project default settings view](/assets/ideal-img/project-default-settings.1ff26c2.400.png)

In the above example, a default gRPC endpoint has been configured for all environments. These settings will apply as long as they are not overwritten via directory default settings or in the operation itself.

## Directory default settings[​](#directory-default-settings "Direct link to Directory default settings")

You can also configure default settings for a directory, which only apply to subdirectories and operations within that directory. To do that, select a directory in the operation list.

![A directory has been selected to configure the directory default settings](/assets/ideal-img/directory-default-settings.17ec43a.400.png)

If you specify values in the directory default settings, they will overwrite the values defined in the project default settings and parent directory settings However, if you leave some values empty, the project (or parent directory) default values will still apply.

In the above example, you can see that the REST endpoint was left blank and thus the project default settings still applies. In addition, a default REST header has been configured, which will apply to all operations in the selected folder.

## Default settings for a specific environment[​](#default-settings-for-a-specific-environment "Direct link to Default settings for a specific environment")

By default, default settings will be applied regardless of the currently active environment. Sometimes, it is useful to specify default values only for specific environments.

![A directory has been selected to configure the directory default settings](/assets/ideal-img/environment-specific-default-settings.4ea53ac.400.png)

In the example, the server certificate validation was disabled, but only for the selected "Staging" environment. You can also see that a default header is inherited, meaning that the "parent" default settings still apply.

## Clarifications[​](#clarifications "Direct link to Clarifications")

If default values are left blank, they are ignored (meaning that the "parent" default values apply).

Arrays of default values, such as gRPC metadata or REST headers, can only be appended to. Removing or overwriting values is not supported.

Settings (ex. the endpoint) are applied in the following order (higher numbers are applied later and thus overwrite previous default settings):

1. Project default settings (for all environments)

2. Project default settings (for the current environment)

3. Starting with the top-most directory, apply this for each directory, then go to the next subdirectory (until the directory is reached which contains the operation)

   <!-- -->

   1. Directory default settings (for all environments)
   2. Directory default settings (for the current environment)

4. Operation settings
