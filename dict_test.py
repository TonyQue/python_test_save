d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85,
    '88': 'aaaaa',
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
print(d['88'])