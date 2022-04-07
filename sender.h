#include <string>
#include <iostream> 
using namespace std;

#define MAX_CURRENT 60
#define MIN_CURRENT 1 
#define MAX_TEMPERATURE 400
#define MIN_TEMPERATURE 30

float generateRandomSimulatedData(int max_value, int min_value, unsigned seed);
string formatdataToCVN(float currentsample, float temperature);
bool streamOnConsole(string DataTobeStreamed);
bool GetdataAndStreamOnCOnsole(unsigned noOfSamplesTobeRead);
