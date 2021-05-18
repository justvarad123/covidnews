from flask import Flask,request,make_response,render_template
import os,json
import requests
import bs4


app = Flask(__name__) 

@app.route('/news', methods =['POST', 'GET'])
def weather():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    if parameters.get("news") :
        url="https://coronaclusters.in/maharashtra/sangli#data"
        ds=requests.get(url)
        sp=bs4.BeautifulSoup(ds.text,'html.parser')
        s=[]
        for data in sp.find_all('h5'):
            d=data.text
            s.append(d)
        cases="Confirmed"+":"+s[0]+'\n'+"Acive"+":"+s[1]+'\n'+"Recoverd"+":"+s[2]+'\n'+"Deaths"+":"+s[3]
        return {
            "fulfillmentText": cases
         }
    elif parameters.get("beds") :
        url="http://117.204.250.138/Covid19mgt/CovidBedInfo.aspx"
        ds=requests.get(url)
        sp=bs4.BeautifulSoup(ds.text,'html.parser')
        l1="https://goo.gl/maps/MsYTYohRebWiuSVR8"
        l2="https://goo.gl/maps/C2jCPVxdErcWbAgM8"
        l4="https://goo.gl/maps/LEiZLqzswssj96PZ9"
        l6="https://goo.gl/maps/mv18wBfQQNQkP8pd9"
        n=[]
        ao=[]
        co=[]
        ib=[]
        wb=[]
        for data in sp.find_all('tr')[25:83]:
            for d in data.find_all('td')[1]:
                if(d=="TASGAON"):
                    for d in data.find_all('td')[2]:
                        n.append(d)
                    for d in data.find_all('td')[4]:
                        ao.append(d)
                    for d in data.find_all('td')[5]:
                        co.append(d)
                    for d in data.find_all('td')[7]:
                        ib.append(d.string)
                    for d in data.find_all('td')[10]:
                        wb.append(d.string)
        info="1) "+n[0]+'\n'+"Administrative Officer :"+" "+ao[0]+'\n'+"Contact No :"+" "+co[0]+'\n'+"ICU Beds Available :"+" "+ib[0]+'\n'+"Ward Beds Available :"+" "+wb[0]+'\n'+"Location :"+" "+l1+'\n'+'\n'+"2) "+n[1]+'\n'+"Administrative Officer :"+" "+ao[1]+'\n'+"Contact No :"+" "+co[1]+'\n'+"ICU Beds Available :"+" "+ib[1]+'\n'+"Ward Beds Available :"+" "+wb[1]+'\n'+'\n'+"3) "+n[2]+'\n'+"Administrative Officer :"+" "+ao[2]+'\n'+"Contact No :"+" "+co[2]+'\n'+"ICU Beds Available :"+" "+ib[2]+'\n'+"Ward Beds Available :"+" "+wb[2]+'\n'+"Location :"+" "+l2+'\n'+'\n'+"4) "+n[3]+'\n'+"Administrative Officer :"+" "+ao[3]+'\n'+"Contact No :"+" "+co[3]+'\n'+"ICU Beds Available :"+" "+ib[3]+'\n'+"Ward Beds Available :"+" "+wb[3]+'\n'+"Location :"+" "+l4+'\n'+'\n'+"5) "+n[4]+'\n'+"Administrative Officer :"+" "+ao[4]+'\n'+"Contact No :"+" "+co[4]+'\n'+"ICU Beds Available :"+" "+ib[4]+'\n'+"Ward Beds Available :"+" "+wb[4]+'\n'+'\n'+"6) "+n[5]+'\n'+"Administrative Officer :"+" "+ao[5]+'\n'+"Contact No :"+" "+co[5]+'\n'+"ICU Beds Available :"+" "+ib[5]+'\n'+"Ward Beds Available :"+" "+wb[5]+'\n'+"Location :"+" "+l6+'\n'+'\n'+"7) "+n[6]+'\n'+"Administrative Officer :"+" "+ao[6]+'\n'+"Contact No :"+" "+co[6]+'\n'+"ICU Beds Available :"+" "+ib[6]+'\n'+"Ward Beds Available :"+" "+wb[6]
        return {
            "fulfillmentText": info
          }

    
if __name__ == '__main__':
    app.run(debug = True) 
