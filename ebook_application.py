# =====Note======
'''
This is the backend code of the ebook main front end.
The front end part underlying code is in ebook_main_front

'''

# ===Task description ========

'''
For this task we build an ebook store
User menu will interact with our database of bookstore

'''
# importing needed packages
import sqlite3
from tabulate import tabulate

# setting up a database
db = sqlite3.connect('database')

"""
# creating a cursor
cursor = db.cursor()


# creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_database(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)

'''
)

db.commit()


"""
"""
#adding books 
sql_insert = "INSERT INTO book_database(id, Title, Author, Qty) VALUES (?,?,?,?)"

values = [
        (3001,'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, "Harry Potter and the Philosopher's Stone", 'J.K Rowling', 40),
        (3003, 'The Lion, The Witch and the Wardrobe', 'C.S Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
        ]

cursor = db.cursor()
cursor.executemany(sql_insert,values)
db.commit()
"""

# Define a function to view all
def view_all():
    db = sqlite3.connect('database')
    cursor = db.cursor()
    sq = "SELECT * FROM book_database;"
    books = cursor.execute(sq)
    print(f"id\t ||Title \t\t\t||Author\t||Quantity")
    print("===============================================================")
    for row in books:
        
        print(f"{row[0]}\t{row[1]} || {row[2]} || {row[3]}")
    
    # commit our command
    db.commit()

    # close our connection
    db.close()
    
    
# view_all()

def add_one():
    db = sqlite3.connect('database')
    cursor = db.cursor()

    # Get user input
    book_ID = int(input("Please enter the book id: "))
    book_title = input("Please enter the title book: ")
    book_author = input("Please add the name of the author: ")
    book_quantity = int(input("Please add the number of books: "))

    # Adding the book to the the database
    cursor.execute("INSERT INTO book_database (id, Title, Author, Qty) VALUES (?,?,?,?)", 
                    (str(book_ID),book_title,book_author,str(book_quantity)))
    print("\nBook successfully added\n")

    # commit our command
    db.commit()

    # close our connection
    db.close()

#Testing
#add_one()
#view_all()

def update_book():
    db = sqlite3.connect('database')
    cursor = db.cursor()
    # print("In progress")

    # Entering the id of the book info to update
    user_choice = int(input("Please input the id of the book you want to update: "))

    # select the book and ask user 
    sql_query = f"SELECT * FROM book_database WHERE id = {str(user_choice)};"
    book_to_update = cursor.execute(sql_query)
    print(book_to_update.fetchone())

    # Ask the user what s/he would like to update
    menu_update = input("""
Please select what you would like to update:
1 - For title
2 - To update the author
3 - To update quantity
4 - To return to the menu   
    
""")
    # Conditionning and update the database
    if menu_update == '1':
        new_title = input("Please add the new title:  ").title()
        sql_query_update = f"""
        UPDATE book_database
        SET Title = ?
        WHERE id = {(user_choice)};
        """
        cursor.execute(sql_query_update,(new_title,))
        print("Title successfully updated.")
    
    elif menu_update =='2':
        new_author = input("Please add the correct author:  ").title()
        sql_update_author = f"""
        UPDATE book_database
        SET Author = ?
        WHERE id = {(user_choice)};
        """
        cursor.execute(sql_update_author,(new_author,))
        print("Author name successfully updated.\n")
    
    elif menu_update =='3':
        new_quantity = int(input("Please add the correct quantity:  "))
        sql_update_qty = f"""
        UPDATE book_database
        SET Qty = ?
        WHERE id = {(user_choice)};
        """
        cursor.execute(sql_update_qty,(new_quantity,))
        print("Quantity successfully updated.\n")

    elif menu_update =='4':
        main_menu()

    else:
        print("Incorrect option")
        main_menu()

    # commit our command
    db.commit()

    # close our connection
    db.close()


def delete_book():
    db = sqlite3.connect('database')
    cursor = db.cursor()

    # Adding book id to delete
    book_ID = int(input("Please enter the id of the book to delete: "))

    # sql query to delete the row
    sql_delete = """DELETE FROM book_database
                WHERE id = ?;"""
    
    # calling sql query
    cursor.execute(sql_delete,(book_ID,))

    print(f"\nThe book with {book_ID} successfully deleted from the table.\n")

    # commit our command
    db.commit()

    # close our connection
    db.close()



def search():
    db = sqlite3.connect('database')
    cursor = db.cursor()
    user_search = input("Please search by keyword or id: ").lower()
    sq = f"""SELECT * FROM book_database
        WHERE Title LIKE '%{str(user_search)}%' OR 
        Author LIKE '%{str(user_search)}%' OR
        id LIKE '%{str(user_search)}%';"""
    
    # Running the query
    search_query = cursor.execute(sq)
    results = search_query.fetchall()
    
    if len(results) >= 1:
        print("\nBelow are the books that match your search")
        print("==========================================")
        for book in results:
            print(f"{book[0]}\t{book[1]} || {book[2]} || {book[3]}")
    else:
        print("We could not match your search.")

    # commit our command
    db.commit()

    # close our connection
    db.close()



# Defining menue
def main_menu():
    while True:
        menu = input("""
Please select below what you would like to do:
A - To add a book
B - To update a book
C - To search based on keyword
D - To delete book
V - To view available books
E - Exit
        
        """).title()
        if menu == 'A':
            add_one()
        
        elif menu =='B':
            update_book()
        
        elif menu =='C':
            search()
        
        elif menu =='D':
            delete_book()
        
        elif menu =='E':
            exit()
        
        elif menu == 'V':
            view_all()
        
        else:
            print("Invalid option; please try again.")
            main_menu()

            break

