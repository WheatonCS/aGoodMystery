
library(stylo) 

# stylo in R:  Bootstrap Concensus Tree (BCT)

# load texts
raw.corpus <- load.corpus(files = list.files(), corpus.dir = "oneEachText", encoding = "UTF-8")

# tokenize
tokenized.corpus <- txt.to.words.ext(raw.corpus, language = "English.all", preserve.case = FALSE)
frequent.features <- make.frequency.list(tokenized.corpus, head = 1000)
freqs <- make.table.of.frequencies(tokenized.corpus, features = frequent.features)

# cull (or not)
# culled.freqs <- perform.culling(freqs, culling.level = 50)

# BCT
stylo(frequencies = freqs, analysis.type = "BCT", mfw.min = 100, mfw.max = 1000, increment=50, custom.graph.title = "Poe et al.", write.png.file = TRUE, gui = FALSE)