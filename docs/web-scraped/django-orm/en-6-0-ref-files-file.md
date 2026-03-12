# Source: https://docs.djangoproject.com/en/6.0/ref/files/file/

Title: The File object | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/files/file/

Markdown Content:
The [`django.core.files`](https://docs.djangoproject.com/en/6.0/ref/files/#module-django.core.files "django.core.files: File handling and storage") module and its submodules contain built-in classes for basic file handling in Django.

The `File` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#the-file-class "Link to this heading")
----------------------------------------------------------------------------------------------------------------

_class_ File(_file\_object_, _name=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L8)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "Link to this definition")
The [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") class is a thin wrapper around a Python [file object](https://docs.python.org/3/glossary.html#term-file-object "(in Python v3.14)") with some Django-specific additions. Internally, Django uses this class when it needs to represent a file.

[`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") objects have the following attributes and methods:

name[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.name "Link to this definition")
The name of the file including the relative path from [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT).

size[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L32)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.size "Link to this definition")
The size of the file in bytes.

file[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.file "Link to this definition")
The underlying [file object](https://docs.python.org/3/glossary.html#term-file-object "(in Python v3.14)") that this class wraps.

Be careful with this attribute in subclasses.

Some subclasses of [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), including [`ContentFile`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.base.ContentFile "django.core.files.base.ContentFile") and [`FieldFile`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile "django.db.models.fields.files.FieldFile"), may replace this attribute with an object other than a Python [file object](https://docs.python.org/3/glossary.html#term-file-object "(in Python v3.14)"). In these cases, this attribute may itself be a [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") subclass (and not necessarily the same subclass). Whenever possible, use the attributes and methods of the subclass itself rather than the those of the subclass’s `file` attribute.

mode[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.mode "Link to this definition")
The read/write mode for the file.

open(_mode=None_, _*args_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L108)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.open "Link to this definition")
Open or reopen the file (which also does `File.seek(0)`). The `mode` argument allows the same values as Python’s built-in [`open()`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)"). `*args` and `**kwargs` are passed after `mode` to Python’s built-in [`open()`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)").

When reopening a file, `mode` will override whatever mode the file was originally opened with; `None` means to reopen with the original mode.

It can be used as a context manager, e.g. `with file.open() as f:`.

 __iter__ ()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L75)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.__iter__ "Link to this definition")
Iterate over the file yielding one line at a time.

chunks(_chunk\_size=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L48)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.chunks "Link to this definition")
Iterate over the file yielding “chunks” of a given size. `chunk_size` defaults to 64 KB.

This is especially useful with very large files since it allows them to be streamed off disk and avoids storing the whole file in memory.

multiple_chunks(_chunk\_size=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L65)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.multiple_chunks "Link to this definition")
Returns `True` if the file is large enough to require multiple chunks to access all of its content give some `chunk_size`.

close()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L117)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.close "Link to this definition")
Close the file.

In addition to the listed methods, [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") exposes the following attributes and methods of its `file` object: `encoding`, `fileno`, `flush`, `isatty`, `newlines`, `read`, `readinto`, `readline`, `readlines`, `seek`, `tell`, `truncate`, `write`, `writelines`, `readable()`, `writable()`, and `seekable()`.

The `ContentFile` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#the-contentfile-class "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

_class_ ContentFile(_content_, _name=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/base.py#L121)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.base.ContentFile "Link to this definition")
The `ContentFile` class inherits from [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), but unlike [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") it operates on string content (bytes also supported), rather than an actual file. For example:

from django.core.files.base import ContentFile

f1 = ContentFile("esta frase está en español")
f2 = ContentFile(b"these are bytes")

The `ImageFile` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#the-imagefile-class "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

_class_ ImageFile(_file\_object_, _name=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/images.py#L13)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.images.ImageFile "Link to this definition")
Django provides a built-in class specifically for images. [`django.core.files.images.ImageFile`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.images.ImageFile "django.core.files.images.ImageFile") inherits all the attributes and methods of [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), and additionally provides the following:

width[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/images.py#L20)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.images.ImageFile.width "Link to this definition")
Width of the image in pixels.

height[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/images.py#L24)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.images.ImageFile.height "Link to this definition")
Height of the image in pixels.

Additional methods on files attached to objects[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#additional-methods-on-files-attached-to-objects "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Any [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") that is associated with an object (as with `Car.photo`, below) will also have a couple of extra methods:

File.save(_name_, _content_, _save=True_)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.save "Link to this definition")
Saves a new file with the file name and contents provided. This will not replace the existing file, but will create a new file and update the object to point to it. If `save` is `True`, the model’s `save()` method will be called once the file is saved. That is, these two lines:

>>> car.photo.save("myphoto.jpg", content, save=False)
>>> car.save()

are equivalent to:

>>> car.photo.save("myphoto.jpg", content, save=True)

Note that the `content` argument must be an instance of either [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") or of a subclass of [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), such as [`ContentFile`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.base.ContentFile "django.core.files.base.ContentFile").

File.delete(_save=True_)[¶](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.delete "Link to this definition")
Removes the file from the model instance and deletes the underlying file. If `save` is `True`, the model’s `save()` method will be called once the file is deleted.
