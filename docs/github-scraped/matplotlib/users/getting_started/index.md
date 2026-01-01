# Getting started

## Installation quick-start

## Draw a first plot

Here is a minimal example plot:

::: {.plot include-source="" align="center"}
import matplotlib.pyplot as plt import numpy as np

x = np.linspace(0, 2 \* np.pi, 200) y = np.sin(x)

fig, ax = plt.subplots() ax.plot(x, y) plt.show()
:::

If a plot does not show up please check
`troubleshooting-faq`{.interpreted-text role="ref"}.

## Where to go next

-   Check out `Plot types </plot_types/index>`{.interpreted-text
    role="doc"} to get an overview of the types of plots you can create
    with Matplotlib.
-   Learn Matplotlib from the ground up in the `Quick-start guide
    <quick_start>`{.interpreted-text role="ref"}.
