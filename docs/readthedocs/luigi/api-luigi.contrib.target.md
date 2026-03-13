# luigi.contrib.target

Classes

`CascadingClient`(clients[, method_names])

A FilesystemClient that will cascade failing function calls through a list of clients.

class luigi.contrib.target.CascadingClient(*clients*, *method_names=None*)

A FilesystemClient that will cascade failing function calls through a list of clients.

Which clients are used are specified at time of construction.

ALL_METHOD_NAMES = ['exists', 'rename', 'remove', 'chmod', 'chown', 'count', 'copy', 'get', 'put', 'mkdir', 'list', 'listdir', 'getmerge', 'isdir', 'rename_dont_move', 'touchz']