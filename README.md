# Steps cQube_Workflow Installation:

- Open Terminal

- Navigate to the directory where cQube_Workflow has been downloaded or cloned

  cd cQube_Workflow/work_deploy/

  git checkout release-2.0

- Copy the config.yml.template to config.yml cp config.yml.template config.yml

- Edit using nano config.yml

- Fill the configuration details for the below mentioned list in config.yml (* all the values are mandatory)

- cQube_Workflow installation process configuring the components in a sequence as mentioned below:

  - Configures Ansible
  - Configures Openjdk
  - Configures Python, pip and flask
  - Configures Postgresql
  - Configures NodeJS
  - Configures Angular and Chart JS
  - Configures Apache Nifi
  - Configures Keycloak
  - Configures Grafana
  - Configures Prometheus and node exporter


- Give the following permission to the install.sh file

  chmod u+x install.sh

- Install cQube using the non-root user with sudo privilege

- Configuration filled in config.yml will be validated first. If there is any error during validation, you will be prompted with the appropriate error message and the installation will be aborted. Refer the error message and solve the errors appropriately, then re-run the installation script sudo ./install.sh

- Start the installation by running install.sh shell script file as mentioned below:

  sudo ./install.sh

- Once installation is completed without any errors, you will be prompted the following message. CQube installed successfully!!

## Steps Post Installation:

### Steps to import Grafana dashboard

- Connect the VPN from local machine
Open https://<domain_name> from the browser and login with admin credentials
- Click on Admin Console
- Click on Monitoring details icon
- New tab will be loaded with grafana login page on http://<private_ip_of_cqube_server>:9000
- Default username is admin and password is admin
- Once your logged in change the password as per the need
- After logged in. Click on Settings icon from the left side menu.
- Click Data Sources
- Click on Add data source and select Prometheus
- In URL field, fill http://<private_ip_of_cqube_server>:9090 Optionally configure the other settings.
- Click on Save
- On home page, click on '+' symbol and select Import
- Click on Upload JSON file and select the json file which is located in git repository cQube/development/grafana/cQube_Monitoring_Dashboard.json and click Import
- Dashboard is succesfully imported to grafana with the name of cQube_Monitoring_Dashboard

## Uploading data to S3 Emission bucket:
- Create cqube_emission directory and place the data files as shown in file structure below inside the cqube_emission folder.

Master Files:
```
cqube_emission
|
├── block_master
│   └── block_mst.zip
│       └── block_mst.csv
├── cluster_master
│   └── cluster_mst.zip
│       └── cluster_mst.csv
├── district_master
│   └── district_mst.zip
│       └── district_mst.csv
├── school_master
│   └── school_mst.zip
│       └── school_mst.csv
├── pat
│   └── periodic_exam_mst.zip
│       └── periodic_exam_mst.csv
├── pat
│   └── periodic_exam_qst_mst.zip
│       └── periodic_exam_qst_mst.csv
├── diksha
│   └── diksha_tpd_mapping.zip
│       └── diksha_tpd_mapping.csv
├── diksha
│   └── diksha_api_progress_exhaust_batch_ids.zip
│       └── diksha_api_progress_exhaust_batch_ids.csv
├── sat
│   └── semester_exam_mst.zip
│       └── semester_exam_mst.csv
├── sat
│   └── semester_exam_qst_mst.zip
│       └── semester_exam_qst_mst.csv
├── sat
│   └── semester_exam_subject_details.zip
│       └── semester_exam_subject_details.csv
├── school_category
│   └── school_category_master.zip
│       └── school_category_master.csv
├── school_management
│   └── school_management_master.zip
│       └── school_management_master.csv
├── sat
│   └── semester_exam_subject_details.zip
│       └── semester_exam_subject_details.csv
├── sat
│   └── semester_exam_grade_details.zip
│       └── semester_exam_grade_details.csv
├── pat
│   └── periodic_exam_subject_details.zip
│       └── periodic_exam_subject_details.csv
├── pat
│   └── periodic_exam_grade_details.zip
│       └── periodic_exam_grade_details.csv
```

Transactional Files:
```
cqube_emission
|
├── student_attendance
│   └── student_attendance.zip
│       └── student_attendance.csv
├── teacher_attendance
│   └── teacher_attendance.zip
│       └── teacher_attendance.csv
├── user_location_master
│   └── user_location_master.zip
│       └── user_location_master.csv
├── inspection_master
│   └── inspection_master.zip
│       └── inspection_master.csv
├── infra_trans
│   └── infra_trans.zip
│       └── infra_trans.csv
├── diksha
│   └── diksha.zip
│       └── diksha.csv
├── pat
│   └── periodic_exam_result_trans.zip
│       └── periodic_exam_result_trans.csv
├── sat
│   └── semester_exam_result_trans.zip
│       └── semester_exam_result_trans.csv
```
- For udise data file structure, please refer the operational document.

- After creating the emission user, Update the emission user details mentioned below in cQube/development/python/client/config.py.

  - emission username
  - emission password
  - location of the cqube_emission directory where the files are placed as below. Example: /home/ubuntu/cqube_emission/
  - emission_url ( https://<domain_name>/data Note: URL depends upon the server configured in firewall which includes SSL and reverse proxy location)
- After completing the configuration. Save and close the file.

- Execute the client.py file located in cQube/development/python/client/ directory, as mentioned below to emit the data files to s3_emission bucket.

  python3 client.py
- Finally see the output in https://<domain_name>

# Upgradation:
### cQube_Base Upgradation:

- Open Terminal
- Navigate to the directory where cQube has been downloaded or cloned
cd cQube_Base/
 git checkout release-2.0
- Copy the upgradation_config.yml.template to upgradation_config.yml cp upgradation_config.yml.template upgradation_config.yml

- This script will update the below cQube components:

  - Creates & Updates table,sequence,index in postgresql database
  - Updates NodeJS server side code
  - Updates Angular and Chart JS client side code
  - Updates & configure Apache Nifi template
  - Updates & configure Keycloak
- Fill the configuration details in upgradation_config.yml (* all the values are mandatory, make sure to fill the same configuration details which were used during installation)

- Edit using nano upgradation_config.yml

- Save and Close the file

- Give the following permission to the upgrade.sh file

  chmod u+x upgrade.sh
- Run the script to update cQube using the non-root user with sudo privilege
Start the upgradation by running upgrade.sh shell script file as mentioned below:
  sudo ./upgrade.sh

Configuration filled in upgradation_config.yml will be validated first. If there is any error during validation, you will be prompted with the appropriate error message and the upgradation will be aborted. Refer the error message and solve the errors appropriately. Restart the upgradation processsudo ./upgrade.sh

Once upgradation is completed without any errors, you will be prompted the following message. CQube upgraded successfully!!

### cQube_Workflow Upgradation:

- Open Terminal
- Navigate to the directory where cQube has been downloaded or cloned
cd cQube_Workflow/work_deploy
 git checkout release-2.0
- Copy the upgradation_config.yml.template to upgradation_config.yml cp upgradation_config.yml.template upgradation_config.yml

- This script will update the below cQube components:

  - Creates & Updates table,sequence,index in postgresql database
  - Updates NodeJS server side code
  - Updates Angular and Chart JS client side code
  - Updates & configure Apache Nifi template
  - Updates & configure Keycloak
- Fill the configuration details in upgradation_config.yml (* all the values are mandatory, make sure to fill the same configuration details which were used during installation)

- Edit using nano upgradation_config.yml

- Save and Close the file

- Give the following permission to the upgrade.sh file

  chmod u+x upgrade.sh
- Run the script to update cQube using the non-root user with sudo privilege
Start the upgradation by running upgrade.sh shell script file as mentioned below:
  sudo ./upgrade.sh

Configuration filled in upgradation_config.yml will be validated first. If there is any error during validation, you will be prompted with the appropriate error message and the upgradation will be aborted. Refer the error message and solve the errors appropriately. Restart the upgradation processsudo ./upgrade.sh

Once upgradation is completed without any errors, you will be prompted the following message. CQube upgraded successfully!!
