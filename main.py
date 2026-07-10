import json,random
lang=json.load(open('language/persian.json',encoding='utf8'))
mem=json.load(open('memory/user.json',encoding='utf8'))
print('RAMTIN AI آماده است. exit برای خروج')
while True:
 x=input('تو: ')
 if x=='exit': break
 if 'اسم من' in x:
  mem['name']=x.replace('اسم من','').strip()
  json.dump(mem,open('memory/user.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
  print('AI: خوشحالم که شناختمت')
  continue
 ans=None
 for k,v in lang.items():
  if k in x: ans=random.choice(v)
 if ans is None: ans='جالب است، بیشتر توضیح بده'
 if 'name' in mem: ans=ans+' '+mem['name']
 print('AI:',ans)
