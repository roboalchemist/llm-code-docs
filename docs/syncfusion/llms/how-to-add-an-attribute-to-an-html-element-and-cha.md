# Source: https://docs.syncfusion.com/windowsforms/html-viewer/faq/how-to-add-an-attribute-to-an-html-element-and-cha.md

# How To add an attribute to an HTML element and change its value at run-time?

You can add an attribute to an HTML element using the Add method of the Attributes property, as shown in the following code snippet.

{% tabs %}

{% highlight C# %}



// textBox is an INPUT element of type 'text' in the HTML document

if(this.textBox.Attributes.Contains("style") == false)

this.textBox.Attributes.Add("style");

{% endhighlight %}

{% highlight VB %}



' textBox is an INPUT element of type 'text' in the HTML document

If Me.textBox.Attributes.Contains("style") = False Then

Me.textBox.Attributes.Add("style")

End If

{% endhighlight %}

{% endtabs %}

You can change the value of an element's attribute at run time by using the Value property of that particular attribute, as shown in the below code snippet.

{% tabs %}

{% highlight C# %}



// textBox is an INPUT element of type 'text' in the HTML document

this.textBox.Attributes["style"].Value = "background-color:red";

{% endhighlight %}

{% highlight VB %}



' textBox is an INPUT element of type 'text' in the HTML document

Private Me.textBox.Attributes("style").Value = "background-color:red"

{% endhighlight %}

{% endtabs %}


