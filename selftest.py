import unittest
import student_code as sc
import expand

dis_map0 = {'A': {'G': 10}, 'B': {'G': 8}, 'E': {'G': 7}, 'F': {'G': 4}, 'C': {'G': 5}, 'D': {'G': 3}, 'G': {'G': 0}}

time_map0 = {'A': {'B': 6, 'C': 8}, 'B': {'A': 6, 'D': 1, 'E': 2}, 'C': {'A': 8, 'G': 10}, 'D': {'B': 1, 'F': 6},
             'E': {'B': 2, 'F': 4}, 'F': {'D': 6, 'E': 4, 'G': 4}
    , 'G': {'F': 4, 'C': 10}}
time_map_extra = {
    'Campus': {'Campus': None, 'Whole_Food': 29, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Campus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 23, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Campus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Campus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Campus': 4, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 5,
                   'Ryan_Field': None, 'YWCA': 7},
    'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 7, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}

dis_map_extra = {
    'Campus': {'Campus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan_Field': 2, 'YWCA': 12},
    'Whole_Food': {'Campus': 3, 'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan_Field': 5, 'YWCA': 8},
    'Beach': {'Campus': 5, 'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan_Field': 7, 'YWCA': 12},
    'Cinema': {'Campus': 5, 'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan_Field': 7, 'YWCA': 2},
    'Lighthouse': {'Campus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 0, 'Ryan_Field': 1, 'YWCA': 15},
    'Ryan_Field': {'Campus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 5, 'Lighthouse': 1, 'Ryan_Field': 0, 'YWCA': 12},
    'YWCA': {'Campus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 7, 'Lighthouse': 15, 'Ryan_Field': 12, 'YWCA': 0}}

time_map_extra_Z = {
    'Zampus': {'Zampus': None, 'Whole_Food': 29, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Zampus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 23, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Zampus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Zampus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Zampus': 4, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Zampus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 5,
                   'Ryan_Field': None, 'YWCA': 7},
    'YWCA': {'Zampus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 7, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}

dis_map_extra_Z = {
    'Zampus': {'Zampus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan_Field': 2, 'YWCA': 12},
    'Whole_Food': {'Zampus': 3, 'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan_Field': 5, 'YWCA': 8},
    'Beach': {'Zampus': 5, 'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan_Field': 7, 'YWCA': 12},
    'Cinema': {'Zampus': 5, 'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan_Field': 7, 'YWCA': 2},
    'Lighthouse': {'Zampus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 0, 'Ryan_Field': 1, 'YWCA': 15},
    'Ryan_Field': {'Zampus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 5, 'Lighthouse': 1, 'Ryan_Field': 0, 'YWCA': 12},
    'YWCA': {'Zampus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 7, 'Lighthouse': 15, 'Ryan_Field': 12, 'YWCA': 0}}

dis_map = {
    'Campus': {'Campus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan_Field': 2, 'YWCA': 12},
    'Whole_Food': {'Campus': 3, 'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan_Field': 5, 'YWCA': 8},
    'Beach': {'Campus': 5, 'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan_Field': 7, 'YWCA': 12},
    'Cinema': {'Campus': 5, 'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan_Field': 7, 'YWCA': 2},
    'Lighthouse': {'Campus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 7, 'Lighthouse': 0, 'Ryan_Field': 1, 'YWCA': 15},
    'Ryan_Field': {'Campus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 7, 'Lighthouse': 1, 'Ryan_Field': 0, 'YWCA': 12},
    'YWCA': {'Campus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 2, 'Lighthouse': 15, 'Ryan_Field': 12, 'YWCA': 0}}

time_map1 = {
    'Campus': {'Campus': None, 'Whole_Food': 14, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Campus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 13, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Campus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Campus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Campus': 11, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 12,
                   'Ryan_Field': None, 'YWCA': 15},
    'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 13, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}
time_map2 = {
    'Campus': {'Campus': None, 'Whole_Food': 28, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Campus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 13, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Campus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Campus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Campus': 11, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 12,
                   'Ryan_Field': None, 'YWCA': 15},
    'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 13, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}
time_map3 = {
    'Campus': {'Campus': None, 'Whole_Food': 22, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Campus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 13, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Campus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Campus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Campus': 11, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 12,
                   'Ryan_Field': None, 'YWCA': 17},
    'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 15, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}
time_map4 = {
    'Campus': {'Campus': None, 'Whole_Food': 29, 'Beach': 13, 'Cinema': None, 'Lighthouse': 11, 'Ryan_Field': None,
               'YWCA': None},
    'Whole_Food': {'Campus': 14, 'Whole_Food': None, 'Beach': 14, 'Cinema': 23, 'Lighthouse': None, 'Ryan_Field': None,
                   'YWCA': None},
    'Beach': {'Campus': 14, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
              'YWCA': None},
    'Cinema': {'Campus': None, 'Whole_Food': 14, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan_Field': None,
               'YWCA': 12},
    'Lighthouse': {'Campus': 11, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None,
                   'Ryan_Field': 11, 'YWCA': None},
    'Ryan_Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 12,
                   'Ryan_Field': None, 'YWCA': 16},
    'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 10, 'Lighthouse': None, 'Ryan_Field': 15,
             'YWCA': None}}


class SearchTest(unittest.TestCase):

    def test1(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map, time_map1, 'Campus', 'Cinema')
        self.assertEqual(path, ['Campus', 'Whole_Food', 'Cinema'])
        self.assertEqual(expand.expand_count, 4)

    def test2(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map, time_map2, 'Campus', 'Cinema')
        self.assertEqual(path, ['Campus', 'Beach', 'Whole_Food', 'Cinema'])
        self.assertEqual(expand.expand_count, 6)

    def test3(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map, time_map3, 'Campus', 'Cinema')
        self.assertEqual(path, ['Campus', 'Whole_Food', 'Cinema'])
        self.assertEqual(expand.expand_count, 5)

    def test4(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map, time_map4, 'Campus', 'Cinema')
        self.assertEqual(path, ['Campus', 'Lighthouse', 'Ryan_Field', 'YWCA', 'Cinema'])
        self.assertEqual(expand.expand_count, 6)

    def test5(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map, time_map1, 'Ryan_Field', 'Beach')
        self.assertEqual(path, ['Ryan_Field', 'Lighthouse', 'Campus', 'Beach'])
        self.assertEqual(expand.expand_count, 4)

    def test6(self):
        expand.expand_count = 0
        path = sc.a_star_search(dis_map0, time_map0, 'A', 'G')
        self.assertEqual(path, ['A', 'B', 'E', 'F', 'G'])
        self.assertEqual(expand.expand_count, 6)
        print(path)

    def test7(self):
        expand.expand_count = 0;
        path = sc.a_star_search(dis_map_extra, time_map_extra, 'Ryan_Field', 'Cinema')
        print(path)
        print(expand.expand_count)
        self.assertEqual(path, ['Ryan_Field', 'YWCA', 'Cinema'])
        self.assertEqual(expand.expand_count, 4)

    def test8(self):
        expand.expand_count = 0;
        path = sc.a_star_search(dis_map_extra_Z, time_map_extra_Z, 'Ryan_Field', 'Cinema')
        print(path)
        print(expand.expand_count)
        self.assertEqual(path, ['Ryan_Field', 'YWCA', 'Cinema'])
        self.assertEqual(expand.expand_count, 3)


if __name__ == "__main__": unittest.main()