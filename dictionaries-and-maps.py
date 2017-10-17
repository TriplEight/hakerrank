#!/bin/python3

n = int(input())

phone_book = {}

for i in range(0, n):
    contact = str(input()).split(' ')
    name = contact[0]
    phone = int(contact[1])
    phone_book[name] = phone

for j in range(0, n):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
