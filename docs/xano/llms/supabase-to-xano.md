# Source: https://docs.xano.com/the-database/migrating-your-data/supabase-to-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Supabase To Xano

## Why migrate from Supabase to Xano?

* **Ease of Use**: Xano's visual development environment makes it accessible for users with minimal coding expertise.

* **Scalability**: Xano supports scaling as your project grows, offering flexibility for future expansions.

* **Integration Capabilities**: Xano's built-in API functionality allows for seamless integrations without having to write code.

* **Efficient Development**: The visual workflow editor in Xano accelerates the backend development process.

* **User-Friendly Interface**: Xano provides an intuitive platform that simplifies the management of applications.

## How do I migrate from Supabase to Xano?

<Frame>
  <iframe src="https://demo.arcade.software/vr2tGLrjNVnIfjlVibnC?embed" title="https://demo.arcade.software/vr2tGLrjNVnIfjlVibnC?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Create your table in Xano">
    You can export a record to CSV from Supabase and import it into Xano to create the table in just a few clicks.
  </Step>

  <Step title="Once the table is created, delete any existing records to ensure they don't conflict with the migration">
    &#x9;
  </Step>

  <Step title="Create a new API endpoint to build the migration into.">
    &#x9;
  </Step>

  <Step title="Add an External PostgreSQL Connection function">
    You can find your connection information in Supabase by clicking <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/56c88624-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=5e115c5f7bfc20344b9172a5c4e799bc" className="inline m-0" width="98" height="31" data-path="images/56c88624-image.jpeg" /> at the top of the screen.

    Make sure to use the **Session Pooler** option and retrieve the information from there.

    If you aren't sure what your database password is, you can reset it from your Supabase account settings.

    You'll also need to provide a SQL statement. In most cases, it should just be a simple SELECT statement, which retrieves all of the records from that table.

    ```sql  theme={null}
    SELECT * from table_name
    ```

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1bb9c2a7-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=bdf172863017b81759060fcb3c6960be" width="545" height="832" data-path="images/1bb9c2a7-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Add a Add Multiple Records In Bulk function">
    Point this function to the output of the previous function, and change the **Allow ID Field** option to **true**

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f1209057-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=44f2efb10065f258c5b1fae65e400a36" width="543" height="434" data-path="images/f1209057-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Run the function stack to start the migration.">
    Once complete, head to your database table in Xano and you should see your records added.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).