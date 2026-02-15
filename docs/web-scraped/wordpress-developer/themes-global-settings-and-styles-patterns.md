# Patterns

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/patterns/](https://developer.wordpress.org/themes/global-settings-and-styles/patterns/)



# Patterns



↑Back to top



Thepatternsproperty intheme.jsonlets you bundle patterns from the WordPressPattern Directorywith your theme. This is a neat system that lets you provide a wide variety of patterns that you’ve personally selected without having to design and build them yourself. Any pattern in the directory is available to you.



And if you’re feeling adventurous, you can even submit your custom-designed patterns to the directory. This will let you both bundle them with your theme and let other theme creators and users use your patterns, even when your theme is not installed.


In this document, you will learn how to include directory patterns for your theme’s users with just a few lines of code intheme.json.


## Adding patterns from the directory


patternsis an optional property that lets you bundle as many or as few patterns as you’d like with your theme. The property accepts an array of pattern slugs, and as long as those patterns exist in the Patterns Directory, they will appear in thePatternsinserter in the WordPress editors.


Here is a look at thepatternsproperty in the defaulttheme.json:


```
{
	"version": 2,
	"patterns": []
}
```


Let’s take a look at one of the patterns from the Pattern Directory:Hero banner with overlap images. To find the slug for the pattern, you need to look in the address bar of your browser, which should give you this URL:


```
https://wordpress.org/patterns/pattern/hero-banner-with-overlap-images/
```


The slug is the part of the URL that comes afterhttps://wordpress.org/patterns/pattern/. In this case, the slug ishero-banner-with-overlap-images(note that the final slash is not included).


To include this pattern with your theme, you need to pass only the slug to thepatternsarray intheme.json:


```
{
	"version": 2,
	"patterns": [
		"hero-banner-with-overlap-images"
	]
}
```


Now that you’ve got the basics down, pick out a couple of other patterns and add them to yourpatternsarray intheme.json:


```
{
	"version": 2,
	"patterns": [
		"fullscreen-cover-image-gallery",
		"hero-banner-with-overlap-images",
		"mixed-shape-gallery"
	]
}
```


Now you should see your chosen patterns in thePatternsinserter in the UI:



The patterns you include will automatically appear under the categories they are assigned to in the Pattern Directory. These are mapped to the existing patterns registered within WordPress. The patterns from the above example code all have thegallerypattern category, so they appear under thePatterns > Gallerytab in the inserter.





First published


October 17, 2023


Last updated


December 14, 2023



[PreviousCustom TemplatesPrevious: Custom Templates](https://developer.wordpress.org/themes/global-settings-and-styles/custom-templates/)
[NextTemplate PartsNext: Template Parts](https://developer.wordpress.org/themes/global-settings-and-styles/template-parts/)


