# Source: https://fiona.readthedocs.io/en/stable/fiona.html

Title: fiona package — Fiona documentation

URL Source: https://fiona.readthedocs.io/en/stable/fiona.html

Published Time: Mon, 16 Sep 2024 20:20:02 GMT

Markdown Content:
Subpackages[](https://fiona.readthedocs.io/en/stable/fiona.html#subpackages "Link to this heading")
----------------------------------------------------------------------------------------------------

*   [fiona.fio package](https://fiona.readthedocs.io/en/stable/fiona.fio.html)
    *   [Submodules](https://fiona.readthedocs.io/en/stable/fiona.fio.html#submodules)
    *   [fiona.fio.bounds module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.bounds)
    *   [fiona.fio.calc module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.calc)
    *   [fiona.fio.cat module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.cat)
    *   [fiona.fio.collect module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.collect)
    *   [fiona.fio.distrib module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.distrib)
    *   [fiona.fio.dump module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.dump)
    *   [fiona.fio.env module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.env)
    *   [fiona.fio.filter module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona-fio-filter-module)
    *   [fiona.fio.helpers module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.helpers)
        *   [`eval_feature_expression()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.eval_feature_expression)
        *   [`id_record()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.id_record)
        *   [`make_ld_context()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.make_ld_context)
        *   [`nullable()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.nullable)
        *   [`obj_gen()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.obj_gen)
        *   [`recursive_round()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.helpers.recursive_round)

    *   [fiona.fio.info module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.info)
    *   [fiona.fio.insp module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.insp)
    *   [fiona.fio.load module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.load)
    *   [fiona.fio.ls module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.ls)
    *   [fiona.fio.main module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.main)
        *   [`configure_logging()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.main.configure_logging)

    *   [fiona.fio.options module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.options)
        *   [`cb_key_val()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.options.cb_key_val)
        *   [`cb_layer()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.options.cb_layer)
        *   [`cb_multilayer()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.options.cb_multilayer)
        *   [`validate_multilayer_file_index()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.options.validate_multilayer_file_index)

    *   [fiona.fio.rm module](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio.rm)
    *   [Module contents](https://fiona.readthedocs.io/en/stable/fiona.fio.html#module-fiona.fio)
        *   [`with_context_env()`](https://fiona.readthedocs.io/en/stable/fiona.fio.html#fiona.fio.with_context_env)

Submodules[](https://fiona.readthedocs.io/en/stable/fiona.html#submodules "Link to this heading")
--------------------------------------------------------------------------------------------------

fiona.collection module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.collection "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

Collections provide file-like access to feature data.

_class_ fiona.collection.BytesCollection(_bytesbuf_, _**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.BytesCollection "Link to this definition")
Bases: [`Collection`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection "fiona.collection.Collection")

BytesCollection takes a buffer of bytes and maps that to a virtual file that can then be opened by fiona.

close()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.BytesCollection.close "Link to this definition")
Removes the virtual file associated with the class.

_class_ fiona.collection.Collection(_path_, _mode='r'_, _driver=None_, _schema=None_, _crs=None_, _encoding=None_, _layer=None_, _vsi=None_, _archive=None_, _enabled\_drivers=None_, _crs\_wkt=None_, _ignore\_fields=None_, _ignore\_geometry=False_, _include\_fields=None_, _wkt\_version=None_, _allow\_unsupported\_drivers=False_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection "Link to this definition")
Bases: `object`

A file-like interface to features of a vector dataset

Python text file objects are iterators over lines of a file. Fiona Collections are similar iterators (not lists!) over features represented as GeoJSON-like mappings.

_property_ bounds[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.bounds "Link to this definition")
Returns (minx, miny, maxx, maxy).

close()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.close "Link to this definition")
In append or write mode, flushes data to disk, then ends access.

_property_ closed[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.closed "Link to this definition")
`False` if data can be accessed, otherwise `True`.

_property_ crs[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.crs "Link to this definition")
The coordinate reference system (CRS) of the Collection.

_property_ crs_wkt[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.crs_wkt "Link to this definition")
Returns a WKT string.

_property_ driver[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.driver "Link to this definition")
Returns the name of the proper OGR driver.

filter(_*args_, _**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.filter "Link to this definition")
Returns an iterator over records, but filtered by a test for spatial intersection with the provided `bbox`, a (minx, miny, maxx, maxy) tuple or a geometry `mask`. An attribute filter can be set using an SQL `where` clause, which uses the [OGR SQL dialect](https://gdal.org/user/ogr_sql_dialect.html#where).

Positional arguments `stop` or `start, stop[, step]` allows iteration to skip over items or stop at a specific item.

Note: spatial filtering using `mask` may be inaccurate and returning all features overlapping the envelope of `mask`.

flush()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.flush "Link to this definition")
Flush the buffer.

get(_item_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.get "Link to this definition")get_tag_item(_key_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.get_tag_item "Link to this definition")
Returns tag item value

Parameters:
*   **key** (_str_) – The key for the metadata item to fetch.

*   **ns** (_str_ _,_ _optional_) – Used to select a namespace other than the default.

Return type:
str

guard_driver_mode()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.guard_driver_mode "Link to this definition")items(_*args_, _**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.items "Link to this definition")
Returns an iterator over FID, record pairs, optionally filtered by a test for spatial intersection with the provided `bbox`, a (minx, miny, maxx, maxy) tuple or a geometry `mask`. An attribute filter can be set using an SQL `where` clause, which uses the [OGR SQL dialect](https://gdal.org/user/ogr_sql_dialect.html#where).

Positional arguments `stop` or `start, stop[, step]` allows iteration to skip over items or stop at a specific item.

Note: spatial filtering using `mask` may be inaccurate and returning all features overlapping the envelope of `mask`.

keys(_*args_, _**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.keys "Link to this definition")
Returns an iterator over FIDs, optionally filtered by a test for spatial intersection with the provided `bbox`, a (minx, miny, maxx, maxy) tuple or a geometry `mask`. An attribute filter can be set using an SQL `where` clause, which uses the [OGR SQL dialect](https://gdal.org/user/ogr_sql_dialect.html#where).

Positional arguments `stop` or `start, stop[, step]` allows iteration to skip over items or stop at a specific item.

Note: spatial filtering using `mask` may be inaccurate and returning all features overlapping the envelope of `mask`.

_property_ meta[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.meta "Link to this definition")
Returns a mapping with the driver, schema, crs, and additional properties.

next()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.next "Link to this definition")
Returns next record from iterator.

_property_ profile[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.profile "Link to this definition")
Returns a mapping with the driver, schema, crs, and additional properties.

_property_ schema[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.schema "Link to this definition")
Returns a mapping describing the data schema.

The mapping has ‘geometry’ and ‘properties’ items. The former is a string such as ‘Point’ and the latter is an ordered mapping that follows the order of fields in the data file.

tags(_ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.tags "Link to this definition")
Returns a dict containing copies of the dataset or layers’s tags. Tags are pairs of key and value strings. Tags belong to namespaces. The standard namespaces are: default (None) and ‘IMAGE_STRUCTURE’. Applications can create their own additional namespaces.

Parameters:
**ns** (_str_ _,_ _optional_) – Can be used to select a namespace other than the default.

Return type:
dict

update_tag_item(_key_, _tag_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.update_tag_item "Link to this definition")
Updates the tag item value

Parameters:
*   **key** (_str_) – The key for the metadata item to set.

*   **tag** (_str_) – The value of the metadata item to set.

*   **ns** (_str_ _,_ _optional_) – Used to select a namespace other than the default.

Return type:
int

update_tags(_tags_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.update_tags "Link to this definition")
Writes a dict containing the dataset or layers’s tags. Tags are pairs of key and value strings. Tags belong to namespaces. The standard namespaces are: default (None) and ‘IMAGE_STRUCTURE’. Applications can create their own additional namespaces.

Parameters:
*   **tags** (_dict_) – The dict of metadata items to set.

*   **ns** (_str_ _,_ _optional_) – Used to select a namespace other than the default.

Return type:
int

validate_record(_record_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.validate_record "Link to this definition")
Compares the record to the collection’s schema.

Returns `True` if the record matches, else `False`.

validate_record_geometry(_record_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.validate_record_geometry "Link to this definition")
Compares the record’s geometry to the collection’s schema.

Returns `True` if the record matches, else `False`.

values(_*args_, _**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.values "Link to this definition")
Returns an iterator over records, but filtered by a test for spatial intersection with the provided `bbox`, a (minx, miny, maxx, maxy) tuple or a geometry `mask`. An attribute filter can be set using an SQL `where` clause, which uses the [OGR SQL dialect](https://gdal.org/user/ogr_sql_dialect.html#where).

Positional arguments `stop` or `start, stop[, step]` allows iteration to skip over items or stop at a specific item.

Note: spatial filtering using `mask` may be inaccurate and returning all features overlapping the envelope of `mask`.

write(_record_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.write "Link to this definition")
Stages a record for writing to disk.

Note: Each call of this method will start and commit a unique transaction with the data source.

writerecords(_records_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection.writerecords "Link to this definition")
Stages multiple records for writing to disk.

fiona.collection.get_filetype(_bytesbuf_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.get_filetype "Link to this definition")
Detect compression type of bytesbuf.

ZIP only. TODO: add others relevant to GDAL/OGR.

fiona.compat module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.compat "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

fiona.compat.strencode(_instr_, _encoding='utf-8'_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.compat.strencode "Link to this definition")
fiona.crs module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.crs "Link to this heading")
--------------------------------------------------------------------------------------------------------------

Coordinate reference systems, the CRS class and supporting functions.

A coordinate reference system (CRS) defines how a dataset’s pixels map to locations on, for example, a globe or the Earth. A CRS may be local or global. The GIS field shares a number of authority files that define CRS. “EPSG:32618” is the name of a regional CRS from the European Petroleum Survey Group authority file. “OGC:CRS84” is the name of a global CRS from the Open Geospatial Consortium authority. Custom CRS can be described in text using several formats. Rasterio’s CRS class is our abstraction for coordinate reference systems.

A fiona.Collection’s crs property is an instance of CRS. CRS are also used to define transformations between coordinate reference systems. These transformations are performed by the PROJ library. Rasterio does not call PROJ functions directly, but invokes them via calls to GDAL’s “OSR*” functions.

_class_ fiona.crs.CRS(_initialdata=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "Link to this definition")
Bases: `object`

A geographic or projected coordinate reference system.

Added in version 1.9.0.

CRS objects may be created by passing PROJ parameters as keyword arguments to the standard constructor or by passing EPSG codes, PROJ mappings, PROJ strings, or WKT strings to the from_epsg, from_dict, from_string, or from_wkt static methods.

Examples

The from_dict method takes PROJ parameters as keyword arguments.

>>> crs = CRS.from_dict(proj="aea")

EPSG codes may be used with the from_epsg method.

>>> crs = CRS.from_epsg(3005)

The from_string method takes a variety of input.

>>> crs = CRS.from_string("EPSG:3005")

data[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.data "Link to this definition")
A PROJ4 dict representation of the CRS.

Make a CRS from an authority name and code.

Added in version 1.9.0.

Parameters:
*   **auth_name** (_str_) – The name of the authority.

*   **code** (_int_ _or_ _str_) – The code used by the authority.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_dict(_initialdata=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_dict "Link to this definition")
Make a CRS from a dict of PROJ parameters or PROJ JSON.

Parameters:
*   **initialdata** (_mapping_ _,_ _optional_) – A dictionary or other mapping

*   **kwargs** (_mapping_ _,_ _optional_) – Another mapping. Will be overlaid on the initialdata.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_epsg(_code_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_epsg "Link to this definition")
Make a CRS from an EPSG code.

Parameters:
**code** (_int_ _or_ _str_) – An EPSG code. Strings will be converted to integers.

Notes

The input code is not validated against an EPSG database.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_proj4(_proj_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_proj4 "Link to this definition")
Make a CRS from a PROJ4 string.

Parameters:
**proj** (_str_) – A PROJ4 string like “+proj=longlat …”

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_string(_value_, _morph\_from\_esri\_dialect=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_string "Link to this definition")
Make a CRS from an EPSG, PROJ, or WKT string

Parameters:
*   **value** (_str_) – An EPSG, PROJ, or WKT string.

*   **morph_from_esri_dialect** (_bool_ _,_ _optional_) – If True, items in the input using Esri’s dialect of WKT will be replaced by OGC standard equivalents.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_user_input(_value_, _morph\_from\_esri\_dialect=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_user_input "Link to this definition")
Make a CRS from a variety of inputs.

Parameters:
*   **value** (_object_) – User input of many different kinds.

*   **morph_from_esri_dialect** (_bool_ _,_ _optional_) – If True, items in the input using Esri’s dialect of WKT will be replaced by OGC standard equivalents.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

_static_ from_wkt(_wkt_, _morph\_from\_esri\_dialect=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.from_wkt "Link to this definition")
Make a CRS from a WKT string.

Parameters:
*   **wkt** (_str_) – A WKT string.

*   **morph_from_esri_dialect** (_bool_ _,_ _optional_) – If True, items in the input using Esri’s dialect of WKT will be replaced by OGC standard equivalents.

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

get(_self_, _item_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.get "Link to this definition")is_epsg_code[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.is_epsg_code "Link to this definition")
Test if the CRS is defined by an EPSG code.

Return type:
bool

is_geographic[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.is_geographic "Link to this definition")
Test if the CRS is a geographic coordinate reference system.

Return type:
bool

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

is_projected[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.is_projected "Link to this definition")
Test if the CRS is a projected coordinate reference system.

Return type:
bool

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

is_valid[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.is_valid "Link to this definition")
Test that the CRS is a geographic or projected CRS.

Return type:
bool

items(_self_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.items "Link to this definition")keys(_self_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.keys "Link to this definition")linear_units[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.linear_units "Link to this definition")
Get a short name for the linear units of the CRS.

Returns:
**units** – “m”, “ft”, etc.

Return type:
str

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

linear_units_factor[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.linear_units_factor "Link to this definition")
Get linear units and the conversion factor to meters of the CRS.

Returns:
*   **units** (_str_) – “m”, “ft”, etc.

*   **factor** (_float_) – Ratio of one unit to one meter.

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

to_authority(_self_, _confidence\_threshold=70_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_authority "Link to this definition")
Convert to the best match authority name and code.

For a CRS created using an EPSG code, that same value is returned. For other CRS, including custom CRS, an attempt is made to match it to definitions in authority files. Matches with a confidence below the threshold are discarded.

Parameters:
**confidence_threshold** (_int_) – Percent match confidence threshold (0-100).

Returns:
*   **name** (_str_) – Authority name.

*   **code** (_str_) – Code from the authority file.

*   _or None_

to_dict(_self_, _projjson=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_dict "Link to this definition")
Convert CRS to a PROJ dict.

Note

If there is a corresponding EPSG code, it will be used when returning PROJ parameter dict.

Added in version 1.9.0.

Parameters:
**projjson** (_bool_ _,_ _default=False_) – If True, will convert to PROJ JSON dict (Requites GDAL 3.1+ and PROJ 6.2+). If False, will convert to PROJ parameter dict.

Return type:
dict

to_epsg(_self_, _confidence\_threshold=70_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_epsg "Link to this definition")
Convert to the best match EPSG code.

For a CRS created using an EPSG code, that same value is returned. For other CRS, including custom CRS, an attempt is made to match it to definitions in the EPSG authority file. Matches with a confidence below the threshold are discarded.

Parameters:
**confidence_threshold** (_int_) – Percent match confidence threshold (0-100).

Return type:
int or None

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

to_proj4(_self_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_proj4 "Link to this definition")
Convert to a PROJ4 representation.

Return type:
str

to_string(_self_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_string "Link to this definition")
Convert to a PROJ4 or WKT string.

The output will be reduced as much as possible by attempting a match to CRS defined in authority files.

Notes

Mapping keys are tested against the `all_proj_keys` list. Values of `True` are omitted, leaving the key bare: {‘no_defs’: True} -> “+no_defs” and items where the value is otherwise not a str, int, or float are omitted.

Return type:
str

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

to_wkt(_self_, _morph\_to\_esri\_dialect=False_, _version=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.to_wkt "Link to this definition")
Convert to a OGC WKT representation.

Added in version 1.9.0.

Parameters:
*   **morph_to_esri_dialect** (_bool_ _,_ _optional_) – Whether or not to morph to the Esri dialect of WKT Only applies to GDAL versions < 3. This parameter will be removed in a future version of fiona (2.0.0).

*   **version** (_WktVersion_ _or_ _str_ _,_ _optional_) – The version of the WKT output. Defaults to GDAL’s default (WKT1_GDAL for GDAL 3).

Return type:
str

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

units_factor[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.units_factor "Link to this definition")
Get units and the conversion factor of the CRS.

Returns:
*   **units** (_str_) – “m”, “ft”, etc.

*   **factor** (_float_) – Ratio of one unit to one radian if the CRS is geographic otherwise, it is to one meter.

Raises:
[**CRSError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "fiona.errors.CRSError") –

values(_self_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.values "Link to this definition")wkt[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS.wkt "Link to this definition")
An OGC WKT representation of the CRS

Return type:
str

fiona.crs.epsg_treats_as_latlong(_input\_crs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.epsg_treats_as_latlong "Link to this definition")
Test if the CRS is in latlon order

Added in version 1.9.0.

From GDAL docs:

> This method returns TRUE if EPSG feels this geographic coordinate system should be treated as having lat/long coordinate ordering.

> Currently this returns TRUE for all geographic coordinate systems with an EPSG code set, and axes set defining it as lat, long.

> FALSE will be returned for all coordinate systems that are not geographic, or that do not have an EPSG code set.

>**Note**

> Important change of behavior since GDAL 3.0. In previous versions, geographic CRS imported with importFromEPSG() would cause this method to return FALSE on them, whereas now it returns TRUE, since importFromEPSG() is now equivalent to importFromEPSGA().

Parameters:
**input_crs** ([_CRS_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")) – Coordinate reference system, as a fiona CRS object Example: CRS({‘init’: ‘EPSG:4326’})

Return type:
bool

fiona.crs.epsg_treats_as_northingeasting(_input\_crs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.epsg_treats_as_northingeasting "Link to this definition")
Test if the CRS should be treated as having northing/easting coordinate ordering

Added in version 1.9.0.

From GDAL docs:

> This method returns TRUE if EPSG feels this projected coordinate system should be treated as having northing/easting coordinate ordering.

> Currently this returns TRUE for all projected coordinate systems with an EPSG code set, and axes set defining it as northing, easting.

> FALSE will be returned for all coordinate systems that are not projected, or that do not have an EPSG code set.

>**Note**

> Important change of behavior since GDAL 3.0. In previous versions, projected CRS with northing, easting axis order imported with importFromEPSG() would cause this method to return FALSE on them, whereas now it returns TRUE, since importFromEPSG() is now equivalent to importFromEPSGA().

Parameters:
**input_crs** ([_CRS_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")) – Coordinate reference system, as a fiona CRS object Example: CRS({‘init’: ‘EPSG:4326’})

Return type:
bool

fiona.crs.from_epsg(_val_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.from_epsg "Link to this definition")
Given an integer code, returns an EPSG-like mapping.

Deprecated since version 1.9.0: This function will be removed in version 2.0. Please use CRS.from_epsg() instead.

fiona.crs.from_string(_val_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.from_string "Link to this definition")
Turn a PROJ.4 string into a mapping of parameters.

Deprecated since version 1.9.0: This function will be removed in version 2.0. Please use CRS.from_string() instead.

fiona.crs.to_string(_val_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.to_string "Link to this definition")
Turn a parameter mapping into a more conventional PROJ.4 string.

Deprecated since version 1.9.0: This function will be removed in version 2.0. Please use CRS.to_string() instead.

fiona.drvsupport module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.drvsupport "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

fiona.drvsupport.driver_from_extension(_path_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.drvsupport.driver_from_extension "Link to this definition")
Attempt to auto-detect driver based on the extension.

Parameters:
**path** (_str_ _or_ _pathlike object_) – The path to the dataset to write with.

Returns:
The name of the driver for the extension.

Return type:
str

fiona.drvsupport.vector_driver_extensions()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.drvsupport.vector_driver_extensions "Link to this definition")Returns:
Map of extensions to the driver.

Return type:
dict

fiona.env module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.env "Link to this heading")
--------------------------------------------------------------------------------------------------------------

Fiona’s GDAL/AWS environment

_class_ fiona.env.Env(_session=None_, _aws\_unsigned=False_, _profile\_name=None_, _session\_class=<function Session.aws\_or\_dummy>_, _**options_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env "Link to this definition")
Bases: `object`

Abstraction for GDAL and AWS configuration

The GDAL library is stateful: it has a registry of format drivers, an error stack, and dozens of configuration options.

Fiona’s approach to working with GDAL is to wrap all the state up using a Python context manager (see PEP 343, [https://www.python.org/dev/peps/pep-0343/](https://www.python.org/dev/peps/pep-0343/)). When the context is entered GDAL drivers are registered, error handlers are configured, and configuration options are set. When the context is exited, drivers are removed from the registry and other configurations are removed.

Example

with fiona.Env(GDAL_CACHEMAX=512) as env:
# All drivers are registered, GDAL’s raster block cache # size is set to 512MB. # Commence processing… … # End of processing.

# At this point, configuration options are set to their # previous (possible unset) values.

A boto3 session or boto3 session constructor arguments aws_access_key_id, aws_secret_access_key, aws_session_token may be passed to Env’s constructor. In the latter case, a session will be created as soon as needed. AWS credentials are configured for GDAL as needed.

credentialize()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env.credentialize "Link to this definition")
Get credentials and configure GDAL

Note well: this method is a no-op if the GDAL environment already has credentials, unless session is not None.

Return type:
None

_classmethod_ default_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env.default_options "Link to this definition")
Default configuration options

Parameters:
**None**

Return type:
dict

drivers()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env.drivers "Link to this definition")
Return a mapping of registered drivers.

_classmethod_ from_defaults(_*args_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env.from_defaults "Link to this definition")
Create an environment with default config options

Parameters:
*   **args** (_optional_) – Positional arguments for Env()

*   **kwargs** (_optional_) – Keyword arguments for Env()

Return type:
[Env](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env "fiona.env.Env")

Notes

The items in kwargs will be overlaid on the default values.

_class_ fiona.env.GDALVersion(_major=0_, _minor=0_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion "Link to this definition")
Bases: `object`

Convenience class for obtaining GDAL major and minor version components and comparing between versions. This is highly simplistic and assumes a very normal numbering scheme for versions and ignores everything except the major and minor components.

at_least(_other_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion.at_least "Link to this definition")major[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion.major "Link to this definition")minor[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion.minor "Link to this definition")_classmethod_ parse(_input_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion.parse "Link to this definition")
Parses input tuple or string to GDALVersion. If input is a GDALVersion instance, it is returned.

Parameters:
**input** (_tuple_ _of_ _(_ _major_ _,_ _minor_ _)_ _,_ _string_ _, or_ _instance_ _of_[_GDALVersion_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion "fiona.env.GDALVersion"))

Return type:
GDALVersion instance

_classmethod_ runtime()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion.runtime "Link to this definition")
Return GDALVersion of current GDAL runtime

_class_ fiona.env.NullContextManager[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.NullContextManager "Link to this definition")
Bases: `object`

_class_ fiona.env.ThreadEnv[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.ThreadEnv "Link to this definition")
Bases: `_local`

fiona.env.defenv(_**options_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.defenv "Link to this definition")
Create a default environment if necessary.

fiona.env.delenv()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.delenv "Link to this definition")
Delete options in the existing environment.

fiona.env.ensure_env(_f_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.ensure_env "Link to this definition")
A decorator that ensures an env exists before a function calls any GDAL C functions.

Parameters:
**f** (_function_) – A function.

Return type:
A function wrapper.

Notes

If there is already an existing environment, the wrapper does nothing and immediately calls f with the given arguments.

fiona.env.ensure_env_with_credentials(_f_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.ensure_env_with_credentials "Link to this definition")
Ensures a config environment exists and has credentials.

Parameters:
**f** (_function_) – A function.

Return type:
A function wrapper.

Notes

The function wrapper checks the first argument of f and credentializes the environment if the first argument is a URI with scheme “s3”.

If there is already an existing environment, the wrapper does nothing and immediately calls f with the given arguments.

fiona.env.env_ctx_if_needed()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.env_ctx_if_needed "Link to this definition")
Return an Env if one does not exist

Return type:
[Env](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.Env "fiona.env.Env") or a do-nothing context manager

fiona.env.getenv()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.getenv "Link to this definition")
Get a mapping of current options.

fiona.env.hascreds()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.hascreds "Link to this definition")fiona.env.hasenv()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.hasenv "Link to this definition")fiona.env.require_gdal_version(_version_, _param=None_, _values=None_, _is\_max\_version=False_, _reason=''_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.require_gdal_version "Link to this definition")
A decorator that ensures the called function or parameters are supported by the runtime version of GDAL. Raises GDALVersionError if conditions are not met.

Examples: 

> @require_gdal_version(‘2.2’) def some_func():

calling some_func with a runtime version of GDAL that is < 2.2 raises a GDALVersionError.


@require_gdal_version(‘2.2’, param=’foo’) def some_func(foo=’bar’):

calling some_func with parameter foo of any value on GDAL < 2.2 raises a GDALVersionError.


@require_gdal_version(‘2.2’, param=’foo’, values=(‘bar’,)) def some_func(foo=None):

calling some_func with parameter foo and value bar on GDAL < 2.2 raises a GDALVersionError.

Parameters:
*   **version** (_tuple_ _,_ _string_ _, or_[_GDALVersion_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.GDALVersion "fiona.env.GDALVersion"))

*   **param** (_string_ _(_ _optional_ _,_ _default: None_ _)_) – If values are absent, then all use of this parameter with a value other than default value requires at least GDAL version.

*   **values** (_tuple_ _,_ _list_ _, or_ _set_ _(_ _optional_ _,_ _default: None_ _)_) – contains values that require at least GDAL version. param is required for values.

*   **is_max_version** (_bool_ _(_ _optional_ _,_ _default: False_ _)_) – if True indicates that the version provided is the maximum version allowed, instead of requiring at least that version.

*   **reason** (_string_ _(_ _optional: default: ''_ _)_) – custom error message presented to user in addition to message about GDAL version. Use this to provide an explanation of what changed if necessary context to the user.

Return type:
wrapped function

fiona.env.setenv(_**options_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.env.setenv "Link to this definition")
Set options in the existing environment.

fiona.errors module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.errors "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

_exception_ fiona.errors.AttributeFilterError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.AttributeFilterError "Link to this definition")
Bases: [`FionaValueError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "fiona.errors.FionaValueError")

Error processing SQL WHERE clause with the dataset.

_exception_ fiona.errors.CRSError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.CRSError "Link to this definition")
Bases: [`FionaValueError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "fiona.errors.FionaValueError")

When a crs mapping has neither init or proj items.

_exception_ fiona.errors.DataIOError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DataIOError "Link to this definition")
Bases: `OSError`

IO errors involving driver registration or availability.

_exception_ fiona.errors.DatasetDeleteError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DatasetDeleteError "Link to this definition")
Bases: `OSError`

Failure to delete a dataset

_exception_ fiona.errors.DriverError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DriverError "Link to this definition")
Bases: [`FionaValueError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "fiona.errors.FionaValueError")

Encapsulates unsupported driver and driver mode errors.

_exception_ fiona.errors.DriverIOError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DriverIOError "Link to this definition")
Bases: `OSError`

A format specific driver error.

_exception_ fiona.errors.DriverSupportError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DriverSupportError "Link to this definition")
Bases: [`DriverIOError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DriverIOError "fiona.errors.DriverIOError")

Driver does not support schema

_exception_ fiona.errors.EnvError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.EnvError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Environment Errors

_exception_ fiona.errors.FeatureWarning[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FeatureWarning "Link to this definition")
Bases: `UserWarning`

A warning about serialization of a feature

_exception_ fiona.errors.FieldNameEncodeError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FieldNameEncodeError "Link to this definition")
Bases: `UnicodeEncodeError`

Failure to encode a field name.

_exception_ fiona.errors.FionaDeprecationWarning[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaDeprecationWarning "Link to this definition")
Bases: `DeprecationWarning`

A warning about deprecation of Fiona features

_exception_ fiona.errors.FionaError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "Link to this definition")
Bases: `Exception`

Base Fiona error

_exception_ fiona.errors.FionaValueError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError"), `ValueError`

Fiona-specific value errors

_exception_ fiona.errors.GDALVersionError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.GDALVersionError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Raised if the runtime version of GDAL does not meet the required version of GDAL.

_exception_ fiona.errors.GeometryTypeValidationError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.GeometryTypeValidationError "Link to this definition")
Bases: [`FionaValueError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "fiona.errors.FionaValueError")

Tried to write a geometry type not specified in the schema

_exception_ fiona.errors.OpenerRegistrationError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.OpenerRegistrationError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Raised when a Python file opener can not be registered.

_exception_ fiona.errors.PathError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.PathError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Raised when a dataset path is malformed or invalid

_exception_ fiona.errors.ReduceError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.ReduceError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

“Raised when reduce operation fails.

_exception_ fiona.errors.SchemaError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.SchemaError "Link to this definition")
Bases: [`FionaValueError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaValueError "fiona.errors.FionaValueError")

When a schema mapping has no properties or no geometry.

_exception_ fiona.errors.TransactionError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.TransactionError "Link to this definition")
Bases: `RuntimeError`

Failure relating to GDAL transactions

_exception_ fiona.errors.TransformError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.TransformError "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Raised if a coordinate transformation fails.

_exception_ fiona.errors.UnsupportedGeometryTypeError[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.UnsupportedGeometryTypeError "Link to this definition")
Bases: `KeyError`

When a OGR geometry type isn’t supported by Fiona.

_exception_ fiona.errors.UnsupportedOperation[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.UnsupportedOperation "Link to this definition")
Bases: [`FionaError`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.FionaError "fiona.errors.FionaError")

Raised when reading from a file opened in ‘w’ mode

fiona.inspector module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.inspector "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

fiona.inspector.main(_srcfile_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.inspector.main "Link to this definition")
Open a dataset in an interactive session.

fiona.io module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.io "Link to this heading")
------------------------------------------------------------------------------------------------------------

Classes capable of reading and writing collections

_class_ fiona.io.MemoryFile(_file\_or\_bytes=None_, _filename=None_, _ext=''_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.MemoryFile "Link to this definition")
Bases: [`MemoryFileBase`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase "fiona.ogrext.MemoryFileBase")

A BytesIO-like object, backed by an in-memory file.

This allows formatted files to be read and written without I/O.

A MemoryFile created with initial bytes becomes immutable. A MemoryFile created without initial bytes may be written to using either file-like or dataset interfaces.

Parameters:
*   **file_or_bytes** (_an open Python file_ _,_ _bytes_ _, or_ _None_) – If not None, the MemoryFile becomes immutable and read-only. If None, it is write-only.

*   **filename** (_str_) – An optional filename. The default is a UUID-based name.

*   **ext** (_str_) – An optional file extension. Some format drivers require a specific value.

listdir(_path=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.MemoryFile.listdir "Link to this definition")
List files in a directory.

Parameters:
**path** (_URI_ _(_ _str_ _or_ _pathlib.Path_ _)_) – A dataset resource identifier.

Returns:
A list of filename strings.

Return type:
list

listlayers(_path=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.MemoryFile.listlayers "Link to this definition")
List layer names in their index order

Parameters:
**path** (_URI_ _(_ _str_ _or_ _pathlib.Path_ _)_) – A dataset resource identifier.

Returns:
A list of layer name strings.

Return type:
list

open(_mode=None_, _driver=None_, _schema=None_, _crs=None_, _encoding=None_, _layer=None_, _vfs=None_, _enabled\_drivers=None_, _crs\_wkt=None_, _allow\_unsupported\_drivers=False_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.MemoryFile.open "Link to this definition")
Open the file and return a Fiona collection object.

If data has already been written, the file is opened in ‘r’ mode. Otherwise, the file is opened in ‘w’ mode.

Parameters:
*   **parameter** (_Note well that there is no path_)

*   **a** (_contains a single dataset and there is no need to specify_)

*   **path.**

*   **the** (_Other parameters are optional and have the same semantics as_)

*   **fiona.open****(****)****.** (_parameters of_)

_class_ fiona.io.ZipMemoryFile(_file\_or\_bytes=None_, _filename=None_, _ext='.zip'_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.ZipMemoryFile "Link to this definition")
Bases: [`MemoryFile`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.MemoryFile "fiona.io.MemoryFile")

A read-only BytesIO-like object backed by an in-memory zip file.

This allows a zip file containing formatted files to be read without I/O.

Parameters:
*   **file_or_bytes** (_an open Python file_ _,_ _bytes_ _, or_ _None_) – If not None, the MemoryFile becomes immutable and read-only. If None, it is write-only.

*   **filename** (_str_) – An optional filename. The default is a UUID-based name.

*   **ext** (_str_) – An optional file extension. Some format drivers require a specific value. The default is “.zip”.

open(_path=None_, _driver=None_, _encoding=None_, _layer=None_, _enabled\_drivers=None_, _allow\_unsupported\_drivers=False_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.io.ZipMemoryFile.open "Link to this definition")
Open a dataset within the zipped stream.

Parameters:
**path** (_str_) – Path to a dataset in the zip file, relative to the root of the archive.

Return type:
A Fiona collection object

fiona.logutils module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.logutils "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

Logging helper classes.

_class_ fiona.logutils.FieldSkipLogFilter(_name=''_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.logutils.FieldSkipLogFilter "Link to this definition")
Bases: `Filter`

Filter field skip log messages.

At most, one message per field skipped per loop will be passed.

filter(_record_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.logutils.FieldSkipLogFilter.filter "Link to this definition")
Pass record if not seen.

_class_ fiona.logutils.LogFiltering(_logger_, _filter_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.logutils.LogFiltering "Link to this definition")
Bases: `object`

fiona.ogrext module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.ogrext "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Extension classes and functions using the OGR C API.

_class_ fiona.ogrext.AbstractField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "Link to this definition")
Bases: `object`

_class_ fiona.ogrext.BinaryField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.BinaryField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.BooleanField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.BooleanField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.DateField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.DateField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

Dates without time.

_class_ fiona.ogrext.DateTimeField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.DateTimeField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

Dates and times.

_class_ fiona.ogrext.FeatureBuilder[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.FeatureBuilder "Link to this definition")
Bases: `object`

Build Fiona features from OGR feature pointers.

No OGR objects are allocated by this function and the feature argument is not destroyed.

OGRPropertyGetter _={(0,0):<class'fiona.ogrext.IntegerField'>,(0,1):<class'fiona.ogrext.BooleanField'>,(0,2):<class'fiona.ogrext.Int16Field'>,(2,0):<class'fiona.ogrext.RealField'>,(4,0):<class'fiona.ogrext.StringField'>,(4,4):<class'fiona.ogrext.JSONField'>,(5,0):<class'fiona.ogrext.StringListField'>,(8,0):<class'fiona.ogrext.BinaryField'>,(9,0):<class'fiona.ogrext.DateField'>,(10,0):<class'fiona.ogrext.TimeField'>,(11,0):<class'fiona.ogrext.DateTimeField'>,(12,0):<class'fiona.ogrext.Integer64Field'>}_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.FeatureBuilder.OGRPropertyGetter "Link to this definition")_class_ fiona.ogrext.Int16Field[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Int16Field "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.Integer64Field[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Integer64Field "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.IntegerField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.IntegerField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.ItemsIterator[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.ItemsIterator "Link to this definition")
Bases: [`Iterator`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Iterator "fiona.ogrext.Iterator")

_class_ fiona.ogrext.Iterator[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Iterator "Link to this definition")
Bases: `object`

Provides iterated access to feature data.

_class_ fiona.ogrext.JSONField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.JSONField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.KeysIterator[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.KeysIterator "Link to this definition")
Bases: [`Iterator`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Iterator "fiona.ogrext.Iterator")

_class_ fiona.ogrext.MemoryFileBase[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase "Link to this definition")
Bases: `object`

Base for a BytesIO-like class backed by an in-memory file.

close()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.close "Link to this definition")
Close and tear down VSI file and directory.

exists()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.exists "Link to this definition")
Test if the in-memory file exists.

Returns:
True if the in-memory file exists.

Return type:
bool

getbuffer()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.getbuffer "Link to this definition")
Return a view on bytes of the file, or None.

read(_size=-1_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.read "Link to this definition")
Read size bytes from MemoryFile.

seek(_offset_, _whence=0_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.seek "Link to this definition")tell()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.tell "Link to this definition")write(_data_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.MemoryFileBase.write "Link to this definition")
Write data bytes to MemoryFile

_class_ fiona.ogrext.OGRFeatureBuilder[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.OGRFeatureBuilder "Link to this definition")
Bases: `object`

Builds an OGR Feature from a Fiona feature mapping.

Allocates one OGR Feature which should be destroyed by the caller. Borrows a layer definition from the collection.

OGRPropertySetter _={(0,0,'float'):<class'fiona.ogrext.RealField'>,(0,0,'int'):<class'fiona.ogrext.IntegerField'>,(0,0,'int32'):<class'fiona.ogrext.IntegerField'>,(0,0,'str'):<class'fiona.ogrext.StringField'>,(0,1,'bool'):<class'fiona.ogrext.BooleanField'>,(0,1,'int'):<class'fiona.ogrext.BooleanField'>,(0,2,'int'):<class'fiona.ogrext.Int16Field'>,(0,2,'str'):<class'fiona.ogrext.StringField'>,(2,0,'float'):<class'fiona.ogrext.RealField'>,(2,0,'str'):<class'fiona.ogrext.StringField'>,(2,3,'float'):<class'fiona.ogrext.RealField'>,(2,3,'float32'):<class'fiona.ogrext.RealField'>,(2,3,'str'):<class'fiona.ogrext.StringField'>,(4,0,'dict'):<class'fiona.ogrext.StringField'>,(4,0,'str'):<class'fiona.ogrext.StringField'>,(4,4,'dict'):<class'fiona.ogrext.JSONField'>,(4,4,'list'):<class'fiona.ogrext.JSONField'>,(5,0,'list'):<class'fiona.ogrext.StringListField'>,(8,0,'bytearray'):<class'fiona.ogrext.BinaryField'>,(8,0,'bytes'):<class'fiona.ogrext.BinaryField'>,(8,0,'memoryview'):<class'fiona.ogrext.BinaryField'>,(9,0,'date'):<class'fiona.ogrext.DateField'>,(9,0,'str'):<class'fiona.ogrext.DateField'>,(10,0,'str'):<class'fiona.ogrext.TimeField'>,(10,0,'time'):<class'fiona.ogrext.TimeField'>,(11,0,'datetime'):<class'fiona.ogrext.DateTimeField'>,(11,0,'str'):<class'fiona.ogrext.DateTimeField'>,(12,0,'float'):<class'fiona.ogrext.RealField'>,(12,0,'int'):<class'fiona.ogrext.Integer64Field'>,(12,0,'int64'):<class'fiona.ogrext.Integer64Field'>,(12,0,'str'):<class'fiona.ogrext.StringField'>}_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.OGRFeatureBuilder.OGRPropertySetter "Link to this definition")_class_ fiona.ogrext.RealField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.RealField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.Session[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session "Link to this definition")
Bases: `object`

OGRFieldGetter _={(0,0):<class'fiona.ogrext.IntegerField'>,(0,1):<class'fiona.ogrext.BooleanField'>,(0,2):<class'fiona.ogrext.Int16Field'>,(2,0):<class'fiona.ogrext.RealField'>,(4,0):<class'fiona.ogrext.StringField'>,(4,4):<class'fiona.ogrext.JSONField'>,(5,0):<class'fiona.ogrext.StringListField'>,(8,0):<class'fiona.ogrext.BinaryField'>,(9,0):<class'fiona.ogrext.DateField'>,(10,0):<class'fiona.ogrext.TimeField'>,(11,0):<class'fiona.ogrext.DateTimeField'>,(12,0):<class'fiona.ogrext.Integer64Field'>}_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.OGRFieldGetter "Link to this definition")get(_fid_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get "Link to this definition")
Provides access to feature data by FID.

Supports Collection.__contains__().

get_crs()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_crs "Link to this definition")
Get the layer’s CRS

Return type:
[CRS](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.crs.CRS "fiona.crs.CRS")

get_crs_wkt()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_crs_wkt "Link to this definition")get_driver()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_driver "Link to this definition")get_extent()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_extent "Link to this definition")get_feature(_fid_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_feature "Link to this definition")
Provides access to feature data by FID.

Supports Collection.__contains__().

get_fileencoding()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_fileencoding "Link to this definition")
DEPRECATED

get_length()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_length "Link to this definition")get_schema()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_schema "Link to this definition")
Get a dictionary representation of a collection’s schema.

The schema dict contains “geometry” and “properties” items.

Return type:
dict

Warning

Fiona 1.9 does not support multiple fields with the name name. When encountered, a warning message is logged and the field is skipped.

get_tag_item(_key_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.get_tag_item "Link to this definition")
Returns tag item value

Parameters:
*   **key** (_str_) – The key for the metadata item to fetch.

*   **ns** (_str_ _,_ _optional_) – Used to select a namespace other than the default.

Return type:
str

has_feature(_fid_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.has_feature "Link to this definition")
Provides access to feature data by FID.

Supports Collection.__contains__().

isactive()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.isactive "Link to this definition")start(_collection_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.start "Link to this definition")stop()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.stop "Link to this definition")tags(_ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session.tags "Link to this definition")
Returns a dict containing copies of the dataset or layers’s tags. Tags are pairs of key and value strings. Tags belong to namespaces. The standard namespaces are: default (None) and ‘IMAGE_STRUCTURE’. Applications can create their own additional namespaces.

Parameters:
**ns** (_str_ _,_ _optional_) – Can be used to select a namespace other than the default.

Return type:
dict

_class_ fiona.ogrext.StringField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.StringField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.StringListField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.StringListField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

_class_ fiona.ogrext.TZ(_minutes_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.TZ "Link to this definition")
Bases: `tzinfo`

utcoffset(_dt_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.TZ.utcoffset "Link to this definition")
datetime -> timedelta showing offset from UTC, negative values indicating West of UTC

_class_ fiona.ogrext.TimeField[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.TimeField "Link to this definition")
Bases: [`AbstractField`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.AbstractField "fiona.ogrext.AbstractField")

Times without dates.

_class_ fiona.ogrext.WritingSession[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.Session "fiona.ogrext.Session")

start(_collection_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession.start "Link to this definition")sync(_collection_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession.sync "Link to this definition")
Syncs OGR to disk.

update_tag_item(_key_, _tag_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession.update_tag_item "Link to this definition")
Updates the tag item value

Parameters:
*   **key** (_str_) – The key for the metadata item to set.

*   **tag** (_str_) – The value of the metadata item to set.

*   **ns** (_str_) – Used to select a namespace other than the default.

Return type:
int

update_tags(_tags_, _ns=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession.update_tags "Link to this definition")
Writes a dict containing the dataset or layers’s tags. Tags are pairs of key and value strings. Tags belong to namespaces. The standard namespaces are: default (None) and ‘IMAGE_STRUCTURE’. Applications can create their own additional namespaces.

Parameters:
*   **tags** (_dict_) – The dict of metadata items to set.

*   **ns** (_str_ _,_ _optional_) – Used to select a namespace other than the default.

Return type:
int

writerecs(_records_, _collection_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.WritingSession.writerecs "Link to this definition")
Writes records to collection storage.

Parameters:
*   **records** (_Iterable_) – A stream of feature records.

*   **collection** ([_Collection_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection "fiona.collection.Collection")) – The collection in which feature records are stored.

Return type:
None

fiona.ogrext.buffer_to_virtual_file(_bytesbuf_, _ext=''_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.buffer_to_virtual_file "Link to this definition")
Maps a bytes buffer to a virtual file.

ext is empty or begins with a period and contains at most one period.

fiona.ogrext.featureRT(_feat_, _collection_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.featureRT "Link to this definition")fiona.ogrext.remove_virtual_file(_vsi\_filename_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.ogrext.remove_virtual_file "Link to this definition")
fiona.path module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.path "Link to this heading")
----------------------------------------------------------------------------------------------------------------

Dataset paths, identifiers, and filenames

Note well: this module is deprecated in 1.3.0 and will be removed in a future version.

fiona.rfc3339 module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.rfc3339 "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

_class_ fiona.rfc3339.group_accessor(_m_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.rfc3339.group_accessor "Link to this definition")
Bases: `object`

group(_i_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.rfc3339.group_accessor.group "Link to this definition")fiona.rfc3339.parse_date(_text_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.rfc3339.parse_date "Link to this definition")
Given a date, returns a datetime tuple

Parameters:
**text** (_string to be parsed_)

Returns:
datetime tuple: (year, month, day, hour, minute, second, microsecond, utcoffset in minutes or None)

Return type:
(int, int , int, int, int, int, int, int)

fiona.rfc3339.parse_datetime(_text_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.rfc3339.parse_datetime "Link to this definition")
Given a datetime, returns a datetime tuple

Parameters:
**text** (_string to be parsed_)

Returns:
datetime tuple: (year, month, day, hour, minute, second, microsecond, utcoffset in minutes or None)

Return type:
(int, int , int, int, int, int, int, int)

fiona.rfc3339.parse_time(_text_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.rfc3339.parse_time "Link to this definition")
Given a time, returns a datetime tuple

Parameters:
**text** (_string to be parsed_)

Returns:
datetime tuple: (year, month, day, hour, minute, second, microsecond, utcoffset in minutes or None)

Return type:
(int, int , int, int, int, int, int, int)

fiona.schema module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.schema "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Fiona schema module.

_class_ fiona.schema.FionaBinaryType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBinaryType "Link to this definition")
Bases: `object`

names _=['bytes']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBinaryType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBinaryType.type "Link to this definition")
alias of `bytes`

_class_ fiona.schema.FionaBooleanType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBooleanType "Link to this definition")
Bases: `object`

names _=['bool']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBooleanType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaBooleanType.type "Link to this definition")
alias of `bool`

_class_ fiona.schema.FionaDateTimeType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateTimeType "Link to this definition")
Bases: `object`

Dates and times.

names _=['datetime']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateTimeType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateTimeType.type "Link to this definition")
alias of `str`

_class_ fiona.schema.FionaDateType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateType "Link to this definition")
Bases: `object`

Dates without time.

names _=['date']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaDateType.type "Link to this definition")
alias of `str`

_class_ fiona.schema.FionaInt16Type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInt16Type "Link to this definition")
Bases: `object`

names _=['int16']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInt16Type.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInt16Type.type "Link to this definition")
alias of `int`

_class_ fiona.schema.FionaInteger64Type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInteger64Type "Link to this definition")
Bases: `object`

names _=['int','int64']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInteger64Type.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaInteger64Type.type "Link to this definition")
alias of `int`

_class_ fiona.schema.FionaIntegerType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaIntegerType "Link to this definition")
Bases: `object`

names _=['int32']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaIntegerType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaIntegerType.type "Link to this definition")
alias of `int`

_class_ fiona.schema.FionaJSONType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaJSONType "Link to this definition")
Bases: `object`

names _=['json']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaJSONType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaJSONType.type "Link to this definition")
alias of `str`

_class_ fiona.schema.FionaRealType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaRealType "Link to this definition")
Bases: `object`

names _=['float','float64']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaRealType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaRealType.type "Link to this definition")
alias of `float`

_class_ fiona.schema.FionaStringListType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringListType "Link to this definition")
Bases: `object`

names _=['List[str]','list[str]']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringListType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringListType.type "Link to this definition")
alias of `List`[`str`]

_class_ fiona.schema.FionaStringType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringType "Link to this definition")
Bases: `object`

names _=['str']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaStringType.type "Link to this definition")
alias of `str`

_class_ fiona.schema.FionaTimeType[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaTimeType "Link to this definition")
Bases: `object`

Times without dates.

names _=['time']_[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaTimeType.names "Link to this definition")type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.FionaTimeType.type "Link to this definition")
alias of `str`

fiona.schema.normalize_field_type(_ftype_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.schema.normalize_field_type "Link to this definition")
Normalize free form field types to an element of FIELD_TYPES

Parameters:
**ftype** (_str_) – A type:width format like ‘int:9’ or ‘str:255’

Returns:
An element from FIELD_TYPES

Return type:
str

fiona.session module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.session "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

Abstraction for sessions in various clouds.

_class_ fiona.session.AWSSession(_session=None_, _aws\_unsigned=False_, _aws\_access\_key\_id=None_, _aws\_secret\_access\_key=None_, _aws\_session\_token=None_, _region\_name=None_, _profile\_name=None_, _endpoint\_url=None_, _requester\_pays=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AWSSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

Configures access to secured resources stored in AWS S3.

_property_ credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AWSSession.credentials "Link to this definition")
The session credentials as a dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AWSSession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AWSSession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.AzureSession(_azure\_storage\_connection\_string=None_, _azure\_storage\_account=None_, _azure\_storage\_access\_key=None_, _azure\_unsigned=False_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AzureSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

Configures access to secured resources stored in Microsoft Azure Blob Storage.

_property_ credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AzureSession.credentials "Link to this definition")
The session credentials as a dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AzureSession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.AzureSession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.DummySession(_*args_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.DummySession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

A dummy session.

credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.DummySession.credentials "Link to this definition")
The session credentials.

Type:
dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.DummySession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.DummySession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.GSSession(_google\_application\_credentials=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.GSSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

Configures access to secured resources stored in Google Cloud Storage

_property_ credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.GSSession.credentials "Link to this definition")
The session credentials as a dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.GSSession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.GSSession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.OSSSession(_oss\_access\_key\_id=None_, _oss\_secret\_access\_key=None_, _oss\_endpoint=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.OSSSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

Configures access to secured resources stored in Alibaba Cloud OSS.

_property_ credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.OSSSession.credentials "Link to this definition")
The session credentials as a dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.OSSSession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.OSSSession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.Session[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "Link to this definition")
Bases: `object`

Base for classes that configure access to secured resources.

credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.credentials "Link to this definition")
Keys and values for session credentials.

Type:
dict

Notes

This class is not intended to be instantiated.

_static_ aws_or_dummy(_*args_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.aws_or_dummy "Link to this definition")
Create an AWSSession if boto3 is available, else DummySession

Parameters:
*   **path** (_str_) – A dataset path or identifier.

*   **args** (_sequence_) – Positional arguments for the foreign session constructor.

*   **kwargs** (_dict_) – Keyword arguments for the foreign session constructor.

Return type:
[Session](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

_static_ cls_from_path(_path_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.cls_from_path "Link to this definition")
Find the session class suited to the data at path.

Parameters:
**path** (_str_) – A dataset path or identifier.

Return type:
class

_static_ from_environ(_*args_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.from_environ "Link to this definition")
Create a session object suited to the environment.

Parameters:
*   **path** (_str_) – A dataset path or identifier.

*   **args** (_sequence_) – Positional arguments for the foreign session constructor.

*   **kwargs** (_dict_) – Keyword arguments for the foreign session constructor.

Return type:
[Session](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

_static_ from_foreign_session(_session_, _cls=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.from_foreign_session "Link to this definition")
Create a session object matching the foreign session.

Parameters:
*   **session** (_obj_) – A foreign session object.

*   **cls** (_Session class_ _,_ _optional_) – The class to return.

Return type:
[Session](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

_static_ from_path(_path_, _*args_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.from_path "Link to this definition")
Create a session object suited to the data at path.

Parameters:
*   **path** (_str_) – A dataset path or identifier.

*   **args** (_sequence_) – Positional arguments for the foreign session constructor.

*   **kwargs** (_dict_) – Keyword arguments for the foreign session constructor.

Return type:
[Session](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

_class_ fiona.session.SwiftSession(_session=None_, _swift\_storage\_url=None_, _swift\_auth\_token=None_, _swift\_auth\_v1\_url=None_, _swift\_user=None_, _swift\_key=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.SwiftSession "Link to this definition")
Bases: [`Session`](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.Session "fiona.session.Session")

Configures access to secured resources stored in OpenStack Swift Object Storage.

_property_ credentials[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.SwiftSession.credentials "Link to this definition")
The session credentials as a dict

get_credential_options()[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.SwiftSession.get_credential_options "Link to this definition")
Get credentials as GDAL configuration options

Return type:
dict

_classmethod_ hascreds(_config_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.session.SwiftSession.hascreds "Link to this definition")
Determine if the given configuration has proper credentials

Parameters:
*   **cls** (_class_) – A Session class.

*   **config** (_dict_) – GDAL configuration as a dict.

Return type:
bool

fiona.transform module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.transform "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Coordinate and geometry warping and reprojection

fiona.transform.transform(_src\_crs_, _dst\_crs_, _xs_, _ys_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.transform.transform "Link to this definition")
Transform coordinates from one reference system to another.

Parameters:
*   **src_crs** (_str_ _or_ _dict_) – A string like ‘EPSG:4326’ or a dict of proj4 parameters like {‘proj’: ‘lcc’, ‘lat_0’: 18.0, ‘lat_1’: 18.0, ‘lon_0’: -77.0} representing the coordinate reference system on the “source” or “from” side of the transformation.

*   **dst_crs** (_str_ _or_ _dict_) – A string or dict representing the coordinate reference system on the “destination” or “to” side of the transformation.

*   **xs** (_sequence_ _of_ _float_) – A list or tuple of x coordinate values. Must have the same length as the `ys` parameter.

*   **ys** (_sequence_ _of_ _float_) – A list or tuple of y coordinate values. Must have the same length as the `xs` parameter.

Returns:
**xp, yp** – A pair of transformed coordinate sequences. The elements of `xp` and `yp` correspond exactly to the elements of the `xs` and `ys` input parameters.

Return type:
list of float

Examples

>>> transform('EPSG:4326', 'EPSG:26953', [-105.0], [40.0])
([957097.0952383667], [378940.8419189212])

fiona.transform.transform_geom(_src\_crs_, _dst\_crs_, _geom_, _antimeridian\_cutting=False_, _antimeridian\_offset=10.0_, _precision=-1_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.transform.transform_geom "Link to this definition")
Transform a geometry obj from one reference system to another.

Parameters:
*   **src_crs** (_str_ _or_ _dict_) – A string like ‘EPSG:4326’ or a dict of proj4 parameters like {‘proj’: ‘lcc’, ‘lat_0’: 18.0, ‘lat_1’: 18.0, ‘lon_0’: -77.0} representing the coordinate reference system on the “source” or “from” side of the transformation.

*   **dst_crs** (_str_ _or_ _dict_) – A string or dict representing the coordinate reference system on the “destination” or “to” side of the transformation.

*   **geom** (_obj_) – A GeoJSON-like geometry object with ‘type’ and ‘coordinates’ members or an iterable of GeoJSON-like geometry objects.

*   **antimeridian_cutting** (_bool_ _,_ _optional_) – `True` to cut output geometries in two at the antimeridian, the default is [``](https://fiona.readthedocs.io/en/stable/fiona.html#id1)False`.

*   **antimeridian_offset** (_float_ _,_ _optional_) – A distance in decimal degrees from the antimeridian, outside of which geometries will not be cut.

*   **precision** (_int_ _,_ _optional_) – Round geometry coordinates to this number of decimal places. This parameter is deprecated and will be removed in 2.0.

Returns:
A new GeoJSON-like geometry (or a list of GeoJSON-like geometries if an iterable was given as input) with transformed coordinates. Note that if the output is at the antimeridian, it may be cut and of a different geometry `type` than the input, e.g., a polygon input may result in multi-polygon output.

Return type:
obj

Examples

>>> transform_geom(
...     'EPSG:4326', 'EPSG:26953',
...     {'type': 'Point', 'coordinates': [-105.0, 40.0]})
{'type': 'Point', 'coordinates': (957097.0952383667, 378940.8419189212)}

fiona.vfs module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona.vfs "Link to this heading")
--------------------------------------------------------------------------------------------------------------

Implementation of Apache VFS schemes and URLs.

fiona.vfs.is_remote(_scheme_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.vfs.is_remote "Link to this definition")fiona.vfs.parse_paths(_uri_, _vfs=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.vfs.parse_paths "Link to this definition")
Parse a URI or Apache VFS URL into its parts

Returns: tuple
(path, scheme, archive)

fiona.vfs.valid_vsi(_vsi_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.vfs.valid_vsi "Link to this definition")
Ensures all parts of our vsi path are valid schemes.

fiona.vfs.vsi_path(_path_, _vsi=None_, _archive=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.vfs.vsi_path "Link to this definition")
fiona module[](https://fiona.readthedocs.io/en/stable/fiona.html#module-fiona "Link to this heading")
------------------------------------------------------------------------------------------------------

Fiona is OGR’s neat, nimble API.

Fiona provides a minimal, uncomplicated Python interface to the open source GIS community’s most trusted geodata access library and integrates readily with other Python GIS packages such as pyproj, Rtree and Shapely.

A Fiona feature is a Python mapping inspired by the GeoJSON format. It has `id`, `geometry`, and `properties` attributes. The value of `id` is a string identifier unique within the feature’s parent collection. The `geometry` is another mapping with `type` and `coordinates` keys. The `properties` of a feature is another mapping corresponding to its attribute table.

Features are read and written using the `Collection` class. These `Collection` objects are a lot like Python `file` objects. A `Collection` opened in reading mode serves as an iterator over features. One opened in a writing mode provides a `write` method.

_class_ fiona.Feature(_geometry=None_, _id=None_, _properties=None_, _**data_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature "Link to this definition")
Bases: `Object`

A GeoJSON-like feature

Notes

Delegates geometry and properties to an instance of _Feature, which will become an extension class in Fiona 2.0.

_classmethod_ from_dict(_ob=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature.from_dict "Link to this definition")_property_ geometry[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature.geometry "Link to this definition")
The feature’s geometry object

Return type:
[Geometry](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry "fiona.Geometry")

_property_ id[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature.id "Link to this definition")
The feature’s id

Return type:
object

_property_ properties[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature.properties "Link to this definition")
The feature’s properties

Return type:
object

_property_ type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Feature.type "Link to this definition")
The Feature’s type

Return type:
str

_class_ fiona.Geometry(_coordinates=None_, _type=None_, _geometries=None_, _**data_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry "Link to this definition")
Bases: `Object`

A GeoJSON-like geometry

Notes

Delegates coordinates and type properties to an instance of _Geometry, which will become an extension class in Fiona 2.0.

_property_ coordinates[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry.coordinates "Link to this definition")
The geometry’s coordinates

Return type:
Sequence

_classmethod_ from_dict(_ob=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry.from_dict "Link to this definition")_property_ geometries[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry.geometries "Link to this definition")
A collection’s geometries.

Return type:
list

_property_ type[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Geometry.type "Link to this definition")
The geometry’s type

Return type:
str

_class_ fiona.Properties(_**kwds_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Properties "Link to this definition")
Bases: `Object`

A GeoJSON-like feature’s properties

_classmethod_ from_dict(_mapping=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.Properties.from_dict "Link to this definition")fiona.bounds(_ob_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.bounds "Link to this definition")
Returns a (minx, miny, maxx, maxy) bounding box.

The `ob` may be a feature record or geometry.

fiona.listdir(_fp_, _opener=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.listdir "Link to this definition")
Lists the datasets in a directory or archive file.

Archive files must be prefixed like “zip://” or “tar://”.

Parameters:
*   **fp** (_str_ _or_ _pathlib.Path_) – Directory or archive path.

*   **opener** (_callable_ _or_ _obj_ _,_ _optional_) –

A custom dataset opener which can serve GDAL’s virtual filesystem machinery via Python file-like objects. The underlying file-like object is obtained by calling _opener_ with (_fp_, _mode_) or (_fp_, _mode_ + “b”) depending on the format driver’s native mode. _opener_ must return a Python file-like object that provides read, seek, tell, and close methods. Note: only one opener at a time per fp, mode pair is allowed.

Alternatively, opener may be a filesystem object from a package like fsspec that provides the following methods: isdir(), isfile(), ls(), mtime(), open(), and size(). The exact interface is defined in the fiona._vsiopener._AbstractOpener class.

Returns:
A list of datasets.

Return type:
list of str

Raises:
**TypeError** – If the input is not a str or Path.

fiona.listlayers(_fp_, _opener=None_, _vfs=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.listlayers "Link to this definition")
Lists the layers (collections) in a dataset.

Archive files must be prefixed like “zip://” or “tar://”.

Parameters:
*   **fp** (_str_ _,_ _pathlib.Path_ _, or_ _file-like object_) – A dataset identifier or file object containing a dataset.

*   **opener** (_callable_ _or_ _obj_ _,_ _optional_) –

A custom dataset opener which can serve GDAL’s virtual filesystem machinery via Python file-like objects. The underlying file-like object is obtained by calling _opener_ with (_fp_, _mode_) or (_fp_, _mode_ + “b”) depending on the format driver’s native mode. _opener_ must return a Python file-like object that provides read, seek, tell, and close methods. Note: only one opener at a time per fp, mode pair is allowed.

Alternatively, opener may be a filesystem object from a package like fsspec that provides the following methods: isdir(), isfile(), ls(), mtime(), open(), and size(). The exact interface is defined in the fiona._vsiopener._AbstractOpener class.

*   **vfs** (_str_) – This is a deprecated parameter. A URI scheme such as “zip://” should be used instead.

*   **kwargs** (_dict_) – Dataset opening options and other keyword args.

Returns:
A list of layer name strings.

Return type:
list of str

Raises:
**TypeError** – If the input is not a str, Path, or file object.

fiona.open(_fp_, _mode='r'_, _driver=None_, _schema=None_, _crs=None_, _encoding=None_, _layer=None_, _vfs=None_, _enabled\_drivers=None_, _crs\_wkt=None_, _ignore\_fields=None_, _ignore\_geometry=False_, _include\_fields=None_, _wkt\_version=None_, _allow\_unsupported\_drivers=False_, _opener=None_, _**kwargs_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.open "Link to this definition")
Open a collection for read, append, or write

In write mode, a driver name such as “ESRI Shapefile” or “GPX” (see OGR docs or `ogr2ogr --help` on the command line) and a schema mapping such as:

> {‘geometry’: ‘Point’,‘properties’: [(‘class’, ‘int’), (‘label’, ‘str’),
> (‘value’, ‘float’)]}

must be provided. If a particular ordering of properties (“fields” in GIS parlance) in the written file is desired, a list of (key, value) pairs as above or an ordered dict is required. If no ordering is needed, a standard dict will suffice.

A coordinate reference system for collections in write mode can be defined by the `crs` parameter. It takes Proj4 style mappings like

> {‘proj’: ‘longlat’, ‘ellps’: ‘WGS84’, ‘datum’: ‘WGS84’,
> ‘no_defs’: True}

short hand strings like

> EPSG:4326

or WKT representations of coordinate reference systems.

The drivers used by Fiona will try to detect the encoding of data files. If they fail, you may provide the proper `encoding`, such as ‘Windows-1252’ for the original Natural Earth datasets.

When the provided path is to a file containing multiple named layers of data, a layer can be singled out by `layer`.

The drivers enabled for opening datasets may be restricted to those listed in the `enabled_drivers` parameter. This and the `driver` parameter afford much control over opening of files.

> # Trying only the GeoJSON driver when opening to read, the # following raises `DataIOError`: fiona.open(‘example.shp’, driver=’GeoJSON’)
> 
> 
> # Trying first the GeoJSON driver, then the Shapefile driver, # the following succeeds: fiona.open(
> 
> 
> > ‘example.shp’, enabled_drivers=[‘GeoJSON’, ‘ESRI Shapefile’])

Some format drivers permit low-level filtering of fields. Specific fields can be omitted by using the `ignore_fields` parameter. Specific fields can be selected, excluding all others, by using the `include_fields` parameter.

Parameters:
*   **fp** (_URI_ _(_ _str_ _or_ _pathlib.Path_ _)_ _, or_ _file-like object_) – A dataset resource identifier or file object.

*   **mode** (_str_) – One of ‘r’, to read (the default); ‘a’, to append; or ‘w’, to write.

*   **driver** (_str_) – In ‘w’ mode a format driver name is required. In ‘r’ or ‘a’ mode this parameter has no effect.

*   **schema** (_dict_) – Required in ‘w’ mode, has no effect in ‘r’ or ‘a’ mode.

*   **crs** (_str_ _or_ _dict_) – Required in ‘w’ mode, has no effect in ‘r’ or ‘a’ mode.

*   **encoding** (_str_) – Name of the encoding used to encode or decode the dataset.

*   **layer** (_int_ _or_ _str_) – The integer index or name of a layer in a multi-layer dataset.

*   **vfs** (_str_) – This is a deprecated parameter. A URI scheme such as “zip://” should be used instead.

*   **enabled_drivers** (_list_) – An optional list of driver names to used when opening a collection.

*   **crs_wkt** (_str_) – An optional WKT representation of a coordinate reference system.

*   **ignore_fields** (_list_ _[_ _str_ _]_ _,_ _optional_) – List of field names to ignore on load.

*   **include_fields** (_list_ _[_ _str_ _]_ _,_ _optional_) – List of a subset of field names to include on load.

*   **ignore_geometry** (_bool_) – Ignore the geometry on load.

*   **wkt_version** (_fiona.enums.WktVersion_ _or_ _str_ _,_ _optional_) – Version to use to for the CRS WKT. Defaults to GDAL’s default (WKT1_GDAL for GDAL 3).

*   **allow_unsupported_drivers** (_bool_) – If set to true do not limit GDAL drivers to set set of known working.

*   **opener** (_callable_ _or_ _obj_ _,_ _optional_) –

A custom dataset opener which can serve GDAL’s virtual filesystem machinery via Python file-like objects. The underlying file-like object is obtained by calling _opener_ with (_fp_, _mode_) or (_fp_, _mode_ + “b”) depending on the format driver’s native mode. _opener_ must return a Python file-like object that provides read, seek, tell, and close methods. Note: only one opener at a time per fp, mode pair is allowed.

Alternatively, opener may be a filesystem object from a package like fsspec that provides the following methods: isdir(), isfile(), ls(), mtime(), open(), and size(). The exact interface is defined in the fiona._vsiopener._AbstractOpener class.

*   **kwargs** (_mapping_) – Other driver-specific parameters that will be interpreted by the OGR library as layer creation or opening options.

Return type:
[Collection](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection "fiona.collection.Collection")

Raises:
[**DriverError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DriverError "fiona.errors.DriverError") – When the selected format driver cannot provide requested capabilities such as ignoring fields.

fiona.prop_type(_text_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.prop_type "Link to this definition")
Returns a schema property’s proper Python type.

Parameters:
**text** (_str_) – A type name, with or without width.

Returns:
A Python class.

Return type:
obj

Examples

>>> prop_type('int')
<class 'int'>
>>> prop_type('str:25')
<class 'str'>

fiona.prop_width(_val_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.prop_width "Link to this definition")
Returns the width of a str type property.

Undefined for non-str properties.

Parameters:
**val** (_str_) – A type:width string from a collection schema.

Return type:
int or None

Examples

>>> prop_width('str:25')
25
>>> prop_width('str')
80

fiona.remove(_path\_or\_collection_, _driver=None_, _layer=None_, _opener=None_)[](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.remove "Link to this definition")
Delete an OGR data source or one of its layers.

If no layer is specified, the entire dataset and all of its layers and associated sidecar files will be deleted.

Parameters:
*   **path_or_collection** (_str_ _,_ _pathlib.Path_ _, or_[_Collection_](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.collection.Collection "fiona.collection.Collection")) – The target Collection or its path.

*   **opener** (_callable_ _or_ _obj_ _,_ _optional_) –

A custom dataset opener which can serve GDAL’s virtual filesystem machinery via Python file-like objects. The underlying file-like object is obtained by calling _opener_ with (_fp_, _mode_) or (_fp_, _mode_ + “b”) depending on the format driver’s native mode. _opener_ must return a Python file-like object that provides read, seek, tell, and close methods. Note: only one opener at a time per fp, mode pair is allowed.

Alternatively, opener may be a filesystem object from a package like fsspec that provides the following methods: isdir(), isfile(), ls(), mtime(), open(), and size(). The exact interface is defined in the fiona._vsiopener._AbstractOpener class.

*   **driver** (_str_ _,_ _optional_) – The name of a driver to be used for deletion, optional. Can usually be detected.

*   **layer** (_str_ _or_ _int_ _,_ _optional_) – The name or index of a specific layer.

Return type:
None

Raises:
[**DatasetDeleteError**](https://fiona.readthedocs.io/en/stable/fiona.html#fiona.errors.DatasetDeleteError "fiona.errors.DatasetDeleteError") – If the data source cannot be deleted.
