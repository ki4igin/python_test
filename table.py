import pandas as pd
import numpy as np
import unittest
from pympler import asizeof

# @formatter:off
GT_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['N', '0.01', '0.05'],
    data=[[3,    1.155,  1.155],
          [4,    1.496,  1.481],
          [5,    1.764,  1.715],
          [6,    1.973,  1.887],
          [7,    2.139,  2.020],
          [8,    2.274,  2.126],
          [9,    2.387,  2.215],
          [10,   2.482,  2.290],
          [11,   2.564,  2.355],
          [12,   2.636,  2.412],
          [13,   2.699,  2.462],
          [14,   2.755,  2.507],
          [15,   2.806,  2.549],
          [16,   2.852,  2.585],
          [17,   2.894,  2.620],
          [18,   2.932,  2.651],
          [19,   2.968,  2.681],
          [20,   3.001,  2.709],
          [21,   3.031,  2.733],
          [22,   3.060,  2.758],
          [23,   3.087,  2.781],
          [24,   3.112,  2.802],
          [25,   3.135,  2.822],
          [26,   3.157,  2.841],
          [27,   3.178,  2.859],
          [28,   3.199,  2.876],
          [29,   3.218,  2.893],
          [30,   3.236,  2.908],
          [31,   3.253,  2.924],
          [32,   3.270,  2.938],
          [33,   3.286,  2.952],
          [34,   3.301,  2.965],
          [36,   3.330,  2.991],
          [38,   3.356,  3.014],
          [40,   3.381,  3.036]])

T_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['N', '0.80', '0.90', '0.95', '0.98', '0.99', '0.995', '0.999'],
    data=[[4,    1.638,  2.353,  3.182,  4.541,  5.841,   7.453,   12.92],
          [5,    1.533,  2.132,  2.776,  3.747,  4.604,   5.598,   8.610],
          [6,    1.476,  2.015,  2.571,  3.365,  4.032,   4.773,   6.869],
          [7,    1.440,  1.943,  2.447,  3.143,  3.707,   4.317,   5.959],
          [8,    1.415,  1.895,  2.365,  2.998,  3.499,   4.029,   5.408],
          [9,    1.397,  1.860,  2.306,  2.896,  3.355,   3.833,   5.041],
          [10,   1.383,  1.833,  2.262,  2.821,  3.250,   3.690,   4.781],
          [11,   1.372,  1.812,  2.228,  2.764,  3.169,   3.581,   4.587],
          [12,   1.363,  1.796,  2.201,  2.718,  3.106,   3.497,   4.437],
          [13,   1.356,  1.782,  2.179,  2.681,  3.055,   3.428,   4.318],
          [14,   1.350,  1.771,  2.160,  2.650,  3.012,   3.372,   4.221],
          [15,   1.345,  1.761,  2.145,  2.624,  2.977,   3.326,   4.140],
          [16,   1.341,  1.753,  2.131,  2.602,  2.947,   3.286,   4.073],
          [17,   1.337,  1.746,  2.120,  2.583,  2.921,   3.252,   4.015],
          [18,   1.333,  1.740,  2.110,  2.567,  2.898,   3.222,   3.965],
          [19,   1.330,  1.734,  2.101,  2.552,  2.878,   3.197,   3.922],
          [20,   1.328,  1.729,  2.093,  2.539,  2.861,   3.174,   3.883],
          [21,   1.325,  1.725,  2.086,  2.528,  2.845,   3.153,   3.850],
          [22,   1.323,  1.721,  2.080,  2.518,  2.831,   3.135,   3.819],
          [23,   1.321,  1.717,  2.074,  2.508,  2.819,   3.119,   3.792],
          [24,   1.319,  1.714,  2.069,  2.500,  2.807,   3.104,   3.767],
          [25,   1.318,  1.711,  2.064,  2.492,  2.797,   3.091,   3.745],
          [26,   1.316,  1.708,  2.060,  2.485,  2.787,   3.078,   3.725],
          [27,   1.315,  1.706,  2.056,  2.479,  2.779,   3.067,   3.707],
          [28,   1.314,  1.703,  2.052,  2.473,  2.771,   3.057,   3.690],
          [29,   1.313,  1.701,  2.048,  2.467,  2.763,   3.047,   3.674],
          [30,   1.311,  1.699,  2.045,  2.462,  2.756,   3.038,   3.659],
          [31,   1.310,  1.697,  2.042,  2.457,  2.750,   3.030,   3.646],
          [40,   1.303,  1.684,  2.021,  2.423,  2.704,   2.971,   3.551],
          [50,   1.299,  1.676,  2.009,  2.403,  2.678,   2.937,   3.496],
          [60,   1.296,  1.671,  2.000,  2.390,  2.660,   2.915,   3.460],
          [80,   1.292,  1.664,  1.990,  2.374,  2.639,   2.887,   3.416],
          [100,  1.290,  1.660,  1.984,  2.364,  2.626,   2.871,   3.390],
          [120,  1.289,  1.658,  1.980,  2.358,  2.617,   2.860,   3.373],
          [150,  1.282,  1.645,  1.960,  2.326,  2.576,   2.807,   3.291]])

N_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['t/sqrt(n)', '0.50', '0.70', '0.90', '0.95', '0.99', '0.999'],
    data=[[1.0,              2,      3,      5,      7,     11,      17],
          [0.5,              3,      6,     13,     18,     31,      50],
          [0.4,              4,      8,     19,     27,     46,      74],
          [0.3,              6,     13,     32,     46,     78,     127],
          [0.2,             13,     29,     70,     99,    171,     277],
          [0.1,             47,    169,    273,     99,    171,     277],
          [0.05,           183,    431,   1084,   1540,   2659,    4338],
          [0.01,          4543,  10732,  27161,  38416,  66358,  108307]])

D_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['N', '0.95dmin', '0.95dmax', '0.99dmin', '0.99dmax'],
    data=[[16,      0.6829,     0.9137,     0.7236,     0.8884],
          [21,      0.6950,     0.9001,     0.7304,     0.8768],
          [26,      0.7040,     0.8901,     0.7360,     0.8686],
          [31,      0.7110,     0.8826,     0.7404,     0.8625],
          [36,      0.7167,     0.8769,     0.7440,     0.8578],
          [41,      0.7216,     0.8722,     0.7470,     0.8540],
          [46,      0.7256,     0.8682,     0.7496,     0.8508],
          [51,      0.7291,     0.8648,     0.7518,     0.8481]])

Z_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['N', 'm', '0.95', '0.99'],
    data=[[15,    1,   2.58,   2.33],
          [20,    1,   2.58,   2.33],
          [21,    2,   2.33,   2.06],
          [23,    2,   2.33,   2.06],
          [24,    2,   2.33,   2.17],
          [27,    2,   2.33,   2.17],
          [28,    2,   2.58,   2.33],
          [49,    2,   2.58,   2.33]])

K_THETA_TABLE = pd.DataFrame(
    dtype=float,
    columns=
          ['m', '0.50', '0.70', '0.90', '0.95', '0.99', '0.999'],
    data=[[2,   0.4141, 0.6395, 0.9668, 1.0976, 1.2721,  1.3673],
          [3,   0.4073, 0.6170, 0.9587, 1.1179, 1.3715,  1.5576],
          [4,   0.4026, 0.6139, 0.9529, 1.1190, 1.4086,  1.6536],
          [5,   0.3996, 0.6104, 0.9523, 1.1204, 1.4246,  1.7033]])
# @formatter:on


def find_in_table(table: pd.DataFrame, col: str, value: float, param: str) -> float:
    arr = np.array(table[col])
    idx = np.argmin(np.abs(arr - value))
    return table[param][idx]


def get_gt(n: int, q='0.01') -> float:
    return find_in_table(GT_TABLE, 'N', n, q)


def get_t(n: int, p='0.95') -> float:
    return find_in_table(T_TABLE, 'N', n, p)


def get_n(t_sqrt_n: float, p='0.95') -> float:
    return find_in_table(N_TABLE, 't/sqrt(n)', t_sqrt_n, p)


def get_d(n: int, p='0.95') -> tuple[float, float]:
    dmin = find_in_table(D_TABLE, 'N', n, p + 'dmin')
    dmax = find_in_table(D_TABLE, 'N', n, p + 'dmax')
    return dmin, dmax


def get_z(n: int, p='0.95') -> tuple[float, float]:
    m = find_in_table(Z_TABLE, 'N', n, 'm')
    z = find_in_table(Z_TABLE, 'N', n, p)
    return m, z


def get_k_theta(m: int, p='0.95') -> float:
    return find_in_table(K_THETA_TABLE, 'm', m, p)


class TestTable(unittest.TestCase):

    def test_get_gt(self):
        self.assertEqual(get_gt(35, '0.01'), 3.301)

    def test_get_t(self):
        self.assertEqual(get_t(45, '0.95'), 2.021)

    def test_get_n(self):
        self.assertEqual(get_n(0.05, '0.95'), 1540.0)

    def test_get_d(self):
        self.assertEqual(get_d(45, '0.95'), (0.7256, 0.8682))

    def test_get_z(self):
        self.assertEqual(get_z(45, '0.95'), (2, 2.58))

    def test_get_k_theta(self):
        self.assertEqual(get_k_theta(3, '0.95'), 1.1179)