# Source: https://docs.syncfusion.com/maui/themes/howto.md

# Switching Between Light Theme and Dark Theme

Refer to the following example code to switch between light and dark themes in Syncfusion<sup>Â®</sup> MAUI controls.

{% highlight C# %} 
void UpdateTheme(object sender, System.EventArgs e)
{
    ICollection<ResourceDictionary> mergedDictionaries = Application.Current.Resources.MergedDictionaries;
    if (mergedDictionaries != null)
    {
        var theme = mergedDictionaries.OfType<SyncfusionThemeResourceDictionary>().FirstOrDefault();
        if (theme != null)
        {
            if (theme.VisualTheme is SfVisuals.MaterialDark)
            {
                theme.VisualTheme = SfVisuals.MaterialLight;
            }
            else
            {
                theme.VisualTheme = SfVisuals.MaterialDark;
            }
        }
     }
}

{% endhighlight %}

The complete theme switch sample is available in this [link](https://github.com/SyncfusionExamples/Switching-between-light-and-dark-themes-in-.NET-Maui).