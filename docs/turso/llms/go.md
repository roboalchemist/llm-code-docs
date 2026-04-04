# Source: https://docs.turso.tech/connect/go.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Turso using Go

<Steps>
  <Step title="Install">
    Add the Turso package to your Go project:

    ```bash  theme={null}
    go get github.com/tursodatabase/turso-go
    go install github.com/tursodatabase/turso-go
    ```
  </Step>

  <Step title="Connect">
    Here's how you can connect to a local SQLite database:

    ```go  theme={null}
    package main

    import (
        "database/sql"
        "fmt"
        _ "github.com/tursodatabase/turso-go"
    )

    func main() {
        conn, _ := sql.Open("turso", "sqlite.db")
        defer conn.Close()
    }
    ```
  </Step>

  <Step title="Create table">
    Create a table for users:

    ```go  theme={null}
    _, err := conn.Exec(`
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
      )
    `)
    if err != nil {
        panic(err)
    }
    ```
  </Step>

  <Step title="Insert data">
    Insert some data into the users table:

    ```go  theme={null}
    _, err = conn.Exec("INSERT INTO users (username) VALUES (?)", "alice")
    if err != nil {
        panic(err)
    }

    _, err = conn.Exec("INSERT INTO users (username) VALUES (?)", "bob")
    if err != nil {
        panic(err)
    }
    ```
  </Step>

  <Step title="Query data">
    Query all users from the table:

    ```go  theme={null}
    stmt, _ := conn.Prepare("SELECT * FROM users")
    defer stmt.Close()

    rows, _ := stmt.Query()
    for rows.Next() {
        var id int
        var username string
        _ = rows.Scan(&id, &username)
        fmt.Printf("User: ID: %d, Username: %s\n", id, username)
    }
    ```
  </Step>
</Steps>
