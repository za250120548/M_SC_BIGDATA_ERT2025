{{ config(
    materialized='table',
    schema='trusted',
    alias='veh_telemetry',
    tags=['trusted']
) }}

WITH source_data AS (
    SELECT
        v.VIN,
        v.OEM,
        v.model_year,
        t.speed,
        t.odometer,
        t.time
    FROM {{ ref('staging_vehicles') }} v
    JOIN {{ ref('staging_telemetry') }} t
    ON v.VIN = t.VIN
)

SELECT
    *
FROM
    source_data
    