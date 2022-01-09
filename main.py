import number_to_pair
import pair_to_number

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

if __name__ == '__main__':
  number_to_pair.test_number_to_pair(4, 'White', 'Brown')
  number_to_pair.test_number_to_pair(5, 'White', 'Slate')
  pair_to_number.test_pair_to_number('Black', 'Orange', 12)
  pair_to_number.test_pair_to_number('Violet', 'Slate', 25)
  pair_to_number.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
