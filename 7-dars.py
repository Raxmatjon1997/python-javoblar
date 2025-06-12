#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#ismlar=["Abror","Mahmud","Nurmuhammad"]
#print("Salom "+ismlar[0]+" bugun choyxona bormi?")
#print(ismlar[1]+", choyxonaga boramizmi?")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
#sonlar=[-1,5,0,12,25,1.5,6.5]
#print(sonlar[0]+sonlar[3])

#Yuqoridagi ro'yxatdagi sonlar ustida 
#turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, 
#ba'zilarini esa almashtiring. 
#print(sonlar[4]//sonlar[1])
#sonlar[0]=11
#print(sonlar[0]+sonlar[1])


#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
    
t_shaxslar=["Alisher Navoiy","Amir Temur", "Bobur","Xorazmiy"]
z_shaxslar=["Ilon Mask","Tramp", "Yamal"]
#print("Men tarixiy shaxslardan "+t_shaxslar.pop(2)+" bilan,\nzamonaviy shaxslardan esa "+z_shaxslar.pop(2)+" bilan \nsuhbat qilishni istar edim")


#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 
#5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends=[]
friends.append("Asqar")
friends.append("Javohir")
friends.append("Musulmon")
friends.append("Jonibek")
friends.append("Dilshod")
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() 
#metodi yordamida o'chrib tashlang.
friends.remove("Javohir")
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append("Sohib")
print(friends)
friends.insert(2, "Nurmuhammad")
print(friends)
friends.insert(0, "Xushnud")
print(friends)



#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
#metodlari yordamida mehmonga kelgan do'stlaringizning ismini 
#friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar=["Akam", "Yangam","Xolam"]
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop())

print(mehmonlar)

























