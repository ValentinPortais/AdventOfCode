#!/usr/bin/env python

number = 1
elf_bag = 0
elf_inventory = open("input.txt",mode="r")
elf_ranking = [{ "number": 0,"calories_total": 0}]
for calories in elf_inventory.read().splitlines():
    if calories:
        elf_bag = elf_bag + int(calories)
    else:
        elf_ranking.append({"number":number, "calories_total":elf_bag})
        number+=1
        elf_bag = 0

elf_ranking.sort(key=lambda x: x.get('calories_total'))
total=sum([elf['calories_total'] for elf in elf_ranking[-3:]])

print("The top 3 Elves carrying the most Calories are {} \nTotal: {}".format(elf_ranking[-3:],total))