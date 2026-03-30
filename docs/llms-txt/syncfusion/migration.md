# Source: https://docs.syncfusion.com/maui/treeview/migration.md

# Source: https://docs.syncfusion.com/maui/timepicker/migration.md

# Source: https://docs.syncfusion.com/maui/textinputlayout/migration.md

# Source: https://docs.syncfusion.com/maui/treemap/migration.md

# Source: https://docs.syncfusion.com/maui/tabview/migration.md

# Source: https://docs.syncfusion.com/maui/switch/migration.md

# Source: https://docs.syncfusion.com/maui/sunburstchart/migration.md

# Source: https://docs.syncfusion.com/maui/stepprogressbar/migration.md

# Source: https://docs.syncfusion.com/maui/slider/migration.md

# Source: https://docs.syncfusion.com/maui/signaturepad/migration.md

# Source: https://docs.syncfusion.com/maui/shimmer/migration.md

# Source: https://docs.syncfusion.com/maui/segmented-control/migration.md

# Source: https://docs.syncfusion.com/maui/scheduler/migration.md

# Source: https://docs.syncfusion.com/maui/rotator/migration.md

# Source: https://docs.syncfusion.com/maui/rich-text-editor/migration.md

# Source: https://docs.syncfusion.com/maui/rating/migration.md

# Source: https://docs.syncfusion.com/maui/range-slider/migration.md

# Source: https://docs.syncfusion.com/maui/radio-button/migration.md

# Source: https://docs.syncfusion.com/maui/radial-menu/migration.md

# Source: https://docs.syncfusion.com/maui/radial-gauge/migration.md

# Source: https://docs.syncfusion.com/maui/pyramid-charts/migration.md

# Source: https://docs.syncfusion.com/maui/pull-to-refresh/migration.md

# Source: https://docs.syncfusion.com/maui/popup/migration.md

# Source: https://docs.syncfusion.com/maui/polar-charts/migration.md

# Source: https://docs.syncfusion.com/maui/picker/migration.md

# Source: https://docs.syncfusion.com/maui/parallax-view/migration.md

# Source: https://docs.syncfusion.com/maui/numericentry/migration.md

# Source: https://docs.syncfusion.com/maui/navigationdrawer/migration.md

# Source: https://docs.syncfusion.com/maui/masked-entry/migration.md

# Source: https://docs.syncfusion.com/maui/maps/migration.md

# Source: https://docs.syncfusion.com/maui/listview/migration.md

# Source: https://docs.syncfusion.com/maui/linearprogressbar/migration.md

# Source: https://docs.syncfusion.com/maui/linear-gauge/migration.md

# Source: https://docs.syncfusion.com/maui/kanban-board/migration.md

# Source: https://docs.syncfusion.com/maui/imageeditor/migration.md

# Source: https://docs.syncfusion.com/maui/funnel-charts/migration.md

# Source: https://docs.syncfusion.com/maui/expander/migration.md

# Source: https://docs.syncfusion.com/maui/effects-view/migration.md

# Source: https://docs.syncfusion.com/maui/digitalgauge/migration.md

# Source: https://docs.syncfusion.com/maui/datetime-range-selector/migration.md

# Source: https://docs.syncfusion.com/maui/datepicker/migration.md

# Source: https://docs.syncfusion.com/maui/datagrid/migration.md

# Source: https://docs.syncfusion.com/maui/dataform/migration.md

# Source: https://docs.syncfusion.com/maui/combobox/migration.md

# Source: https://docs.syncfusion.com/maui/circularprogressbar/migration.md

# Source: https://docs.syncfusion.com/maui/checkbox/migration.md

# Source: https://docs.syncfusion.com/maui/circular-charts/migration.md

# Source: https://docs.syncfusion.com/maui/chips/migration.md

# Source: https://docs.syncfusion.com/maui/chat/migration.md

# Source: https://docs.syncfusion.com/maui/cartesian-charts/migration.md

# Source: https://docs.syncfusion.com/maui/carousel-view/migration.md

# Source: https://docs.syncfusion.com/maui/calendar/migration.md

# Source: https://docs.syncfusion.com/maui/cards/migration.md

# Source: https://docs.syncfusion.com/maui/button/migration.md

# Source: https://docs.syncfusion.com/maui/busy-indicator/migration.md

# Source: https://docs.syncfusion.com/maui/barcode-generator/migration.md

# Source: https://docs.syncfusion.com/maui/badge-view/migration.md

# Source: https://docs.syncfusion.com/maui/backdrop/migration.md

# Source: https://docs.syncfusion.com/maui/avatar-view/migration.md

# Source: https://docs.syncfusion.com/maui/autocomplete/migration.md

# Source: https://docs.syncfusion.com/maui/accordion/migration.md

# Source: https://docs.syncfusion.com/maui/common/migration.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor-classic/migration.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/migration.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/migration.md

# Migration from PDF Viewer (Classic) to SfPdfViewer

## Why PDF Viewer (Classic) to PDF Viewer control

Migrating to the PDF Viewer control delivers better performance and a simplified deployment model. Scrolling, page navigation, and printing are optimized for a smoother user experience. The newer viewer also removes the WebAssembly server service dependency required by the classic control, reducing app complexity and maintenance.

* **Enhanced performance**:
Experience faster scrolling, more responsive page navigation, and improved printing throughput for large documents.

* **No server service dependency**:
The newer viewer does not require a separate ServiceUrl or server-side WebAssembly service; client-side rendering is handled by the component.

* **Unified package across platforms**:
A single package supports Windows, macOS, and Linux, making installation consistent across environments.

### Nuget Package

To initialize the PDF Viewer component, add the following package references to the project **.csproj** file.

<table>
<tr>
<th>PDF Viewer (Classic)</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle=".csproj" hl_lines="4 7" %}

<ItemGroup>

	<!-- If you are using a Web Assembly application, include the following line in the .csproj file -->
	<PackageReference Include="Syncfusion.Blazor.PdfViewer"/>

    <!-- If you are using a Server Assembly application, include the following line in the .csproj file -->
	<!--<PackageReference Include="Syncfusion.Blazor.PdfViewerServer"/>-->
		
</ItemGroup>

{% endhighlight %}
{% endtabs %}
</td>
</tr>
<tr>
<th>PDF Viewer</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle=".csproj" hl_lines="2" %}

<ItemGroup>
    <PackageReference Include="Syncfusion.Blazor.SfPdfViewer"/>
</ItemGroup>

{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

### Script File

To use the PDF Viewer component, add the corresponding script reference in the app host page (**Host.cshtml** or **Layout.cshtml**) based on the framework version.

N> The same script file is used for both `Server application` and `Web assembly application` for the PDF Viewer component.

<table>
<tr>
<th>PDF Viewer (Classic)</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight html tabtitle="(~/Layout.cshtml/Host.cshtml)" hl_lines="7" %}

<head>
    <!-- Syncfusion Blazor PDF Viewer controls theme style sheet -->
    <link href="_content/Syncfusion.Blazor.Themes/bootstrap5.css" rel="stylesheet" />
</head>
<body>
    <!-- Syncfusion Blazor PDF Viewer controls scripts -->
    <script src="_content/Syncfusion.Blazor.PdfViewer/scripts/syncfusion-blazor-pdfviewer.min.js" type="text/javascript"></script>
</body>

{% endhighlight %}
{% endtabs %}
</td>
</tr>
<tr>
<th>PDF Viewer</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight html tabtitle="(~/Layout.cshtml/Host.cshtml)" hl_lines="7" %}

<head>
    <!-- Syncfusion Blazor SfPdfViewer controls theme style sheet -->
    <link href="_content/Syncfusion.Blazor.Themes/bootstrap5.css" rel="stylesheet" />
</head>
<body>
    <!-- Syncfusion Blazor SfPdfViewer controls scripts -->
    <script src="_content/Syncfusion.Blazor.SfPdfViewer/scripts/syncfusion-blazor-sfpdfviewer.min.js" type="text/javascript"></script>
</body>

{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

### Program.cs

Add the following to the **Program.cs** file to register Syncfusion Blazor services. For WebAssembly apps, enable in-memory caching as shown in the comment.

<table>
<tr>
<th>PDF Viewer (Classic)</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle=".NET 6 & .NET 7 (~/Program.cs)" hl_lines="1" %}

builder.Services.AddSyncfusionBlazor();

{% endhighlight %}
{% endtabs %}
</td>
</tr>

<tr>
<th>PDF Viewer</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle=".NET 6 & .NET 7 (~/Program.cs)" hl_lines="1 4" %}

builder.Services.AddSyncfusionBlazor();

// If you are using a WebAssembly application, include the following line in the Program.cs file
// builder.Services.AddMemoryCache();

{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

### Index.razor

To render the PDF Viewer component, add the following code in the **Index.razor** file. In the newer viewer, a ServiceUrl is not required; specify only the DocumentPath and layout attributes.

<table>
<tr>
<th>PDF Viewer (Classic)</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle="Index.razor" hl_lines="2 5" %}

@* If you are using a Web Assembly application, include the following line in the Index.razor file*@
<SfPdfViewer DocumentPath="PDF_Succinctly.pdf" ServiceUrl="api/pdfviewer" Height="100%" Width="100%"></SfPdfViewer>

@* If you are using a Server Assembly application, include the following line in the Index.razor file
<SfPdfViewerServer DocumentPath="PDF_Succinctly.pdf" Height="100%" Width="100%"></SfPdfViewerServer>*@

{% endhighlight %}
{% endtabs %}

</td>
</tr>
<tr>
<th>PDF Viewer</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle="Index.razor" %}

<SfPdfViewer2 DocumentPath="PDF_Succinctly.pdf" Height="100%" Width="100%"></SfPdfViewer2>

{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

### Project.cs

For WebAssembly applications, include the following properties in the project **.csproj** file to ensure proper functionality and compatibility.

<table>
<tr>
<th>PDF Viewer</th>
</tr>
<tr>
<td>
{% tabs %}
{% highlight C# tabtitle="csproj" hl_lines="2 6 7" %}
<ItemGroup>
    <NativeFileReference Include="$(SkiaSharpStaticLibraryPath)\2.0.23\*.a" />
</ItemGroup>

<PropertyGroup>
	<WasmNativeStrip>true</WasmNativeStrip>
	<WasmBuildNative>true</WasmBuildNative>
</PropertyGroup>
{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

N> For WebAssembly applications, install the [SkiaSharp.NativeAssets.WebAssembly](https://www.nuget.org/packages/SkiaSharp.NativeAssets.WebAssembly) NuGet package.

N> When hosting in certain environments (for example, Azure App Service), use [SkiaSharp.Views.Blazor](https://www.nuget.org/packages/SkiaSharp.Views.Blazor) instead of [SkiaSharp.NativeAssets.WebAssembly](https://www.nuget.org/packages/SkiaSharp.NativeAssets.WebAssembly). Align native asset versions in the project file with the installed package version.

## See also

* [Getting Started with Blazor SfPdfViewer Component in Blazor Web app Server App](./getting-started/web-app)

* [Getting Started with Blazor SfPdfViewer Component in Blazor WASM App](./getting-started/web-assembly-application)