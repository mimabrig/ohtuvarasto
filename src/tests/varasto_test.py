import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, 10)


    def test_otetaan_liikaa(self):
        otettu_maara = self.varasto.ota_varastosta(400)

        self.assertAlmostEqual(otettu_maara, 10)

    def test_liikaa_otettu_saldo_nolla(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otetaan_negatiivinen_maara(self):
        otetaan_negatiivinen = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(otetaan_negatiivinen, 0)




class TestNegatiivinenVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10)

    def test_negatiivisella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

class TestNegatiivinenSaldo(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, -5)

    def test_negatiivinen_saldo_alustuksessa(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestLiianIsoSaldo(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, 20)

    def test_liian_iso_saldo_alustuksessa(self):
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_stringify(self):
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")