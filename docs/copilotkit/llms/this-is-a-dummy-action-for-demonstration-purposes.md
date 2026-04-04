# this is a dummy action for demonstration purposes
action = CopilotAction(
    name="fetchNameForUserId",
    description="Fetches user name from the database for a given ID.",
    parameters=[\
        {\
            "name": "userId",\
            "type": "string",\
            "description": "The ID of the user to fetch data for.",\
            "required": True,\
        }\
    ],
    handler=fetch_name_for_user_id
)