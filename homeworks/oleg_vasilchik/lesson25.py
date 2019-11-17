import re


def normalized(Text):
    status = any(c.isalnum() for c in Text)
    if not status:
        return ""
    if not "/" in Text:
        return Text

    will_deleted = []
    index = -1

    string = Text.split("/")
    string = list(filter(lambda x: x != "", string))
    string = list(filter(lambda y: y != ".", string))

    for i in string:
        index += 1
        if i == "..":
            will_deleted.append(index - 1)

    will_deleted.remove(-1)

    for i in reversed(will_deleted):
        string.pop(i)

    string = list(filter(lambda z: z != "..", string))
    slash = "/"

    if len(string) == 1:
        return slash + str(string[0])
    else:
        return slash.join(string)


print(normalized("Oleg"))