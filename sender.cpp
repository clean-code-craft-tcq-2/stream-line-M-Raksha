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
