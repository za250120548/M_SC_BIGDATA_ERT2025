
  
    

  create  table "airflow"."driven_staging"."dim_veh_avg_speed__dbt_tmp"
  
  
    as
  
  (
    

WITH source_data AS (
    SELECT
        VIN,
        AVG(speed) AS avg_speed
    FROM
        "airflow"."driven_raw"."raw_batch_data"
    GROUP BY VIN
)

SELECT
    *
FROM
    source_data
  );
  