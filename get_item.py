import random
items = [' âąđ±đïŽżÖ â„', 'đżïŽżÖ â„', 'âą đžđž â„Ë  ', 'đđïŽżÖ', ' âą đŒđżïŽŸÖ', ' âąđđïŽżÖ â„', '-đ„âšïŽżÖ â„ ', 'âą|âą ăđâ',
' âĄïžđ âą|âąâĄ', '- âœđ·âšâÖ', 'â„âđđ„â', 'đđ­âĄÖ', '-âđđâ', '- âœđ©đżâÖ',
'âÌŻ đŒđ |âĄ', 'â đđ·', 'ââœâ„ÌÍąâ đŁđ', 'âą|âą âšđžâ', '  Ö đ­đÛŠ', 'Ö đđ­ÛŠ', 'Ö âĄïžđ±ÛŠ',
'âĄáŽÌđâšâźï ', 'âźï âœđâïžâÛŠË', 'ââđ„ââ©', ' ââŠâœâ»đ„ââÙ°ÛŠ', 'âĄ Ìâ âšđŻâŁâŠ', 'ââ©âœđđ©ââŁâż',
'ÛŠÙ°âââ„ ÍąËđŠđÛŠâ', 'âĄïžâÖâ', 'ââŁđ°âïžââŠ', 'âŸâŁâżđââ„', ' ââżđ„đ âââ„', 'đŽđžâżâŁ', 'â„ââœ âĄđŠđž']
decoration_items={"item1":["â€â€â€â€â€","âŠâŠâŠâŠâŠ"],"item2":["đ","đ"],"item3":["âćœĄ(",")ćœĄâ"],"item4":["`â”âą.Âž,â”Â°â”.ïœĄ.â°","â°.ïœĄ.â”Â°â”,Âž.âąâ”ÂŽ"],"item5":["Â·âÂ·Ă·Â±âĄÂ±:â","â:Â±âĄÂ±Ă·Â·âÂ·"],"item6":["âȘâą]âąÂ·Âșâ«Â·ăÂ»","Â«ăÂ·â«ÂșÂ·âą[âąâȘ"],"item7":["âą]âąÂ·âŠÂșâŠÂ·Â»","Â«Â·âŠÂșâŠÂ·âą[âą"],"item8":["~-<đŽ>-~","~-<âïž>-~"],"item9":["âââ","âââ"],"item10":["âÂž.âąââą.Âžâ","ââĄ.âąââą.â"]}

item1={"A":"đ°","a":"đ",
       "B":"đ±","b":"đ",
       "C":"đČ","c":"đ",
       "D":"đł","d":"đ",
       "E":"đŽ","e":"đ",
       "F":"đ”","f":"đ",
       "G":"đ¶","g":"đ",
       "H":"đ·","h":"đ",
       "I":"đž","i":"đ",
       "J":"đč","j":"đ",
       "K":"đș","k":"đ",
       "L":"đ»","l":"đ",
       "M":"đŒ","m":"đ",
       "N":"đœ","n":"đ",
       "O":"đŸ","o":"đ",
       "P":"đż","p":"đ",
       "Q":"đ","q":"đ",
       "R":"đ","r":"đ",
       "S":"đ","s":"đ",
       "T":"đ","t":"đ",
       "U":"đ","u":"đ",
       "V":"đ","v":"đ",
       "W":"đ","w":"đ ",
       "X":"đ","x":"đĄ",
       "Y":"đ","y":"đą",
       "Z":"đ","z":"đŁ"}

item2={"A":"đ","a":"đą",
       "B":"đ","b":"đŁ",
       "C":"đ","c":"đ€",
       "D":"đ","d":"đ„",
       "E":"đ","e":"đŠ",
       "F":"đ","f":"đ§",
       "G":"đ","g":"đš",
       "H":"đ","h":"đ©",
       "I":"đ","i":"đȘ",
       "J":"đ","j":"đ«",
       "K":"đ","k":"đŹ",
       "L":"đ","l":"đ­",
       "M":"đ","m":"đź",
       "N":"đ","n":"đŻ",
       "O":"đ","o":"đ°",
       "P":"đ","p":"đ±",
       "Q":"đ","q":"đČ",
       "R":"đ","r":"đł",
       "S":"đ","s":"đŽ",
       "T":"đ","t":"đ”",
       "U":"đ","u":"đ¶",
       "V":"đ","v":"đ·",
       "W":"đ","w":"đž",
       "X":"đ","x":"đč",
       "Y":"đ ","y":"đș",
       "Z":"đĄ","z":"đ»"}

item3={"A":"đ","a":"đȘ",
       "B":"đ","b":"đ«",
       "C":"đ","c":"đŹ",
       "D":"đ","d":"đ­",
       "E":"đ","e":"đź",
       "F":"đ","f":"đŻ",
       "G":"đ","g":"đ°",
       "H":"đ","h":"đ±",
       "I":"đ","i":"đČ",
       "J":"đ","j":"đł",
       "K":"đ","k":"đŽ",
       "L":"đ","l":"đ”",
       "M":"đ","m":"đ¶",
       "N":"đ","n":"đ·",
       "O":"đ","o":"đž",
       "P":"đ","p":"đč",
       "Q":"đ ","q":"đș",
       "R":"đĄ","r":"đ»",
       "S":"đą","s":"đŒ",
       "T":"đŁ","t":"đœ",
       "U":"đ€","u":"đŸ",
       "V":"đ„","v":"đż",
       "W":"đŠ","w":"đ",
       "X":"đ§","x":"đ",
       "Y":"đš","y":"đ",
       "Z":"đ©","z":"đ"}

item4={"A":"áŽ","a":"áŽ",
       "B":"Ê","b":"Ê",
       "C":"áŽ","c":"áŽ",
       "D":"áŽ","d":"áŽ",
       "E":"áŽ","e":"áŽ",
       "F":"ê°","f":"ê°",
       "G":"Éą","g":"Éą",
       "H":"Ê","h":"Ê",
       "I":"ÉȘ","i":"ÉȘ",
       "J":"áŽ","j":"áŽ",
       "K":"áŽ","k":"áŽ",
       "L":"Ê","l":"Ê",
       "M":"áŽ","m":"áŽ",
       "N":"ÉŽ","n":"ÉŽ",
       "O":"áŽ","o":"áŽ",
       "P":"áŽ","p":"áŽ",
       "R":"Ê","r":"Ê",
       "S":"s","s":"s",
       "T":"áŽ","t":"áŽ",
       "U":"áŽ","u":"áŽ",
       "V":"áŽ ","v":"áŽ ",
       "W":"áŽĄ","w":"áŽĄ",
       "X":"x","x":"x",
       "Y":"Ê","y":"Ê",
       "Z":"áŽą","z":"áŽą"}

def get(item,text,decoration=None):
    if decoration:
        if decoration=="items":
            smile=random.choice(items)
            b=list(smile)
            b.reverse()
            match=""
            for c in b:
                match+=c
            response=""
            if item=="item1":
                for letter in text:
                    if letter in item1.keys():
                        response+=item1[letter]
                    else:
                        response+=letter
            
            
            elif item=="item2":
                for letter in text:
                    if letter in item2.keys():
                        response+=item2[letter]
                    else:
                        response+=letter
            elif item=="item3":
                for letter in text:
                    if letter in item3.keys():
                        response+=item3[letter]
                    else:
                        response+=letter
            elif item=="item4":
                for letter in text:
                    if letter in item4.keys():
                        response+=item4[letter]
                    else:
                        response+=letter
            response=smile+response+match
        elif decoration=="decoration_items":
            item_name=["item1","item2","item3","item4","item5","item6","item7","item8","item9","item10"]
            smile=random.choice(item_name)
            smile=decoration_items[smile]
            response=""
            if item=="item1":
                for letter in text:
                    if letter in item1.keys():
                        response+=item1[letter]
                    else:
                        response+=letter
            
            
            elif item=="item2":
                for letter in text:
                    if letter in item2.keys():
                        response+=item2[letter]
                    else:
                        response+=letter
            elif item=="item3":
                for letter in text:
                    if letter in item3.keys():
                        response+=item3[letter]
                    else:
                        response+=letter
            elif item=="item4":
                for letter in text:
                    if letter in item4.keys():
                        response+=item4[letter]
                    else:
                        response+=letter
            response=smile[0]+response+smile[1]
    else:
            response=""
            if item=="item1":
                for letter in text:
                    if letter in item1.keys():
                        response+=item1[letter]
                    else:
                        response+=letter
            
            
            elif item=="item2":
                for letter in text:
                    if letter in item2.keys():
                        response+=item2[letter]
                    else:
                        response+=letter
            elif item=="item3":
                for letter in text:
                    if letter in item3.keys():
                        response+=item3[letter]
                    else:
                        response+=letter
            elif item=="item4":
                for letter in text:
                    if letter in item4.keys():
                        response+=item4[letter]
                    else:
                        response+=letter
        
    return response

def add_item(text,smile_type):
    if smile_type=="items":
        match=""
        smile=random.choice(items)
        b=list(smile)
        b.reverse()
        for c in b:
            match+=c
        response=smile+text+match
    elif smile_type=="decoration_items":
            item_name=["item1","item2","item3","item4","item5","item6","item7","item8","item9","item10"]
            smile=random.choice(item_name)
            smile=decoration_items[smile]
            response=smile[0]+text+smile[1]
            
    return response
        
        

            
        
    
    
#print(add_item("đđđđđ","decoration_items"))
#print(get("item1","Salom"))



#request=input(">>")
#match=""
#for letter in request:
#    if letter in item1.keys():
#        match+=item1[letter]
#    else:
#        match+=letter
#print(match)

#if letter in item2.keys():
#        response2=request.replace(letter,item2[letter])
#    else:
#        continue