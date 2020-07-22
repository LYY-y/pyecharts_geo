from mongoCon import *

count = 0
# district.drop()
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'guangzhou' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('guangzhou')
print(count)

count = 0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'chenzhou' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('chenzhou')
print(count)


count = 0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'jinhua' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('jinhua')
print(count)

count = 0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'wenzhou' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('wenzhou')
print(count)

count=0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'nanyang' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('nanyang')
print(count)

count=0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'shanghai' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('shanghai')
print(count)

count=0
for address in shop.find({},{"_id":0, "address": 1}):
    try:
        addressArr = str(address['address']).lower().replace(","," ").split(" ")
        # print(addressArr)
        for a in addressArr:
            if 'foshan' == a:
                count += 1
                print(addressArr)
                break
    except KeyError:
        print("地址为空！")
        pass

print('foshan')
print(count)
