# Source: https://conform.guide/file-upload

# File Upload 

To handle file uploads, the form [encType] attribute must be set to `multipart/form-data` and the method must be `POST`.

## [\#](/file-upload#configuration)Configuration 

Setting up a file input is no different from other inputs.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5const schema = z.object(),
7});
8
9function Example() ) );
13    },
14  });
15
16  return (
17    <form method="POST" encType="multipart/form-data" id=>
18      <div>
19        <label>Profile</label>
20        <input type="file" name= />
21        <div></div>
22      </div>
23      <button>Upload</button>
24    </form>
25  );
26}
```

## [\#](/file-upload#multiple-files)Multiple files 

To allow uploading multiple files, you need to set the [multiple] attribute on the file input. It is important to note that the errors on the field metadata might not include all the errors on each file. As the errors from both yup and zod are mapped based on the corresponding paths and the errors of each file will be mapped to its corresponding index, e.g. `files[0]` instead of the array itself, e.g. `files`. If you want to display all the errors, you can consider using the [allErrors] property on the field metadata instead.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5const schema = z.object();
18
19function Example() ) );
23    },
24  });
25
26  return (
27    <form method="POST" encType="multipart/form-data" id=>
28      <div>
29        <label>Mutliple Files</label>
30        <input type="file" name= multiple />
31        <div></div>
32      </div>
33      <button>Upload</button>
34    </form>
35  );
36}
```