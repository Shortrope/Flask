def who_do_you_know():
    people = input("Enter people you know: ")
    return people.split()

def ask_user(known_people):
    person = input("Enter a name: ")
    match = False

    match = [p for p in known_people if person == p]
    print("You know: {}".format(match))

#    if person in known_people:
#        print("You know: {}".format(person))
#        match = True

    if not match:
        print("You don't know anyone!")

print(ask_user(who_do_you_know()))

