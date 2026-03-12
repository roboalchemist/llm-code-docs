# Source: https://docs.djangoproject.com/en/6.0/ref/files/storage/

Title: File storage API | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/files/storage/

Markdown Content:
Getting the default storage class[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#getting-the-default-storage-class "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Django provides convenient ways to access the default storage class:

storages[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.storages "Link to this definition")
A dictionary-like object that allows retrieving a storage instance using its alias as defined by [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES).

`storages` has an attribute `backends`, which defaults to the raw value provided in [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES).

Additionally, `storages` provides a `create_storage()` method that accepts the dictionary used in [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES) for a backend, and returns a storage instance based on that backend definition. This may be useful for third-party packages needing to instantiate storages in tests:

>>> from django.core.files.storage import storages
>>> storages.backends
{'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
 'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
 'custom': {'BACKEND': 'package.storage.CustomStorage'}}
>>> storage_instance = storages.create_storage({"BACKEND": "package.storage.CustomStorage"})

_class_ DefaultStorage[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/__init__.py#L21)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.DefaultStorage "Link to this definition")
[`DefaultStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.DefaultStorage "django.core.files.storage.DefaultStorage") provides lazy access to the default storage system as defined by `default` key in [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES). [`DefaultStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.DefaultStorage "django.core.files.storage.DefaultStorage") uses [`storages`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.storages "django.core.files.storage.storages") internally.

default_storage[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.default_storage "Link to this definition")
[`default_storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.default_storage "django.core.files.storage.default_storage") is an instance of the [`DefaultStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.DefaultStorage "django.core.files.storage.DefaultStorage").

The `FileSystemStorage` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#the-filesystemstorage-class "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

_class_ FileSystemStorage(_location=None_, _base\_url=None_, _file\_permissions\_mode=None_, _directory\_permissions\_mode=None_, _allow\_overwrite=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L19)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "Link to this definition")
The [`FileSystemStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "django.core.files.storage.FileSystemStorage") class implements basic file storage on a local filesystem. It inherits from [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") and provides implementations for all the public methods thereof.

Note

The `FileSystemStorage.delete()` method will not raise an exception if the given file name does not exist.

location[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L44)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.location "Link to this definition")
Absolute path to the directory that will hold the files. Defaults to the value of your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) setting.

base_url[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L48)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.base_url "Link to this definition")
URL that serves the files stored at this location. Defaults to the value of your [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) setting.

file_permissions_mode[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L54)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.file_permissions_mode "Link to this definition")
The file system permissions that the file will receive when it is saved. Defaults to [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_PERMISSIONS).

directory_permissions_mode[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L60)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.directory_permissions_mode "Link to this definition")
The file system permissions that the directory will receive when it is saved. Defaults to [`FILE_UPLOAD_DIRECTORY_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_DIRECTORY_PERMISSIONS).

allow_overwrite[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.allow_overwrite "Link to this definition")
Flag to control allowing saving a new file over an existing one. Defaults to `False`.

get_created_time(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/filesystem.py#L220)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage.get_created_time "Link to this definition")
Returns a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") of the system’s ctime, i.e. [`os.path.getctime()`](https://docs.python.org/3/library/os.path.html#os.path.getctime "(in Python v3.14)"). On some systems (like Unix), this is the time of the last metadata change, and on others (like Windows), it’s the creation time of the file.

The `InMemoryStorage` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#the-inmemorystorage-class "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

_class_ InMemoryStorage(_location=None_, _base\_url=None_, _file\_permissions\_mode=None_, _directory\_permissions\_mode=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/memory.py#L168)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage "Link to this definition")
The [`InMemoryStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage "django.core.files.storage.InMemoryStorage") class implements a memory-based file storage. It has no persistence, but can be useful for speeding up tests by avoiding disk access.

location[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/memory.py#L193)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage.location "Link to this definition")
Absolute path to the directory name assigned to files. Defaults to the value of your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) setting.

base_url[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/memory.py#L197)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage.base_url "Link to this definition")
URL that serves the files stored at this location. Defaults to the value of your [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) setting.

file_permissions_mode[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/memory.py#L203)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage.file_permissions_mode "Link to this definition")
The file system permissions assigned to files, provided for compatibility with `FileSystemStorage`. Defaults to [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_PERMISSIONS).

directory_permissions_mode[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/memory.py#L209)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.InMemoryStorage.directory_permissions_mode "Link to this definition")
The file system permissions assigned to directories, provided for compatibility with `FileSystemStorage`. Defaults to [`FILE_UPLOAD_DIRECTORY_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_DIRECTORY_PERMISSIONS).

The `Storage` class[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#the-storage-class "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

_class_ Storage[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L11)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "Link to this definition")
The [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") class provides a standardized API for storing files, along with a set of default behaviors that all other storage systems can inherit or override as necessary.

Note

When methods return naive `datetime` objects, the effective timezone used will be the current value of `os.environ['TZ']`; note that this is usually set from Django’s [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE).

delete(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L142)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.delete "Link to this definition")
Deletes the file referenced by `name`. If deletion is not supported on the target storage system this will raise `NotImplementedError` instead.

exists(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L150)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.exists "Link to this definition")
Returns `True` if a file referenced by the given name already exists in the storage system.

get_accessed_time(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L181)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_accessed_time "Link to this definition")
Returns a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") of the last accessed time of the file. For storage systems unable to return the last accessed time this will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(in Python v3.14)").

If [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, returns an aware `datetime`, otherwise returns a naive `datetime` in the local timezone.

get_alternative_name(_file\_root_, _file\_ext_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L67)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_alternative_name "Link to this definition")
Returns an alternative filename based on the `file_root` and `file_ext` parameters, an underscore plus a random 7 character alphanumeric string is appended to the filename before the extension.

get_available_name(_name_, _max\_length=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L75)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_available_name "Link to this definition")
Returns a filename based on the `name` parameter that’s free and available for new content to be written to on the target storage system.

The length of the filename will not exceed `max_length`, if provided. If a free unique filename cannot be found, a [`SuspiciousFileOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") exception will be raised.

If a file with `name` already exists, [`get_alternative_name()`](https://docs.djangoproject.com/en/6.0/howto/custom-file-storage/#django.core.files.storage.get_alternative_name "django.core.files.storage.get_alternative_name") is called to obtain an alternative name.

get_created_time(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L190)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_created_time "Link to this definition")
Returns a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") of the creation time of the file. For storage systems unable to return the creation time this will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(in Python v3.14)").

If [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, returns an aware `datetime`, otherwise returns a naive `datetime` in the local timezone.

get_modified_time(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L199)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_modified_time "Link to this definition")
Returns a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") of the last modified time of the file. For storage systems unable to return the last modified time this will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(in Python v3.14)").

If [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, returns an aware `datetime`, otherwise returns a naive `datetime` in the local timezone.

get_valid_name(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L60)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.get_valid_name "Link to this definition")
Returns a filename based on the `name` parameter that’s suitable for use on the target storage system.

generate_filename(_filename_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L117)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.generate_filename "Link to this definition")
Validates the `filename` by calling [`get_valid_name`](https://docs.djangoproject.com/en/6.0/howto/custom-file-storage/#django.core.files.storage.get_valid_name "django.core.files.storage.get_valid_name") and returns a filename to be passed to the [`save()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.save "django.core.files.storage.Storage.save") method.

The `filename` argument may include a path as returned by [`FileField.upload_to`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.upload_to "django.db.models.FileField.upload_to"). In that case, the path won’t be passed to [`get_valid_name`](https://docs.djangoproject.com/en/6.0/howto/custom-file-storage/#django.core.files.storage.get_valid_name "django.core.files.storage.get_valid_name") but will be prepended back to the resulting name.

The default implementation uses [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "(in Python v3.14)") operations. Override this method if that’s not appropriate for your storage.

listdir(_path_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L159)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.listdir "Link to this definition")
Lists the contents of the specified path, returning a 2-tuple of lists; the first item being directories, the second item being files. For storage systems that aren’t able to provide such a listing, this will raise a `NotImplementedError` instead.

open(_name_, _mode='rb'_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L20)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.open "Link to this definition")
Opens the file given by `name`. Note that although the returned file is guaranteed to be a `File` object, it might actually be some subclass. In the case of remote file storage this means that reading/writing could be quite slow, so be warned.

path(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L131)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.path "Link to this definition")
The local filesystem path where the file can be opened using Python’s standard `open()`. For storage systems that aren’t accessible from the local filesystem, this will raise `NotImplementedError` instead.

save(_name_, _content_, _max\_length=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L24)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.save "Link to this definition")
Saves a new file using the storage system, preferably with the name specified. If there already exists a file with this name `name`, the storage system may modify the filename as necessary to get a unique name. The actual name of the stored file will be returned.

The `max_length` argument is passed along to [`get_available_name()`](https://docs.djangoproject.com/en/6.0/howto/custom-file-storage/#django.core.files.storage.get_available_name "django.core.files.storage.get_available_name").

The `content` argument must be an instance of [`django.core.files.File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") or a file-like object that can be wrapped in `File`.

size(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L168)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.size "Link to this definition")
Returns the total size, in bytes, of the file referenced by `name`. For storage systems that aren’t able to return the file size this will raise `NotImplementedError` instead.

url(_name_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/files/storage/base.py#L174)[¶](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.url "Link to this definition")
Returns the URL where the contents of the file referenced by `name` can be accessed. For storage systems that don’t support access by URL this will raise `NotImplementedError` instead.

There are community-maintained solutions too!

Django has a vibrant ecosystem. There are storage backends highlighted on the [Community Ecosystem](https://www.djangoproject.com/community/ecosystem/#storage-and-static-files) page. The Django Packages [Storage Backends grid](https://djangopackages.org/grids/g/storage-backends/) has even more options for you!
