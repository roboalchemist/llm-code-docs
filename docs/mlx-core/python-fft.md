:::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::: bd-content
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
  [.rst]{.btn__text-container}](../_sources/python/fft.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}
::::
:::::
::::::
:::::::::
::::::::::

::::: {#jb-print-docs-body .onlyprint}
# FFT

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#fft .section}
[]{#id1}

# FFT[\#](#fft "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`fft`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.fft.html#mlx.core.fft.fft "mlx.core.fft.fft"){.reference .internal}(a\[, n, axis, stream\])                        One dimensional discrete Fourier Transform.
  [[`ifft`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.ifft.html#mlx.core.fft.ifft "mlx.core.fft.ifft"){.reference .internal}(a\[, n, axis, stream\])                    One dimensional inverse discrete Fourier Transform.
  [[`fft2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.fft2.html#mlx.core.fft.fft2 "mlx.core.fft.fft2"){.reference .internal}(a\[, s, axes, stream\])                    Two dimensional discrete Fourier Transform.
  [[`ifft2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.ifft2.html#mlx.core.fft.ifft2 "mlx.core.fft.ifft2"){.reference .internal}(a\[, s, axes, stream\])                Two dimensional inverse discrete Fourier Transform.
  [[`fftn`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.fftn.html#mlx.core.fft.fftn "mlx.core.fft.fftn"){.reference .internal}(a\[, s, axes, stream\])                    n-dimensional discrete Fourier Transform.
  [[`ifftn`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.ifftn.html#mlx.core.fft.ifftn "mlx.core.fft.ifftn"){.reference .internal}(a\[, s, axes, stream\])                n-dimensional inverse discrete Fourier Transform.
  [[`rfft`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfft.html#mlx.core.fft.rfft "mlx.core.fft.rfft"){.reference .internal}(a\[, n, axis, stream\])                    One dimensional discrete Fourier Transform on a real input.
  [[`irfft`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.irfft.html#mlx.core.fft.irfft "mlx.core.fft.irfft"){.reference .internal}(a\[, n, axis, stream\])                The inverse of [[`rfft()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfft.html#mlx.core.fft.rfft "mlx.core.fft.rfft"){.reference .internal}.
  [[`rfft2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfft2.html#mlx.core.fft.rfft2 "mlx.core.fft.rfft2"){.reference .internal}(a\[, s, axes, stream\])                Two dimensional real discrete Fourier Transform.
  [[`irfft2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.irfft2.html#mlx.core.fft.irfft2 "mlx.core.fft.irfft2"){.reference .internal}(a\[, s, axes, stream\])            The inverse of [[`rfft2()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfft2.html#mlx.core.fft.rfft2 "mlx.core.fft.rfft2"){.reference .internal}.
  [[`rfftn`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfftn.html#mlx.core.fft.rfftn "mlx.core.fft.rfftn"){.reference .internal}(a\[, s, axes, stream\])                n-dimensional real discrete Fourier Transform.
  [[`irfftn`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.irfftn.html#mlx.core.fft.irfftn "mlx.core.fft.irfftn"){.reference .internal}(a\[, s, axes, stream\])            The inverse of [[`rfftn()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.rfftn.html#mlx.core.fft.rfftn "mlx.core.fft.rfftn"){.reference .internal}.
  [[`fftshift`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.fftshift.html#mlx.core.fft.fftshift "mlx.core.fft.fftshift"){.reference .internal}(a\[, axes, stream\])       Shift the zero-frequency component to the center of the spectrum.
  [[`ifftshift`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.ifftshift.html#mlx.core.fft.ifftshift "mlx.core.fft.ifftshift"){.reference .internal}(a\[, axes, stream\])   The inverse of [[`fftshift()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fft.fftshift.html#mlx.core.fft.fftshift "mlx.core.fft.fftshift"){.reference .internal}.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.fast.cuda_kernel.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.fast.cuda_kernel
:::

[](_autosummary/mlx.core.fft.fft.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.fft.fft
:::
:::::
::::::::::::::::::::
:::::::::::::::::::::

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
::::::::::::::::::::::::::::
