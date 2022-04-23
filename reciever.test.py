import unittest
import reciever
import os

class reciever_test(unittest.TestCase):
    data = "SOC,10 20 50 100 80 90 60 44 15 54 65 54 10 20 50 100 80 90 60 44 15 54 65 54 10 20 50 100 80 90 60 44 15 54 65 54 10 20 50 100 80 90 60 44 15 54 65 54 88 66\nTEMPERATURE,1 4 7 9 2 5 2 20 15 30 1 4 7 9 2 5 2 20 15 30 1 4 7 9 2 5 2 20 15 30 1 4 7 9 2 5 2 20 15 30 1 4 7 9 2 5 2 20 15 30"

    def test_split_data_from_sender(self):
        consoleData = "58.400000,300
29.000000,309.000000
29.000000,309.000000
43.000000,137.000000
34.000000,376.000000
43.000000,376.000000
33.000000,325.000000
27.000000,53.000000
48.000000,350.000000
59.000000,350.000000"

        soc_list,temp_list = reciever.split_data_from_sender(consoleData)
        self.assertEqual(soc_list, [58, 29, 29, 43, 34, 43, 33, 27, 48, 59])
        self.assertEqual(temp_list, [300, 309, 309, 137, 376, 376, 325, 53, 350, 350])
    
    def test_compute_statitics(self):
        soc_list,temp_list = reciever.split_data_from_sender(self.data)
        stats = reciever.compute_statitics(soc_list, temp_list, 3)
        self.assertEqual(stats.max_soc, 50)
        self.assertEqual(stats.min_soc, 10)
        self.assertEqual(stats.max_temp, 7)
        self.assertEqual(stats.min_temp, 1)
        self.assertEqual(stats.mov_avg_soc, 16.0)
        self.assertEqual(stats.mov_avg_temp, 2.4)
    
    def test_process_data_from_sender(self):
        stats = reciever.process_data_from_sender(self.data)
        self.assertEqual(stats.max_soc, 100)
        self.assertEqual(stats.min_soc, 10)
        self.assertEqual(stats.max_temp, 30)
        self.assertEqual(stats.min_temp, 1)
        self.assertEqual(stats.mov_avg_soc, 55.2)
        self.assertEqual(stats.mov_avg_temp, 8.8)
    
    


if __name__ == '__main__':
  #unittest.main()
