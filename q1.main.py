import json
import os
def analyze_log(filepath):
    d={
        "total":0,
        "by_level":{},
        "by_user":{},
        "last_error":None
    }
    if not os.path.exists(filepath):
        return d
    try:
        f=open(filepath,'r',encoding='utf-8')
        lines=f.readlines()
    except:
        return d

    for line in lines:
        line = line.strip()
        if line =="":
            continue
        try:
            data = json.loads(line)
        except:
            continue

        d["total"]+=1

        lvl=data["level"]
        usr=data["user"]

        if lvl not in d["by_level"]:
            d["by_level"][lvl]=0
        d["by_level"][lvl]=d["by_level"][lvl]+1

        if usr not in d["by_user"]:
            d["by_user"][usr]=0
        d["by_user"][usr]=d["by_user"][usr]+1

        if lvl == "ERROR":
            d["last_error"]=data["message"]

    f.close()
    return d
