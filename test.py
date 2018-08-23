import hug
from falcon import HTTP_200

import app


response = hug.test.call('POST', app, 'csv/sort', body={
    'content': 'B\t2\t4\t1\n \t1\t1\n1\t2\t3\nA\t2\t3'
})

assert response.status == HTTP_200
assert response.data == {'result': ' \t1\t1\t\n1\t2\t3\t\nA\t2\t3\t\nB\t2\t4\t1.0\n'}
