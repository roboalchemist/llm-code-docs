# Source: https://docs.roboflow.com/developer/command-line-interface/install-and-set-up-the-cli.md

# Install and Set Up the CLI

You will need to have `Python >=3.9, <3.13`  to use the Roboflow Python package.

So, after you have python installed on your system, run the following command to install the Roboflow Python package:

```bash
pip install roboflow
```

After installing you should now have the roboflow CLI installed. Go ahead and test it.

```bash
roboflow --help
```

Which should show some help about the roboflow commands that you can run

If that's working, then you need to authenticate so that you can run CLI commands as your roboflow user.

```bash
roboflow login
```

Open the link on your browser, get the token and paste it on the terminal and hit ENTER. The credentials are saved in the disk at `~/.config/roboflow/config.json` so you should only need to do that once.
