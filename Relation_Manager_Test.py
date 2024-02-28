import unittest
from datetime import date
from relations_manager import RelationsManager
from employee import Employee

class TestRelationsManager(unittest.TestCase):
    def setUp(self):
        self.manager = RelationsManager()

    def test_team_leader_john_doe(self):
        john_doe = [employee for employee in self.manager.get_all_employees() if employee.first_name == "John" and employee.last_name == "Doe"][0]
        self.assertEqual(john_doe.birth_date, date(1970, 1, 31))

    def test_team_members_of_john_doe(self):
        john_doe = [employee for employee in self.manager.get_all_employees() if employee.first_name == "John" and employee.last_name == "Doe"][0]
        team_members = self.manager.get_team_members(john_doe)
        expected_members = [2, 3]
        self.assertEqual(team_members, expected_members)

    def test_tomas_andre_not_team_member_of_john_doe(self):
        john_doe = [employee for employee in self.manager.get_all_employees() if employee.first_name == "John" and employee.last_name == "Doe"][0]
        team_members = self.manager.get_team_members(john_doe)
        self.assertNotIn(5, team_members)  # Tomas Andre's ID is 5

    def test_gretchen_walford_base_salary(self):
        gretchen_walford = [employee for employee in self.manager.get_all_employees() if employee.first_name == "Gretchen" and employee.last_name == "Watford"][0]
        self.assertEqual(gretchen_walford.base_salary, 4000)

    def test_tomas_andre_not_team_leader(self):
        tomas_andre = [employee for employee in self.manager.get_all_employees() if employee.first_name == "Tomas" and employee.last_name == "Andre"][0]
        self.assertFalse(self.manager.is_leader(tomas_andre))

    def test_retrieve_team_members_of_tomas_andre(self):
        tomas_andre = [employee for employee in self.manager.get_all_employees() if
                       employee.first_name == "Tomas" and employee.last_name == "Andre"][0]
        with self.assertRaises(KeyError):
            self.manager.get_team_members(tomas_andre)

    def test_jude_overcash_not_in_database(self):
        jude_overcash = Employee(id=7, first_name="Jude", last_name="Overcash", base_salary=2000,
                                 birth_date=date(1985, 1, 1), hire_date=date(2010, 1, 1))
        self.assertNotIn(jude_overcash, self.manager.get_all_employees())

if __name__ == '__main__':
    unittest.main()
