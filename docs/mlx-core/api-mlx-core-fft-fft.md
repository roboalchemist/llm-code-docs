:::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::: bd-content
:::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-bars}
:::
::::

:::::: header-article-items__end
::::: header-article-item
:::: article-header-buttons
[[
]{.btn__icon-container}](https://github.com/ml-explore/mlx "Source repository"){.btn
.btn-sm .btn-source-repository-button target="_blank"
bs-placement="bottom" bs-toggle="tooltip"}

::: {.dropdown .dropdown-download-buttons}

- [[ ]{.btn__icon-container}
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.fft.fft.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}

[]{.fa-solid .fa-list}
::::
:::::
::::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# mlx.core.fft.fft

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`fft()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.fft.fft){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-fft-fft .section}
# mlx.core.fft.fft[\#](#mlx-core-fft-fft "Link to this heading"){.headerlink}

[[fft]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[a]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[n]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[axis]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[-1]{.pre}]{.default_value}*, *[[stream]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[Stream]{.pre}](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Device]{.pre}](mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.fft.fft "Link to this definition"){.headerlink}

:   One dimensional discrete Fourier Transform.

    Parameters[:]{.colon}

    :   - **a**
          ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}) -- The input array.

        - **n**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- Size of the transformed axis. The
          corresponding axis in the input is truncated or padded with
          zeros to match [`n`{.docutils .literal .notranslate}]{.pre}.
          The default value is [`a.shape[axis]`{.docutils .literal
          .notranslate}]{.pre}.

        - **axis**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- Axis along which to perform the
          FFT. The default is [`-1`{.docutils .literal
          .notranslate}]{.pre}.

    Returns[:]{.colon}

    :   The DFT of the input along the given axis.

    Return type[:]{.colon}

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}
:::

::::: prev-next-area
[](../fft.html "previous page"){.left-prev}

::: prev-next-info
previous

FFT
:::

[](mlx.core.fft.ifft.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.fft.ifft
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`fft()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.fft.fft){.reference .internal
  .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::

::::::: {.bd-footer-content__inner .container}
::: footer-item
By MLX Contributors
:::

::: footer-item
© Copyright 2023, Apple.\
:::

::: footer-item
:::

::: footer-item
:::
:::::::
::::::::::::::::::::::::::::::::
