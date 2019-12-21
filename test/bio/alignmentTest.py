import unittest

from bio.alignment import *

class AlignmentTest(unittest.TestCase):
    def test_alignment1(self):
        seq1 = "GATTA"
        seq2 = "GCTAC"
        global_alignment = Alignment(seq1, seq2, AlignmentMethod.NEEDLE)
        global_alignment.set_params(gap_penalty=-2, match_award=3, mismatch_penalty=-1)
        global_alignment.set_method(AlignmentMethod.NEEDLE)
        global_alignment.fill_matrix()
        res1, res2 = global_alignment.backtracking()
        self.assertEqual(global_alignment.get_score(), 4)
        self.assertEqual(res1, "GATTA-")
        self.assertEqual(res2, "G-CTAC")

    def test_alignment2(self):
        seq1 = ("CACGTTTCTTGTGGCAGCTTAAGTTTGAATGTCATTTCTTCAATGGGACGGA"
                    "GCGGGTGCGGTTGCTGGAAAGATGCATCTATAACCAAGAGGAGTCCGTGCGCTTCGACAGC"
                    "GACGTGGGGGAGTACCGGGCGGTGACGGAGCTGGGGCGGCCTGATGCCGAGTACTGGAACA"
                    "GCCAGAAGGACCTCCTGGAGCAGAGGCGGGCCGCGGTGGACACCTACTGCAGACACAACTA"
                    "CGGGGTTGGTGAGAGCTTCACAGTGCAGCGGCGAG")

        seq2 = ("ACGAGTGCGTGTTTTCCCGCCTGGTCCCCAGGCCCCCTTTCCGTCCTCAGGAA"
                    "GACAGAGGAGGAGCCCCTCGGGCTGCAGGTGGTGGGCGTTGCGGCGGCGGCCGGTTAAGGT"
                    "TCCCAGTGCCCGCACCCGGCCCACGGGAGCCCCGGACTGGCGGCGTCACTGTCAGTGTCTT"
                    "CTCAGGAGGCCGCCTGTGTGACTGGATCGTTCGTGTCCCCACAGCACGTTTCTTGGAGTAC"
                    "TCTACGTCTGAGTGTCATTTCTTCAATGGGACGGAGCGGGTGCGGTTCCTGGACAGATACT"
                    "TCCATAACCAGGAGGAGAACGTGCGCTTCGACAGCGACGTGGGGGAGTTCCGGGCGGTGAC"
                    "GGAGCTGGGGCGGCCTGATGCCGAGTACTGGAACAGCCAGAAGGACATCCTGGAAGACGAG"
                    "CGGGCCGCGGTGGACACCTACTGCAGACACAACTACGGGGTTGTGAGAGCTTCACCGTGCA"
                    "GCGGCGAGACGCACTCGT")
        global_alignment = Alignment(seq1, seq2, AlignmentMethod.NEEDLE)
        global_alignment.set_params(gap_penalty=-5, match_award=3, mismatch_penalty=-2)
        global_alignment.set_method(AlignmentMethod.NEEDLE)
        global_alignment.fill_matrix()
        res1, res2 = global_alignment.backtracking()


