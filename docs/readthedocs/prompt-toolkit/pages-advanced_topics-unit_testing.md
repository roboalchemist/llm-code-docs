# Unit testing

Testing user interfaces is not always obvious. Here are a few tricks for
testing prompt_toolkit applications.

## PosixPipeInput and DummyOutput

During the creation of a prompt_toolkit
`Application`, we can specify what input and
output device to be used. By default, these are output objects that correspond
with sys.stdin and sys.stdout. In unit tests however, we want to replace
these.

- 

For the input, we want a “pipe input”. This is an input device, in which we
can programmatically send some input. It can be created with
`create_pipe_input()`, and that return either a
`PosixPipeInput` or a
`Win32PipeInput` depending on the
platform.

- 

For the output, we want a `DummyOutput`. This is
an output device that doesn’t render anything. We don’t want to render
anything to sys.stdout in the unit tests.

Note

Typically, we don’t want to test the bytes that are written to
sys.stdout, because these can change any time when the rendering
algorithm changes, and are not so meaningful anyway. Instead, we want to
test the return value from the
`Application` or test how data
structures (like text buffers) change over time.