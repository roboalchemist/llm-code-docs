# luigi.format

Functions

`get_default_format`()

Classes

`BaseWrapper`(stream, *args, **kwargs)

`Bzip2Format`()

`ChainFormat`(*args, **kwargs)

`FileWrapper`(file_object)

Wrap file in a "real" so stuff can be added to it after creation.

`Format`()

Interface for format specifications.

`GzipFormat`([compression_level])

`InputPipeProcessWrapper`(command[, input_pipe])

Initializes a InputPipeProcessWrapper instance.

`MixedUnicodeBytesFormat`(*args, **kwargs)

`MixedUnicodeBytesWrapper`(stream[, encoding])

`NewlineFormat`(*args, **kwargs)

`NewlineWrapper`(stream[, newline])

`NopFormat`()

`OutputPipeProcessWrapper`(command[, output_pipe])

`TextFormat`(*args, **kwargs)

`TextWrapper`(stream, *args, **kwargs)

`WrappedFormat`(*args, **kwargs)

class luigi.format.FileWrapper(*file_object*)

Wrap file in a “real” so stuff can be added to it after creation.

class luigi.format.InputPipeProcessWrapper(*command*, *input_pipe=None*)

Initializes a InputPipeProcessWrapper instance.

Parameters:

**command** – a subprocess.Popen instance with stdin=input_pipe and
stdout=subprocess.PIPE.
Alternatively, just its args argument as a convenience.

create_subprocess(*command*)

http://www.chiark.greenend.org.uk/ucgi/~cjwatson/blosxom/2009-07-02-python-sigpipe.html

close()

readable()

writable()

seekable()

class luigi.format.OutputPipeProcessWrapper(*command*, *output_pipe=None*)

WRITES_BEFORE_FLUSH = 10000

write(**args*, ***kwargs*)

writeLine(*line*)

close()

abort()

readable()

writable()

seekable()

class luigi.format.BaseWrapper(*stream*, **args*, ***kwargs*)

class luigi.format.NewlineWrapper(*stream*, *newline=None*)

read(*n=-1*)

writelines(*lines*)

write(*b*)

class luigi.format.MixedUnicodeBytesWrapper(*stream*, *encoding=None*)

write(*b*)

writelines(*lines*)

class luigi.format.Format

Interface for format specifications.

classmethod pipe_reader(*input_pipe*)

classmethod pipe_writer(*output_pipe*)

class luigi.format.ChainFormat(**args*, ***kwargs*)

pipe_reader(*input_pipe*)

pipe_writer(*output_pipe*)

class luigi.format.TextWrapper(*stream*, **args*, ***kwargs*)

class luigi.format.NopFormat

pipe_reader(*input_pipe*)

pipe_writer(*output_pipe*)

class luigi.format.WrappedFormat(**args*, ***kwargs*)

pipe_reader(*input_pipe*)

pipe_writer(*output_pipe*)

class luigi.format.TextFormat(**args*, ***kwargs*)

input = 'unicode'

output = 'bytes'

wrapper_cls

alias of `TextWrapper`

class luigi.format.MixedUnicodeBytesFormat(**args*, ***kwargs*)

output = 'bytes'

wrapper_cls

alias of `MixedUnicodeBytesWrapper`

class luigi.format.NewlineFormat(**args*, ***kwargs*)

input = 'bytes'

output = 'bytes'

wrapper_cls

alias of `NewlineWrapper`

class luigi.format.GzipFormat(*compression_level=None*)

input = 'bytes'

output = 'bytes'

pipe_reader(*input_pipe*)

pipe_writer(*output_pipe*)

class luigi.format.Bzip2Format

input = 'bytes'

output = 'bytes'

pipe_reader(*input_pipe*)

pipe_writer(*output_pipe*)

luigi.format.get_default_format()