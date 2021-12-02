
from datetime import datetime
start = datetime(1996,02,26)
end = datetime(2018,04,04)
diff = (end.year - start.year) * 12 + (end.month  - start.month )
print('Difference between dates in months:')
print(diff)