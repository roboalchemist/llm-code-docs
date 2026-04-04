# Source: https://planetscale.com/docs/vitess/tutorials/planetscale-serverless-driver.md

# PlanetScale serverless driver for JavaScript

## Why use the PlanetScale serverless driver

Before learning how to use the PlanetScale serverless driver for JavaScript, it’s worth understanding why you should use this over other MySQL packages available in the directory. Some serverless and edge function hosts do not permit arbitrary outbound TCP connections, which is how many MySQL clients operate.

Using the PlanetScale serverless driver for JavaScript provides a means of accessing your database and executing queries over an HTTP connection, which is generally not blocked by cloud providers. If you encounter issues using MySQL packages with PlanetScale, use the serverless driver instead.

<Note>
  Be sure to check out our [F1 Championship Stats demo application](https://github.com/planetscale/f1-championship-stats) to find examples for use with Cloudflare Workers, Vercel Edge Functions, and Netlify Edge Functions.
</Note>

## Add and use the PlanetScale serverless driver for JavaScript to your project

To install the package in your project, run the following install command:

```bash  theme={null}
npm install @planetscale/database
```

### Connect to the database

The first step to using the PlanetScale serverless driver for JavaScript is to connect to your database.

You can get your connection string in the PlanetScale dashboard by clicking on your database, clicking "**Connect**", and selecting `database-js` from the "Select your language or framework" section.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=90c1d10b58839a8ae02f43ea55a4cec1" alt="Database-js selection priority" data-og-width="3512" width="3512" data-og-height="1632" height="1632" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ac68aacadd62607e3e6a2b327029527c 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5b57ec3a6d666ef6c43388464d2fd061 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=58bd08177ed713cedcc761f99b34a595 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a4b54aa055fe7442c9b3be9850f706d7 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7d181469927efbc41ece4368c33ebe01 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver/connect-serverless-credentials-database-js.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=2df54bdf74427117e4c266aedb62ef51 2500w" />
</Frame>

Scroll down to the env variables. You'll need this to connect to your database.

Use the `connect` function to create the connection and return it to an object.

```js  theme={null}
const config = {
  host: 'aws.connect.psdb.cloud',
  username: '<PS_USERNAME>',
  password: '<PS_PASSWORD>'
}
const conn = await connect(config)
```

### Executing queries

To execute a query, use the `execute` function of the connection object, with the query passed as the first parameter.

```js  theme={null}
const results = await conn.execute('SELECT * FROM hotels')
```

Here is the content of the `results` object from the `SELECT` statement:

```js expandable theme={null}
{
  headers: [ 'id', 'name', 'address', 'stars' ],
  types: {
    id: 'UINT32',
    name: 'VARCHAR',
    address: 'VARCHAR',
    stars: 'FLOAT32'
  },
  rows: [
    {
      id: 1,
      name: 'Four Seasons Resort Jackson hole',
      address: '7680 Granite Loop Rd, Teton Village, WY 83025',
      stars: 4.7
    },
    {
      id: 2,
      name: 'The Galt House',
      address: '140 N Fourth St, Louisville, KY 40202',
      stars: 4
    },
    // ...results removed for brevity
  ],
  rowsAffected: null,
  insertId: null,
  error: null,
  size: 5,
  statement: 'SELECT * FROM hotels',
  time: 136
}
```

For parameterized queries, there are two ways in which to pass data to the query. The first is by the order in which they appear in the query. The first step is to add a `?` in the specific locations you want the parameters passed into.

```js  theme={null}
const query = 'INSERT INTO hotels (`name`, `address`, `stars`) VALUES (?, ?, ?)'
```

Then you can pass your parameters as an array of values. The driver package will replace the `?` entries in the query with the values passed in the array, in the order in which they were placed.

```js  theme={null}
const params = ['The Galt House', '140 N Fourth St, Louisville, KY 40202', 4.2]
const results = await conn.execute(query, params)
```

Here is the content of the `results` object for the `INSERT` statement:

```js  theme={null}
{
  headers: [],
  types: {},
  rows: [],
  rowsAffected: 1,
  insertId: '6',
  error: null,
  size: 0,
  statement: "INSERT INTO hotels (`name`, `address`, `stars`) VALUES ('Montage Kapalua Bay 2', '1 Bay Dr, Lahaina, HI 96761', 4)",
  time: 102
}
```

Alternately, you can name your parameters using the `:param_name` format.

```js  theme={null}
const query = 'INSERT INTO hotels (`name`, `address`, `stars`) VALUES (:name, :address, :stars)'
const params = {
  name: 'The Galt House',
  address: '140 N Fourth St, Louisville, KY 40202',
  stars: 4.2
}
const results = await conn.execute(query, params)
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt