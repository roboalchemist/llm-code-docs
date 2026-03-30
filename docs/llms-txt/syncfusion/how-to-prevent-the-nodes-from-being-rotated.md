# Source: https://docs.syncfusion.com/windowsforms/diagram/faq/how-to-prevent-the-nodes-from-being-rotated.md

# How To Prevent the Nodes From Being Rotated

This can be done by raising the Diagram.Model.EventSink.RotationChanging event and canceling the operation.

{% tabs %}

{% highlight c# %}

this.diagram1.Model.EventSink.RotationChanging += new RotationChangingEventHandler(EventSink_RotationChanging); 

void EventSink_RotationChanging(RotationChangingEventArgs evtArgs) 

{ 

    evtArgs.Cancel = true; 

}

{% endhighlight %}

{% highlight vbnet %}

Me.diagram1.Model.EventSink.RotationChanging += New RotationChangingEventHandler(EventSink_RotationChanging) 

Private Sub EventSink_RotationChanging(ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.RotationChangingEventArgs)

evtArgs.Cancel = True

End Sub

{% endhighlight %}

{% endtabs %}