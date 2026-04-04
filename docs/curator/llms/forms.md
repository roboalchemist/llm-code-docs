# Source: https://docs.curator.interworks.com/site_content_design/pages/forms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Forms

> Build custom web forms for data collection, feedback, and user requests using Curator Data Manager capabilities.

Whether it's storing small data-sets from around your business, getting valuable feedback from your users, or creating a
simple contact-us / request access form Curator's data manager has the web form building capabilities you need.

## Creating a Form

You can create a form on the backend using Curator's Data Manager feature.  See here for more information on how to
create forms and fields in our [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
section.

## Adding a Form to a Page

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you want to add your form to from the Pages list or click "New Page" to create a new page.
4. Add a new element to your page, and when the modal pops-up, click the "Analytic Element" tab and select the "Curator
   Data Group" option.
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1879c9c74c991a65fff875b668794946" alt="Curator Data Group element" data-og-width="929" width="929" data-og-height="634" height="634" data-path="assets/images/site_content_design/pages/select_data_group_page_element.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=5e0ea6bff05a3994a2b8c135e1089f1b 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=07ba7ceb93938e74b8a903ea2f16c42b 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=d9bc228a29b2a675aae6253bc947444f 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=3dcce62f9529215e0c72e13fd9caa867 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=585ebdd8b1d7529b770ce522a4853f59 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/pages/select_data_group_page_element.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a74faf85334ec5ce00b47fc587191853 2500w" />
5. In the Page Styles section on the left-hand side, you can choose to either embed the Form Only for receiving inputs,
   or you can add the Table view to allow your end-users to see the data that has already been added.

## Forms and Tableau Dashboards on Pages

Some Tableau Dashboards can pull their results from Form submissions. In cases like this it can be useful to have the
Tableau Dashboard refresh it's data after a Form submission. Curator will automatically refresh all Tableau Dashboards
that are on a page with a Form if a Form submission occurs.
