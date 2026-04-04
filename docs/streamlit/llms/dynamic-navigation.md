# Source: https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation

# Create a dynamic navigation menu - Streamlit Docs

Create a dynamic navigation menu
===============================

`st.navigation` makes it easy to build dynamic navigation menus. You can change the set of pages passed to `st.navigation` with each rerun, which changes the navigation menu to match. This is a convenient feature for creating custom, role-based navigation menus.

This tutorial uses `st.navigation` and `st.Page`, which were introduced in Streamlit version 1.36.0. For an older workaround using the `pages/` directory and `st.page_link`, see [Build a custom navigation menu with `st.page_link`](/develop/tutorials/multipage/st.page_link-nav).

Applied concepts
----------------

1.  Use `st.navigation` and `st.Page` to define a multipage app.
2.  Create a dynamic, role-based navigation menu.

Prerequisites
-------------

1.  This tutorial requires the following version of Streamlit:
    
    ```bash
    streamlit>=1.36.0
    ```
    
2.  You should have a clean working directory called `your-repository`.
    
3.  You should have a basic understanding of `st.navigation` and `st.Page`.
    

Build the example
-----------------

1.  Return to `streamlit_app.py` and initialize `role` in Session State.
    
    ```python
    if "role" not in st.session_state:
        st.session_state.role = None
    ```
    
2.  Define your account pages.
    
    ```python
    logout_page = st.Page(
        "logout",
        title="Log out",
        icon=":material/logout:",
        default=(role == "Requester"),
    )
    settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
    ```
    
3.  Define your request pages.
    
    ```python
    request_1 = st.Page(
        "request/request_1.py",
        title="Request 1",
        icon=":material/help:",
        default=(role == "Requester"),
    )
    request_2 = st.Page(
        "request/request_2.py",
        title="Request 2",
        icon=":material/bug_report:",
    )
    ```
    
4.  Define your remaining pages.
    
    ```python
    respond_1 = st.Page(
        "respond/respond_1.py",
        title="Respond 1",
        icon=":material/healing:",
        default=(role == "Responder"),
    )
    respond_2 = st.Page(
        "respond/respond_2.py",
        title="Respond 2",
        icon=":material/handyman:",
    )
    admin_1 = st.Page(
        "admin/admin_1.py",
        title="Admin 1",
        icon=":material/person_add:",
        default=(role == "Admin"),
    )
    admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")
    ```
    
5.  Group your pages into convenient lists.
    
    ```python
    account_pages = [logout_page, settings]
    request_pages = [request_1, request_2]
    respond_pages = [respond_1, respond_2]
    admin_pages = [admin_1, admin_2]
    ```
    
6.  Define your common elements and navigation.
    
    ```python
    st.title("Request manager")
    st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")
    
    page_dict = {}
    
    if st.session_state.role in ["Requester", "Admin"]:
        page_dict["Request"] = request_pages
    if st.session_state.role in ["Responder", "Admin"]:
        page_dict["Respond"] = respond_pages
    if st.session_state.role == "Admin":
        page_dict["Admin"] = admin_pages
    
    if len(page_dict) > 0:
        pg = st.navigation({"Account": account_pages} | page_dict)
    
    pg.run()
    ```
    
7.  Save your `streamlit_app.py` file and view your app!
    
    Try logging in, switching pages, and logging out. Try again with a different role.