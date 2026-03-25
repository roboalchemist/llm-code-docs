# Source: https://seaborn.pydata.org/api.html

Title: API reference — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/api.html

Markdown Content:
Objects interface[#](https://seaborn.pydata.org/api.html#objects-interface "Permalink to this heading")
-------------------------------------------------------------------------------------------------------

### Plot object[#](https://seaborn.pydata.org/api.html#plot-object "Permalink to this heading")

[`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")An interface for declaratively specifying statistical graphics.

### Mark objects[#](https://seaborn.pydata.org/api.html#mark-objects "Permalink to this heading")

Dot marks

[`Dot`](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "seaborn.objects.Dot")A mark suitable for dot plots or less-dense scatterplots.
[`Dots`](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn.objects.Dots "seaborn.objects.Dots")A dot mark defined by strokes to better handle overplotting.

Line marks

[`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")A mark connecting data points with sorting along the orientation axis.
[`Lines`](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "seaborn.objects.Lines")A faster but less-flexible mark for drawing many lines.
[`Path`](https://seaborn.pydata.org/generated/seaborn.objects.Path.html#seaborn.objects.Path "seaborn.objects.Path")A mark connecting data points in the order they appear.
[`Paths`](https://seaborn.pydata.org/generated/seaborn.objects.Paths.html#seaborn.objects.Paths "seaborn.objects.Paths")A faster but less-flexible mark for drawing many paths.
[`Dash`](https://seaborn.pydata.org/generated/seaborn.objects.Dash.html#seaborn.objects.Dash "seaborn.objects.Dash")A line mark drawn as an oriented segment for each datapoint.
[`Range`](https://seaborn.pydata.org/generated/seaborn.objects.Range.html#seaborn.objects.Range "seaborn.objects.Range")An oriented line mark drawn between min/max values.

Bar marks

[`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar")A bar mark drawn between baseline and data values.
[`Bars`](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "seaborn.objects.Bars")A faster bar mark with defaults more suitable for histograms.

Fill marks

[`Area`](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn.objects.Area "seaborn.objects.Area")A fill mark drawn from a baseline to data values.
[`Band`](https://seaborn.pydata.org/generated/seaborn.objects.Band.html#seaborn.objects.Band "seaborn.objects.Band")A fill mark representing an interval between values.

Text marks

[`Text`](https://seaborn.pydata.org/generated/seaborn.objects.Text.html#seaborn.objects.Text "seaborn.objects.Text")A textual mark to annotate or represent data values.

### Stat objects[#](https://seaborn.pydata.org/api.html#stat-objects "Permalink to this heading")

[`Agg`](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn.objects.Agg "seaborn.objects.Agg")Aggregate data along the value axis using given method.
[`Est`](https://seaborn.pydata.org/generated/seaborn.objects.Est.html#seaborn.objects.Est "seaborn.objects.Est")Calculate a point estimate and error bar interval.
[`Count`](https://seaborn.pydata.org/generated/seaborn.objects.Count.html#seaborn.objects.Count "seaborn.objects.Count")Count distinct observations within groups.
[`Hist`](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "seaborn.objects.Hist")Bin observations, count them, and optionally normalize or cumulate.
[`KDE`](https://seaborn.pydata.org/generated/seaborn.objects.KDE.html#seaborn.objects.KDE "seaborn.objects.KDE")Compute a univariate kernel density estimate.
[`Perc`](https://seaborn.pydata.org/generated/seaborn.objects.Perc.html#seaborn.objects.Perc "seaborn.objects.Perc")Replace observations with percentile values.
[`PolyFit`](https://seaborn.pydata.org/generated/seaborn.objects.PolyFit.html#seaborn.objects.PolyFit "seaborn.objects.PolyFit")Fit a polynomial of the given order and resample data onto predicted curve.

### Move objects[#](https://seaborn.pydata.org/api.html#move-objects "Permalink to this heading")

[`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge")Displacement and narrowing of overlapping marks along orientation axis.
[`Jitter`](https://seaborn.pydata.org/generated/seaborn.objects.Jitter.html#seaborn.objects.Jitter "seaborn.objects.Jitter")Random displacement along one or both axes to reduce overplotting.
[`Norm`](https://seaborn.pydata.org/generated/seaborn.objects.Norm.html#seaborn.objects.Norm "seaborn.objects.Norm")Divisive scaling on the value axis after aggregating within groups.
[`Stack`](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "seaborn.objects.Stack")Displacement of overlapping bar or area marks along the value axis.
[`Shift`](https://seaborn.pydata.org/generated/seaborn.objects.Shift.html#seaborn.objects.Shift "seaborn.objects.Shift")Displacement of all marks with the same magnitude / direction.

### Scale objects[#](https://seaborn.pydata.org/api.html#scale-objects "Permalink to this heading")

[`Boolean`](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html#seaborn.objects.Boolean "seaborn.objects.Boolean")A scale with a discrete domain of True and False values.
[`Continuous`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous "seaborn.objects.Continuous")A numeric scale supporting norms and functional transforms.
[`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")A categorical scale without relative importance / magnitude.
[`Temporal`](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html#seaborn.objects.Temporal "seaborn.objects.Temporal")A scale for date/time data.

### Base classes[#](https://seaborn.pydata.org/api.html#base-classes "Permalink to this heading")

[`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark")Base class for objects that visually represent data.
[`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat")Base class for objects that apply statistical transformations.
[`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move")Base class for objects that apply simple positional transforms.
[`Scale`](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html#seaborn.objects.Scale "seaborn.objects.Scale")Base class for objects that map data values to visual properties.

Function interface[#](https://seaborn.pydata.org/api.html#function-interface "Permalink to this heading")
---------------------------------------------------------------------------------------------------------

### Relational plots[#](https://seaborn.pydata.org/api.html#relational-plots "Permalink to this heading")

[`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")Figure-level interface for drawing relational plots onto a FacetGrid.
[`scatterplot`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")Draw a scatter plot with possibility of several semantic groupings.
[`lineplot`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")Draw a line plot with possibility of several semantic groupings.

### Distribution plots[#](https://seaborn.pydata.org/api.html#distribution-plots "Permalink to this heading")

[`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")Figure-level interface for drawing distribution plots onto a FacetGrid.
[`histplot`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")Plot univariate or bivariate histograms to show distributions of datasets.
[`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")Plot univariate or bivariate distributions using kernel density estimation.
[`ecdfplot`](https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot "seaborn.ecdfplot")Plot empirical cumulative distribution functions.
[`rugplot`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "seaborn.rugplot")Plot marginal distributions by drawing ticks along the x and y axes.
[`distplot`](https://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot "seaborn.distplot")DEPRECATED

### Categorical plots[#](https://seaborn.pydata.org/api.html#categorical-plots "Permalink to this heading")

[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")Figure-level interface for drawing categorical plots onto a FacetGrid.
[`stripplot`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")Draw a categorical scatterplot using jitter to reduce overplotting.
[`swarmplot`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot "seaborn.swarmplot")Draw a categorical scatterplot with points adjusted to be non-overlapping.
[`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")Draw a box plot to show distributions with respect to categories.
[`violinplot`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")Draw a patch representing a KDE and add observations or box plot statistics.
[`boxenplot`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot "seaborn.boxenplot")Draw an enhanced box plot for larger datasets.
[`pointplot`](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot "seaborn.pointplot")Show point estimates and errors using lines with markers.
[`barplot`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")Show point estimates and errors as rectangular bars.
[`countplot`](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot "seaborn.countplot")Show the counts of observations in each categorical bin using bars.

### Regression plots[#](https://seaborn.pydata.org/api.html#regression-plots "Permalink to this heading")

[`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")Plot data and regression model fits across a FacetGrid.
[`regplot`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")Plot data and a linear regression model fit.
[`residplot`](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot "seaborn.residplot")Plot the residuals of a linear regression.

### Matrix plots[#](https://seaborn.pydata.org/api.html#matrix-plots "Permalink to this heading")

[`heatmap`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")Plot rectangular data as a color-encoded matrix.
[`clustermap`](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap "seaborn.clustermap")Plot a matrix dataset as a hierarchically-clustered heatmap.

Multi-plot grids[#](https://seaborn.pydata.org/api.html#multi-plot-grids "Permalink to this heading")
-----------------------------------------------------------------------------------------------------

### Facet grids[#](https://seaborn.pydata.org/api.html#facet-grids "Permalink to this heading")

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")Multi-plot grid for plotting conditional relationships.

### Pair grids[#](https://seaborn.pydata.org/api.html#pair-grids "Permalink to this heading")

[`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")Plot pairwise relationships in a dataset.
[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")Subplot grid for plotting pairwise relationships in a dataset.

### Joint grids[#](https://seaborn.pydata.org/api.html#joint-grids "Permalink to this heading")

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")Draw a plot of two variables with bivariate and univariate graphs.
[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")Grid for drawing a bivariate plot with marginal univariate plots.

Themeing[#](https://seaborn.pydata.org/api.html#themeing "Permalink to this heading")
-------------------------------------------------------------------------------------

[`set_theme`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")Set aspects of the visual theme for all matplotlib and seaborn plots.
[`axes_style`](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style "seaborn.axes_style")Get the parameters that control the general style of the plots.
[`set_style`](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style "seaborn.set_style")Set the parameters that control the general style of the plots.
[`plotting_context`](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context "seaborn.plotting_context")Get the parameters that control the scaling of plot elements.
[`set_context`](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context "seaborn.set_context")Set the parameters that control the scaling of plot elements.
[`set_color_codes`](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes "seaborn.set_color_codes")Change how matplotlib color shorthands are interpreted.
[`reset_defaults`](https://seaborn.pydata.org/generated/seaborn.reset_defaults.html#seaborn.reset_defaults "seaborn.reset_defaults")Restore all RC params to default settings.
[`reset_orig`](https://seaborn.pydata.org/generated/seaborn.reset_orig.html#seaborn.reset_orig "seaborn.reset_orig")Restore all RC params to original settings (respects custom rc).
[`set`](https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set "seaborn.set")Alias for [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme"), which is the preferred interface.

Color palettes[#](https://seaborn.pydata.org/api.html#color-palettes "Permalink to this heading")
-------------------------------------------------------------------------------------------------

[`set_palette`](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette "seaborn.set_palette")Set the matplotlib color cycle using a seaborn palette.
[`color_palette`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")Return a list of colors or continuous colormap defining a palette.
[`husl_palette`](https://seaborn.pydata.org/generated/seaborn.husl_palette.html#seaborn.husl_palette "seaborn.husl_palette")Return hues with constant lightness and saturation in the HUSL system.
[`hls_palette`](https://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn.hls_palette "seaborn.hls_palette")Return hues with constant lightness and saturation in the HLS system.
[`cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")Make a sequential palette from the cubehelix system.
[`dark_palette`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")Make a sequential palette that blends from dark to `color`.
[`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette")Make a sequential palette that blends from light to `color`.
[`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")Make a diverging palette between two HUSL colors.
[`blend_palette`](https://seaborn.pydata.org/generated/seaborn.blend_palette.html#seaborn.blend_palette "seaborn.blend_palette")Make a palette that blends between a list of colors.
[`xkcd_palette`](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn.xkcd_palette "seaborn.xkcd_palette")Make a palette with color names from the xkcd color survey.
[`crayon_palette`](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html#seaborn.crayon_palette "seaborn.crayon_palette")Make a palette with color names from Crayola crayons.
[`mpl_palette`](https://seaborn.pydata.org/generated/seaborn.mpl_palette.html#seaborn.mpl_palette "seaborn.mpl_palette")Return a palette or colormap from the matplotlib registry.

### Palette widgets[#](https://seaborn.pydata.org/api.html#palette-widgets "Permalink to this heading")

Utility functions[#](https://seaborn.pydata.org/api.html#utility-functions "Permalink to this heading")
-------------------------------------------------------------------------------------------------------

[`despine`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")Remove the top and right spines from plot(s).
[`move_legend`](https://seaborn.pydata.org/generated/seaborn.move_legend.html#seaborn.move_legend "seaborn.move_legend")Recreate a plot's legend at a new location.
[`saturate`](https://seaborn.pydata.org/generated/seaborn.saturate.html#seaborn.saturate "seaborn.saturate")Return a fully saturated color with the same hue.
[`desaturate`](https://seaborn.pydata.org/generated/seaborn.desaturate.html#seaborn.desaturate "seaborn.desaturate")Decrease the saturation channel of a color by some percent.
[`set_hls_values`](https://seaborn.pydata.org/generated/seaborn.set_hls_values.html#seaborn.set_hls_values "seaborn.set_hls_values")Independently manipulate the h, l, or s channels of a color.
[`load_dataset`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")Load an example dataset from the online repository (requires internet).
[`get_dataset_names`](https://seaborn.pydata.org/generated/seaborn.get_dataset_names.html#seaborn.get_dataset_names "seaborn.get_dataset_names")Report available example datasets, useful for reporting issues.
[`get_data_home`](https://seaborn.pydata.org/generated/seaborn.get_data_home.html#seaborn.get_data_home "seaborn.get_data_home")Return a path to the cache directory for example datasets.
