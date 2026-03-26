# Source: https://docs.syncfusion.com/windowsforms/testing/uft/limitations.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/limitations.md

# Limitations in WPF Spreadsheet (SfSpreadsheet)

## Release memory held by AutomationPeer

SfSpreadsheet holds some instance in memory even after disposing the spreadsheet or removed the sheets from the spreadsheet. Because, theÂ **AutomationPeer** for WPF Components holdsÂ some memory andÂ itÂ needsÂ toÂ beÂ releasedÂ manually. This can be done byÂ using theÂ following steps.

Create a class derived fromÂ `WindowAutomationPeer`Â andÂ overrideÂ it'sÂ `GetChildrenCore`Â method and returnsÂ ânullâ value that clearsÂ theÂ **AutomationPeer**Â item from memory as follows

{% tabs %}
{% highlight c# %}
public class FakeWindowsPeer : WindowAutomationPeer
{

    public FakeWindowsPeer (Window window): base(window)
    { }

    protected override List<AutomationPeer> GetChildrenCore()
    {
        return null;
    }
}
{% endhighlight %}
{% endtabs %}

NowÂ overrideÂ theÂ `OnCreateAutomationPeer`Â ofÂ the window andÂ itÂ returns theÂ classÂ as follows.

{% tabs %}
{% highlight c# %}
public partial class MainWindow : Window
{

    public MainWindow()
    {
        InitializeComponent();
    }

    protected override AutomationPeer OnCreateAutomationPeer()
    {
        return new FakeWindowsPeer(this);
    }
}
{% endhighlight %}
{% endtabs %}


N> You can refer to our [WPF Spreadsheet](https://www.syncfusion.com/wpf-controls/spreadsheet) feature tour page for its groundbreaking feature representations. You can also explore our [WPF Spreadsheet example](https://github.com/syncfusion/wpf-demos) to know how to render and configure the spreadsheet.