# This is a project I submitted as an university assignment. Due to time constraints, it's far from finished and refactoring is in progress. 
import datetime


class Books(object):

    def __init__(self, book_id, book_title, book_author, book_year,
                 book_publisher, book_available_copies, book_copies, book_publication_date):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.book_publisher = book_publisher
        self.book_available_copies = int(book_available_copies)
        self.book_copies = int(book_copies)
        self.book_publication_date = book_publication_date

    def setBookID(self, book_id):
        self.book_id = book_id

    def setTitle(self, book_title):
        self.book_title = book_title

    def setAuthor(self, book_author):
        self.book_author = book_author

    def setYear(self, book_year):
        self.book_year = book_year

    def setPublisher(self, book_publisher):
        self.book_publisher = book_publisher

    def setNumAvailableCopies(self, book_available_copies):
        self.book_available_copies = book_available_copies

    def Copies(self, book_copies):
        self.book_copies = book_copies

    def setPublicationDate(self, book_publication_date):
        self.book_publication_date = book_publication_date

    def getBookID(self):
        return self.book_id

    def getTitle(self):
        return self.book_title

    def getAuthor(self):
        return self.book_author

    def getYear(self):
        return self.book_year

    def getPublisher(self):
        return self.book_publisher

    def getNumAvailableCopies(self):
        return self.book_available_copies

    def getCopies(self):
        return self.book_copies

    def getPublicationDate(self):
        return self.book_publication_date

    # Display book details
    def display_book(self):
        print(f'\nBook ID: {self.book_id}',
              f'\nBook title: {self.book_title}',
              f'\nBook author: {self.book_author}',
              f'\nPublished in: {self.book_year}',
              f'\nPublished by: {self.book_publisher}',
              f'\nAvailable copies: {self.book_available_copies}',
              f'\nTotal copies: {self.book_copies}',
              f'\nPublication date: {self.book_publication_date}')

    # Check if substrings exist in title, author, publisher and publication date
    def __contains__(self, substring):
        if substring in self.book_title:
            return True

        elif substring in self.book_author:
            return True

        elif substring in self.book_publisher:
            return True

        elif substring in self.book_publication_date:
            return True

        else:
            return False


class BookList:

    book_collection = []

    def __init__(self):
        self.book_collection = []


    def add_book(self, book: Books):
        self.book_collection.append(book)

    
    def search(self):

        while True:
            search_options = input(f' You can search by:'
                                   f'\n A) Title'
                                   f'\n B) Author'
                                   f'\n C) Publisher'
                                   f'\n D) Publication Date'
                                   f'\n Choose A, B, C or D: ')
            if search_options in ['A', 'a']:
                t_search = input('Search by title: ')
                for book in self.book_collection:
                    if book.book_title.__contains__(t_search):
                        book.display_book()
                    else:
                        print('Try again')
                break

            elif search_options in ['B', 'b']:
                a_search = input('Search by Author: ')
                for book in self.book_collection:
                    if book.book_author.__contains__(a_search):
                        book.display_book()
                    else:
                        print('Try again')
                break

            elif search_options in ['C', 'c']:
                p_search = input('Search by publisher: ')
                for book in self.book_collection:
                    if book.book_publisher.__contains__(p_search):
                        book.display_book()
                    else:
                        print('Try again')
                break

            elif search_options in ['D', 'd']:
                p_date_search = input('Search by publication date: ')
                for book in self.book_collection:
                    if book.book_publication_date.__contains__(p_date_search):
                        book.display_book()
                    else:
                        print('Try again')
                break
            else:
                print('Try again')
                continue

    # Remove book by title
    def remove_book(self):
        del_book = input('Delete book by title: ')
        for book in self.book_collection:
            if book.book_title in del_book:
                self.book_collection.remove(book)
                print(f'{book.book_title}has been removed')
            else:
                print('Try again')
        return self.book_collection

    
    def total_books(self):
        print(len(self.book_collection))
        return len(self.book_collection)

    # Check if book exists in the collection
    def getBook(self):
        found = 0
        not_found = 0
        bookDetails = None
        while True:
            request = input('Enter book title: ')
            for book in self.book_collection:
                if book.book_title == request:
                    found += 1
                    bookDetails = book
                else:
                    not_found += 1

            if found > 0:
                print('Book found')
                break
            else:
                print('Try again ')
                continue

        if found > 0:
            return bookDetails
        else:
            pass


class Users(object):

    def __init__(self, username, first_name, surname, house_number, street_name, postcode,
                 email, date_of_birth):
        self.username = username
        self.first_name = first_name
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.date_of_birth = date_of_birth

    def getUsername(self):
        return self.username

    def getFirstName(self):
        return self.first_name

    def getSurname(self):
        return self.surname

    def getHouseNumber(self):
        return self.house_number

    def getStreetName(self):
        return self.street_name

    def getPostcode(self):
        return self.postcode

    def getEmail(self):
        return self.email

    def getDateOfBirth(self):
        return self.date_of_birth

    def editFirstName(self):
        edit_fname = input('Change first name to: ')
        self.first_name = edit_fname
        print(f'New firstname is: {edit_fname}')

    def editSurname(self):
        edit_sname = input('Change surname to: ')
        self.surname = edit_sname
        print(f'New surname is: {edit_sname}')

    def editEmail(self):
        edit_email = input('Change email to: ')
        self.email = edit_email
        print(f'New email is: {self.email}')

    def editDateOfBirth(self):
        edit_dob = input('Change date of birth to: ')
        self.date_of_birth = edit_dob
        print(f'New date of birth is: {self.date_of_birth}')

    # Check if substring exists in username
    def __contains__(self, uname):
        if uname in self.username:
            return True
        else:
            return False

    # Display user details
    def display_userDetails(self):
        print(f'\n Username: {self.username}',
              f'\n First name: {self.first_name}',
              f'\n Surname: {self.surname}',
              f'\n House number: {self.house_number}',
              f'\n Street name: {self.street_name}',
              f'\n Postcode: {self.postcode}',
              f'\n Email address: {self.email}',
              f'\n Date of birth: {self.date_of_birth}')


class UserList:
    list_of_users = []

    def __init__(self):
        self.list_of_users = []

    def addUser(self, user: Users):
        self.list_of_users.append(user)

    def findDuplicate(self):
        num_duplicates = 0
        del_user = input('Enter user firstname: ')
        for name in self.list_of_users:
            if name.first_name in del_user:
                num_duplicates += 1
                print(f'\n{name.username}: {name.first_name} {name.surname}')
        print(f'\nThere are {num_duplicates} users with the same first name')
        if num_duplicates > 0:
            return True
        else:
            pass

    def removeUser(self):
        if self.findDuplicate() is True:
            del_book = input('Enter username to delete user: ')
            for user in self.list_of_users:
                if user.username in del_book:
                    self.list_of_users.remove(user)
                    print(f'{user.username} has been deleted')
                    print(self.list_of_users)

    def totalUsers(self):
        return len(self.list_of_users)

    # Prints user details by getting username as input
    def showUserDetails(self):
        found = 0
        not_found = 0
        while True:
            user_detail = input('Show user details: ')
            for user in self.list_of_users:
                if user.username == user_detail:
                    found +=1
                else:
                    not_found +=1

                if found > 0:
                    break
                else:
                    continue

            if found > 0:
                return user.display_userDetails()
            else:
                print('Invalid user')
                continue

    # Validates username exists in the list of users
    def checkUsername(self):
        found = 0
        not_found = 0
        while True:
            check_uname = input('Enter your username: ')
            for user in self.list_of_users:
                if user.username == check_uname:
                    found += 1
                else:
                    not_found += 1

            if found > 0:
                print('User found')
                break
            else:
                print('Invalid user ')
                continue

        if found > 0:
            return str(check_uname)
        else:
            pass


class Loan(object):

    def __init__(self, user_name, book_name, due_date):
        self.user_name = user_name
        self.book_name = book_name
        self.due_date = due_date


class Loans:
    loans = []

    def __init__(self):
        self.loans = []
        

    def add_loan(self, loan: Loan):
        self.loans.append(loan)

    def borrowBook(self, username, book):
        available_copies = book.getNumAvailableCopies()
        book.setNumAvailableCopies(available_copies - 1)
        loanedBook = Loan(username, book.book_title, datetime.datetime.now())
        self.loans.append(loanedBook)
        print(f'Book issued. Available copies left: {book.getNumAvailableCopies()}')

    # Counts the number of books a user has borrowed
    def booksLoaned(self, username):
        count = 0
        for item in self.loans:
            if item.user_name == username:
                count += 1
            else:
                pass
        print(count)

    # Fetches details about loan
    def getLoan(self, username, book):
        found = 0
        not_found = 0
        loanDetails = None
        for loan in self.loans:
            if (loan.user_name == username) and (loan.book_name == book.book_title):
                found += 1
                loanDetails = loan
            else:
                not_found += 1

        if found > 0:
            return loanDetails
        else:
            pass
        
    def returnBook(self, username, book):
        if len(loans.loans) == 0:
            print("No books are issued. \n")
        else:
            available_copies = book.getNumAvailableCopies()
            book.setNumAvailableCopies(available_copies + 1)
            returned_book = self.getLoan(username, book)
            self.loans.remove(returned_book)
            print(f'Book returned. Available copies left: {book.getNumAvailableCopies()}')

    def overdueBooks(self):
        overdue_books = []
        for item in self.loans:
            weeks = abs(datetime.datetime.now() - item.due_date).days / 7
            if weeks > 1:
                overdue_books.append(item)
        print(overdue_books)
        return overdue_books


# Example loans
loan1 = Loan('example1', "Man's search for meaning", datetime.datetime(2022, 8, 10))
loan2 = Loan('example2', 'Seeking wisdom: From Darwin to Munger', datetime.datetime(2022, 8, 10))

loans = Loans()
loans.add_loan(loan1)
loans.add_loan(loan2)


book1 = Books('1504234', "Man's search for meaning", 'Viktor Frankl',
              '1946', 'Verlag für Jugend und Volk (Austria)', 5, 5, '1946')
book2 = Books('1504231', 'Seeking wisdom: From Darwin to Munger', 'Peter Bevelin',
              '2003', 'Post Scriptum AB', 4, 4, '2007')
book3 = Books('1504232', 'Rich man, poor man', 'Irwin Shaw',
              '1969', '	Delacorte Press', 3, 3, '1.9.1970')
book4 = Books('1504233', 'The old man and the sea', 'Ernest Hemingway',
              '1952', 'Charles Scribner Sons', 4, 4, '1952')

user1 = Users('example1', 'Nikola', 'Ivanov', '97', 'Ul. Dyado Dobrev', '1220',
              'nikolaos.todorov@gmail.com', '12.09.1995')
user2 = Users('example2', 'Nikola', 'Marinov', '98', 'Ul. Lomsko shose', '1000',
              'nikolaos.todorov@gmail.com', '13.09.1995')
user3 = Users('example3', 'Nikola', 'Todorov', '99', 'Ul. Bulgaria', '1220',
              'nikolaos.todorov@gmail.com', '14.09.1995')
user4 = Users('example4', 'Kostadin', 'Mutafchiev', '100', 'Ul. Slivnitsa', '1000',
              'kostadin.todorov@gmail.com', '15.09.1995')
user5 = Users('example5', 'Ivan', 'Choksi', '101', 'Ul. Vitosha', '1220',
              'ivan.todorov@gmail.com', '16.09.1995')

b = BookList()
b.add_book(book1)
b.add_book(book2)
b.add_book(book3)
b.add_book(book4)

u = UserList()
u.addUser(user1)
u.addUser(user2)
u.addUser(user3)
u.addUser(user4)
u.addUser(user5)


print(f'\n--------  Welcome to the library  --------')
print(f'\n You can: '
      f'\n 1. Search for a book'
      f'\n 2. Remove a book from the collection'
      f'\n 3. Display total number of books'
      f'\n 4. Remove a user'
      f'\n 5. Display total number of users'
      f'\n 6. Show user details'
      f'\n 7. Borrow a book'
      f'\n 8. Return a book'
      f'\n 9. Display number of books borrowed by user'
      f'\n 10. See overdue books'
      f'\n 11. Exit')

while True:
    try:
        user_response = int(input("\n Enter your choice: "))

        if user_response == 1:
            b.search()
        elif user_response == 2:
            b.remove_book()
        elif user_response == 3:
            b.total_books()
        elif user_response == 4:
            u.removeUser()
        elif user_response == 5:
            u.totalUsers()
        elif user_response == 6:
            u.showUserDetails()
        elif user_response == 7:
            loans.borrowBook(u.checkUsername(), b.getBook())
        elif user_response == 8:
            loans.returnBook(u.checkUsername(), b.getBook())
        elif user_response == 9:
            loans.booksLoaned(u.checkUsername())
        elif user_response == 10:
            loans.overdueBooks()
        elif user_response == 11:
            print('Thank you')
            exit()
        else:
            print('Choose a valid option')

    except Exception:  # catch errors
        print(f" Invalid input! \n")


