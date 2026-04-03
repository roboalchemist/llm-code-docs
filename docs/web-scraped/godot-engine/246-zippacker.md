# ZIPPacker

# ZIPPacker
Inherits:RefCounted<Object
Allows the creation of ZIP files.

## Description
This class implements a writer that allows storing the multiple blobs in a ZIP archive. See alsoZIPReaderandPCKPacker.
```
# Create a ZIP archive with a single file at its root.
func write_zip_file():
    var writer = ZIPPacker.new()
    var err = writer.open("user://archive.zip")
    if err != OK:
        return err
    writer.start_file("hello.txt")
    writer.write_file("Hello World".to_utf8_buffer())
    writer.close_file()

    writer.close()
    return OK
```

## Properties

| int | compression_level | -1 |

compression_level

## Methods

| Error | close() |
|---|---|
| Error | close_file() |
| Error | open(path:String, append:ZipAppend= 0) |
| Error | start_file(path:String) |
| Error | write_file(data:PackedByteArray) |

Error
close()
Error
close_file()
Error
open(path:String, append:ZipAppend= 0)
Error
start_file(path:String)
Error
write_file(data:PackedByteArray)

## Enumerations
enumZipAppend:🔗
ZipAppendAPPEND_CREATE=0
Create a new zip archive at the given path.
ZipAppendAPPEND_CREATEAFTER=1
Append a new zip archive to the end of the already existing file at the given path.
ZipAppendAPPEND_ADDINZIP=2
Add new files to the existing zip archive at the given path.
enumCompressionLevel:🔗
CompressionLevelCOMPRESSION_DEFAULT=-1
Start a file with the default Deflate compression level (6). This is a good compromise between speed and file size.
CompressionLevelCOMPRESSION_NONE=0
Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).
CompressionLevelCOMPRESSION_FAST=1
Start a file with the fastest Deflate compression level (1). This is fast to compress, but results in larger file sizes thanCOMPRESSION_DEFAULT. Decompression speed is generally unaffected by the chosen compression level.
CompressionLevelCOMPRESSION_BEST=9
Start a file with the best Deflate compression level (9). This is slow to compress, but results in smaller file sizes thanCOMPRESSION_DEFAULT. Decompression speed is generally unaffected by the chosen compression level.

## Property Descriptions
intcompression_level=-1🔗
- voidset_compression_level(value:int)
voidset_compression_level(value:int)
- intget_compression_level()
intget_compression_level()
The compression level used whenstart_file()is called. UseCompressionLevelas a reference.

## Method Descriptions
Errorclose()🔗
Closes the underlying resources used by this instance.
Errorclose_file()🔗
Stops writing to a file within the archive.
It will fail if there is no open file.
Erroropen(path:String, append:ZipAppend= 0)🔗
Opens a zip file for writing at the given path using the specified write mode.
This must be called before everything else.
Errorstart_file(path:String)🔗
Starts writing to a file within the archive. Only one file can be written at the same time.
Must be called afteropen().
Errorwrite_file(data:PackedByteArray)🔗
Write the givendatato the file.
Needs to be called afterstart_file().

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.