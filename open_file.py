def open_file(file_name, intention,return_type=None,text_for_write=None):
    if intention=="r" and return_type=="list":
        with open(file_name,"r") as file:
            r=file.readlines()
            response=[d.rstrip() for d in r]
        return response
    elif intention=="r" and return_type=="read": 
        with open(file_name,"r") as file:
            response=file.read()
        return response
    elif intention=="a":
        with open(file_name,"a+") as file:
            file.write(text_for_write+"\n")
    elif intention=="w":
        with open(file_name,"w") as file:
            file.write(text_for_write)
    
    else:
        pass

#print(open_file("database/database.txt","w",text_for_write="test"))
        