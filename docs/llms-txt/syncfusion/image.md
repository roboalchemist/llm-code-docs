# Source: https://docs.syncfusion.com/document-processing/word/word-processor/wpf/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/uwp/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/image.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/image.md

# Images

Document Editor supports common raster format images like PNG, BMP, JPEG, SVG and GIF. You can insert an image file or online image in the document using the `insertImage()` method.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<input type="file" id="insertImageButton" style="position:fixed; left:-110em" accept=".jpg,.jpeg,.png,.bmp" />
<ejs-button id="insert_picture">Image</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableImageResizer=true enableEditorHistory=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        document.getElementById('insert-picture').addEventListener('click', function () {
            var pictureUpload = document.getElementById("insertImageButton");
            pictureUpload.value = '';
            pictureUpload.click();
        });
        document.getElementById('insertImageButton').addEventListener('change', onInsertImage);
        function onInsertImage(args) {
            if (navigator.userAgent.match('Chrome') || navigator.userAgent.match('Firefox') || navigator.userAgent.match('Edge') || navigator.userAgent.match('MSIE') || navigator.userAgent.match('.NET')) {
                if (args.target.files[0]) {
                    var path = args.target.files[0];
                    var reader = new FileReader();
                    reader.onload = function (frEvent) {
                        var base64String = frEvent.target.result;
                        var image = document.createElement('img');
                        image.addEventListener('load', function () {
                            documenteditor.editor.insertImage(base64String, this.width, this.height);
                        })
                        image.src = base64String;
                    };
                    reader.readAsDataURL(path);
                }
                //Safari does not Support FileReader Class
            } else {
                var image = document.createElement('img');
                image.addEventListener('load', function () {
                    documenteditor.editor.insertImage(args.target.value);
                })
                image.src = args.target.value;
            }
        }

    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Image.cs" %}
{% endhighlight %}{% endtabs %}


Image files will be internally converted to base64 string. Whereas, online images are preserved as URL.

## Image resizing

Document editor provides built-in image resizer that can be injected into your application based on the requirements. This allows to resize the image by dragging the resizing points using mouse or touch interactions. This resizer appears as follows.

![Image](images/image.JPG)

## Changing size

Document editor exposes API to get or set the size of the selected image.

```typescript
documenteditor.selection.imageFormat.width = 800;
documenteditor.selection.imageFormat.height = 800;
```

N> Images are stored and processed (read/write) as base64 string in DocumentEditor. The online image URL is preserved as a URL in DocumentEditor upon saving.

## Text wrapping style

Text wrapping refers to how images fit with surrounding text in a document. [Refer to this page](../asp-net-core/text-wrapping-style) for more information about text wrapping styles available in Word documents.

## Positioning the image

DocumentEditor preserves the position properties of the image and displays the image based on position properties. It does not support modifying the position properties. Whereas the image will be automatically moved along with text edited if it is positioned relative to the line or paragraph.

## See Also

* [Feature modules](../asp-net-core/feature-module)
