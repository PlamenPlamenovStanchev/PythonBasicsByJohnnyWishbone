target_book = input()
command = input()
book_count = 0
is_found = False
while command != "No More Books":

    current_book = command
    if current_book == target_book:
       is_found = True
       break
    book_count += 1
    command = input()
if not is_found:
    print("The book you search is not here!")
    print(f'You checked {book_count} books.')
else:
    print(f'You checked {book_count} books and found it.')