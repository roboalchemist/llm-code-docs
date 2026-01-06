# Source: https://docs.helix-editor.com/configuration.html

# Configuration

To override global configuration parameters, create aconfig.tomlfile located in your config directory:
- Linux and Mac:~/.config/helix/config.toml
- Windows:%AppData%\helix\config.toml
> 💡 You can easily open the config file by typing:config-openwithin Helix normal mode.
Example config:

```
theme = "onedark"

[editor]
line-number = "relative"
mouse = false

[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"

[editor.file-picker]
hidden = false
```

You can use a custom configuration file by specifying it with the-cor--configcommand line argument, for examplehx -c path/to/custom-config.toml.
You can reload the config file by issuing the:config-reloadcommand. Alternatively, on Unix operating systems, you can reload it by sending the USR1
signal to the Helix process, such as by using the commandpkill -USR1 hx.
Finally, you can have aconfig.tomllocal to a project by putting it under a.helixdirectory in your repository.
Its settings will be merged with the configuration directoryconfig.tomland the built-in configuration.