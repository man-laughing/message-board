#!/usr/bin/python 
#coding:utf8

from random import random
from flask import Flask,render_template,request,jsonify
from flask_redis import FlaskRedis
from datetime import datetime
import uuid
import json
import time

app = Flask(__name__) 
app.config['REDIS_URL']="redis://messageboard-redis:6379/0" 
redis_store = FlaskRedis(app)

'''
def utc2local(utc_dtm):
    local_tm = datetime.fromtimestamp( 0 )
    utc_tm = datetime.utcfromtimestamp( 0 )
    offset = local_tm - utc_tm
    return str(utc_dtm + offset)
'''

def getLocaltime():
    local_time = datetime.now()
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

@app.route("/")
def index():
    return render_template("index.html")

#"utm":time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()) 
@app.route("/liuyanbanpost",methods=['POST'])
def liuyanbanpost():
    msg  = request.form['msg'].strip().encode('utf8')
    uid = "user_"+str(uuid.uuid4()).split('-')[-1]
    #"utm":datetime.utcnow()
    mdoc = {
             "uid":uid,
             "umsg":msg,
             "utm": getLocaltime()
    }
    redisstring = json.dumps(mdoc)
    rs = redis_store.lpush("messages",redisstring)
    if rs:
        return jsonify({"code":1,"msg":"留言成功!"})
    else:
        return jsonify({"code":0,"msg":"留言失败!"})
    

@app.route("/zuixinpinglunpost",methods=['GET'])
def zuixinpinglunpost():
   ddd = []
   rrr = redis_store.lrange("messages",0,2)
   for i in rrr:ddd.append(json.loads(i)) 
   return jsonify(ddd)
    
@app.route("/healthcheck",methods=['GET'])
def healthcheck():
    time.sleep(0.02)
    return jsonify({"code":200,"status":"OK"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
