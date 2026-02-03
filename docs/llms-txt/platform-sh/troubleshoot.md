# Source: https://docs.upsun.com/domains/troubleshoot.md

# Source: https://docs.upsun.com/integrations/source/troubleshoot.md

# Source: https://docs.upsun.com/development/troubleshoot.md

# Source: https://docs.upsun.com/languages/php/troubleshoot.md

# Source: https://docs.upsun.com/add-services/mysql/troubleshoot.md

# Troubleshoot MySQL

For more general information, see how to [troubleshoot development](https://docs.upsun.com/development/troubleshoot.md).

## Lock wait timeout

If a process running in your application acquired a lock from MySQL for a long period of time,
you receive MySQL error messages like this:

```sql
SQLSTATE[HY000]: General error: 1205 Lock wait timeout exceeded;
```

This is typically caused by one of the following:

* There are multiple places acquiring locks in different order.
  For example, code path 1 first locks record A and then locks record B,
  while code path 2 first locks record B and then locks record A.
* There is a long running background process executed by your application that holds the lock until it ends.

If you're using [MariaDB 10+](https://docs.upsun.com/add-services/mysql.md), use the SQL query `SHOW FULL PROCESSLIST \G` to list DB queries waiting for locks.
To determine where to debug, find output like the following:

```sql

Command: Query
Time: ...
State: Waiting for table metadata lock
Info: SELECT ...

```

To find active background processes, run `ps aufx` on your application container.

Make sure that locks are acquired in a pre-defined order and released as soon as possible.

## Definer/invoker of view lack rights to use them

There is a single MySQL user, so you can not use "DEFINER" Access Control mechanism for Stored Programs and Views.

When creating a `VIEW`, you may need to explicitly set the `SECURITY` parameter to `INVOKER`:

```sql
CREATE OR REPLACE SQL SECURITY INVOKER
VIEW `view_name` AS
SELECT
```

## Server has gone away

### Disk space issues

Errors such as `PDO Exception 'MySQL server has gone away'` are usually the result of exhausting your available disk space.
Get an estimate of current disk usage using the CLI command `upsun db:size`.
Just keep in mind it's an estimate and not exact.

Allocate more space to the service by running the `upsun resources:set` command.
For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

As table space can grow rapidly,
it's usually advisable to make your database mount size twice the size reported by the `db:size` command.

You may want to add a [low-disk warning](https://docs.upsun.com../../integrations/notifications.md#low-disk-warning)
to learn about low disk space before it becomes an issue.

### Packet size limitations

`MySQL server has gone away` errors may be caused by the size of the database packets.
If so, the logs may show warnings like `Error while sending QUERY packet` before the error.

One way to resolve the issue is to use the [`max_allowed_packet` parameter](https://docs.upsun.com/add-services/mysql.md#configure-the-database).

### Worker timeout

`MySQL server has gone away` errors may be caused by server timeouts.
MySQL has a built-in timeout for idle connections, which defaults to 10 minutes.
Most typical web connections end long before that's ever approached,
but a long-running worker may idle and not need the database for longer than the timeout, leading to a "server has gone away" message.

The best approach is to wrap your connection logic in code that detects a "server has gone away" exception
and tries to re-establish the connection.

Alternatively, if your worker is idle for too long it can self-terminate.
Upsun automatically restarts the worker process and the new process can establish a new database connection.

## Too many connections

You may get the following [error message](https://mariadb.com/kb/en/e1040/): `Error 1040: Too many connections`.

A common way to solve this issue is to increase the `max_connections` property in your MariaDB service configuration.
However, on Upsun, you **cannot** configure `max_connections` directly.

### Quick fix

You cannot configure `max_connections` directly in Upsun service configurations.
However, to solve `Error 1040`, you can increase `max_connections` indirectly.

Given the following services configuration for MariaDB:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  mariadb:
    type: mariadb:11.8
    configuration:
      properties:
        max_allowed_packet: 16
```

And assuming you have set the resources for that service using the following CLI command:

```bash
upsun resources:set --size mariadb:1
```

`max_connections` in this case is `332` as [set by Upsun](#how-it-works):

To **increase** `max_connections`, you can **either**:

- **decrease** `max_allowed_packet` (for example, `16` → `15` results in `max_connections=355`)
- or **increase** `size` using the `resources:set` command (for example, `1` → `2`  results in `max_connections=500`)

### How it works

Behind the scenes, `max_connections` is calculated from values that you _can_ change:

1. **`max_allowed_packet`**: `max_allowed_packet` is [directly configurable](https://docs.upsun.com/add-services/mysql.md#configure-the-database) in your `.upsun/config.yaml` file with an integer value.
The default value of `16` is shown below to illustrate:

    ```yaml  {location=".upsun/config.yaml"}
    services:
      # The name of the service container. Must be unique within a project.
      mariadb:
        type: mariadb:11.8
        configuration:
          properties:
            max_allowed_packet: 16
    ```

1. **The memory available to the service**: Resources are provisioned to Upsun containers according to your definition via the API, often through the `resources:set` CLI command:

    ```bash
    upsun resources:set --size mariadb:1
    ```

    The memory for a given container from its `size` depends on its [container profile](https://docs.upsun.com/manage-resources/adjust-resources.md#advanced-container-profiles).

    For example, [MariaDB](https://docs.upsun.com/manage-resources/adjust-resources.md#default-container-profiles) has a [`HIGH_MEMORY` container profile](https://docs.upsun.com/manage-resources/adjust-resources.md#advanced-container-profiles).
    For `--size mariadb:1`, it means 1 CPU and 2432 MB of memory.

If we assume the configuration above, where:

- `--size  mariadb:1`, which we know is `2432` MB, referred to below as `application_size`
- `mariadb.configuration.properties.max_allowed_packet: 16`
- You are using the default `HIGH_MEMORY` profile assigned to MariaDB containers. [Changing the container profile](https://docs.upsun.com/manage-resources/adjust-resources.md#adjust-a-container-profile) changes the behavior below.

`max_allowed_packet` is `332`, which is determined by Upsun according to:

\begin{aligned}
\texttt{max_connections} = \text{int}\Biggl[ \min \left( \frac{\texttt{FREE_MEMORY}}{\texttt{max_allowed_packet}}, 500 \right) \Biggr]
\end{aligned}

This calculation uses three additional calculations:

\begin{aligned}
\texttt{FREE_MEMORY} = \texttt{AVAILABLE_MEMORY} - \left( 50 + \texttt{innodb_buffer_pool_size} \right) \newline \newline
\texttt{AVAILABLE_MEMORY} = (\texttt{application_size} * 2) + 512 \newline \newline
\texttt{innodb_buffer_pool_size} = \frac{\text{int}\left( 0.75 \cdot \texttt{application_size} \right)}{1024^{2}}
\end{aligned}

So for our current example, where:

\begin{aligned}
\texttt{application_size} = 2432 \newline
\texttt{max_allowed_packet} = 16
\end{aligned}

You get:

\begin{aligned}
\texttt{innodb_buffer_pool_size} = \frac{\text{int}\left( 0.75 \cdot \texttt{application_size} \right)}{1024^{2}} = \frac{\text{int}\left( 0.75 \cdot \texttt{1280} \right)}{1024^{2}} \approx 1.7395 \times 10^{-3}
\end{aligned}

\begin{aligned}
\texttt{AVAILABLE_MEMORY} = (\texttt{application_size} * 2) + 512 = (1280 * 2) + 512 = 5376
\end{aligned}

\begin{aligned}
\texttt{FREE_MEMORY} = \texttt{AVAILABLE_MEMORY} - \left( 50 + \texttt{innodb_buffer_pool_size} \right) \newline \newline
\texttt{FREE_MEMORY} = 3072 - \left( 50 + 0.0009155... \right) = 5325.998...
\end{aligned}

\begin{aligned}
\texttt{max_connections} = \text{int}\Biggl[ \min \left( \frac{\texttt{FREE_MEMORY}}{\texttt{max_allowed_packet}}, 500 \right) \Biggr] = \text{int}\Biggl[ \min \left( \frac{3021.999084}{16}, 500 \right) \Biggr] = \text{int}\Biggl[ 332.87... \Biggr]
\end{aligned}

\begin{aligned}
\texttt{max_connections} = 332
\end{aligned}

The following table provides additional example calculations of `max_connections` for all `size` settings
and for a number of `max_allow_packet` settings.

            MariaDB ``max_connections``
            ``application_size````size`` (memory in MB)

 0.1 (448 MB) | 0.25 (832 MB) | 0.5 (1408 MB) | 1 (2432 MB) | 2 (4032 MB) | 4 (6720 MB) | 6 (9024 MB) | 8 (11200 MB) |

 1(min) | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 |

 2 | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 |

 8 | 169 | 265 | 409 | 500 | 500 | 500 | 500 | 500 |

 16(default) | 84 | 132 | 204 | 332 | 500 | 500 | 500 | 500 |

 32 | 42 | 66 | 102 | 166 | 266 | 434 | 500 | 500 |

 64 | 21 | 33 | 51 | 83 | 133 | 217 | 289 | 357 |

 100(max) | 13 | 21 | 32 | 53 | 85 | 139 | 185 | 228 |

**Note**: 

The maximum value for ``max_connections`` is 500, indicated with italicized integers in the table.

Also, you can **increase** ``max_connections`` in your environments by either:

 - **decreasing** the ``max_allow_packet`` value in your service configuration
 - or **increasing** the service’s resources by using the CLI command ``resources:set`` and the ``--size`` flag


