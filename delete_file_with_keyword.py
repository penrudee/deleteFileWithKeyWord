list_key_word=[
'apple',
'banana',
'pap',
'zebra',
'sea',
'bat'
]
pathE=r"E:/jpg"
for root, dirs, files in os.walk(pathE):
    for name in files:
        for k in list_key_word:
            if k in name:
                f = os.path.join(pathE,name)
                print(name)
                os.remove(f)
                
