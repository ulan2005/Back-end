menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak':"130"})
print(menu)
menu["lagman"] = 135
print(menu)
del menu["borsh"]
print(menu)
