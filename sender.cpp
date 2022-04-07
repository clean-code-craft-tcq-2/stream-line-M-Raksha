#include "sender.h"

float generateRandomSimulatedData(int max_value, int min_value, unsigned seed)
{
    
    srand(seed);
  
    float data = (rand() % (int)(max_value+1)) ;
    if(data < min_value)
  {
    data = data + min_value;
  }
   return data;
}


string formatdataToCVN(float currentsample, float temperature)
{
    string dataToCVN = to_string(currentsample)+","+to_string(temperature);
    return dataToCVN;
}

bool streamOnConsole(string DataTobeStreamed)
{
    bool DatastreamingSuccess = true;
    cout<<DataTobeStreamed<<endl;
    return DatastreamingSuccess;
}

bool GetdataAndStreamOnCOnsole(unsigned noOfSamplesTobeRead)
{
    unsigned loopCounter;
    float currentValue;
    float temperature;
    string formatttedData;
    bool retVal;
    for(loopCounter =0; loopCounter< noOfSamplesTobeRead; loopCounter++)
    {
       currentValue = generateRandomSimulatedData(MAX_CURRENT,MIN_CURRENT,loopCounter);
       temperature = generateRandomSimulatedData(MAX_TEMPERATURE,MIN_TEMPERATURE,loopCounter);
       formatttedData = formatdataToCVN(currentValue,temperature);
       retVal=streamOnConsole(formatttedData);
    }
    
    return retVal;
}
