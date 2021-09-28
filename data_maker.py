from datetime import datetime
hozir=datetime.now()
vaqt=hozir.strftime("%H:%M:%S")
def make_data(data_type):
    if data_type=="count":
                    with open("count/trans_count.txt","r+") as count:
                        r=count.readlines()
                        son=int(r[0])
                        a=son+1
                        a=str(a)
                        with open("count/trans_count.txt","w") as count:
                            count.write(a)
    


def get_data(data_type):
    if data_type=="user_info":
                    with open("database/data.txt","r+") as db:
                        r=db.readlines()
                        users=[d.rstrip() for d in r]
                        return len(users)
    elif data_type=="trans_count":
                                with open("count/trans_count.txt","r") as count:
                                    read=count.readlines()
                                    return max(read)
    elif data_type=="all_datas":
                    with open("database/data.txt","r+") as db:
                        r=db.readlines()
                        users=[d.rstrip() for d in r]
                    with open("count/trans_count.txt","r") as count:
                                read=count.readlines()
                                
                    response=f"👥Bot foydalanuvchilari➙{len(users)} ta\n📅Bugungi sana➙{hozir.date()}\n🕰️Hozirgi vaqt➙{vaqt}\n✅Shu vaqtgacha qilingan tarjimalar soni➙{max(read)} ta"
                    return response             
                                
                            
    
                    