# Source: https://www.elastic.co/docs/deploy-manage/manage-spaces

﻿---
title: Spaces
description: Spaces let you organize your content and users according to your needs. Each space has its own saved objects.Users can access only the spaces that they...
url: https://www.elastic.co/docs/deploy-manage/manage-spaces
products:
  - Elastic Cloud Serverless
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Spaces
**Spaces** let you organize your content and users according to your needs.
- Each space has its own saved objects.
- Users can access only the spaces that they have been granted access to. This access is based on user roles, and a given role can have different permissions per space.
- In Elastic Stack deployments on version 8.16 and later, each space has its own navigation, called solution view.

Kibana creates a default space for you. When you create more spaces, users are asked to choose a space when they log in, and can change their current space at any time from the top menu.
![Change current space menu](https://www.elastic.co/docs/deploy-manage/images/kibana-change-space.png)

You can find the **Spaces** management page in the navigation menu or use the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
For more info on working with spaces, check out:
- [Create a space](#spaces-managing)
- [Define access to a space](#spaces-control-user-access)
- [Move saved objects between spaces](#spaces-moving-objects)
- [Configure a space-level landing page](#spaces-default-route)
- [Make API calls to a space](#spaces-api-requests)
- [Delete a space](#_delete_a_space)

Check out [Using Spaces with Fleet](https://www.elastic.co/docs/deploy-manage/manage-spaces-fleet) for info on using spaces with Fleet in a space-aware data model.

## Required permissions

- <applies-to>Elastic Cloud Serverless: Generally available</applies-to> `Admin` role or equivalent
- <applies-to>Elastic Stack: Generally available</applies-to> `kibana_admin` or equivalent


## Create a space

The maximum number of spaces that you can have differs by deployment type:
- <applies-to>Elastic Cloud Serverless: Generally available</applies-to> Maximum of 100 spaces.
- <applies-to>Elastic Stack: Generally available</applies-to> Controlled by the `xpack.spaces.maxSpaces` setting. Default is 1000. View the [full list of Space settings](https://www.elastic.co/docs/reference/kibana/configuration-reference/spaces-settings).

To create a space:
<applies-switch>
  <applies-item title="serverless:" applies-to="Elastic Cloud Serverless: Generally available">
    1. Click **Create space** or select the space you want to edit.
    2. Provide:
       - A meaningful name and description for the space.
    - A URL identifier. The URL identifier is a short text string that becomes part of the Kibana URL. Kibana suggests a URL identifier based on the name of your space, but you can customize the identifier to your liking. You cannot change the space identifier later.
    3. Customize the avatar of the space to your liking.
    4. Save the space.
  </applies-item>

  <applies-item title="stack:" applies-to="Elastic Stack: Generally available">
    1. Select **Create space** and provide a name, description, and URL identifier.
       The URL identifier is a short text string that becomes part of the Kibana URL when you are inside that space. Kibana suggests a URL identifier based on the name of your space, but you can customize the identifier to your liking. You cannot change the space identifier once you create the space.
    2. Select a **Solution view**. This setting controls the navigation that all users of the space will get:
       - **Search**: A light navigation menu focused on analytics and Search use cases. Features specific to Observability and Security are hidden.
    - **Observability**: A light navigation menu focused on analytics and Observability use cases. Features specific to Search and Security are hidden.
    - **Security**: A light navigation menu focused on analytics and Security use cases. Features specific to Observability and Search are hidden.
    - **Classic**: All features from all solutions are visible by default using the classic, multilayered navigation menus. You can customize which features are visible individually.
    3. If you selected the **Classic** solution view, you can customize the **Feature visibility** as you need it to be for that space.
       <note>
       Even when disabled in this menu, some Management features can remain visible to some users depending on their privileges. Additionally, controlling feature visibility is not a security feature. To secure access to specific features on a per-user basis, you must configure [Kibana Security](https://www.elastic.co/docs/reference/elasticsearch/roles).
       </note>
    4. Customize the avatar of the space to your liking.
    5. Save your new space by selecting **Create space**.
  </applies-item>
</applies-switch>

You can edit all of the space settings you just defined at any time, except for the URL identifier.
Elastic also allows you to manage spaces using APIs:
- <applies-to>Elastic Cloud Serverless: Generally available</applies-to> [Serverless Spaces API](https://www.elastic.co/docs/api/doc/serverless/operation/operation-get-spaces-space)
- <applies-to>Elastic Stack: Generally available</applies-to> [Spaces API](https://www.elastic.co/docs/api/doc/kibana/operation/operation-post-spaces-copy-saved-objects)


## Define access to a space

Users can access spaces based on the roles that they have.
- Certain reserved roles can view and access all spaces by default. You can’t prevent those roles from accessing a space. Instead, you can grant different roles to your users.
- When creating or editing a role, you can define which existing spaces that role can access, and with which permissions. Role management differs between Elastic Stack deployments and serverless projects.
  - <applies-to>Elastic Cloud Serverless: Generally available</applies-to> Check [Custom roles](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-organization/user-roles).
- <applies-to>Elastic Stack: Generally available</applies-to> Check [Creating or editing a role](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/defining-roles).

If you're managing an Elastic Stack deployment, then you can also assign roles and define permissions for a space from the **Permissions** tab of the space settings.
When a role is assigned to *All Spaces*, you can’t remove its access from the space settings. You must instead edit the role to give it more granular access to individual spaces.

## Move saved objects between spaces

To move saved objects between spaces, you can [copy objects](/docs/explore-analyze/find-and-organize/saved-objects#managing-saved-objects-copy-to-space), or [export and import objects](/docs/explore-analyze/find-and-organize/saved-objects#managing-saved-objects-export-objects).

## Customize Kibana's home page

<applies-to>
  - Serverless Elasticsearch projects: Unavailable
  - Serverless Observability projects: Generally available
  - Serverless Security projects: Unavailable
  - Elastic Stack: Generally available
</applies-to>

Customize the Kibana landing page on a per-space basis to create a tailored experience for users. For example, you can direct users to a specific dashboard, application, or saved object. Users navigate to the custom landing page when:
- They enter the space.
- <applies-to>Elastic Stack: Generally available since 9.3</applies-to> They select the `logo_elastic` logo in the header.

To configure the landing page, use the default route setting in the [Kibana advanced settings](https://www.elastic.co/docs/reference/kibana/advanced-settings#kibana-general-settings). For example, you might set the default route to `/app/dashboards`.
You can access the **Advanced Settings** management page in the navigation menu or by using the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
![Configure space-level landing page](https://www.elastic.co/docs/deploy-manage/images/kibana-spaces-configure-landing-page.png)


## Make API calls to a space

When you access resources in Kibana using the [Kibana APIs](https://www.elastic.co/docs/api/doc/kibana/), unless you specify otherwise the API request is directed at the default space. To direct a request at a specific space, indicate that space by adding a `/<space>` element to the request path, directly after the Kibana URL.
For example, the following request retrieves a list of saved objects of type `dashboard` in the default Kibana space:
```bash
curl -u user:pass -H "kbn-xsrf: true" \
"https://${KIBANA_URL}/api/saved_objects/_find?type=dashboard"
```

To target the same request at a specific space, such as `marketing`, include the space identifier in the request path:
```bash
curl -u user:pass -H "kbn-xsrf: true" \
"https://${KIBANA_URL}/s/marketing/api/saved_objects/_find?type=dashboard"
```


## Delete a space

Deleting a space permanently removes the space and all of its contents. Find the space on the **Spaces** overview page and click the trash icon in the Actions column. You can’t delete the default space, but you can customize it to your liking.