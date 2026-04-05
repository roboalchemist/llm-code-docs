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
  [.rst]{.btn__text-container}](../_sources/python/devices_and_streams.rst "Download source file"){.btn
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
# Devices and Streams

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#devices-and-streams .section}
[]{#id1}

# Devices and Streams[\#](#devices-and-streams "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------
  [[`Device`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference .internal}(\*args, \*\*kwargs)                                       A device to run operations on.
  [[`Stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}                                                              A stream for running operations on a given device.
  [[`default_device`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.default_device.html#mlx.core.default_device "mlx.core.default_device"){.reference .internal}()                         Get the default device.
  [[`set_default_device`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.set_default_device.html#mlx.core.set_default_device "mlx.core.set_default_device"){.reference .internal}(device)   Set the default device.
  [[`default_stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.default_stream.html#mlx.core.default_stream "mlx.core.default_stream"){.reference .internal}(device)                   Get the device\'s default stream.
  [[`new_stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.new_stream.html#mlx.core.new_stream "mlx.core.new_stream"){.reference .internal}(device)                                   Make a new stream on the given device.
  [[`set_default_stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.set_default_stream.html#mlx.core.set_default_stream "mlx.core.set_default_stream"){.reference .internal}(stream)   Set the default stream.
  [[`stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.stream.html#mlx.core.stream "mlx.core.stream"){.reference .internal}(s)                                                        Create a context manager to set the default device and stream.
  [[`synchronize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.synchronize.html#mlx.core.synchronize "mlx.core.synchronize"){.reference .internal}(\[stream\])                           Synchronize with the given stream.
  [[`device_count`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.device_count.html#mlx.core.device_count "mlx.core.device_count"){.reference .internal}(device_type)                      Get the number of available devices for the given device type.
  [[`device_info`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.device_info.html#mlx.core.device_info "mlx.core.device_info"){.reference .internal}(\[d\])                                Get information about a device.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.finfo.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.finfo
:::

[](_autosummary/mlx.core.Device.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.Device
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
