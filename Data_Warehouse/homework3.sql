--Creating external table
CREATE OR REPLACE EXTERNAL TABLE `affable-elf-412323.ny_taxi_rides.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://homework3-abhi/nyc_green_taxi_2022.parquet']
);

--Creating BQ table
CREATE OR REPLACE TABLE `affable-elf-412323.ny_taxi_rides.green_tripdata`
AS
SELECT * FROM `ny_taxi_rides.external_green_tripdata`;

--Question 1
SELECT count(*) FROM `affable-elf-412323.ny_taxi_rides.external_green_tripdata`
--Answer : 840 402

--Question 2
SELECT COUNT(DISTINCT PULocationID) FROM ny_taxi_rides.external_green_tripdata;
SELECT COUNT(DISTINCT PULocationID) FROM ny_taxi_rides.green_tripdata;
--Solution: 0,6.41MB

--Question 3
SELECT COUNT(*) FROM ny_taxi_rides.external_green_tripdata WHERE fare_amount =0;
--Solution : 1622

--Question 4
CREATE OR REPLACE TABLE ny_taxi_rides.green_tripdata_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM ny_taxi_rides.external_green_tripdata;

--Question 5
SELECT DISTINCT PULocationID 
FROM ny_taxi_rides.green_tripdata
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'
;
-- Bytes processed 12.82 MB

 SELECT DISTINCT PULocationID
FROM ny_taxi_rides.green_tripdata_partitoned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'
;
-- Bytes processed 1.12 MB 

--Question 6
-- GCP Bucket

--Question 7
--Yes