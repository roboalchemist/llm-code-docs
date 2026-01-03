::: {#troubleshooting-install}
::: redirect-from
/users/installing/troubleshooting_faq
:::
:::

# Troubleshooting

## Obtaining Matplotlib version {#matplotlib-version}

To find out your Matplotlib version number, import it and print the
`__version__` attribute:

\>\>\> import matplotlib \>\>\> matplotlib.\_\_version\_\_ \'0.98.0\'

## `matplotlib`{.interpreted-text role="file"} install location {#locating-matplotlib-install}

You can find what directory Matplotlib is installed in by importing it
and printing the `__file__` attribute:

\>\>\> import matplotlib \>\>\> matplotlib.\_\_file\_\_
\'/home/jdhunter/dev/lib64/python2.5/site-packages/matplotlib/\_\_init\_\_.pyc\'

## `matplotlib`{.interpreted-text role="file"} configuration and cache directory locations {#locating-matplotlib-config-dir}

Each user has a Matplotlib configuration directory which may contain a
`matplotlibrc <customizing-with-matplotlibrc-files>`{.interpreted-text
role="ref"} file. To locate your `matplotlib/`{.interpreted-text
role="file"} configuration directory, use
`matplotlib.get_configdir`{.interpreted-text role="func"}:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_configdir()
\'/home/darren/.config/matplotlib\'

On Unix-like systems, this directory is generally located in your
`HOME`{.interpreted-text role="envvar"} directory under the
`.config/`{.interpreted-text role="file"} directory.

In addition, users have a cache directory. On Unix-like systems, this is
separate from the configuration directory by default. To locate your
`.cache/`{.interpreted-text role="file"} directory, use
`matplotlib.get_cachedir`{.interpreted-text role="func"}:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_cachedir()
\'/home/darren/.cache/matplotlib\'

On Windows, both the config directory and the cache directory are the
same and are in your `Documents and Settings`{.interpreted-text
role="file"} or `Users`{.interpreted-text role="file"} directory by
default:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_configdir()
\'C:\\Documents and Settings\\jdhunter\\.matplotlib\' \>\>\>
mpl.get_cachedir() \'C:\\Documents and Settings\\jdhunter\\.matplotlib\'

If you would like to use a different configuration directory, you can do
so by specifying the location in your `MPLCONFIGDIR`{.interpreted-text
role="envvar"} environment variable \-- see
`setting-linux-macos-environment-variables`{.interpreted-text
role="ref"}. Note that `MPLCONFIGDIR`{.interpreted-text role="envvar"}
sets the location of both the configuration directory and the cache
directory.
