# activity-heatmap API

This is a heatmap visualisation of activities data from the ChEMBL database. From the ChEMBL Web Services, activity data extracted into a JSON file for a list of targets given below.

Documentation for the Web Services is available here: 
https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services 
https://www.ebi.ac.uk/chembl/api/data/docs

A python client is also available here:
https://github.com/chembl/chembl_webresource_client

The JSON file extraction code is in backend/extract_activities.py.

Each activity returned relates a target (target_chembl_id) to an active molecule (molecule_chembl_id) through a pChEMBL value. Higher, pChEMBL values indicate more active molecules. 

The aim of the visualisation is to show activity count, maximum pChEMBL value and average pChEMBL value per target-molecule pair. 

The x-axis is the target_chembl_id and the y-axis is the molecule_chembl_id. On the click of each button, the connector list changes between activity count, maximum pChEMBL value and average pChEMBL value.

### Provided Lists

List of targets:
CHEMBL325
CHEMBL1937
CHEMBL1829
CHEMBL3524
CHEMBL2563
CHEMBL1865
CHEMBL2716
CHEMBL3192
CHEMBL4145
CHEMBL5103
CHEMBL3310

List of molecules:
CHEMBL98
CHEMBL99
CHEMBL27759
CHEMBL2018302
CHEMBL483254
CHEMBL1213490
CHEMBL356769
CHEMBL272980
CHEMBL430060
CHEMBL1173445
CHEMBL356066
CHEMBL1914702
## Run the project
```
docker-compose up
```
Visit localhost:8080/ to access the visualisation of heatmap and 10.5.0.5:5000/activities to access the json file data from the backend. To access all endpoints visit urls below,

Activity count url: 10.5.0.5:5000/activities/activity_count
Maximum pchembl value url: 10.5.0.5:5000/activities/max_pchembl_value
Average pchembl value url: 10.5.0.5:5000/activities/avg_pchembl_value


