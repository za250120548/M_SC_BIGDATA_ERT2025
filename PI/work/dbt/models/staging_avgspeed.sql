{{ config(
    materialized='table',
    schema='staging',
    alias='dim_veh_avg_speed',
    tags=['staging']
) }}

WITH source_data AS (
    SELECT
        VIN,
        AVG(speed) AS avg_speed
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
    GROUP BY VIN
)

SELECT
    *
FROM
    source_data
    