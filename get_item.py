import random
items = [' •🌱💚﴿ֆ ❥', '🍿﴿ֆ ❥', '• 🌸💸 ❥˓  ', '💝🎀﴿ֆ', ' • 🐼🌿﴾ֆ', ' •🙊💙﴿ֆ ❥', '-🐥✨﴿ֆ ❥ ', '•|• 〄💖‘',
' ⚡️💊 •|•℡', '- ⁽🌷✨₎ֆ', '❥┇👑🔥“', '💜💭℡ֆ', '-┆💙👒♕', '- ⁽🎩🍿₎ֆ',
'“̯ 🐼💗 |℡', '⁞ 🐝🍷', '┋⁽❥̚͢₎ 🐣💗', '•|• ✨🌸‘', '  ֆ 💭💔ۦ', 'ֆ 💛💭ۦ', 'ֆ ⚡️🔱ۦ',
'℡ᴖ̈💜✨⋮', '⋮⁽🌔☄️₎ۦ˛', '⁞❉💥┋♩', ' ⁞✦⁽☻🔥₎“ٰۦ', '℡ ̇₎ ✨🐯⇣✦', '⁞♩⁽💎🌩₎⇣✿',
'ۦٰ‏┋❥ ͢˓🦁💛ۦ‏', '⚡️♛ֆ₎', '♛⇣🐰☄️₎✦', '⁾⇣✿💖┊❥', ' ₎✿💥🎃 ⁞“❥', '😴🌸✿⇣', '❥┊⁽ ℡🦁🌸']
decoration_items={"item1":["↤↤↤↤↤","↦↦↦↦↦"],"item2":["𒆜","𒆜"],"item3":["★彡(",")彡★"],"item4":["`✵•.¸,✵°✵.｡.✰","✰.｡.✵°✵,¸.•✵´"],"item5":["·∙·÷±‡±:∙","∙:±‡±÷·∙·"],"item6":["♪•]•·º♫·》»","«《·♫º·•[•♪"],"item7":["•]•·✦º✦·»","«·✦º✦·•[•"],"item8":["~-<🌴>-~","~-<☀️>-~"],"item9":["⇉⇉⇉","⇇⇇⇇"],"item10":["★¸.•☆•.¸★","★⡀.•☆•.★"]}

item1={"A":"𝙰","a":"𝚊",
       "B":"𝙱","b":"𝚋",
       "C":"𝙲","c":"𝚌",
       "D":"𝙳","d":"𝚍",
       "E":"𝙴","e":"𝚎",
       "F":"𝙵","f":"𝚏",
       "G":"𝙶","g":"𝚐",
       "H":"𝙷","h":"𝚑",
       "I":"𝙸","i":"𝚒",
       "J":"𝙹","j":"𝚓",
       "K":"𝙺","k":"𝚔",
       "L":"𝙻","l":"𝚕",
       "M":"𝙼","m":"𝚖",
       "N":"𝙽","n":"𝚗",
       "O":"𝙾","o":"𝚘",
       "P":"𝙿","p":"𝚙",
       "Q":"𝚀","q":"𝚚",
       "R":"𝚁","r":"𝚛",
       "S":"𝚂","s":"𝚜",
       "T":"𝚃","t":"𝚝",
       "U":"𝚄","u":"𝚞",
       "V":"𝚅","v":"𝚟",
       "W":"𝚆","w":"𝚠",
       "X":"𝚇","x":"𝚡",
       "Y":"𝚈","y":"𝚢",
       "Z":"𝚉","z":"𝚣"}

item2={"A":"𝘈","a":"𝘢",
       "B":"𝘉","b":"𝘣",
       "C":"𝘊","c":"𝘤",
       "D":"𝘋","d":"𝘥",
       "E":"𝘌","e":"𝘦",
       "F":"𝘍","f":"𝘧",
       "G":"𝘎","g":"𝘨",
       "H":"𝘏","h":"𝘩",
       "I":"𝘐","i":"𝘪",
       "J":"𝘑","j":"𝘫",
       "K":"𝘒","k":"𝘬",
       "L":"𝘓","l":"𝘭",
       "M":"𝘔","m":"𝘮",
       "N":"𝘕","n":"𝘯",
       "O":"𝘖","o":"𝘰",
       "P":"𝘗","p":"𝘱",
       "Q":"𝘘","q":"𝘲",
       "R":"𝘙","r":"𝘳",
       "S":"𝘚","s":"𝘴",
       "T":"𝘛","t":"𝘵",
       "U":"𝘜","u":"𝘶",
       "V":"𝘝","v":"𝘷",
       "W":"𝘞","w":"𝘸",
       "X":"𝘟","x":"𝘹",
       "Y":"𝘠","y":"𝘺",
       "Z":"𝘡","z":"𝘻"}

item3={"A":"𝓐","a":"𝓪",
       "B":"𝓑","b":"𝓫",
       "C":"𝓒","c":"𝓬",
       "D":"𝓓","d":"𝓭",
       "E":"𝓔","e":"𝓮",
       "F":"𝓕","f":"𝓯",
       "G":"𝓖","g":"𝓰",
       "H":"𝓗","h":"𝓱",
       "I":"𝓘","i":"𝓲",
       "J":"𝓙","j":"𝓳",
       "K":"𝓚","k":"𝓴",
       "L":"𝓛","l":"𝓵",
       "M":"𝓜","m":"𝓶",
       "N":"𝓝","n":"𝓷",
       "O":"𝓞","o":"𝓸",
       "P":"𝓟","p":"𝓹",
       "Q":"𝓠","q":"𝓺",
       "R":"𝓡","r":"𝓻",
       "S":"𝓢","s":"𝓼",
       "T":"𝓣","t":"𝓽",
       "U":"𝓤","u":"𝓾",
       "V":"𝓥","v":"𝓿",
       "W":"𝓦","w":"𝔀",
       "X":"𝓧","x":"𝔁",
       "Y":"𝓨","y":"𝔂",
       "Z":"𝓩","z":"𝔃"}

item4={"A":"ᴀ","a":"ᴀ",
       "B":"ʙ","b":"ʙ",
       "C":"ᴄ","c":"ᴄ",
       "D":"ᴅ","d":"ᴅ",
       "E":"ᴇ","e":"ᴇ",
       "F":"ꜰ","f":"ꜰ",
       "G":"ɢ","g":"ɢ",
       "H":"ʜ","h":"ʜ",
       "I":"ɪ","i":"ɪ",
       "J":"ᴊ","j":"ᴊ",
       "K":"ᴋ","k":"ᴋ",
       "L":"ʟ","l":"ʟ",
       "M":"ᴍ","m":"ᴍ",
       "N":"ɴ","n":"ɴ",
       "O":"ᴏ","o":"ᴏ",
       "P":"ᴘ","p":"ᴘ",
       "R":"ʀ","r":"ʀ",
       "S":"s","s":"s",
       "T":"ᴛ","t":"ᴛ",
       "U":"ᴜ","u":"ᴜ",
       "V":"ᴠ","v":"ᴠ",
       "W":"ᴡ","w":"ᴡ",
       "X":"x","x":"x",
       "Y":"ʏ","y":"ʏ",
       "Z":"ᴢ","z":"ᴢ"}

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
        
        

            
        
    
    
#print(add_item("𝚂𝚊𝚕𝚘𝚖","decoration_items"))
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