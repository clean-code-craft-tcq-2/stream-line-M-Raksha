#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"

// test random generator
    float random_Data[30];
    for(int i = 0;i<30;i++)
    {
        
      random_Data[i] = generateRandomSimulatedData(MAX_CURRENT,MIN_CURRENT,i);
      REQUIRE(random_Data[i] != 0);
      
    }


     
