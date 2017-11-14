def newStyleFormatting(s):
   a= '%'.join([re.sub(r'%[bcxdefsgnof]','{}',S) for S in s.split('%%')])
   return a
