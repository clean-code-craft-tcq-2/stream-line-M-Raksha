import unittest
import reciever
import os

for x in range(50):
    print("58.400000,300")

    
class reciever_test(unittest.TestCase):
    consoleData = """58.400000,300
29.000000,309.000000
29.000000,309.000000
43.000000,137.000000
34.000000,376.000000
43.000000,376.000000
33.000000,325.000000
27.000000,53.000000
48.000000,350.000000
59.000000,350.000000"""
    
    def test_get_data_from_sender(self):
        textRead = get_data_from_sender()
        print("Receiver Data Received")
        print(textRead)
        readingsLen = len(list(textRead.split("\n")))
        self.assertTrue(readingsLen>0)
        
    def test_split_data_from_sender(self):
        soc_list,temp_list = reciever.split_data_from_sender(self.consoleData)
        self.assertEqual(soc_list, [58, 29, 29, 43, 34, 43, 33, 27, 48, 59])
        self.assertEqual(temp_list, [300, 309, 309, 137, 376, 376, 325, 53, 350, 350])
    
    def test_compute_statitics(self):
        soc_list,temp_list = reciever.split_data_from_sender(self.consoleData)
        stats = reciever.compute_statitics(soc_list, temp_list, 3)
        self.assertEqual(stats.max_soc, 58)
        self.assertEqual(stats.min_soc, 29)
        self.assertEqual(stats.max_temp, 309)
        self.assertEqual(stats.min_temp, 300)
        self.assertEqual(stats.mov_avg_soc, 23.2)
        self.assertEqual(stats.mov_avg_temp, 183.6)
    
    def test_process_data_from_sender(self):
        stats = reciever.process_data_from_sender(self.consoleData)
        self.assertEqual(stats.max_soc, 58)
        self.assertEqual(stats.min_soc, 27)
        self.assertEqual(stats.max_temp, 376)
        self.assertEqual(stats.min_temp, 53)
        self.assertEqual(stats.mov_avg_soc, 37)
        self.assertEqual(stats.mov_avg_temp, 296)
    
    


if __name__ == '__main__':
  unittest.main()
