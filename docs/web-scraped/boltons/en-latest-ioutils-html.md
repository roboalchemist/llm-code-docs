# Source: https://boltons.readthedocs.io/en/latest/ioutils.html

Title: Input/output enhancements — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/ioutils.html

Markdown Content:
Module `ioutils` implements a number of helper classes and functions which are useful when dealing with input, output, and bytestreams in a variety of ways.

Spooled Temporary Files[](https://boltons.readthedocs.io/en/latest/ioutils.html#spooled-temporary-files "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

Spooled Temporary Files are file-like objects that start out mapped to in-memory objects, but automatically roll over to a temporary file once they reach a certain (configurable) threshold. Unfortunately the built-in SpooledTemporaryFile class in Python does not implement the exact API that some common classes like StringIO do. SpooledTemporaryFile also spools all of it’s in-memory files as cStringIO instances. cStringIO instances cannot be deep-copied, and they don’t work with the zip library either. This along with the incompatible api makes it useless for several use-cases.

To combat this but still gain the memory savings and usefulness of a true spooled file-like-object, two custom classes have been implemented which have a compatible API.

### SpooledBytesIO[](https://boltons.readthedocs.io/en/latest/ioutils.html#spooledbytesio "Link to this heading")

_class_ boltons.ioutils.SpooledBytesIO(_max\_size=5000000_, _dir=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/ioutils.html#SpooledBytesIO)[](https://boltons.readthedocs.io/en/latest/ioutils.html#boltons.ioutils.SpooledBytesIO "Link to this definition")
SpooledBytesIO is a spooled file-like-object that only accepts bytes. On Python 2.x this means the ‘str’ type; on Python 3.x this means the ‘bytes’ type. Bytes are written in and retrieved exactly as given, but it will raise TypeErrors if something other than bytes are written.

Example:

>>> from boltons import ioutils
>>> with ioutils.SpooledBytesIO() as f:
...     f.write(b"Happy IO")
...     _ = f.seek(0)
...     isinstance(f.getvalue(), bytes)
True

### SpooledStringIO[](https://boltons.readthedocs.io/en/latest/ioutils.html#spooledstringio "Link to this heading")

_class_ boltons.ioutils.SpooledStringIO(_*args_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/ioutils.html#SpooledStringIO)[](https://boltons.readthedocs.io/en/latest/ioutils.html#boltons.ioutils.SpooledStringIO "Link to this definition")
SpooledStringIO is a spooled file-like-object that only accepts unicode values. On Python 2.x this means the ‘unicode’ type and on Python 3.x this means the ‘str’ type. Values are accepted as unicode and then coerced into utf-8 encoded bytes for storage. On retrieval, the values are returned as unicode.

Example:

>>> from boltons import ioutils
>>> with ioutils.SpooledStringIO() as f:
...     f.write(u"— Hey, an emdash!")
...     _ = f.seek(0)
...     isinstance(f.read(), str)
True

Examples[](https://boltons.readthedocs.io/en/latest/ioutils.html#examples "Link to this heading")
--------------------------------------------------------------------------------------------------

It’s not uncommon to find excessive usage of StringIO in older Python code. A SpooledTemporaryFile would be a nice replacement if one wanted to reduce memory overhead, but unfortunately its api differs too much. This is a good candidate for [SpooledBytesIO](https://boltons.readthedocs.io/en/latest/ioutils.html#spooledbytesio) as it is api compatible and thus may be used as a drop-in replacement.

Old Code:

flo = StringIO()
flo.write(gigantic_string)

Updated:

from boltons.ioutils import SpooledBytesIO

flo = SpooledBytesIO()
flo.write(gigantic_string)

Another good use case is downloading a file from some remote location. It’s nice to keep it in memory if it’s small, but writing a large file into memory can make servers quite grumpy. If the file being downloaded happens to be a zip file then things are worse. You can’t use a normal SpooledTemporaryFile because it isn’t compatible. A [SpooledBytesIO](https://boltons.readthedocs.io/en/latest/ioutils.html#spooledbytesio) instance is a good alternative. Here is a simple example using the requests library to download a zip file:

from zipfile import ZipFile

import requests
from boltons import ioutils

# Using a context manager with stream=True ensures the connection is closed. See:
# http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow
with requests.get("http://127.0.0.1/test_file.zip", stream=True) as r:
    if r.status_code == 200:
        with ioutils.SpooledBytesIO() as flo:
            for chunk in r.iter_content(chunk_size=64000):
                flo.write(chunk)

            flo.seek(0)

            zip_doc = ZipFile(flo)

            # Print all the files in the zip
            print(zip_doc.namelist())

Multiple Files[](https://boltons.readthedocs.io/en/latest/ioutils.html#multiple-files "Link to this heading")
--------------------------------------------------------------------------------------------------------------

### MultiFileReader[](https://boltons.readthedocs.io/en/latest/ioutils.html#multifilereader "Link to this heading")

_class_ boltons.ioutils.MultiFileReader(_*fileobjs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/ioutils.html#MultiFileReader)[](https://boltons.readthedocs.io/en/latest/ioutils.html#boltons.ioutils.MultiFileReader "Link to this definition")
Takes a list of open files or file-like objects and provides an interface to read from them all contiguously. Like [`itertools.chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain "(in Python v3.14)"), but for reading files.

>>> mfr = MultiFileReader(BytesIO(b'ab'), BytesIO(b'cd'), BytesIO(b'e'))
>>> mfr.read(3).decode('ascii')
u'abc'
>>> mfr.read(3).decode('ascii')
u'de'

The constructor takes as many fileobjs as you hand it, and will raise a TypeError on non-file-like objects. A ValueError is raised when file-like objects are a mix of bytes- and text-handling objects (for instance, BytesIO and StringIO).
