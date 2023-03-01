import re
txt = 'nernnero imerimer,ofnrmer.wpomermpr'
x = re.sub('[ .,]', ';', txt, 4)
print(x)