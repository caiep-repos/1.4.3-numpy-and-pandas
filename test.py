import unittest
import pandas as pd
from assignment import create_dataframe, select_young_people, calculate_average_age

class TestPandas(unittest.TestCase):
    def setUp(self):
        self.data = {
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'age': [25, 32, 28, 45, 29]
        }
        self.df = pd.DataFrame(self.data)

    def test_create_dataframe(self):
        df = create_dataframe(self.data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape, (5, 2))

    def test_select_young_people(self):
        young_people_df = select_young_people(self.df)
        self.assertEqual(young_people_df.shape, (3, 2))
        self.assertTrue(all(young_people_df['age'] < 30))

    def test_calculate_average_age(self):
        avg_age = calculate_average_age(self.df)
        self.assertAlmostEqual(avg_age, 31.8)

if __name__ == '__main__':
    unittest.main()
