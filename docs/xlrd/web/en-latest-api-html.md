# Source: https://xlrd.readthedocs.io/en/latest/api.html

Title: API Reference — xlrd 2.0.1 documentation

URL Source: https://xlrd.readthedocs.io/en/latest/api.html

Markdown Content:
xlrd[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd "Permalink to this headline")
------------------------------------------------------------------------------------------------

xlrd.FILE_FORMAT_DESCRIPTIONS _={'xls':'Excel xls','xlsb':'Excel 2007 xlsb file','xlsx':'Excel xlsx file','ods':'Openoffice.org ODS file','zip':'Unknown ZIP file',None:'Unknown file type'}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.FILE_FORMAT_DESCRIPTIONS "Permalink to this definition")
descriptions of the file types [`xlrd`](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd "xlrd") can [`inspect`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.inspect_format "xlrd.inspect_format").

xlrd.inspect_format(_path=None_, _content=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.inspect_format "Permalink to this definition")
Inspect the content at the supplied path or the [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") content provided and return the file’s type as a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)"), or `None` if it cannot be determined.

Parameters
*   **path** – A [`string`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") path containing the content to inspect. `~` will be expanded.

*   **content** – The [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") content to inspect.

Returns
A [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)"), or `None` if the format cannot be determined. The return value can always be looked up in [`FILE_FORMAT_DESCRIPTIONS`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.FILE_FORMAT_DESCRIPTIONS "xlrd.FILE_FORMAT_DESCRIPTIONS") to return a human-readable description of the format found.

xlrd.open_workbook(_filename=None_, _logfile=<\_io.TextIOWrapper name='<stdout>'mode='w'encoding='utf-8'>_, _verbosity=0_, _use\_mmap=True_, _file\_contents=None_, _encoding\_override=None_, _formatting\_info=False_, _on\_demand=False_, _ragged\_rows=False_, _ignore\_workbook\_corruption=False_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "Permalink to this definition")
Open a spreadsheet file for data extraction.

Parameters
*   **filename** – The path to the spreadsheet file to be opened.

*   **logfile** – An open file to which messages and diagnostics are written.

*   **verbosity** – Increases the volume of trace material written to the logfile.

*   **use_mmap** –

Whether to use the mmap module is determined heuristically. Use this arg to override the result.

Current heuristic: mmap is used if it exists.

*   **file_contents** – A string or an [`mmap.mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "(in Python v3.9)") object or some other behave-alike object. If `file_contents` is supplied, `filename` will not be used, except (possibly) in messages.

*   **encoding_override** – Used to overcome missing or bad codepage information in older-version files. See [Handling of Unicode](https://xlrd.readthedocs.io/en/latest/unicode.html).

*   **formatting_info** –

The default is `False`, which saves memory. In this case, “Blank” cells, which are those with their own formatting information but no data, are treated as empty by ignoring the file’s `BLANK` and `MULBLANK` records. This cuts off any bottom or right “margin” of rows of empty or blank cells. Only [`cell_value()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_value "xlrd.sheet.Sheet.cell_value") and [`cell_type()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_type "xlrd.sheet.Sheet.cell_type") are available.

When `True`, formatting information will be read from the spreadsheet file. This provides all cells, including empty and blank cells. Formatting information is available for each cell.

Note that this will raise a NotImplementedError when used with an xlsx file.

*   **on_demand** – Governs whether sheets are all loaded initially or when demanded by the caller. See [Loading worksheets on demand](https://xlrd.readthedocs.io/en/latest/on_demand.html).

*   **ragged_rows** –

The default of `False` means all rows are padded out with empty cells so that all rows have the same size as found in [`ncols`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.ncols "xlrd.sheet.Sheet.ncols").

`True` means that there are no empty cells at the ends of rows. This can result in substantial memory savings if rows are of widely varying sizes. See also the [`row_len()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_len "xlrd.sheet.Sheet.row_len") method.

*   **ignore_workbook_corruption** – This option allows to read corrupted workbooks. When `False` you may face CompDocError: Workbook corruption. When `True` that exception will be ignored.

Returns
An instance of the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") class.

xlrd.dump(_filename_, _outfile=<\_io.TextIOWrapper name='<stdout>'mode='w'encoding='utf-8'>_, _unnumbered=False_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.dump "Permalink to this definition")
For debugging: dump an XLS file’s BIFF records in char & hex.

Parameters
*   **filename** – The path to the file to be dumped.

*   **outfile** – An open file, to which the dump is written.

*   **unnumbered** – If true, omit offsets (for meaningful diffs).

xlrd.count_records(_filename_, _outfile=<\_io.TextIOWrapper name='<stdout>'mode='w'encoding='utf-8'>_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.count_records "Permalink to this definition")
For debugging and analysis: summarise the file’s BIFF records. ie: produce a sorted file of `(record_name, count)`.

Parameters
*   **filename** – The path to the file to be summarised.

*   **outfile** – An open file, to which the summary is written.

xlrd.biffh[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.biffh "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

_exception_ xlrd.biffh.XLRDError[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.XLRDError "Permalink to this definition")
An exception indicating problems reading data from an Excel file.

_class_ xlrd.biffh.BaseObject[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.BaseObject "Permalink to this definition")
Parent of almost all other classes in the package. Defines a common [`dump()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.BaseObject.dump "xlrd.biffh.BaseObject.dump") method for debugging.

dump(_f=None_, _header=None_, _footer=None_, _indent=0_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.BaseObject.dump "Permalink to this definition")Parameters
*   **f** – open file object, to which the dump is written

*   **header** – text to write before the dump

*   **footer** – text to write after the dump

*   **indent** – number of leading spaces (for recursive calls)

xlrd.biffh.error_text_from_code _={0:'#NULL!',7:'#DIV/0!',15:'#VALUE!',23:'#REF!',29:'#NAME?',36:'#NUM!',42:'#N/A'}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.error_text_from_code "Permalink to this definition")
This dictionary can be used to produce a text version of the internal codes that Excel uses for error cells.

xlrd.biffh.unpack_unicode(_data_, _pos_, _lenlen=2_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.unpack_unicode "Permalink to this definition")
Return unicode_strg

xlrd.biffh.unpack_unicode_update_pos(_data_, _pos_, _lenlen=2_, _known\_len=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.unpack_unicode_update_pos "Permalink to this definition")
Return (unicode_strg, updated value of pos)

xlrd.book[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.book "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

_class_ xlrd.book.Name[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name "Permalink to this definition")
Information relating to a named reference, formula, macro, etc.

Note

Name information is **not** extracted from files older than Excel 5.0 (`Book.biff_version < 50`)

hidden _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.hidden "Permalink to this definition")
0 = Visible; 1 = Hidden

func _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.func "Permalink to this definition")
0 = Command macro; 1 = Function macro. Relevant only if macro == 1

vbasic _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.vbasic "Permalink to this definition")
0 = Sheet macro; 1 = VisualBasic macro. Relevant only if macro == 1

macro _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.macro "Permalink to this definition")
0 = Standard name; 1 = Macro name

complex _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.complex "Permalink to this definition")
0 = Simple formula; 1 = Complex formula (array formula or user defined).

Note

No examples have been sighted.

builtin _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.builtin "Permalink to this definition")
0 = User-defined name; 1 = Built-in name

Common examples: `Print_Area`, `Print_Titles`; see OOo docs for full list

funcgroup _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.funcgroup "Permalink to this definition")
Function group. Relevant only if macro == 1; see OOo docs for values.

binary _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.binary "Permalink to this definition")
0 = Formula definition; 1 = Binary data

Note

No examples have been sighted.

name_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.name_index "Permalink to this definition")
The index of this object in book.name_obj_list

raw_formula _=b''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.raw_formula "Permalink to this definition")
An 8-bit string.

scope _=-1_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.scope "Permalink to this definition")`-1`:
The name is global (visible in all calculation sheets).

`-2`:
The name belongs to a macro sheet or VBA sheet.

`-3`:
The name is invalid.

`0 <= scope < book.nsheets`:
The name is local to the sheet whose index is scope.

cell()[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.cell "Permalink to this definition")
This is a convenience method for the frequent use case where the name refers to a single cell.

Returns
An instance of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") class.

Raises
[**xlrd.biffh.XLRDError**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.XLRDError "xlrd.biffh.XLRDError") – The name is not a constant absolute reference to a single cell.

area2d(_clipped=True_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name.area2d "Permalink to this definition")
This is a convenience method for the use case where the name refers to one rectangular area in one worksheet.

Parameters
**clipped** – If `True`, the default, the returned rectangle is clipped to fit in `(0, sheet.nrows, 0, sheet.ncols)`. it is guaranteed that `0 <= rowxlo <= rowxhi <= sheet.nrows` and that the number of usable rows in the area (which may be zero) is `rowxhi - rowxlo`; likewise for columns.

Returns
a tuple `(sheet_object, rowxlo, rowxhi, colxlo, colxhi)`.

Raises
[**xlrd.biffh.XLRDError**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.biffh.XLRDError "xlrd.biffh.XLRDError") – The name is not a constant absolute reference to a single area in a single sheet.

_class_ xlrd.book.Book[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "Permalink to this definition")
Contents of a “workbook”.

Warning

You should not instantiate this class yourself. You use the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") object that was returned when you called [`open_workbook()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "xlrd.open_workbook").

datemode _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.datemode "Permalink to this definition")
Which date system was in force when this file was last saved.

0:
1900 system (the Excel for Windows default).

1:
1904 system (the Excel for Macintosh default).

Defaults to 0 in case it’s not specified in the file.

biff_version _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.biff_version "Permalink to this definition")
Version of BIFF (Binary Interchange File Format) used to create the file. Latest is 8.0 (represented here as 80), introduced with Excel 97. Earliest supported by this module: 2.0 (represented as 20).

codepage _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.codepage "Permalink to this definition")
An integer denoting the character set used for strings in this file. For BIFF 8 and later, this will be 1200, meaning Unicode; more precisely, UTF_16_LE. For earlier versions, this is used to derive the appropriate Python encoding to be used to convert to Unicode. Examples: `1252 -> 'cp1252'`, `10000 -> 'mac_roman'`

encoding _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.encoding "Permalink to this definition")
The encoding that was derived from the codepage.

countries _=(0,0)_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.countries "Permalink to this definition")
A tuple containing the telephone country code for:

`[0]`:
the user-interface setting when the file was created.

`[1]`:
the regional settings.

Example: `(1, 61)` meaning `(USA, Australia)`.

This information may give a clue to the correct encoding for an unknown codepage. For a long list of observed values, refer to the OpenOffice.org documentation for the `COUNTRY` record.

user_name _=''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.user_name "Permalink to this definition")
What (if anything) is recorded as the name of the last user to save the file.

font_list _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.font_list "Permalink to this definition")
A list of [`Font`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font "xlrd.formatting.Font") class instances, each corresponding to a FONT record.

New in version 0.6.1.

format_list _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.format_list "Permalink to this definition")
A list of [`Format`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format "xlrd.formatting.Format") objects, each corresponding to a `FORMAT` record, in the order that they appear in the input file. It does _not_ contain builtin formats.

If you are creating an output file using (for example) `xlwt`, use this list.

The collection to be used for all visual rendering purposes is [`format_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.format_map "xlrd.book.Book.format_map").

New in version 0.6.1.

format_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.format_map "Permalink to this definition")
The mapping from [`format_key`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.format_key "xlrd.formatting.XF.format_key") to [`Format`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format "xlrd.formatting.Format") object.

New in version 0.6.1.

load_time_stage_1 _=-1.0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.load_time_stage_1 "Permalink to this definition")
Time in seconds to extract the XLS image as a contiguous string (or mmap equivalent).

load_time_stage_2 _=-1.0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.load_time_stage_2 "Permalink to this definition")
Time in seconds to parse the data from the contiguous string (or mmap equivalent).

sheets()[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.sheets "Permalink to this definition")Returns
A list of all sheets in the book.

All sheets not already loaded will be loaded.

sheet_by_index(_sheetx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.sheet_by_index "Permalink to this definition")Parameters
**sheetx** – Sheet index in `range(nsheets)`

Returns
A [`Sheet`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet "xlrd.sheet.Sheet").

sheet_by_name(_sheet\_name_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.sheet_by_name "Permalink to this definition")Parameters
**sheet_name** – Name of the sheet required.

Returns
A [`Sheet`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet "xlrd.sheet.Sheet").

sheet_names()[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.sheet_names "Permalink to this definition")Returns
A list of the names of all the worksheets in the workbook file. This information is available even when no sheets have yet been loaded.

sheet_loaded(_sheet\_name\_or\_index_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.sheet_loaded "Permalink to this definition")Parameters
**sheet_name_or_index** – Name or index of sheet enquired upon

Returns
`True` if sheet is loaded, `False` otherwise.

New in version 0.7.1.

unload_sheet(_sheet\_name\_or\_index_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.unload_sheet "Permalink to this definition")Parameters
**sheet_name_or_index** – Name or index of sheet to be unloaded.

New in version 0.7.1.

release_resources()[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.release_resources "Permalink to this definition")
This method has a dual purpose. You can call it to release memory-consuming objects and (possibly) a memory-mapped file ([`mmap.mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "(in Python v3.9)") object) when you have finished loading sheets in `on_demand` mode, but still require the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") object to examine the loaded sheets. It is also called automatically (a) when [`open_workbook()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "xlrd.open_workbook") raises an exception and (b) if you are using a `with` statement, when the `with` block is exited. Calling this method multiple times on the same object has no ill effect.

name_and_scope_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.name_and_scope_map "Permalink to this definition")A mapping from `(lower_case_name, scope)` to a single [`Name`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name "xlrd.book.Name")
object.

New in version 0.6.0.

name_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.name_map "Permalink to this definition")
A mapping from lower_case_name to a list of [`Name`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name "xlrd.book.Name") objects. The list is sorted in scope order. Typically there will be one item (of global scope) in the list.

New in version 0.6.0.

nsheets _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.nsheets "Permalink to this definition")
The number of worksheets present in the workbook file. This information is available even when no sheets have yet been loaded.

name_obj_list _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.name_obj_list "Permalink to this definition")
List containing a [`Name`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Name "xlrd.book.Name") object for each `NAME` record in the workbook.

New in version 0.6.0.

colour_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.colour_map "Permalink to this definition")
This provides definitions for colour indexes. Please refer to [The Palette; Colour Indexes](https://xlrd.readthedocs.io/en/latest/formatting.html#palette) for an explanation of how colours are represented in Excel.

Colour indexes into the palette map into `(red, green, blue)` tuples. “Magic” indexes e.g. `0x7FFF` map to `None`.

[`colour_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.colour_map "xlrd.book.Book.colour_map") is what you need if you want to render cells on screen or in a PDF file. If you are writing an output XLS file, use [`palette_record`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.palette_record "xlrd.book.Book.palette_record").

Note

Extracted only if `open_workbook(..., formatting_info=True)`

New in version 0.6.1.

palette_record _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.palette_record "Permalink to this definition")
If the user has changed any of the colours in the standard palette, the XLS file will contain a `PALETTE` record with 56 (16 for Excel 4.0 and earlier) RGB values in it, and this list will be e.g. `[(r0, b0, g0), ..., (r55, b55, g55)]`. Otherwise this list will be empty. This is what you need if you are writing an output XLS file. If you want to render cells on screen or in a PDF file, use [`colour_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.colour_map "xlrd.book.Book.colour_map").

Note

Extracted only if `open_workbook(..., formatting_info=True)`

New in version 0.6.1.

xf_list _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.xf_list "Permalink to this definition")
A list of [`XF`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF "xlrd.formatting.XF") class instances, each corresponding to an `XF` record.

New in version 0.6.1.

style_name_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.style_name_map "Permalink to this definition")
This provides access via name to the extended format information for both built-in styles and user-defined styles.

It maps `name` to `(built_in, xf_index)`, where `name` is either the name of a user-defined style, or the name of one of the built-in styles. Known built-in names are Normal, RowLevel_1 to RowLevel_7, ColLevel_1 to ColLevel_7, Comma, Currency, Percent, “Comma [0]”, “Currency [0]”, Hyperlink, and “Followed Hyperlink”.

`built_in` has the following meanings

1:
built-in style

0:
user-defined

`xf_index` is an index into [`Book.xf_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.xf_list "xlrd.book.Book.xf_list").

References: OOo docs s6.99 (`STYLE` record); Excel UI Format/Style

New in version 0.6.1.

Extracted only if `open_workbook(..., formatting_info=True)`

New in version 0.7.4.

xlrd.book.unpack_SST_table(_datatab_, _nstrings_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.unpack_SST_table "Permalink to this definition")
Return list of strings

xlrd.compdoc[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.compdoc "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

Implements the minimal functionality required to extract a “Workbook” or “Book” stream (as one big string) from an OLE2 Compound Document file.

xlrd.compdoc.SIGNATURE _=b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.compdoc.SIGNATURE "Permalink to this definition")
Magic cookie that should appear in the first 8 bytes of the file.

_exception_ xlrd.compdoc.CompDocError[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.compdoc.CompDocError "Permalink to this definition")_class_ xlrd.compdoc.CompDoc(_mem_, _logfile=<\_io.TextIOWrapper name='<stdout>'mode='w'encoding='utf-8'>_, _DEBUG=0_, _ignore\_workbook\_corruption=False_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.compdoc.CompDoc "Permalink to this definition")
Compound document handler.

Parameters
**mem** – The raw contents of the file, as a string, or as an [`mmap.mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "(in Python v3.9)") object. The only operation it needs to support is slicing.

get_named_stream(_qname_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.compdoc.CompDoc.get_named_stream "Permalink to this definition")
Interrogate the compound document’s directory; return the stream as a string if found, otherwise return `None`.

Parameters
**qname** – Name of the desired stream e.g. `'Workbook'`. Should be in Unicode or convertible thereto.

locate_named_stream(_qname_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.compdoc.CompDoc.locate_named_stream "Permalink to this definition")
Interrogate the compound document’s directory.

If the named stream is not found, `(None, 0, 0)` will be returned.

If the named stream is found and is contiguous within the original byte sequence (`mem`) used when the document was opened, then `(mem, offset_to_start_of_stream, length_of_stream)` is returned.

Otherwise a new string is built from the fragments and `(new_string, 0, length_of_stream)` is returned.

Parameters
**qname** – Name of the desired stream e.g. `'Workbook'`. Should be in Unicode or convertible thereto.

xlrd.formatting[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.formatting "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------

Module for formatting information.

xlrd.formatting.nearest_colour_index(_colour\_map_, _rgb_, _debug=0_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.nearest_colour_index "Permalink to this definition")
General purpose function. Uses Euclidean distance. So far used only for pre-BIFF8 `WINDOW2` record. Doesn’t have to be fast. Doesn’t have to be fancy.

_class_ xlrd.formatting.EqNeAttrs[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.EqNeAttrs "Permalink to this definition")
This mixin class exists solely so that [`Format`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format "xlrd.formatting.Format"), [`Font`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font "xlrd.formatting.Font"), and [`XF`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF "xlrd.formatting.XF") objects can be compared by value of their attributes.

_class_ xlrd.formatting.Font[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font "Permalink to this definition")
An Excel “font” contains the details of not only what is normally considered a font, but also several other display attributes. Items correspond to those in the Excel UI’s Format -> Cells -> Font tab.

New in version 0.6.1.

bold _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.bold "Permalink to this definition")
1 = Characters are bold. Redundant; see “weight” attribute.

character_set _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.character_set "Permalink to this definition")
Values:

0 = ANSI Latin
1 = System default
2 = Symbol,
77 = Apple Roman,
128 = ANSI Japanese Shift-JIS,
129 = ANSI Korean (Hangul),
130 = ANSI Korean (Johab),
134 = ANSI Chinese Simplified GBK,
136 = ANSI Chinese Traditional BIG5,
161 = ANSI Greek,
162 = ANSI Turkish,
163 = ANSI Vietnamese,
177 = ANSI Hebrew,
178 = ANSI Arabic,
186 = ANSI Baltic,
204 = ANSI Cyrillic,
222 = ANSI Thai,
238 = ANSI Latin II (Central European),
255 = OEM Latin I

colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.colour_index "Permalink to this definition")
An explanation of “colour index” is given in [The Palette; Colour Indexes](https://xlrd.readthedocs.io/en/latest/formatting.html#palette).

escapement _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.escapement "Permalink to this definition")
1 = Superscript, 2 = Subscript.

family _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.family "Permalink to this definition")
Values:

0 = None (unknown or don't care)
1 = Roman (variable width, serifed)
2 = Swiss (variable width, sans-serifed)
3 = Modern (fixed width, serifed or sans-serifed)
4 = Script (cursive)
5 = Decorative (specialised, for example Old English, Fraktur)

font_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.font_index "Permalink to this definition")
The 0-based index used to refer to this Font() instance. Note that index 4 is never used; xlrd supplies a dummy place-holder.

height _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.height "Permalink to this definition")
Height of the font (in twips). A twip = 1/20 of a point.

italic _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.italic "Permalink to this definition")
1 = Characters are italic.

name _=''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.name "Permalink to this definition")
The name of the font. Example: `"Arial"`.

struck_out _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.struck_out "Permalink to this definition")
1 = Characters are struck out.

underline_type _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.underline_type "Permalink to this definition")
Values:

0 = None
1 = Single;  0x21 (33) = Single accounting
2 = Double;  0x22 (34) = Double accounting

underlined _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.underlined "Permalink to this definition")
1 = Characters are underlined. Redundant; see [`underline_type`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.underline_type "xlrd.formatting.Font.underline_type") attribute.

weight _=400_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.weight "Permalink to this definition")
Font weight (100-1000). Standard values are 400 for normal text and 700 for bold text.

outline _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.outline "Permalink to this definition")
1 = Font is outline style (Macintosh only)

shadow _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Font.shadow "Permalink to this definition")
1 = Font is shadow style (Macintosh only)

_class_ xlrd.formatting.Format(_format\_key_, _ty_, _format\_str_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format "Permalink to this definition")
“Number format” information from a `FORMAT` record.

New in version 0.6.1.

format_key _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format.format_key "Permalink to this definition")
The key into [`format_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.format_map "xlrd.book.Book.format_map")

type _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format.type "Permalink to this definition")
A classification that has been inferred from the format string. Currently, this is used only to distinguish between numbers and dates. Values:

FUN = 0 # unknown
FDT = 1 # date
FNU = 2 # number
FGE = 3 # general
FTX = 4 # text

format_str _=''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.Format.format_str "Permalink to this definition")
The format string

xlrd.formatting.fmt_bracketed_sub(_repl_, _string_, _count=0_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.fmt_bracketed_sub "Permalink to this definition")
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.

_class_ xlrd.formatting.XFBorder[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder "Permalink to this definition")
A collection of the border-related attributes of an `XF` record. Items correspond to those in the Excel UI’s Format -> Cells -> Border tab.

An explanations of “colour index” is given in [The Palette; Colour Indexes](https://xlrd.readthedocs.io/en/latest/formatting.html#palette).

There are five line style attributes; possible values and the associated meanings are:

0 = No line,
1 = Thin,
2 = Medium,
3 = Dashed,
4 = Dotted,
5 = Thick,
6 = Double,
7 = Hair,
8 = Medium dashed,
9 = Thin dash-dotted,
10 = Medium dash-dotted,
11 = Thin dash-dot-dotted,
12 = Medium dash-dot-dotted,
13 = Slanted medium dash-dotted.

The line styles 8 to 13 appear in BIFF8 files (Excel 97 and later) only. For pictures of the line styles, refer to OOo docs s3.10 (p22) “Line Styles for Cell Borders (BIFF3-BIFF8)”.</p>

New in version 0.6.1.

top_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.top_colour_index "Permalink to this definition")
The colour index for the cell’s top line

bottom_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.bottom_colour_index "Permalink to this definition")
The colour index for the cell’s bottom line

left_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.left_colour_index "Permalink to this definition")
The colour index for the cell’s left line

right_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.right_colour_index "Permalink to this definition")
The colour index for the cell’s right line

diag_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.diag_colour_index "Permalink to this definition")
The colour index for the cell’s diagonal lines, if any

top_line_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.top_line_style "Permalink to this definition")
The line style for the cell’s top line

bottom_line_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.bottom_line_style "Permalink to this definition")
The line style for the cell’s bottom line

left_line_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.left_line_style "Permalink to this definition")
The line style for the cell’s left line

right_line_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.right_line_style "Permalink to this definition")
The line style for the cell’s right line

diag_line_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.diag_line_style "Permalink to this definition")
The line style for the cell’s diagonal lines, if any

diag_down _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.diag_down "Permalink to this definition")
1 = draw a diagonal from top left to bottom right

diag_up _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder.diag_up "Permalink to this definition")
1 = draw a diagonal from bottom left to top right

_class_ xlrd.formatting.XFBackground[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBackground "Permalink to this definition")
A collection of the background-related attributes of an `XF` record. Items correspond to those in the Excel UI’s Format -> Cells -> Patterns tab.

An explanations of “colour index” is given in [The Palette; Colour Indexes](https://xlrd.readthedocs.io/en/latest/formatting.html#palette).

New in version 0.6.1.

fill_pattern _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBackground.fill_pattern "Permalink to this definition")
See section 3.11 of the OOo docs.

background_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBackground.background_colour_index "Permalink to this definition")
See section 3.11 of the OOo docs.

pattern_colour_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBackground.pattern_colour_index "Permalink to this definition")
See section 3.11 of the OOo docs.

_class_ xlrd.formatting.XFAlignment[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment "Permalink to this definition")
A collection of the alignment and similar attributes of an `XF` record. Items correspond to those in the Excel UI’s Format -> Cells -> Alignment tab.

New in version 0.6.1.

hor_align _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.hor_align "Permalink to this definition")
Values: section 6.115 (p 214) of OOo docs

vert_align _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.vert_align "Permalink to this definition")
Values: section 6.115 (p 215) of OOo docs

rotation _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.rotation "Permalink to this definition")
Values: section 6.115 (p 215) of OOo docs.

Note

file versions BIFF7 and earlier use the documented `orientation` attribute; this will be mapped (without loss) into [`rotation`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.rotation "xlrd.formatting.XFAlignment.rotation").

text_wrapped _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.text_wrapped "Permalink to this definition")
1 = text is wrapped at right margin

indent_level _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.indent_level "Permalink to this definition")
A number in `range(15)`.

shrink_to_fit _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.shrink_to_fit "Permalink to this definition")
1 = shrink font size to fit text into cell.

text_direction _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment.text_direction "Permalink to this definition")
0 = according to context; 1 = left-to-right; 2 = right-to-left

_class_ xlrd.formatting.XFProtection[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFProtection "Permalink to this definition")
A collection of the protection-related attributes of an `XF` record. Items correspond to those in the Excel UI’s Format -> Cells -> Protection tab. Note the OOo docs include the “cell or style” bit in this bundle of attributes. This is incorrect; the bit is used in determining which bundles to use.

New in version 0.6.1.

cell_locked _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFProtection.cell_locked "Permalink to this definition")
1 = Cell is prevented from being changed, moved, resized, or deleted (only if the sheet is protected).

formula_hidden _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFProtection.formula_hidden "Permalink to this definition")
1 = Hide formula so that it doesn’t appear in the formula bar when the cell is selected (only if the sheet is protected).

_class_ xlrd.formatting.XF[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF "Permalink to this definition")
eXtended Formatting information for cells, rows, columns and styles.

Each of the 6 flags below describes the validity of a specific group of attributes.

In cell XFs:

*   `flag==0` means the attributes of the parent style `XF` are used, (but only if the attributes are valid there);

*   `flag==1` means the attributes of this `XF` are used.

In style XFs:

*   `flag==0` means the attribute setting is valid;

*   `flag==1` means the attribute should be ignored.

Note

the API provides both “raw” XFs and “computed” XFs. In the latter case, cell XFs have had the above inheritance mechanism applied.

New in version 0.6.1.

is_style _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.is_style "Permalink to this definition")
0 = cell XF, 1 = style XF

parent_style_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.parent_style_index "Permalink to this definition")
cell XF: Index into Book.xf_list of this XF’s style XF

style XF: 0xFFF

xf_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.xf_index "Permalink to this definition")
Index into [`xf_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.xf_list "xlrd.book.Book.xf_list")

font_index _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.font_index "Permalink to this definition")
Index into [`font_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.font_list "xlrd.book.Book.font_list")

format_key _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.format_key "Permalink to this definition")
Key into [`format_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.format_map "xlrd.book.Book.format_map")

Warning

OOo docs on the XF record call this “Index to FORMAT record”. It is not an index in the Python sense. It is a key to a map. It is true _only_ for Excel 4.0 and earlier files that the key into format_map from an XF instance is the same as the index into format_list, and _only_ if the index is less than 164.

protection _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.protection "Permalink to this definition")
An instance of an [`XFProtection`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFProtection "xlrd.formatting.XFProtection") object.

background _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.background "Permalink to this definition")
An instance of an [`XFBackground`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBackground "xlrd.formatting.XFBackground") object.

alignment _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.alignment "Permalink to this definition")
An instance of an [`XFAlignment`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFAlignment "xlrd.formatting.XFAlignment") object.

border _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF.border "Permalink to this definition")
An instance of an [`XFBorder`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XFBorder "xlrd.formatting.XFBorder") object.

xlrd.formula[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.formula "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

Module for parsing/evaluating Microsoft Excel formulas.

xlrd.formula.rangename3d(_book_, _ref3d_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.rangename3d "Permalink to this definition")
Utility function: `Ref3D(1, 4, 5, 20, 7, 10)` =>`'Sheet2:Sheet3!$H$6:$J$20'` (assuming Excel’s default sheetnames)

xlrd.formula.rangename3drel(_book_, _ref3d_, _browx=None_, _bcolx=None_, _r1c1=0_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.rangename3drel "Permalink to this definition")
Utility function: `Ref3D(coords=(0, 1, -32, -22, -13, 13), relflags=(0, 0, 1, 1, 1, 1))`

In R1C1 mode =>`'Sheet1!R[-32]C[-13]:R[-23]C[12]'`

In A1 mode => depends on base cell `(browx, bcolx)`

xlrd.formula.cellname(_rowx_, _colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.cellname "Permalink to this definition")
Utility function: `(5, 7)` =>`'H6'`

xlrd.formula.cellnameabs(_rowx_, _colx_, _r1c1=0_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.cellnameabs "Permalink to this definition")
Utility function: `(5, 7)` =>`'$H$6'`

xlrd.formula.colname(_colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.colname "Permalink to this definition")
Utility function: `7` =>`'H'`, `27` =>`'AB'`

_class_ xlrd.formula.Operand(_akind=None_, _avalue=None_, _arank=0_, _atext='?'_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.Operand "Permalink to this definition")
Used in evaluating formulas. The following table describes the kinds and how their values are represented.

| Kind symbol | Kind number | Value representation |
| --- | --- | --- |
| oBOOL | 3 | integer: 0 => False; 1 => True |
| oERR | 4 | None, or an int error code (same as XL_CELL_ERROR in the Cell class). |
| oMSNG | 5 | Used by Excel as a placeholder for a missing (not supplied) function argument. Should *not* appear as a final formula result. Value is None. |
| oNUM | 2 | A float. Note that there is no way of distinguishing dates. |
| oREF | -1 | The value is either None or a non-empty list of absolute Ref3D instances. |
| oREL | -2 | The value is None or a non-empty list of fully or partially relative Ref3D instances. |
| oSTRG | 1 | A Unicode string. |
| oUNK | 0 | The kind is unknown or ambiguous. The value is None |
kind _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.Operand.kind "Permalink to this definition")
oUNK means that the kind of operand is not known unambiguously.

value _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.Operand.value "Permalink to this definition")
None means that the actual value of the operand is a variable (depends on cell data), not a constant.

text _='?'_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.Operand.text "Permalink to this definition")
The reconstituted text of the original formula. Function names will be in English irrespective of the original language, which doesn’t seem to be recorded anywhere. The separator is “,”, not “;” or whatever else might be more appropriate for the end-user’s locale; patches welcome.

_class_ xlrd.formula.Ref3D(_atuple_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formula.Ref3D "Permalink to this definition")
Represents an absolute or relative 3-dimensional reference to a box of one or more cells.

The `coords` attribute is a tuple of the form:

(shtxlo, shtxhi, rowxlo, rowxhi, colxlo, colxhi)

where `0 <= thingxlo <= thingx < thingxhi`.

Note

It is quite possible to have `thingx > nthings`; for example `Print_Titles` could have `colxhi == 256` and/or `rowxhi == 65536` irrespective of how many columns/rows are actually used in the worksheet. The caller will need to decide how to handle this situation. Keyword: [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.9)") :-)

The components of the coords attribute are also available as individual attributes: `shtxlo`, `shtxhi`, `rowxlo`, `rowxhi`, `colxlo`, and `colxhi`.

The `relflags` attribute is a 6-tuple of flags which indicate whether the corresponding (sheet|row|col)(lo|hi) is relative (1) or absolute (0).

Note

There is necessarily no information available as to what cell(s) the reference could possibly be relative to. The caller must decide what if any use to make of `oREL` operands.

New in version 0.6.0.

xlrd.sheet[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd-sheet "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

_class_ xlrd.sheet.Sheet(_book_, _position_, _name_, _number_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet "Permalink to this definition")
Contains the data for one worksheet.

In the cell access functions, `rowx` is a row index, counting from zero, and `colx` is a column index, counting from zero. Negative values for row/column indexes and slice positions are supported in the expected fashion.

For information about cell types and cell values, refer to the documentation of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") class.

Warning

You don’t instantiate this class yourself. You access [`Sheet`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet "xlrd.sheet.Sheet") objects via the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") object that was returned when you called [`xlrd.open_workbook()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "xlrd.open_workbook").

col(_colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col "Permalink to this definition")
Returns a sequence of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") objects in the given column.

gcw[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.gcw "Permalink to this definition")
A 256-element tuple corresponding to the contents of the GCW record for this sheet. If no such record, treat as all bits zero. Applies to BIFF4-7 only. See docs of the [`Colinfo`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo "xlrd.sheet.Colinfo") class for discussion.

vert_split_pos _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.vert_split_pos "Permalink to this definition")
Number of columns in left pane (frozen panes; for split panes, see comments in code)

horz_split_pos _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.horz_split_pos "Permalink to this definition")
Number of rows in top pane (frozen panes; for split panes, see comments in code)

horz_split_first_visible _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.horz_split_first_visible "Permalink to this definition")
Index of first visible row in bottom frozen/split pane

vert_split_first_visible _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.vert_split_first_visible "Permalink to this definition")
Index of first visible column in right frozen/split pane

split_active_pane _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.split_active_pane "Permalink to this definition")
Frozen panes: ignore it. Split panes: explanation and diagrams in OOo docs.

has_pane_record _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.has_pane_record "Permalink to this definition")
Boolean specifying if a `PANE` record was present, ignore unless you’re `xlutils.copy`

book _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.book "Permalink to this definition")
A reference to the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") object to which this sheet belongs.

Example usage: `some_sheet.book.datemode`

name _=''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.name "Permalink to this definition")
Name of sheet.

nrows _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.nrows "Permalink to this definition")
Number of rows in sheet. A row index is in `range(thesheet.nrows)`.

ncols _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.ncols "Permalink to this definition")
Nominal number of columns in sheet. It is one more than the maximum column index found, ignoring trailing empty cells. See also the `ragged_rows` parameter to [`open_workbook()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "xlrd.open_workbook") and [`row_len()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_len "xlrd.sheet.Sheet.row_len").

defcolwidth _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.defcolwidth "Permalink to this definition")
Default column width from `DEFCOLWIDTH` record, else `None`. From the OOo docs:

> Column width in characters, using the width of the zero character from default font (first FONT record in the file). Excel adds some extra space to the default width, depending on the default font and default font size. The algorithm how to exactly calculate the resulting column width is not known. Example: The default width of 8 set in this record results in a column width of 8.43 using Arial font with a size of 10 points.

For the default hierarchy, refer to the [`Colinfo`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo "xlrd.sheet.Colinfo") class.

New in version 0.6.1.

standardwidth _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.standardwidth "Permalink to this definition")
Default column width from `STANDARDWIDTH` record, else `None`.

From the OOo docs:

> Default width of the columns in 1/256 of the width of the zero character, using default font (first FONT record in the file).

For the default hierarchy, refer to the [`Colinfo`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo "xlrd.sheet.Colinfo") class.

New in version 0.6.1.

default_row_height _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.default_row_height "Permalink to this definition")
Default value to be used for a row if there is no `ROW` record for that row. From the _optional_`DEFAULTROWHEIGHT` record.

default_row_height_mismatch _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.default_row_height_mismatch "Permalink to this definition")
Default value to be used for a row if there is no `ROW` record for that row. From the _optional_`DEFAULTROWHEIGHT` record.

default_row_hidden _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.default_row_hidden "Permalink to this definition")
Default value to be used for a row if there is no `ROW` record for that row. From the _optional_`DEFAULTROWHEIGHT` record.

default_additional_space_above _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.default_additional_space_above "Permalink to this definition")
Default value to be used for a row if there is no `ROW` record for that row. From the _optional_`DEFAULTROWHEIGHT` record.

default_additional_space_below _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.default_additional_space_below "Permalink to this definition")
Default value to be used for a row if there is no `ROW` record for that row. From the _optional_`DEFAULTROWHEIGHT` record.

colinfo_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.colinfo_map "Permalink to this definition")
The map from a column index to a [`Colinfo`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo "xlrd.sheet.Colinfo") object. Often there is an entry in `COLINFO` records for all column indexes in `range(257)`.

Note

xlrd ignores the entry for the non-existent 257th column.

On the other hand, there may be no entry for unused columns.

New in version 0.6.1.

Populated only if `open_workbook(..., formatting_info=True)`

rowinfo_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.rowinfo_map "Permalink to this definition")
The map from a row index to a [`Rowinfo`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo "xlrd.sheet.Rowinfo") object.

..note::
It is possible to have missing entries – at least one source of XLS files doesn’t bother writing `ROW` records.

New in version 0.6.1.

Populated only if `open_workbook(..., formatting_info=True)`

col_label_ranges _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col_label_ranges "Permalink to this definition")
List of address ranges of cells containing column labels. These are set up in Excel by Insert > Name > Labels > Columns.

New in version 0.6.0.

How to deconstruct the list:

for crange in thesheet.col_label_ranges:
    rlo, rhi, clo, chi = crange
    for rx in xrange(rlo, rhi):
        for cx in xrange(clo, chi):
            print "Column label at (rowx=%d, colx=%d) is %r" \
                (rx, cx, thesheet.cell_value(rx, cx))

row_label_ranges _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_label_ranges "Permalink to this definition")
List of address ranges of cells containing row labels. For more details, see [`col_label_ranges`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col_label_ranges "xlrd.sheet.Sheet.col_label_ranges").

New in version 0.6.0.

merged_cells _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.merged_cells "Permalink to this definition")
List of address ranges of cells which have been merged. These are set up in Excel by Format > Cells > Alignment, then ticking the “Merge cells” box.

Note

The upper limits are exclusive: i.e. `[2, 3, 7, 9]` only spans two cells.

Note

Extracted only if `open_workbook(..., formatting_info=True)`

New in version 0.6.1.

How to deconstruct the list:

for crange in thesheet.merged_cells:
    rlo, rhi, clo, chi = crange
    for rowx in xrange(rlo, rhi):
        for colx in xrange(clo, chi):
            # cell (rlo, clo) (the top left one) will carry the data
            # and formatting info; the remainder will be recorded as
            # blank cells, but a renderer will apply the formatting info
            # for the top left cell (e.g. border, pattern) to all cells in
            # the range.

rich_text_runlist_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.rich_text_runlist_map "Permalink to this definition")
Mapping of `(rowx, colx)` to list of `(offset, font_index)` tuples. The offset defines where in the string the font begins to be used. Offsets are expected to be in ascending order. If the first offset is not zero, the meaning is that the cell’s `XF`’s font should be used from offset 0.

This is a sparse mapping. There is no entry for cells that are not formatted with rich text.

How to use:

runlist = thesheet.rich_text_runlist_map.get((rowx, colx))
if runlist:
    for offset, font_index in runlist:
        # do work here.
        pass

New in version 0.7.2.

Populated only if `open_workbook(..., formatting_info=True)`

horizontal_page_breaks _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.horizontal_page_breaks "Permalink to this definition")
A list of the horizontal page breaks in this sheet. Breaks are tuples in the form `(index of row after break, start col index, end col index)`.

Populated only if `open_workbook(..., formatting_info=True)`

New in version 0.7.2.

vertical_page_breaks _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.vertical_page_breaks "Permalink to this definition")
A list of the vertical page breaks in this sheet. Breaks are tuples in the form `(index of col after break, start row index, end row index)`.

Populated only if `open_workbook(..., formatting_info=True)`

New in version 0.7.2.

visibility _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.visibility "Permalink to this definition")
Visibility of the sheet:

0 = visible
1 = hidden (can be unhidden by user -- Format -> Sheet -> Unhide)
2 = "very hidden" (can be unhidden only by VBA macro).

hyperlink_list _=[]_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_list "Permalink to this definition")
A list of [`Hyperlink`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink "xlrd.sheet.Hyperlink") objects corresponding to `HLINK` records found in the worksheet.

New in version 0.7.2.

hyperlink_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_map "Permalink to this definition")
A sparse mapping from `(rowx, colx)` to an item in [`hyperlink_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_list "xlrd.sheet.Sheet.hyperlink_list"). Cells not covered by a hyperlink are not mapped. It is possible using the Excel UI to set up a hyperlink that covers a larger-than-1x1 rectangle of cells. Hyperlink rectangles may overlap (Excel doesn’t check). When a multiply-covered cell is clicked on, the hyperlink that is activated (and the one that is mapped here) is the last in [`hyperlink_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_list "xlrd.sheet.Sheet.hyperlink_list").

New in version 0.7.2.

cell_note_map _={}_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_note_map "Permalink to this definition")
A sparse mapping from `(rowx, colx)` to a [`Note`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note "xlrd.sheet.Note") object. Cells not containing a note (“comment”) are not mapped.

New in version 0.7.2.

cell(_rowx_, _colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell "Permalink to this definition")
[`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") object in the given row and column.

cell_value(_rowx_, _colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_value "Permalink to this definition")
Value of the cell in the given row and column.

cell_type(_rowx_, _colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_type "Permalink to this definition")
Type of the cell in the given row and column.

Refer to the documentation of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") class.

cell_xf_index(_rowx_, _colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_xf_index "Permalink to this definition")
XF index of the cell in the given row and column. This is an index into [`xf_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.xf_list "xlrd.book.Book.xf_list").

New in version 0.6.1.

row_len(_rowx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_len "Permalink to this definition")
Returns the effective number of cells in the given row. For use with `open_workbook(ragged_rows=True)` which is likely to produce rows with fewer than [`ncols`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.ncols "xlrd.sheet.Sheet.ncols") cells.

New in version 0.7.2.

row(_rowx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row "Permalink to this definition")
Returns a sequence of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") objects in the given row.

get_rows()[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.get_rows "Permalink to this definition")
Returns a generator for iterating through each row.

row_types(_rowx_, _start\_colx=0_, _end\_colx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_types "Permalink to this definition")
Returns a slice of the types of the cells in the given row.

row_values(_rowx_, _start\_colx=0_, _end\_colx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_values "Permalink to this definition")
Returns a slice of the values of the cells in the given row.

row_slice(_rowx_, _start\_colx=0_, _end\_colx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.row_slice "Permalink to this definition")
Returns a slice of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") objects in the given row.

col_slice(_colx_, _start\_rowx=0_, _end\_rowx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col_slice "Permalink to this definition")
Returns a slice of the [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") objects in the given column.

col_values(_colx_, _start\_rowx=0_, _end\_rowx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col_values "Permalink to this definition")
Returns a slice of the values of the cells in the given column.

col_types(_colx_, _start\_rowx=0_, _end\_rowx=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.col_types "Permalink to this definition")
Returns a slice of the types of the cells in the given column.

computed_column_width(_colx_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.computed_column_width "Permalink to this definition")
Determine column display width.

Parameters
**colx** – Index of the queried column, range 0 to 255. Note that it is possible to find out the width that will be used to display columns with no cell information e.g. column IV (colx=255).

Returns
The column width that will be used for displaying the given column by Excel, in units of 1/256th of the width of a standard character (the digit zero in the first font).

New in version 0.6.1.

_class_ xlrd.sheet.MSODrawing[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.MSODrawing "Permalink to this definition")_class_ xlrd.sheet.MSObj[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.MSObj "Permalink to this definition")_class_ xlrd.sheet.MSTxo[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.MSTxo "Permalink to this definition")_class_ xlrd.sheet.Note[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note "Permalink to this definition")
Represents a user “comment” or “note”. Note objects are accessible through [`Sheet.cell_note_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.cell_note_map "xlrd.sheet.Sheet.cell_note_map").

New in version 0.7.2.

Author of note

col_hidden _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.col_hidden "Permalink to this definition")
`True` if the containing column is hidden

colx _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.colx "Permalink to this definition")
Column index

rich_text_runlist _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.rich_text_runlist "Permalink to this definition")
List of `(offset_in_string, font_index)` tuples. Unlike [`Sheet.rich_text_runlist_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.rich_text_runlist_map "xlrd.sheet.Sheet.rich_text_runlist_map"), the first offset should always be 0.

row_hidden _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.row_hidden "Permalink to this definition")
True if the containing row is hidden

rowx _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.rowx "Permalink to this definition")
Row index

show _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.show "Permalink to this definition")
True if note is always shown

text _=''_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Note.text "Permalink to this definition")
Text of the note

_class_ xlrd.sheet.Hyperlink[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink "Permalink to this definition")
Contains the attributes of a hyperlink. Hyperlink objects are accessible through [`Sheet.hyperlink_list`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_list "xlrd.sheet.Sheet.hyperlink_list") and [`Sheet.hyperlink_map`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.hyperlink_map "xlrd.sheet.Sheet.hyperlink_map").

New in version 0.7.2.

frowx _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.frowx "Permalink to this definition")
Index of first row

lrowx _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.lrowx "Permalink to this definition")
Index of last row

fcolx _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.fcolx "Permalink to this definition")
Index of first column

lcolx _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.lcolx "Permalink to this definition")
Index of last column

type _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.type "Permalink to this definition")
Type of hyperlink. Unicode string, one of ‘url’, ‘unc’, ‘local file’, ‘workbook’, ‘unknown’

url_or_path _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.url_or_path "Permalink to this definition")
The URL or file-path, depending in the type. Unicode string, except in the rare case of a local but non-existent file with non-ASCII characters in the name, in which case only the “8.3” filename is available, as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") (3.x) or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") (2.x) string, _with unknown encoding._

desc _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.desc "Permalink to this definition")
Description. This is displayed in the cell, and should be identical to the cell value. Unicode string, or `None`. It seems impossible NOT to have a description created by the Excel UI.

target _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.target "Permalink to this definition")
Target frame. Unicode string.

Note

No cases of this have been seen in the wild. It seems impossible to create one in the Excel UI.

textmark _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.textmark "Permalink to this definition")
The piece after the “#” in “[http://docs.python.org/library#struct_module](http://docs.python.org/library#struct_module)”, or the `Sheet1!A1:Z99` part when type is “workbook”.

quicktip _=None_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Hyperlink.quicktip "Permalink to this definition")
The text of the “quick tip” displayed when the cursor hovers over the hyperlink.

_class_ xlrd.sheet.Cell(_ctype_, _value_, _xf\_index=None_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "Permalink to this definition")
Contains the data for one cell.

Warning

You don’t call this class yourself. You access [`Cell`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Cell "xlrd.sheet.Cell") objects via methods of the [`Sheet`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet "xlrd.sheet.Sheet") object(s) that you found in the [`Book`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book "xlrd.book.Book") object that was returned when you called [`open_workbook()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.open_workbook "xlrd.open_workbook")

Cell objects have three attributes: `ctype` is an int, `value` (which depends on `ctype`) and `xf_index`. If `formatting_info` is not enabled when the workbook is opened, `xf_index` will be `None`.

The following table describes the types of cells and how their values are represented in Python.

| Type symbol | Type number | Python value |
| --- | --- | --- |
| XL_CELL_EMPTY | 0 | empty string '' |
| XL_CELL_TEXT | 1 | a Unicode string |
| XL_CELL_NUMBER | 2 | float |
| XL_CELL_DATE | 3 | float |
| XL_CELL_BOOLEAN | 4 | int; 1 means TRUE, 0 means FALSE |
| XL_CELL_ERROR | 5 | int representing internal Excel codes; for a text representation, refer to the supplied dictionary error_text_from_code |
| XL_CELL_BLANK | 6 | empty string ''. Note: this type will appear only when open_workbook(..., formatting_info=True) is used. |
_class_ xlrd.sheet.Colinfo[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo "Permalink to this definition")
Width and default formatting information that applies to one or more columns in a sheet. Derived from `COLINFO` records.

Here is the default hierarchy for width, according to the OOo docs:

> In BIFF3, if a `COLINFO` record is missing for a column, the width specified in the record `DEFCOLWIDTH` is used instead.
> 
> 
> In BIFF4-BIFF7, the width set in this `COLINFO` record is only used, if the corresponding bit for this column is cleared in the `GCW` record, otherwise the column width set in the `DEFCOLWIDTH` record is used (the `STANDARDWIDTH` record is always ignored in this case [1](https://xlrd.readthedocs.io/en/latest/api.html#f1)).
> 
> 
> In BIFF8, if a `COLINFO` record is missing for a column, the width specified in the record `STANDARDWIDTH` is used. If this `STANDARDWIDTH` record is also missing, the column width of the record `DEFCOLWIDTH` is used instead.

[1](https://xlrd.readthedocs.io/en/latest/api.html#id1)
The docs on the `GCW` record say this:

If a bit is set, the corresponding column uses the width set in the `STANDARDWIDTH` record. If a bit is cleared, the corresponding column uses the width set in the `COLINFO` record for this column.

If a bit is set, and the worksheet does not contain the `STANDARDWIDTH` record, or if the bit is cleared, and the worksheet does not contain the `COLINFO` record, the `DEFCOLWIDTH` record of the worksheet will be used instead.

xlrd goes with the GCW version of the story. Reference to the source may be useful: see [`Sheet.computed_column_width()`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Sheet.computed_column_width "xlrd.sheet.Sheet.computed_column_width").

New in version 0.6.1.

width _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.width "Permalink to this definition")
Width of the column in 1/256 of the width of the zero character, using default font (first `FONT` record in the file).

xf_index _=-1_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.xf_index "Permalink to this definition")
XF index to be used for formatting empty cells.

hidden _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.hidden "Permalink to this definition")
1 = column is hidden

bit1_flag _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.bit1_flag "Permalink to this definition")
Value of a 1-bit flag whose purpose is unknown but is often seen set to 1

outline_level _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.outline_level "Permalink to this definition")
Outline level of the column, in `range(7)`. (0 = no outline)

collapsed _=0_[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Colinfo.collapsed "Permalink to this definition")
1 = column is collapsed

_class_ xlrd.sheet.Rowinfo[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo "Permalink to this definition")
Height and default formatting information that applies to a row in a sheet. Derived from `ROW` records.

New in version 0.6.1.

height[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.height "Permalink to this definition")
Height of the row, in twips. One twip == 1/20 of a point.

has_default_height[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.has_default_height "Permalink to this definition")
0 = Row has custom height; 1 = Row has default height.

outline_level[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.outline_level "Permalink to this definition")
Outline level of the row (0 to 7)

outline_group_starts_ends[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.outline_group_starts_ends "Permalink to this definition")
1 = Outline group starts or ends here (depending on where the outline buttons are located, see `WSBOOL` record, which is not parsed by xlrd), _and_ is collapsed.

hidden[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.hidden "Permalink to this definition")
1 = Row is hidden (manually, or by a filter or outline group)

height_mismatch[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.height_mismatch "Permalink to this definition")
1 = Row height and default font height do not match.

has_default_xf_index[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.has_default_xf_index "Permalink to this definition")
1 = the xf_index attribute is usable; 0 = ignore it.

xf_index[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.xf_index "Permalink to this definition")
Index to default [`XF`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.formatting.XF "xlrd.formatting.XF") record for empty cells in this row. Don’t use this if `has_default_xf_index == 0`.

additional_space_above[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.additional_space_above "Permalink to this definition")
This flag is set if the upper border of at least one cell in this row or if the lower border of at least one cell in the row above is formatted with a thick line style. Thin and medium line styles are not taken into account.

additional_space_below[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.sheet.Rowinfo.additional_space_below "Permalink to this definition")
This flag is set if the lower border of at least one cell in this row or if the upper border of at least one cell in the row below is formatted with a medium or thick line style. Thin line styles are not taken into account.

xlrd.xldate[¶](https://xlrd.readthedocs.io/en/latest/api.html#module-xlrd.xldate "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

Tools for working with dates and times in Excel files.

The conversion from `days` to `(year, month, day)` starts with an integral “julian day number” aka JDN. FWIW:

*   JDN 0 corresponds to noon on Monday November 24 in Gregorian year -4713.

More importantly:

*   Noon on Gregorian 1900-03-01 (day 61 in the 1900-based system) is JDN 2415080.0

*   Noon on Gregorian 1904-01-02 (day 1 in the 1904-based system) is JDN 2416482.0

_exception_ xlrd.xldate.XLDateError[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateError "Permalink to this definition")
A base class for all datetime-related errors.

_exception_ xlrd.xldate.XLDateNegative[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateNegative "Permalink to this definition")
`xldate < 0.00`

_exception_ xlrd.xldate.XLDateAmbiguous[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateAmbiguous "Permalink to this definition")
The 1900 leap-year problem `(datemode == 0 and 1.0 <= xldate < 61.0)`

_exception_ xlrd.xldate.XLDateTooLarge[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateTooLarge "Permalink to this definition")
Gregorian year 10000 or later

_exception_ xlrd.xldate.XLDateBadDatemode[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadDatemode "Permalink to this definition")
`datemode` arg is neither 0 nor 1

_exception_ xlrd.xldate.XLDateBadTuple[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadTuple "Permalink to this definition")xlrd.xldate.xldate_as_tuple(_xldate_, _datemode_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate_as_tuple "Permalink to this definition")
Convert an Excel number (presumed to represent a date, a datetime or a time) into a tuple suitable for feeding to datetime or mx.DateTime constructors.

Parameters
*   **xldate** – The Excel number

*   **datemode** – 0: 1900-based, 1: 1904-based.

Raises
*   [**xlrd.xldate.XLDateNegative**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateNegative "xlrd.xldate.XLDateNegative") –

*   [**xlrd.xldate.XLDateAmbiguous**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateAmbiguous "xlrd.xldate.XLDateAmbiguous") –

*   [**xlrd.xldate.XLDateTooLarge**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateTooLarge "xlrd.xldate.XLDateTooLarge") –

*   [**xlrd.xldate.XLDateBadDatemode**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadDatemode "xlrd.xldate.XLDateBadDatemode") –

*   [**xlrd.xldate.XLDateError**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateError "xlrd.xldate.XLDateError") –

Returns
Gregorian `(year, month, day, hour, minute, nearest_second)`.

Warning

When using this function to interpret the contents of a workbook, you should pass in the [`datemode`](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.book.Book.datemode "xlrd.book.Book.datemode") attribute of that workbook. Whether the workbook has ever been anywhere near a Macintosh is irrelevant.

Special case

If `0.0 <= xldate < 1.0`, it is assumed to represent a time; `(0, 0, 0, hour, minute, second)` will be returned.

Note

`1904-01-01` is not regarded as a valid date in the `datemode==1` system; its “serial number” is zero.

xlrd.xldate.xldate_as_datetime(_xldate_, _datemode_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate_as_datetime "Permalink to this definition")
Convert an Excel date/time number into a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.9)") object.

Parameters
*   **xldate** – The Excel number

*   **datemode** – 0: 1900-based, 1: 1904-based.

Returns
A [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.9)") object.

xlrd.xldate.xldate_from_date_tuple(_date\_tuple_, _datemode_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate_from_date_tuple "Permalink to this definition")
Convert a date tuple (year, month, day) to an Excel date.

Parameters
*   **year** – Gregorian year.

*   **month** – `1 <= month <= 12`

*   **day** – `1 <= day <= last day of that (year, month)`

*   **datemode** – 0: 1900-based, 1: 1904-based.

Raises
*   [**xlrd.xldate.XLDateAmbiguous**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateAmbiguous "xlrd.xldate.XLDateAmbiguous") –

*   [**xlrd.xldate.XLDateBadDatemode**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadDatemode "xlrd.xldate.XLDateBadDatemode") –

*   [**xlrd.xldate.XLDateBadTuple**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadTuple "xlrd.xldate.XLDateBadTuple") – `(year, month, day)` is too early/late or has invalid component(s)

*   [**xlrd.xldate.XLDateError**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateError "xlrd.xldate.XLDateError") –

xlrd.xldate.xldate_from_time_tuple(_time\_tuple_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate_from_time_tuple "Permalink to this definition")
Convert a time tuple `(hour, minute, second)` to an Excel “date” value (fraction of a day).

Parameters
*   **hour** – `0 <= hour < 24`

*   **minute** – `0 <= minute < 60`

*   **second** – `0 <= second < 60`

Raises
[**xlrd.xldate.XLDateBadTuple**](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.XLDateBadTuple "xlrd.xldate.XLDateBadTuple") – Out-of-range hour, minute, or second

xlrd.xldate.xldate_from_datetime_tuple(_datetime\_tuple_, _datemode_)[¶](https://xlrd.readthedocs.io/en/latest/api.html#xlrd.xldate.xldate_from_datetime_tuple "Permalink to this definition")
Convert a datetime tuple `(year, month, day, hour, minute, second)` to an Excel date value. For more details, refer to other xldate_from_*_tuple functions.

Parameters
*   **datetime_tuple** – `(year, month, day, hour, minute, second)`

*   **datemode** – 0: 1900-based, 1: 1904-based.
