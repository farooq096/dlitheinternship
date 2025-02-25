'''



a=["apple","orange","apple"]
print(len(a))

a=["apple","orange","apple"]
b=[23,28.09,22<23,25>28]
c=[2.90,9.0,99.9]
d=[23>40,35<38]
e=["apple","orange",94,90.0,40<39,38>35]
print(a)
print(b)
print(c)
print(d)
print(e)
print(type(e))





a=list(("apple","orange",94,90.0,40<39,38>35))
print(a)



a=list(("apple","orange",94,90.0,40<39,38>35))
print(a[-5])



a=list(("apple","orange",94,90.0,40<39,38>35))
print(a[:-1])
print(a[:1])
print(a[:4])
print(a[1:])
if "apple" in a:
      print("true")



a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
a[1:4]=["adc","dsa","ade"]
print(a)




a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
a[1:4]=["DBC","BC","VANILLLA"]
a.append("mango")
a.insert(1,"kiwi")

print(a)





a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
b=["adc","dsa","ade"]
a.extend(b)
print(a)




a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
b=("adc","dsa","ade")
a.extend(b)
print(a)




a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
a.remove("BC")
print(a)

a=["DBC","BC","VANILLLA","BELGIUM","BUTTERSCOTCH"]
a.pop(1)
print(a)



bike=["ninja","ducati","bmw","xpulse","RX100"]
bike.clear()


a=["hyd","udupi","bidar"]
a[2]="goa"
print(a)


web=["sqiud games","lost in space","kota factory"]
web.insert(0,"got")
print(web)





web=["sqiud games","lost in space","kota factory","got","family"]
web.insert(3,"get")
print(web)





cricket=["ICT","RCB","KB","CSK"]
cricket.remove("CSK")
print(cricket)



a=[51,234,44,23,12,112,2344,123,33]
a.sort()
print(a)


web=["sqiud games","lost in space","kota factory","got","family"]
web.sort()
print(web)


a=["dj","zain","shabaz"]
a.append("roshan")
a.sort()
print(a)



hob=["code","sleeping","walk","bike ride"]
hob.insert(0,"coding")
hob.remove("coding")
print(hob)
hob.append("python")
print(hob)
hob.pop(3)
print(hob)

'''

