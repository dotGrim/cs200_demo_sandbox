import main
import pytest





@pytest.mark.parametrize(
	('input_x', 'input_y', 'expected'),
	(
		(0, 0, 1),
		(1, 0, 1),
		(2, 1, 3),
		(3, 5, 16)
	)
)



def test_foo(input_x, input_y, expected):
	assert main.foo(input_x, input_y) == expected


@pytest.mark.parametrize(("a", "b", "result"), [(3, 2, 12), (3, 0, 3)])
def test_bar(a, b, result):
	assert main.bar(a, b) == result