Michl = int(input("Enter a year of birth not going before the year 1900."))
if Michl < 1900:
            print("That is an invalid year. Please input a year that is not before the year 1900.")
            exit()
if Michl % 12 == 4:
  print("Your Chinese Zodiac sign is: Rat (鼠 / Shǔ)")
elif Michl % 12 == 5:
  print("Your Chinese Zodiac sign is: Ox (牛 / Niú)")
elif Michl % 12 == 6:
  print("Your Chinese Zodiac sign is: Tiger (虎 / Hǔ)")
elif Michl % 12 == 7:
  print("Your Chinese Zodiac sign is: Rabbit (兔 / Tù)")
elif Michl % 12 == 8:
  print("Your Chinese Zodiac sign is: Dragon (龙 / Lóng)")
elif Michl % 12 == 9:
  print("Your Chinese Zodiac sign is: Snake (蛇 / Shé)")
elif Michl % 12 == 10:
  print("Your Chinese Zodiac sign is: Horse (马 / Mǎ)")
elif Michl % 12 == 11:
  print("Your Chinese Zodiac sign is: Goat (羊 / Yáng)")
elif Michl % 12 == 0:
  print("Your Chinese Zodiac sign is: Monkey (猴 / Hóu)")
elif Michl % 12 == 1:
  print("Your Chinese Zodiac sign is: Rooster (鸡 / Jī)")
elif Mich % 12 == 2:
  print("Your Chinese Zodiac sign is: Dog (狗 / Gǒu)")
elif Mich % 12 == 3:
  print("Your Chinese Zodiac sign is: Pig (猪 / Zhū)")
