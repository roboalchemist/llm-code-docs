# Source: https://docs.syncfusion.com/uwp/radial-menu/populating-color-palette.md

# Source: https://docs.syncfusion.com/wpf/radial-menu/populating-color-palette.md

# Populating Color Palette in WPF Radial Menu (SfRadialMenu)

Color Palette can be formed in Radial Menu with the Radial Color Items. 

{%highlight xaml%}





<navigation:SfRadialMenu IsOpen="True" >

    <navigation:SfRadialMenuItem Header="Font Color">



       <navigation:SfRadialMenuItem Header="Font"/>



       <navigation:SfRadialColorItem Color="Red">

           <navigation:SfRadialColorItem Color="DarkRed"/>

           <navigation:SfRadialColorItem Color="IndianRed"/>

           <navigation:SfRadialColorItem Color="OrangeRed"/>

           <navigation:SfRadialColorItem Color="MediumVioletRed"/>

       </navigation:SfRadialColorItem>

       <navigation:SfRadialColorItem Color="Green"/>

       <navigation:SfRadialColorItem Color="Blue"/>



     </navigation:SfRadialMenuItem>

</navigation:SfRadialMenu>

{%endhighlight%}



![Concepts_img5](Concepts_images/Concepts_img5.png)

