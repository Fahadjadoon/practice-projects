from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace with your MySQL credentials
username = "root"
host = "localhost"
database = "LMS_Database"

# Create the database connection string
connection_string = f"mysql+pymysql://{username}@{host}/{database}"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connected to the database successfully!")
except Exception as e:
    print("Error connecting to the database:", e)

#Base Class
Base = declarative_base()

#Session maker
Session = sessionmaker(bind=engine)
session = Session()

# Book Model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    copies = Column(Integer, default=1)

# Member Model
class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    roll_no = Column(String(50), unique=True, nullable=False)
    membership_status = Column(String(50), default="Active")

#Library Class
class Library:

# Initialize database tables
    Base.metadata.create_all(engine)
    
    # Insert initial data into the database
    if not session.query(Book).first() and not session.query(Member).first():
        initial_books = [
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 4},
            {"title": "1984", "author": "George Orwell", "copies": 5},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "copies": 3},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2},
            {"title": "Moby Dick", "author": "Herman Melville", "copies": 1},
    ]
        initial_members = [
            {"name": "john", "roll_no": "0001", "membership_status": "Active"},
            {"name": "emily", "roll_no": "0002", "membership_status": "Inactive"},
            {"name": "michael", "roll_no": "0003", "membership_status": "Active"},
            {"name": "sophia", "roll_no": "0004", "membership_status": "Active"},
    ]
    
#double astarik ** here will unpack the dictionary
#like this Book(title="To Kill a Mockingbird", author="Harper Lee", copies=4)

    for book in initial_books:
        session.add(Book(**book))
    for member in initial_members:
        session.add(Member(**member))
    session.commit()
    print("Initial data inserted.")

    # Show Books Method
    @staticmethod
    def show_books():
        books = session.query(Book).all()
        for book in books:
            print(f"{book.id}. {book.title} by {book.author}, Copies: {book.copies}")

    # This method will add new book
    @staticmethod
    def add_new_book(title, author, copies):
        new_book = Book(title=title, author=author, copies=copies)
        session.add(new_book)
        session.commit()
        print(f"Book '{title}' added successfully.")

    @staticmethod
    def remove_book(book_id):
        book = session.query(Book).filter(Book.id == book_id).first()
        if book:
            session.delete(book)
            session.commit()
            print(f"Book '{book.title}' removed successfully.")
        else:
            print("Book not found.")

    @staticmethod
    def show_members():
        members = session.query(Member).all()
        for member in members:
            print(f"Name: {member.name}, Roll-no: {member.roll_no}, Membership: {member.membership_status}")
            print("----------------------------------------------")

    @staticmethod
    def add_new_member(name, roll_no):
        new_member = Member(name=name, roll_no=roll_no)
        session.add(new_member)
        session.commit()
        print(f"Member '{name}' added successfully.")

    @staticmethod
    def remove_member(roll_no):
        member = session.query(Member).filter(Member.roll_no == roll_no).first()
        if member:
            session.delete(member)
            session.commit()
            print(f"Member '{member.name}' removed successfully.")
        else:
            print("Member not found.")


library = Library()

while True:
    print("1. Manage Books")
    print("2. Manage Members")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\n1. Show books")
            print("2. Add a new book")
            print("3. Remove a book")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                library.show_books()
            elif choice == '2':
                title = input('Insert book title: ')
                author = input('Insert author\'s name: ')
                copies = int(input('Insert number of copies: '))
                library.add_new_book(title, author, copies)
            elif choice == '3':
                book_id = int(input('Insert book ID to remove the book: '))
                library.remove_book(book_id)
            elif choice == '4':
                break
            else:
                print("Invalid choice, please select again.")

    elif choice == '2':
        while True:
            print("\n1. Show Members")
            print("2. Add a new Member")
            print("3. Remove a Member")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                library.show_members()
            elif choice == '2':
                name = input("Enter Name: ")
                roll_no = input("Enter Roll-no: ")
                library.add_new_member(name, roll_no)
            elif choice == '3':
                roll_no = input("Insert member's roll-no to remove: ")
                library.remove_member(roll_no)
            elif choice == '4':
                break
            else:
                print("Invalid choice, please select again.")

    elif choice == '3':
        print("Exit")
        break