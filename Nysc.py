while True:
    nysc_data_base = {"Name:"  "Adam", "Batch:"  " C2 "  "state:" "kano"}
    Nysc_data_base_2 = {"Name:" "Sani", "Batch:" "A1", "state:" "Jigawa"}
    user_input = input("input yor name \n")
    if user_input == "Adam":
        print(nysc_data_base)
    elif user_input == "Sani":
        print(Nysc_data_base_2)
    if user_input == "exit":
        print("Good bye!!")
        break
