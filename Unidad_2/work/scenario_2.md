# **Reporte Unidad 2** 
**Actividad en pgAdmin4. Creación de tablas**

## Normalizacion capa Bronce
Despues de importar el CSV se revisa y elimina los registros repetidos y aquellos con valores Null, en mi caso se detactaron registros reepetidos en la informacion sintetica creada, Existian Nombres y correos repetidos, solo se dejo el primer registro.

### Ejemplo de SQL para borrar duplicados

    WITH duplicates AS(
        SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY person_name, email
            ORDER BY unique_id
                created_at
            ) AS rn
    FROM bronze_layer.batch_first_load
    )
    SELECT *
    FROM duplicates
    WHERE rn > 1;

### Ejemplo de SQL para detectar titulos del nombre
Ejemplo

    SELECT
    person_name,
    REGEXP_REPLACE(person_name, '^(Lic\.|Sr\.|Dr\.)\s*', '', 'i') AS normalized_name,
    unique_id
    FROM silver_layer.batch_first_load
    WHERE person_name ~* '^(Lic\.|Sr\.|Dr\.)';

###SQL para actualizar tabla
Ejemplo

    UPDATE silver_layer.batch_first_load
    SET person_name = REGEXP_REPLACE(person_name, '^(Lic\.|Sr\.|Dr\.)\s*', '', 'i')
    WHERE person_name ~* '^(Lic\.|Sr\.|Dr\.)';


### Remover vocales acentuadas de correo
Ejemplo

    SELECT
    email,
    REGEXP_REPLACE(
        REGEXP_REPLACE(
        REGEXP_REPLACE(
            REGEXP_REPLACE(
            REGEXP_REPLACE(email, 'á', 'a', 'gi'),
            'é', 'e', 'gi'),
            'í', 'i', 'gi'),
        'ó', 'o', 'gi'),
        'ú', 'u', 'gi') AS normalized_email
    FROM silver_layer.batch_first_load
    WHERE email ~* '[áéíóú]';


## Actividad en pdAdmin4 y creacion de Tablas
Referirse al archivos PDF BigData_ProcLotes.pdf

![Carga de Datos "raw"](/Unidad_2/work/images/raw_pub.png)

![Bronze Normalizacion](/Unidad_2/work/images/Bronze_normalization.png)

![Silver Star Schema](/Unidad_2/work/images/Silver_StartSchema.png)

![Gold PII & Masking](/Unidad_2/work/images/BigData_Golden_PII_masking.png)

