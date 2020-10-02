#################################################################################
# Program which ask for few questions & evaluates probabilty of Covid infection #
#################################################################################

print("||SELF SCREENING COVID-19||")

name = ""
try:
    ask = input("Do you want to start your test.(yes/no)").lower()
    validOptions = ("yes" , "no")
    validOptionsMsg = "Valid options are yes/no."
    if ask not in validOptions: raise ValueError(validOptionsMsg)

    if ask == "yes":
        print("OK")

        name = str(input("enter your name..."))
        print(f"Hello {name}!")
        a = input("1 = Do you have fever above 101.4?\nکیا آپ کو تیز بخار ھے (4۔101 سے زیادہ) ؟\n(yes/no)").lower()
        if a not in validOptions: raise ValueError(validOptionsMsg)

        b = input("2 = Do you have cough - (dry cough)?\nکیا آپ کو خشک کھانسی ھے ؟\n(yes/no)").lower()
        if b not in validOptions: raise ValueError(validOptionsMsg)

        c = input("3 = Do you have Cough - (Wet Cough)?\nکیا آپ کو بلغمی کھانسی ھے ؟\n(yes/no)").lower()
        if c not in validOptions: raise ValueError(validOptionsMsg)

        d = input("4 = Do you have Shortness of Breath?\nکیا آپ کو سانس لینے میں تکلیف ہوتی ہے)\n(yes/no)").lower()
        if d not in validOptions: raise ValueError(validOptionsMsg)

        e = input("5 = Do you have Flu?\nکیا آپ کو نزلا ہے ؟\n(yes/no)").lower()
        if e not in validOptions: raise ValueError(validOptionsMsg)

        f = input("6 = Have you travelled abroad in the last 15 days?\nکیا آپ نے پچھلے 15 دنوں میں بیرون ملک سفر کیا ہے؟\n(yes/no)").lower()
        if f not in validOptions: raise ValueError(validOptionsMsg)

        g = input("7 = Have you been in contact with any person who has recently travelled internationally?\nکیا آپ کسی ایسے شخص سے رابطے میں ہیں جس نے حال ہی میں بین الاقوامی سفر کیا ہے ؟\n(yes/no)").lower()
        if g not in validOptions: raise ValueError(validOptionsMsg)

        h = input("8 = Do you have chest infection?\nکیا آپ کو سانس میں تکلیف کی بیماری ہے؟\n(yes/no)").lower()
        if h not in validOptions: raise ValueError(validOptionsMsg)

        i = input("9 = Is your age more than or equal to 60 years of age?\nکیا آپ کی عمر 60 سال سے زیادہ یا مساوی ہے؟\n(yes/no)").lower()
        if i not in validOptions: raise ValueError(validOptionsMsg)

        j = input("10 = Due to Co-morbidities, do you take any medicine?\nکیا آپ کو کوئی اور بیماری ہے جس کی وجہ سے آپ دوائی لیتے ہیں؟\n(yes/no)").lower()
        if j not in validOptions: raise ValueError(validOptionsMsg)

        permission = input("If you want to submit your test, type (submit)")
        if permission.lower() == "submit":
            print(name, "your test has been submitted!")
            if a == b == c == d == e == f == g == h == i == j == "no":
                print(name, "You are safe from COVID-19!")
            elif a == b == d == f == g == i == "yes":
                print(name, "Ooops! High Probability of Corona ! Test for Corona, Inform to Authorities \n Follow Govt Instructions\n Isolate at home")
            else:
                print(name, "Ooops! Higher probability of Corona ! Test for Corona.")
        else:
            print(name, "your test has been discarded")
    else:
        print("OK")
except Exception as e:
    print(name, f"Ooops! Invalid entry detected. {str(e)} Please try again.")
