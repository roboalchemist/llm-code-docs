# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/python/procedure-python-read-files.md

# Reading files with a Python stored procedure

## Reading from stages

By using the `SnowflakeFile` class in the Snowpark `snowflake.snowpark.files` module, your Python handler can dynamically read a
file [from either internal or external stages](../../../sql-reference/sql/create-stage.md).

Snowflake supports reading files with `SnowflakeFile` for both stored procedures and user-defined functions. For more information
about reading files in your handler code, as well as more examples, refer to [Reading a File with a Python UDF Handler](../../udf/python/udf-python-examples.md).

## Example

This example demonstrates how to create and call an [owner’s rights stored procedure](../stored-procedures-rights.md)
that reads a file using the `SnowflakeFile` class.

Create the stored procedure with an in-line handler, specifying the input mode as binary by passing `rb` for the `mode` argument:

```sqlexample-python
CREATE OR REPLACE PROCEDURE calc_phash(file_path string)
RETURNS STRING
LANGUAGE PYTHON
RUNTIME_VERSION = '3.9'
PACKAGES = ('snowflake-snowpark-python','imagehash','pillow')
HANDLER = 'run'
AS
$$
from PIL import Image
import imagehash
from snowflake.snowpark.files import SnowflakeFile

def run(ignored_session, file_path):
    with SnowflakeFile.open(file_path, 'rb') as f:
        return imagehash.average_hash(Image.open(f))
$$;
```

Call the stored procedure:

```sqlexample
CALL calc_phash(build_scoped_file_url(@my_files, 'my_image.jpg'));
```
