import unittest
from unittest.mock import patch
from datetime import date
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager


class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.rm = RelationsManager()

        self.e1 = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                           birth_date=date(1970, 1, 31), hire_date=date(1990, 10, 1))

        self.e2 = Employee(id=2, first_name="Myrta", last_name="Torkelson", base_salary=1000,
                           birth_date=date(1980, 1, 1), hire_date=date(2000, 1, 1))

        self.e3 = Employee(id=3, first_name="Jettie", last_name="Lynch", base_salary=1500,
                           birth_date=date(1987, 1, 1), hire_date=date(2015, 1, 1))

        self.e4 = Employee(id=4, first_name="Gretchen", last_name="Watford", base_salary=4000,
                           birth_date=date(1960, 1, 1), hire_date=date(1990, 1, 1))

        self.e5 = Employee(id=5, first_name="Tomas", last_name="Andre", base_salary=1600,
                           birth_date=date(1995, 1, 1), hire_date=date(2015, 1, 1))

        self.e6 = Employee(id=6, first_name="Scotty", last_name="Bomba", base_salary=1000,
                           birth_date=date(1977, 1, 1), hire_date=date(1998, 10, 10))

        self.em = EmployeeManager(self.rm)

    def test_calculate_salary_non_leader(self):
        salary = self.em.calculate_salary(self.e6)
        self.assertEqual(salary, 3600)

    def test_calculate_salary_team_leader(self):
        salary = self.em.calculate_salary(self.e1)
        self.assertEqual(salary, 4200)

    @patch('employee_manager.EmployeeManager.calculate_salary_and_send_email')
    def test_email_notification(self, mock_calculate_salary_and_send_email):
        self.em.calculate_salary_and_send_email(self.e1)
        mock_calculate_salary_and_send_email.assert_called_once_with(self.e1)


if __name__ == '__main__':
    unittest.main()
