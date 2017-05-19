special_code = (
    '110000',
    '120000',
    '310000',
    '500000',
    '810000',
    '820000'
)
special_code_prefix = (
    '11',
    '12',
    '31',
    '50',
    '81',
    '82'
)


d = []
last_province = {}
last_city = {}

with open('list.json', 'r') as wf:
    line = wf.readline()
    while line:
        try:
            k, v = line.split(":")
            k = k[1: -1]
            v = v[1:-3]
        except Exception as e:
            line = wf.readline()
            continue

        if k.endswith('0000'):
            if last_province:
                d.append(last_province)
            last_province = {
                'label': v,
                'value': v,
                'code': k,
                'children': []
            }
        else:

            if k[0:2] not in special_code_prefix:
                if k.endswith('00'):
                    if last_city:
                        last_province['children'].append(last_city)
                    last_city = {
                        'label': v,
                        'value': v,
                        'code': k,
                        'children': []
                    }
                else:
                    last_region = {
                        'label': v,
                        'value': v,
                        'code': k
                    }
                    last_city['children'].append(last_region)
            else:
                if last_city:
                    last_province['children'].append(last_city)
                last_city = {
                    'label': v,
                    'value': v,
                    'code': k
                }
        line = wf.readline()

with open('addressData.min.js', 'w+') as f:
    f.write("export const addressData=" + str(d).replace("\'", "\""))
