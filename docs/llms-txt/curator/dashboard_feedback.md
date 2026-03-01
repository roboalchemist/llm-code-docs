# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/dashboard_feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dashboard Feedback

> Enable user feedback collection on dashboards through Data Manager integration for improved user experience and insights.

In order to gather valuable insights from your audience about their experience using your Dashboards, Curator can
provide a simple and easy feedback mechanism for your users to submit their feedback, questions, and requests.  After
following the [Creating a Form](/embedding_using_analytics/data_manager/creating_a_form)
outline to build out your desired form, follow the guide below to integrate the Dashboard feedback in to your Dashboard
pages.

## Modifying your for to support the Dashboard URL

In order to gather the context of which Dashboard a user is providing feedback for, you'll need to add a new hidden
field that will store the Dashboard URL (the Curator URL).

### Adding a new Data Attribute

To add this attribute to your form:

1. Go to Data Manager > Data Attributes to set up the fields you want:
   <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=029761ded0b7309fd67bf21e591eba61" alt="Create Data Attribute" data-og-width="1209" width="1209" data-og-height="757" height="757" data-path="assets/images/embedding_using_analytics/data_manager/DashFeed4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=dde77fa6e66c297e3874e8639a2a552c 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=7bf0a197aa01cd5c56ca54d3f58a5855 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=eb10561b9407b47f815813a84c57803f 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=12090b2c015eccc9a8ce7fa2142d642a 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=7227558d2278471404bfea66f62b6be3 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed4.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=887d53db463561bd92e812a2a0fc519f 2500w" />
2. In the Create Attribute page, set the name, description (optional), and the field type.
3. Make sure the field type is set to **Short Text**.
   <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e089de57806d1e0ef0cac575e8e4f62e" alt="Select Short Text from Dropdown" data-og-width="1327" width="1327" data-og-height="1039" height="1039" data-path="assets/images/embedding_using_analytics/data_manager/DashFeed5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f058c32d19e269795b30834d179be223 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ad03e7a7e1c6abd8623909a7726c5fee 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4b1d3a4699c07f5badb72f24ad423281 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=2b5a49718313d165bb5fe9f05bd2b8af 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=75fdb94d6fc56624d60a39a23d215e60 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed5.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=1d8bcd9232c71ed339cff54fc4969fda 2500w" />

Next, navigate to your Data Manager Group, and associate the Attribute you just created with your Group.

### Identifying the form to use in Portal Settings

There's one last step to set up your Dashboard Feedback.

1. Navigate to Settings > Tableau > Tableau Server Settings.
2. Find the Dashboard Feedback on the General tab.
3. For the **Feedback Form** select your Data Group.
4. For the **Dashboard URL** select the Short Text Data Attribute you created to store the the Dashboard URL.

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=02047220f69fd42fd4f844e941f6c0d5" alt="Settings" data-og-width="1084" width="1084" data-og-height="967" height="967" data-path="assets/images/embedding_using_analytics/data_manager/DashFeed6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ceb9ba5a4bc4ed2da889541b609984b7 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8168772ccfd208df2559eddf5e671d7d 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=23f05fa623e06a39dfff87da9cd0771c 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=62307bd593166f5c5b9b5a6c634b2ab1 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=0a8fca34e4b98c160120d501630cb226 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/data_manager/DashFeed6.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ec7088839eee77e0e0ab843563021ca2 2500w" />
