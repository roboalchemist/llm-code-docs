# Source: https://docs.pytest.org/en/stable/how-to/bash-completion.html

[]

# How to set up bash completion[¶](#how-to-set-up-bash-completion "Link to this heading")

When using bash as your shell, [`pytest`] can use argcomplete ([https://kislyuk.github.io/argcomplete/](https://kislyuk.github.io/argcomplete/)) for auto-completion. For this [`argcomplete`] needs to be installed **and** enabled.

Install argcomplete using:

    sudo pip install 'argcomplete>=0.5.7'

For global activation of all argcomplete enabled python applications run:

    sudo activate-global-python-argcomplete

For permanent (but not global) [`pytest`] activation, use:

    register-python-argcomplete pytest >> ~/.bashrc

For one-time activation of argcomplete for [`pytest`] only, use:

    eval "$(register-python-argcomplete pytest)"