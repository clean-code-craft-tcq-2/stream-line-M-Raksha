import unittest
import reciever
import os

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
59.000000,350.000000
9.000000,149.000000
47.000000,398.000000
41.000000,147.000000
58.000000,219.000000
49.000000,83.000000
49.000000,48.000000
27.000000,98.000000
44.000000,308.000000
38.000000,125.000000
57.000000,316.000000
45.000000,357.000000
48.000000,174.000000
19.000000,202.000000
1.000000,274.000000
42.000000,269.000000
45.000000,336.000000
56.000000,308.000000
47.000000,355.000000
49.000000,100.000000
27.000000,200.000000
16.000000,51.000000
23.000000,186.000000
34.000000,109.000000
3.000000,221.000000
29.000000,138.000000
28.000000,270.000000
28.000000,254.000000
19.000000,188.000000
30.000000,69.000000
31.000000,56.000000
1.000000,400.000000
50.000000,234.000000
48.000000,263.000000
49.000000,124.000000
24.000000,289.000000
36.000000,367.000000
35.000000,107.000000
48.000000,217.000000
27.000000,208.000000
12.000000,247.000000"""
    
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
    
    '''def test_process_data_from_sender(self):
        stats = reciever.process_data_from_sender(self.consoleData)
        self.assertEqual(stats.max_soc, 59)
        self.assertEqual(stats.min_soc, 27)
        self.assertEqual(stats.max_temp, 376)
        self.assertEqual(stats.min_temp, 53)
        #self.assertEqual(stats.mov_avg_soc, 55.2)
        #self.assertEqual(stats.mov_avg_temp, 8.8)'''
    
    


if __name__ == '__main__':
  unittest.main()
