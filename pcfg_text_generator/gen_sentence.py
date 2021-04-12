from pcfg import pcfg_rules
from cfg import cfg_rules
from nltk.parse.generate import generate, demo_grammar
print('from cfg' + '=' * 30)
for i in generate(cfg_rules, n=10, depth=5):
  print(' '.join(i))

print('from pcfg' + '=' * 30)
for i in generate(pcfg_rules, n=10, depth=5):
  print(' '.join(i))