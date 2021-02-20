
import abc
import Constants
import Helper
from time import time


class Monitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def business_logic(self, *args):
        pass

    @abc.abstractmethod
    def process(self, data):
        pass


class Logs(Monitor):

    def __init__(self, data):
        self.data = data

    def __business_logic_monitor_log(self, file_name, text_to_search):
        f = open(file_name, "r")
        for x in f:
            if x.startswith(text_to_search):
                return 1
        f.close()
        return 0

    def business_logic(self, *args):
        return self.__business_logic_monitor_log(args[0], args[1])

    def process(self):

        print("MT: START of LOGS Monitoring - " + str(time()))
        logs_monitor_result = 1

        for log_to_monitor in self.data:
            log_file = Helper.generate_file_path(log_to_monitor[Constants.MONITOR_LOGS_FILE_LOCATION],
                                                 log_to_monitor[Constants.MONITOR_LOGS_FILE_NAME])

            print("MT: START Log File " + log_file)

            log_monitor_result = self.business_logic(log_file, log_to_monitor[Constants.MONITOR_LOGS_SEARCH_STRING])

            print(log_monitor_result)

            log_to_monitor[Constants.MONITOR_LOGS_OUTPUT] = log_monitor_result

            print("MT: END Log File " + log_file)

            if log_monitor_result == 0:
                logs_monitor_result = 0

        print("MT: END of LOGS Monitoring - " + str(time()))
        return logs_monitor_result


class Other(Monitor):

    def __init__(self, data):
        self.data = data

    def business_logic(self, *args):
        pass

    def process(self):
        print("MT: START of OTHER Monitoring - " + str(time()))
        print("MT: END of OTHER Monitoring - " + str(time()))
        return 1


class MonitoringFactory:
    def create_monitor_domain(self, type, data):
        if type == Constants.MONITOR_LOGS:
            return Logs(data)
        if type == Constants.MONITOR_OTHER:
            return Other(data)
