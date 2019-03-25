import nltk
Base = [('2013000 16010000','Alimentos'),
('22029900 22021000','Bebidas'),
('19059020 19041000 19059090 19053100 19053200','Biscoitos'),
('34022000 18063210 17049020','Doces e salgados'),
('8061000','Frutas'),
('3051000 33043000 33072010 33059000 96190000 33061000 38099190','Higiene'),
('4031000 040510000 4061090','Leite e derivados'),
('34011190','Limpeza'),
('19023000 19021900 19059010','Massas')]

# tokenize método de quebra de frases
#num = nltk.tokenize.sent_tokenize(Base)

# cada palavra e considerado com um token
#tokens = nltk.word_tokenize(Base)

# Divide as palavras em classes
#classes = nltk.pos_tag(tokens)

# método de detecção de entidades só funciona com palavras
# entidades = nltk.chunk.ne_chunk(num)...

print(Base[0])