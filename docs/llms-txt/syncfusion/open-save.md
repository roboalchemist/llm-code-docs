# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/open-save.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/open-save.md

# Open and Save in ASP.NET Core Spreadsheet control

To import an excel file, it needs to be read and converted to client side Spreadsheet model. The converted client side Spreadsheet model is sent as JSON which is used to render Spreadsheet. Similarly, when you save the Spreadsheet, the client Spreadsheet model is sent to the server as JSON for processing and saved. Server configuration is used for this process.

## Open

The Spreadsheet component opens an Excel document with its data, style, format, and more. To enable this feature, set [`allowOpen`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowOpen) as `true` and assign service url to the [`openUrl`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_OpenUrl) property.

**User Interface**:

In user interface you can open an Excel document by clicking `File > Open` menu item in ribbon.

The following sample shows the `Open` option by using the [`openUrl`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_OpenUrl) property in the Spreadsheet control. You can also use the [`beforeOpen`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeOpen) event to trigger before opening an Excel file.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" allowOpen = "true" beforeOpen="beforeOpen">

</ejs-spreadsheet>

<script>

    function beforeOpen(args) {
        // your code snippets here
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="Opencontroller.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}



Find the below table for the beforeOpen event arguments.

 | **Parameter** | **Type** | **Description** |
| ----- | ----- | ----- |
| file | FileList or string or File | To get the file stream. `FileList` -  contains length and item index. <br/> `File` - specifies the file lastModified and file name. |
| cancel | boolean | To prevent the open operation. |
| requestData | object |  To provide the Form data. |

N> * Use `Ctrl + O` keyboard shortcut to open Excel documents.
<br/> * The default value of the [allowOpen](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowOpen) property is `true`. For demonstration purpose, we have showcased the [allowOpen](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowOpen) property in previous code snippet.

### Open an excel file using a file uploader

If you explore your machine to select and upload an excel document using the file uploader, you will receive the uploaded document as a raw file in the `success` event of the file uploader. In this `success` event, you should pass the received raw file as an argument to the Spreadsheet's `open` method to see the appropriate output.

The following code example shows how to import an excel document using file uploader in spreadsheet.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
@using Syncfusion.EJ2
@{
var asyncSettings = new Syncfusion.EJ2.Inputs.UploaderAsyncSettings { SaveUrl =
"https://services.syncfusion.com/aspnet/production/api/FileUploader/Save", RemoveUrl =
"https://services.syncfusion.com/aspnet/production/api/FileUploader/Remove" };
}
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open">

</ejs-spreadsheet>
<ejs-uploader id="UploadFiles" success="onSuccess" asyncSettings="@asyncSettings" allowedExtensions=".xls, .xlsx, .csv">
</ejs-uploader>

<script>
    function onSuccess(args){
        var ssObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        if (args.operation === 'upload')
            ssObj.open({ file: args.file.rawFile });
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Opencontroller.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

    public void Save(IList<IFormFile> UploadFiles)
        {
            long size = 0;
            try
            {
                foreach (var file in UploadFiles)
                {
                    var filename = ContentDispositionHeaderValue
                                    .Parse(file.ContentDisposition)
                                    .FileName
                                    .Trim('"');
                    filename = hostingEnv.WebRootPath + $@"\{filename}";
                    size += file.Length;
                    if (!System.IO.File.Exists(filename))
                    {
                        using (FileStream fs = System.IO.File.Create(filename))
                        {
                            //file.CopyTo(fs);
                            //fs.Flush();
                        }
                    }
                    else
                    {
                        using (FileStream fs = System.IO.File.Open(filename, FileMode.Append))
                        {
                            //file.CopyTo(fs);
                            //fs.Flush();
                        }
                    }
                }
            }
            catch (Exception e)
            {
                Response.Clear();
                Response.StatusCode = 204;
                Response.HttpContext.Features.Get<IHttpResponseFeature>().ReasonPhrase = "File failed to upload";
                Response.HttpContext.Features.Get<IHttpResponseFeature>().ReasonPhrase = e.Message;
            }
        }


public void Remove(string UploadFile)
{
    try
       {
        var filename = hostingEnv.WebRootPath + $@"\{UploadFile}";
        if (System.IO.File.Exists(filename))
        {
            System.IO.File.Delete(filename);
        }
        }
        catch (Exception e)
            {
                Response.Clear();
                Response.StatusCode = 200;
                Response.HttpContext.Features.Get<IHttpResponseFeature>().ReasonPhrase = "File removed successfully";
                Response.HttpContext.Features.Get<IHttpResponseFeature>().ReasonPhrase = e.Message;
            }
}
{% endhighlight %}
{% endtabs %}

### Open an external URL excel file while initial load

You can achieve to access the remote excel file by using the [`created`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_Created) event. In this event you can fetch the excel file and convert it to a blob. Convert this blob to a file and `open` this file by using Spreadsheet component open method.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openUrl="Open" allowOpen ="true" created="created">

</ejs-spreadsheet>

<script>

    function created() {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        fetch("https://cdn.syncfusion.com/scripts/spreadsheet/Sample.xlsx") // fetch the remote url
            .then((response) => {
                response.blob().then((fileBlob) => { // convert the excel file to blob
                    var file = new File([fileBlob], "Sample.xlsx"); //convert the blob into file
                    spreadsheet.open({ file: file }); // open the file into Spreadsheet
                })
            })
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="Opencontroller.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}

### Open an excel file from blob data

By default, the Spreadsheet control provides an option to browse files from the local file system and open them within the control. If you want to open an Excel file from blob data, you need to fetch the blob data from the server or another source and convert this blob data into a `File` object. Then, you can use the `open` method in the Spreadsheet control to load that `File` object.

Please find the code to fetch the blob data and load it into the Spreadsheet control below.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" saveUrl="Home/Save" created="created">

</ejs-spreadsheet>

<script>
    var base64String = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,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";
    function created() {
        var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        fetch(base64String)
            // To obtain blob data from base64 string.
            .then((response) => response.blob())
            .then((fileBlob) => {
                // To convert obtained blob data as a file.
                var file = new File([fileBlob], 'Sample.xlsx');
                spreadsheetObj.open({ file: file });
            });
    }

</script>

{% endhighlight %}
{% highlight c# tabtitle="OpenController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}
{% endhighlight %}
{% endtabs %}

### Open an Excel file located on a server

By default, the Spreadsheet control provides an option to browse files from the local file system and open them within the control. If you want to load an Excel file located on a server, you need to configure the server endpoint to fetch the Excel file from the server location, process it using `Syncfusion.EJ2.Spreadsheet.AspNet.Core`, and send it back to the client side as `JSON data`. On the client side, you should use the `openFromJson` method to load that `JSON data` into the Spreadsheet control.

```csharp
    public IActionResult Open([FromBody] FileOptions options)
    {
        OpenRequest open = new OpenRequest();
        string filePath = _env.ContentRootPath.ToString() + "\\Files\\" + options.FileName + ".xlsx";
        // Getting the file stream from the file path.
        FileStream fileStream = new FileStream(filePath, FileMode.Open);
        // Converting "MemoryStream" to "IFormFile".
        IFormFile formFile = new FormFile(fileStream, 0, fileStream.Length, "", options.FileName + ".xlsx"); 
        open.File = formFile;
        // Processing the Excel file and return the workbook JSON.
        var result = Workbook.Open(open);
        fileStream.Close();
        return Content(result);
    }

    public class FileOptions
    {
        public string FileName { get; set; } = string.Empty;
    }
```

```js

    // Fetch call to server to load the Excel file.
    fetch('Home/Open', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ FileName: 'Sample' }),
    })
    .then((response) => response.json())
    .then((data) => {
            // Load the JSON data into spreadsheet.
            spreadsheet.openFromJson({ file: data });
    })

```

You can find the server endpoint code to fetch and process the Excel file in this [attachment](https://www.syncfusion.com/downloads/support/directtrac/general/ze/WebApplication1_(1)-880363187).

### Open an excel file using a hosted web service in AWS Lambda

Before proceeding with the opening process, you should deploy the spreadsheet open/save web API service in AWS Lambda. To host the open/save web service in the AWS Lambda environment, please refer to the following KB documentation.

After deployment, you will get the AWS service URL for the open and save actions. Before opening the Excel file with this hosted open URL, you need to prevent the default file opening process to avoid getting a corrupted file on the open service end. The spreadsheet component appends the file to the `formData` and sends it to the open service, which causes the file to get corrupted. To prevent this, set the `args.cancel` value to `true` in the [`beforeOpen`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeOpen) event. After that, you will get the selected file in the `beforeOpen` event argument. Then, convert this file into a base64 string and send it to the open service URL using a fetch request.

On the open service end, convert the base64 string back to a file and pass it as an argument to the workbook `Open` method. The open service will process the file and return the spreadsheet data in JSON format. You will then receive this JSON data in the fetch success callback. Finally, use the `openFromJson` method to load this JSON data into the spreadsheet component.

The following code example shows how to open an Excel file using a hosted web service in AWS Lambda, as mentioned above.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-spreadsheet id="spreadsheet" openUrl="https://xxxxxxxxxxxxxxxxxx.amazonaws.com/Prod/api/spreadsheet/open" allowOpen = "true" beforeOpen="beforeOpen">

</ejs-spreadsheet>

<script>

    function beforeOpen(eventArgs) {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        eventArgs.cancel = true; // To prevent the default open action.
        if (eventArgs.file) {
            const reader = new FileReader();
            reader.readAsDataURL(eventArgs.file);
            reader.onload = () => {
                // Removing the xlsx file content-type.
                const base64Data = reader.result.replace('data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,', '');
                openExcel({
                    file: base64Data,
                    extension: eventArgs.file.name.slice(eventArgs.file.name.lastIndexOf('.') + 1),
                    password: eventArgs.password || ''
                });
            };
        }
    }
    function openExcel (requestData) {
        // Fetch call to AWS server for open processing.
        fetch('https://xxxxxxxxxxxxxxxxxx.amazonaws.com/Prod/api/spreadsheet/open', {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify(requestData)
        }).then((response) => {
            if (response.ok) {
                return response.json();
            }
        }).then((data) => {
            // Loading the JSON data into our spreadsheet.
            if (data.Workbook && data.Workbook.sheets) {
                spreadsheet.openFromJson({ file: data });
            }
        }).catch((error) => {
            console.log(error);
        });
    };

</script>

{% endhighlight %}
{% endtabs %}

### Open an excel file from Base64 string data

In the Syncfusion<sup style="font-size:70%">&reg;</sup> Spreadsheet component, there is no direct option to open data as a `Base64` string. To achieve this, the `import()` function fetches the `Base64` string, converts it to a Blob, creates a File object from the Blob, and then opens it using the `open` method in the spreadsheet.

The following code example shows how to open the spreadsheet data as base64 string.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="importBtn" content="Import Base64"></ejs-button>
<ejs-button id="exportBtn" content="Export as Base64"></ejs-button>
<ejs-spreadsheet id="spreadsheet" beforeSave="beforeSave" saveComplete="saveComplete" openUrl="Home/Open">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
					<e-spreadsheet-columns>
						<e-spreadsheet-column width="130"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
					</e-spreadsheet-columns>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    var base64String;
    function beforeSave(args) {
        args.needBlobData = true; // To trigger the saveComplete event.
        args.isFullPost = false; // Get the spreadsheet data as blob data in the saveComplete event.
    }

    function saveComplete(args) {
        // Convert blob data to base64 string.
        var reader = new FileReader();
        reader.readAsDataURL(args.blobData);
        reader.onloadend = function () {
            base64String = reader.result;
        };
    }

    document.getElementById("importBtn").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        // Open the file based on saved base64 string.
        fetch(base64String)
            .then((response) => response.blob())
            .then((fileBlob) => {
                var file = new File([fileBlob], 'Sample.xlsx');
                spreadsheetObj.open({ file: file });
            });
    });
    document.getElementById("exportBtn").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.save({
            url: 'https://localhost:{{port number}}/Home/Save',
            fileName: 'Worksheet',
            saveType: 'Xlsx',
        }); // Specifies the save URL, file name, file type need to be saved.
        // Logs base64 string into the console.
        console.log('Base64 String - ', base64String);
    });
</script>

{% endhighlight %}
{% highlight c# tabtitle="OpenController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}

public IActionResult Index()
{
    List<object> defaultData = new List<object>()
    {
        new { ItemName= "Casual Shoes", Date= "02/14/2014", Time= "11:34:32 AM", Quantity= "10", Price= "20", Amount= "200", Discount= "1", Profit= "10" },
        new { ItemName= "Sports Shoes", Date= "06/11/2014", Time= "05:56:32 AM", Quantity= "20", Price= "30", Amount= "600", Discount= "5", Profit= "50" },
        new { ItemName= "Formal Shoes", Date= "07/27/2014", Time= "03:32:44 AM", Quantity= "20", Price= "15", Amount= "300", Discount= "7", Profit= "27" },
        new { ItemName= "Sandals & Floaters", Date= "11/21/2014", Time= "06:23:54 AM", Quantity= "15", Price= "20", Amount= "300", Discount= "11", Profit= "67" },
        new { ItemName= "Flip- Flops & Slippers", Date= "06/23/2014", Time= "12:43:59 AM", Quantity= "30", Price= "10", Amount= "300", Discount= "10", Profit= "70" },
        new { ItemName= "Sneakers", Date= "07/22/2014", Time= "10:55:53 AM", Quantity= "40", Price= "20", Amount= "800", Discount= "13", Profit= "66" },
        new { ItemName= "Running Shoes", Date= "02/04/2014", Time= "03:44:34 AM", Quantity= "20", Price= "10", Amount= "200", Discount= "3", Profit= "14" },
        new { ItemName= "Loafers", Date= "11/30/2014", Time= "03:12:52 AM", Quantity= "31", Price= "10", Amount= "310", Discount= "6", Profit= "29" },
        new { ItemName= "Cricket Shoes", Date= "07/09/2014", Time= "11:32:14 AM", Quantity= "41", Price= "30", Amount= "1210", Discount= "12", Profit= "166" },
        new { ItemName= "T-Shirts", Date= "10/31/2014", Time= "12:01:44 AM", Quantity= "50", Price= "10", Amount= "500", Discount= "9", Profit= "55" }
    };
    ViewBag.DefaultData = defaultData;
    return View();

}
{% endhighlight %}
{% endtabs %}

### Open excel file into a read-only mode

You can open excel file into a read-only mode by using the [`openComplete`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_OpenComplete) event. In this event, you must protect all the sheets and lock its used range cells by using `protectSheet` and `lockCells` methods.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" openComplete="openComplete" openUrl="Home/Open">

</ejs-spreadsheet>

<script>
    function openComplete(args) {
        var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
      var sheets = spreadsheet.sheets;
      for (var index = 0; index < sheets.length; index++) {
          var name = spreadsheet.sheets[index].name;
          var protectSetting = {
              selectCells: true,
              formatCells: false,
          };

          //To protect the sheet using sheet name
          spreadsheet.protectSheet(name, protectSetting);
          var address = ejs.spreadsheet.getRangeAddress([
              0,
              0,
              sheets[index].usedRange.rowIndex,
              sheets[index].usedRange.colIndex,
          ]);
          //To lock the used range cells
          spreadsheet.lockCells(name + '!' + address, true);
      }

    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Opencontroller.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}

### Configure JSON deserialization options

Previously, when opening a workbook JSON object into the Spreadsheet using the `openFromJson` method, the entire workbook, including all features specified in the JSON object, was processed and loaded into the Spreadsheet. 

Now, you have the option to selectively ignore some features during the opening of the JSON object by configuring deserialization options and passing them as arguments to the `openFromJson` method. This argument is optional, and if not configured, the entire workbook JSON object will be loaded without ignoring any features.

```ts
spreadsheet.openFromJson({ file: file }, { ignoreStyle: true });
```

| Options | Description |
| ----- | ----- |
| onlyValues |  If **true**, only the cell values will be loaded. |
| ignoreStyle | If **true**, styles will be excluded when loading the JSON data. |
| ignoreFormula | If **true**, formulas will be excluded when loading the JSON data. |
| ignoreFormat | If **true**, number formats will be excluded when loading the JSON data. |
| ignoreConditionalFormat | If **true**, conditional formatting will be excluded when loading the JSON data. |
| ignoreValidation | If **true**, data validation rules will be excluded when loading the JSON data. |
| ignoreFreezePane | If **true**, freeze panes will be excluded when loading the JSON data. |
| ignoreWrap | If **true**, text wrapping settings will be excluded when loading the JSON data. |
| ignoreChart | If **true**, charts will be excluded when loading the JSON data. |
| ignoreImage | If **true**, images will be excluded when loading the JSON data. |
| ignoreNote | If **true**, notes will be excluded when loading the JSON data. |

The following code snippet demonstrates how to configure the deserialization options and pass them as arguments to the openFromJson method:

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
@using Syncfusion.EJ2
@{
var asyncSettings = new Syncfusion.EJ2.Inputs.UploaderAsyncSettings { SaveUrl =
"https://services.syncfusion.com/aspnet/production/api/FileUploader/Save", RemoveUrl =
"https://services.syncfusion.com/aspnet/production/api/FileUploader/Remove" };
}
<div id="Openfromjson">
    <label id="Heading">Open From Json Options:</label> <br>
    <input type="checkbox" id="valueOnly" onchange="toggleCheckboxes()"><label for="valueOnly">Only Values</label>
    <input type="checkbox" id="style"><label for="style">Ignore Style</label>
    <input type="checkbox" id="formula"><label for="formula">Ignore Formula</label>
    <input type="checkbox" id="format"><label for="format">Ignore Format</label>
    <input type="checkbox" id="cf"><label for="cf">Ignore CF</label>
    <input type="checkbox" id="dv"><label for="dv">Ignore Validation</label>
    <input type="checkbox" id="freeze"><label for="freeze">Ignore Freezepane</label>
    <input type="checkbox" id="wrap"><label for="wrap">Ignore Wrap</label>
    <input type="checkbox" id="chart"><label for="chart">Ignore Chart</label>
    <input type="checkbox" id="image"><label for="image">Ignore Image</label>
    <input type="checkbox" id="note"><label for="note">Ignore Note</label>
</div>
<ejs-uploader id="UploadFiles" success="onSuccess" asyncSettings="@asyncSettings" allowedExtensions=".xls, .xlsx, .csv"
    showFileList="false"> </ejs-uploader>
<ejs-spreadsheet id="spreadsheet" saveUrl="Home/Save" allowSave="true" beforeOpen="beforeOpen"> </ejs-spreadsheet>

<style>
    #Openfromjson {
        margin-top: 10px;
        margin-bottom: 20px;
    }

    #Openfromjson input[type="checkbox"] {
        margin: 7px;
    }

    #Openfromjson label {
        font-size: 14px;
    }

    #Heading {
        font-weight: bold;
    }
</style>

<script>

    window.onload = function (args) {
        var uploaderObj = document.getElementById("UploadFiles").ej2_instances[0];
        uploaderObj.setProperties({
            buttons: {
                browse: 'Choose file'
            }
        });
    }

    function beforeOpen(args) {
        args.cancel = true;
        var valueOnlyCheckbox = document.getElementById("valueOnly").checked;
        var options = valueOnlyCheckbox ? { onlyValues: true } : createOptions();
        fetch(
            'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/open',
            args.requestData
        ).then((response) => {
            response.json().then((data) => {
                var ssObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
                ssObj.openFromJson({ file: data }, options)
            });
        });
    }

    function onSuccess(args) {
        var ssObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
        if (args.operation === 'upload')
            ssObj.open({ file: args.file.rawFile });
    }

    function toggleCheckboxes() {
        var valueOnlyCheckbox = document.getElementById('valueOnly');
        var checkboxes = document.querySelectorAll('#Openfromjson input[type="checkbox"]:not(#valueOnly)');
        checkboxes.forEach(checkbox => {
            (checkbox).disabled = valueOnlyCheckbox.checked;
            if (valueOnlyCheckbox.checked) {
                (checkbox).checked = false;
            }
        });
    }

    function createOptions() {
        const options = {};
        options.ignoreStyle = document.getElementById('style').checked;
        options.ignoreFormula = document.getElementById('formula').checked;
        options.ignoreFormat = document.getElementById('format').checked;
        options.ignoreConditionalFormat = document.getElementById('cf').checked;
        options.ignoreValidation = document.getElementById('dv').checked;
        options.ignoreFreezePane = document.getElementById('freeze').checked;
        options.ignoreWrap = document.getElementById('wrap').checked;
        options.ignoreChart = document.getElementById('chart').checked;
        options.ignoreImage = document.getElementById('image').checked;
        options.ignoreNote = document.getElementById('note').checked;
        return options;
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="OpenController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

{% endhighlight %}
{% endtabs %}

### Improving Excel file open performance with parsing options

Opening large Excel files into the EJ2 Spreadsheet control can sometimes lead to slower performance and increased memory usage. This is often caused by the processing of additional elements such as styles and number formatsâeven when the actual data content is minimal. For example, an Excel file with only a small amount of data but a large number of styled or formatted empty cells can significantly impact load time and memory consumption.

To address this, we've introduced parsing options that allow users to selectively skip non-essential features during the open process. By enabling options like `IgnoreStyle` and `IgnoreFormat`, you can reduce the amount of data processed, resulting in:
* Faster load times
* Lower memory usage
* Smaller JSON responses

These enhancements are especially beneficial for users working with large or complex Excel files, offering a more efficient and responsive experience.

> **Note:** These options are ideal when styles and number formats are not critical to your use case and the focus is on loading the actual data efficiently. 

The code example below demonstrates how to configure the `IgnoreStyle` and `IgnoreFormat` parsing options on the `server-side`.

**Code Snippet:**

**Server-Side Configuration:**
```csharp
public IActionResult Open(IFormCollection openRequest) 
{ 
    OpenRequest open = new OpenRequest(); 
    ...
    open.ParseOptions = new WorkbookParseOptions() { 
        IgnoreStyle = true, 
        IgnoreFormat = true
    }; 
    ...
    return Content(Workbook.Open(open)); 
} 
```

### Chunk response processing

When opening large Excel files with many features and data, the server response can become very large. This might cause memory issues or connection problems during data transmission. The `Chunk Response Processing` feature solves this by dividing the server response into smaller parts, called chunks, and sending them to the client in parallel. The client receives these chunks and combines them to load the Excel data smoothly into the spreadsheet.

You can enable this feature by setting the `chunkSize` property in the [`openSettings`](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_OpenSettings) object. Set the `chunkSize` to a value greater than 0 (in bytes). The `chunkSize` defines how large each chunk will be. Make sure your server supports chunked responses to use this feature effectively.

> This feature reduces memory usage on both the server and client, ensuring that resources are managed efficiently during data transmission. By sending smaller parts of data, it prevents connection issues that could occur with large payloads, making the transmission process more reliable. Additionally, it allows large Excel files to be loaded smoothly into the spreadsheet, providing a seamless user experience even with extensive data.

The following code example demonstrates the client-side and server-side configuration required for handling chunk-based responses when opening an Excel file.

**Client Side**:

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" created="created">
</ejs-spreadsheet>

<script>
    function created() {
        this.openSettings = { chunkSize: 1000000, retryCount: 3, retryAfterDelay: 500 }
    }
</script>

{% endhighlight %}
{% endtabs %}

**Server Endpoint**:

```csharp
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    if (openRequest.Files.Count > 0)
    {
        open.File = openRequest.Files[0];
    }
    Microsoft.Extensions.Primitives.StringValues chunkPayload;
    if (openRequest.TryGetValue("chunkPayload", out chunkPayload))
    {
        // The chunk payload JSON data includes information essential for processing chunked responses.
        open.ChunkPayload = chunkPayload;
    }
    var result = Workbook.Open(open, 150);
    return Content(result);
}
```

The [attachment](https://www.syncfusion.com/downloads/support/directtrac/general/ze/WebApplication1_7-101537213) includes the server endpoint code for handling chunk-based open processing. After launching the server endpoint, update the `openUrl` property of the spreadsheet in the client-side sample with the server URL, as shown below.

```js
    // Specifies the service URL for processing the Excel file, converting it into a format suitable for loading in the spreadsheet.
    <ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" created="created">
    </ejs-spreadsheet>
```

### Add custom header during open

You can add your own custom header to the open action in the Spreadsheet. For processing the data, it has to be sent from server to client side and adding customer header can provide privacy to the data with the help of Authorization Token. Through the [`beforeOpen`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeOpen) event, the custom header can be added to the request during open action.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" beforeOpen="beforeOpen" openUrl="Home/Open">
  
</ejs-spreadsheet>

<script>
  function beforeOpen(args) {
    args.requestData["headers"] = { Authorization: "YOUR TEXT" };
  }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Opencontroller.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}

### External workbook confirmation dialog

When you open an excel file that contains external workbook references, you will see a confirmation dialog. This dialog allows you to either continue with the file opening or cancel the operation. This confirmation dialog will appear only if you set the `AllowExternalWorkbook` property value to **false** during the open request, as shown below. This prevents the spreadsheet from displaying inconsistent data.

```csharp
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.AllowExternalWorkbook = false;
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
```

> This feature is only applicable when importing an Excel file and not when loading JSON data or binding cell data.

![External workbook confirmation dialog](./images/external-reference-dialog-alert.png)

## Supported file formats

The following list of Excel file formats are supported in Spreadsheet:

* Microsoft Excel (.xlsx)
* Microsoft Excel 97-2003 (.xls)
* Comma Separated Values (.csv)
* Excel Macro-Enabled Workbook (.xlsm)
* Excel Binary Workbook(.xlsb)

## Save

The Spreadsheet component saves its data, style, format, and more as Excel file document. To enable this feature, set [`allowSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowSave) as `true` and assign service url to the [`saveUrl`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_SaveUrl) property.

**User Interface**:

In user interface, you can save Spreadsheet data as Excel document by clicking `File > Save As` menu item in ribbon.

The following sample shows the `Save` option by using the [`saveUrl`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_SaveUrl) property in the Spreadsheet control. You can also use the [`beforeSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeSave) event to trigger before saving the Spreadsheet as an Excel file.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" saveUrl="Home/Save" allowSave = "true">

</ejs-spreadsheet>
{% endhighlight %}
{% highlight c# tabtitle="Savecontroller.cs" %}
public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}
{% endhighlight %}
{% endtabs %}



Find the below table for the beforeSave event arguments.

| **Parameter** | **Type** | **Description** |
| ----- | ----- | ----- |
| url | string |  Specifies the save url.  |
| fileName | string | Specifies the file name. |
| saveType | SaveType | Specifies the saveType like `Xlsx`, `Xls`, `Csv` and `Pdf`. |
| customParams | object | Passing the custom parameters from client to server while performing save operation. |
| isFullPost | boolean | It sends the form data from client to server, when set to true. It fetches the data from client to server and returns the data from server to client, when set to false. |
| needBlobData | boolean | You can get the blob data if set to true. |
| cancel | boolean | To prevent the save operations. |

N> * Use `Ctrl + S` keyboard shortcut to save the Spreadsheet data as Excel file.
<br/> * The default value of [allowSave](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowSave) property is `true`. For demonstration purpose, we have showcased the [allowSave](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_AllowSave) property in previous code snippet.
<br/> * Demo purpose only, we have used the online web service url link.

### Save an excel file as blob data

By default, the Spreadsheet control saves the Excel file and downloads it to the local file system. If you want to save an Excel file as blob data, you need to set `needBlobData` property to **true** and `isFullPost` property to **false** in the `beforeSave` event of the spreadsheet. Subsequently, you will receive the spreadsheet data as a blob in the `saveComplete` event. You can then post the blob data to the server endpoint for saving.

Please find below the code to retrieve blob data from the Spreadsheet control below.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" beforeSave="beforeSave" saveComplete="saveComplete" openUrl="Home/Open" saveUrl="https://localhost:{{port number}}/Home/Save">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
					<e-spreadsheet-columns>
						<e-spreadsheet-column width="130"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
					</e-spreadsheet-columns>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    function beforeSave(args) {
        args.needBlobData = true; // To trigger the saveComplete event.
        args.isFullPost = false; // Get the spreadsheet data as blob data in the saveComplete event.
    }

    function saveComplete(args) {
        // To obtain the blob data
        console.log('Spreadsheet BlobData : ', args.blobData);
    }

</script>

{% endhighlight %}
{% highlight c# tabtitle="SaveController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}

public IActionResult Index()
{
    List<object> defaultData = new List<object>()
    {
        new { ItemName= "Casual Shoes", Date= "02/14/2014", Time= "11:34:32 AM", Quantity= "10", Price= "20", Amount= "200", Discount= "1", Profit= "10" },
        new { ItemName= "Sports Shoes", Date= "06/11/2014", Time= "05:56:32 AM", Quantity= "20", Price= "30", Amount= "600", Discount= "5", Profit= "50" },
        new { ItemName= "Formal Shoes", Date= "07/27/2014", Time= "03:32:44 AM", Quantity= "20", Price= "15", Amount= "300", Discount= "7", Profit= "27" },
        new { ItemName= "Sandals & Floaters", Date= "11/21/2014", Time= "06:23:54 AM", Quantity= "15", Price= "20", Amount= "300", Discount= "11", Profit= "67" },
        new { ItemName= "Flip- Flops & Slippers", Date= "06/23/2014", Time= "12:43:59 AM", Quantity= "30", Price= "10", Amount= "300", Discount= "10", Profit= "70" },
        new { ItemName= "Sneakers", Date= "07/22/2014", Time= "10:55:53 AM", Quantity= "40", Price= "20", Amount= "800", Discount= "13", Profit= "66" },
        new { ItemName= "Running Shoes", Date= "02/04/2014", Time= "03:44:34 AM", Quantity= "20", Price= "10", Amount= "200", Discount= "3", Profit= "14" },
        new { ItemName= "Loafers", Date= "11/30/2014", Time= "03:12:52 AM", Quantity= "31", Price= "10", Amount= "310", Discount= "6", Profit= "29" },
        new { ItemName= "Cricket Shoes", Date= "07/09/2014", Time= "11:32:14 AM", Quantity= "41", Price= "30", Amount= "1210", Discount= "12", Profit= "166" },
        new { ItemName= "T-Shirts", Date= "10/31/2014", Time= "12:01:44 AM", Quantity= "50", Price= "10", Amount= "500", Discount= "9", Profit= "55" }
    };
    ViewBag.DefaultData = defaultData;
    return View();

}
{% endhighlight %}
{% endtabs %}

### Save an Excel file to a server

By default, the Spreadsheet control saves the Excel file and downloads it to the local file system. If you want to save an Excel file to a server location, you need to configure the server endpoint to convert the spreadsheet data into a file stream and save it to the server location. To do this, first, on the client side, you must convert the spreadsheet data into `JSON` format using the `saveAsJson` method and send it to the server endpoint. On the server endpoint, you should convert the received spreadsheet `JSON` data into a file stream using `Syncfusion.EJ2.Spreadsheet.AspNet.Core`, then convert the stream into an Excel file, and finally save it to the server location.

```js

    // Convert the spreadsheet workbook to JSON data.
    spreadsheet.saveAsJson().then((json) => {
        const formData = new FormData();
        formData.append('FileName', "Sample");
        formData.append('saveType', 'Xlsx');
        // Passing the JSON data to perform the save operation.
        formData.append('JSONData', JSON.stringify(json.jsonObject.Workbook));
        formData.append('PdfLayoutSettings', JSON.stringify({ FitSheetOnOnePage: false }));
        // Using fetch to invoke the save process.
        fetch('Home/Save', {
            method: 'POST',
            body: formData
        }).then((response) => {
            console.log(response);
        });
    });

```

```csharp

    public string Save(SaveSettings saveSettings)
    {
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;
        try
        {
            
            // Save the workbook as stream.
            Stream fileStream = Workbook.Save<Stream>(saveSettings);
            // Using XLSIO, we are opening the file stream and saving the file in the server under "Files" folder.
            // You can also save the stream file in your server location.
            IWorkbook workbook = application.Workbooks.Open(fileStream);
            string basePath = _env.ContentRootPath + "\\Files\\" + saveSettings.FileName + ".xlsx";
            var file = System.IO.File.Create(basePath);
            fileStream.Seek(0, SeekOrigin.Begin);
            // To convert the stream to file options.
            fileStream.CopyTo(file);
            file.Dispose();
            fileStream.Dispose();
            return string.Empty;
        }
        catch (Exception ex)
        {
            return ex.Message;
        }
    }

```

You can find the server endpoint code to save the spreadsheet data as an Excel file in this [attachment](https://www.syncfusion.com/downloads/support/directtrac/general/ze/WebApplication1_(1)-880363187).

### Save an excel file using a hosted web service in AWS Lambda

Before proceeding with the save process, you should deploy the spreadsheet open/save web API service in AWS Lambda. To host the open/save web service in the AWS Lambda environment, please refer to the following KB documentation.

After deployment, you will get the AWS service URL for the open and save actions. Before saving the Excel file with this hosted save URL, you need to prevent the default save action to avoid getting a corrupted excel file on the client end. The save service returns the file stream as a result to the client, which can cause the file to become corrupted. To prevent this, set the `args.cancel` value to `true` in the [`beforeSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeSave) event. After that, convert the spreadsheet data into JSON format using the `saveAsJson` method in the `beforeSave` event and send it to the save service endpoint URL using a fetch request.

On the server side, the save service will take the received JSON data, pass it to the workbook `Save` method, and return the result as a base64 string. The fetch success callback will receive the Excel file in base64 string format on the client side. Finally, you can then convert the base64 string back to a file on the client end to obtain a non-corrupted Excel file.

The following code example shows how to save an Excel file using a hosted web service in AWS Lambda, as mentioned above.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-spreadsheet id="spreadsheet" saveUrl="https://xxxxxxxxxxxxxxxxxxxxxxxxx.amazonaws.com/Prod/api/spreadsheet/save" allowSave="true" beforeSave="beforeSave">

</ejs-spreadsheet>

<script>
    var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
    var saveInitiated;
    function beforeSave(eventArgs) {
        if (!saveInitiated) {
            eventArgs.cancel = true; // Preventing default save action.
            saveInitiated = true; // The "beforeSave" event will trigger for "saveAsJson" action also, so we are preventing for the "saveAsJson".
            saveAsExcel(eventArgs);
        }
    };
    function saveAsExcel(eventArgs) {
        // Convert the spreadsheet workbook to JSON data.
        spreadsheet.saveAsJson().then(Json => {
            saveInitiated = false;
            const formData = new FormData();
            // Passing the JSON data to server to perform save operation.
            formData.append('JSONData', JSON.stringify(Json.jsonObject.Workbook));
            formData.append('saveType', 'Xlsx');
            formData.append('fileName', 'Worksheet');
            formData.append('pdfLayoutSettings', '{"fitSheetOnOnePage":false,"orientation":"Portrait"}');
            // Using fetch API to invoke the server for save processing.
            fetch('https://xxxxxxxxxxxxxxxxxxxxxxxxx.amazonaws.com/Prod/api/spreadsheet/save', {
                method: 'POST', body: formData
            }).then(response => {
                if (response.ok) {
                    return response.blob();
                }
            }).then(data => {
                const reader = new FileReader();
                reader.onload = function () {
                    //Converts the result of the file reading operation into a base64 string.
                    const textBase64Str = reader.result.toString();
                    //Converts the base64 string into a Excel base64 string.
                    const excelBase64Str = atob(textBase64Str.replace('data:text/plain;base64,', ''));
                    //Converts the Excel base64 string into byte characters.
                    const byteCharacters = atob(excelBase64Str.replace('data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,', ''));
                    const byteArrays = [];
                    for (let i = 0; i < byteCharacters.length; i++) {
                        byteArrays.push(byteCharacters.charCodeAt(i));
                    }
                    const byteArray = new Uint8Array(byteArrays);
                    //creates a blob data from the byte array with xlsx content type.
                    const blobData = new Blob([byteArray], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                    const blobUrl = URL.createObjectURL(blobData);
                    const anchor = document.createElement('a');
                    anchor.download = 'Sample.xlsx';
                    anchor.href = blobUrl;
                    document.body.appendChild(anchor);
                    anchor.click();
                    URL.revokeObjectURL(blobUrl);
                    document.body.removeChild(anchor);
                }
                reader.readAsDataURL(data);
            });
        });        
    };
</script>

{% endhighlight %}
{% endtabs %}

### Save data as a Base64 string

In the Spreadsheet control, there is currently no direct option to save data as a `Base64` string. You can achieve this by saving the Spreadsheet data as blob data and then converting that saved blob data to a `Base64` string using `FileReader`. 

> You can get the Spreadsheet data as blob in the [saveComplete](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_SaveComplete) event when you set the  `needBlobData` as **true** and `isFullPost` as **false** in the [beforeSave](https://help.syncfusion.com/cr/aspnetcore-js2/syncfusion.ej2.spreadsheet.spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeSave) event.

The following code example shows how to save the spreadsheet data as base64 string.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="importBtn" content="Import Base64"></ejs-button>
<ejs-button id="exportBtn" content="Export as Base64"></ejs-button>
<ejs-spreadsheet id="spreadsheet" beforeSave="beforeSave" saveComplete="saveComplete" openUrl="Home/Open">
            <e-spreadsheet-sheets>
                <e-spreadsheet-sheet name="Price Details">
                    <e-spreadsheet-ranges>
                        <e-spreadsheet-range dataSource="ViewBag.DefaultData" startCell="A1"></e-spreadsheet-range>
                    </e-spreadsheet-ranges>
					<e-spreadsheet-columns>
						<e-spreadsheet-column width="130"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
						<e-spreadsheet-column width="100"></e-spreadsheet-column>
					</e-spreadsheet-columns>
                </e-spreadsheet-sheet>
            </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    var base64String;
    function beforeSave(args) {
        args.needBlobData = true; // To trigger the saveComplete event.
        args.isFullPost = false; // Get the spreadsheet data as blob data in the saveComplete event.
    }

    function saveComplete(args) {
        // Convert blob data to base64 string.
        var reader = new FileReader();
        reader.readAsDataURL(args.blobData);
        reader.onloadend = function () {
            base64String = reader.result;
        };
    }

    document.getElementById("importBtn").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        // Open the file based on saved base64 string.
        fetch(base64String)
            .then((response) => response.blob())
            .then((fileBlob) => {
                var file = new File([fileBlob], 'Sample.xlsx');
                spreadsheetObj.open({ file: file });
            });
    });
    document.getElementById("exportBtn").addEventListener('click', function () {
        var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
        spreadsheetObj.save({
            url: 'https://localhost:{{port number}}/Home/Save',
            fileName: 'Worksheet',
            saveType: 'Xlsx',
        }); // Specifies the save URL, file name, file type need to be saved.
        // Logs base64 string into the console.
        console.log('Base64 String - ', base64String);
    });
</script>

{% endhighlight %}
{% highlight c# tabtitle="OpenController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}

public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}

public IActionResult Index()
{
    List<object> defaultData = new List<object>()
    {
        new { ItemName= "Casual Shoes", Date= "02/14/2014", Time= "11:34:32 AM", Quantity= "10", Price= "20", Amount= "200", Discount= "1", Profit= "10" },
        new { ItemName= "Sports Shoes", Date= "06/11/2014", Time= "05:56:32 AM", Quantity= "20", Price= "30", Amount= "600", Discount= "5", Profit= "50" },
        new { ItemName= "Formal Shoes", Date= "07/27/2014", Time= "03:32:44 AM", Quantity= "20", Price= "15", Amount= "300", Discount= "7", Profit= "27" },
        new { ItemName= "Sandals & Floaters", Date= "11/21/2014", Time= "06:23:54 AM", Quantity= "15", Price= "20", Amount= "300", Discount= "11", Profit= "67" },
        new { ItemName= "Flip- Flops & Slippers", Date= "06/23/2014", Time= "12:43:59 AM", Quantity= "30", Price= "10", Amount= "300", Discount= "10", Profit= "70" },
        new { ItemName= "Sneakers", Date= "07/22/2014", Time= "10:55:53 AM", Quantity= "40", Price= "20", Amount= "800", Discount= "13", Profit= "66" },
        new { ItemName= "Running Shoes", Date= "02/04/2014", Time= "03:44:34 AM", Quantity= "20", Price= "10", Amount= "200", Discount= "3", Profit= "14" },
        new { ItemName= "Loafers", Date= "11/30/2014", Time= "03:12:52 AM", Quantity= "31", Price= "10", Amount= "310", Discount= "6", Profit= "29" },
        new { ItemName= "Cricket Shoes", Date= "07/09/2014", Time= "11:32:14 AM", Quantity= "41", Price= "30", Amount= "1210", Discount= "12", Profit= "166" },
        new { ItemName= "T-Shirts", Date= "10/31/2014", Time= "12:01:44 AM", Quantity= "50", Price= "10", Amount= "500", Discount= "9", Profit= "55" }
    };
    ViewBag.DefaultData = defaultData;
    return View();

}
{% endhighlight %}
{% endtabs %}

### Configure JSON serialization options

Previously, when saving the Spreadsheet as a workbook JSON object using the `saveAsJson` method, the entire workbook with all loaded features were processed and saved as a JSON object. 

Now, you have the option to selectively ignore some features while saving the Spreadsheet as a JSON object by configuring serialization options and passing them as arguments to the `saveAsJson` method. This argument is optional, and if not configured, the entire workbook JSON object will be saved without ignoring any features.

```ts
spreadsheet.saveAsJson({ onlyValues: true });
```

| Options | Description |
| ----- | ----- |
| onlyValues |  If **true**, includes only the cell values in the JSON output. |
| ignoreStyle | If **true**, excludes styles from the JSON output. |
| ignoreFormula | If **true**, excludes formulas from the JSON output. |
| ignoreFormat | If **true**, excludes number formats from the JSON output. |
| ignoreConditionalFormat | If **true**, excludes conditional formatting from the JSON output. |
| ignoreValidation | If **true**, excludes data validation rules from the JSON output. |
| ignoreFreezePane | If **true**, excludes freeze panes from the JSON output. |
| ignoreWrap | If **true**, excludes text wrapping settings from the JSON output. |
| ignoreChart | If **true**, excludes charts from the JSON output. |
| ignoreImage | If **true**, excludes images from the JSON output. |
| ignoreNote | If **true**, excludes notes from the JSON output. |

The following code snippet demonstrates how to configure the serialization options and pass them as arguments to the saveAsJson method:

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="Saveasjson">
    <label id="Heading">Save As Json Options:</label> <br>
    <input type="checkbox" id="valueOnly" onchange="toggleCheckboxes()"><label for="valueOnly">Only Values</label>
    <input type="checkbox" id="style"><label for="style">Ignore Style</label>
    <input type="checkbox" id="formula"><label for="formula">Ignore Formula</label>
    <input type="checkbox" id="format"><label for="format">Ignore Format</label>
    <input type="checkbox" id="cf"><label for="cf">Ignore CF</label>
    <input type="checkbox" id="dv"><label for="dv">Ignore Validation</label>
    <input type="checkbox" id="freeze"><label for="freeze">Ignore Freezepane</label>
    <input type="checkbox" id="wrap"><label for="wrap">Ignore Wrap</label>
    <input type="checkbox" id="chart"><label for="chart">Ignore Chart</label>
    <input type="checkbox" id="image"><label for="image">Ignore Image</label>
    <input type="checkbox" id="note"><label for="note">Ignore Note</label>
    <button id="save">Save with JSON Serialization</button>
</div>
<ejs-spreadsheet id="spreadsheet" openUrl="Home/Open" allowOpen="true"> </ejs-spreadsheet>

<style>
    #Saveasjson {
        margin-top: 10px;
        margin-bottom: 20px;
    }

    #Saveasjson input[type="checkbox"] {
        margin: 7px;
    }

    #Saveasjson label {
        font-size: 14px;
    }

    #Heading {
        font-weight: bold;
    }
</style>

<script>

    function toggleCheckboxes() {
        let valueOnlyCheckbox = document.getElementById('valueOnly');
        let checkboxes = document.querySelectorAll('#Saveasjson input[type="checkbox"]:not(#valueOnly)');
        checkboxes.forEach(checkbox => {
            checkbox.disabled = valueOnlyCheckbox.checked;
            if (valueOnlyCheckbox.checked) {
                checkbox.checked = false;
            }
        });
    }

    function createOptions() {
        const options = {};
        options.ignoreStyle = document.getElementById('style').checked;
        options.ignoreFormula = document.getElementById('formula').checked;
        options.ignoreFormat = document.getElementById('format').checked;
        options.ignoreConditionalFormat = document.getElementById('cf').checked;
        options.ignoreValidation = document.getElementById('dv').checked;
        options.ignoreFreezePane = document.getElementById('freeze').checked;
        options.ignoreWrap = document.getElementById('wrap').checked;
        options.ignoreChart = document.getElementById('chart').checked;
        options.ignoreImage = document.getElementById('image').checked;
        options.ignoreNote = document.getElementById('note').checked;
        return options;
    }

    var saveElement = document.getElementById("save");
    if (saveElement) {
        // Save button click event listener
        saveElement.onclick = () => {
            var valueOnlyCheckbox = document.getElementById("valueOnly").checked;
            var options = valueOnlyCheckbox ? { onlyValues: true } : createOptions();
            var spreadsheetObj = document.getElementById("spreadsheet").ej2_instances[0];
            spreadsheetObj.saveAsJson(options).then((response) => {
                var formData = new FormData();
                formData.append(
                    'JSONData',
                    JSON.stringify(response.jsonObject.Workbook)
                );
                formData.append('fileName', 'Sample');
                formData.append('saveType', 'Xlsx');
                formData.append('pdfLayoutSettings', JSON.stringify({ fitSheetOnOnePage: false, orientation: 'Portrait' })),
                    fetch(
                        'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save',
                        {
                            method: 'POST',
                            body: formData,
                        }
                    ).then((response) => {
                        response.blob().then((data) => {
                            var anchor = ej.base.createElement('a', {
                                attrs: { download: 'Sample.xlsx' },
                            });
                            var url = URL.createObjectURL(data);
                            anchor.href = url;
                            document.body.appendChild(anchor);
                            anchor.click();
                            URL.revokeObjectURL(url);
                            document.body.removeChild(anchor);
                        });
                    });
            });
        };
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="SaveController.cs" %}
public IActionResult Open(IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
{% endhighlight %}
{% endtabs %}

### Send and receive custom params from client to server

Passing the custom parameters from client to server by using [`beforeSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeSave) event.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowSave="true" saveUrl="Save" beforeSave="beforeSave">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-columns>
                <e-spreadsheet-column width="180"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="180"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="120"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

    function beforeSave(args) {
        args.customParams = { customParams: 'you can pass custom params in server side' }; // you can pass the custom params
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="CustomParamsController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Green",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Indigo",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    ViewBag.DefaultData = data;
    return View();
}

public IActionResult Save(SaveSettings saveSettings, string customParams)
{
    return Workbook.Save(saveSettings);
}
{% endhighlight %}
{% endtabs %}

### Add custom header during save

You can add your own custom header to the save action in the Spreadsheet. For processing the data, it has to be sent from client to server side and adding customer header can provide privacy to the data with the help of Authorization Token. Through the [`fileMenuItemSelect`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_FileMenuItemSelect) event, the custom header can be added to the request during save action.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" fileMenuItemSelect="onFileMeuItemSelect" saveUrl="Home/Save">
    <e-spreadsheet-sheets>
      <e-spreadsheet-sheet>
        <e-spreadsheet-ranges>
          <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
        </e-spreadsheet-ranges>
      </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
  </ejs-spreadsheet>

<script>

  function onFileMeuItemSelect(args) {
    var spreadsheet = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
    if (args.item.text === "Microsoft Excel") {
      args.cancel = true;
      spreadsheet.saveAsJson().then(response => {
        var formData = new FormData();
        formData.append(
          "JSONData",
          JSON.stringify(response.jsonObject.Workbook)
        );
        formData.append("fileName", "Sample");
        formData.append("saveType", "Xlsx");
        formData.append("pdfLayoutSettings", JSON.stringify({ fitSheetOnOnePage: false, orientation: "Portrait" }));
        fetch(
          "https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save",
          {
            method: "POST",
            headers: { Authorization: "YOUR TEXT" },
            body: formData
          }
        ).then(response => {
          response.blob().then(data => {
            var anchor = createElement("a", {
              attrs: { download: "Sample.xlsx" }
            });
            var url = URL.createObjectURL(data);
            anchor.href = url;
            document.body.appendChild(anchor);
            anchor.click();
            URL.revokeObjectURL(url);
            document.body.removeChild(anchor);
          });
        });
      });
    }


    } 
</script>
{% endhighlight %}
{% highlight c# tabtitle="CustomHeaderController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Green",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Indigo",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    ViewBag.DefaultData = data;
    return View();
}
        
public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}
{% endhighlight %}
{% endtabs %}

### Change the PDF orientation

By default, the PDF document is created in **Portrait** orientation. You can change the orientation of the PDF document by using the `args.pdfLayoutSettings.orientation` argument settings in the [`beforeSave`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_BeforeSave) event.

The possible values are:

* **Portrait** - Used to display content in a vertical layout.
* **Landscape** - Used to display content in a horizontal layout.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" allowSave="true" saveUrl="Home/Save" beforeSave="beforeSave">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
            <e-spreadsheet-columns>
                <e-spreadsheet-column width="180"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="180"></e-spreadsheet-column>
                <e-spreadsheet-column width="130"></e-spreadsheet-column>
                <e-spreadsheet-column width="120"></e-spreadsheet-column>
            </e-spreadsheet-columns>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>

    function beforeSave(args) {
        args.pdfLayoutSettings.orientation = 'Landscape'; // You can change the orientation of the PDF document
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="pdfOrientationController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Green",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Indigo",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    ViewBag.DefaultData = data;
    return View();
}
        
public IActionResult Save(SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}
{% endhighlight %}
{% endtabs %}

### Supported file formats

The following list of Excel file formats are supported in Spreadsheet:

* Microsoft Excel (.xlsx)
* Microsoft Excel 97-2003 (.xls)
* Comma Separated Values (.csv)
* Portable Document Format (.pdf)

### Methods

To save the Spreadsheet document as an `xlsx, xls, csv, or pdf` file, by using `save` method should be called with the `url`, `fileName` and `saveType` as parameters. The following code example shows to save the spreadsheet file as an `xlsx, xls, csv, or pdf` in the button click event.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-dropdownbutton id="element" content="Save" items="ViewBag.items" select="itemSelect"></ejs-dropdownbutton>

<ejs-spreadsheet id="spreadsheet">
    <e-spreadsheet-sheets>
        <e-spreadsheet-sheet>
            <e-spreadsheet-ranges>
                <e-spreadsheet-range dataSource="ViewBag.DefaultData"></e-spreadsheet-range>
            </e-spreadsheet-ranges>
        </e-spreadsheet-sheet>
    </e-spreadsheet-sheets>
</ejs-spreadsheet>

<script>
    function itemSelect(args) {
    var spreadsheetObj = ej.base.getComponent(document.getElementById('spreadsheet'), 'spreadsheet');
    if (args.item.text === 'Save As xlsx')
      spreadsheetObj.save({url: 'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save', fileName: "Sample", saveType: "Xlsx"});
    if (args.item.text === 'Save As xls')
      spreadsheetObj.save({url: 'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save', fileName: "Sample", saveType: "Xls"});
    if (args.item.text === 'Save As csv')
      spreadsheetObj.save({url: 'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save',fileName: "Sample", saveType: "Csv"});
    if (args.item.text === 'Save As pdf')
      spreadsheetObj.save({url: 'https://document.syncfusion.com/web-services/spreadsheet-editor/api/spreadsheet/save',fileName: "Sample", saveType: "Pdf"});
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="OpenSaveController.cs" %}
public IActionResult Index()
{
    List<object> data = new List<object>()
    {
        new { CustomerName= "Romona Heaslip",  Model= "Taurus",  Color= "Aquamarine",  PaymentMode= "Debit Card",  DeliveryDate= "07/11/2015",  Amount= "8529.22" },
        new { CustomerName= "Clare Batterton",  Model= "Sparrow",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/13/2016",  Amount= "17866.19" },
        new { CustomerName= "Eamon Traise",  Model= "Grand Cherokee",  Color= "Blue",  PaymentMode= "Net Banking",  DeliveryDate= "09/04/2015",  Amount= "13853.09" },
        new { CustomerName= "Julius Gorner",  Model= "GTO",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/15/2017",  Amount= "2338.74" },
        new { CustomerName= "Jenna Schoolfield",  Model= "LX",  Color= "Yellow",  PaymentMode= "Credit Card",  DeliveryDate= "10/08/2014",  Amount= "9578.45" },
        new { CustomerName= "Marylynne Harring",  Model= "Catera",  Color= "Green",  PaymentMode= "Cash On Delivery",  DeliveryDate= "7/01/2017",  Amount= "19141.62" },
        new { CustomerName= "Vilhelmina Leipelt",  Model= "7 Series",  Color= "Goldenrod",  PaymentMode= "Credit Card",  DeliveryDate= "12/20/2015",  Amount= "6543.30" },
        new { CustomerName= "Barby Heisler",  Model= "Corvette",  Color= "Red",  PaymentMode= "Credit Card",  DeliveryDate= "11/24/2014",  Amount= "13035.06" },
        new { CustomerName= "Karyn Boik",  Model= "Regal",  Color= "Indigo",  PaymentMode= "Debit Card",  DeliveryDate= "05/12/2014",  Amount= "18488.80" },
        new { CustomerName= "Jeanette Pamplin",  Model= "S4",  Color= "Fuscia",  PaymentMode= "Net Banking",  DeliveryDate= "12/30/2014",  Amount= "12317.04" },
        new { CustomerName= "Cristi Espinos",  Model= "TL",  Color= "Aquamarine",  PaymentMode= "Credit Card",  DeliveryDate= "12/18/2013",  Amount= "6230.13" },
        new { CustomerName= "Issy Humm",  Model= "Club Wagon",  Color= "Pink",  PaymentMode= "Cash On Delivery",  DeliveryDate= "02/02/2015",  Amount= "9709.49" },
        new { CustomerName= "Tuesday Fautly",  Model= "V8 Vantage",  Color= "Crimson",  PaymentMode= "Debit Card",  DeliveryDate= "11/19/2014",  Amount= "9766.10" },
        new { CustomerName= "Rosemaria Thomann",  Model= "Caravan",  Color= "Violet",  PaymentMode= "Net Banking",  DeliveryDate= "02/08/2014",  Amount= "7685.49" },
    };
    List<object> items = new List<object>();
    items.Add(new
    {
        text = "Save As xlsx"
    });
    items.Add(new
    {
        text = "Save As xls"
    });
    items.Add(new
    {
        text = "Save As csv"
    });
    items.Add(new
    {
        text = "Save As pdf"
    });
    ViewBag.items = items;
    ViewBag.DefaultData = data;
    return View();
}
{% endhighlight %}
{% endtabs %}



## Server Configuration

In Spreadsheet component, import and export operation processed in `server-side`, to use importing and exporting in your projects, it is required to create a server with any of the following web services.

* WebAPI
* WCF Service
* ASP.NET MVC Controller Action

N> * Refer the above open and save operation to shows the create a server using WebAPI configuration for Excel import and export. In ASP.NET Core and ASP.NET MVC you can configure the server in controller.

## Server Dependencies

Open and save helper functions are shipped in the Syncfusion.EJ2.Spreadsheet package, which is available in Essential Studio<sup style="font-size:70%">&reg;</sup> and [`nuget.org`](https://www.nuget.org/). Following list of dependencies required for Spreadsheet open and save operations.

| **Platforms** | **Assembly** | **Nuget Package** |
| ----- | ----- | ----- |
| ASP.NET Core (Targeting .NET Core) | Syncfusion.EJ2.AspNet.Core <br/> Syncfusion.EJ2.Spreadsheet.AspNet.Core <br/> Syncfusion.Compression.Net.Core <br/> Syncfusion.XlsIO.Net.Core <br/> Syncfusion.XlsIORenderer.Net.Core <br/> | [Syncfusion.EJ2.Spreadsheet.AspNet.Core](https://www.nuget.org/packages/Syncfusion.EJ2.Spreadsheet.AspNet.Core) <br/> [Syncfusion.XlsIORenderer.Net.Core](https://www.nuget.org/packages/Syncfusion.XlsIORenderer.Net.Core) |
| ASP.NET MVC5 | Syncfusion.EJ2.MVC5 <br/>Syncfusion.EJ2.Spreadsheet.AspNet.MVC5 <br/> Syncfusion.Compression.Base <br/> Syncfusion.XlsIO.AspNet.Mvc5 <br/> Syncfusion.ExcelToPdfConverter.AspNet.Mvc5 <br/> | [Syncfusion.EJ2.Spreadsheet.AspNet.MVC5](https://www.nuget.org/packages/Syncfusion.EJ2.Spreadsheet.AspNet.MVC5) <br/> [Syncfusion.ExcelToPdfConverter.AspNet.Mvc5](https://www.nuget.org/packages/Syncfusion.ExcelToPdfConverter.AspNet.Mvc5) |


## See Also

* [Filtering](filter)
* [Sorting](sort)
* [Hyperlink](link)
* [Docker Image](./docker-deployment)