import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,members_json_file,organizers_json_file,Email,Password):
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    f=open(events_json_file,'w+')
    d_eve={     
            "Id":Event_ID,
            "Name":Event_Name,
            "Organizer":org,
            "Start Date":Start_Date,
            "Start Time":Start_Time,
            "End Date":End_Date,
            "End Time":End_Time,
            "Users Registered":Users_Registered,
            "Capacity":Capacity,
            "Seats Available":Availability
        }
    try:
        content=json.load(f)
        if d_eve not in content:
            content.append(d_eve)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
        
    except JSONDecodeError:
        li=[]
        li.append(d_eve)
        json.dump(li,f)
        f.close()
         
def View_Events(org,events_json_file):
    name=org
    file=open(events_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Organizer"]==org:
            dit=[{
                "ID":content[i]['Id'],
                "Name":content[i]['Name'],
                "Organizer":content[i]['Organizer'],
                "Start Date":content[i]['Start Date'],
                "Start Time":content[i]['Start Time'],
                "End Date":content[i]['End Date'],
                "End Time":content[i]['End Time'],
                "Users Registered":content[i]['Users Registered'],
                "Capacity":content[i]['Capacity'],
                "Seats Available":content[i]['Seats Available'],
            }]
            return dit
        else:
            pass
    file.close()
    
def View_Event_ByID(events_json_file,Event_ID):
    f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Id"]==Event_ID:
              d=[{
                "ID":content[i]['Id'],
                "Name":content[i]['Name'],
                "Organizer":content[i]['Organizer'],
                "Start Date":content[i]['Start Date'],
                "Start Time":content[i]['Start Time'],
                "End Date":content[i]['End Date'],
                "End Time":content[i]['End Time'],
                "Users Registered":content[i]['Users Registered'],
                "Capacity":content[i]['Capacity'],
                "Seats Available":content[i]['Seats Available'],
            }]
    
    return d
   
    f.close()

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    f=open(events_json_file,'w+')
    content=json.load(f)
    organizer=org
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            if detail_to_be_updated=='Name':
                content[i]['Name']=updated_detail
            elif detail_to_be_updated=='Start Date':
                content[i]['Start Date']=updated_detail
            elif detail_to_be_updated=='Start Time':
                content[i]['Start Time']=updated_detail
            elif detail_to_be_updated=='End Date':
                content[i]['End Date']=updated_detail
            elif detail_to_be_updated=='End Time':
                content[i]['End Time']=updated_detail
            else:
                return False  
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close() 
    return True
    

def Delete_Event(org,events_json_file,event_ID):
    file=open(events_json_file,'r+')
    content=json.load(file)
    id=event_ID
    for i in range(len(content)):
        if content[i]["Id"]==event_ID:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            return False

def Register_for_Event(events_json_file,event_id,Full_Name):
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    f=open(events_json_file,'w+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            content[i]["Users Registered"].append(Full_Name)
            content[i]['Seats Available']-=1
    f.seek(0)
    f.truncate()
    json.dump(content, f)
    f.close()
    return True


       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f=open(events_json_file,'r+')
    content=json.load(f)
    print(content)
    for i in range(len(content)):
        if Full_Name in content[i]['Users Registered']:
            datetime. strptime(content[i]['Start Date'], '%y/%m/%d')
            if datetime. strptime(content[i]['Start Date'], '%y/%m/%d')>=date_today:
                if content[i]['Start Time']>=now:
                    upcoming_ongoing.append(content[i])
                    return upcoming_ongoing
                else:
                    pass
            else:
                pass
    

def Update_Password(members_json_file,Full_Name,new_password):
    file=open(members_json_file,'w+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
           content[i]["Password"]=new_password
    file.seek(0)
    file.truncate()
    json.dump(content, file)
    file.close()
    return True

def View_all_events(events_json_file):
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details