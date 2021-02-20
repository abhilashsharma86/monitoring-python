
from time import time
import json
import Constants
import Helper
import Business


def monitor_server(server):
    print("MT: START of Monitoring of Server " + server[Constants.INPUT_SERVERS_LIST_ID] + " - " + str(time()))
    server_ip_file_name = Helper.generate_file_path(Constants.INPUT_FILES_LOCATION,
                                                    server[Constants.INPUT_SERVERS_LIST_SERVER_IP_JSON])

    server_monitor_result = 1

    with open(server_ip_file_name) as server_json_file:
        data_server = json.load(server_json_file)

        for monitoring_type in data_server[Constants.INPUT_ROOT_MONITOR]:

            monitoring_factory = Business.MonitoringFactory()
            monitor_object = monitoring_factory.create_monitor_domain(monitoring_type, data_server[Constants.INPUT_ROOT_MONITOR][monitoring_type])
            monitoring_result = monitor_object.process()

            if monitoring_result == 0:
                server_monitor_result = 0

    print("MT: RESULT of Monitoring of Server " + str(server_monitor_result))

    print("MT: START of Output Creation of Server")
    server_monitor_output_data = Helper.copy_data(data_server)
    server_op_file_name = Helper.generate_file_path(Constants.OUTPUT_FILES_LOCATION,
                                                    server[Constants.INPUT_SERVERS_LIST_SERVER_OP_JSON])
    Helper.generate_json_file(server_monitor_output_data, server_op_file_name)
    print("MT: END of Output Creation of Server")

    server[Constants.INPUT_SERVERS_LIST_SERVER_OUTPUT] = server_monitor_result

    print("MT: END of Monitoring of Server " + server[Constants.INPUT_SERVERS_LIST_ID] + " - " + str(time()))


if __name__ == "__main__":

    print("MT: START of Monitoring Library - " + str(time()))

    servers_ip_file_name = Helper.generate_file_path(Constants.INPUT_FILES_LOCATION, Constants.INPUT_SERVERS_LIST)

    with open(servers_ip_file_name) as servers_list_json_file:
        servers_data = json.load(servers_list_json_file)
        for server in servers_data[Constants.INPUT_SERVERS_LIST_SERVERS]:
            monitor_server(server)

    servers_output_data = servers_data.copy()
    servers_op_file_name = Helper.generate_file_path(Constants.OUTPUT_FILES_LOCATION, Constants.INPUT_SERVERS_LIST)
    Helper.generate_json_file(servers_output_data, servers_op_file_name)

    print("MT: END of Monitoring Library - " + str(time()))

