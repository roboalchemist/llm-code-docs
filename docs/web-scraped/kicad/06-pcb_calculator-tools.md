:::::: {#header}

# PCB Calculator

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}
::: {#toctitle}
Table of Contents
:::

- [Introduction](#introduction)
- [Calculators](#calculators)
  - [Regulators](#regulators)
  - [Track-Width](#track-width)
  - [Electrical-Spacing](#electrical-spacing)
  - [TransLine](#transline)
  - [RF-Attenuators](#rf-attenuators)
  - [Color-Code](#color-code)
  - [Board-Classes](#board-classes)
::::
::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}
:::::::::::::: {#preamble}
::::::::::::: sectionbody
::: paragraph
*Reference manual*
:::

::: {#copyright .paragraph}
**Copyright**
:::

::: paragraph
This document is Copyright © 2019 by it's contributors as listed below.
You may distribute it and/or modify it under the terms of either the GNU
General Public License
([http://www.gnu.org/licenses/gpl.html](http://www.gnu.org/licenses/gpl.html){.bare}),
version 3 or later, or the Creative Commons Attribution License
([http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/){.bare}),
version 3.0 or later.
:::

::: {#contributors .paragraph}
**Contributors**
:::

::: paragraph
Heitor de Bittencourt. Mathias Neumann
:::

::: {#feedback .paragraph}
**Feedback**
:::

::: paragraph
Please direct any bug reports, suggestions or new versions to here:
:::

::: ulist

- About KiCad document:
  [https://github.com/KiCad/kicad-doc/issues](https://github.com/KiCad/kicad-doc/issues){.bare}

- About KiCad software:
  [https://bugs.launchpad.net/kicad](https://bugs.launchpad.net/kicad){.bare}

- About KiCad software i18n:
  [https://github.com/KiCad/kicad-i18n/issues](https://github.com/KiCad/kicad-i18n/issues){.bare}
:::

::: {#publication_date_and_software_version .paragraph}
**Publication date and software version**
:::

::: paragraph
july 17, 2019
:::
:::::::::::::
::::::::::::::

:::::: sect1

## Introduction

::::: sectionbody
::: paragraph
The KiCad PCB Calculator is a set of utilities to help you find the
values of components or other paremeters of a layout. The Calculator has
the following tools:
:::

::: ulist

- Regulators

- Track Width

- Electrical Spacing

- Trans Line

- RF Attenuators

- Color Code

- Board Classes
:::
:::::
::::::

::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Calculators

:::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::::: sect2

### Regulators

::: paragraph
This calculator helps with the task of finding the values of the
resistors needed for linear and low-dropout voltage regulators.
:::

:::: imageblock
::: content
![Regulators](images/en/regulators.png)
:::
::::

::: paragraph
For the *Standard Type*, the output voltage Vout as a function of the
reference voltage Vref and resistors R1 and R2 is given by:
:::

:::: imageblock
::: content
![Regulators](images/Calculation1.png)
:::
::::

::: paragraph
For the *3 terminal type*, there is a correction factor due to the
quiescent current Iadj flowing from the adjust pin:
:::

:::: imageblock
::: content
![Regulators](images/Calculation2.png)
:::
::::

::: paragraph
This current is typically below 100 uA and can be neglected with
caution.
:::

::: paragraph
To use this calculator, enter the parameters of the regulator *Type*,
*Vref* and, if needed, *Iadj*, select the field you want to calculate
(one of the resistors or the output voltage) and enter the other two
values.
:::
::::::::::::::

:::::: sect2

### Track-Width

::: paragraph
The Track Width tool calculates the trace width for printed circuit
board conductors for a given current and temperature rise. It uses
formulas from IPC-2221 (formerly IPC-D-275).
:::

:::: imageblock
::: content
![Track-Width](images/en/trackwidth.png)
:::
::::
::::::

::::::: sect2

### Electrical-Spacing

::: paragraph
This table helps finding the minimum clearance between conductors.
:::

::: paragraph
Each line of the table has a minimum recomended distance between
conductors for a given voltage (DC or AC peaks) range. If you need the
values for voltages higher than 500V, enter the value in the box in the
left corner and press *Update Values*.
:::

:::: imageblock
::: content
![Electrical-Spacing](images/en/electricalspacing.png)
:::
::::
:::::::

:::::::::: sect2

### TransLine

::: paragraph
Transmission line theory is a cornerstone in the teaching of RF and
microwave engineering.
:::

::: paragraph
In the calculator you can choose different sorts of Line Types and their
special parameters. The models implemented are frequency-dependent, so
they disagree with simpler models at high *enough* frequencies.
:::

::: paragraph
This calculator is heavilly based on
[Transcalc](http://transcalc.sourceforge.net/).
:::

::: paragraph
The transmission line types and the reference of their mathematical
models are listed below:
:::

::: ulist

- Microstrip line:

  ::: ulist

  - H. A. Atwater, "Simplified Design Equations for Microstrip Line
    Parameters", Microwave Journal, pp. 109-115, November 1989.
  :::

- Coplanar wave guide.

- Coplanar wave guide with ground plane.

- Rectangular waveguide:

  ::: ulist

  - S. Ramo, J. R. Whinnery and T. van Duzer, \"Fields and Waves in
    Communication Electronics\", Wiley-India, 2008, ISBN: 9788126515257.
  :::

- Coaxial line.

- Coupled microstrip line:

  ::: ulist

  - H. A. Atwater, "Simplified Design Equations for Microstrip Line
    Parameters", Microwave Journal, pp. 109-115, November 1989.

  - M. Kirschning and R. H. Jansen, \"Accurate Wide-Range Design
    Equations for the Frequency-Dependent Characteristic of Parallel
    Coupled Microstrip Lines,\" in IEEE Transactions on Microwave Theory
    and Techniques, vol. 32, no. 1, pp. 83-90, Jan. 1984. doi:
    10.1109/TMTT.1984.1132616.

  - Rolf Jansen, \"High-Speed Computation of Single and Coupled
    Microstrip Parameters Including Dispersion, High-Order Modes, Loss
    and Finite Strip Thickness\", IEEE Trans. MTT, vol. 26, no. 2, pp.
    75-82, Feb. 1978.

  - S. March, \"Microstrip Packaging: Watch the Last Step\", Microwaves,
    vol. 20, no. 13, pp. 83.94, Dec. 1981.
  :::

- Stripline.

- Twisted pair.
:::

:::: imageblock
::: content
![TransLine](images/en/transline.png)
:::
::::
::::::::::

:::::::: sect2

### RF-Attenuators

::: paragraph
With the RF Attenuator utility you can calculate the values of the
resistors needed for different types of attenuators:
:::

::: ulist

- PI

- Tee

- Bridged Tee

- Resistive Splitter
:::

::: paragraph
To use this tool, first select the type of attenuator you need, then
enter the desired attenuation (in dB) and input/output impedances (in
Ohms).
:::

:::: imageblock
::: content
![RF Attenuators](images/en/rfattenuators.png)
:::
::::
::::::::

::::::: sect2

### Color-Code

::: paragraph
This calculator helps translating the color bars from the resistor to
its value. To use it, first select the *tolerance* of the resistor: 10%,
5% or equal or smaller than 2%. For example:
:::

::: ulist

- Yellow Violet Red Gold: 4 7 x100 ±5% = 4700 Ohm, 5% tolerance

- 1kOhm, 1% tolerance: Brown Black Black Brown Brown
:::

:::: imageblock
::: content
![Color-Code](images/en/colorcode.png)
:::
::::
:::::::

::::: sect2

### Board-Classes

:::: imageblock
::: content
![Board-Classes](images/en/boardclasses.png)
:::
::::
:::::
::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}
::: {#footer-text}
Last updated 2026-03-15 16:35:47 -0700
:::
::::
