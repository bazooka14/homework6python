# Файл с visit logs был пуст (в нем было только "ПРИВЕТ!")
# поэтому я предположил каким он должен был быть и написал программу

with open('6_visit_log.csv', 'r') as logs, open('funnel.csv', 'w') as fun:
    while True:
        line = logs.readline()
        if not line:
            break
        
        log = line.strip().split(',')
        if log[1] and log[2]:
            fun.write(','.join(log) + '\n')
        