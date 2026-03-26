# Source: https://docs.syncfusion.com/uwp/numeric-updown/autoreverse.md

# Source: https://docs.syncfusion.com/uwp/domain-updown/autoreverse.md

# Source: https://docs.syncfusion.com/wpf/domain-updown/autoreverse.md

# AutoReverse in WPF Domain Updown (SfDomainUpDown)

Incrementing the value starts from the maximum value once it has reached the minimum value and starts from the minimum value once it has reached the maximum value.

{% tabs %}
{%highlight xaml%}

<editors:SfDomainUpDown x:Name="domainUpDown"
                       HorizontalAlignment="Center"
                       VerticalAlignment="Center"
                       Width="200" 
                       AutoReverse="True"
                       ItemsSource="{Binding Employees}">
</editors:SfDomainUpDown >

{%endhighlight%}
{% endtabs %}
