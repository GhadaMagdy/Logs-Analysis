# Logs-Analysis


## Introduction

This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course.
In this, we have to execute complex queries on a large database (> 1000k rows) to extract intersting stats.

The database in question is a newspaper company database where we have 3 tables; `articles`, `authors` and `log`.
* `articles` - Contains articles posted in the newspaper so far.
* `authors` - Contains list of authors who have published their articles.
* `log` - Stores log of every request sent to the newspaper server.

This project implements a single query solution for each of the question in hand.
See [main.py](main.py) for more details.


## Running

* Make sure you have `newsdata.sql`, the SQL script file with all the data.
```sh
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```

* Then run the following command to execute it in `news` database. You might have to create the database before-hand.

```sh
psql -d news -f newsdata.sql
```

* Finally run the script.

```sh
python main.py
```

* It will present you with necessary stats.

----
