# Import the required library
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
            curr.execute("CREATE TABLE IF NOT EXISTS "
                         "cartoon(cartoonID INTEGER, name TEXT,"
                         "cartoonImg BYTEA)")
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


def write_blob(cartoonID, file_path, name):
    try:
        # Read data from a image file
        drawing = open(file_path, 'rb').read()
        # Read database configuration
        conn, cursor = create_connection()
        try:
            # Execute the INSERT statement
            # Convert the image data to Binary
            cursor.execute("INSERT INTO imagen "
                           "(clave, descripcion, imagen) "
                           "VALUES(%s,%s,%s)",
                           (cartoonID, name, psycopg2.Binary(drawing)))
            # Commit the changes to the database
            conn.commit()
            print("inserted")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data in cartoon table", error)
        finally:
            # Close the connection object
            conn.close()
    finally:
        # Since we do not have to do
        # anything here we will pass
        pass


def read_data(clave):
    conn, cursor = create_connection()



# Call the create table method
# create_table()
# Prepare sample data, of images, from local drive
"""
write_blob(1, "F:\\TeachPytho\\GFGPhotos\\casper.jpg", "Casper")
write_blob(2, "F:\\TeachPytho\\GFGPhotos\\archie.jpg", "Archie")
"""
# write_blob(1, "/home/carlosgd17/Pictures/a_Pics/batman.jpg", "Batman")

drawing = open("/home/carlosgd17/Pictures/a_Pics/batman.jpg", 'rb').read()
print(psycopg2.Binary(drawing))

