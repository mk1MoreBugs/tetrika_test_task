import csv
import unittest

from task2.solution import get_html_page, count_number_animals_on_page, save_data_in_csv


class TestTask2Solution(unittest.TestCase):
    def test__get_html_page__make_bad_request__return_none(self):
        html_page = get_html_page("bad_request")

        self.assertEqual(html_page, None)


    def test__count_number_animals_on_page__pass_none_page__return_empty_dict(self):
        next_page_tag_parent, number_animals_on_page = count_number_animals_on_page(None)

        self.assertEqual(next_page_tag_parent, None)
        self.assertEqual(len(number_animals_on_page), 0)


    def test__save_data_in_csv__create_csv_file_and_read_data(self):
        data_to_write = {"key": 1}

        save_data_in_csv(data_to_write)

        with open("beasts.csv") as csvfile:
            reader = csv.reader(csvfile)
            content = list(reader)[0]
            self.assertEqual(content[0],"key")
            self.assertEqual(int(content[1]), data_to_write["key"])


if __name__ == '__main__':
    unittest.main()
