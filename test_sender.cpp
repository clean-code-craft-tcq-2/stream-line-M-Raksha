#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include "sender.h"


// test random generator

TEST_CASE("Genearte Random data")
{
    float random_Data[30];
    int seed;
    for(seed=0;seed<30;seed++)
    {
        
      random_Data[seed] = generateRandomSimulatedData(MAX_CURRENT,MIN_CURRENT,seed);
      REQUIRE(random_Data[seed] != 0);
      
    }

}
 //test data format in CVN   
TEST_CASE("format data to cvn")
{

    float cuurentSample = 34;
    float temperature = 80;
    REQUIRE(formatdataToCVN(cuurentSample,temperature) == "34.000000,80.000000");
}

 //test streaming data on console
TEST_CASE("stream data on console")
{
    string DataTobeStreamed = to_string(58.4)+","+to_string(300);
    REQUIRE(streamOnConsole(DataTobeStreamed)== true);
}

//get currentValueand temperature from random generator and stream on console
TEST_CASE("get data and stream on console")
{
    unsigned noOfSamplesTobeRead = 50;
    REQUIRE(GetdataAndStreamOnCOnsole(noOfSamplesTobeRead)== true);
}
