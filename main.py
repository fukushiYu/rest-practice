from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import _config as cfg
import pymysql,json
import pymysqlpool

app = FastAPI() 
print(cfg.package_title)
try:
    # 先使用mysql,以後要加 oracle, postgresql
    pool = pymysqlpool.ConnectionPool(**cfg.config)
    print(">>> fastapi + pymysql-pool[%s] +"%(str(pool.size()),))
except:
    print(">>> error open DB")
    exit()


def selectHandler(sqlname,params):
    global pool
    sqlobj = cfg.sqlstrings[sqlname]
    try:
        pobj = json.loads(params)
        for k,v in pobj.items():
            sqlobj["params"][k]=v
    except:
        pass
    try:
        #這裡會根據不同的DB，有不同的語法
        connection=pool.get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        print(sqlobj["sql"],str(sqlobj["params"]))
        cursor.execute(sqlobj["sql"],sqlobj["params"])
        results = cursor.fetchall()
        connection.close()
        return {"detail": results}
    except Exception as e:
        return {"detail": e}


@app.get("/") 
def root():
    rstr = cfg.html["root"]
    return HTMLResponse(content=rstr)

@app.get("/query/{sqlname}")
def query(sqlname:str, params:str = ''):
    if sqlname in cfg.sqlstrings:
        return selectHandler(sqlname,params)
    else:
        return {"detail":"Not found in /query"}
 
 

