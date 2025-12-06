# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/collaborative-tagging

Learn how to use Atlas to annotate datasets with your team.

## Tags and selections​

Atlas uses the concept of selections to let you create flexible selections of points in your dataset across
browsing sessions. Tags provide a way to save sets of points you're interested in, share them with your team,
and mark them for future action. We've seen people use tags for things like identifying data to remove from machine learning training runs,
flagging data as potential misconduct, or just to bookmark datapoints they want to look at later.

As an example, let's explore tagging on Wikipedia

### Tagging selections​

First, build a selection on your dataset. Below, we select two regions using the lasso tool,
one in the top right and one in the left regions of our map.
We can combine these lasso selections with a union operation by clicking 'any' in the top section of the selection tools.
(Choose 'all' if you want the strict intersection of the lassos.)

To save and label these points, click the 'tag' icon. This will open a pop-up that shows the different
tags already applied to your selection, and a bar chart of counts for each tag.
To add a new tag or apply an existing tag to a selection, type your desired tag name
into the textbox at the top of the pop-up and press Enter on your keyboard or click 'Add'.

You can use this pattern to annotate complex subsets of your data by combining different Atlas selection tools.
For example, we perform a full-text search for "New York" and intersect it with a lasso over the newspaper region
to create a "new york newspapers" tag.

### Tagging individual datapoints​

Atlas gives you the ability to fine-tune your tagged selections.
Browsing through selected points in "new york newspapers", we can apply a new or existing
tag to specific points by clicking the '+' icon, and
remove a tag by clicking on 'x' for a label that we do not want a point to have.

## View collaborator tags​

Atlas tags are scoped on a user level. Tags created by collaborators will show up as '@collaborator/tag_name' for
project owners and editors.
Only users with Edit permissions (currently owners and admins) may create tags for a map.
You can view selections from both your and your collaborator's tags
by using the Filter tool. If you select multiple tags from the Filter dropdown, this creates a new selection
of all tags selected by any user.

## Building off of existing tags​

You can easily work off your and your collaborator's tags by using the Tag Filter.
In the image below, several users have created 'person' tags using different kinds of searches.
Now, we can

- filter on all those tags
- tag new points by using a lasso or any other selection tool, and finally
- tag the entire selection with 'person' to update our tag to include all of our and our collaborator's changes. This
updated tag will be visible to your collaborators.
## Export your tags​

Create a selection from your target tags using the filter tool and download the selection.

- Tags and selectionsTagging selectionsTagging individual datapoints
- Tagging selections
- Tagging individual datapoints
- View collaborator tags
- Building off of existing tags
- Export your tags
