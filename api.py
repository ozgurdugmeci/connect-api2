import urllib3
import requests
import pandas as pd
import datetime 
import sys

date = datetime.date.today()

url1='http://www.xxxx.com.tr/rest1/auth/login/yyyy?pass=xxxx5@'
r = requests.get(url1)

a=r.json().get('data')

for x in a:
  token = (x['token'])
  print(token)


cvr='0'


timeStart= str(date)+'T00:00:00Z'
timeEnd=str(date)+'T24:00:00Z'


dummycvr=0

urly= 'http://xxxx/rest1/order2/getOrders?'

params = {'token' : token, 'OrderDateTimeStart' : timeStart  , 'OrderDateTimeEnd': timeEnd ,'start' : cvr }


r2 = requests.post(urly, params)

dongu= r2.json().get('summary')
dongu= dongu['totalRecordCount']
dongu=int(dongu)


liste=[]
orderno=[]
price=[]

id=-1 


while dummycvr < dongu :
 
 urly= 'http://xxxx/rest1/order2/getOrders?'
 params = {'token' : token, 'OrderDateTimeStart' : timeStart  , 'OrderDateTimeEnd': timeEnd ,'start' : cvr }

 r2 = requests.post(urly, params)
 a2= r2.json().get('data') 
 urunler= 0
 for item in a2:
  row=[]
 
 
  orderno.append(item['OrderCode'])
  detay=item['OrderDetails']  
 
  for x in detay:
    id=id+1
    #row.append(id)
    #row.append(item['OrderCode'])
    #row.append(item['OrderStatusId'])
    row.append(x['ProductCode'])
    row.append(x['ProductName'])
    row.append(x['Quantity'])
    urunler= int(x['Quantity'])+urunler
	#row.append(x['SellingPrice'])
    #row.append(x['SellingCurrency'])
    #row.append(x['SellingCurrencyExchangeRate'])
    liste.append(row)
    row=[]
    
 cvr= int(cvr)
 
 cvr=cvr+50
 dummycvr=cvr
 cvr=str(cvr)

 if len(liste)==0:
  print("heniz sipariş yok")
  quit() 
df= pd.DataFrame(liste, columns=['kod', 'urun adı', 'adet'])
grup= df.groupby(['kod','urun adı']).agg({'adet':sum})
print(grup.sort_values('adet', ascending=False).head(10))
print("Toplam sipariş sayısı", dongu)
print("Toplam satılan ürün adet", urunler)

input("Enter'a basıp çıkabilirsin")
