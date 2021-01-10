import string

Message = "Hello, {}"

print( Message.format("name") )

print( "This is a {} message".format("blank"))

FancyString = "This is a {name} string. It has no real {exp}. But {name} sounds cool."

print(FancyString.format(name = "BigBrain", exp = "Meaning" ))

template = string.Template("${artist} was seen ${action} in ${year}")

Dictionary = [
    dict(artist = "Joe Van Doe", action = "fleeing from a crime scene", year = "1457"),
    dict(artist = "Billy Dole", action = "robbing a bank", year = 1898),
    dict(artist = "Jhon Cena", action = "nowhere after his first you can't see me move", year = "1410")   
]

for i in Dictionary:
    print(template.substitute(i))