
#2.1
m=[]
for i in logs:
    n=i["level"]
    if n=="ERROR":
        m.append(i)

#2.2
d={}
for i in logs:
    u=i["user"]
    if u in d:
        d[u]=d[u]+1
    else:
        d[u]=1

#2.3因为len（logs）算出来的是日志的条数，算不出每个用户出现几次· 得用for循环，把user对应的值取出来重复一次加一


