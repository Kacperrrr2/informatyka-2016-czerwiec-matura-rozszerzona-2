wiersze= open('liczby.txt','r')
tab=[]
for line in wiersze:
     tab.append(line.strip())
# ZAD6.1
# licznik_osemkowych=0
# for i in range(0,len(tab)):
#     if tab[i][len(tab[i])-1]=="8":
#         licznik_osemkowych+=1
#
# print(licznik_osemkowych)
# ZAD6.2
# licznik_zer_int=0
# licznik_zer = True
# for i in range(0,len(tab)):
#     if tab[i][len(tab[i])-1]=="4":
#         for j in range(0,len(tab[i])):
#             if tab[i][j]!="0":
#                 licznik_zer=True
#             else:
#                 licznik_zer=False
#                 break
#         if  licznik_zer:
#             licznik_zer_int+=1
#
# print(licznik_zer_int)


# ZAD.6.3
# string=""
# tab_dwojkowy=[]
# licznik_zer_int=0
# licznik_zer = True
# for i in range(0,len(tab)):
#     if tab[i][len(tab[i])-1]=="2":
#        tab_dwojkowy.append(tab[i])
# tab_dwojkowy_bez_znacznika=[]
# for i in range(0,len(tab_dwojkowy)):
#     for j in range(0,len(tab_dwojkowy[i])-1):
#         string+=tab_dwojkowy[i][j]
#     tab_dwojkowy_bez_znacznika.append(string)
#     string=""
# print(tab_dwojkowy_bez_znacznika)
# licznik_dwojkowych_parzystych=0
# for i in range(0,len(tab_dwojkowy)):
#      l=bin(tab_dwojkowy[i])
#      z= int(l,2)
#      if z%2==0:
#         licznik_dwojkowych_parzystych+=1
# print(licznik_dwojkowych_parzystych)
# ZAD6.4


