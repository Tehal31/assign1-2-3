
def string_from_both_ends(string):
  if len(string) < 2:
    return 'empty string'

  return string[0:2] + string[-2:]

print(string_from_both_ends('w3resource'))
print(string_from_both_ends('w'))