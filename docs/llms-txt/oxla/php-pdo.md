# Source: https://docs.oxla.com/clients-tools/language-clients/php-pdo.md

# PHP (PDO)

## Overview

[The PHP Data Objects (PDO)](https://www.php.net/manual/en/book.pdo.php) is an extension, which supports PostgreSQL protocol implemented in Oxla and provides consistent interface for accessing databases in PHP. This page and its sections describe how to use PHP PDO with Oxla and also lists unsupported functions and structures.

## Establishing connection

```PHP  theme={null}
conn = new PDO(
    "pgsql:host={oxla_host};port={oxla_port};dbname=oxla",
    {oxla_user},
    {oxla_password},
    [ 
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => true,
    ]);
```

Note that the `PDO::ATTR_EMULATE_PREPARES` attribute is set to `true`, which is required in Oxla to ensure stability of query execution. Without this attribute setup, you may encounter `prepared statement` errors during queries execution:

```
    ERROR: prepared statement [...]
```

<Info> If you are running Oxla Cloud, you can append <code>`sslmode=verify-full;sslrootcert=\{path to ssl cert from SaaS\}`</code> to the first parameter of <code>PDO</code> to ensure full SSL endpoint verification and encryption. </Info>

## Example usage

This example shows basic query execution, once the connection has been established:

```PHP  theme={null}
$stmt = $conn->prepare("SELECT :number as num;", [PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY]);
$stmt->execute(['number' => 1234]);
$res = $stmt->fetchAll();
print_r($res)
```

## Unsupported Functions & Structures

Here you can find a list of functions and potentially related structures, that we currently do not support when working with Oxla and PHP PDO:

* `PDO::pgsqlLOBCreate`, `pgsqlLOBOpen` - [Large Objects](https://www.postgresql.org/docs/current/largeobjects.html)
* `PDO::pgsqlGetPid` - [returning processes ID](https://www.php.net/manual/en/function.pg-get-pid.php)
* `PDO::pgsqlCopytFromFile`, `PDO::pgsqlCopytFromArray` - [copy from STDIN](https://www.postgresql.org/docs/current/sql-copy.html)
* `PDO::pgsqlCopytToFile` - [copy to STDIN](https://www.postgresql.org/docs/current/sql-copy.html)
* `PDO::pgsqlCopytToArray` - [copy to STDOUT](https://www.postgresql.org/docs/current/sql-copy.html)
* `PDO::pgsqlGetNotify` - [`LISTEN`](https://www.postgresql.org/docs/current/sql-listen.html) and [`NOTIFY`](https://www.postgresql.org/docs/current/sql-notify.html) channel commands
* `PDO::lastInsertId` - [SEQUENCES](https://www.postgresql.org/docs/current/sql-createsequence.html)
* `PDO::beginTransaction`, `PDO::inTransaction`, `PDO::commit`, `PDO::rollBack` - [Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
* `PDOStatement::rowCount` - returns improper number of rows for `DELETE`, `UPDATE`, `INSERT INTO ... (SELECT)` and `COPY` statements
