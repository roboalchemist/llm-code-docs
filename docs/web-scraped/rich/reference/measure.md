# Source: https://rich.readthedocs.io/en/latest/reference/measure.html

[]

# rich.measure[](#module-rich.measure "Link to this heading")

*[[class]][ ]*[[rich.measure.]][[Measurement]][(]*[[minimum]]*, *[[maximum]]*[)][[[\[source\]]]](../_modules/rich/measure.html#Measurement)[](#rich.measure.Measurement "Link to this definition")

:   Stores the minimum and maximum widths (in characters) required to render an object.

    Parameters[:]

    :   -   **minimum** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **maximum** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

    [[clamp]][(]*[[min_width]][[=]][[None]]*, *[[max_width]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/measure.html#Measurement.clamp)[](#rich.measure.Measurement.clamp "Link to this definition")

    :   Clamp a measurement within the specified range.

        Parameters[:]

        :   -   **min_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Minimum desired width, or [`None`] for no minimum. Defaults to None.

            -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum desired width, or [`None`] for no maximum. Defaults to None.

        Returns[:]

        :   New Measurement object.

        Return type[:]

        :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

    *[[classmethod]][ ]*[[get]][(]*[[console]]*, *[[options]]*, *[[renderable]]*[)][[[\[source\]]]](../_modules/rich/measure.html#Measurement.get)[](#rich.measure.Measurement.get "Link to this definition")

    :   Get a measurement for a renderable.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

            -   **options** ([*ConsoleOptions*](console.html#rich.console.ConsoleOptions "rich.console.ConsoleOptions")) -- Console options.

            -   **renderable** (*RenderableType*) -- An object that may be rendered with Rich.

        Raises[:]

        :   **errors.NotRenderableError** -- If the object is not renderable.

        Returns[:]

        :   Measurement object containing range of character widths required to render the object.

        Return type[:]

        :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

    [[maximum]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.measure.Measurement.maximum "Link to this definition")

    :   Maximum number of cells required to render.

    [[minimum]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.measure.Measurement.minimum "Link to this definition")

    :   Minimum number of cells required to render.

    [[normalize]][(][)][[[\[source\]]]](../_modules/rich/measure.html#Measurement.normalize)[](#rich.measure.Measurement.normalize "Link to this definition")

    :   Get measurement that ensures that minimum \<= maximum and minimum \>= 0

        Returns[:]

        :   A normalized measurement.

        Return type[:]

        :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

    *[[property]][ ]*[[span]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.measure.Measurement.span "Link to this definition")

    :   Get difference between maximum and minimum.

    [[with_maximum]][(]*[[width]]*[)][[[\[source\]]]](../_modules/rich/measure.html#Measurement.with_maximum)[](#rich.measure.Measurement.with_maximum "Link to this definition")

    :   Get a RenderableWith where the widths are \<= width.

        Parameters[:]

        :   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum desired width.

        Returns[:]

        :   New Measurement object.

        Return type[:]

        :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

    [[with_minimum]][(]*[[width]]*[)][[[\[source\]]]](../_modules/rich/measure.html#Measurement.with_minimum)[](#rich.measure.Measurement.with_minimum "Link to this definition")

    :   Get a RenderableWith where the widths are \>= width.

        Parameters[:]

        :   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Minimum desired width.

        Returns[:]

        :   New Measurement object.

        Return type[:]

        :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

```
<!-- -->
```

[[rich.measure.]][[measure_renderables]][(]*[[console]]*, *[[options]]*, *[[renderables]]*[)][[[\[source\]]]](../_modules/rich/measure.html#measure_renderables)[](#rich.measure.measure_renderables "Link to this definition")

:   Get a measurement that would fit a number of renderables.

    Parameters[:]

    :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

        -   **options** ([*ConsoleOptions*](console.html#rich.console.ConsoleOptions "rich.console.ConsoleOptions")) -- Console options.

        -   **renderables** (*Iterable\[RenderableType\]*) -- One or more renderable objects.

    Returns[:]

    :   

        Measurement object containing range of character widths required to

        :   contain all given renderables.

    Return type[:]

    :   [Measurement](#rich.measure.Measurement "rich.measure.Measurement")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).