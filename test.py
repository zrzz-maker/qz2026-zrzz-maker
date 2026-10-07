from main import analyze_log
f = open("app.jsonl","w",encoding="utf-8")
f.write('{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}\n')
f.write('{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}\n')
f.write('随便写的\n')
f.write('{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}\n')
f.close()

res=analyze_log("app.jsonl")
print("总数:",res["total"])
print("级别统计：",res["by_level"])
print("用户统计",res["by_user"])
print("最后一条错误：",res["last_error"])