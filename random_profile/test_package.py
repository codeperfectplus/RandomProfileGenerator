import unittest

from random_profile import RandomProfile
random_profile = RandomProfile(num=1)


class RandomProfileTest(unittest.TestCase):
    def test_faname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).first_name()), 10)

    def test_lname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).last_name()), 10)

    def test_full_name_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_name()), 10)

    def test_full_profile(self):
        self.assertEqual(len(random_profile.full_profile()), 1)

    def test_full_profile_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_profile()), 10)

    def test_ipv4(self):
        self.assertEqual(len(random_profile.ipv4()), 1)

    def test_ipv4_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).ipv4()), 10)

    def test_job_title(self):
        self.assertEqual(len(random_profile.job_title()), 1)

    def test_job_title_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).job_title()), 10)


if __name__ == "__main__":
    unittest.main()
