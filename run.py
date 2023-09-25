from etlalchemy.ETLAlchemySource import ETLAlchemySource
from etlalchemy.ETLAlchemyTarget import ETLAlchemyTarget

source = ETLAlchemySource("mssql+pyodbc://username:password@DSN_NAME")
target = ETLAlchemyTarget("mysql://username:password@hostname/db_name", drop_database=True)
target.addSource(source)
target.migrate()
