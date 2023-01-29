# Trips Challenge

The purpose of this repo, is to solve the challenged referenced by:
[Data Engineering Challenge](./app/docs/Data%20Engineering%20Challenge.pdf)

### Solved:

- [x] There must be an automated process to ingest and store the data. (Use http://127.0.0.1:8000/docs#/default/create_ingestion_create_ingestion_post)
- [x] Trips with similar origin, destination, and time of day should be grouped together. (Use http://127.0.0.1:8000/docs#/default/create_grouped_data_create_grouped_data_post)
- [x] Develop a way to obtain the weekly average number of trips for an area, defined by a
bounding box (given by coordinates) or by a region. (Use http://127.0.0.1:8000/docs#/default/get_weekly_average_number_of_trips_get_weekly_average_number_of_trips_post)
- [x] Develop a way to inform the user about the status of the data ingestion without using a
polling solution. (Used [sendgrid](https://app.sendgrid.com/guide/integrate/langs/python) for that, but unfortunatly api is returning 403, could not solve this in enough time)
- [x] The solution should be scalable to 100 million entries. It is encouraged to simplify the
data by a data model. Please add proof that the solution is scalable. (Bigquery makes it possible to scale up for hundred of millions rows and process it without doing any kind of adjustment because it's a SaaS solution. [Proof that can be scalable](https://cloud.google.com/bigquery/quotas#query_jobs)))
- [x] Use a SQL database.

### Bonus features:

- [x] Containerize your solution.
- [x] [From the two most commonly appearing regions, which is the latest datasource?](./app/docs/queries/latest_datasource.sql)
- [x] [What regions has the "cheap_mobile" datasource appeared in?](./app/docs/queries/cheap_mobile.sql)

## Architecture:

- I didn't use any IaC solution to deploy these services/tools because it was really simple doing that using interface

![Architecture](./app/docs/imgs/arch.svg "trips_challenge")

## Setup:

- Create a .env file
    ```bash
    USER_EMAIL="" 
    CSV_FILE_PATH="./path/to_docs/samples/file.csv"
    GOOGLE_APPLICATION_CREDENTIALS="./path/example.json"
    GOOGLE_CLOUD_BUCKET_NAME="jobsity"
    SENDGRID_API_KEY=''
    SENDGRID_EMAIL_SENDER=''
    ```

## Build application:

```docker
docker build . -t trips_challenge:latest
docker run -p 8000:8000 trips_challenge --host 0.0.0.0
```
> Browser: http://127.0.0.1:8000/docs#/

## Run locally:

### Requesites:
- Python >= 3.10.6

```bash
virtualenv venv
source venv/bin/activate
```
```python
pip install -r requirements.txt
```
```bash
uvicorn app.main:app
```