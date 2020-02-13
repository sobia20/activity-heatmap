from chembl_webresource_client.new_client import new_client
import json


def extract_json():
    """Extracts JSON data from the ChEMBL database using their Web Services and put it in a file"""

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
    list_of_activities = []
    print('Fetching activity data from ChEMBL database to a json file')
    for target in targets:
        activities = new_client.activity.filter(target_chembl_id=target, molecule_chembl_id__in=molecules,
                                                pchembl_value__isnull=False)
        list_of_activities = list_of_activities + list(activities)
    activities_dict = {"activity": list_of_activities}
    f = open('./static/data/activities.json', 'w')
    f.write(json.dumps(activities_dict))
    f.close()
    print('Successfully fetched data for targets and molecules in ./static/data/activities.json')


if __name__ == '__main__':
    extract_json()
