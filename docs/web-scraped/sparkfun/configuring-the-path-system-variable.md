# Source: https://learn.sparkfun.com/tutorials/configuring-the-path-system-variable

## Introduction

A [path](https://en.wikipedia.org/wiki/Path_(computing)) is the name of a file\'s directory, which specifies a unique location in a file system. Whereas, the [PATH system variable](https://en.wikipedia.org/wiki/PATH_(variable)) (`$PATH`), specifies a set of directories where executable programs are located. This allows software applications to access commonly executed programs.

There are different methods for modifying the (`$`)`PATH` variable on various operating systems. The directions below are based on the most common methods for each operating system. For more information, just use your favorite search engine with the keywords: `path system variable` along with `<the name of the OS you are working on>`.

## Windows 10

In Windows 10, the `PATH` system variable is configured through the **System Properties** window. There are various methods for users to access the **System Properties** window; for example, users can search `view advanced system settings` from the taskbar [⊞ Start] menu.

[![searching for system properties window](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/2/9/8/win10_search_for_advanced_system_settings.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/win10_search_for_advanced_system_settings.PNG)

*Searching `view adva` from the taskbar* [⊞ Start] *menu, to access the the **System Properties** window. (Click to enlarge)*

Once the **System Properties** window has been pulled up, select the [Environment Variables\...] button from the `Advanced` tab.

[![opening the environment variables window](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/2/9/8/win10_advanced_system_settings.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/win10_advanced_system_settings.PNG)

*Opening the **Environment Variables** window. (Click to enlarge)*

Within the **Environment Variables** window, select the `Path` variable from the **User variables for \<username\>** section. Then, select the [Edit\...] button to configure the `PATH` system variable.

**Note:** The **User variables** are specific for a user account on the computer; while, the **System variables** will be available for all accounts on the computer.

[![opening the path system variable window](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/2/9/8/win10_environment_variables.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/win10_environment_variables.png)

*Opening the `PATH` system variable window. (Click to enlarge)*

From the `PATH` **Edit environment variable** window, select the [Browse\...] button. Once the pop-up dialog box appears, navigate to the folder containing the executable file to be included in the `PATH` system variable.

**Note:** Make sure not to select and overwrite a previously configured file path. Users can click on the black space area to make sure that a previously configured file path isn\'t highlighted and therefore, won\'t get overwritten.

[![adding a directory to the path system variable](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/2/9/8/win10_edit_environment_variables.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/win10_edit_environment_variables.PNG)

*Adding a directory to the `PATH` system variable. (Click to enlarge)*

## Mac OSX and Linux Based Systems

On Mac OSX and linux based systems, users can display the paths for the `$PATH` system variable by entering `echo $PATH` into the terminal.

**Note:** The commands below use the [GNU nano](https://en.wikipedia.org/wiki/GNU_nano) text editor. Feel free to use another text editor of your choice *(such as `vi` for [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)))*.

To modify the variable:

1.  Open up Terminal and run the following command to edit the paths file: `sudo nano <file path location>`
    - There are several locations where users might be able to modify the `$PATH` system variable:
      - `/etc/paths` (Mac OSX - Mountain Lion)
      - `/usr/bin`
      - `/usr/local/bin`
      - `/usr/local/sbin`
      - `/usr/sbin`
      - `~/.bash_profile`
      - `~/.bashrc`
      - `~/.profile`
2.  Enter the super user *(administrative)* password, if prompted.
3.  Enter the modifications for the path you wish to add.
    - The entry field is usually near the bottom of the file.
4.  Hit [Ctrl]+[X] to quit.
5.  At the input prompt, send [Y] and hit [Enter] or [Return] to save the modified buffer.

[![PATH variable](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/path_raspberry_pi_small.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/8/path_raspberry_pi.gif)

*Displaying paths of `$PATH` variable and accessing the `~/.profile` file for modifications. (Click to enlarge)*

That's it! To verify the changes, in a terminal window, type: `echo $PATH`

**Note:** Another common method is to use the `export` command in the terminal.

Example: `export PATH=$PATH:<file path to be added>`