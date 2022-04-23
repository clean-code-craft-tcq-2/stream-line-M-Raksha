import sys

class statistics:
    max_soc, min_soc, max_temp, min_temp, mov_avg_soc, mov_avg_temp = 0, 0, 0, 0, 0, 0

# get the data streamed  on console by the sensor/sender
def get_data_from_sender():
    data = sys.stdin.read() # read console data
    return data

def split_data_from_sender(data):
    
    # create a list of sensor data set read from the console
    dataSet_list = data.split('\n')
    
    # get only 50 sample of sensor data set
    dataSet_list = dataSet_list[0:50]
    
    # loop each data set of sensor data set list
    batteryCurrent_list = []
    batteryTemperature_list = []
    for dataSet in dataSet_list: 
        BatteryParameter_list = dataSet.split(',')
        batteryCurrent_list.append(BatteryParameter_list[0])
        batteryTemperature_list.append(BatteryParameter_list[1])
    
    # converting str in int
    batteryCurrent_list, batteryTemperature_list = list(map(int, batteryCurrent_list)), list(map(int, batteryTemperature_list))
    print("batteryCurrent_list = ", batteryCurrent_list, "batteryTemperature_list = ", batteryTemperature_list)
    
    return batteryCurrent_list, batteryTemperature_list


def compute_statitics(soc_list, temp_list, index):
    stats = statistics()
    stats.max_soc = max(soc_list[0:index])
    stats.min_soc = min(soc_list[0:index])
    stats.max_temp = max(temp_list[0:index])
    stats.min_temp = min(temp_list[0:index])
    stats.mov_avg_soc = round(sum(soc_list[0:index][-5:])/5,2)
    stats.mov_avg_temp = round(sum(temp_list[0:index][-5:])/5,2)
    return stats

def process_data_from_sender(data):
    soc_list,temp_list = split_data_from_sender(data)
    for index in range(1,50):
        stats = compute_statitics(soc_list, temp_list, index)
        print ("Soc :{}\tTemp:{}\tMax Soc:{}\tMin Soc:{}\tMax Temp:{}\tMin Temp:{}\tMoving Avg Soc:{}\tMoving Avg Temp:{}".format(soc_list[index], temp_list[index],stats.max_soc, stats.min_soc, stats.max_temp, stats.min_temp, stats.mov_avg_soc, stats.mov_avg_temp))
    return stats

if __name__ == '__main__':
    data = get_data_from_sender()
    print("data recieved from sender\n", data)
    process_data_from_sender(data)
