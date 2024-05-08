import mysql.connector

class SchoolManagement:
    def __init__(self):
        self.db = self.connect_to_database()
        self.cursor = self.db.cursor()

    def connect_to_database(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="saipavan",
                password="saipavan55",
                database="school_management"
            )
            return db
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
            exit(1)

    def is_admin(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == "admin" and password == "secret_password":
            return True
        else:
            print("Invalid admin credentials.")
            return False

    def create_table(self, table_name):
        """Creates a table in the database, enforcing constraints."""
        if not self.is_admin():
            return

        columns = []
        if table_name == "student":
            columns.append("sno INT AUTO_INCREMENT PRIMARY KEY")
            columns.append("student_name VARCHAR(255) NOT NULL")
            columns.append("student_age INT NOT NULL")
            columns.append("student_sex CHAR(1) NOT NULL")
            columns.append("doj DATE NOT NULL")
            columns.append("python_mark INT")
            columns.append("sql_mark INT")
            columns.append("ds_mark INT")
            columns.append("class VARCHAR(255)")
        elif table_name == "teacher":
            columns.append("sno INT AUTO_INCREMENT PRIMARY KEY")
            columns.append("teacher_name VARCHAR(255) NOT NULL")
            columns.append("teacher_salary DECIMAL(10, 2) NOT NULL")
            columns.append("class_teacher VARCHAR(255)")
        elif table_name == "principal":
            columns.append("sno INT AUTO_INCREMENT PRIMARY KEY")
            columns.append("principal_name VARCHAR(255) NOT NULL")
            columns.append("principal_salary DECIMAL(10, 2) NOT NULL")
        elif table_name == "admin":
            columns.append("sno INT AUTO_INCREMENT PRIMARY KEY")
            columns.append("admin_name VARCHAR(255) NOT NULL")
            columns.append("admin_password VARCHAR(255) NOT NULL")
        else:
            print("Invalid table name.")
            return
        if table_name == "teacher":
            columns[3] += " DEFAULT NULL"
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.cursor.execute(query)
        self.db.commit()
        print(f"Table '{table_name}' created successfully.")

    def navigate_table(self, table_name):
        if not self.is_admin():
            return
        while True:
            print("\n1. Read")
            print("2. Update")
            print("3. Delete")
            print("4. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.read_table(table_name)
            elif choice == '2':
                self.update_table(table_name)
            elif choice == '3':
                self.delete_table(table_name)
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def read_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        specific_read = input("Do you want to read specific data (y/n)? ")
        if specific_read.lower() == 'y':
            condition = input("Enter the condition (e.g., student_name='John Doe'): ")
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        
