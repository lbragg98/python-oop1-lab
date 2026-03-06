#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self,size = size
        self.price = price

    def size(self):
        return self.size
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self.size = value
        else:
            print ("size must be in Small, Medium, or Large")
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1