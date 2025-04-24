# # Question 1:Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.


def display_message(message):
    print('''Hello everyone! In this chapter I am  learning a variety of ways to pass information to functions.
I am also learning how to write certain functions whose primary job is to display information and 
other functions designed to process data and return a value or set of values.Finally, I am learning to how 
store functions in separate files called modules to help organize your main program files''')


display_message("good")


# quetion 2: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.


def favourite_book(Math, biology):
    print(" My favorite books is {math}and {bilogy}.")


favourite_book("calxulus", "genetics")

# # uestion 3:
# # """ T-Shirt: Write a function called make_shirt() that accepts a si
# ze and the text of a message that should be printed on the shirt.
#  The function should print a sentence summarizing the
#  size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a
# shirt. Call the function a second time using keyword arguments"""


def T_shirt(Size, message):
    print(f'the size of the T-shirt is {Size} ')
    print(f"message displayed is {message}")


T_shirt("35", "Better by far")
T_shirt(Size="35", message="Better by far")

# using return


def retur(good, bad):
    """retun full neatly"""
    do = f"{good}and {bad}"
    return do


message = ("charity", "stealing")
print(message)


def name(first, last,):
    Auwal = {"city": first, "country": last, }
    return Auwal


mmen = name("Satiago", "chile",)
print(mmen)


while True:
    user_input = input("input the artist and album name:\n")
    data_1 = "Ala" or "Kwairo"

    def make_albun(artist_name, album_title, non=""):
        info = {"artist": artist_name, "ablum": album_title, "none": non}
        if user_input == data_1:
            print("take your result")
            return info
    do = make_albun("Ala", "Jamia", "10 number of sons")
    print(do)
    if user_input == "Exit":
        print("Good bye!!!")
        break

printin_model = ["form 1", "form 2", "form 3", "fprm 4"]
current_printed = []
while printin_model:
    for printing in printin_model:  
        print(f"printin mode{printin_model}")
    completed = printin_model.pop()
    current_printed.append(completed)
    print(f'completed {current_printed}')
