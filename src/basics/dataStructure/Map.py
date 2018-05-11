'''
Created on 2018年5月11日

Map 是一种关联数组的数据结构，也常被称为字典或键值对。
在 Python 中 dict(Map) 是一种基本的数据结构。
'''

if __name__ == '__main__':
   # map 在 python 中是一个keyword
    hash_map = {} # or dict()
    hash_map['shaun'] = 98
    hash_map['wei'] = 99
    exist = 'wei' in hash_map  # check existence
    point = hash_map['shaun']  # get value by key
    point = hash_map.pop('shaun') # remove by key, return value
    keys = hash_map.keys()  # return key list
    # iterate dictionary(map)
    for key, value in hash_map.items():
        # do something with k, v
        pass