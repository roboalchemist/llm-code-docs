# Source: https://xlrd.readthedocs.io/

Title: xlrd — xlrd 2.0.1 documentation

URL Source: https://xlrd.readthedocs.io/

Published Time: Sat, 21 Aug 2021 19:46:23 GMT

Markdown Content:
[![Image 1: Build Status](https://circleci.com/gh/python-excel/xlrd/tree/master.svg?style=shield)](https://circleci.com/gh/python-excel/xlrd/tree/master)[![Image 2: Coverage Status](https://codecov.io/gh/python-excel/xlrd/branch/master/graph/badge.svg?token=lNSqwBBbvk)](https://codecov.io/gh/python-excel/xlrd)[![Image 3: Documentation](https://readthedocs.org/projects/xlrd/badge/?version=latest)](http://xlrd.readthedocs.io/en/latest/?badge=latest)[![Image 4: PyPI version](https://badge.fury.io/py/xlrd.svg)](https://badge.fury.io/py/xlrd)

xlrd is a library for reading data and formatting information from Excel files in the historical `.xls` format.

Warning

This library will no longer read anything other than `.xls` files. For alternatives that read newer file formats, please see [http://www.python-excel.org/](http://www.python-excel.org/).

The following are also not supported but will safely and reliably be ignored:

*   Charts, Macros, Pictures, any other embedded object, **including** embedded worksheets.

*   VBA modules

*   Formulas, but results of formula calculations are extracted.

*   Comments

*   Hyperlinks

*   Autofilters, advanced filters, pivot tables, conditional formatting, data validation

Password-protected files are not supported and cannot be read by this library.

Quick start:

pip install xlrd

import xlrd
book = xlrd.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
    print(sh.row(rx))

From the command line, this will show the first, second and last rows of each sheet in each file:

python PYDIR/scripts/runxlrd.py 3rows *blah*.xls

You may also wish to consult the [tutorial](https://github.com/python-excel/tutorial).

Details:

*   [Handling of Unicode](https://xlrd.readthedocs.io/en/latest/unicode.html)
*   [Dates in Excel spreadsheets](https://xlrd.readthedocs.io/en/latest/dates.html)
*   [Named references, constants, formulas, and macros](https://xlrd.readthedocs.io/en/latest/references.html)
*   [Formatting information in Excel Spreadsheets](https://xlrd.readthedocs.io/en/latest/formatting.html)
*   [Loading worksheets on demand](https://xlrd.readthedocs.io/en/latest/on_demand.html)
*   [API Reference](https://xlrd.readthedocs.io/en/latest/api.html)

For details of how to get involved in development of this package, and other meta-information, please see the sections below:

*   [Development](https://xlrd.readthedocs.io/en/latest/development.html)
*   [Changes](https://xlrd.readthedocs.io/en/latest/changes.html)
*   [Acknowledgements](https://xlrd.readthedocs.io/en/latest/acknowledgements.html)
*   [Licenses](https://xlrd.readthedocs.io/en/latest/licenses.html)

Indices and tables[¶](https://xlrd.readthedocs.io/#indices-and-tables "Permalink to this headline")
---------------------------------------------------------------------------------------------------

*   [Index](https://xlrd.readthedocs.io/en/latest/genindex.html)

*   [Module Index](https://xlrd.readthedocs.io/en/latest/py-modindex.html)

*   [Search Page](https://xlrd.readthedocs.io/en/latest/search.html)
