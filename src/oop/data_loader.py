from abc import ABC, abstractmethod
import pandas as pd
from sqlalchemy import create_engine


# Database Configuration
class DatabaseConfig:
    def __init__(self, host: str, port: int, db_name: str, user: str, password: str):
        self.host = host
        self.port = port
        self._user = user  #Encapsulation
        self.__password = password #Private attribute(name mangled)
        self.db_name = db_name

    def get_connection_url(self):
        return f"postgresql+psycopg://{self._user}:{self.__password}@{self.host}:{self.port}/{self.db_name}"


# Pipeline
class SupermarketPipeline(ABC):
    def __init__(self, filepath: str, source_name: str, db_config: DatabaseConfig):
        self.filepath = filepath
        self.source_name = source_name
        self.__db_config = db_config  #private attribute
        self.df = None

    @abstractmethod
    def extract(self):
        pass

    def transform(self):
        print(f"[{self.source_name}] Transforming data...")
        for col in ["retailer", "category", "product_name", "pack_size", "price_kes", "date_collected"]:
            self.df[col] = self.df[col].astype(str).str.strip()

        self.df["pipeline_source"] = self.source_name

    def load(self):
        print(f"[(self.source_name)] Connecting to Postgres and loading {len(self.df)} records...")

        try:
            connection_url = self.__db_config.get_connection_url()
            engine = create_engine(connection_url)

            self.df.to_sql(
                name = "Supermarket_prices",
                con = engine,
                if_exists = 'append',
                index = False
            )

            print(f"[{self.source_name}] Successfully committed records to PostgreSQL")

        except Exception as e:
            print("Database Error!")
            print(f"Error details: {e}")
            raise

    def run(self):
        print(f"Starting Pipeline {self.source_name}")
        self.extract()
        self.transform()
        self.load()

# Pipelines
# CSV Pipeline
class CSVPipeline(SupermarketPipeline):
    def extract(self):
            print(f"[{self.source_name}] ExtractingCSV from {self.filepath}")
            self.df = pd.read_csv(self.filepath)


# JSON Pipeline
class JSONPipeline(SupermarketPipeline):
    def extract(self):
        print(f"[{self.source_name}] Extracting JSON from {self.filepath}")
        self.df = pd.read_json(self.filepath)

# Creating objects
prod_db_config = DatabaseConfig(
    "127.0.0.1",
     5432,
    "postgres",
    "postgres",
    "4963"
)
# csv_pipeline = CSVPipeline(filepath=)
# json_pipeline = JSONPipeline()

pipelines = [
    CSVPipeline(r"D:\OOP\data\kenya_supermarket_prices.csv", "Naivas", prod_db_config),
    JSONPipeline(r"D:\OOP\data\kenya_supermarket_prices.json", "Carrefour", prod_db_config)

]


for pipeline in pipelines:
    pipeline.run()





# supermarket1 = SupermarketPipeline("MyDrive","Quickmart","asdfghjk")

