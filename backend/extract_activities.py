from chembl_webresource_client.new_client import new_client
import json

targets = ['CHEMBL325',
'CHEMBL1937',
'CHEMBL1829',
'CHEMBL3524',
'CHEMBL2563',
'CHEMBL1865',
'CHEMBL2716',
'CHEMBL3192',
'CHEMBL4145',
'CHEMBL5103',
'CHEMBL3310']

molecules = ['CHEMBL98',
'CHEMBL99',
'CHEMBL27759',
'CHEMBL2018302',
'CHEMBL483254',
'CHEMBL1213490',
'CHEMBL356769',
'CHEMBL272980',
'CHEMBL430060',
'CHEMBL1173445',
'CHEMBL356066',
'CHEMBL1914702']
new_client.activity.set_format('json')
with open('./static/data/activities.json', 'w') as f: 
    f.write('{"activity":[')
    for t in targets:
        activities = new_client.activity.filter(target_chembl_id=t, molecule_chembl_id__in=molecules, pchembl_value__isnull=False)
        for a in activities:
            json.dump(a, f)
            f.write(",")
    f.write(']}')
f.close()
