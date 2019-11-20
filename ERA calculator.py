# ERA calculator


no_decimalError = True
no_valueError = True

while no_valueError:
    try:
        _er = int(input("Enter total earned runs: \n"))
    except ValueError:
        print("Invalid entry. \nMust be a number, no letters or special characters.")

    else:
        print("You entered " + str(_er) + " total earned runs.")
        no_valueError = False

while no_decimalError:
    try:
        _ip = float(input("Enter total innings pitched: \n"))
        if round(float(_ip) - int(_ip), 2) * 10 > 2:
            raise TypeError
    except TypeError:
        print("Invalid entry. \nInnings pitched decimal must be 0, 1, or 2.\nPlease check your information and try again.")

    except ValueError:
        print("Invalid entry. \nMust be a number, no letters or special characters.")

    else:
        print("You entered " + str(_ip) + " total innings pitched.")
        no_decimalError = False

def era(_er, _ip):
    def er_per_out():
        return _er * 27

    def calc_total_outs():
        return int(_ip * 3) + round(float(_ip) - int(_ip), 2) * 10

    return(er_per_out() / (calc_total_outs()))

ERA = era(_er, _ip)

print("This player has a " + str(ERA) + " ERA!\n")
if float(ERA) > 5.0:
    print("That\'s not good, he might be looking for a new job soon.")
elif float(ERA) <= 5.0 and float(ERA) >= 3.5:
    print("Meh, an average ERA.")
elif float(ERA) <= 3.5 and float(ERA) >= 2.5:
    print("This guy is good!")
else:
    print("Wow, he might win the Cy Young award!!!")




quit()



