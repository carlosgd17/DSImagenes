# Import the required library
from io import BytesIO
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import psycopg2


# Method to create a connection object
# It creates a pointer cursor to the database
# and returns it along with Connection object
def create_connection():
    # Connect to the database
    # using the psycopg2 adapter.
    # Pass your database name ,# username , password ,
    # hostname and port number
    conn = psycopg2.connect(dbname='myDB',
                            user='postgres',
                            password='1712253',
                            host='localhost',
                            port='5432')
    # Get the cursor object from the connection object
    curr = conn.cursor()
    return conn, curr


def create_table():
    try:
        # Get the cursor object from the connection object
        conn, curr = create_connection()
        try:
            # Fire the CREATE query
            curr.execute("CREATE TABLE IF NOT EXISTS imagen("
                         "clave INTEGER, "
                         "descripcion VARCHAR(250), "
                         "imagen BYTEA"
                         ")")
        except(Exception, psycopg2.Error) as error:
            # Print exception
            print("Error while creating cartoon table", error)
        finally:
            # Close the connection object
            conn.commit()
            conn.close()
    finally:
        # Since we do not have to do anything here we will pass
        pass


def write_blob(clave, file_path, descripcion):
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


def select_blob(clave):
    try:
        conn, cursor = create_connection()
        try:
            cursor.execute("SELECT imagen FROM imagen WHERE clave=%s", clave)
#                           "WHERE clave==%s", (clave,))
            result = cursor.fetchone()
            if result:
                image = mpimg.imread(BytesIO(result[0]))
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
        # Call the create table method
        # create_table()
        # Prepare sample data, of images, from local drive
        """
        write_blob(1, "F:\\TeachPytho\\GFGPhotos\\casper.jpg", "Casper")
        """
        write_blob(clave, file_path, descripcion)

        # drawing = open("/home/carlosgd17/Pictures/a_Pics/batman.jpg", 'rb').read()
        # print(psycopg2.Binary(drawing))
    if opcion == 2:
        clave = input("Digite la clave: ")
        select_blob(clave)
