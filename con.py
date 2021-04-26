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
        n=[]
        ao=[]
        co=[]
        ib=[]
        wb=[]
        for data in sp.find_all('tr')[26:29]:
            for d in data.find_all('td')[2]:
                n.append(d)
        for data in sp.find_all('tr')[26:29]:
            for d in data.find_all('td')[4]:
                ao.append(d)
        for data in sp.find_all('tr')[26:29]:
            for d in data.find_all('td')[5]:
                co.append(d)
        for data in sp.find_all('tr')[26:29]:
            for d in data.find_all('td')[7]:
                ib.append(d)
        for data in sp.find_all('tr')[26:29]:
            for d in data.find_all('td')[10]:
                wb.append(d)
        info="1) "+n[0]+'\n'+"Administrative Officer :"+" "+ao[0]+'\n'+"Contact No :"+" "+co[0]+'\n'+"ICU Beds Available :"+" "+ib[0]+'\n'+"Ward Beds Available :"+" "+wb[0]+'\n'+'\n'+"2) "+n[1]+'\n'+"Administrative Officer :"+" "+ao[1]+'\n'+"Contact No :"+" "+co[1]+'\n'+"ICU Beds Available :"+" "+ib[1]+'\n'+"Ward Beds Available :"+" "+wb[1]+'\n'+'\n'+"3) "+n[2]+'\n'+"Administrative Officer :"+" "+ao[2]+'\n'+"Contact No :"+" "+co[2]+'\n'+"ICU Beds Available :"+" "+ib[2]+'\n'+"Ward Beds Available :"+" "+wb[2]
        return {
            "fulfillmentText": info
          }

    
if __name__ == '__main__':
    app.run(debug = True) 
