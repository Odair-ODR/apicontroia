import pyodbc as odbc


#"""
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'tcp:controia-server.database.windows.net'
DATA_BASE_NAME = 'DB_CONTROIA'
USER = 'SERVER-CONTROIA'
PASSWORD = '@kamenes1697'
#"""
"""
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'ODAIR\SQLEXPRESS'
DATA_BASE_NAME = 'DB_CONTROLA'
USER = 'sa'
PASSWORD = 'odr'
#"""

try:
    # Driver={ODBC Driver 18 for SQL Server};Server=tcp:controia-server.database.windows.net,1433;Database=DB_CONTROIA;Uid=SERVER-CONTROIA;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
    connection_string = f'DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATA_BASE_NAME};UID={USER};PWD={PASSWORD}'
    connection_db = odbc.connect(connection_string)
    print(connection_db)
except Exception as ex:
    print(ex)
