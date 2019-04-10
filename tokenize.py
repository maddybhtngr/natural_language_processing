import nltk
texts = ["""The second question deals with relative performance. 
Although both types of benchmark provide answers, a system’s overall ranking can hinge on 
the type of application involved. The same machine can perform the best and the worst, so relying on simple 
numbers not only provides inaccurate answers, it can lead to the wrong conclusions about machine suitability and HPC 
technology in general. The strength of specialized kernel benchmarks is their ability to measure individual machine features 
by focusing on a particular system aspect. However, the results don’t answer the question of relative component importance—breaking 
down a real application’s execution time into computation, communication, and I/O, for example, shows each component’s true 
relative importance. We can’t get this type of information by combining each component’s individual kernel benchmarks. However, 
kernel metrics can answer the question of what percentage of peak performance the floating-point operations can achieve: such 
metrics are idealized bounds under a given code pattern. But these results don’t represent the percentage of peak performance 
a real application can achieve. """]
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        word = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(word)
        print(tagged_words)