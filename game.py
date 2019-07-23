# -*- coding: utf-8 -*-
import os
import time as wkt

class game:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print("[ " + self.name + " Attack -> " + lawan.name + " ]")
        lawan.defense(self, self.attack)

    def defense(self, lawan, attack_lawan):
        armor_gw = attack_lawan / self.armor
        print("< Di Serang > : " + lawan.name)
        self.health -= armor_gw
        print("< Armor > : " + str(self.armor))
        print("< Health > : " + str(self.health) + "\n")

    def menu():
        print("  _      [Simple RPG Game]")
        print("/ ! \         [ By ]")
        print("\ _ /     [Fajar Firdaus]\n")

        print("[:-----------Hero-----------:]")
        print("[1] > Sniper ")
        print("[2] > Mage")
        print("[3] > Tank")
        print("[:--------------------------:]\n")

        user = input("[Choose Player] >_ ")

        if user == "1":
            print("\n[Details Characters]")
            print("[Name] > Sniper   [O]  ")
            print("[Health] > 50     /|- ︻デ═一")     
            print("[Damage] > 40     / \ ")
            print("[Armor] > 20\n")
            

            print(" [O]                           O")
            print(" /|- ︻デ═一   -     -       (:|:\  ")
            print(" / \                          / \ ")

            user = game("Sniper", 50, 40, 20)
            rival = game("[BOT]", 50, 40, 20)
            user.serang(rival)

            wkt.sleep(3)

            print("   O                  [O]")
            print(" /:|:- - - - -       ( |\ ")
            print("  / \                 / \ ")

            rival.serang(user)

        elif user == "2":
            print("[Details Characters]")
            print("[Name] > Mage           _-_    ")
            print("[Health] > 60          / 0    ")
            print("[Armor] > 20          /  |\/+    ")
            print("[Damage] > 30        /  / \    ")
            
            print("    _-_")
            print("   / 0                             O")
            print("  /  |\/+ . * -- . ' * --        (:|:\  ")
            print(" /  / \                           / \ ")

            user = game("Mage", 60, 30, 20)
            rival = game("[BOT]", 30, 20, 40)
            user.serang(rival)

            wkt.sleep(3)

            print("                       _-_ ")
            print("   O                    O \ ")
            print(" /:|:- - - - -        (-|\ \ ")
            print("  / \                  / \  \ ")

            rival.serang(user)
        
        elif user == "3":
            print("\n[Details Characters]")
            print("[Name] > Tank       _  ")
            print("[Health] > 100     /0\ ")     
            print("[Damage] > 50    /[[|]]\/+  ")
            print("[Armor] > 75       / \  \n")

            print("   _ ")
            print("  /0\                       0 ")
            print("/[[|]]\/+******************:|:\ ")
            print("  / \                      / \ ")

            user = game("Tank", 100, 50, 75)
            rival = game("[BOT]", 58, 40, 50)
            user.serang(rival)

            wkt.sleep(3)

            print("                             _ ")
            print("  0                         /0\  ")
            print("/:|:/+ - - -- -- -       (-[[|]]\ ")
            print(" / \                        / \ ")

            rival.serang(user)



run = game.menu()
