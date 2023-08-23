# Import the required library
from io import BytesIO
from matplotlib import pyplot as plt
import psycopg2
from PIL import Image


# Method to create a connection object
# It creates a pointer cursor to the database and returns it along with Connection object
def create_connection():
    # Connect to the database using the psycopg2 adapter.
    # Pass your database name, username, password, hostname and port number
    conn = psycopg2.connect(dbname='myDB', user='postgres', password='1712253',
                            host='localhost', port='5432')
    # Get the cursor object from the connection object
    curr = conn.cursor()
    return conn, curr


def INSERT(clave, file_path, descripcion):
    try:
        # Read data from a image file
        imagen = open(file_path, 'rb').read()
        # Read database configuration
        conn, cursor = create_connection()
        try:
            # Execute the INSERT statement
            # Convert the image data to Binary
            cursor.execute("INSERT INTO imagen "
                           "(clave, descripcion, imagen) "
                           "VALUES(%s,%s,%s)",
                           (clave, descripcion, psycopg2.Binary(imagen)))
            # Commit the changes to the database
            conn.commit()
            print("\n**Registro guardado**\n")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data in imagen table", error)
        finally:
            # Close the connection object
            conn.close()
    finally:
        # Since we do not have to do anything here we will pass
        pass


def SELECT(clave):
    try:
        conn, cursor = create_connection()
        try:
            cursor.execute("SELECT imagen FROM imagen WHERE clave=%s", clave)
            result = cursor.fetchone()
            if result:
                image = Image.open(BytesIO(result[0]))
                plt.imshow(image)
                plt.show()
            else:
                print("Image not found.")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while selecting data in imagen table", error)
        finally:
            conn.close()
    finally:
        pass


if __name__ == "__main__":
    print("Programa principal")
    opcion = int(input("1. Insertar\n2. Leer\nDigite la opcion: "))
    if opcion == 1:
        file_path = input("Escriba la ruta de la imagen: ")
        descripcion = input("Escriba la descripcion de la imagen: ")
        clave = input("Digite la clave de la imagen: ")
        INSERT(clave, file_path, descripcion)
    if opcion == 2:
        clave = input("Digite la clave: ")
        SELECT(clave)
