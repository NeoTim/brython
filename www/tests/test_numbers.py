# numbers
x = 1
assert x.__class__ == int
assert isinstance(x, int)
assert str(x) == "1"

assert 2 + 2 == 4
assert (50 - 5 * 6) / 4 == 5.0
assert 8 / 5 == 1.6
assert 7 // 3 == 2
assert 7 // -3 == -3
width = 20
height = 5 * 9
assert width * height == 900
x = y = z = 0
assert x == 0
assert y == 0
assert z == 0

assert 3 * 3.75 / 1.5 == 7.5
assert 7.0 / 2 == 3.5

y = 3.14
assert y.__class__ == float
assert isinstance(3.14, float)
assert str(y) == "3.14"

x = -3
assert x.__abs__() == 3
assert -x.__abs__() == -3

assert x.__ceil__() == x
assert x.__ceil__() == -3

assert x.__divmod__(2) == (-2, 1)


#issue 98
assert int.from_bytes(b'\xfc', 'big') == 252
assert int.from_bytes(bytearray([252, 0]), 'big') == 64512
assert int.from_bytes(b'\x00\x10', byteorder='big') == 16
assert int.from_bytes(b'\x00\x10', byteorder='little') == 4096
assert int.from_bytes(b'\xfc\x00', byteorder='big', signed=True) == -1024
assert int.from_bytes(b'\xfc\x00', byteorder='big', signed=False) == 64512
assert int.from_bytes([255, 0, 0], byteorder='big') == 16711680

# issue 115
a = 1
assert a.numerator == 1
assert a.denominator == 1
assert a.real == 1
assert a.imag == 0
assert isinstance(a.imag, int) == True
a = 1 + 2j
assert a.real == 1
assert a.imag == 2
assert isinstance(a.real, float) == True
assert isinstance(a.imag, float) == True

# True and False are instances of int
assert isinstance(True, int)
assert isinstance(False, int)

# issue 294
assert int.from_bytes(bytes=b'some_bytes',byteorder='big') == \
    545127616933790290830707

# issue 350
a = float("-inf")
b = float("-infinity")
assert a == b
assert repr(a) == '-inf'
assert a * 1. == b
assert a * 1 == b

# issue 352
a = float("inf")
assert a * 1 == a

# complex numbers
x = 8j
y = 8.3j
z = 3.2e6j
a = 4 + 2j
b = 2 - 3j
c = 3.0 - 3j

assert a * b == 14 - 8j
assert x * x == -64
assert x - 7j == 1j
assert -7j + x == 1j
assert x - 2.0j == 6j
assert 1 / a == 0.2 - 0.1j
assert 2.0 / a == 0.4 - 0.2j
assert 1 + a == 5 + 2j
assert 2 - a == -2 -2j
assert 3 * a == 12 + 6j
assert 1.0 + a == 5 + 2j
assert 2.0 - a == -2 -2j
assert 3.0 * a == 12 + 6j
assert abs(3 + 4j) == 5
assert abs(4 + 3j) == 5.0
assert abs(4 + 3j) == abs(3 + 4j)

# issue 498
assert (1 + 2j) * 2.4 == 2.4 + 4.8j

assert hash(1.0) == 1

r = 0
t = 0.5
assert int(r + t)==0
assert int(r + 0.5)==0

# long integers
import math

assert 10 ** 50 / math.pi == 3.183098861837907e+49
assert 10 ** 50 // math.pi == 3.183098861837907e+49
assert 10 ** 50 / 2 == 5e+49
assert 10 ** 50 // 2 == 50000000000000000000000000000000000000000000000000

assert 54545400516506505640987 ** 54 == 6094516993408491992717058206554386213417915204282550520580173630741479188519340788843629287628151801401531280484190484808107809271896207848468766316369387868615942195705186609725632301540802654841087447819153660908915523083623229576696678140304820900222252911769804932640891926749203064507743998679197424915190740760487839030635635524983269458329073226234934906817084587829534314798088951835646661008306240083129624656185367771063790241091117474534590020274074136357197645935060221291548216756250807752871656640000397916793935066325678308875294763565871249294663947951463338441414225943925113720065959282539207445752286988465907078586737338772584087046523710599804501329581165543748980030118117212198624410981372454011696164126682234324920269752028023856536950012015786770231258409600204108521358592401364755168512993999226284880314977761963287301136818231324076353404996749453313086116069644242663548622522635961543805984510834241759298667823778964361782775453343709473315538820123572991073589042203709526463926126985507611602224263739126014633222508048003050310698628707258846954246136227525382040513707929524854001570426683736205561486053982749877898481108145486760466316963709172336931026901114323426213180770145849112343689

assert int('100000000000000000000000000000000', 2) == 4294967296
assert int('102002022201221111211', 3) == 4294967296
assert int('10000000000000000', 4) == 4294967296
assert int('32244002423141', 5) == 4294967296
assert int('1550104015504', 6) == 4294967296
assert int('211301422354', 7) == 4294967296
assert int('40000000000', 8) == 4294967296
assert int('12068657454', 9) == 4294967296
assert int('4294967296', 10) == 4294967296
assert int('1904440554', 11) == 4294967296
assert int('9ba461594', 12) == 4294967296
assert int('535a79889', 13) == 4294967296
assert int('2ca5b7464', 14) == 4294967296
assert int('1a20dcd81', 15) == 4294967296
assert int('100000000', 16) == 4294967296
assert int('a7ffda91', 17) == 4294967296
assert int('704he7g4', 18) == 4294967296
assert int('4f5aff66', 19) == 4294967296
assert int('3723ai4g', 20) == 4294967296
assert int('281d55i4', 21) == 4294967296
assert int('1fj8b184', 22) == 4294967296
assert int('1606k7ic', 23) == 4294967296
assert int('mb994ag', 24) == 4294967296
assert int('hek2mgl', 25) == 4294967296
assert int('dnchbnm', 26) == 4294967296
assert int('b28jpdm', 27) == 4294967296
assert int('8pfgih4', 28) == 4294967296
assert int('76beigg', 29) == 4294967296
assert int('5qmcpqg', 30) == 4294967296
assert int('4q0jto4', 31) == 4294967296
assert int('4000000', 32) == 4294967296
assert int('3aokq94', 33) == 4294967296
assert int('2qhxjli', 34) == 4294967296
assert int('2br45qb', 35) == 4294967296
assert int('1z141z4', 36) == 4294967296

a = 2 ** 53 - 3
assert a + 10 == 9007199254740999
assert a + 11 == 9007199254741000

# float subclass
class Float(float):

    def __eq__(self, other):
        if not float.__eq__(self, other) and self.almost_equal(other):
            raise FloatCompError('you probably meant almost equal')
        return float.__eq__(self, other)

    def almost_equal(self, other):
        return abs(self - other) < 10 ** -8


class FloatCompError(Exception):
    pass


assert str(Float(0.3)) == "0.3"
assert Float(0.1) + Float(0.1) == Float(0.2)

float_sum = Float(0.1) + Float(0.1) + Float(0.1)
assert Float(0.3).almost_equal(float_sum)
try:
    Float(0.3) == float_sum
    raise Exception("should have raised FloatCompError")
except FloatCompError:
    pass

# issue 564
x = 2
assert isinstance(.5 * x, float)
assert isinstance(1.0 + x, float)
assert isinstance(3.0 - x, float)

# issue 749
assert float.__eq__(1.5, 1.5)
assert float.__eq__(1.0, 1)
assert not float.__eq__(1, 0)
assert int.__eq__(1, 1)
assert not int.__eq__(1, 0)

# issue 794
assert (-1024).to_bytes(2, "big", signed=True) == b'\xfc\x00'
assert (1024).to_bytes(2, "big") == b'\x04\x00'
assert (1024).to_bytes(2, "little") == b'\x00\x04'

# issue 840
x = 123 ** 20
y = 123 ** 20
assert (id(x) != id(y) or x is y)

# PEP 515
from tester import assertRaises

population = 65_345_123
assert population == 65345123

population = int("65_345_123")
assert population == 65345123

assertRaises(ValueError, int, "_12000")

amount = 10_000_000.0
assert amount == 10000000.0

addr = 0xCAFE_F00D
assert addr == 0xCAFEF00D

flags = 0b_0011_1111_0100_1110
assert flags == 0b0011111101001110

flags = int('0b_1111_0000', 2)
assert flags == 0b11110000

assert complex("8_7.6+2_67J") == (87.6 + 267j)
assertRaises(ValueError, complex, "_8_7.6+2_67J")
assertRaises(ValueError, complex, "8_7.6+_2_67J")

# issue 955
x = True

try:
    x.real = 2
    raise Exception("should have raised AttributeError")
except AttributeError as exc:
    assert "is not writable" in exc.args[0]

try:
    x.foo = "a"
    raise Exception("should have raised AttributeError")
except AttributeError as exc:
    assert "has no attribute 'foo'" in exc.args[0]

# issue 967
assert not (True == "Toggle")
assert True == True
assert True == 1
assert not (True == 8)
assert True == 1.0
assert not (True == 1.1)
assert not (False == "Toggle")
assert False == False
assert False == 0
assert False == 0.0
assert not (False == 8)

# issue 982
try:
    int("0x505")
    raise Exception("should have raised ValueError")
except ValueError:
    pass

# issue 1001
assert 1j / 1 == 1j
assert 1j / 1.0 == 1j

# issue 1033
from fractions import *
x = Fraction(1,1000000000000000)/10
assert str(x) == "1/10000000000000000"

# issue 1040
assert True + 2 == 3
assert False + 2 == 2
assert True * 3 == 3
assert False * 3 == 0
assert True / 2 == 0.5
assert False / 2 == 0
try:
    1 / False
    raise Exception("should have raised ZeroDivisionError")
except ZeroDivisionError:
    pass

# issue 1049
class Myfloat(float):
    pass

assert issubclass(Myfloat, float)

# issue 1092
assert (1024).to_bytes(4, byteorder='big') == b'\x00\x00\x04\x00'

# issue 1098
def test(x, pattern):
    assert x == pattern, f'''{x!r} != {pattern!r}'''

test( f'''{1.230e-1}''',     '0.123'   )
test( f'''{1.230e-11}''',    '1.23e-11')
test( f'''{1.230e-10}''',    '1.23e-10')
test( f'''{1.230e-3:8.6}''', ' 0.00123')
test( f'''{1.230e-3:1.6}''', '0.00123' )
test(f'''{1.23e-11:1.6}''', '1.23e-11')
test( f'''{1.23e-10:1.6}''', '1.23e-10')
test( f'''{1.23e-10:9.6}''',' 1.23e-10')
test(     f'''{1.23e-10:1.15}''', '1.23e-10')
test(1.23e-10.__format__('1.15'), '1.23e-10')

# issue 1115
class sffloat(float):
    def __new__(cls, value, sf=None):
        return super().__new__(cls, value)

    def __init__(self, value, sf=None):
        float.__init__(value)
        self.sf = sf

assert issubclass(sffloat, float)

a = sffloat(1.0,2)
b = sffloat(2.0,3)
assert isinstance(a, float)

assert a * b == 2.0
assert a.sf == 2
assert b.sf == 3

# issue 1156
try:
    isinstance(42, 43)
    raise Exception("should have raised TypeError")
except TypeError:
    pass

# issue 1211
assert .1j == .1j
assert .1j + 2 == 2 + 0.1j

# issue 1127
class A:

    def __rand__(self, other):
        return "A-rand"

    def __ror__(self, other):
        return "A-ror"

    def __rxor__(self, other):
        return "A-rxor"

assert False | A() == "A-ror"
assert True | A() == "A-ror"
assert False & A() == "A-rand"
assert True & A() == "A-rand"
assert False ^ A() == "A-rxor"
assert True ^ A() == "A-rxor"

# issue 1234
assert round(3.75, 1) == 3.8
assert round(3.65, 1) == 3.6
assert round(-3.75, 1) == -3.8
assert round(-3.65, 1) == -3.6
assert round(3.5) == 4
assert round(4.5) == 4

# issue 1245
assert eval("0j") == 0j

print('passed all tests...')
