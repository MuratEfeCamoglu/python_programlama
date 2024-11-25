sayılar=[]

print('5 sayı giriniz')

for i in range(5):
    a=eval(input(f"{i+1}. sayı:" ))
    sayılar.append(a)


işlenmiş=[(sayı,sayı**2-20)for sayı in sayılar]
sıralı=sorted(işlenmiş,key=lambda x:x[1])
print("Sırlanmış ", sıralı)