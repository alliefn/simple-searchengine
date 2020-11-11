def readinput(content):
  content_list = content.split()
  counts = dict()
  for i in content_list:
    counts[i] = counts.get(i, 0) + 1
  data.append(counts)
  return "<h1>data: {}</h1>".format(data)