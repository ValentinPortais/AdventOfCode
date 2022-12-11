#!/usr/bin/env python

elf_bag = 0
elf_inventory = open("input.txt",mode="r")
elf_glutony = { "number": 0,"calories_total": 0}
for calories in elf_inventory.read().splitlines():
    if calories:
      elf_bag = elf_bag + int(calories)
    else:
      if elf_bag > elf_glutony["calories_total"]:
        elf_glutony["calories_total"] = elf_bag
        elf_glutony["number"]+=1
      elf_bag = 0
    
print("The Elf carrying the most Calories is the number {} with a total of {} Calories".format(elf_glutony["number"],elf_glutony["calories_total"]))