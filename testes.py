import unittest
from massa import massa_molecular


class MassaTest(unittest.TestCase):

    def test_massa(self):
        molecula_test = massa_molecular("2H2SO4")
        self.assertEqual(molecula_test.fm, "H2SO4")
        self.assertEqual(molecula_test.mm, 98)
        self.assertEqual(molecula_test.qm, 2)
        self.assertEqual(molecula_test.atomos, ['H', 'S', 'O'])
        self.assertEqual(molecula_test.mc, 196)


if __name__ == '__main__':
    unittest.main()
