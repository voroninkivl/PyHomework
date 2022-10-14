name=input("Введите имя студента ")
surname=input("Введите фамилию студента ")
years=input("Введите год рождения студента ")
print(name+'_'+surname+'_'+years)
name,surname=surname,name
years=int(years)+60
print(name+'_'+surname+'_'+str(years))
