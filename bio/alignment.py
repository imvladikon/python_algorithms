import numpy as np
import tabulate
from IPython.core.display import HTML
from enum import Enum


class AlignmentMethod(Enum):
    NEEDLE = 1,  # global
    LOCAL = 2 # local


class Alignment(object):
    seq1 = ""
    seq2 = ""
    matrix = None
    gap_penalty = 0
    match_award = 0
    mismatch_penalty = 0
    method = AlignmentMethod.NEEDLE

    def __init__(self, seq1, seq2, method=AlignmentMethod.NEEDLE):
        # self.gap_penalty = -2
        # self.match_award = 3
        # self.mismatch_penalty = -1
        self.seq1 = seq1
        self.seq2 = seq2
        self.method = method

    def set_method(self, value):
        self.method = value

    def set_params(self, gap_penalty, match_award, mismatch_penalty):
        self.set_mismatch_penalty(mismatch_penalty)
        self.set_gap_penalty(gap_penalty)
        self.set_match_award(match_award)

    def set_gap_penalty(self, value):
        self.gap_penalty = value

    def set_match_award(self, value):
        self.match_award = value

    def set_mismatch_penalty(self, value):
        self.mismatch_penalty = value

    def get_gap_penalty(self) -> int:
        return self.gap_penalty

    def get_match_award(self) -> int:
        return self.match_award

    def get_mismatch_penalty(self) -> int:
        return self.mismatch_penalty

    def get_score(self) -> int:
        if self.method.value == AlignmentMethod.LOCAL.value:
            i, j = np.unravel_index(self.matrix.argmax(), self.matrix.shape)
            return self.matrix[i, j]
        return self.matrix[-1, -1]

    def init_matrix(self):
        num_rows = len(self.seq1) + 1
        num_cols = len(self.seq2) + 1
        self.matrix = np.zeros(shape=(num_rows, num_cols), dtype=np.int)
        if self.method == AlignmentMethod.NEEDLE:
            self.matrix[0, :] = np.arange(0, num_cols * self.gap_penalty, self.gap_penalty)
            self.matrix[:, 0] = np.arange(0, num_rows * self.gap_penalty, self.gap_penalty)
        else:
            self.matrix[0, :] = 0
            self.matrix[:, 0] = 0

    def match_score(self, char1, char2) -> int:
        if char1 == char2:
            return self.match_award
        elif char1 == '-' or char2 == '-':
            return self.gap_penalty
        else:
            return self.mismatch_penalty

    def fill_matrix(self):
        self.init_matrix()
        for row, char1 in enumerate(self.seq1):
            for col, char2 in enumerate(self.seq2):
                match = self.matrix[row][col] + self.match_score(char1, char2)
                delete = self.matrix[row][col + 1] + self.match_score(char1, '-')
                insert = self.matrix[row + 1][col] + self.match_score('-', char2)
                if self.method == AlignmentMethod.NEEDLE:
                    self.matrix[row + 1][col + 1] = max(match, delete, insert)
                else:
                    self.matrix[row + 1][col + 1] = max(match, delete, insert, 0)

    def show_matrix(self):
        # pandas.DataFrame(self.matrix, list(self.seq1), list(self.seq2))
        return HTML(Alignment.show(self.seq2, self.seq1, self.matrix))

    def backtracking(self):
        alignment1 = ""
        alignment2 = ""
        m = len(self.seq1)
        n = len(self.seq2)
        while m > 0 and n > 0:
            score_current = self.matrix[m][n]
            score_diag = self.matrix[m - 1][n - 1]
            score_left = self.matrix[m][n - 1]
            score_up = self.matrix[m - 1][n]
            char1 = self.seq1[m - 1]
            char2 = self.seq2[n - 1]
            if score_current == score_diag + self.match_score(char1, char2):
                m, n = m - 1, n - 1
            elif score_current == score_up + self.match_score(char1, "-"):
                char2 = "-"
                m -= 1
            elif score_current == score_left + self.match_score("-", char2):
                char1 = "-"
                n -= 1
            alignment1 = char1 + alignment1
            alignment2 = char2 + alignment2
        return alignment1, alignment2

    def show(h_sequence, v_sequence, data, hide_zeros=False, nonzero_val=None):
        rows = []
        col_headers = [c for c in list(h_sequence)]
        row_headers = [c for c in list(v_sequence)]
        pad_headers = data.shape == (len(row_headers) + 1, len(col_headers) + 1)
        if pad_headers:
            row_headers = [" "] + row_headers
            col_headers = [" "] + col_headers
        for h, d in zip(row_headers, data):
            current_row = ["<b>%s</b>" % h]
            for e in d:
                if e == 0:
                    if hide_zeros:
                        current_row.append('')
                    else:
                        current_row.append(0)
                else:
                    if nonzero_val is not None:
                        current_row.append(nonzero_val)
                    else:
                        current_row.append(e)
            rows.append(current_row)
        return tabulate.tabulate(rows, headers=col_headers, tablefmt='html')
