# Source: https://ml-explore.github.io/mlx/build/html/dev/metal_logging.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/dev/metal_logging.rst "Download source file")
- [ ] [.pdf]

[ ]

# Metal Logging

# Metal Logging[\#](#metal-logging "Link to this heading")

In debug builds, MLX compiles Metal kernels with [`os_log`] enabled so shader warnings and debug messages are visible during development.

Note

Metal logging is only available with Metal 3.2 or higher (macOS 15 and up, iOS 18 and up).

To enable logging from kernels, first make sure to build in debug mode:

    DEBUG=1 python -m pip install -e .

Then, in the kernel source code include MLX's logging shim and use [`mlx::os_log`]:

    #include "mlx/backend/metal/kernels/logging.h"

    constant mlx::os_log logger("mlx", "my_kernel");

    kernel void my_kernel(/* ... */) 

When you run the program, set the Metal log level to your desired level and forward logs to [`stderr`]:

    MTL_LOG_LEVEL=MTLLogLevelDebug MTL_LOG_TO_STDERR=1 python script.py

See the [Metal logging guide](https://developer.apple.com/documentation/metal/logging-shader-debug-messages) for more details.

[](metal_debugger.html "previous page")

previous

Metal Debugger

[](custom_metal_kernels.html "next page")

next

Custom Metal Kernels

By MLX Contributors

© Copyright 2023, Apple.\