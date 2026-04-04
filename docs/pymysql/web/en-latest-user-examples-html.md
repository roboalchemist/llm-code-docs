# Source: https://pymysql.readthedocs.io/en/latest/user/examples.html

Title: Examples — PyMySQL 0.7.2 documentation

URL Source: https://pymysql.readthedocs.io/en/latest/user/examples.html

Markdown Content:
CRUD[](https://pymysql.readthedocs.io/en/latest/user/examples.html#crud "Link to this heading")
------------------------------------------------------------------------------------------------

The following examples make use of a simple table

CREATE TABLE `users` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `email` varchar(255) COLLATE utf8_bin NOT NULL,
 `password` varchar(255) COLLATE utf8_bin NOT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             database='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

This example will print:

{'id': 1, 'password': 'very-secret'}
