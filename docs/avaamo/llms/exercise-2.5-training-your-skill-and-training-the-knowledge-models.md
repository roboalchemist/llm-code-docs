# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-2-building-an-answers-skill/exercise-2.5-training-your-skill-and-training-the-knowledge-models.md

# Exercise 2.5: Training the knowledge models

### **Retrain**

If you have edited the details of your uploaded document or URL then you need to retrain the document. You could also use this option if there has been an error during upload.

**To retrain follow the following steps**:

* In the Answers Skill page, navigate to Implementation -> Documents\
  option in the left navigation menu.
* Click Retrain option, this starts a new cycle of extracting the content and creating a new knowledge base.

### **Edit**

Here you can make edits to your document. To make edits to your document

* In the Answers Skill page, navigate to Implementation -> Documents\
  option in the left navigation menu.
* Click the Edit option. Update the title. (Attributes will be covered in the advanced training).

![](https://lh4.googleusercontent.com/-bKbXtWo98qScILLEj99qp930Z1UXoAeNBB4hITlVXXq_qi_wSSLjEeA7GyMmk7By24YHJfmvNfYLAXremaC4Fi2CDqXHLUtqf1HSBuzuYateJtjSrLDMsXLj4yfrH4RA6bhN8Av)

### **Adding Training Variations**

You can train the skill to increase the accuracy of the skill. In order to do so, we need to identify the section to which your question corresponds and then train the section with your question.

In our example- What is the late payment fee?, let’s add the training data: What is the late fee?

* Navigate to Answers -> Implementation -> Knowledge -> Section
* Search for the section using the search bar located in the section tab

![](https://lh6.googleusercontent.com/cpFKvh9bN5XOZPRNE9W12Ev2koNWKTbblM6ruCWuOx6gwyuCDjoRxQI8-ycsLrxevJAlE8UzoWVum-KudytI2PMJPpHs-64hiO7tFhUouWRTul465lg8KnDJ6p31ZYo3qdhun8x8)

* Once you have found the section, let's add, What is the late fee? as training data to the Add Training Data section.
* Save your changes in the Skill and test this variation in the Agent.&#x20;
* Repeat this exercise for 3 other sections of the document.<br>
