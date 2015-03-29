import time

from nomenklatura.query.parser import QueryNode
from nomenklatura.query.builder import QueryBuilder


def execute_query(dataset, q):
    qb = QueryBuilder(dataset, None, QueryNode(None, None, q))
    t = time.time()
    result = qb.query()
    duration = (time.time() - t) * 1000
    return {
        'status': 'ok',
        'query': qb.node.to_dict(),
        'result': result,
        'time': duration
    }