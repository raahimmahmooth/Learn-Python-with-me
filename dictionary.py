phone_no={#dict() can be use
    "raahim":591957,
    'shiyam':999300,
    'mohan':494449
}
print(phone_no['raahim'])
print(phone_no)
phone_no['raahim']=4884884882
print(phone_no)
phone_no['kumar']={111,222,3333}
phone_no['raahim']={'raahim_home':859133993939939,'raahim_per':2993939}
print(phone_no)
print(phone_no['raahim']['raahim_home'])

data={
    3:"raahim",
    2:"linoshen",
    0:"ikram"
}
print(data[0])
del data[3]
print(data)
print(data.pop(0))#return ikram
print(data)
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())