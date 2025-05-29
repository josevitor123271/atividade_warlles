import mysql.connector as mysql

# Create a connection with mysql database
connection = mysql.connect(host="localhost", user="root", password="jociluna2003", database="clinica_revisao_tarde");
cursor = connection.cursor()

# Execute operation
cursor.execute("call listar_consultas_paciente(4)")
result_database = cursor.fetchall()

# Close connection
connection.close()

# print(result_database[0]) # Return the first tuple
print(result_database) # Return all tuples
