from trump_clinton_calls import TrumpClintonMediaPresence
import unittest
import logging

logging.basicConfig(filename="sample.log", level=logging.DEBUG)
logging.debug('This is a debug message')


class TrumpClintonMediaPresenceTest(unittest.TestCase):

    def test_sentences(self):
        a = TrumpClintonMediaPresence()
        a.clump_sentences()
        assert a.mc is not None
#
    def test_words(self):
        a = TrumpClintonMediaPresence()
        a.clump_words()
        assert a.mc is not None

if __name__ == "__main__":
    unittest.main()
