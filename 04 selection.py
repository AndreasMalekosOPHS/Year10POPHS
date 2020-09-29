#SELECTION

#selection uses if/elif and else
#things people get wrong are
#1.forgetting the colon:
#2.forgetting indentation
#3.not understanding comparison operators ==

skycolour = "blue"

if skycolour == ("blue"):
    print("the sky is blue today")

print("good bye!")

baby = input("Has the baby been born yet? y or n?")

if baby == ("y"):
    print("congratulations")
else:
        print("call us when you have the news")

food = "kebab"

if food == "kebab":
    print("ummmmmm, my favourite")
    print("I feel like saying it 100 times...")
    print(100*(food + "!"))
else:
        print("i'm hungry")
