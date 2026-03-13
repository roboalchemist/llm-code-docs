# luigi.contrib.opener

OpenerTarget support, allows easier testing and configuration by abstracting
out the LocalTarget, S3Target, and MockTarget types.

Example:

```
from luigi.contrib.opener import OpenerTarget

OpenerTarget('/local/path.txt')
OpenerTarget('s3://zefr/remote/path.txt')

```