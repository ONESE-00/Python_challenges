def add_dots(name):
    return ".".join(name)
def remove_dots(name):
    return name.replace(".", "")
print(add_dots("onese"))
print(remove_dots('o.n.e.s.e'))
print(remove_dots(add_dots("onese")))
