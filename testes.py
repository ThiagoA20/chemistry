import unittest
from mass import molecular_mass


class MassaTest(unittest.TestCase):

    def test_massa(self):
        molecula_test = molecular_mass("2H2SO4")
        self.assertEqual(molecula_test.fm, "H2SO4")
        self.assertEqual(molecula_test.mm, 98)
        self.assertEqual(molecula_test.qm, 2)
        self.assertEqual(molecula_test.atoms, ['H', 'S', 'O'])
        self.assertEqual(molecula_test.mc, 196)


if __name__ == '__main__':
    unittest.main()
