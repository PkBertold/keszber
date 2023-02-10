#=================|| Készenlétis bérkalkulátor - Bertold ||==================#
#                                                                            #
# Kalkuláció:                                                                #
# 1, Bruttó bér / havi óraszám = 1 órás munkabér                             #
# 2, 1 órás munkabér x készenléti óraszám = készenlétis bér teljes           #
# 3, készenlétis bér teljes x 0,20 = készenlétis bér 20%                     #
#                                                                            #
# Description:                                                               #
# A script azt számolja ki, hogy mennyi pénzt termelt ki az aktuálisan       #
# ledolgozott készenlétis idő (Amit a TimeSheet-ben a megjegyzéshez írunk)   #
#                                                                            #
#____________________________________________________________________________#
import math
brutto_ber = input("Add meg a bruttó béred: ")
havi_oraszam = input("Add meg a havi óraszámod: (Default:160) ")
keszenlet_oraszam = input("Add meg a havi készenlétis óraszámot (Beosztás): ")
keszenlet_ledolgozott = input("Add meg a ledolgozott készenlétis óraszámot (Munkaidőnyilvántartó): ")

oras_munkaber = int(brutto_ber) / int(havi_oraszam)
print("Az 1 órás munkabéred: ", math.trunc(oras_munkaber),"Ft")
keszenlet20 = int(oras_munkaber) * int(keszenlet_oraszam) * 0.20
keszenlet100 = int(oras_munkaber) * int(keszenlet_ledolgozott)
print("A havi készenléti idő értéke: ", math.trunc(keszenlet20),"Ft")
print("A havi ledolgozott készenléti idő értéke:", keszenlet100,"Ft")
