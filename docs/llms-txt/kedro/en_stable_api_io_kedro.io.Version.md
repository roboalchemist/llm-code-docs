# Source: https://docs.kedro.org/en/stable/api/io/kedro.io.Version/index.md

## kedro.io.Version

Bases: `namedtuple('Version', ['load', 'save'])`

This namedtuple is used to provide load and save versions for versioned datasets. If `Version.load` is None, then the latest available version is loaded. If `Version.save` is None, then save version is formatted as YYYY-MM-DDThh.mm.ss.sssZ of the current timestamp.

### __slots__

```
__slots__ = ()
```
