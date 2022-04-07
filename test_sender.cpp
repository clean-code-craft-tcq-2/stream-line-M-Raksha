#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include "sender.h"


// test random generator
    float random_Data[30];
    int seed;
    for(seed=0;seed<30;seed++)
    {
        
      random_Data[i] = generateRandomSimulatedData(MAX_CURRENT,MIN_CURRENT,seed);
      REQUIRE(random_Data[i] != 0);
      
    }


     
