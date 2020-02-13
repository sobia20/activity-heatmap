from flask import Flask, url_for
import json, os, requests
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='')
cors = CORS(app, resources={r"/*/*": {"origins": "*"}})


@app.route('/')
def index():
    """Display URL for Navigation to the json file data"""
    return 'Please visit /activities to find the activities.json file'


def get_json_data():
    """Retrieve JSON file data"""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "activities.json")
    data = json.load(open(json_url))
    return data


@app.route('/activities/', methods=['GET'])
def activities_all():
    """Retrieves all activity data"""
    data = get_json_data()
    return json.dumps(data)


def combine_for_api(t_m_pairs, count, name):
    """Combines the target-molecule pair with the activity count and max and average pchembl value"""
    i = 0
    for pair in t_m_pairs:
        pair[name] = count[i]
        i = i + 1
    return t_m_pairs


def make_t_m_pairs(name):
    """Form pairs of target and molecules and calculate the activity count and
max and average pchembl value according to the name parameter"""
    data = requests.get("http://localhost:5000/activities/").json()
    t_m_pairs = []
    count = []
    for i in data['activity']:
        if {'target': i['target_chembl_id'], 'molecule': i['molecule_chembl_id']} in t_m_pairs:
            ind = t_m_pairs.index({'target': i['target_chembl_id'], 'molecule': i['molecule_chembl_id']})
            if name == 'activity_count':
                count[ind] = count[ind] + 1
            if name == 'max_pchembl_value':
                count[ind] = max(float(count[ind]), float(i['pchembl_value']))
            if name == 'avg_pchembl_value':
                count[ind] = (float(count[ind]) + float(i['pchembl_value'])) / 2
        else:
            t_m_pairs.append({'target': i['target_chembl_id'], 'molecule': i['molecule_chembl_id']})
            if name == 'max_pchembl_value':
                count.append(i['pchembl_value'])
            if name == 'avg_pchembl_value':
                count.append(i['pchembl_value'])
            if name == 'activity_count':
                count.append(1)
    t_m_pairs = combine_for_api(t_m_pairs, count, name)

    return json.dumps(t_m_pairs)


@app.route('/activities/activity_count/', methods=['GET'])
def activities():
    """return activity count wrt target molecule pairs"""
    t_m_pairs = make_t_m_pairs('activity_count')
    return t_m_pairs


@app.route('/activities/max_pchembl_value/', methods=['GET'])
def max_pchembl_val():
    """return max pchembl value wrt target molecule pairs"""
    t_m_pairs = make_t_m_pairs('max_pchembl_value')
    return t_m_pairs


@app.route('/activities/avg_pchembl_value/', methods=['GET'])
def avg_pchembl_val():
    """return average pchembl value wrt target molecule pairs"""
    t_m_pairs = make_t_m_pairs('avg_pchembl_value')
    return t_m_pairs


if __name__ == '__main__':
    app.run(debug=True)
