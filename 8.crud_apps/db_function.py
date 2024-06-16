import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c =  conn.cursor()


# Database connection
# Table
# Field / Columns
# DataType 


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT, task_due_date DATE)")

def add_data(task, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM taskstable")
    data = c.fetchall()
    return data

def view_unique_task():
    c.execute("SELECT DISTINCT task FROM taskstable")
    data = c.fetchall()
    return data

def get_task(task_id):
    c.execute("SELECT * FROM taskstable WHERE task=?",(task_id,))
    data = c.fetchall()
    return data

def update_task(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date):
    c.execute("UPDATE taskstable SET task=?,task_status=?,task_due_date=? WHERE task=? AND task_status=? AND task_due_date=?",(new_task,new_task_status,new_task_due_date,task, task_status, task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task, task_status, task_due_date):
    c.execute("DELETE FROM taskstable WHERE task=? AND task_status=? AND task_due_date=?",(task, task_status, task_due_date))
    conn.commit()
    data = c.fetchall()
    return data