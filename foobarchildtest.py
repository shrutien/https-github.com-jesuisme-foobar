from foobarchild import FoobarChild
import unittest


class FoobarChildTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_data(self):
        childobject = FoobarChild()
        childobject.read_data()
        self.assertGreater(len(childobject.student_list), 0)
        self.assertTrue(childobject.card_labels, [['A1', 'A2', 'A4', 'A3']])
        self.assertTrue(childobject.email_list, [['test@test.com']])
        # self.assertIn(child.card_labels,[['A1', 'A2', 'A4', 'A3'], ['A1', 'A2', 'A4', 'A3', 'A5'], ['A5', 'A2', 'A4', 'A3', 'A1'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'], ['A5', 'A4', 'A3', 'A2', 'A1'], ['A1', 'A2', 'A3', 'A4', 'A5'], ['A1', 'A3', 'A2', 'A5', 'A4'], ['A1', 'A2', 'A3', 'A5'], ['A1', 'A2', 'A4', 'A3', 'A5'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'], ['A4'], ['A1', 'A2', 'A4', 'A3', 'A5'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'], ['A1', 'A2', 'A4', 'A3', 'A5'], ['A1', 'A6', 'A4', 'A3', 'A5']])
        # self.assertEquals(child.read_data(child.card_labels,child.emails),[['A1','A2']],[['test@test.com']])

    def test_compute_score(self):
        childobject = FoobarChild()
        self.assertTrue('abcde', childobject.transform_card_order_to_string(['A1', 'A2', 'A3', 'A4', 'A5']))
        self.assertTrue(5, childobject.levenshtein_score(['A1', 'A6', 'A4', 'A3', 'A5']))

    def test_standard_deviation(self):
        childobject = FoobarChild()
        # self.assertTrue(12.170221268090637,childobject.standard_deviation([4, 4, -2, 28, -8, 16, 4, 10, 4, 28, -8, 4, 28, 4, -2]))
        # self.assertEqual(12.170221268090637,childobject.scores([148.15]))
        # self.assertEqual(12.170221268090637,childobject.standard_deviation())


if __name__ == '__main__':
    unittest.main()
