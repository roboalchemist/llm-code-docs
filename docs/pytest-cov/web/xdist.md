# Distributed testing (xdist)

## “load” mode

Distributed testing with dist mode set to “load” will report on the combined coverage of all workers.
The workers may be spread out over any number of hosts and each worker may be located anywhere on the
file system.  Each worker will have its subprocesses measured.

Running distributed testing with dist mode set to load:

```
pytest --cov=myproj -n 2 tests/

```
