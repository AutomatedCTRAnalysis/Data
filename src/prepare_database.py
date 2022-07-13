from ast import keyword
import os
import json
from collections import defaultdict

root_folder = '../data/'
folder_names = ['enterprise-intrusion-set', 'ics-intrusion-set']

dataset = defaultdict(lambda: defaultdict(list))

for folder_name in folder_names: 

    folder = os.path.join(root_folder, folder_name)

    for filename in os.listdir(folder): 
        if filename.endswith('.json'):
            with open(os.path.join(folder, filename)) as file:
                file_json = json.load(file)["objects"][0] 
                
                # retrieve information:
                apt_group = []
                urls = []
                mitre_domain = file_json['x_mitre_domains']
                description = file_json["description"]

                if 'aliases' in file_json:
                    apt_group.extend(file_json['aliases']) 
               
                apt_group.append(file_json['name'])

                for ref in file_json['external_references'][1:]:
                    if 'url' in ref: # check if source has url 
                        url = ref['url'] # retrieve url 
                        urls.append(url)
                
                dataset[apt_group]['urls'].append(urls)
                dataset[apt_group]['mitre_domain'].append(mitre_domain)
                dataset[apt_group]['description'].append(description)

name = 'APT_group_dataset'
pd.DataFrame(dataset.values()).to_csv(name+'.csv')
with open(name+'.json', 'w') as file:
    json.dump(dataset, file, indent=4)
                
