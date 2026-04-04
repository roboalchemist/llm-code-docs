# Source: https://uat.rive.app/docs/editor/text/text-modifiers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Modifiers

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="RkahZjwf3aQ" />

Modifiers provide powerful ways to manipulate and animate the glyphs that make up text. Currently, the available Text Modifier properties include:

* Position
* Rotation
* Scale
* Origin
* Opacity
* Variables (requires variable supported font)

## Modifier Group

A Text Modifier group contains at least one range and up to one of each modifier property. Each Text object can have multiple modifier groups.

Use the `+` action alongside the modifier group name to enable a chosen property.

<Info>
  Each modifier group may only add one of each property type.
</Info>

<img src="https://mintcdn.com/rive/lCW_2ehNjFqyOfhq/images/editor/text/text-runs-modifiers-create.gif?s=cd6765433383866d9bb9e75bac4b395f" alt="Create Text Modifier Groups via the Inspector" width="1000" height="391" data-path="images/editor/text/text-runs-modifiers-create.gif" />

***

## Modifier Range

### Range

The modifier range defines the start and end point within the text for the applied properties. The range can be a percentage or an index value for a character, word, or line. Open the Range Options fly-out to configure the value increment type.

As an example, a range with a start point of 0% and an end value of 50% will only apply the defined properties to the first half of the text. So if we opt to add a scale property with a value of 25% to the modifier group — only the glyphs in the first half of the text will have the scale value of 25%.

You can see a visual representation of the range via a shaded area on the stage. You can configure the stage visual options in the visibility menu on the toolbar.

<img src="https://mintcdn.com/rive/lCW_2ehNjFqyOfhq/images/editor/text/text-runs-modifiers-range.gif?s=c630362d02e42913530f826ad2c5a8a8" alt="Apply transforms to the target text range" width="1000" height="485" data-path="images/editor/text/text-runs-modifiers-range.gif" />

### Falloff

Use the falloff values to add interpolation to the applied modifier properties. For example, a modifier group that scales glyphs to 200% with a range from 0% to 100% and a falloff of 25% to 75% will gradually scale glyphs up form 100% to 200% over the first quarter of the text, and back down again over the last quarter of the text.

The falloff can be visualised via the darker shading on the stage guide.

<img src="https://mintcdn.com/rive/lCW_2ehNjFqyOfhq/images/editor/text/text-runs-modifiers-fallof.gif?s=d8c1b0b74b27d01868534a18d7e9864d" alt="Use falloff to interpolate applied modifier properties" width="1000" height="475" data-path="images/editor/text/text-runs-modifiers-fallof.gif" />

### Offset

Use the offset value to traverse the range along the text value. Try animating the offset value to create wipe effects along a text value. For example, a scale modifier can animate the offset to make individual glyphs scale up and back down again.

<img src="https://mintcdn.com/rive/lCW_2ehNjFqyOfhq/images/editor/text/text-runs-modifiers-offset.gif?s=e7890ca7b6459ab6c9651c4fe309bfaa" alt="Text Runs Modifiers Offset" width="1000" height="471" data-path="images/editor/text/text-runs-modifiers-offset.gif" />

### Range Options

Additional range options can be found in the fly-out alongside the range name for more fine-grained control over the range selection behaviour.

#### Increment

Define whether modifier properties get applied by:

* Characters (with or without spaces)
* Words
* Lines

<Info>
  The increment value will affect an index-based Range Type.
</Info>

#### Mode

Change the range mode to define how modifier properties should be calculated when multiple ranges on the same group cross over. For example, if a modifier with multiple ranges applied a scale value of 200% — an add mode would increase the scale to 400% if the ranges were to crossover.

<Info>
  Turn on Modifier Range Values in the visibility menu to get a numerical indication of how much a Text Modifier is affecting glyphs.
</Info>

#### Strength

Adjust the strength to reduce the effect of a modifier within the range.

#### Range Type

Set the range type to configure range start, end, and offset values as a percentage of the text length, or by indices. You may also want to consider which increment value to use alongside the Range Type. For example, an index value of 1 incremented by characters will target the second character, whereas an index value of 1 incremented by words will target the start of the second word.

#### Falloff Interpolation

Modify the falloff interpolation to define a custom cubic curve. The falloff defaults to linear interpolation.

### View Options

Toggle visual guides on the stage via the visibility menu in the toolbar:

* Modifier Range: Toggle the display of a shaded area on the stage to highlight the range position on a selected text object.
* Modifier Range Values: Toggle the display of per-glyph values on modifier ranges to indicate the applied strength of a given modifier.

<img src="https://mintcdn.com/rive/lCW_2ehNjFqyOfhq/images/editor/text/text-runs-modifiers-options.gif?s=87389ff2c2cc6a2118d4b4ee20de7a86" alt="Text Runs Modifiers View Options" width="1000" height="426" data-path="images/editor/text/text-runs-modifiers-options.gif" />

## Use case: Animating a text pendulum

This simple example will get you used to animating with Text Modifiers.

<YouTube id="Wec_F45NLoY" />
