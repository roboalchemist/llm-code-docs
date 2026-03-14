# Source: https://fiona.readthedocs.io/

Title: access to simple geospatial feature data — Fiona documentation

URL Source: https://fiona.readthedocs.io/

Markdown Content:
[Fiona](https://fiona.readthedocs.io/#)
Fiona streams simple feature data to and from GIS formats like GeoPackage and Shapefile. Simple features are record, or row-like, and have a single geometry attribute. Fiona can read and write real-world simple feature data using multi-layered GIS formats, zipped and in-memory virtual file systems, from files on your hard drive or in cloud storage. This project includes Python modules and a command line interface (CLI).

Here’s an example of streaming and filtering features from a zipped dataset on the web and saving them to a new layer in a new Geopackage file.

import fiona

with fiona.open(
    "zip+https://github.com/Toblerity/Fiona/files/11151652/coutwildrnp.zip"
) as src:
    profile = src.profile
    profile["driver"] = "GPKG"

    with fiona.open("example.gpkg", "w", layer="selection", **profile) as dst:
        dst.writerecords(feat in src.filter(bbox=(-107.0, 37.0, -105.0, 39.0)))

The same result can be achieved on the command line using a combination of fio-cat and fio-load.

fio cat zip+https://github.com/Toblerity/Fiona/files/11151652/coutwildrnp.zip --bbox "-107.0,37.0,-105.0,39.0" \
| fio load -f GPKG --layer selection example.gpkg

*   [Project Information](https://fiona.readthedocs.io/en/stable/README.html)
    *   [Installation](https://fiona.readthedocs.io/en/stable/README.html#installation)
    *   [Python Usage](https://fiona.readthedocs.io/en/stable/README.html#python-usage)
    *   [CLI Usage](https://fiona.readthedocs.io/en/stable/README.html#cli-usage)
    *   [Documentation](https://fiona.readthedocs.io/en/stable/README.html#documentation)
    *   [Changes](https://fiona.readthedocs.io/en/stable/README.html#changes)
    *   [Credits](https://fiona.readthedocs.io/en/stable/README.html#credits)

*   [Installation](https://fiona.readthedocs.io/en/stable/install.html)
    *   [Easy installation](https://fiona.readthedocs.io/en/stable/install.html#easy-installation)
    *   [Advanced installation](https://fiona.readthedocs.io/en/stable/install.html#advanced-installation)

*   [User Manual](https://fiona.readthedocs.io/en/stable/manual.html)
    *   [1.1 Introduction](https://fiona.readthedocs.io/en/stable/manual.html#introduction)
    *   [1.2 Data Model](https://fiona.readthedocs.io/en/stable/manual.html#data-model)
    *   [1.3 Reading Vector Data](https://fiona.readthedocs.io/en/stable/manual.html#reading-vector-data)
    *   [1.4 Format Drivers, CRS, Bounds, and Schema](https://fiona.readthedocs.io/en/stable/manual.html#format-drivers-crs-bounds-and-schema)
    *   [1.5 Features](https://fiona.readthedocs.io/en/stable/manual.html#features)
    *   [1.6 Writing Vector Data](https://fiona.readthedocs.io/en/stable/manual.html#writing-vector-data)
    *   [1.7 Advanced Topics](https://fiona.readthedocs.io/en/stable/manual.html#advanced-topics)
    *   [1.8 Fiona command line interface](https://fiona.readthedocs.io/en/stable/manual.html#fiona-command-line-interface)
    *   [1.9 Final Notes](https://fiona.readthedocs.io/en/stable/manual.html#final-notes)
    *   [1.10 References](https://fiona.readthedocs.io/en/stable/manual.html#references)

*   [API Documentation](https://fiona.readthedocs.io/en/stable/modules.html)
    *   [fiona package](https://fiona.readthedocs.io/en/stable/fiona.html)

*   [CLI Documentation](https://fiona.readthedocs.io/en/stable/cli.html)
    *   [bounds](https://fiona.readthedocs.io/en/stable/cli.html#bounds)
    *   [calc](https://fiona.readthedocs.io/en/stable/cli.html#calc)
    *   [cat](https://fiona.readthedocs.io/en/stable/cli.html#cat)
    *   [collect](https://fiona.readthedocs.io/en/stable/cli.html#collect)
    *   [distrib](https://fiona.readthedocs.io/en/stable/cli.html#distrib)
    *   [dump](https://fiona.readthedocs.io/en/stable/cli.html#dump)
    *   [info](https://fiona.readthedocs.io/en/stable/cli.html#info)
    *   [load](https://fiona.readthedocs.io/en/stable/cli.html#load)
    *   [filter](https://fiona.readthedocs.io/en/stable/cli.html#filter)
    *   [map](https://fiona.readthedocs.io/en/stable/cli.html#map)
    *   [reduce](https://fiona.readthedocs.io/en/stable/cli.html#reduce)
    *   [rm](https://fiona.readthedocs.io/en/stable/cli.html#rm)
    *   [Expressions and functions](https://fiona.readthedocs.io/en/stable/cli.html#expressions-and-functions)
    *   [Builtin Python functions](https://fiona.readthedocs.io/en/stable/cli.html#builtin-python-functions)
    *   [Itertools functions](https://fiona.readthedocs.io/en/stable/cli.html#itertools-functions)
    *   [Shapely functions](https://fiona.readthedocs.io/en/stable/cli.html#shapely-functions)
    *   [Functions specific to fiona](https://fiona.readthedocs.io/en/stable/cli.html#functions-specific-to-fiona)
    *   [Feature and geometry context for expressions](https://fiona.readthedocs.io/en/stable/cli.html#feature-and-geometry-context-for-expressions)
    *   [Coordinate Reference System Transformations](https://fiona.readthedocs.io/en/stable/cli.html#coordinate-reference-system-transformations)
    *   [Sizing up and simplifying shapes](https://fiona.readthedocs.io/en/stable/cli.html#sizing-up-and-simplifying-shapes)

Indices and tables[](https://fiona.readthedocs.io/#indices-and-tables "Link to this heading")
----------------------------------------------------------------------------------------------

*   [Index](https://fiona.readthedocs.io/en/stable/genindex.html)

*   [Module Index](https://fiona.readthedocs.io/en/stable/py-modindex.html)

*   [Search Page](https://fiona.readthedocs.io/en/stable/search.html)
