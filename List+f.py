
def pizza(*topping):
    print(
        f'the following pizza will be  made available {topping}')


pizza("tuwo")
pizza(
    "Awara", 
    "Teba", 
    "shinkafa",
    "kunu")


def user_profile(first, last, **info):
    user_input = input("Input yor name \n")
    user_input2= input("input your pasword\n")
    if user_input and user_input2 == '@Abubakar' and 'Abkr@3537':
        info["first_name"] = first
        info["last_name"] = last
    return info

user_infor = user_profile(
    "Abubakar", 
    "umar", 
    loctaion="kana",
    fild="Biochemistry",
    gender="Male", 
    class_of_degree = 
    "first class" )
print(user_infor)

