def arithmetic_arranger(problems, count=False):
  firsts = ''
  seconds = ''
  sumx = ''
  lines = ''
  if len(problems) >= 6:
    return "Error: Too many problems."
  for problem in problems:
    x = problem.split()
    first = x[0]
    operator = x[1]
    second = x[2]
    if not first.isdigit() or not second.isdigit():
      return "Error: Numbers must only contain digits."
    if len(first) > 4 or len(second) > 4:
      return "Error: Numbers cannot be more than four digits."
    if operator == "+" or operator == '-':
      if operator == "+":
        sums = str(int(first) + int(second))
      else:
        sums = str(int(first) - int(second))
      length = max(len(first), len(second)) + 2
      top = str(first).rjust(length)
      bottom = operator + str(second).rjust(length - 1)
      line = ''
      result = str(sums).rjust(length)
      for s in range(length):
        line += '-'

      if problem != problems[-1]:
        firsts += top + '    '
        seconds += bottom + '    '
        lines += line + '    '
        sumx += result + '    '
      else:
        firsts += top
        seconds += bottom
        lines += line
        sumx += result
    else:
      return "Error: Operator must be '+' or '-'."
  firsts.rstrip()
  seconds.rstrip()
  lines.rstrip()
  if count:
    sumx.rstrip()
    arranged_problems = firsts + '\n' + seconds + '\n' + lines + '\n' + sumx
  else:
    arranged_problems = firsts + '\n' + seconds + '\n' + lines
  return arranged_problems  
    
  
  