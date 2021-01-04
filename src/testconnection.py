import pyodbc

server = 'localhost'
database = 'mytestdatabase'
username = 'sa'
password = 'Asdf123456'
# driver='/usr/local/lib/libmsodbcsql.17.dylib'

driver='{ODBC Driver 17 for SQL Server}'

pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)