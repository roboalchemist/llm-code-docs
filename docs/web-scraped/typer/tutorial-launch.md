# Source: https://typer.tiangolo.com/tutorial/launch/

# Launching Applications[¶](#launching-applications "Permanent link")

You can launch applications from your CLI program with `typer.launch()`.

It will launch the appropriate application depending on the URL or file type you pass it:

Python 3.9+

Check it:

    $ python main.py

    Opening Typer docs

    // Opens browser with Typer's docs

## Locating a file[¶](#locating-a-file "Permanent link")

You can also make the operating system open the file browser indicating where a file is located with `locate=True`:

Python 3.9+

Tip

The rest of the code in this example is just making sure the app directory exists and creating the config file.

But the most important part is the `typer.launch(config_file_str, locate=True)` with the argument `locate=True`.

Check it:

    $ python main.py

    Opening config directory

    // Opens a file browser indicating where the config file is located