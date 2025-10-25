import random
import csv
import logging
import uuid
import polars as pl

from faker import Faker
from datetime import date, datetime, timedelta

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

headers = [
    "person_name", "user_name", "email", "personal_number", "birth_date", "address",
    "phone", "mac_address", "ip_address", "iban", "accessed_at",
    "session_duration", "download_speed", "upload_speed", "consumed_traffic"
]

def create_data(locale: str) -> Faker:
    """Crea una instancia de Faker con la configuración regional especificada."""
    logging.info(f"Creating synthetic data with locale: {locale.split('_')[-1]} country code.")
    return Faker(locale)

def generate_record(fake: Faker) -> list:
    # Generar datos personales aleatorios.
    person_name = fake.name()
    user_name = person_name.replace(" ", "").lower()
    email = f"{user_name}@{fake.free_email_domain()}"
    personal_number = fake.ssn()
    birth_date = fake.date_of_birth()
    address = fake.address().replace("\n", ", ")
    phone_number = fake.phone_number()
    mac_address = fake.mac_address()
    ip_address = fake.ipv4()
    iban = fake.iban()
    accessed_at = fake.date_time_between("-1y")
    session_duration = random.randint(0, 36_000)
    download_speed = random.randint(0, 1_000)
    upload_speed = random.randint(0, 800)
    consumed_traffic = random.randint(0, 2_000_000)

    return [
        person_name, user_name, email, personal_number, birth_date,
        address, phone_number, mac_address, ip_address, iban, accessed_at,
        session_duration, download_speed, upload_speed, consumed_traffic
    ]

def write_to_csv(file_path: str, rows: int, locale: str)-> None:
    fake = create_data(locale)
    logging.info(f"Faker locale set to: {locale}")
    print(f"Generating {rows} records...")
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for _ in range(rows):
            writer.writerow(generate_record(fake))
    logging.info(f"Written {rows} records to the CSV file.")


def add_id(file_name) -> None:
    """
    Add a unique UUID to each row of a CSV file.
    Args:
        file_name (str): Path to the CSV file to process.
    """
    df = pl.read_csv(file_name)
    uuid_list = [str(uuid.uuid4()) for _ in range(df.height)]
    df = df.with_columns(pl.Series("unique_id", uuid_list))
    df.write_csv(file_name)
    logging.info("Added UUID to the dataset.")


def update_datetime(file_name: str, run: str) -> None:
    if run == "next":
        current_time = datetime.now().replace(microsecond=0)
        yesterday_time = str(current_time - timedelta(days=1))
        df = pl.read_csv(file_name)
        df = df.with_columns(pl.lit(yesterday_time).alias("accessed_at"))
        df.write_csv(file_name)
        logging.info("Updated accessed timestamp.")
    

if __name__ == "__main__":
    # Configuración inicial
    logging.info(f"Started batch processing for {date.today()}.")
    locale = "es_MX"
    output_file =  f"./data/batch_{date.today()}.csv"
    #output_file =  f"./data/batch_2025-09-24.csv"
    
    if str(date.today()) == "2025-09-24":
        records = random.randint(300_372, 300_372)
        run_type = "first"
    else:
        records = random.randint(1, 1_101)
        run_type = "next"
    
    #run_type = "first"
    #records = random.randint(300_372, 300_372)

    write_to_csv(output_file, records, locale)

    add_id(output_file)

    update_datetime(output_file, run_type)

# Configuración