while(True):
    days = 31
    i = 1
    count1 = 0
    count2 = 0
    count3 = 0
    count = 0
    year = int(input("Введите год: "))
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("Вискокосный год")
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count1 = count1+b+c
            i+=1
        count1*=7
        i=1
        days=30
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count2 = count2+b+c
            i+=1
        count2*=4
        days=29
        i=1
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count3 = count3+b+c
            i+=1
        print(count1+count2+count3)
    else: 
        print("Не вискокосный год")
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count1 = count1+b+c
            i+=1
        count1*=7
        i=1
        days=30
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count2 = count2+b+c
            i+=1
        count2*=4
        days=28
        i=1
        while(days>=i):
            a=i
            b=a%10
            a-=b
            c=a//10
            count3 = count3+b+c
            i+=1
        print(count1+count2+count3)