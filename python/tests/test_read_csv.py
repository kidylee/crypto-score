import unittest
import os
import csv

from src.app import read_csv_file


class TestReadCsvFile(unittest.TestCase):

    def tearDown(self):
        for file_path in ["empty_file.csv", "one_record.csv", "multiple_records.csv"]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            list(read_csv_file("nonexistent_file.csv"))

    def test_empty_file(self):
        file_path = "empty_file.csv"
        with open(file_path, "w") as f:
            pass
        self.assertEqual(list(read_csv_file(file_path)), [])

    def test_file_with_one_record(self):
        file_path = "one_record.csv"
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["John", "Doe", "30"])
        self.assertEqual(list(read_csv_file(file_path)), [["John", "Doe", "30"]])

    def test_file_with_multiple_records(self):
        file_path = "multiple_records.csv"
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["John", "Doe", "30"])
            writer.writerow(["Jane", "Doe", "28"])
            writer.writerow(["Bob", "Smith", "40"])
        self.assertEqual(list(read_csv_file(file_path)),
                         [["John", "Doe", "30"], ["Jane", "Doe", "28"], ["Bob", "Smith", "40"]])


if __name__ == '__main__':
    unittest.main()
