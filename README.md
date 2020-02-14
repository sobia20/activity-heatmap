# Activity-Heatmap API

This is a heatmap visualisation of activities data from the ChEMBL database. From the ChEMBL Web Services, activity data extracted into a JSON file for a list of targets given below.

![screen_gif](https://i.imgur.com/tGLmfqR.gif)

Documentation for the Web Services is available here: 
https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services 
https://www.ebi.ac.uk/chembl/api/data/docs

A python client is also available here:
https://github.com/chembl/chembl_webresource_client

The JSON file extraction code is in `backend/extract_activities.py`.

Each activity returned relates a target (`target_chembl_id`) to an active molecule (`molecule_chembl_id`) through a `pChEMBL value`. Higher, `pChEMBL values` indicate more active molecules. 

The aim of the visualisation is to show `activity count`, `maximum pChEMBL value` and `average pChEMBL value` per target-molecule pair. 

The x-axis is the `target_chembl_id` and the y-axis is the `molecule_chembl_id`. On the click of each button, the connector list changes between `activity count`, `maximum pChEMBL value` and `average pChEMBL value`.

### Provided Lists

* <b>List of targets:</b><br>
CHEMBL325<br>
CHEMBL1937<br>
CHEMBL1829<br>
CHEMBL3524<br>
CHEMBL2563<br>
CHEMBL1865<br>
CHEMBL2716<br>
CHEMBL3192<br>
CHEMBL4145<br>
CHEMBL5103<br>
CHEMBL3310<br>

* <b>List of molecules:</b><br>
CHEMBL98<br>
CHEMBL99<br>
CHEMBL27759<br>
CHEMBL2018302<br>
CHEMBL483254<br>
CHEMBL1213490<br>
CHEMBL356769<br>
CHEMBL272980<br>
CHEMBL430060<br>
CHEMBL1173445<br>
CHEMBL356066<br>
CHEMBL1914702<br>

## Run the project
```
docker-compose up
```
Visit <i>`localhost:8080/`</i> to access the visualisation of heatmap and <i>`localhost:5000/activities`</i> to access the json file data from the backend. To access all endpoints visit urls below,

* <b>Activity count url:</b> <br>
<i>`localhost:5000/activities/activity_count`</i>

* <b>Maximum pchembl value url: </b><br>
<i>`localhost:5000/activities/max_pchembl_value`</i>

* <b>Average pchembl value url:</b> <br>
<i>`localhost:5000/activities/avg_pchembl_value`</i>


