import nltk
from nltk.stem import PorterStemmer
stemmerporter= PorterStemmer()
from nltk.stem import WordNetLemmatizer

example = """The Indian subcontinent was home to the urban Indus Valley Civilisation of the 3rd millennium BCE. 
In the following millennium, the oldest scriptures associated with Hinduism began to be composed. Social stratification, 
based on caste, emerged in the first millennium BCE, and Buddhism and Jainism arose. Early political consolidations 
took place under the Maurya and Gupta empires; later peninsular Middle Kingdoms influenced cultures as far as Southeast 
Asia. In the medieval era, Judaism, Zoroastrianism, Christianity, and Islam arrived, and Sikhism emerged, all adding 
to the region's diverse culture. Much of the north fell to the Delhi Sultanate; the south was united under the 
Vijayanagara Empire. The economy expanded in the 17th century in the Mughal Empire. In the mid-18th century, the 
subcontinent came under British East India Company rule, and in the mid-19th under British crown rule. A nationalist 
movement emerged in the late 19th century, which later, under Mahatma Gandhi, was noted for nonviolent resistance and 
led to India's independence in 1947."""
example=[stemmerporter.stem(token) for token in example.split(" ")]
print(" ".join(example))

print()

lemmatizer= WordNetLemmatizer()
example = """The Indian subcontinent was home to the urban Indus Valley Civilisation of the 3rd millennium BCE. 
In the following millennium, the oldest scriptures associated with Hinduism began to be composed. Social stratification, 
based on caste, emerged in the first millennium BCE, and Buddhism and Jainism arose. Early political consolidations 
took place under the Maurya and Gupta empires; later peninsular Middle Kingdoms influenced cultures as far as Southeast 
Asia. In the medieval era, Judaism, Zoroastrianism, Christianity, and Islam arrived, and Sikhism emerged, all adding 
to the region's diverse culture. Much of the north fell to the Delhi Sultanate; the south was united under the 
Vijayanagara Empire. The economy expanded in the 17th century in the Mughal Empire. In the mid-18th century, the 
subcontinent came under British East India Company rule, and in the mid-19th under British crown rule. A nationalist 
movement emerged in the late 19th century, which later, under Mahatma Gandhi, was noted for nonviolent resistance and 
led to India's independence in 1947."""
example=[lemmatizer.lemmatize(token) for token in example.split(" ")]
print(" ".join(example))