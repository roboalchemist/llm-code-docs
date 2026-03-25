# Source: https://seaborn.pydata.org/tutorial/color_palettes.html

Title: Choosing color palettes — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/tutorial/color_palettes.html

Published Time: Thu, 25 Jan 2024 13:24:12 GMT

Markdown Content:
Choosing color palettes — seaborn 0.13.2 documentation
===============
- [x] - [x] 

Ctrl+K

[![Image 1: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)![Image 2: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/index.html)

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
*   [API](https://seaborn.pydata.org/api.html)
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/citing.html)
*   [FAQ](https://seaborn.pydata.org/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
*   [API](https://seaborn.pydata.org/api.html)
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/citing.html)
*   [FAQ](https://seaborn.pydata.org/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

*   [An introduction to seaborn](https://seaborn.pydata.org/tutorial/introduction.html)

*   [Overview of seaborn plotting functions](https://seaborn.pydata.org/tutorial/function_overview.html)

*   [Data structures accepted by seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)

*   [The seaborn.objects interface](https://seaborn.pydata.org/tutorial/objects_interface.html)

*   [Properties of Mark objects](https://seaborn.pydata.org/tutorial/properties.html)

*   [Visualizing statistical relationships](https://seaborn.pydata.org/tutorial/relational.html)

*   [Visualizing distributions of data](https://seaborn.pydata.org/tutorial/distributions.html)

*   [Visualizing categorical data](https://seaborn.pydata.org/tutorial/categorical.html)

*   [Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)

*   [Estimating regression fits](https://seaborn.pydata.org/tutorial/regression.html)

*   [Building structured multi-plot grids](https://seaborn.pydata.org/tutorial/axis_grids.html)

*   [Controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)

*   [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#)

 On this page 

*   [General principles for using color in plots](https://seaborn.pydata.org/tutorial/color_palettes.html#general-principles-for-using-color-in-plots)
    *   [Components of color](https://seaborn.pydata.org/tutorial/color_palettes.html#components-of-color)
    *   [Vary hue to distinguish categories](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-hue-to-distinguish-categories)
    *   [Vary luminance to represent numbers](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-luminance-to-represent-numbers)

*   [Tools for choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#tools-for-choosing-color-palettes)
*   [Qualitative color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes)
    *   [Using circular color systems](https://seaborn.pydata.org/tutorial/color_palettes.html#using-circular-color-systems)
    *   [Using categorical Color Brewer palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#using-categorical-color-brewer-palettes)

*   [Sequential color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes)
    *   [Perceptually uniform palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-palettes)
    *   [Discrete vs. continuous mapping](https://seaborn.pydata.org/tutorial/color_palettes.html#discrete-vs-continuous-mapping)
    *   [Sequential “cubehelix” palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-cubehelix-palettes)
    *   [Custom sequential palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#custom-sequential-palettes)
    *   [Sequential Color Brewer palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-brewer-palettes)

*   [Diverging color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#diverging-color-palettes)
    *   [Perceptually uniform diverging palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-diverging-palettes)
    *   [Custom diverging palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#custom-diverging-palettes)
    *   [Other diverging palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#other-diverging-palettes)

Choosing color palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#choosing-color-palettes "Permalink to this heading")
=======================================================================================================================================

Seaborn makes it easy to use colors that are well-suited to the characteristics of your data and your visualization goals. This chapter discusses both the general principles that should guide your choices and the tools in seaborn that help you quickly find the best solution for a given application.

General principles for using color in plots[#](https://seaborn.pydata.org/tutorial/color_palettes.html#general-principles-for-using-color-in-plots "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Components of color[#](https://seaborn.pydata.org/tutorial/color_palettes.html#components-of-color "Permalink to this heading")

Because of the way our eyes work, a particular color can be defined using three components. We usually program colors in a computer by specifying their RGB values, which set the intensity of the red, green, and blue channels in a display. But for analyzing the perceptual attributes of a color, it’s better to think in terms of _hue_, _saturation_, and _luminance_ channels.

Hue is the component that distinguishes “different colors” in a non-technical sense. It’s property of color that leads to first-order names like “red” and “blue”:

Saturation (or chroma) is the _colorfulness_. Two colors with different hues will look more distinct when they have more saturation:

And lightness corresponds to how much light is emitted (or reflected, for printed colors), ranging from black to white:

### Vary hue to distinguish categories[#](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-hue-to-distinguish-categories "Permalink to this heading")

When you want to represent multiple categories in a plot, you typically should vary the color of the elements. Consider this simple example: in which of these two plots is it easier to count the number of triangular points?

![Image 3: ../_images/color_palettes_9_0.png](https://seaborn.pydata.org/_images/color_palettes_9_0.png)
In the plot on the right, the orange triangles “pop out”, making it easy to distinguish them from the circles. This pop-out effect happens because our visual system prioritizes color differences.

The blue and orange colors differ mostly in terms of their hue. Hue is useful for representing categories: most people can distinguish a moderate number of hues relatively easily, and points that have different hues but similar brightness or intensity seem equally important. It also makes plots easier to talk about. Consider this example:

![Image 4: ../_images/color_palettes_11_0.png](https://seaborn.pydata.org/_images/color_palettes_11_0.png)
Most people would be able to quickly ascertain that there are five distinct categories in the plot on the left and, if asked to characterize the “blue” points, would be able to do so.

With the plot on the right, where the points are all blue but vary in their luminance and saturation, it’s harder to say how many unique categories are present. And how would we talk about a particular category? “The fairly-but-not-too-blue points?” What’s more, the gray dots seem to fade into the background, de-emphasizing them relative to the more intense blue dots. If the categories are equally important, this is a poor representation.

So as a general rule, use hue variation to represent categories. With that said, here are few notes of caution. If you have more than a handful of colors in your plot, it can become difficult to keep in mind what each one means, unless there are pre-existing associations between the categories and the colors used to represent them. This makes your plot harder to interpret: rather than focusing on the data, a viewer will have to continually refer to the legend to make sense of what is shown. So you should strive not to make plots that are too complex. And be mindful that not everyone sees colors the same way. Varying both shape (or some other attribute) and color can help people with anomalous color vision understand your plots, and it can keep them (somewhat) interpretable if they are printed to black-and-white.

### Vary luminance to represent numbers[#](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-luminance-to-represent-numbers "Permalink to this heading")

On the other hand, hue variations are not well suited to representing numeric data. Consider this example, where we need colors to represent the counts in a bivariate histogram. On the left, we use a circular colormap, where gradual changes in the number of observation within each bin correspond to gradual changes in hue. On the right, we use a palette that uses brighter colors to represent bins with larger counts:

![Image 5: ../_images/color_palettes_14_0.png](https://seaborn.pydata.org/_images/color_palettes_14_0.png)
With the hue-based palette, it’s quite difficult to ascertain the shape of the bivariate distribution. In contrast, the luminance palette makes it much more clear that there are two prominent peaks.

Varying luminance helps you see structure in data, and changes in luminance are more intuitively processed as changes in importance. But the plot on the right does not use a grayscale colormap. Its colorfulness makes it more interesting, and the subtle hue variation increases the perceptual distance between two values. As a result, small differences slightly easier to resolve.

These examples show that color palette choices are about more than aesthetics: the colors you choose can reveal patterns in your data if used effectively or hide them if used poorly. There is not one optimal palette, but there are palettes that are better or worse for particular datasets and visualization approaches.

And aesthetics do matter: the more that people want to look at your figures, the greater the chance that they will learn something from them. This is true even when you are making plots for yourself. During exploratory data analysis, you may generate many similar figures. Varying the color palettes will add a sense of novelty, which keeps you engaged and prepared to notice interesting features of your data.

So how can you choose color palettes that both represent your data well and look attractive?

Tools for choosing color palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#tools-for-choosing-color-palettes "Permalink to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The most important function for working with color palettes is, aptly, [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette"). This function provides an interface to most of the possible ways that one can generate color palettes in seaborn. And it’s used internally by any function that has a `palette` argument.

The primary argument to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") is usually a string: either the name of a specific palette or the name of a family and additional arguments to select a specific member. In the latter case, [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") will delegate to more specific function, such as [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette"). It’s also possible to pass a list of colors specified any way that matplotlib accepts (an RGB tuple, a hex code, or a name in the X11 table). The return value is an object that wraps a list of RGB tuples with a few useful methods, such as conversion to hex codes and a rich HTML representation.

Calling [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") with no arguments will return the current default color palette that matplotlib (and most seaborn functions) will use if colors are not otherwise specified. This default palette can be set with the corresponding [`set_palette()`](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette "seaborn.set_palette") function, which calls [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") internally and accepts the same arguments.

To motivate the different options that [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") provides, it will be useful to introduce a classification scheme for color palettes. Broadly, palettes fall into one of three categories:

*   qualitative palettes, good for representing categorical data

*   sequential palettes, good for representing numeric data

*   diverging palettes, good for representing numeric data with a categorical boundary

Qualitative color palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

Qualitative palettes are well-suited to representing categorical data because most of their variation is in the hue component. The default color palette in seaborn is a qualitative palette with ten distinct hues:

sns.color_palette()

These colors have the same ordering as the default matplotlib color palette, `"tab10"`, but they are a bit less intense. Compare:

sns.color_palette("tab10")

Seaborn in fact has six variations of matplotlib’s palette, called `deep`, `muted`, `pastel`, `bright`, `dark`, and `colorblind`. These span a range of average luminance and saturation values:

![Image 6: ../_images/color_palettes_22_0.svg](https://seaborn.pydata.org/_images/color_palettes_22_0.svg)
Many people find the moderated hues of the default `"deep"` palette to be aesthetically pleasing, but they are also less distinct. As a result, they may be more difficult to discriminate in some contexts, which is something to keep in mind when making publication graphics. [This comparison](https://gist.github.com/mwaskom/b35f6ebc2d4b340b4f64a4e28e778486) can be helpful for estimating how the seaborn color palettes perform when simulating different forms of colorblindess.

### Using circular color systems[#](https://seaborn.pydata.org/tutorial/color_palettes.html#using-circular-color-systems "Permalink to this heading")

When you have an arbitrary number of categories, the easiest approach to finding unique hues is to draw evenly-spaced colors in a circular color space (one where the hue changes while keeping the brightness and saturation constant). This is what most seaborn functions default to when they need to use more colors than are currently set in the default color cycle.

The most common way to do this uses the `hls` color space, which is a simple transformation of RGB values. We saw this color palette before as a counterexample for how to plot a histogram:

sns.color_palette("hls", 8)

Because of the way the human visual system works, colors that have the same luminance and saturation in terms of their RGB values won’t necessarily look equally intense To remedy this, seaborn provides an interface to the [husl](https://www.hsluv.org/) system (since renamed to HSLuv), which achieves less intensity variation as you rotate around the color wheel:

sns.color_palette("husl", 8)

When seaborn needs a categorical palette with more colors than are available in the current default, it will use this approach.

### Using categorical Color Brewer palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#using-categorical-color-brewer-palettes "Permalink to this heading")

Another source of visually pleasing categorical palettes comes from the [Color Brewer](https://colorbrewer2.org/) tool (which also has sequential and diverging palettes, as we’ll see below).

sns.color_palette("Set2")

Be aware that the qualitative Color Brewer palettes have different lengths, and the default behavior of [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") is to give you the full list:

sns.color_palette("Paired")

Sequential color palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

The second major class of color palettes is called “sequential”. This kind of mapping is appropriate when data range from relatively low or uninteresting values to relatively high or interesting values (or vice versa). As we saw above, the primary dimension of variation in a sequential palette is luminance. Some seaborn functions will default to a sequential palette when you are mapping numeric data. (For historical reasons, both categorical and numeric mappings are specified with the `hue` parameter in functions like [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot") or [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot"), even though numeric mappings use color palettes with relatively little hue variation).

### Perceptually uniform palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-palettes "Permalink to this heading")

Because they are intended to represent numeric values, the best sequential palettes will be _perceptually uniform_, meaning that the relative discriminability of two colors is proportional to the difference between the corresponding data values. Seaborn includes four perceptually uniform sequential colormaps: `"rocket"`, `"mako"`, `"flare"`, and `"crest"`. The first two have a very wide luminance range and are well suited for applications such as heatmaps, where colors fill the space they are plotted into:

sns.color_palette("rocket", as_cmap=True)

![Image 7: rocket color map](blob:http://localhost/269172ea9bbfcb00372fc247b0499517)

sns.color_palette("mako", as_cmap=True)

![Image 8: mako color map](blob:http://localhost/b822a8b82c33c999d308eb106d9533fe)
Because the extreme values of these colormaps approach white, they are not well-suited for coloring elements such as lines or points: it will be difficult to discriminate important values against a white or gray background. The “flare” and “crest” colormaps are a better choice for such plots. They have a more restricted range of luminance variations, which they compensate for with a slightly more pronounced variation in hue. The default direction of the luminance ramp is also reversed, so that smaller values have lighter colors:

sns.color_palette("flare", as_cmap=True)

![Image 9: flare color map](blob:http://localhost/d0c8d14d69660f284339290a419f50ca)

sns.color_palette("crest", as_cmap=True)

![Image 10: crest color map](blob:http://localhost/a30d3a86512e951385633c6f6460f680)
It is also possible to use the perceptually uniform colormaps provided by matplotlib, such as `"magma"` and `"viridis"`:

sns.color_palette("magma", as_cmap=True)

![Image 11: magma color map](blob:http://localhost/e6298f4e8586190fbfc098cbffe06821)

sns.color_palette("viridis", as_cmap=True)

![Image 12: viridis color map](blob:http://localhost/13b8e0ca98f7da0751e44885b8fe3ec5)
As with the convention in matplotlib, every continuous colormap has a reversed version, which has the suffix `"_r"`:

sns.color_palette("rocket_r", as_cmap=True)

![Image 13: rocket_r color map](blob:http://localhost/00f8e8765124d72d467460d45d908af6)
### Discrete vs. continuous mapping[#](https://seaborn.pydata.org/tutorial/color_palettes.html#discrete-vs-continuous-mapping "Permalink to this heading")

One thing to be aware of is that seaborn can generate discrete values from sequential colormaps and, when doing so, it will not use the most extreme values. Compare the discrete version of `"rocket"` against the continuous version shown above:

sns.color_palette("rocket")

Internally, seaborn uses the discrete version for categorical data and the continuous version when in numeric mapping mode. Discrete sequential colormaps can be well-suited for visualizing categorical data with an intrinsic ordering, especially if there is some hue variation.

### Sequential “cubehelix” palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-cubehelix-palettes "Permalink to this heading")

The perceptually uniform colormaps are difficult to programmatically generate, because they are not based on the RGB color space. The [cubehelix](https://www.mrao.cam.ac.uk/~dag/CUBEHELIX/) system offers an RGB-based compromise: it generates sequential palettes with a linear increase or decrease in brightness and some continuous variation in hue. While not perfectly perceptually uniform, the resulting colormaps have many good properties. Importantly, many aspects of the design process are parameterizable.

Matplotlib has the default cubehelix version built into it:

sns.color_palette("cubehelix", as_cmap=True)

![Image 14: cubehelix color map](blob:http://localhost/2a5eb080ad9f99b058cea7c08d58d89c)
The default palette returned by the seaborn [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette") function is a bit different from the matplotlib default in that it does not rotate as far around the hue wheel or cover as wide a range of intensities. It also reverses the luminance ramp:

sns.cubehelix_palette(as_cmap=True)

![Image 15: seaborn_cubehelix color map](blob:http://localhost/6cf456f52e221846dfb81a1d4a4d4e33)
Other arguments to [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette") control how the palette looks. The two main things you’ll change are the `start` (a value between 0 and 3) and `rot`, or number of rotations (an arbitrary value, but usually between -1 and 1)

sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)

![Image 16: seaborn_cubehelix color map](blob:http://localhost/edbdd5fbf9d5544ed0f590731fee3201)
The more you rotate, the more hue variation you will see:

sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)

![Image 17: seaborn_cubehelix color map](blob:http://localhost/2158c0a48ae4074cd7a2b33987b0a6d1)
You can control both how dark and light the endpoints are and their order:

sns.cubehelix_palette(start=2, rot=0, dark=0, light=.95, reverse=True, as_cmap=True)

![Image 18: seaborn_cubehelix color map](blob:http://localhost/8d2cdcb313b818d15ef687212e416a0a)
The [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") accepts a string code, starting with `"ch:"`, for generating an arbitrary cubehelix palette. You can passs the names of parameters in the string:

sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True)

![Image 19: seaborn_cubehelix color map](blob:http://localhost/c9d16e80068a25c4bec82d42b73f4819)
And for compactness, each parameter can be specified with its first letter:

sns.color_palette("ch:s=-.2,r=.6", as_cmap=True)

![Image 20: seaborn_cubehelix color map](blob:http://localhost/0c841a6a624cda7ee88acf278c36f5cf)
### Custom sequential palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#custom-sequential-palettes "Permalink to this heading")

For a simpler interface to custom sequential palettes, you can use [`light_palette()`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette") or [`dark_palette()`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette"), which are both seeded with a single color and produce a palette that ramps either from light or dark desaturated values to that color:

sns.light_palette("seagreen", as_cmap=True)

![Image 21: blend color map](blob:http://localhost/cb32651a16fd9fdb0c96210063dd5962)

sns.dark_palette("#69d", reverse=True, as_cmap=True)

![Image 22: blend color map](blob:http://localhost/3386be0e8f690ab6566f66086637ea3c)
As with cubehelix palettes, you can also specify light or dark palettes through [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette") or anywhere `palette` is accepted:

sns.color_palette("light:b", as_cmap=True)

![Image 23: blend color map](blob:http://localhost/fd6ad0ca1c70cb8a51c8309000be0e2d)
Reverse the colormap by adding `"_r"`:

sns.color_palette("dark:salmon_r", as_cmap=True)

![Image 24: blend color map](blob:http://localhost/7d4862239fb19b1222cb9f2c5ef6ef12)
### Sequential Color Brewer palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-brewer-palettes "Permalink to this heading")

The Color Brewer library also has some good options for sequential palettes. They include palettes with one primary hue:

sns.color_palette("Blues", as_cmap=True)

![Image 25: Blues color map](blob:http://localhost/8573dab2e38cea950f6ee4354d06f3a5)
Along with multi-hue options:

sns.color_palette("YlOrBr", as_cmap=True)

![Image 26: YlOrBr color map](blob:http://localhost/fbf2aec51397472b58713740e5bd936b)
Diverging color palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#diverging-color-palettes "Permalink to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

The third class of color palettes is called “diverging”. These are used for data where both large low and high values are interesting and span a midpoint value (often 0) that should be de-emphasized. The rules for choosing good diverging palettes are similar to good sequential palettes, except now there should be two dominant hues in the colormap, one at (or near) each pole. It’s also important that the starting values are of similar brightness and saturation.

### Perceptually uniform diverging palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-diverging-palettes "Permalink to this heading")

Seaborn includes two perceptually uniform diverging palettes: `"vlag"` and `"icefire"`. They both use blue and red at their poles, which many intuitively processes as “cold” and “hot”:

sns.color_palette("vlag", as_cmap=True)

![Image 27: vlag color map](blob:http://localhost/0b0fdc71d1beb6d5cd215edfecb89295)

sns.color_palette("icefire", as_cmap=True)

![Image 28: icefire color map](blob:http://localhost/dff2f1528b8b99e5027ef84ecd407815)
### Custom diverging palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#custom-diverging-palettes "Permalink to this heading")

You can also use the seaborn function [`diverging_palette()`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette") to create a custom colormap for diverging data. This function makes diverging palettes using the `husl` color system. You pass it two hues (in degrees) and, optionally, the lightness and saturation values for the extremes. Using `husl` means that the extreme values, and the resulting ramps to the midpoint, while not perfectly perceptually uniform, will be well-balanced:

sns.diverging_palette(220, 20, as_cmap=True)

![Image 29: blend color map](blob:http://localhost/1f4b2de1c0e0a8c24106f95859f8302b)
This is convenient when you want to stray from the boring confines of cold-hot approaches:

sns.diverging_palette(145, 300, s=60, as_cmap=True)

![Image 30: blend color map](blob:http://localhost/1513586f4e41a09cf89e9ed909d6ccf3)
It’s also possible to make a palette where the midpoint is dark rather than light:

sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)

![Image 31: blend color map](blob:http://localhost/e624cf45872b02fd8f7e8793e225d83f)
It’s important to emphasize here that using red and green, while intuitive, [should be avoided](https://en.wikipedia.org/wiki/Color_blindness).

### Other diverging palettes[#](https://seaborn.pydata.org/tutorial/color_palettes.html#other-diverging-palettes "Permalink to this heading")

There are a few other good diverging palettes built into matplotlib, including Color Brewer palettes:

sns.color_palette("Spectral", as_cmap=True)

![Image 32: Spectral color map](blob:http://localhost/141d9b3dae704444d5d6ae1319cdd20c)
And the `coolwarm` palette, which has less contrast between the middle values and the extremes:

sns.color_palette("coolwarm", as_cmap=True)

![Image 33: coolwarm color map](blob:http://localhost/8bf2e758cdb91e8ffbf3d2793bccafa9)
As you can see, there are many options for using color in your visualizations. Seaborn tries both to use good defaults and to offer a lot of flexibility.

This discussion is only the beginning, and there are a number of good resources for learning more about techniques for using color in visualizations. One great example is this [series of blog posts](https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/08/05/subtleties-of-color-part-1-of-6/) from the NASA Earth Observatory. The matplotlib docs also have a [nice tutorial](https://matplotlib.org/stable/users/explain/colors/colormaps.html) that illustrates some of the perceptual properties of their colormaps.

© Copyright 2012-2024, [Michael Waskom](https://mwaskom.github.io/).

 Created using [Sphinx](https://www.sphinx-doc.org/) and the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

[Archive](https://seaborn.pydata.org/tutorial/color_palettes.html#)

[v0.12](https://seaborn.pydata.org/archive/0.12/index.html)[v0.11](https://seaborn.pydata.org/archive/0.11/index.html)[v0.10](https://seaborn.pydata.org/archive/0.10/index.html)[v0.9](https://seaborn.pydata.org/archive/0.9/index.html)

v0.13.2
