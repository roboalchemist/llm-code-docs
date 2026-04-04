# Source: https://planetscale.com/docs/vitess/tutorials/connect-go-app.md

# Connect a Go application to PlanetScale

export const VimeoEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://player.vimeo.com/video/${id}?dnt=true`} title={title} className="aspect-video w-full" allow="autoplay; fullscreen; picture-in-picture" />
    </Frame>;
};

<VimeoEmbed id="759188218" title="Connect to PlanetScale with Go" />

## Introduction

In this guide, you’ll learn how to connect to a PlanetScale MySQL database with Go by exploring a sample API built using the Gin routing framework.

**Prerequisites:**

* [Go](https://go.dev/doc/install)
* [A PlanetScale account](https://auth.planetscale.com/sign-up)
* [VS Code](https://code.visualstudio.com/download) (optional)
* The [VS Code Rest Client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) (optional)

<Tip>
  Already have a Go application and just want to connect to PlanetScale? Check out the [Go quick connect repo](https://github.com/planetscale/connection-examples/tree/main/go).
</Tip>

## Create the database

Start in PlanetScale by creating a new database. From the dashboard, click "**New Database**", then "**Create new database**". Name the database `products_db`, select the desired [Plan type](/docs/planetscale-plans), and click "**Create database**".

By default, web console access to production branches is disabled to prevent accidental deletion. From your database's dashboard page, click on the "**Settings**" tab, check the box labelled "**Allow web console access to production branches**", and click "**Save database settings**".

Then, click on the **"Console"** tab, then "**Connect**".

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e929a8164f551599c3e017eaa84822a2" alt="The Console tab" data-og-width="1529" width="1529" data-og-height="1108" height="1108" data-path="docs/images/assets/docs/tutorials/connect-go-app/console-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d5a32e5945bfb91095bd6efb432f2885 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5d752f103cb8719e90ca64917dad9d07 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=b1d6e198141a4ee71403472eaed9ec29 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ceeb905aad3b2a1dd0c86911ecabed84 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0e417a25b629e3b588b5eda5ef045e3e 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/console-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8e57adb68a39cb5e8656a548e9131152 2500w" />
</Frame>

Run the following two commands to create a sample table and insert some data:

```sql  theme={null}
CREATE TABLE `products` (
	`id` int PRIMARY KEY AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`price` int NOT NULL
);

INSERT INTO `products` (name, price) VALUES
  ('Cyberfreak 2076', 40),
  ('Destination 2: Shining Decline', 20),
  ('Edge Properties 3', 15);
```

Finally, head to the **"Dashboard"** tab and click **"Connect"**.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=53c1edb9e16bac9c8119103690844757" alt="The location of the Connect button" data-og-width="1598" width="1598" data-og-height="806" height="806" data-path="docs/images/assets/docs/tutorials/connect-go-app/connect-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=db431b276de850eee09743d33005c5ca 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f0941b0b42cd57c7bb26884cc5a42bd5 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=808691765296267e54988ad0dc44555b 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f5ec8b34d6726a3e0cedfb402ff9193b 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c979d16c8cc363ea2d789478ea934125 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/connect-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3a7ddec18decaf35febd384199dbba96 2500w" />
</Frame>

On the following page, click **"Create password"** to generate a new password for your database. Then click **Go** in the **Select your language or framework** section, and copy the contents of the `.env` file. You'll need it for the next section.

## Run the demo project

Start by opening a terminal on your workstation and clone the sample repository provided.

```bash  theme={null}
git clone https://github.com/planetscale/golang-example-gin.git
```

Open the project in VS Code and add a new file in the root of the project named `.env`, Populate the file with the contents taken from the Connect modal in the previous section.

```sql  theme={null}
DSN=****************:************@tcp(us-east.connect.psdb.cloud)/products_db?tls=true&interpolateParams=true
```

Now open an integrated terminal in VS Code and run the project using the following commands:

```bash  theme={null}
go mod tidy
go run .
```

The terminal should update with the following output.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f66347a6a0754688762e69a9ffcc229b" alt="The output of the GET test" data-og-width="3140" width="3140" data-og-height="1322" height="1322" data-path="docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9b8d8a2b4423b2d0e642ef372ecc682e 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=63c6d8ecf725017eac32667b4df60d5f 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3c07de26b2faff0d0dc7c2b4c235027f 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6fc1d6918f14bb4e91ee9f12d79a2c44 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d092e57eb20014556af4ad0e26e76449 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9f74af27aecbd69b5832266383eaf2cf 2500w" />
</Frame>

## Exploring the code

Now that the project is running, let’s explore the code to see how everything works. All of the code is stored in `main.go`, with each of the core SQL operations mapped by HTTP method in the `main` function:

| HTTP Method Name | Query Type |
| :--------------- | :--------- |
| get              | SELECT     |
| post             | INSERT     |
| put              | UPDATE     |
| delete           | DELETE     |

```go  theme={null}
func main() {
	// Load in the `.env` file
	err := godotenv.Load()
	if err != nil {
		log.Fatal("failed to load env", err)
	}

	// Open a connection to the database
	db, err = sql.Open("mysql", os.Getenv("DSN"))
	if err != nil {
		log.Fatal("failed to open db connection", err)
	}

	// Build router & define routes
	router := gin.Default()
	router.GET("/products", GetProducts)
	router.GET("/products/:productId", GetSingleProduct)
	router.POST("/products", CreateProduct)
	router.PUT("/products/:productId", UpdateProduct)
	router.DELETE("/products/:productId", DeleteProduct)

	// Run the router
	router.Run()
}
```

Open the `tests.http` file, which contains HTTP requests that can be sent to test the API. Running the `get {{hostname}}/products` test is the equivalent of running `SELECT * FROM products` in SQL and returning the results as JSON.

<Warning>
  If you do not wish to use VS Code with the Rest Client plugin, you may use `tests.http` as a reference for your preferred IDE and API testing software.
</Warning>

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f66347a6a0754688762e69a9ffcc229b" alt="The terminal output of the go run command" data-og-width="3140" width="3140" data-og-height="1322" height="1322" data-path="docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9b8d8a2b4423b2d0e642ef372ecc682e 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=63c6d8ecf725017eac32667b4df60d5f 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3c07de26b2faff0d0dc7c2b4c235027f 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6fc1d6918f14bb4e91ee9f12d79a2c44 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d092e57eb20014556af4ad0e26e76449 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-app/go-run-output.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9f74af27aecbd69b5832266383eaf2cf 2500w" />
</Frame>

This is the `GetProducts` function defined in `main.go`. Notice how the `query` variable is the `SELECT` statement, which is passed into `db.Query` before being scanned into a slice of `Product` structs.

```go expandable theme={null}
func GetProducts(c *gin.Context) {
	query := "SELECT * FROM products"
	res, err := db.Query(query)
	defer res.Close()
	if err != nil {
		log.Fatal("(GetProducts) db.Query", err)
	}

	products := []Product{}
	for res.Next() {
		var product Product
		err := res.Scan(&product.Id, &product.Name, &product.Price)
		if err != nil {
			log.Fatal("(GetProducts) res.Scan", err)
		}
		products = append(products, product)
	}

	c.JSON(http.StatusOK, products)
}
```

To pass parameters into queries, you may use a `?` as a placeholder for the parameter. For example, `GetSingleProduct` uses a query with a `WHERE` clause that is passed into the `db.QueryRow` function along with the query string.

```go expandable theme={null}
func GetSingleProduct(c *gin.Context) {
	productId := c.Param("productId")
	productId = strings.ReplaceAll(productId, "/", "")
	productIdInt, err := strconv.Atoi(productId)
	if err != nil {
		log.Fatal("(GetSingleProduct) strconv.Atoi", err)
	}

	var product Product
	// `?` is a placeholder for the parameter
	query := `SELECT * FROM products WHERE id = ?`
	// `productIdInt` is passed in with the query
	err = db.QueryRow(query, productIdInt).Scan(&product.Id, &product.Name, &product.Price)
	if err != nil {
		log.Fatal("(GetSingleProduct) db.Exec", err)
	}

	c.JSON(http.StatusOK, product)
}
```

Parameters in queries are populated in the order they are passed into the respective `db` function, as demonstrated in `CreateProduct`.

```go expandable theme={null}
func CreateProduct(c *gin.Context) {
	var newProduct Product
	err := c.BindJSON(&newProduct)
	if err != nil {
		log.Fatal("(CreateProduct) c.BindJSON", err)
	}

	// This query has multiple `?` parameter placeholders
	query := `INSERT INTO products (name, price) VALUES (?, ?)`
	// The `Exec` function takes in a query, as well as the values for
	//     the parameters in the order they are defined
	res, err := db.Exec(query, newProduct.Name, newProduct.Price)
	if err != nil {
		log.Fatal("(CreateProduct) db.Exec", err)
	}
	newProduct.Id, err = res.LastInsertId()
	if err != nil {
		log.Fatal("(CreateProduct) res.LastInsertId", err)
	}

	c.JSON(http.StatusOK, newProduct)
}
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt