from datetime import date


actual = list(map(int, input().split()))
expected = list(map(int, input().split()))

actual = date(day=actual[0], month=actual[1], year=actual[2])
expected = date(day=expected[0], month=expected[1], year=expected[2])

years_late = actual.year - expected.year
months_late = actual.month - expected.month
days_late = actual.day - expected.day

bill = 0
if actual > expected:
    
    if years_late:
        bill = 10000
    elif months_late:
        bill = 500 * months_late
    else: 
        bill = 15 * days_late
        
print(bill)
