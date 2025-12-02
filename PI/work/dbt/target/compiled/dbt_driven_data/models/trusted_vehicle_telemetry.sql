

WITH source_data AS (
    SELECT
        v.VIN,
        v.OEM,
        v.model_year,
        t.speed,
        t.odometer,
        t.time
    FROM "airflow"."driven_staging"."dim_vehicles" v
    JOIN "airflow"."driven_staging"."dim_telemetry" t
    ON v.VIN = t.VIN
)

SELECT
    *
FROM
    source_data