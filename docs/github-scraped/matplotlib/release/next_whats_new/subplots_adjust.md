# Resetting the subplot parameters for figure.clear()

When calling [.Figure.clear()]{.title-ref} the settings for
[.gridspec.SubplotParams]{.title-ref} are restored to the default
values.

[\~.SubplotParams.to_dict]{.title-ref} is a new method to get the
subplot parameters as a dict, and [\~.SubplotParams.reset]{.title-ref}
resets the parameters to the defaults.
