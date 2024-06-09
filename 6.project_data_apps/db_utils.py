import sqlite3

conn = sqlite3.connect("metadata.db")
c = conn.cursor()


# database management
def create_uploaded_files_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS filestable(file_name TEXT, file_type TEXT, file_size INTEGER, file_uploaded_on TEXT)"
    )
    conn.commit()


# add details
def add_file_details(file_name, file_type, file_size, file_uploaded):
    c.execute(
        "INSERT INTO filestable(file_name, file_type, file_size, file_uploaded_on) VALUES (?,?,?,?)",
        (file_name, file_type, file_size, file_uploaded),
    )
    conn.commit()


# view the details
def view_all_files():
    c.execute("SELECT * FROM filestable")
    data = c.fetchall()
    return data


def delete_all_files():
    c.execute("DELETE FROM filestable")
    conn.commit()
