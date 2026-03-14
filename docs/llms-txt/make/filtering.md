# Source: https://developers.make.com/api-documentation/pagination-sorting-filtering/filtering.md

# Filtering

Use the `cols[]` parameter to select values you want in the response. You can also use the `cols[]` parameter to get values that the endpoint does not return by default. The set of available filtering values is different for each endpoint. Check the example API call responses to see what data you can get from the API call.

Specify the `cols[]` parameter multiple times in the API call to get multiple values from the endpoint. You can put numbers in the brackets to specify order in which you want to list the values in the API call response.

**Example:** Get only the `name`, `id` and `teams` in the specified organization. List the data in order: `name`, `id`, `teams`.

{% stepper %}
{% step %}
The request URL snippet to get the `name`, `id` and `teams` values of the specified organization, in the specified order, looks like this:

```
/organizations/{organizationId}?cols[1]=id&cols[2]=name&cols[3]=teams
```

{% endstep %}

{% step %}
After encoding the square brackets you get the following request URL. The `organizationId` in our test case is 8013:

```
/organizations/8013?cols%5B1%5D=id&cols%5B2%5D=name&cols%5B3%5D=teams
```

{% endstep %}

{% step %}
The full request looks like this:

```
GET {base-url}/organizations/8013?cols%5B1%5D=id&cols%5B2%5D=name&cols%5B3%5D=teams
```

{% endstep %}
{% endstepper %}

Some endpoints have specific filtering parameters. For example, in the `/templates` endpoint you can use the `usedApps[]` parameter. The `usedApps[]` parameter allows you to get only the templates containing specific apps.
