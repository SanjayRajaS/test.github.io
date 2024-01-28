from datetime import datetime as D

def temporal_remainder(target):
  now = D.now()
  Target = D.strptime(target,"%Y-%m-%d %H:%M:%S.%f")
  diff = Target-now
  return diff #f'{now}\n{target}\n\n{diff}'

t = '2024-02-03 00:01:00.0'
print(temporal_remainder(t))
