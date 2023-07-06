for the start postgres db in docker:
` docker run --name <container_name> -e POSTGRES_USER=<username> -e POSTGRES_PASSWORD=<yourpassword> -e POSTGRES_DB=<db_name> -p 5432:5432 -d postgres
`