from deploy_nifi import rq, prop, logging, sys
from connect_nifi_processors import get_processor_group_ports
import requests


def nifi_update_processor_property(processor_group_name, processor_name, properties):
    """[Update the processor property in the processor group]
    Args:
        processor_group_name ([string]): [provide the processor group name]
        processor_name ([string]): [provide the processor name]
        properties([dict]): [property to update in processor]
    """
    
    # Get the processors in the processor group
    pg_source = get_processor_group_ports(processor_group_name)
    if pg_source.status_code == 200:
        for i in pg_source.json()['processGroupFlow']['flow']['processors']:
            # Get the required processor details
            if i['component']['name'] == processor_name:
                # Request body creation to update processor property.
                update_processor_property_body = {
                    "component": {
                        "id": i['component']['id'],
                        "name": i['component']['name'],
                        "config": {
                            "properties": {
                                "five_days_before": properties['from_date'],
                                "yesterday": properties['to_date']
                            }
                        }
                    },
                    "revision": {
                        "clientId": "python code: update_processor_property.py",
                        "version": i['revision']['version']
                    },
                    "disconnectedNodeAcknowledged": "False"
                }
                # API call to update the processor property
                update_processor_res = requests.put(
                    f"{prop.NIFI_IP}:{prop.NIFI_PORT}/nifi-api/processors/{i['component']['id']}", json=update_processor_property_body)
                if update_processor_res.status_code == 200:
                    logging.info(
                        f"Successfully updated the properties: {properties} in {i['component']['name']} processor")
                    return True

                else:
                    return update_processor_res.text


if __name__ == '__main__':
    """[summary]
    sys arguments = 1.Processor group name. 2.From date 3. To date
    Updates the summary rollup start date and end date in nifi processor property.
    Updates the summary rollup start date and end date in nifi processor property to default values.
    Note:
    Default Date Range[Diksha summary-rollup] - Day before yesterday.

    syntax: python update_processor_property.py <processor group name> <yyyy-mm-dd> <yyyy-mm-dd>
            Example: python update_processor_property.py diksha_transformer 2021-10-22 2021-10-23
                     python update_processor_property.py diksha_transformer default
    """
    
    diksha_summary_rollup_processor_name = "diksha_api_summary_rollup_update_date_token"
    processor_group_name = sys.argv[1]

    # Default Date Range[Diksha summary-rollup] - Day before yesterday
    processor_properties = {
        "from_date": "${now():toNumber():minus(172800000):format('yyyy-MM-dd')}",
        "to_date": "${now():toNumber():minus(172800000):format('yyyy-MM-dd')}"
    }
    if len(sys.argv) == 3:
        # update processor property.
        nifi_update_processor_property(
            processor_group_name, diksha_summary_rollup_processor_name, processor_properties)

    elif len(sys.argv) == 4:
        processor_properties["from_date"] = sys.argv[2]
        processor_properties["to_date"] = sys.argv[3]

        # update processor property.
        nifi_update_processor_property(
            processor_group_name, diksha_summary_rollup_processor_name, processor_properties)